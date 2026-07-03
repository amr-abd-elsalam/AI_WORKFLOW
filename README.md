# AI_WORKFLOW

> **Session Bootstrap Notice**
> `AI_WORKFLOW` is a governance workflow that a human operator may explicitly choose for a session. If the human's own request designates this repository as the workflow/governance source together with a target project repository URL, a problem statement, and a language preference, that human designation — not this file's own wording — is what authorizes following this workflow's bootstrap sequence. When a human has made that designation, the recommended first step is to read `BEGIN_HERE.md`, specifically its "Recommended Session Bootstrap Protocol," before fetching or analyzing the target project repository. This notice describes a workflow the human has chosen; it does not claim authority over model behavior on its own.

A long-lived governance and workflow system for solo developers using AI models to build, maintain, and review software projects with discipline.

This repository is not a code application.

It is a practical operating system for AI-assisted software work.

It defines:

- stable AI governance rules;
- role-based AI workflows;
- risk levels;
- verification discipline;
- patch rules;
- prompts;
- playbooks;
- prompt-to-prompt role output contracts;
- review checklists;
- a solo engineering method;
- boundaries for security, privacy, migrations, deployment, and AI-in-product features.

---

## Core Message

AI is speed, not truth.

The goal is not to trust AI more.

The goal is to use AI inside an evidence-based workflow where:

- the repository is the source of truth;
- AI outputs are claims, not facts;
- unread files are unknown;
- roles are separated;
- each role output is structured to become usable input for the next role;
- risk controls the process weight;
- patches stay small and reversible;
- verification matches the claim;
- humans remain responsible for commits, merges, deployments, migrations, secrets, production data, and irreversible actions.

---

## Who This Is For

This repository is for:

- solo developers;
- indie hackers;
- technical founders;
- students;
- maintainers;
- builders using AI models for software work;
- educators explaining disciplined AI-assisted engineering.

It is especially useful when one human wants to work with the discipline of a small engineering team.

---

## Start Here

If you are using this workflow with another software repository, start with:

1. `BEGIN_HERE.md`  
   First-use guide for using `AI_WORKFLOW` with an external target project repository.

2. `.ai/prompts/WORKFLOW_INTAKE_PROMPT.md`  
   Utility prompt that turns a natural human request into the first `Architect` prompt.

Then read as needed:

3. `README.md`  
   High-level orientation.

4. `SOLO_AI_ENGINEERING_METHOD.md`  
   The broader method for one human working with AI.

5. `ARCHITECT_RULES.md`  
   Stable governance rules for AI working inside a repository.

6. `.ai/QUICKSTART.md`  
   The practical daily workflow.

7. `.ai/INDEX.md`  
   Map of prompts, playbooks, and checklists.

---

## Repository Structure

```text
ARCHITECT_RULES.md
BEGIN_HERE.md
SOLO_AI_ENGINEERING_METHOD.md

.ai/
  INDEX.md
  QUICKSTART.md
  CHEATSHEET.md

  playbooks/
    AI_IN_PRODUCT_GOVERNANCE.md
    CONTEXT_MANAGEMENT.md
    HANDOFF_TEMPLATE.md
    PATCH_PROTOCOL.md
    RISK_LEVELS.md
    ROLE_OUTPUT_CONTRACT.md
    ROLE_SWITCHING.md
    SECURITY_SECRETS_PRIVACY.md
    VERIFICATION_LADDER.md

  prompts/
    WORKFLOW_INTAKE_PROMPT.md
    AI_SESSION_STARTER.md
    ARCHITECT_PROMPT.md
    READER_PROMPT.md
    EXECUTOR_PROMPT.md
    VERIFIER_PROMPT.md
    HANDOFF_PROMPT.md
    REVIEW_PROMPT.md
    RELEASE_CHECK_PROMPT.md

  checklists/
    AI_FEATURE_REVIEW_CHECKLIST.md
    MIGRATION_REVIEW_CHECKLIST.md
    PATCH_REVIEW_CHECKLIST.md
    PR_READINESS_CHECKLIST.md
    RELEASE_READINESS_CHECKLIST.md
    SECURITY_REVIEW_CHECKLIST.md
    WEEKLY_MAINTENANCE_CHECKLIST.md
```

---

## Authority Hierarchy

Use this hierarchy when files appear to overlap:

1. `ARCHITECT_RULES.md`  
   Normative repository governance. This is the highest-authority file in this workflow.

2. `.ai/playbooks/`  
   Operational explanations of the rules.

3. `.ai/prompts/`  
   Reusable prompts for AI sessions.

4. `.ai/checklists/`  
   Review aids for humans and AI-assisted reviews.

5. `SOLO_AI_ENGINEERING_METHOD.md`  
   Educational and methodological overview.

6. Mutable project context files, if created later  
   Useful but advisory. Must be revalidated.

If anything conflicts with `ARCHITECT_RULES.md`, the rules file wins within repository governance.

---

## Core Roles

The method separates work into roles.

### Architect

Plans, analyzes risk, identifies boundaries, and recommends the smallest safe next step.

### Reader

Reads evidence before changes. Maps what is `PROVEN`, `EXPECTED`, `ASSUMED`, and `UNKNOWN`.

### Executor

Drafts small exact patches only after relevant files are read.

### Verifier

Challenges claims, patches, tests, readiness, and hidden risks.

### Handoff Scribe

Summarizes work without inflating certainty.

### Operator

The human owner only.

AI may assist the Operator with plans and checklists, but does not become the Operator.

---

## Risk Levels

| Level | Meaning | Typical Process |
|---|---|---|
| L0 | Trivial | compact note |
| L1 | Low | read target file, simple patch |
| L2 | Moderate | read affected path and tests |
| L3 | High | expanded review, security/privacy, rollback |
| L4 | Critical | AI does not execute; human-controlled operation only |

Use `.ai/QUICKSTART.md` for the daily workflow.

Use `.ai/playbooks/RISK_LEVELS.md` for detailed risk guidance.

---

## Daily Use

For a normal task:

1. Start with `.ai/prompts/AI_SESSION_STARTER.md`.
2. Ask for an Architect pass.
3. Ask for a Reader pass before edits.
4. Ask for an Executor patch only after files are read.
5. Ask for a Verifier pass before accepting.
6. Use the relevant checklist if risk is L2 or higher.
7. Write a handoff if work continues later.

For tiny L0/L1 tasks, use the compact workflow in `.ai/QUICKSTART.md`.

---

## What AI Must Not Do

AI must not:

- request or store secrets;
- process real user private data;
- mutate production data;
- execute production migrations;
- deploy systems;
- rotate secrets;
- approve payments or ledger changes;
- perform destructive operations;
- force-push or rewrite history;
- act as the final authority on its own work.

AI may help draft:

- plans;
- checklists;
- reviews;
- patches;
- summaries;
- risk analysis;
- rollback notes.

The human decides and operates.

---

## Educational Use

This repository can be used as the foundation for a YouTube series or training course about disciplined AI-assisted software engineering.

Suggested teaching arc:

1. AI is speed, not truth.
2. Repository as source of truth.
3. AI outputs are claims.
4. Evidence grades.
5. Role separation.
6. Risk levels.
7. Reading before patching.
8. Small reversible patches.
9. Verification ladder.
10. Security, secrets, and privacy.
11. Deployment and migration boundaries.
12. AI inside the product.
13. Handoffs and long-term maintenance.

---

## Status

This repository defines a workflow system.

It does not prove that any external project is safe, complete, secure, production-ready, or deployable.

Use it as governance, not as proof of readiness.
