# SOLO_AI_ENGINEERING_METHOD.md
# A Practical Method for One Human Building Durable Software with AI

This document describes a long-lived working method for a solo human owner using AI models to build, maintain, verify, and evolve software projects.

It is not a project status file.
It is not a patch brief.
It is not a roadmap.
It is not proof of readiness.
It must not contain secrets, current branch state, temporary plans, production data, or incident-specific facts.

The purpose of this method is to help one human operate with the discipline of a small engineering team while retaining human ownership, evidence-based reasoning, and safe control over the project.

---

## 1. Core Idea

AI does not remove the need for engineering discipline.

AI increases speed, but speed without governance increases the speed of mistakes.

The goal is not to trust AI more.

The goal is to create a working system where AI remains useful even when it is incomplete, uncertain, or wrong.

A solo human using AI should not behave like an unstructured individual with a powerful autocomplete tool.

A solo human should behave like a small engineering organization compressed into one person, supported by AI roles, evidence, verification, and automation.

---

## 2. The Central Rule

The repository is the source of truth.

AI is not the source of truth.
AI memory is not the source of truth.
Prior chats are not the source of truth.
Generated summaries are not the source of truth.
Documentation is not automatically runtime truth.
Passing tests are not automatically production readiness.

Every material claim must be tied to evidence.

If evidence is missing, the correct answer is not confidence.

The correct answer is:

> unknown, assumed, expected, or proven within a limited scope.

---

## 3. The Solo AI Engineering Model

A solo owner must deliberately separate the roles that a team would normally separate.

The same human may use the same AI model, but the work must be divided into passes.

The core roles are:

1. Architect
2. Reader
3. Executor
4. Verifier
5. Handoff Scribe
6. Operator

The AI may assist in the first five.
The human remains responsible for the sixth.

---

## 4. Role 1: Architect

The Architect thinks before changing.

The Architect asks:

- What are we trying to solve?
- What is the smallest safe next step?
- What are the risks?
- What files are likely relevant?
- What could create false confidence?
- What should not be touched?
- Is this a design problem, runtime problem, test problem, documentation problem, or operational problem?

The Architect may propose:

- options;
- tradeoffs;
- risk levels;
- sequencing;
- rollback thinking;
- boundaries;
- test strategy.

The Architect must not:

- claim implementation without reading code;
- claim readiness from documentation;
- recommend major rewrites without evidence;
- hide uncertainty;
- jump directly into broad patches.

Typical output:

```md
Role: Architect
Goal:
Risk level:
Relevant areas to inspect:
Assumptions:
Unknowns:
Smallest safe next step:
Options:
Recommendation:
```

---

## 5. Role 2: Reader

The Reader gathers evidence.

The Reader asks:

- What files must be read before any patch?
- What callers and dependencies matter?
- What tests actually assert behavior?
- What configuration changes runtime behavior?
- Are docs making claims that source does not support?
- Is there generated content that must not be treated as authority?

The Reader does not modify code.

The Reader produces an evidence map.

Typical output:

```md
Role: Reader

Files read:
-

Relevant evidence:
-

Missing evidence:
-

Assumptions:
-

Unknowns:
-

Recommended next role:
-
```

The Reader protects the project from the most common AI failure:

> editing a system it has not actually inspected.

---

## 6. Role 3: Executor

The Executor drafts the smallest safe patch.

The Executor acts only after enough relevant files have been read.

The Executor must:

- keep one primary concern per patch;
- use exact edits for existing files;
- provide full content for new files;
- avoid hidden activation;
- avoid unrelated refactors;
- avoid dependency changes unless approved;
- describe side effects;
- suggest verification.

The Executor must not self-approve.

Typical output:

```md
Role: Executor
Risk level:
Patch category:
Files read:
Requirement addressed:
Scope:
Expected side effects:
What this patch proves:
What this patch does not prove:
Suggested verification:
Rollback:
```

For existing files, use:

````md
path/to/file.ext

FIND:
exact current content

REPLACE:
new content
````

For new files, use:

````md
NEW FILE: path/to/file.ext

complete file content
````

---

## 7. Role 4: Verifier

The Verifier challenges the work.

The Verifier is not there to be encouraging.

The Verifier asks:

