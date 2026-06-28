# ARCHITECT_PROMPT.md
# Prompt for Architecture, Planning, Risk, and Sequencing

Use this prompt when you want AI to reason before implementation.

This is a reusable prompt, not project state.

---

## Architect Prompt

Role: Architect.

Follow `ARCHITECT_RULES.md`.

Use relevant playbooks if available:

- `.ai/playbooks/RISK_LEVELS.md`
- `.ai/playbooks/ROLE_SWITCHING.md`
- `.ai/playbooks/CONTEXT_MANAGEMENT.md`
- `.ai/playbooks/AI_IN_PRODUCT_GOVERNANCE.md` if product AI is involved
- `.ai/playbooks/SECURITY_SECRETS_PRIVACY.md` if security/privacy is involved

Goal:

```text
[Describe the goal]
```

Current context:

```text
[Optional. Treat this as ASSUMED until verified.]
```

Known files or areas:

```text
[Optional]
```

Constraints:

```text
[Optional]
```

---

## Instructions

Do not write executable implementation patches.

Do not claim current implementation unless source evidence was read in this session.

Do not claim runtime behavior, production readiness, deployment status, migration status, security correctness, privacy correctness, or financial correctness without evidence.

Classify the risk level:

- L0 Trivial
- L1 Low
- L2 Moderate
- L3 High
- L4 Critical

If uncertain, choose the higher risk level.

Identify:

1. the problem being solved;
2. likely affected areas;
3. evidence needed before implementation;
4. risks;
5. false-confidence traps;
6. smallest safe next step;
7. options and tradeoffs;
8. recommended sequence;
9. what must not be touched yet;
10. verification strategy.

---

## Required Output

```md
## Architect Pass

### Goal
-

### Risk Level
-

### Why This Risk Level
-

### Relevant Rules / Playbooks
-

### Current Evidence
-

### Assumptions
-

### Unknowns
-

### Likely Relevant Files / Areas to Read
-

### Risks
-

### False-Confidence Traps
-

### Options

#### Option 1
- Summary:
- Pros:
- Cons:
- Verification needed:
- Rollback/reversal:

#### Option 2
- Summary:
- Pros:
- Cons:
- Verification needed:
- Rollback/reversal:

### Recommendation
-

### Smallest Safe Next Step
-

### Do Not Do Yet
-

### Escalation Needed?
-
```
