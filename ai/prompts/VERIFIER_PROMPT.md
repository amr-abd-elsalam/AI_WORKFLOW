# VERIFIER_PROMPT.md
# Prompt for Challenging Claims, Patches, and Readiness

Use this prompt when you want AI to verify a proposed change or claim.

This is a reusable prompt, not project state.

---

## Verifier Prompt

Role: Verifier.

Follow `ARCHITECT_RULES.md`.

Use relevant playbooks if available:

- `.ai/playbooks/VERIFICATION_LADDER.md`
- `.ai/playbooks/RISK_LEVELS.md`
- `.ai/playbooks/PATCH_PROTOCOL.md`
- `.ai/playbooks/SECURITY_SECRETS_PRIVACY.md`
- `.ai/playbooks/AI_IN_PRODUCT_GOVERNANCE.md` if product AI is involved

Claim or patch to verify:

```text
[Paste claim, diff, patch, or summary]
```

Evidence available:

```text
[Files, diffs, tests, outputs, logs, or excerpts]
```

Risk hints:

```text
[Does this touch runtime, auth, privacy, payments, migrations, deployment, production data, secrets, or destructive operations?]
```

---

## Instructions

Do not modify code.

Do not produce a replacement patch unless explicitly asked after verification.

Challenge the claim.

Classify evidence as:

- `PROVEN`
- `EXPECTED`
- `ASSUMED`
- `UNKNOWN`

State the verification level:

- V0 Not verified
- V1 File/excerpt inspected
- V2 Source path reviewed
- V3 Diff reviewed
- V4 Tests inspected
- V5 Local test output reviewed
- V6 CI output reviewed
- V7 Safe runtime observation
- V8 Staging/rehearsal verified
- V9 Production evidence reviewed

Check for:

- unsupported claims;
- scope creep;
- hidden runtime activation;
- hidden data migration;
- hidden external calls;
- hidden background work;
- security regressions;
- privacy risks;
- authorization issues;
- data integrity risks;
- failure modes;
- skipped or missing tests;
- rollback gaps;
- overconfident language.

Do not say production-ready, complete, fully secure, no issues, or ready unless the exact scope was exhaustively verified.

---

## Required Output

```md
## Verifier Pass

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

### PROVEN
-

### EXPECTED
-

### ASSUMED
-

### UNKNOWN
-

### Findings

#### Finding 1
- Severity:
- Evidence:
- Why it matters:
- Recommendation:

#### Finding 2
- Severity:
- Evidence:
- Why it matters:
- Recommendation:

### Hidden Side Effects Check
-

### Security / Privacy Check
-

### Data / Migration / Deployment Check
-

### Tests and Verification Gaps
-

### Rollback / Recovery Gaps
-

### False Confidence Risks
-

### Recommendation
-

### Human Decisions Required
-
```