- Did we read enough?
- Did the patch do only what it claims?
- Are there hidden side effects?
- Are tests actually asserting the claim?
- Are skipped tests being ignored?
- Does this affect auth, privacy, payments, data, migrations, deployment, or production?
- Is rollback possible?
- Is the language overconfident?
- What remains unknown?

The Verifier classifies evidence:

- `PROVEN`
- `EXPECTED`
- `ASSUMED`
- `UNKNOWN`

Typical output:

```md
Role: Verifier
Risk level:
Evidence reviewed:
Verification level:

## PROVEN
-

## EXPECTED
-

## ASSUMED
-

## UNKNOWN
-

## Risks
-

## Missing checks
-

## Recommendation
-
```

The Verifier must not:

- modify code while verifying;
- approve its own prior work as final proof;
- generalize beyond reviewed evidence.

---

## 8. Role 5: Handoff Scribe

The Handoff Scribe preserves useful context without inflating certainty.

The Scribe writes what the next session needs to know, but does not turn plans into facts.

A good handoff includes:

- task goal;
- role used;
- risk level;
- files read;
- files changed or proposed;
- tests run;
- tests not run;
- proven facts;
- expected but unproven behavior;
- assumptions;
- unknowns;
- risks;
- rollback notes;
- next safe options;
- human decisions required.

A handoff is not source authority.

It is a map.

The next session must re-read relevant files.

---

## 9. Role 6: Operator

The Operator is the human.

AI may assist the Operator, but must not become the Operator.

The human controls:

- commits;
- merges;
- pushes;
- deployments;
- migrations;
- production operations;
- secrets;
- payment systems;
- destructive operations;
- incident decisions;
- rollback decisions.

AI may help draft:

- checklists;
- dry-run plans;
- risk analysis;
- rollback plans;
- release notes;
- incident summaries;
- review questions.

AI must not casually execute or authorize sensitive operations.

The Operator rule:

> AI may advise. The human decides and operates.

---

## 10. The Standard Work Loop

Use this loop for meaningful work.

```text
1. Define the goal.
2. Classify risk.
3. Select role.
4. Read relevant evidence.
5. Propose smallest safe change.
6. Verify claims.
7. Run appropriate checks.
8. Record handoff if needed.
9. Human decides.
10. Commit or continue.
```

For small L0/L1 tasks, this loop can be compact.

For L2/L3/L4 tasks, make the loop explicit.

---

## 11. Risk Levels

Use risk levels to prevent both recklessness and paralysis.

### L0 — Trivial

Examples:

- typo;
- harmless formatting;
- comment wording.

Expected process:

- read target text;
- make minimal edit;
- no runtime claims.

---

### L1 — Low Risk

Examples:

- docs-only;
- test-only;
- CSS-only;
- local cleanup.

Expected process:

- read target file;
- avoid broad claims;
- verify if docs mention runtime behavior.

---

### L2 — Moderate Risk

Examples:

- limited runtime logic;
- validation;
- error handling;
- small internal refactor.

Expected process:

- read target file;
- read direct callers/dependencies where relevant;
- read tests;
- suggest focused verification.

---

### L3 — High Risk

Examples:

- auth;
- permissions;
- user data;
- privacy;
- external calls;
- queues;
- background jobs;
- runtime config;
- database writes;
- non-production migrations.

Expected process:

- expanded source review;
- failure-mode analysis;
- security/privacy review;
- rollback notes;
- human approval for activation-sensitive changes.

---

### L4 — Critical

Examples:

- production data;
- production migration;
- deployment;
- payment or ledger mutation;
- secrets;
- destructive operations;
- rollback;
- queue drains;
- force push to shared branch.

Expected process:

- AI does not execute;
- human decision required;
- safe environment confirmation;
- backup/recovery plan;
- rollback plan;
- redacted evidence only.

---

## 12. Evidence Grades

Use four evidence grades.

### PROVEN

Directly supported by current source, diff, tool output, test output, or safe observed behavior in this session.

Example:

> The reviewed file contains this function.

---

### EXPECTED

Logically follows from proven evidence, but was not directly observed.

Example:

> Based on the reviewed code path, this input is expected to return validation error X, but the behavior was not run.

---

### ASSUMED

Based on docs, prior sessions, memory, incomplete evidence, or unverified human statements.

Example:

