# Release Readiness Checklist

Use this checklist before release or deployment planning.

This checklist does not authorize deployment.

AI must not execute production deployment as default workflow.

---

## 1. Scope

- [ ] Release scope is defined.
- [ ] Included changes are listed.
- [ ] Excluded changes are listed where relevant.
- [ ] Target environment is identified.
- [ ] Risk level is stated.
- [ ] Human approval requirement is clear.

Notes:

```text

```

---

## 2. Repository Evidence

- [ ] Branch/commit/tag is known from Git evidence.
- [ ] Working tree status is known if relevant.
- [ ] Diff or PR was reviewed.
- [ ] No unrelated changes are included.
- [ ] Generated files are understood.
- [ ] Dependency changes are understood.
- [ ] Release notes are drafted or updated.

Notes:

```text

```

---

## 3. Tests and CI

- [ ] Unit tests passed or not-run status is stated.
- [ ] Integration tests passed or not-run status is stated.
- [ ] E2E tests passed or not-run status is stated where relevant.
- [ ] Build passed or not-run status is stated.
- [ ] Lint/typecheck passed or not-run status is stated.
- [ ] CI output was reviewed directly.
- [ ] Skipped/flaky/failing tests are disclosed.
- [ ] Test scope matches release risk.

Notes:

```text

```

---

## 4. Security / Privacy

- [ ] No secrets included.
- [ ] Secret handling is unchanged or reviewed.
- [ ] Auth/authz changes are reviewed.
- [ ] User data handling is reviewed.
- [ ] Logging does not expose sensitive data.
- [ ] Dependency/security scanning reviewed where applicable.
- [ ] AI feature risks reviewed where applicable.

Notes:

```text

```

---

## 5. Configuration / Environment

- [ ] Required config changes are listed.
- [ ] No secret values are pasted.
- [ ] Feature flags are listed.
- [ ] Runtime activation is explicit.
- [ ] Environment differences are considered.
- [ ] Backward compatibility is considered.
- [ ] Rollout strategy is described if needed.

Notes:

```text

```

---

## 6. Data / Migration

- [ ] No migration is needed, or migration plan is reviewed.
- [ ] Migration execution is human-approved if production.
- [ ] Backup/snapshot plan exists if data risk exists.
- [ ] Rollback/recovery plan exists.
- [ ] Data integrity checks are planned.
- [ ] Post-migration checks are listed.

Notes:

```text

```

---

## 7. Observability

- [ ] Logs/metrics/traces are sufficient for changed area.
- [ ] Error monitoring is available where relevant.
- [ ] Alerting is considered for high-risk changes.
- [ ] Post-release checks are defined.
- [ ] Known failure signals are listed.

Notes:

```text

```

---

## 8. Rollback / Recovery

- [ ] Rollback method is known.
- [ ] Rollback owner is human.
- [ ] Data rollback limitations are stated.
- [ ] Config rollback is considered.
- [ ] Feature flag rollback is considered if applicable.
- [ ] Recovery plan exists for partial failure.

Notes:

```text

```

---

## 9. Deployment Boundary

- [ ] AI is not executing deployment.
- [ ] Human approval is explicit.
- [ ] Deployment command/process is known to the human.
- [ ] Production access is controlled.
- [ ] No secrets are exposed to AI.
- [ ] No production mutation is casually recommended.

Notes:

```text

```

---

## 10. Decision

Choose one:

- [ ] Not enough evidence to proceed.
- [ ] Proceed only after blockers are resolved.
- [ ] Ready for staging/rehearsal.
- [ ] Ready for human-approved production release within reviewed scope.
- [ ] Release blocked.

Decision notes:

```text

```
