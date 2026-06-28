# Weekly Maintenance Checklist

Use this checklist periodically to keep a solo AI-assisted project durable and manageable.

This checklist is stable guidance, not project state.

---

## 1. Repository Hygiene

- [ ] Working tree state is understood.
- [ ] Uncommitted changes are intentional.
- [ ] No unrelated changes are mixed.
- [ ] Generated files are understood.
- [ ] Ignored files are appropriate.
- [ ] Temporary files are not committed.
- [ ] Large files/binaries are intentional.
- [ ] Documentation does not contain stale operational state.

Notes:

```text

```

---

## 2. Tests and CI

- [ ] Key tests pass or failures are documented.
- [ ] Skipped tests are intentional.
- [ ] Flaky tests are identified.
- [ ] High-risk paths have meaningful tests.
- [ ] Test data is synthetic or redacted.
- [ ] CI status is reviewed from actual output.
- [ ] Build/typecheck/lint status is known where relevant.

Notes:

```text

```

---

## 3. Security and Privacy

- [ ] No secrets are present in repo files.
- [ ] No secrets are present in docs or examples.
- [ ] No private user data is committed.
- [ ] Logs/tests/fixtures do not contain sensitive data.
- [ ] Dependency vulnerabilities are reviewed where tooling exists.
- [ ] Access control changes are understood.
- [ ] AI-related data flows are reviewed if applicable.

Notes:

```text

```

---

## 4. Dependencies and Supply Chain

- [ ] Dependency changes are intentional.
- [ ] Unused dependencies are identified.
- [ ] High-risk dependencies are reviewed.
- [ ] Lockfiles are consistent.
- [ ] Build scripts are understood.
- [ ] CI workflow permissions are least-privilege where possible.
- [ ] Dangerous workflow patterns are avoided.

Notes:

```text

```

---

## 5. Architecture

- [ ] Module boundaries remain understandable.
- [ ] Coupling pain points are identified.
- [ ] Repeated risky edits are noted.
- [ ] Areas needing characterization tests are identified.
- [ ] Premature expansion is avoided.
- [ ] Simplification opportunities are identified.
- [ ] Runtime activation points are explicit.

Notes:

```text

```

---

## 6. Data / Migrations

- [ ] Pending migrations are understood.
- [ ] Migration status is not assumed from static files.
- [ ] Data repair/import/backfill plans are not hidden in code.
- [ ] Rollback limitations are documented where relevant.
- [ ] Production data is not exposed to AI.
- [ ] Schema/runtime compatibility is reviewed where relevant.

Notes:

```text

```

---

## 7. Documentation and Context

- [ ] `ARCHITECT_RULES.md` remains stable and state-free.
- [ ] Playbooks remain stable and generally applicable.
- [ ] Mutable context files are current or marked stale.
- [ ] Handoffs do not overclaim.
- [ ] Docs distinguish intent from implemented behavior.
- [ ] Roadmap/plans are not mixed into stable rules.

Notes:

```text

```

---

## 8. AI Process Quality

- [ ] AI read files before suggesting edits.
- [ ] AI separated `PROVEN`, `EXPECTED`, `ASSUMED`, `UNKNOWN`.
- [ ] AI did not rely on memory as authority.
- [ ] AI did not self-approve material changes.
- [ ] Verification passes challenged claims.
- [ ] Risk levels were used.
- [ ] Escalations were made when needed.
- [ ] No hidden activation was accepted.

Notes:

```text

```

---

## 9. Operations Readiness

- [ ] Deployment assumptions are not treated as facts.
- [ ] Release process is understood.
- [ ] Rollback path is understood for recent changes.
- [ ] Observability is adequate for high-risk areas.
- [ ] No production operations were delegated to AI.
- [ ] Incident notes, if any, are stored outside stable governance files.

Notes:

```text

```

---

## 10. Next Safe Options

List up to three next safe actions:

1.

2.

3.

---

## 11. Human Decisions Needed

```text

```

---

## 12. Final Weekly Assessment

Choose one:

- [ ] Project state is understood within reviewed scope.
- [ ] Some risks need follow-up.
- [ ] High-risk issue requires escalation.
- [ ] Context is stale and needs cleanup.
- [ ] Insufficient evidence for assessment.

Assessment notes:

```text

```
