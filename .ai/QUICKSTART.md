# AI Workflow Quickstart

A compact daily guide for using this repository's AI workflow without unnecessary ceremony.

This file is stable guidance, not project state.

---

## The Five-Minute Version

For most tasks:

1. State the goal.
2. Classify the risk.
3. Read relevant files.
4. Make the smallest safe change.
5. Verify only what the evidence supports.

Never skip:

- no secrets;
- no production operations by AI;
- no edits to unread files;
- no claims beyond evidence.

---

## Tiny Task Mode — L0

Use for:

- typo fixes;
- harmless formatting;
- comment wording;
- wording with no runtime claim.

Minimum workflow:

```md
Role: Executor
Risk level: L0
Files read:
Change:
Verification:
Rollback: revert this edit
```

Rules:

- read the target text;
- make only the tiny edit;
- do not claim runtime impact;
- no long handoff needed.

---

## Low-Risk Mode — L1

Use for:

- docs-only edits;
- CSS-only edits;
- simple test-only changes;
- local cleanup with no runtime claim.

Minimum workflow:

```md
Role:
Risk level: L1
Files read:
Scope:
Patch:
What is proven:
What is not proven:
Verification:
Rollback:
```

Rules:

- read target file;
- if docs describe runtime behavior, verify source or mark it unverified;
- keep patch narrow;
- avoid unrelated cleanup.

---

## Normal Mode — L2

Use for:

- limited runtime behavior;
- validation;
- error handling;
- small internal refactor.

Workflow:

1. Architect pass.
2. Reader pass.
3. Executor pass.
4. Verifier pass.
5. Relevant tests/checks.

Use:

- `.ai/prompts/ARCHITECT_PROMPT.md`
- `.ai/prompts/READER_PROMPT.md`
- `.ai/prompts/EXECUTOR_PROMPT.md`
- `.ai/prompts/VERIFIER_PROMPT.md`
- `.ai/checklists/PATCH_REVIEW_CHECKLIST.md`

Minimum evidence:

- target file read;
- direct callers/dependencies read where material;
- relevant tests read where material;
- verification and rollback stated.

---

## Strict Mode — L3

Use for:

- authentication;
- authorization;
- user data;
- privacy;
- external calls;
- queues;
- background jobs;
- database writes;
- runtime config;
- AI product features;
- non-production migrations.

Workflow:

1. Architect pass.
2. Reader pass.
3. Security/privacy review if relevant.
4. Executor patch only after evidence is sufficient.
5. Verifier pass.
6. Tests for success and failure modes.
7. Rollback or recovery notes.
8. Human approval for activation-sensitive changes.

Use relevant checklists:

- `SECURITY_REVIEW_CHECKLIST.md`
- `AI_FEATURE_REVIEW_CHECKLIST.md`
- `MIGRATION_REVIEW_CHECKLIST.md`
- `PATCH_REVIEW_CHECKLIST.md`

---

## Critical Mode — L4

Use for:

- production migration;
- production data mutation;
- deployment;
- payment/ledger mutation;
- secrets rotation;
- destructive operations;
- queue drains;
- bulk repairs;
- force pushes or history rewrites.

Rules:

- AI must not execute.
- AI must not casually authorize.
- Human controls the operation.
- Use redacted evidence only.
- Require backup/recovery and rollback planning.

AI may help draft:

- risk analysis;
- dry-run plan;
- read-only inspection plan;
- rollback checklist;
- communication notes;
- post-operation review.

---

## Quick Role Guide

| Role | Use When | Must Not |
|---|---|---|
| Architect | You need direction before edits | write final executable patches |
| Reader | You need evidence before edits | modify code |
| Executor | You need a precise patch | self-approve |
| Verifier | You need to challenge claims | modify code |
| Handoff Scribe | You need to transfer context | invent state |
| Operator | Human-only responsibility | be delegated to AI |

---

## Quick Evidence Language

Use:

- `PROVEN`: directly supported by current evidence.
- `EXPECTED`: follows from evidence but not observed.
- `ASSUMED`: based on incomplete or prior context.
- `UNKNOWN`: not determined.

Examples:

```text
PROVEN: The file contains this function.
EXPECTED: The code path should reject empty input, but it was not run.
ASSUMED: The prior handoff says tests passed.
UNKNOWN: Whether this is deployed is unknown.
```

---

## Good Starter Prompt

```text
Use .ai/prompts/AI_SESSION_STARTER.md.

Role requested: Architect.
Goal: [describe the task]
Known context: [optional, treat as ASSUMED]
Risk hints: [auth/privacy/payments/migrations/deployment/secrets?]
Constraints: [scope limits]
```

---

## For Small Patches

Use:

```text
Role: Executor.

Risk level: L0/L1.
Files read:
Goal:
Propose the smallest safe patch.
Use exact FIND/REPLACE.
Do not claim runtime behavior unless verified.
State rollback.
```

---

## For Reviews

Use:

```text
Role: Verifier.

Review this patch/diff.
Do not modify code.
Classify evidence as PROVEN, EXPECTED, ASSUMED, UNKNOWN.
Find false confidence, missing tests, hidden side effects, and security/privacy risks.
```

---

## Stop Immediately If

- exact file content is missing;
- a file must be edited but was not read;
- secrets appear;
- production data appears;
- deployment or migration execution appears;
- risk level increases;
- the task touches payments, auth, privacy, destructive operations, or production;
- AI is being asked to approve its own work.

Use the escalation format from `ARCHITECT_RULES.md`.
