# HANDOFF_PROMPT.md
# Prompt for Accurate Session Handoffs

Use this prompt when ending a session or preparing context for the next AI/human pass.

This is a reusable prompt, not project state.

---

## Handoff Prompt

Role: Handoff Scribe.

Follow `ARCHITECT_RULES.md`.

Use relevant playbooks if available:

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

---

## Required Output

```md
# AI Handoff

## Task Goal
-

## Role(s) Used
-

## Risk Level
-

## Files Read
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

## PROVEN
-

## EXPECTED
-

## ASSUMED
-

## UNKNOWN
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

## Freshness Warning

This handoff is not source authority.
The next session must re-read relevant files, diffs, and test output before relying on it.
```
