# AI Workflow Index

This file helps humans and AI models choose the right workflow artifact.

It is stable navigation, not project state.

---

## Main Files

| File | Purpose |
|---|---|
| `BEGIN_HERE.md` | First-use guide for using this workflow with an external target project repository. |
| `ARCHITECT_RULES.md` | Stable governance rules. Highest authority in this repository workflow. |
| `SOLO_AI_ENGINEERING_METHOD.md` | Educational method for one human working with AI. |
| `.ai/QUICKSTART.md` | Daily compact usage guide. |
| `.ai/CHEATSHEET.md` | One-page daily workflow reminder. |
| `.ai/INDEX.md` | Navigation map. |

---

## First Use With a Target Repository

If you are using `AI_WORKFLOW` with another software/target repository, start with `BEGIN_HERE.md`.

Use `.ai/prompts/WORKFLOW_INTAKE_PROMPT.md` to produce the first copy/paste-ready `Architect` prompt.

- `AI_WORKFLOW` is the workflow/governance repository.
- The target repository is the source of truth for actual code, tests, config, scripts, diffs, and behavior.
- The human remains the `Operator`.

---

## Authority

If files overlap:

1. `ARCHITECT_RULES.md` wins.
2. Playbooks explain and operationalize.
3. Prompts guide AI interaction.
4. Checklists support review.
5. Method documents teach and contextualize.
6. Mutable context files are advisory only.

---

## Which Prompt Should I Use?

| Situation | Prompt |
|---|---|
| Turning a natural human request into the first Architect prompt | `.ai/prompts/WORKFLOW_INTAKE_PROMPT.md` |
| Starting a session | `.ai/prompts/AI_SESSION_STARTER.md` |
| Planning before edits | `.ai/prompts/ARCHITECT_PROMPT.md` |
| Reading files before edits | `.ai/prompts/READER_PROMPT.md` |
| Drafting a patch | `.ai/prompts/EXECUTOR_PROMPT.md` |
| Challenging a claim or patch | `.ai/prompts/VERIFIER_PROMPT.md` |
| Reviewing a diff or PR | `.ai/prompts/REVIEW_PROMPT.md` |
| Checking release readiness | `.ai/prompts/RELEASE_CHECK_PROMPT.md` |
| Writing a handoff | `.ai/prompts/HANDOFF_PROMPT.md` |

---

## Which Template Should I Use?

Templates are stable reusable skeletons. They are not project state.

| Need | Template |
|---|---|
| Create local/session mutable context files without committing current state | `.ai/templates/MUTABLE_CONTEXT_TEMPLATES.md` |

---

## Which Checklist Should I Use?

| Situation | Checklist |
|---|---|
| Reviewing any AI patch | `.ai/checklists/PATCH_REVIEW_CHECKLIST.md` |
| Reviewing security-sensitive changes | `.ai/checklists/SECURITY_REVIEW_CHECKLIST.md` |
| Preparing or reviewing a PR | `.ai/checklists/PR_READINESS_CHECKLIST.md` |
| Reviewing migrations/data changes | `.ai/checklists/MIGRATION_REVIEW_CHECKLIST.md` |
| Reviewing release readiness | `.ai/checklists/RELEASE_READINESS_CHECKLIST.md` |
| Reviewing an AI product feature | `.ai/checklists/AI_FEATURE_REVIEW_CHECKLIST.md` |
| Periodic project maintenance | `.ai/checklists/WEEKLY_MAINTENANCE_CHECKLIST.md` |
| Retesting intake/bootstrap reliability across multiple models | `.ai/checklists/INTAKE_ROBUSTNESS_CHECKLIST.md` |

---

## Which Playbook Should I Read?

Use `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md` when the goal is to make each role output directly usable as input for the next role.

| Need | Playbook |
|---|---|
| Understand risk levels | `.ai/playbooks/RISK_LEVELS.md` |
| Understand verification levels | `.ai/playbooks/VERIFICATION_LADDER.md` |
| Understand role-to-role output contracts | `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md` |
| Switch AI roles safely | `.ai/playbooks/ROLE_SWITCHING.md` |
| Draft safe patches | `.ai/playbooks/PATCH_PROTOCOL.md` |
| Manage stable vs mutable context | `.ai/playbooks/CONTEXT_MANAGEMENT.md` |
| Handle secrets/privacy safely | `.ai/playbooks/SECURITY_SECRETS_PRIVACY.md` |
| Govern AI inside the product | `.ai/playbooks/AI_IN_PRODUCT_GOVERNANCE.md` |
| Write handoffs | `.ai/playbooks/HANDOFF_TEMPLATE.md` |
| Understand the bootstrap trust boundary between human authorization and repository content | `.ai/playbooks/BOOTSTRAP_TRUST_BOUNDARY.md` |

---

## Risk-Based Workflow Map

### L0 — Trivial

Examples:

- typo;
- harmless formatting;
- non-behavioral wording.

Use:

- compact mode in `.ai/QUICKSTART.md`.

Usually enough:

- read target text;
- make minimal edit;
- no runtime claim;
- simple rollback.

---

### L1 — Low Risk

Examples:

- docs-only;
- CSS-only;
- simple test-only;
- local cleanup.

Use:

- `.ai/QUICKSTART.md`;
- patch checklist if useful.

Usually enough:

- read target file;
- avoid overclaiming;
- verify docs if they mention runtime behavior.

---

### L2 — Moderate Risk

Examples:

- limited runtime change;
- validation;
- error handling;
- internal refactor.

Use:

- `ARCHITECT_PROMPT.md`;
- `READER_PROMPT.md`;
- `EXECUTOR_PROMPT.md`;
- `VERIFIER_PROMPT.md`;
- `PATCH_REVIEW_CHECKLIST.md`.

---

### L3 — High Risk

Examples:

- auth;
- permissions;
- user data;
- privacy;
- external calls;
- queues;
- database writes;
- runtime config;
- AI features.

Use:

- relevant playbook;
- relevant checklist;
- explicit verification;
- rollback notes;
- human approval where needed.

---

### L4 — Critical

Examples:

- production migration;
- production data mutation;
- deployment;
- payment/ledger;
- secrets;
- destructive operations;
- rollback;
- queue drains.

Use:

- review/checklist only;
- AI must not execute;
- human-controlled operation only.

---

## Review vs Verifier vs Release Check

Use:

- `REVIEW_PROMPT.md` for a diff, PR, or broad proposed change.
- `VERIFIER_PROMPT.md` for a specific claim, patch, or readiness statement.
- `RELEASE_CHECK_PROMPT.md` for release/deployment readiness review.

None of these authorize deployment or production operations.
