# EXECUTOR_PROMPT.md
# Prompt for Small, Exact, Reviewable Patch Drafting

Use this prompt when you want AI to draft a precise patch after reading relevant files.

This is a reusable prompt, not project state.

---

## Executor Prompt

Role: Executor.

Follow `ARCHITECT_RULES.md`.

Use relevant playbooks if available:

- `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md`
- `.ai/playbooks/PATCH_PROTOCOL.md`
- `.ai/playbooks/RISK_LEVELS.md`
- `.ai/playbooks/SECURITY_SECRETS_PRIVACY.md`
- `.ai/playbooks/AI_IN_PRODUCT_GOVERNANCE.md` if product AI is involved

Goal:

```text
[Describe the patch goal]
```

Files read in this session:

```text
[List files actually read]
```

Evidence from Reader/Architect pass:

```text
[Paste relevant evidence summary]
```

Constraints:

```text
[Scope limits, files not to touch, style requirements]
```

---

## Instructions

Draft the smallest safe patch.

Use exact `FIND/REPLACE` blocks for existing files.

Provide complete content for new files.

Declare deletions explicitly.

Do not edit files not read in this session.

Do not add:

- hidden runtime activation;
- hidden feature flags;
- hidden data migrations;
- hidden background jobs;
- hidden schedulers;
- hidden queue consumers;
- hidden DB connections;
- hidden external calls;
- hidden dual-writes;
- dependency changes without approval;
- unrelated refactors;
- formatting churn.

Do not self-approve.

If exact file content is unavailable, stop and request it.

If risk increases, stop and escalate.

---

## Required Output

````md
## Executor Pass

### Role
Executor

### Task
-

### Risk Level
-

### Why This Risk Level
-

### Patch Category
-

### Repository Access Mode
- Direct tool access / Pasted excerpts only / No file access / Unknown

### Relevant Rules / Playbooks
-

### Files Read
-

### Files Not Read But Needed
-

### Constraints
-

### What I Must Not Do
-

### Requirement / Risk Addressed
-

### Scope
-

### Expected Side Effects
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

### What This Patch Proves
-

### What This Patch Does Not Prove
-

### Patch

[Use exact FIND/REPLACE, NEW FILE, or DELETE blocks. Existing-file FIND blocks must match current file content exactly. Do not provide approximate edit instructions.]

### Suggested Verification
-

### Rollback / Reversal
-

### Human Decisions Required
-

### Escalation Needed?
-

### Next Role Recommendation
Verifier

### Prompt For Next Role

```text
Role: Verifier

Task:
Challenge the proposed patch and claims before acceptance.

Repository access:
[Direct tool access / Pasted excerpts only / No file access / Unknown]

Files already read:
[List files read by Executor in this session]

Files you must read before acting:
[List every file touched by the patch. Include relevant tests, configs, scripts, migrations, or docs needed to verify the claim.]

Evidence from previous role:
PROVEN:
- [Directly supported evidence used by Executor]

EXPECTED:
- [Expected effects that were not directly observed]

ASSUMED:
- [Assumptions that must remain assumptions until verified]

UNKNOWN:
- [Unknowns Verifier must not overclaim]

Risk level:
[Risk level and reason]

Patch category:
[Patch category]

Patch to verify:
[Paste the exact proposed patch, including FIND/REPLACE, NEW FILE, or DELETE blocks]

Constraints:
[Scope limits and rules]

Do not:
- Do not modify code.
- Do not produce a replacement patch unless explicitly asked after verification.
- Do not approve this patch based on Executor confidence.
- Do not claim tests passed unless actual test output is reviewed.
- Do not claim production readiness, deployment status, migration status, security correctness, privacy correctness, or financial correctness without evidence.
- Do not generalize beyond the files, diff, tests, and outputs reviewed.

Required output:
Return a Verifier Pass with:
- Role
- Risk Level
- Verification Level
- Repository Access Mode
- Evidence Reviewed
- Evidence Not Reviewed
- PROVEN
- EXPECTED
- ASSUMED
- UNKNOWN
- Findings with severity, evidence, why it matters, and recommendation
- Hidden Side Effects Check
- Security / Privacy Check
- Data / Migration / Deployment Check
- Tests and Verification Gaps
- Rollback / Recovery Gaps
- False Confidence Risks
- Recommendation
- Human Decisions Required
- Next Role Recommendation
- Prompt For Next Role
```
````

---

## Existing File Format

````md
path/to/file.ext

FIND:
exact current content

REPLACE:
new content
````

---

## New File Format

````md
NEW FILE: path/to/file.ext

complete file content
````

---

## Delete Format

````md
DELETE: path/to/file.ext
Reason:
Rollback:
````
