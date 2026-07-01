# HANDOFF_PROMPT.md
# Prompt for Accurate Session Handoffs

Use this prompt when ending a session or preparing context for the next AI/human pass.

This is a reusable prompt, not project state.

---

## Handoff Prompt

Role: Handoff Scribe.

Follow `ARCHITECT_RULES.md`.

Use relevant playbooks if available:

- `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md`
- `.ai/playbooks/HANDOFF_TEMPLATE.md`
- `.ai/playbooks/CONTEXT_MANAGEMENT.md`
- `.ai/playbooks/VERIFICATION_LADDER.md`

Task goal:

```text
[Describe the task]
```

Session evidence:

```text
[Files read, patches proposed, tests run, outputs, decisions]
```

Known unresolved items:

```text
[Optional]
```

---

## Instructions

Do not invent repository state.

Do not claim commits, branch state, CI, deployment, migration, or test status unless evidence is provided.

Do not include secrets or private data.

Separate:

- files read;
- files changed or proposed;
- tests run;
- tests not run;
- `PROVEN`;
- `EXPECTED`;
- `ASSUMED`;
- `UNKNOWN`;
- risks;
- next safe options;
- human decisions.

A handoff is not source authority. It is a map for the next session.

The `Prompt For Next Role` is a next-model transfer packet, not proof.

It must clearly separate:

- files and context to send to the next model;
- files the next model must re-read before acting;
- facts proven in this session;
- assumptions and unknowns that must not be promoted without evidence.

---

## Required Output

````md
# AI Handoff

## Role
Handoff Scribe

## Task Goal
-

## Risk Level
-

## Why This Risk Level
-

## Repository Access Mode
- Direct tool access / Pasted excerpts only / No file access / Unknown

## Role(s) Used
-

## Relevant Rules / Playbooks
-

## Files Read
-

## Files Not Read But Needed
-

## Files / Context To Send To Next Model
-

## Files Changed or Proposed
-

## Patch Category
-

## Tests / Checks Run
-

## Tests / Checks Not Run
-

## Verification Level
-

## Evidence Status

### PROVEN
-

### EXPECTED
-

### ASSUMED
-

### UNKNOWN
-

## Constraints
-

## What I Must Not Do
-

## Risks and Open Questions
-

## Security / Privacy Notes
-

## Data / Migration / Deployment Notes
-

## Rollback or Reversal Notes
-

## Next Safe Options

1.
2.
3.

## Human Decisions Required
-

## Verification Needed
-

## Escalation Needed?
-

## Next Role Recommendation
-

## Prompt For Next Role

```text
Role: [Architect / Reader / Executor / Verifier / Handoff Scribe]

Task:
[State the exact next task for the next session.]

Repository access:
[Direct tool access / Pasted excerpts only / No file access / Unknown]

Files / context to send to next model:
[List handoff context, proposed patches, reviewed evidence, and relevant mutable context. Do not present this as source authority.]

Files already read:
[List files read in the previous session. Treat them as needing re-read if freshness matters.]

Files you must re-read before acting:
[List exact files the next role must re-read before making claims, plans, patches, reviews, or handoffs.]

Evidence from previous role:
PROVEN:
- [Facts directly supported by evidence in the previous session]

EXPECTED:
- [Expected but not directly observed]

ASSUMED:
- [Context that must remain assumed until re-verified]

UNKNOWN:
- [Unknowns that must not be overclaimed]

Risk level:
[Risk level and reason]

Verification level:
[Verification level and scope]

Constraints:
[Scope limits and rules]

Do not:
- Do not treat this handoff as source authority.
- Do not rely on prior AI memory as evidence.
- Do not edit files before re-reading the exact current content.
- Do not claim commits, branch state, CI, deployment, migration, test status, security correctness, privacy correctness, or production readiness unless current evidence is reviewed.
- Do not convert plans, recommendations, assumptions, or expected behavior into completed facts.

Required output:
Use the required output format for the selected role.
Include Evidence Status with PROVEN, EXPECTED, ASSUMED, UNKNOWN.
Include Files Read and Files Not Read But Needed.
Include Prompt For Next Role unless escalation or human-only Operator work is required.
```

## Freshness Warning

This handoff is not source authority.
The next session must re-read relevant files, diffs, and test output before relying on it.
````
