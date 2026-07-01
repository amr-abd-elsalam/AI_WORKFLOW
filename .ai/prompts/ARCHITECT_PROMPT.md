# ARCHITECT_PROMPT.md
# Prompt for Architecture, Planning, Risk, and Sequencing

Use this prompt when you want AI to reason before implementation.

This is a reusable prompt, not project state.

---

## Architect Prompt

Role: Architect.

Follow `ARCHITECT_RULES.md`.

Use relevant playbooks if available:

- `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md`
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

## Architect Pass

### Role
Architect

### Task
-

### Risk Level
-

### Why This Risk Level
-

### Repository Access Mode
- Direct tool access / Pasted excerpts only / No file access / Unknown

### Relevant Rules / Playbooks
-

### Files Read
-

### Files Not Read But Needed
-

### Evidence Status

#### PROVEN
-

#### EXPECTED
-

#### ASSUMED
-

#### UNKNOWN
-

### Constraints
-

### What I Must Not Do
-

### Output Produced

#### Problem Being Solved
-

#### Likely Affected Areas
-

#### Evidence Needed Before Implementation
-

#### Risks
-

#### False-Confidence Traps
-

#### Options

##### Option 1
- Summary:
- Pros:
- Cons:
- Verification needed:
- Rollback/reversal:

##### Option 2
- Summary:
- Pros:
- Cons:
- Verification needed:
- Rollback/reversal:

#### Recommendation
-

#### Smallest Safe Next Step
-

#### Do Not Do Yet
-

### Verification Needed
-

### Escalation Needed?
-

### Next Role Recommendation
-

### Prompt For Next Role

```text
Role: Reader

Task:
Build an evidence map for this task before any implementation.

Repository access:
[Direct tool access / Pasted excerpts only / No file access / Unknown]

Files / context to send to next model:
[List planning context, evidence needs, recommended sequence, and relevant constraints. Do not present this as source authority.]

Files already read:
[List files read by Architect in this session]

Files you must re-read before acting:
[List exact files or areas identified by Architect]

Evidence from previous role:
PROVEN:
- [Directly supported evidence]

EXPECTED:
- [Expected but not directly observed]

ASSUMED:
- [Assumptions to verify]

UNKNOWN:
- [Unknowns to resolve]

Risk level:
[Risk level and reason]

Constraints:
[Scope limits and rules]

Do not:
- Do not propose patches.
- Do not rewrite code.
- Do not infer unread file contents.
- Do not treat this Architect pass as source authority.
- Do not claim runtime behavior, production readiness, deployment status, migration status, security correctness, privacy correctness, or financial correctness without evidence.

Required output:
Return a Reader Pass with these sections:
- Role
- Task
- Risk Level
- Repository Access Mode
- Files Read
- Files Not Read But Needed
- Evidence Status with PROVEN, EXPECTED, ASSUMED, UNKNOWN
- Relevant Runtime Paths
- Relevant Tests
- Relevant Config / Scripts / Migrations
- Docs or Contracts That Need Verification
- Missing Evidence
- Risks
- Recommended Next Role
- Smallest Safe Next Step
- Escalation Needed?
- Prompt For Next Role
```
