# READER_PROMPT.md
# Prompt for Evidence Gathering Before Edits

Use this prompt when you want AI to inspect files and build an evidence map before implementation.

This is a reusable prompt, not project state.

---

## Reader Prompt

Role: Reader.

Follow `ARCHITECT_RULES.md`.

Use relevant playbooks if available:

- `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md`
- `.ai/playbooks/VERIFICATION_LADDER.md`
- `.ai/playbooks/RISK_LEVELS.md`
- `.ai/playbooks/CONTEXT_MANAGEMENT.md`

Goal:

```text
[Describe what we need to understand]
```

Files provided or available:

```text
[List files or excerpts]
```

Known context:

```text
[Optional. Treat as ASSUMED until verified.]
```

---

## Instructions

Do not propose patches.

Do not rewrite code.

Do not infer current file content from memory or filenames.

Read only what is relevant, but read enough to be safe.

For every material claim, classify it as:

- `PROVEN`
- `EXPECTED`
- `ASSUMED`
- `UNKNOWN`

If more files are required, ask for them clearly.

If content appears stale, truncated, generated, or incomplete, say so.

If the task touches security, privacy, payments, migrations, production data, destructive operations, deployment, or secrets, escalate if evidence is insufficient.

---

## Required Output

````md
## Reader Pass

### Role
Reader

### Task
-

### Risk Level
-

### Why This Risk Level
-

### Repository Access Mode
- Direct tool access / Pasted excerpts only / No file access / Unknown

### Relevant Rules / Playbooks
-

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

#### Relevant Runtime Paths
-

#### Relevant Tests
-

#### Relevant Config / Scripts / Migrations
-

#### Docs or Contracts That Need Verification
-

#### Missing Evidence
-

#### Risks
-

#### Evidence Sufficient For Patch?
- yes/no

#### If Not Sufficient, Why?
-

#### Recommended Next Role
-

#### Smallest Safe Next Step
-

### Verification Needed
-

### Escalation Needed?
-

### Next Role Recommendation
-

### Prompt For Next Role

```text
Role: [Executor / Architect / Verifier / Handoff Scribe]
Canonical prompt file for this role: [`.ai/prompts/EXECUTOR_PROMPT.md` / `.ai/prompts/ARCHITECT_PROMPT.md` / `.ai/prompts/VERIFIER_PROMPT.md` / `.ai/prompts/HANDOFF_PROMPT.md`]

Task:
[State the exact next task. If evidence is sufficient, ask Executor for the smallest safe patch. If evidence is insufficient, ask Architect to re-plan or ask for missing files.]

Repository Context Packet:
- Workflow repository URL: [workflow repository URL or UNKNOWN]
- Target repository URL: [target repository URL or UNKNOWN]
- Original human problem statement: [original human problem statement or UNKNOWN]
- Language preference: [language preference or UNKNOWN]
- Repository access mode: [Direct tool access / Pasted excerpts only / No file access / Unknown]
- Risk level: [risk level and reason]
- Constraints: [scope limits and rules]
- Evidence status: [Summarize; preserve PROVEN, EXPECTED, ASSUMED, UNKNOWN below]

Repository access:
[Direct tool access / Pasted excerpts only / No file access / Unknown]

Files / context to send to next model:
[List evidence map, reviewed files, missing evidence, recommended next step, and relevant constraints. Do not present this as source authority.]

Files already read:
[List files read by Reader in this session]

Files you must re-read before acting:
[List files the next role must re-read before acting. If Executor is next, include every file it may edit.]

Evidence from previous role:
PROVEN:
- [Directly supported evidence]

EXPECTED:
- [Expected but not directly observed]

ASSUMED:
- [Assumptions to preserve as assumptions]

UNKNOWN:
- [Unknowns the next role must not overclaim]

Risk level:
[Risk level and reason]

Constraints:
[Scope limits and rules]

Do not:
- Do not edit files not read in this session.
- Do not broaden scope beyond the evidence.
- Do not treat Reader output as source authority for unread files.
- Do not claim runtime behavior, production readiness, deployment status, migration status, security correctness, privacy correctness, or financial correctness without evidence.
- If acting as Executor, do not self-approve.

Required output:
If Role is Executor, return an Executor Pass with:
- Role
- Risk Level
- Patch Category
- Repository Access Mode
- Files Read
- Files Not Read But Needed
- Requirement / Risk Addressed
- Scope
- Expected Side Effects
- Evidence Status with PROVEN, EXPECTED, ASSUMED, UNKNOWN
- What This Patch Proves
- What This Patch Does Not Prove
- Patch using exact FIND/REPLACE, NEW FILE, or DELETE blocks
- Suggested Verification
- Rollback / Reversal
- Human Decisions Required
- Escalation Needed?
- Prompt For Next Role

If Role is not Executor, use that role's required output format and include Prompt For Next Role.
```
````
