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

- `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md`
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

````md
## Release / Deployment Readiness Review

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

### Scope Reviewed
-

### Evidence Reviewed
-

### Evidence Not Reviewed
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

#### Change Scope
-

#### Tests / CI
-

#### Security / Privacy
-

#### Data / Migration
-

#### Config / Secrets
-

#### Dependencies / Supply Chain
-

#### Observability / Monitoring
-

#### Rollback / Recovery
-

#### Human Approvals Needed
-

#### Blockers
-

#### Non-Blocking Risks
-

#### Recommended Pre-Release Checklist
1.
2.
3.

#### Recommended Post-Release Checks
1.
2.
3.

#### Recommendation

Choose one:

- Not enough evidence to proceed
- Proceed only after listed blockers are resolved
- Proceed with human approval and stated risks
- Ready only within the reviewed non-production scope

### Verification Needed
-

### Escalation Needed?
-

### Next Role Recommendation
-

### Prompt For Next Role Or Human Decision Packet

```text
Role: [Reader / Architect / Verifier / Handoff Scribe / Human Operator decision packet]

Task:
[State the exact next task. If evidence is missing, ask Reader to gather it. If scope or risk needs replanning, ask Architect. If another readiness challenge is needed, ask Verifier. If the review should be preserved, ask Handoff Scribe. If the next step is release/deployment execution, provide a Human Operator decision packet instead of assigning AI as Operator.]

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
[List release-check findings, reviewed evidence, recommendation scope, human decision packet context, and relevant constraints. Do not present this as source authority.]

Files already read:
[List files read during this release check]

Files you must re-read before acting:
[List files, diffs, CI outputs, test outputs, release notes, migration plans, rollback plans, configs, or checklists the next role must re-read before making claims.]

Evidence from previous role:
PROVEN:
- [Directly supported release-check evidence]

EXPECTED:
- [Expected but not directly observed]

ASSUMED:
- [Assumptions that must not be promoted to facts]

UNKNOWN:
- [Unknowns that remain after release check]

Risk level:
[Risk level and reason]

Verification level:
[Verification level and reviewed scope]

Release recommendation:
[One of the allowed recommendation choices, with scope]

Constraints:
[Scope limits, approvals, no-go areas, and rules]

Do not:
- Do not execute deployment.
- Do not claim deployment happened unless deployment evidence is reviewed.
- Do not claim CI passed unless actual CI output is reviewed.
- Do not claim production readiness beyond reviewed evidence.
- Do not treat this readiness review as approval to operate.
- Do not convert assumptions, expected behavior, plans, or checklists into completed facts.
- Do not assign AI as Operator. Operator is human-only.

Required output:
If Role is Reader, return a Reader Pass focused only on missing release evidence and include Prompt For Next Role.

If Role is Architect, return an Architect Pass focused on release risk, sequencing, rollback, and no-go boundaries. Include Prompt For Next Role.

If Role is Verifier, return a Verifier Pass challenging a specific release claim or evidence packet. Include Prompt For Next Role.

If Role is Handoff Scribe, return an AI Handoff that separates files read, files changed or proposed, verification level, PROVEN, EXPECTED, ASSUMED, UNKNOWN, risks, next safe options, and human decisions. Include a next-session prompt.

If this is a Human Operator decision packet, include:
- Decision needed
- Evidence reviewed
- Evidence missing
- Risk level
- Blockers
- Required approvals
- Required backup / rollback / recovery notes
- Dry-run or read-only checks available
- Explicit no-go conditions
- Post-action evidence the human should collect
```
````
