# Patch Review Checklist

Use this checklist before accepting or applying an AI-generated patch.

This checklist is stable guidance, not project state.

---

## 1. Scope

- [ ] The patch has one primary purpose.
- [ ] The patch category is stated.
- [ ] The risk level is stated.
- [ ] The change is tied to a confirmed requirement, bug, or risk.
- [ ] No unrelated refactor is included.
- [ ] No formatting churn is included unless requested.
- [ ] No generated-file changes are hidden.

Notes:

```text

```

---

## 2. Evidence

- [ ] The AI listed files read.
- [ ] Every edited file was read in the current session.
- [ ] Relevant callers/dependencies were read where needed.
- [ ] Relevant tests were read where needed.
- [ ] Relevant configs/scripts/migrations were read where needed.
- [ ] Files not read but needed are listed explicitly.
- [ ] Any unread but relevant files are listed as unknown.
- [ ] Repository access mode is stated.
- [ ] Prior handoffs or summaries are treated as `ASSUMED`, not source truth.

Notes:

```text

```

---

## 3. Patch Format

- [ ] Patch uses `Output Patch Rules — Strict`.
- [ ] Existing file edits use exact `FIND/REPLACE` blocks.
- [ ] `FIND` blocks appear exact and unique.
- [ ] `FIND` blocks are the smallest unique blocks that safely locate the edits.
- [ ] No ellipses are used in `FIND` or `REPLACE`.
- [ ] New files are provided in full.
- [ ] Deletions are explicit and justified.
- [ ] Unsafe edits with insufficient context request the exact file instead of guessing.
- [ ] Paths, identifiers, commands, and code are in English.
- [ ] Explanatory prose is understandable to the human owner.

Notes:

```text

```

---

## 4. Side Effects

- [ ] Expected side effects are stated.
- [ ] No hidden runtime activation is included.
- [ ] No hidden feature flag is included.
- [ ] No hidden background job or scheduler is included.
- [ ] No hidden queue consumer is included.
- [ ] No hidden external call is included.
- [ ] No hidden database connection or write is included.
- [ ] No hidden dual-write is included.
- [ ] No hidden data migration is included.
- [ ] No dependency change is included without approval.

Notes:

```text

```

---

## 5. Security / Privacy

- [ ] No secrets are included.
- [ ] No private user data is included.
- [ ] No access is broadened silently.
- [ ] Authentication is not weakened.
- [ ] Authorization is not weakened.
- [ ] Sensitive values are not logged.
- [ ] Validation is not weakened.
- [ ] Security protections are not disabled unless clearly labeled `DEV-ONLY / INSECURE`.

Notes:

```text

```

---

## 6. Verification

- [ ] Suggested verification is provided.
- [ ] Tests/checks run are stated.
- [ ] Tests/checks not run are stated.
- [ ] Evidence is separated into `PROVEN`, `EXPECTED`, `ASSUMED`, and `UNKNOWN`.
- [ ] The verification level matches the claim.
- [ ] Passing tests are not overstated.
- [ ] No production-readiness claim is made without production evidence.

Notes:

```text

```

---

## 7. Rollback

- [ ] Rollback or reversal is stated.
- [ ] For L0/L1, simple revert is enough.
- [ ] For L2, affected files and reversal are clear.
- [ ] For L3/L4, rollback considers data, config, runtime activation, and human approval.

Notes:

```text

```

---

## 8. Role Output Contract

- [ ] The output includes `Prompt For Next Role` when another AI pass is needed.
- [ ] The next role is appropriate for the current evidence and risk.
- [ ] The next-role prompt lists files already read.
- [ ] The next-role prompt lists files the next role must read before acting.
- [ ] The next-role prompt transfers `PROVEN`, `EXPECTED`, `ASSUMED`, and `UNKNOWN` without inflating certainty.
- [ ] The next-role prompt states what the next role must not do.
- [ ] If the next step is human-only Operator work, AI provides a decision packet or checklist instead of becoming Operator.

Notes:

```text

```

---

## 9. Decision

Choose one:

- [ ] Accept within reviewed scope.
- [ ] Accept after small changes.
- [ ] Request changes.
- [ ] Escalate before proceeding.
- [ ] Reject.

Decision notes:

```text

```
