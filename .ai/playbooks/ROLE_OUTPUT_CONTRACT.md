# Role Output Contract Playbook

This playbook defines the handoff contract between AI roles.

It is stable guidance, not project state.

---

## Principle

Role separation is not enough.

Each role must produce output that can be used directly as input for the next role.

A role output must reduce ambiguity for the next model or next pass by transferring:

- evidence;
- risk;
- files read;
- files still needed;
- constraints;
- unknowns;
- what must not be done;
- the exact prompt for the next role.

If a role cannot safely recommend a next role, it must say why and escalate instead of guessing.

---

## Contract Requirements

Every non-trivial role output should include these packets.

For L0/L1 work, the packet may be compact.

For L2/L3/L4 work, the packet should be explicit.

### Evidence Packet

Must separate:

- `PROVEN`
- `EXPECTED`
- `ASSUMED`
- `UNKNOWN`

Rules:

- Do not convert assumptions into facts.
- Do not treat prior AI output, memory, summaries, or handoffs as source authority.
- Do not claim runtime behavior, deployment status, test success, security correctness, privacy correctness, or production readiness without evidence.

### Risk Packet

Must include:

- risk level;
- why this risk level applies;
- risk triggers;
- escalation status;
- human decisions needed.

Risk levels:

- `L0 Trivial`
- `L1 Low`
- `L2 Moderate`
- `L3 High`
- `L4 Critical`

When uncertain, choose the higher risk level.

### Files Packet

Must include:

- files read in this session;
- files not read but needed;
- files the next role must read before acting;
- whether file access was direct or based on pasted excerpts.

Repository access mode must be one of:

- `Direct tool access`
- `Pasted excerpts only`
- `No file access`
- `Unknown`

Unread files must remain `UNKNOWN`.

### Role-Specific Output Packet

Each role must produce only the artifact allowed for that role.

- Architect produces planning, sequencing, risks, options, and the next reading prompt.
- Reader produces evidence mapping and the next execution or planning prompt.
- Executor produces exact patch instructions and the next verification prompt.
- Verifier produces findings, verification status, gaps, and the next correction or handoff prompt.
- Handoff Scribe produces an accurate handoff and the next session prompt.
- Operator is human-only. AI may prepare decision packets or checklists for the human Operator, but must not become Operator.

### Next-Role Prompt Packet

Every role output must include a prompt for the next role unless the correct next step is escalation or human-only operation.

The prompt must be directly usable by another AI model.

It must include:

- next role;
- task;
- repository access mode;
- files already read;
- files the next role must read before acting;
- evidence from the previous role;
- risk level;
- constraints;
- what not to do;
- exact required output format.

---

## Standard Role Output Envelope

Use this envelope as the default shape.

Prompts may adapt it, but must preserve the same information.

```md
## Role Output

### Role
-

### Task
-

### Risk Level
-

### Repository Access Mode
- Direct tool access / Pasted excerpts only / No file access / Unknown

### Files Read
-

### Files Not Read But Needed
-

### Evidence Status

#### PROVEN
-

#### EXPECTED
-

#### ASSUMED
-

#### UNKNOWN
-

### Constraints
-

### What I Must Not Do
-

### Output Produced
-

### Verification Needed
-

### Escalation Needed?
-

### Next Role Recommendation
-

### Prompt For Next Role

```text
Role: [Next Role]

Task:
[...]

Repository access:
[...]

Files already read:
[...]

Files you must read before acting:
[...]

Evidence from previous role:
[...]

Risk level:
[...]

Constraints:
[...]

Do not:
[...]

Required output:
[exact required output format]
```

---

## Role-Specific Next Prompts

### Architect to Reader

Architect should usually hand off to Reader.

The Architect must not write executable patches.

The next prompt should tell Reader:

- what files or areas are likely relevant;
- what evidence is needed before implementation;
- what risk traps to check;
- what must not be patched yet.

### Reader to Executor

Reader may hand off to Executor only if enough evidence was gathered for a safe patch.

The next prompt should tell Executor:

- files already read;
- files Executor may edit;
- exact scope;
- evidence supporting the change;
- unknowns that must not be overclaimed;
- patch format requirements.

If evidence is insufficient, Reader should hand off to Architect or escalate.

### Executor to Verifier

Executor must hand off to Verifier.

The next prompt should tell Verifier:

- patch category;
- files read;
- exact patch proposed;
- evidence used;
- expected side effects;
- what the patch proves;
- what it does not prove;
- verification needed;
- rollback notes.

Executor must not self-approve.

### Verifier to Executor or Handoff Scribe

Verifier should hand off based on findings.

If changes are needed, the next prompt should go to Executor and include:

- findings;
- severity;
- exact evidence;
- required correction scope;
- what must not be broadened.

If the patch is acceptable within reviewed scope, the next prompt may go to Handoff Scribe and include:

- verified scope;
- unverified scope;
- remaining unknowns;
- human decisions required.

Verifier must not claim readiness beyond the evidence reviewed.

### Handoff Scribe to Next Session

Handoff Scribe should produce a next-session prompt.

The next prompt should tell the next model:

- that the handoff is not source authority;
- which files must be re-read;
- what was proven;
- what was assumed;
- what remains unknown;
- the safest next role;
- what not to do first.

---

## Operator Boundary

Operator is human-only.

AI must not switch into Operator.

AI may prepare:

- decision packet;
- checklist;
- dry-run plan;
- rollback checklist;
- read-only inspection plan;
- risk summary.

AI must not execute, authorize, or claim completion of:

- commits;
- merges;
- pushes;
- deployments;
- migrations;
- production operations;
- secrets rotation;
- destructive operations;
- payment or ledger changes.

If the next step is Operator-only, the `Next Role Recommendation` must say:

```text
Human Operator only
```

The `Prompt For Next Role` should be replaced with a human decision packet or checklist.

---

## Anti-Paralysis Rule

The contract must reduce false confidence without blocking safe progress.

If evidence is incomplete, the role should do one of:

1. request the exact missing files or excerpts;
2. recommend a Reader pass;
3. propose a smaller safe scope;
4. escalate if risk requires it.

Do not stop with vague caution.

Convert uncertainty into a clear next action.
