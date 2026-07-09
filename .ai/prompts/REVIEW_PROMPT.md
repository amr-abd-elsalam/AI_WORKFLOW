# REVIEW_PROMPT.md
# Prompt for Reviewing a Diff, PR, or Proposed Change

Use this prompt when you want AI to review a change like a careful engineer.

This is a reusable prompt, not project state.

---

## Review Prompt

Role: Verifier.

Follow `ARCHITECT_RULES.md`.

Use relevant playbooks if available:

- `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md`
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

Start with a Source-Truth Phase Review:

- identify the claimed source of truth;
- identify which files, diffs, tests, logs, outputs, or Git evidence were actually reviewed;
- identify which handoff, memory, summary, or prior AI claims are not source authority;
- identify which files or evidence must be re-read before accepting the claim;
- state the highest verification level supported by the reviewed evidence.

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

````md
## Review

### Role
Verifier

### Task
-

### Risk Level
-

### Why This Risk Level
-

### Verification Level
-

### Repository Access Mode
- Direct tool access / Pasted excerpts only / No file access / Unknown

### Relevant Rules / Playbooks
-

### Evidence Reviewed
-

### Evidence Not Reviewed
-

### Source-Truth Phase Review
-

### Files Read
-

### Files Not Read But Needed
-

### Constraints
-

### What I Must Not Do
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

### Output Produced

#### Summary
-

#### Findings

##### 1. [Severity] Title
- Evidence:
- Why it matters:
- Recommendation:

##### 2. [Severity] Title
- Evidence:
- Why it matters:
- Recommendation:

#### Positive Notes
-

#### Tests / Checks Reviewed
-

#### Tests / Checks Missing
-

#### Security / Privacy Review
-

#### Data / Migration / Deployment Review
-

#### False Confidence Risks
-

#### Required Human Decisions
-

#### Recommendation

Choose one:

- Accept within reviewed scope
- Accept after small changes
- Request changes
- Escalate before proceeding
- Insufficient evidence to review

### Verification Needed
-

### Escalation Needed?
-

### Next Role Recommendation
-

### Prompt For Next Role

```text
Role: [Executor / Reader / Architect / Handoff Scribe]
Canonical prompt file for this role: [`.ai/prompts/EXECUTOR_PROMPT.md` / `.ai/prompts/READER_PROMPT.md` / `.ai/prompts/ARCHITECT_PROMPT.md` / `.ai/prompts/HANDOFF_PROMPT.md`]

Task:
[State the exact next task. If findings require changes, ask Executor for a minimal correction patch. If evidence is missing, ask Reader to gather the missing evidence. If scope or risk needs replanning, ask Architect. If accepted within reviewed scope, ask Handoff Scribe to record an accurate handoff.]

Repository Context Packet:
- Workflow repository URL: [workflow repository URL or UNKNOWN]
- Target repository URL: [target repository URL or UNKNOWN]
- Original human problem statement: [original human problem statement or UNKNOWN]
- Language preference: [language preference or UNKNOWN]
- Repository access mode: [Direct tool access / Pasted excerpts only / No file access / Unknown]
- Risk level: [risk level and reason]
- Constraints: [scope limits and rules]
- Evidence status: [Summarize; preserve PROVEN, EXPECTED, ASSUMED, UNKNOWN below]

Repository access:
[Direct tool access / Pasted excerpts only / No file access / Unknown]

Files / context to send to next model:
[List review findings, reviewed evidence, proposed correction scope, and relevant context. Do not present this as source authority.]

Files already read:
[List files read by Reviewer/Verifier in this session]

Files you must re-read before acting:
[List files the next role must re-read before acting. If Executor is next, include every file it may edit.]

Evidence from previous role:
PROVEN:
- [Directly supported evidence from review]

EXPECTED:
- [Expected but not directly observed]

ASSUMED:
- [Assumptions that must not be promoted to facts]

UNKNOWN:
- [Unknowns that remain after review]

Risk level:
[Risk level and reason]

Verification level:
[Verification level and reviewed scope]

Review findings to carry forward:
- [List findings, severities, evidence, and recommendations]

Constraints:
[Scope limits and rules]

Do not:
- Do not treat this review as broader than its reviewed scope.
- Do not claim CI passed unless actual CI output was reviewed.
- Do not claim deployment happened unless deployment evidence was reviewed.
- Do not claim production readiness, migration completion, full security, full privacy correctness, or complete correctness unless exhaustively verified for the exact stated scope.
- Do not convert assumptions or expected behavior into proven facts.
- If acting as Executor, do not broaden the patch beyond the reviewed findings.
- If acting as Handoff Scribe, do not turn review recommendations or unverified claims into completed facts.

Required output:
If Role is Executor, return a minimal correction Executor Pass using `Output Patch Rules — Strict` and include Prompt For Next Role.

If Role is Reader, return a Reader Pass focused only on missing evidence and include Prompt For Next Role.

If Role is Architect, return an Architect Pass focused on re-planning the unsafe or unclear scope and include Prompt For Next Role.

If Role is Handoff Scribe, return an AI Handoff that separates files read, files changed or proposed, verification level, PROVEN, EXPECTED, ASSUMED, UNKNOWN, risks, next safe options, and human decisions. Include a next-session prompt.
```
````