> The prior handoff says CI passed, but no CI output was reviewed in this session.

---

### UNKNOWN

Cannot be determined from available evidence.

Example:

> Whether this is deployed to production is unknown.

---

## 13. Verification Ladder

Claims must match verification strength.

| Verification Level | Meaning |
|---|---|
| V0 | Not verified |
| V1 | File/excerpt inspected |
| V2 | Source path reviewed |
| V3 | Diff reviewed |
| V4 | Tests inspected |
| V5 | Local test output reviewed |
| V6 | CI output reviewed |
| V7 | Safe runtime observation |
| V8 | Staging/rehearsal verified |
| V9 | Production evidence reviewed |

Do not claim a higher level than the evidence supports.

Examples:

- Reading code does not prove tests pass.
- Reading tests does not prove they ran.
- CI config does not prove CI passed.
- Migration file does not prove migration executed.
- Deployment config does not prove deployment happened.
- Logs show observed events, not complete truth.

---

## 14. The Three Context Layers

A durable solo AI workflow separates context into three layers.

### 1. Stable Governance

Examples:

- `ARCHITECT_RULES.md`
- `.ai/playbooks/*.md`

Contains:

- rules;
- roles;
- risk levels;
- verification discipline;
- security boundaries.

Must not contain:

- current branch;
- current patch;
- latest test status;
- temporary plans;
- incident details;
- secrets.

---

### 2. Mutable Project Context

Examples:

- `.ai/CURRENT_STATE.md`
- `.ai/HANDOFF.md`
- `.ai/NEXT_PATCH_BRIEF.md`
- `.ai/DECISIONS_LOG.md`

Contains:

- current task;
- known open issues;
- latest handoff;
- decisions;
- current risks;
- tests recently run.

Must be treated as advisory.

Mutable context may be stale.

---

### 3. Evidence

Examples:

- current source files;
- diffs;
- tests;
- actual test output;
- Git history;
- CI logs;
- safe runtime observations.

Evidence outranks narrative.

---

## 15. Daily Workflow for a Solo Owner

A practical daily AI-assisted workflow:

### Start

1. Read the current goal.
2. Check repository state if relevant.
3. Read `ARCHITECT_RULES.md`.
4. Read relevant mutable context.
5. Treat mutable context as assumed until verified.

### Plan

1. Ask AI as Architect.
2. Classify risk.
3. Identify files to read.
4. Choose smallest safe next step.

### Work

1. Ask AI as Reader.
2. Ask AI as Executor only after reading.
3. Apply patch manually or through reviewed tooling.
4. Run appropriate tests/checks.

### Verify

1. Ask AI as Verifier.
2. Review actual diff.
3. Review actual test output.
4. Record what remains unknown.

### End

1. Commit only reviewed scope.
2. Write/update handoff if work continues later.
3. Do not store secrets or temporary noise in stable files.

---

## 16. Weekly Workflow

Once per week or per major milestone, perform a maintenance review.

Suggested checklist:

```md
## Weekly Solo AI Engineering Review

### Repository hygiene
- Are there unrelated changes?
- Are generated files understood?
- Are dependencies changed intentionally?
- Are ignored files appropriate?

### Tests and verification
- Are key tests passing?
- Are skipped tests intentional?
- Are brittle tests hiding risk?
- Is coverage missing around high-risk logic?

### Security and privacy
- Any secrets risk?
- Any sensitive data in logs/tests/docs?
- Any broadened access?
- Any dependency vulnerabilities?

### Architecture
- Are boundaries still clear?
- Any module becoming too coupled?
- Any repeated pain that needs a seam?
- Any premature expansion being proposed?

### AI process
- Did AI make unsupported claims?
- Did handoffs stay accurate?
- Did mutable context become stale?
- Did any prompt override governance?

### Next safe options
1.
2.
3.
```

---

## 17. Monthly or Milestone Review

At larger intervals, review the project as a system.

Questions:

1. What parts are stable?
2. What parts are risky?
3. What parts lack tests?
4. What parts lack ownership clarity?
5. What docs claim more than source proves?
6. What runtime behavior is not verified?
7. What dependencies or services increase operational risk?
8. What would make rollback easier?
9. What should be deleted or simplified?
10. What should not be expanded yet?

The goal is not to create bureaucracy.

