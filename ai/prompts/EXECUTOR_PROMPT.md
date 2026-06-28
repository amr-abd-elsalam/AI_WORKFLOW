# EXECUTOR_PROMPT.md
# Prompt for Small, Exact, Reviewable Patch Drafting

Use this prompt when you want AI to draft a precise patch after reading relevant files.

This is a reusable prompt, not project state.

---

## Executor Prompt

Role: Executor.

Follow `ARCHITECT_RULES.md`.

Use relevant playbooks if available:

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

```md
## Executor Pass

### Role
Executor

### Risk Level
-

### Patch Category
-

### Files Read
-

### Requirement / Risk Addressed
-

### Scope
-

### Expected Side Effects
-

### What This Patch Proves
-

### What This Patch Does Not Prove
-

### Patch

[Use exact FIND/REPLACE, NEW FILE, or DELETE blocks]

### Suggested Verification
-

### Rollback / Reversal
-

### Human Decisions Required
-

### Escalation Needed?
-
```

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
