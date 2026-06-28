# Context Management Playbook

This playbook defines how to separate stable rules from mutable project state.

It is stable guidance, not project state.

---

## Principle

Stable governance and changing project facts must not be mixed.

Stable rules belong in:

- `ARCHITECT_RULES.md`
- `.ai/playbooks/*.md`

Mutable state belongs elsewhere.

---

## Stable Context

Stable context includes:

- governance rules;
- role definitions;
- verification rules;
- patch rules;
- security rules;
- risk levels;
- handoff templates;
- long-lived project principles.

Stable context should not contain:

- current branch;
- current commit;
- latest patch;
- current failing tests;
- current TODOs;
- current deployment state;
- incident details;
- temporary migration plans;
- environment-specific URLs;
- credentials;
- private data.

---

## Mutable Context

Mutable context may include:

- current task;
- current branch;
- current known failures;
- latest handoff;
- next patch brief;
- open risks;
- recent test output;
- current implementation status;
- PR status;
- release notes.

Suggested files:

- `.ai/CURRENT_STATE.md`
- `.ai/NEXT_PATCH_BRIEF.md`
- `.ai/HANDOFF.md`
- `.ai/DECISIONS_LOG.md`

---

## Mutable Context Rules

Mutable context is advisory.

Before relying on mutable context:

- re-check current repository files;
- re-check diffs;
- re-check tests if material;
- treat prior AI claims as `ASSUMED`;
- mark stale information clearly.

---

## Suggested Header for Mutable Files

```md
# Mutable Context

This file contains changing project state.
It may be stale.
Do not treat it as source authority.
Revalidate against current repository files, diffs, tests, and Git evidence before relying on it.

Last updated:
Updated by:
Scope:
```

---

## Do Not Store

Never store in mutable context:

- secrets;
- raw `.env` values;
- private keys;
- access tokens;
- production credentials;
- private user data;
- production dumps;
- sensitive incident details unsuitable for repo storage.

---

## Handoff Freshness Rule

A handoff is not proof.

It is a map for the next session.

The next session must re-read relevant files before modifying them.
