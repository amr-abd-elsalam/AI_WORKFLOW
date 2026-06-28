# RELEASE_CHECK_PROMPT.md
# Prompt for Pre-Release or Deployment Readiness Review

Use this prompt before release or deployment planning.

This prompt does not authorize deployment.

This is a reusable prompt, not project state.

---

## Release Check Prompt

Role: Verifier.

Follow `ARCHITECT_RULES.md`.

Use relevant playbooks if available:

- `.ai/playbooks/RISK_LEVELS.md`
- `.ai/playbooks/VERIFICATION_LADDER.md`
- `.ai/playbooks/SECURITY_SECRETS_PRIVACY.md`
- `.ai/playbooks/AI_IN_PRODUCT_GOVERNANCE.md` if product AI is involved

Release or deployment target:

```text
[Describe target. Do not include secrets.]
```

Evidence available:

```text
[Diffs, commits, test output, CI output, release notes, migration plan, rollback plan]
```

Scope:

```text
[What is intended to be released]
```

Constraints:

```text
[Maintenance window, environment, approvals, no-go areas]
```

---

## Instructions

This is a readiness review, not deployment execution.

Do not execute deployment.

Do not claim deployment happened.

Do not claim production readiness beyond evidence.

Classify all evidence as:

- `PROVEN`
- `EXPECTED`
- `ASSUMED`
- `UNKNOWN`

Check:

- scope of changes;
- diffs reviewed;
- tests and CI;
- skipped/failing tests;
- configuration;
- secrets handling;
- migrations;
- data changes;
- dependencies;
- security/privacy;
- observability;
- rollback;
- human approvals;
- release notes;
- post-release checks.

If evidence is missing for a high-risk area, escalate.

---

## Required Output

```md
## Release / Deployment Readiness Review

### Role
Verifier

### Risk Level
-

### Verification Level
-

### Scope Reviewed
-

### Evidence Reviewed
-

### Evidence Missing
-

### PROVEN
-

### EXPECTED
-

### ASSUMED
-

### UNKNOWN
-

### Change Scope
-

### Tests / CI
-

### Security / Privacy
-

### Data / Migration
-

### Config / Secrets
-

### Dependencies / Supply Chain
-

### Observability / Monitoring
-

### Rollback / Recovery
-

### Human Approvals Needed
-

### Blockers
-

### Non-Blocking Risks
-

### Recommended Pre-Release Checklist
1.
2.
3.

### Recommended Post-Release Checks
1.
2.
3.

### Recommendation

Choose one:

- Not enough evidence to proceed
- Proceed only after listed blockers are resolved
- Proceed with human approval and stated risks
- Ready only within the reviewed non-production scope
```