The goal is to keep a solo project from becoming unmanageable.

---

## 18. Prompt Patterns

Use prompts that force evidence and role separation.

### Architect Prompt

```text
Role: Architect.

Goal:
[describe goal]

Use repository evidence only where available.
Do not propose code yet.
Classify risk.
Identify files that must be read before implementation.
List assumptions and unknowns.
Recommend the smallest safe next step.
```

---

### Reader Prompt

```text
Role: Reader.

Read the relevant files for this task.
Do not propose edits yet.
List files read.
Summarize evidence.
Identify missing files or uncertainty.
State what is proven, expected, assumed, and unknown.
```

---

### Executor Prompt

```text
Role: Executor.

Use only files read in this session.
Propose the smallest safe patch.
Use exact FIND/REPLACE blocks for existing files.
Provide full content for new files.
State risk level, scope, expected side effects, verification, and rollback.
Do not add hidden activation or unrelated refactors.
```

---

### Verifier Prompt

```text
Role: Verifier.

Challenge the proposed patch and claims.
Do not modify code.
Review source, diff, and tests where available.
Classify evidence as PROVEN, EXPECTED, ASSUMED, UNKNOWN.
Find hidden side effects, missing tests, security/privacy risks, and false confidence.
State what remains unverified.
```

---

### Handoff Prompt

```text
Role: Handoff Scribe.

Write a compact handoff.
Do not invent repository state.
Separate files read, files changed, tests run, tests not run, proven facts, expected behavior, assumptions, unknowns, risks, rollback notes, next safe options, and human decisions required.
```

---

## 19. Bad AI Usage Patterns

Avoid these patterns.

### 1. The Everything Prompt

Bad:

```text
Read the project, fix the bug, refactor the architecture, add tests, verify everything, and tell me if it's ready.
```

Why bad:

- mixes roles;
- encourages broad edits;
- creates false confidence;
- hides missing evidence.

---

### 2. The Confidence Trap

Bad:

```text
Are we production-ready?
```

Better:

```text
Given the files and test output reviewed in this session, what is proven, what is expected, and what remains unknown about production readiness?
```

---

### 3. The Memory Trap

Bad:

```text
Continue from last time.
```

Better:

```text
Use the prior handoff only as ASSUMED context. Re-read the files you plan to modify before proposing edits.
```

---

### 4. The Broad Refactor Trap

Bad:

```text
Clean up this module.
```

Better:

```text
Identify one small, reversible cleanup that reduces risk without changing runtime behavior. Do not patch until relevant files are read.
```

---

### 5. The Hidden Activation Trap

Bad:

```text
Add the new worker and wire it in.
```

Better:

```text
Draft the worker scaffold only. Do not activate runtime scheduling, queues, external calls, or data writes without a separate approval and verification pass.
```

---

## 20. The Solo Owner Decision Rule

AI can multiply output, but the human owns judgment.

Before accepting AI work, the human should ask:

1. Did the model read the relevant files?
2. Did it distinguish evidence from assumption?
3. Is the change small enough?
4. Is the risk level correct?
5. Are side effects explicit?
6. Are tests appropriate?
7. Is rollback clear?
8. Is there any hidden activation?
9. Are secrets or private data involved?
10. Would I be comfortable reviewing this diff tomorrow?

If the answer is unclear, slow down.

---

## 21. Architecture Growth Rule

Do not scale architecture because AI suggests a sophisticated pattern.

Scale architecture because evidence shows the current structure is unsafe, unclear, expensive, or unable to evolve.

Avoid by default:

- microservices;
- framework rewrites;
- agent meshes;
- distributed data stores;
- external queues;
- search clusters;
- multi-server splits;
- autonomous operational agents.

Prefer first:

- module boundaries;
- repository interfaces;
- characterization tests;
- simple contracts;
- static checks;
- explicit seams;
- better observability;
- reversible configuration;
- deletion of unnecessary complexity.

Expansion is justified by evidence such as:

- measured performance bottlenecks;
- repeated incidents;
- security boundaries;
- compliance constraints;
- independent deployment needs;
- ownership separation;
- data lifecycle differences;
- failure isolation needs.

---

## 22. AI-in-Product Rule

If the product itself uses AI, treat it as a high-risk feature until proven otherwise.

