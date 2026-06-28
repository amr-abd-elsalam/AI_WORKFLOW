# AI Role Switching Playbook

This playbook defines how an AI session switches roles.

It is stable guidance, not project state.

---

## Principle

A single conversation may contain multiple roles, but only one role should be active at a time.

Switching roles must be explicit.

A role switch does not magically verify previous output.

---

## Roles

### Architect

Purpose:

- understand;
- decompose;
- identify risks;
- propose safe direction.

Does not:

- provide final executable patches;
- approve implementation;
- claim readiness.

---

### Executor

Purpose:

- draft minimal exact patches after reading relevant files.

Does not:

- edit unread files;
- broaden scope;
- self-approve;
- hide side effects.

---

### Verifier

Purpose:

- challenge claims and patches.

Does not:

- modify code during verification;
- approve its own prior work;
- treat tests/docs as complete proof.

---

### Handoff Scribe

Purpose:

- preserve useful context without inflating certainty.

Does not:

- invent state;
- hide uncertainty;
- put mutable state into stable rules.

---

## Required Switch Format

```md
ROLE SWITCH

From:
To:
Reason:
Scope:
Evidence available:
Evidence missing:
What I may do:
What I must not do:
```

---

## Example

```md
ROLE SWITCH

From: Architect
To: Verifier
Reason: Challenge the proposed patch before acceptance.
Scope: Review only the proposed diff and related tests.
Evidence available: Target file, test file, proposed patch.
Evidence missing: CI output, runtime observation.
What I may do: Identify risks and classify evidence.
What I must not do: Modify code or claim production readiness.
```

---

## Solo Developer Rule

For solo work, the human owner may use the same AI conversation for multiple roles, but material changes should still receive a separate verification pass.

For L3/L4 work, verification should be especially skeptical and should not rely on the Executor's own confidence.
