# READER_PROMPT.md
# Prompt for Evidence Gathering Before Edits

Use this prompt when you want AI to inspect files and build an evidence map before implementation.

This is a reusable prompt, not project state.

---

## Reader Prompt

Role: Reader.

Follow `ARCHITECT_RULES.md`.

Use relevant playbooks if available:

- `.ai/playbooks/VERIFICATION_LADDER.md`
- `.ai/playbooks/RISK_LEVELS.md`
- `.ai/playbooks/CONTEXT_MANAGEMENT.md`

Goal:

```text
[Describe what we need to understand]
```

Files provided or available:

```text
[List files or excerpts]
```

Known context:

```text
[Optional. Treat as ASSUMED until verified.]
```

---

## Instructions

Do not propose patches.

Do not rewrite code.

Do not infer current file content from memory or filenames.

Read only what is relevant, but read enough to be safe.

For every material claim, classify it as:

- `PROVEN`
- `EXPECTED`
- `ASSUMED`
- `UNKNOWN`

If more files are required, ask for them clearly.

If content appears stale, truncated, generated, or incomplete, say so.

If the task touches security, privacy, payments, migrations, production data, destructive operations, deployment, or secrets, escalate if evidence is insufficient.

---

## Required Output

```md
## Reader Pass

### Goal
-

### Risk Level
-

### Files Read
-

### Files Not Read But Likely Relevant
-

### Evidence Map

#### PROVEN
-

#### EXPECTED
-

#### ASSUMED
-

#### UNKNOWN
-

### Relevant Runtime Paths
-

### Relevant Tests
-

### Relevant Config / Scripts / Migrations
-

### Docs or Contracts That Need Verification
-

### Missing Evidence
-

### Risks
-

### Recommended Next Role
-

### Smallest Safe Next Step
-

### Escalation Needed?
-
```
