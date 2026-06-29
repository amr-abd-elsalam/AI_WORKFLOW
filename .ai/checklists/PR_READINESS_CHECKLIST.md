# PR Readiness Checklist

Use this checklist before opening, reviewing, or merging a pull request.

This checklist is stable guidance, not project state.

---

## 1. Purpose

- [ ] PR has one primary purpose.
- [ ] PR description explains why the change exists.
- [ ] Scope is clear.
- [ ] Non-goals are clear where relevant.
- [ ] Risk level is stated.
- [ ] Patch category is stated.

Notes:

```text

```

---

## 2. Diff Hygiene

- [ ] Diff was reviewed.
- [ ] No unrelated files are changed.
- [ ] No generated files are hidden.
- [ ] No formatting churn unless intentional.
- [ ] No dependency changes unless intentional and approved.
- [ ] No large rewrite unless explicitly justified.
- [ ] No debug code left behind.
- [ ] No temporary comments or TODOs that should not ship.

Notes:

```text

```

---

## 3. Evidence

- [ ] Relevant files were read.
- [ ] Files not read but needed are listed explicitly.
- [ ] Repository access mode is stated.
- [ ] Prior handoffs, summaries, and AI memory are treated as `ASSUMED`, not source truth.
- [ ] Relevant tests were read or added where needed.
- [ ] Actual test output is available or lack of it is stated.
- [ ] CI status is known from actual CI output, not assumed.
- [ ] Skipped/failing tests are disclosed.
- [ ] Documentation claims match source or are marked as intent.
- [ ] Evidence is separated where needed into `PROVEN`, `EXPECTED`, `ASSUMED`, and `UNKNOWN`.

Notes:

```text

```

---

## 4. Tests

- [ ] Relevant unit tests were run or not-run status is stated.
- [ ] Relevant integration tests were run or not-run status is stated.
- [ ] Typecheck/lint/build checks were run where applicable.
- [ ] Tests cover expected success path where relevant.
- [ ] Tests cover failure path where relevant.
- [ ] High-risk behavior has appropriate test coverage or explicit risk acceptance.
- [ ] No test relies on secrets or production data.
- [ ] No test mutates real data.

Notes:

```text

```

---

## 5. Runtime and Side Effects

- [ ] Runtime behavior change is clearly described.
- [ ] No hidden activation.
- [ ] No hidden external calls.
- [ ] No hidden database writes.
- [ ] No hidden queues/jobs/schedulers.
- [ ] No hidden feature flags.
- [ ] Config changes are described.
- [ ] Backward compatibility is considered.

Notes:

```text

```

---

## 6. Security / Privacy

- [ ] No secrets are included.
- [ ] No private user data is included.
- [ ] Auth/authz impact is reviewed where relevant.
- [ ] Sensitive logs are avoided.
- [ ] External data sharing is reviewed.
- [ ] Dependency/security implications are reviewed.
- [ ] AI-related security is reviewed if applicable.

Notes:

```text

```

---

## 7. Data / Migration

- [ ] No migration is included, or migration is explicitly reviewed.
- [ ] No data mutation is hidden.
- [ ] Backfill/import/repair behavior is not included unless approved.
- [ ] Rollback implications are understood.
- [ ] Production data is not touched by the PR itself.

Notes:

```text

```

---

## 8. Documentation

- [ ] Docs updated if behavior changed.
- [ ] Docs do not overclaim readiness.
- [ ] Docs distinguish intent from implemented behavior where needed.
- [ ] Handoff or PR notes include what remains unverified.

Notes:

```text

```

---

## 9. Role Handoff

- [ ] PR notes include `Prompt For Next Role` when another AI pass is needed.
- [ ] The next role is appropriate for the risk and evidence level.
- [ ] The next-role prompt lists files already read.
- [ ] The next-role prompt lists files the next role must read before acting.
- [ ] The next-role prompt preserves `PROVEN`, `EXPECTED`, `ASSUMED`, and `UNKNOWN` without inflating certainty.
- [ ] Human-only Operator decisions are listed as decisions or checklist items, not delegated to AI.

Notes:

```text

```

---

## 10. Merge Decision

Choose one:

- [ ] Ready to open PR.
- [ ] Ready for human review.
- [ ] Ready to merge within reviewed scope.
- [ ] Needs changes.
- [ ] Needs escalation.
- [ ] Insufficient evidence.

Decision notes:

```text

```
