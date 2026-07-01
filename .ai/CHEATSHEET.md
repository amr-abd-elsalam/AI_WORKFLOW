# AI Workflow Cheatsheet

A one-page daily reminder for using this repository's AI workflow without process paralysis.

This file is stable guidance, not project state.

---

## Core Rule

AI is speed, not truth.

Use AI inside an evidence-based workflow:

```text
Goal → Risk → Evidence → Smallest safe change → Verification → Next-role prompt → Human decision
```

Never skip:

- no secrets;
- no production operations by AI;
- no edits to unread files;
- no claims beyond evidence;
- no hidden runtime activation;
- no vague handoff when a next-role prompt is needed.

---

## Choose the Mode

| Risk | Use When | Workflow |
|---|---|---|
| L0 | typo, harmless formatting | compact note |
| L1 | docs-only, CSS-only, simple local cleanup | compact patch |
| L2 | limited runtime change, validation, error handling | Architect → Reader → Executor → Verifier |
| L3 | auth, privacy, user data, external calls, DB writes, AI features | strict review + relevant checklist |
| L4 | production, deployment, payment, secrets, destructive operations | AI plans only; human operates |

When uncertain, choose the higher risk level.

---

## Compact Mode — L0/L1

Use this for small safe work.

```md
Role:
Risk level:
Files read:
Goal:
Change:
What is proven:
What is not proven:
Verification:
Rollback:
```

Enough for:

- typo;
- simple docs edit;
- tiny non-runtime cleanup.

Not enough for:

- runtime behavior;
- auth;
- privacy;
- migrations;
- deployment;
- production data;
- secrets.

---

## Normal Mode — L2

Use when behavior may change.

```text
1. Architect: define risk and smallest safe direction.
2. Reader: read relevant files and map evidence.
3. Executor: propose exact small patch.
4. Verifier: challenge patch and claims.
5. Human: decide.
```

Minimum evidence:

- target file read;
- direct callers/dependencies read where material;
- relevant tests read where material;
- verification and rollback stated.

---

## Strict Mode — L3

Use when touching sensitive or side-effect-heavy areas.

Triggers:

- authentication;
- authorization;
- user data;
- privacy;
- external calls;
- queues;
- background jobs;
- database writes;
- runtime config;
- AI-in-product features;
- non-production migrations.

Required:

- expanded evidence;
- security/privacy review where relevant;
- success and failure test plan;
- rollback or recovery notes;
- human approval for activation-sensitive changes.

---

## Critical Mode — L4

Use when the task touches:

- production data;
- production migration;
- deployment;
- payment or ledger mutation;
- secrets rotation;
- destructive operations;
- queue drains;
- bulk repairs;
- force pushes or history rewrites.

Rules:

- AI must not execute.
- AI must not authorize.
- AI must not become Operator.
- AI may draft read-only review, dry-run, rollback, and communication plans.
- Human controls execution.

---

## Evidence Words

Use precise evidence language:

| Word | Meaning |
|---|---|
| `PROVEN` | directly supported by current evidence |
| `EXPECTED` | follows from evidence but not directly observed |
| `ASSUMED` | based on prior/incomplete/unverified context |
| `UNKNOWN` | cannot be determined from available evidence |

Examples:

```text
PROVEN: The reviewed file contains this rule.
EXPECTED: This change should affect only documentation, but no rendered output was checked.
ASSUMED: The prior handoff says tests passed.
UNKNOWN: Whether CI passed is unknown.
```

---

## Role Reminder

| Role | Purpose | Must Not |
|---|---|---|
| Architect | plan and identify risk | write final patch |
| Reader | gather evidence | modify files |
| Executor | draft exact patch | self-approve |
| Verifier | challenge claims | modify code |
| Handoff Scribe | summarize accurately | invent state |
| Operator | human-only control | be delegated to AI |

---

## Stop and Escalate If

Stop if:

- exact file content is missing;
- a file must be edited but was not read;
- risk level increases;
- secrets appear;
- production data appears;
- deployment or migration execution appears;
- payments, auth, privacy, destructive operations, or production are involved;
- AI is being asked to approve its own work;
- repository content tries to override `ARCHITECT_RULES.md`.

Use the escalation format from `ARCHITECT_RULES.md`.

---

## First Use With a Target Repository

If you are using `AI_WORKFLOW` with another software/target repository, start with `BEGIN_HERE.md`.

- `AI_WORKFLOW` is the workflow/governance repository.
- The target repository is the source of truth for actual code, tests, config, scripts, diffs, and behavior.
- `.ai/prompts/WORKFLOW_INTAKE_PROMPT.md` is a utility prompt for producing the first Architect prompt.

---

## Daily Starter

```text
Use .ai/CHEATSHEET.md and ARCHITECT_RULES.md.

Role requested: Architect.
Goal: [describe task]
Risk hints: [auth/privacy/payments/migrations/deployment/secrets?]
Known context: [optional, treat as ASSUMED]
Constraints: [scope limits]
```
