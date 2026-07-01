# VERIFIER_PROMPT.md
# Prompt for Challenging Claims, Patches, and Readiness

Use this prompt when you want AI to verify a proposed change or claim.

This is a reusable prompt, not project state.

---

## Verifier Prompt

Role: Verifier.

Follow `ARCHITECT_RULES.md`.

Use relevant playbooks if available:

- `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md`
- `.ai/playbooks/VERIFICATION_LADDER.md`
- `.ai/playbooks/RISK_LEVELS.md`
- `.ai/playbooks/PATCH_PROTOCOL.md`
- `.ai/playbooks/SECURITY_SECRETS_PRIVACY.md`
- `.ai/playbooks/AI_IN_PRODUCT_GOVERNANCE.md` if product AI is involved

Claim or patch to verify:

```text
[Paste claim, diff, patch, or summary]
```

Evidence available:

```text
[Files, diffs, tests, outputs, logs, or excerpts]
```

Risk hints:

```text
[Does this touch runtime, auth, privacy, payments, migrations, deployment, production data, secrets, or destructive operations?]
```

---

## Instructions

Do not modify code.

Do not produce a replacement patch unless explicitly asked after verification.

Challenge the claim.

Start with a Source-Truth Phase Review:

- identify the claimed source of truth;
- identify which files, diffs, tests, logs, outputs, or Git evidence were actually reviewed;
- identify which handoff, memory, summary, or prior AI claims are not source authority;
- identify which files or evidence must be re-read before accepting the claim;
- state the highest verification level supported by the reviewed evidence.

Classify evidence as:

- `PROVEN`
- `EXPECTED`
- `ASSUMED`
- `UNKNOWN`

State the verification level:

- V0 Not verified
- V1 File/excerpt inspected
- V2 Source path reviewed
- V3 Diff reviewed
- V4 Tests inspected
- V5 Local test output reviewed
- V6 CI output reviewed
- V7 Safe runtime observation
- V8 Staging/rehearsal verified
- V9 Production evidence reviewed

Check for:

- unsupported claims;
- scope creep;
- hidden runtime activation;
- hidden data migration;
- hidden external calls;
- hidden background work;
- security regressions;
- privacy risks;
- authorization issues;
- data integrity risks;
- failure modes;
- skipped or missing tests;
- rollback gaps;
- overconfident language.

Do not say production-ready, complete, fully secure, no issues, or ready unless the exact scope was exhaustively verified.

---

## Required Output

````md
## Verifier Pass

### Role
Verifier

### Task
-

### Risk Level
-

### Why This Risk Level
-

### Verification Level
-

### Repository Access Mode
- Direct tool access / Pasted excerpts only / No file access / Unknown

### Relevant Rules / Playbooks
-

### Evidence Reviewed
-

### Evidence Not Reviewed
-

### Source-Truth Phase Review
-

### Files Read
-

### Files Not Read But Needed
-

### Constraints
-

### What I Must Not Do
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

### Output Produced

#### Findings

##### Finding 1
- Severity:
- Evidence:
- Why it matters:
- Recommendation:

##### Finding 2
- Severity:
- Evidence:
- Why it matters:
- Recommendation:

#### Hidden Side Effects Check
-

#### Security / Privacy Check
-

#### Data / Migration / Deployment Check
-

#### Tests and Verification Gaps
-

#### Rollback / Recovery Gaps
-

#### False Confidence Risks
-

#### Recommendation
-

#### Human Decisions Required
-

### Verification Needed
-

### Escalation Needed?
-

### Next Role Recommendation
-

### Prompt For Next Role

```text
Role: [Executor / Reader / Architect / Handoff Scribe]

Task:
[State the exact next task. If findings require changes, ask Executor for a minimal correction patch. If evidence is missing, ask Reader to gather the missing evidence. If the plan needs reshaping, ask Architect. If acceptable within reviewed scope, ask Handoff Scribe to record an accurate handoff.]

Repository access:
[Direct tool access / Pasted excerpts only / No file access / Unknown]

Files / context to send to next model:
[List verification findings, reviewed evidence, proposed correction scope, and relevant context. Do not present this as source authority.]

Files already read:
[List files read by Verifier in this session]

Files you must re-read before acting:
[List files the next role must re-read before acting. If Executor is next, include every file it may edit.]

Evidence from previous role:
PROVEN:
- [Directly supported evidence from verification]

EXPECTED:
- [Expected but not directly observed]

ASSUMED:
- [Assumptions that must not be promoted to facts]

UNKNOWN:
- [Unknowns that remain after verification]

Risk level:
[Risk level and reason]

Verification level:
[Verification level and scope]

Findings to carry forward:
- [List findings, severities, and evidence]

Constraints:
[Scope limits and rules]

Do not:
- Do not treat this verification as broader than its reviewed scope.
- Do not claim production readiness, deployment status, migration completion, full security, full privacy correctness, or complete correctness unless exhaustively verified for the exact stated scope.
- Do not convert assumptions or expected behavior into proven facts.
- If acting as Executor, do not broaden the patch beyond the verified findings.
- If acting as Handoff Scribe, do not turn plans, recommendations, or unverified claims into completed facts.

Required output:
If Role is Executor, return a minimal correction Executor Pass using `Output Patch Rules — Strict` and include Prompt For Next Role.

If Role is Reader, return a Reader Pass focused only on the missing evidence and include Prompt For Next Role.

If Role is Architect, return an Architect Pass focused on re-planning the unsafe or unclear scope and include Prompt For Next Role.

If Role is Handoff Scribe, return an AI Handoff that separates files read, files changed or proposed, verification level, PROVEN, EXPECTED, ASSUMED, UNKNOWN, risks, next safe options, and human decisions. Include a next-session prompt.
```
````
