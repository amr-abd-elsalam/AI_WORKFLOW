# Patch Protocol Playbook

This playbook defines how AI should propose patches.

It is stable guidance, not project state.

---

## Principle

A patch should be small, reviewable, reversible, testable, and tied to a confirmed task or risk.

Avoid cleverness.
Avoid scope creep.
Avoid hidden activation.

---

## Patch Categories

Use one primary category:

- `docs-only`
- `test-only`
- `runtime-behavior`
- `config`
- `migration`
- `dependency`
- `security`
- `privacy`
- `generated`
- `refactor`
- `build-ci`
- `release-deployment`
- `ai-product`
- `cleanup`

If multiple categories apply, state the primary one and list secondary categories.

---

## Before Proposing a Patch

State:

```md
Role:
Risk level:
Patch category:
Files read:
Requirement or risk addressed:
Scope:
Expected side effects:
What this patch proves:
What this patch does not prove:
Suggested verification:
Rollback/reversal:
```

---

## Command Boundary

Patch proposals may include suggested verification commands, but commands are not proof.

If commands are included:

- label them as human Operator actions or read-only inspection suggestions;
- do not imply the AI executed them;
- do not claim command output unless the output was actually provided and reviewed;
- do not include commits, merges, pushes, deployments, migrations, secrets rotation, destructive operations, production operations, or payment/ledger actions as AI-executed steps.

If a command would require Operator authority, state that it is human-only.

### Human Operator Command Packet

After a patch is verified and accepted by the human, AI may provide a clearly labeled Human Operator Command Packet for possible git commit or push actions.

The packet must:

- state that the human decides whether to run commands;
- state that AI did not execute, authorize, or complete the commands;
- include preflight inspection before staging or push suggestions;
- stage only reviewed files, not `git add .` by default;
- make branch and remote assumptions explicit before push suggestions;
- avoid force push, destructive git cleanup, deployment, migration, secret rotation, production, payment, and ledger commands unless separately approved by the human.

A Human Operator Command Packet is a checklist or suggestion, not execution evidence.

### Git Metadata Suggestions

For patches that are likely to be accepted, Executor may include suggested git metadata as a planning aid.

Suggested git metadata may include:

- branch name;
- commit message;
- PR title;
- PR body outline;
- verification checklist.

Executor must label this as suggested metadata, not execution.

Executor must not claim that a commit, push, PR, merge, or deployment happened.

Verifier may refine the suggested git metadata after verification.

If verification is only `Patch-text verification`, git metadata must remain draft-only.

If verification is `Applied-diff verification` and the provided evidence supports acceptance within scope, Verifier may include a Human Operator Command Packet with:

- preflight inspection commands;
- staging commands for reviewed files only;
- proposed commit message;
- proposed push command with explicit branch/remote assumptions;
- proposed PR title/body.

---

## Output Patch Rules — Strict

You must output edits only in one of these forms.

### Existing file

```text
📄 path/to/file.ext

🔍 FIND:
<exact current content>

✏️ REPLACE:
<replacement content>
```

Rules:

```text
- FIND must be an exact match from the current file.
- FIND must be the smallest unique block that safely locates the edit.
- Do not use ellipses.
- Do not output whole files for small edits.
- If multiple edits are needed in one file, output multiple separate FIND/REPLACE blocks.
- If exact FIND cannot be guaranteed, do not guess. Ask to read the file.
```

### New file

````text
📄 path/to/new-file.ext

```text
<full file content>
```
````

Use the appropriate language fence for the new file when known, such as `md`, `js`, `ts`, `py`, `json`, `yaml`, or `text`.

### Unsafe / not enough context

```text
⚠️ Need to read path/to/file.ext before proposing a safe edit.
```

---

## Forbidden Patch Behavior

Do not include:

- hidden runtime activation;
- hidden feature flags;
- hidden background jobs;
- hidden schedulers;
- hidden queue consumers;
- hidden DB connections;
- hidden external calls;
- hidden dual-writes;
- hidden data migrations;
- hidden telemetry;
- dependency changes without approval;
- formatting churn;
- broad rewrites;
- unrelated refactors;
- generated-file changes hidden from review;
- security weakening without explicit `DEV-ONLY / INSECURE` labeling.

---

## Rollback Notes

For L0/L1:

- "Revert this patch."

For L2:

- describe affected files and expected reversal.

For L3/L4:

- include rollback sequence, data concerns, config concerns, and human approval requirements.

---

## Patch Review Questions

Before finalizing, ask:

1. Is this the smallest safe change?
2. Did I read every file I edit?
3. Did I avoid unrelated changes?
4. Did I introduce side effects?
5. Did I alter runtime behavior?
6. Did I touch sensitive data, auth, payments, migrations, deployment, or secrets?
7. Is verification proportional to risk?
8. Is rollback clear enough?
