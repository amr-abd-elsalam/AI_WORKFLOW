# Risk Levels Playbook

This playbook explains how to apply risk-proportional governance.

It is stable guidance, not project state.

---

## Principle

Do not apply the same process weight to every change.

A typo, CSS adjustment, validation change, authentication change, payment mutation, and production migration do not deserve the same workflow.

When uncertain, classify the task at the higher risk level.

---

## L0 — Trivial

### Examples

- Typo fix.
- Formatting-only change.
- Comment wording with no behavioral claim.
- Non-authoritative wording cleanup.

### Required AI behavior

- Read the target text.
- Keep the change minimal.
- Avoid runtime claims.
- Compact output is acceptable.

### Verification

Usually enough:

- target file inspected;
- exact edit provided;
- no runtime behavior claimed.

### Avoid saying

- "This is fully correct."
- "No impact."
- "Ready."

Say instead:

- "This appears limited to wording in the reviewed file."

---

## L1 — Low Risk

### Examples

- Docs-only change.
- Test-only change that does not alter helpers used broadly.
- CSS-only change.
- Local cleanup with no intended runtime behavior change.
- Metadata update with no deployment implication.

### Required AI behavior

- Read target file.
- Read referenced file if the doc makes factual claims.
- Avoid broad refactors.
- State what was not verified.

### Verification

Suggested:

- inspect file;
- if docs mention runtime behavior, check source or mark as unverified;
- run relevant lightweight checks if available.

---

## L2 — Moderate Risk

### Examples

- Limited runtime behavior change.
- Validation logic.
- Error handling.
- Internal API change.
- Small refactor intended to preserve behavior.
- Config default for local/dev behavior.
- New non-sensitive test fixture.

### Required AI behavior

- Read target file.
- Read direct callers and direct dependencies when material.
- Read relevant tests.
- Identify expected side effects.
- Suggest verification.

### Verification

Suggested:

- relevant unit tests;
- typecheck/lint if applicable;
- focused manual review of affected path;
- note untested edge cases.

### Escalate if

- auth, privacy, payments, migrations, deployment, production data, or external calls appear.

---

## L3 — High Risk

### Examples

- Authentication.
- Authorization.
- User data access.
- Privacy-sensitive logic.
- External service calls.
- Background jobs.
- Queue behavior.
- Schedulers.
- Runtime feature flags.
- Database writes.
- Non-production migrations.
- Config affecting runtime behavior.
- Logging changes that may expose data.
- Dependency addition touching runtime.

### Required AI behavior

- Explicitly state risk level.
- Read broader context.
- Review failure modes.
- Review security/privacy implications.
- Avoid hidden activation.
- Provide rollback notes.
- Require human approval for activation-sensitive changes.

### Verification

Suggested:

- unit tests for success and failure;
- integration tests where relevant;
- authorization checks;
- idempotency checks;
- data integrity checks;
- logging/privacy review;
- config review;
- rollback/recovery review.

### Escalate if

- production, payments, destructive actions, secrets, deployment, or irreversible changes appear.

---

## L4 — Critical

### Examples

- Production migration.
- Production data mutation.
- Payment, ledger, invoice, receipt, or financial state mutation.
- Deployment or rollback.
- Secrets rotation.
- Editing deployment secrets.
- Destructive database operation.
- Queue drain against real data.
- Bulk repair against real data.
- Killing production processes.
- Force push to shared/protected branch.
- Any irreversible or hard-to-recover operation.

### Required AI behavior

AI must not execute.

AI may help draft:

- risk assessment;
- read-only inspection plan;
- dry-run plan;
- backup checklist;
- rollback plan;
- human approval checklist;
- communication plan.

### Mandatory conditions before human execution

- explicit human decision;
- safe environment confirmation;
- risk acceptance;
- backup/recovery plan;
- rollback plan;
- human-controlled execution;
- redacted outputs only.

### Verification

Requires evidence appropriate to the operation.

Do not claim success without actual, reviewed execution evidence.
