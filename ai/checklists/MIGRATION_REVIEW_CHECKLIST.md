# Migration Review Checklist

Use this checklist for database migrations, schema changes, backfills, imports, repairs, or data-shape changes.

This checklist is stable guidance, not project state.

AI must not execute production migrations.

---

## 1. Scope and Classification

- [ ] Migration/change purpose is clear.
- [ ] Risk level is stated.
- [ ] Environment is identified.
- [ ] Production execution is not being performed by AI.
- [ ] Human approval is required for production or irreversible operations.
- [ ] Data affected is described.
- [ ] Tables/collections/indexes affected are identified.

Notes:

```text

```

---

## 2. Source Review

- [ ] Migration file was read.
- [ ] Schema references were read.
- [ ] Runtime code using affected schema was read where relevant.
- [ ] Tests were read or planned.
- [ ] Scripts/backfills were read where relevant.
- [ ] Guards/safety checks were read where relevant.
- [ ] Rollback/down migration was reviewed if present.

Notes:

```text

```

---

## 3. Safety

- [ ] Migration is not destructive, or destructive impact is explicit and approved.
- [ ] No production connection string is exposed.
- [ ] No production data dump is used.
- [ ] No real user data is included in prompts/docs/tests.
- [ ] Large table impact is considered.
- [ ] Locking/performance impact is considered.
- [ ] Timeout/retry behavior is considered.
- [ ] Idempotency is considered.
- [ ] Partial failure behavior is considered.

Notes:

```text

```

---

## 4. Data Integrity

- [ ] Existing data compatibility is considered.
- [ ] Defaults/nullability are considered.
- [ ] Constraints are considered.
- [ ] Indexes are considered.
- [ ] Foreign keys/relations are considered.
- [ ] Uniqueness conflicts are considered.
- [ ] Backward compatibility with old code is considered.
- [ ] Forward compatibility with new code is considered.

Notes:

```text

```

---

## 5. Backfill / Import / Repair

If applicable:

- [ ] Operation is explicitly approved.
- [ ] Dry-run mode exists or is planned.
- [ ] Read-only inspection can be performed first.
- [ ] Batch size is considered.
- [ ] Resume/retry behavior is considered.
- [ ] Duplicate processing is handled.
- [ ] Audit/logging is considered.
- [ ] Rollback or compensation is considered.
- [ ] Production execution is human-controlled.

Notes:

```text

```

---

## 6. Verification

- [ ] Migration was reviewed statically.
- [ ] Migration was tested locally or not-run status is stated.
- [ ] Migration was tested in staging/rehearsal if needed.
- [ ] Tests cover runtime code using changed schema where relevant.
- [ ] Failure path is considered.
- [ ] Verification level is stated.
- [ ] Migration execution is not claimed unless actual evidence exists.

Notes:

```text

```

---

## 7. Rollback / Recovery

- [ ] Rollback path exists or limitation is stated.
- [ ] Backup/snapshot plan exists for production.
- [ ] Recovery plan exists.
- [ ] Data loss risk is stated.
- [ ] Human approval is required before production execution.
- [ ] Post-migration checks are listed.

Notes:

```text

```

---

## 8. Decision

Choose one:

- [ ] Safe to keep as static migration draft only.
- [ ] Safe for local/dev testing.
- [ ] Safe for staging rehearsal.
- [ ] Production execution requires further approval.
- [ ] Blocked due to missing rollback/recovery.
- [ ] Blocked due to data integrity risk.
- [ ] Insufficient evidence.

Decision notes:

```text

```
