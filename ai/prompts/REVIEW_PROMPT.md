# REVIEW_PROMPT.md
# Prompt for Reviewing a Diff, PR, or Proposed Change

Use this prompt when you want AI to review a change like a careful engineer.

This is a reusable prompt, not project state.

---

## Review Prompt

Role: Verifier.

Follow `ARCHITECT_RULES.md`.

Use relevant playbooks if available:

- `.ai/playbooks/VERIFICATION_LADDER.md`
- `.ai/playbooks/RISK_LEVELS.md`
- `.ai/playbooks/PATCH_PROTOCOL.md`
- `.ai/playbooks/SECURITY_SECRETS_PRIVACY.md`
- `.ai/playbooks/AI_IN_PRODUCT_GOVERNANCE.md` if product AI is involved

Change to review:

```text
[Paste diff, PR summary, patch, or file excerpts]
```

Context:

```text
[Optional. Treat as ASSUMED unless verified.]
```

Tests/checks output:

```text
[Optional. Paste actual output if available.]
```

---

## Instructions

Review only what is provided or read.

Do not assume the working tree is clean.

Do not assume CI passed.

Do not assume deployment happened.

Do not approve readiness beyond evidence.

Classify issues by severity:

- `BLOCKER`
- `HIGH`
- `MEDIUM`
- `LOW`
- `NIT`
- `QUESTION`

Look for:

- correctness bugs;
- scope creep;
- hidden activation;
- hidden side effects;
- security issues;
- privacy issues;
- auth/permission issues;
- data integrity issues;
- migration risks;
- deployment assumptions;
- missing tests;
- brittle tests;
- rollback gaps;
- misleading documentation;
- overconfident claims.

---

## Required Output

```md
## Review

### Role
Verifier

### Risk Level
-

### Verification Level
-

### Evidence Reviewed
-

### Evidence Not Reviewed
-

### Summary
-

### Findings

#### 1. [Severity] Title
- Evidence:
- Why it matters:
- Recommendation:

#### 2. [Severity] Title
- Evidence:
- Why it matters:
- Recommendation:

### Positive Notes
-

### Tests / Checks Reviewed
-

### Tests / Checks Missing
-

### Security / Privacy Review
-

### Data / Migration / Deployment Review
-

### False Confidence Risks
-

### Required Human Decisions
-

### Recommendation

Choose one:

- Accept within reviewed scope
- Accept after small changes
- Request changes
- Escalate before proceeding
- Insufficient evidence to review
```