Review:

- what data is sent to models;
- whether data is sensitive;
- whether users consent;
- provider retention policies;
- prompt injection risk;
- output validation;
- human oversight;
- audit logs;
- cost/rate limits;
- fallback behavior;
- whether AI can trigger actions.

AI output should not directly perform sensitive actions.

Sensitive actions include:

- payments;
- legal decisions;
- medical decisions;
- permission changes;
- production mutations;
- destructive actions;
- irreversible communication;
- security decisions.

AI output is untrusted until validated.

---

## 23. Security and Secrets Rule

AI must not become a place where secrets live.

Never paste:

- API keys;
- passwords;
- `.env` values;
- private keys;
- tokens;
- production connection strings;
- payment credentials;
- real user data;
- production dumps.

If a secret appears:

1. stop;
2. redact;
3. do not repeat it;
4. rotate where appropriate;
5. check Git history and logs if exposed;
6. continue only with placeholders.

Use synthetic data by default.

---

## 24. Release and Deployment Rule

Repository readiness is not deployment readiness.

Deployment depends on:

- environment;
- configuration;
- secrets management;
- infrastructure;
- data state;
- migrations;
- CI/CD;
- observability;
- rollback;
- human approval;
- operational capacity.

AI may help draft release checklists.

AI must not claim deployment success without deployment evidence.

AI must not execute production deployment as default workflow.

---

## 25. The Durable Project Rule

A durable AI-assisted project should optimize for:

- clarity;
- reversibility;
- evidence;
- tests;
- boundaries;
- small patches;
- explicit decisions;
- low secret exposure;
- low hidden side effects;
- accurate handoffs;
- simple architecture;
- recovery paths.

Not for:

- impressive-looking complexity;
- giant AI-generated rewrites;
- unreviewed velocity;
- hidden automation;
- undocumented assumptions;
- confidence without evidence.

---

## 26. Maturity Levels

A solo AI workflow can mature gradually.

### M0 — Ad Hoc

- prompts are informal;
- little verification;
- AI memory used as truth;
- risky.

Goal: leave this level quickly.

---

### M1 — Basic Discipline

- repository treated as source of truth;
- AI reads before editing;
- patches are smaller;
- no secrets pasted.

Good for small projects.

---

### M2 — Role-Based Workflow

- Architect / Executor / Verifier / Scribe separated;
- risk levels used;
- handoffs written;
- tests considered.

Good for serious solo projects.

---

### M3 — Evidence-Driven Workflow

- verification ladder used;
- CI/test output reviewed;
- diffs are central;
- mutable context separated;
- security checks added.

Good for durable products.

---

### M4 — Operational Discipline

- release checklists;
- rollback planning;
- observability;
- dependency scanning;
- secret scanning;
- production changes human-controlled.

Good for real users and production systems.

---

### M5 — Long-Term Engineering System

- architecture evolves by evidence;
- AI-in-product governed;
- security and privacy reviewed;
- incident learning captured;
- automation supports governance;
- documentation stays honest.

Good for large, long-lived systems.

---

## 27. The Video Teaching Path

A good teaching sequence for this method:

1. AI is speed, not truth.
2. The repository is the source of truth.
3. AI outputs are claims.
4. Evidence grades: proven, expected, assumed, unknown.
5. Roles: Architect, Reader, Executor, Verifier, Scribe, Operator.
6. Risk levels.
7. Reading before patching.
8. Small reversible patches.
9. Verification ladder.
10. Stable vs mutable context.
11. Security, secrets, and privacy.
12. Git and diffs as evidence.
13. Runtime activation and deployment boundaries.
14. AI inside the product.
15. How one person works like a small disciplined team.
16. How to grow architecture without overengineering.
17. How to build systems that survive beyond the current chat.

Main message:

> The future is not one human asking AI to do everything.
> The future is one human using AI inside a disciplined evidence-based operating system.

---

## 28. Final Operating Principle

The best solo AI engineer is not the person who gets the model to generate the most code.

The best solo AI engineer is the person who can reliably decide:

- what should be changed;
- what should not be changed;
- what is known;
- what is unknown;
- what is risky;
- what is reversible;
- what requires human approval;
- what must be verified before trust.

AI should increase capability without weakening judgment.

That is the method.
