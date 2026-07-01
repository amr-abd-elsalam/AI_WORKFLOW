# Mutable Context Templates

These are stable reusable skeletons for optional operational mutable context files.

They are templates, not project state.

Copy the relevant section into the matching operational file only when a session needs it:

- `.ai/CURRENT_STATE.md`
- `.ai/NEXT_PATCH_BRIEF.md`
- `.ai/HANDOFF.md`

Do not treat these templates, or any copied mutable context, as source authority.

Before relying on mutable context, revalidate against current repository files, diffs, tests, and Git evidence.

Use the canonical mutable context sequence from `.ai/playbooks/CONTEXT_MANAGEMENT.md` before promoting mutable claims to `PROVEN`.

Do not commit filled mutable context files unless the human explicitly accepts the stale-state risk.

Never store secrets, private keys, access tokens, production credentials, private user data, production dumps, or sensitive incident details in mutable context.

---

## Template for `.ai/CURRENT_STATE.md`

```md
# Mutable Context

This file contains changing project state.
It may be stale.
Do not treat it as source authority.
Revalidate against current repository files, diffs, tests, and Git evidence before relying on it.

Last updated:
Updated by:
Scope:

## Current Task

-

## Current Branch / Commit

-

## Current Repository Status

-

## Known Relevant Files

-

## Known Open Risks

-

## Recent Checks

-

## Notes for Next Session

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
```

---

## Template for `.ai/NEXT_PATCH_BRIEF.md`

```md
# Mutable Context

This file contains changing project state.
It may be stale.
Do not treat it as source authority.
Revalidate against current repository files, diffs, tests, and Git evidence before relying on it.

Last updated:
Updated by:
Scope:

## Next Patch Goal

-

## Reason for Patch

-

## Risk Level

-

## Patch Category

-

## Files Likely Relevant

-

## Files That Must Be Re-read Before Editing

-

## Constraints

-

## Out of Scope

-

## Suggested Verification

-

## Rollback / Reversal

-

## Human Decisions Required

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
```

---

## Template for `.ai/HANDOFF.md`

```md
# Mutable Context

This file contains changing project state.
It may be stale.
Do not treat it as source authority.
Revalidate against current repository files, diffs, tests, and Git evidence before relying on it.

Last updated:
Updated by:
Scope:

# AI Handoff

## Task Goal

-

## Role Used

-

## Risk Level

-

## Files Read

-

## Files Changed or Proposed

-

## Files / Context To Send To Next Model

-

## Patch Category

-

## Tests / Checks Run

-

## Tests / Checks Not Run

-

## Evidence Level

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

## Do Not Forget

- Prior AI claims are not source authority.
- Re-read relevant files before editing.
- Re-check diffs and tests before claiming status.
```
