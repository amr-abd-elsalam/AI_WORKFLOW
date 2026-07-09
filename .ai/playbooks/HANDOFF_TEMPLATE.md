# Handoff Template

Use this template when ending a session or transferring work.

This is a template, not project state.

---

````md
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

## Do Not Forget

- Prior AI claims are not source authority.
- Re-read relevant files before editing.
- Re-check diffs and tests before claiming status.

## NEXT_ROLE_PROMPT

Include either a copy/paste-ready fenced `text` prompt for the next role, or `NOT APPLICABLE` plus the reason.

```text
Role: [Next Role]
Canonical prompt file for this role: [`.ai/prompts/<ROLE>_PROMPT.md` matching the named Role, or `NOT APPLICABLE — human-only decision, no AI prompt file`]

Task:
[...]

Repository Context Packet:
- Workflow repository URL: [...]
- Target repository URL: [...]
- Original human problem statement: [...]
- Language preference: [language preference or UNKNOWN. For Arabic preference, use: Arabic prose. Keep filenames, commands, role names, and technical terms in English.]
- Repository access mode: [...]
- Risk level: [...]
- Constraints: [...]
- Evidence status: [Summarize; preserve PROVEN, EXPECTED, ASSUMED, UNKNOWN below]

Required output:
[exact required output format]
```
````
