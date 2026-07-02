# Begin Here

Use this file when you want to use `AI_WORKFLOW` with another software repository.

This repository is not the target application.

`AI_WORKFLOW` is the workflow and governance reference.

Your target project repository is the source of truth for actual code, tests, configuration, diffs, scripts, and project behavior.

---

## Start Here If You Have Another Repository

Use this path when you have:

1. a target project repository URL;
2. the `AI_WORKFLOW` repository URL;
3. a problem statement or task;
4. a language preference;
5. optional risk hints or constraints.

### Automatic Intake Dispatch Rule

If a human's natural request contains these inputs, the model must treat the request as an intake request even if the human does not explicitly mention `.ai/prompts/WORKFLOW_INTAKE_PROMPT.md`:

- target project repository URL;
- `AI_WORKFLOW` repository URL;
- problem statement or task;
- language preference.

In that case, the model must return an `Intake Result` with a copy/paste-ready next role prompt, usually `Role: Architect`.

The model must not inspect the target repository, solve the target problem, guess root cause, recommend implementation steps, or draft patches during intake.

Example human request:

```text
ده repo المشروع:
https://github.com/example/my-app

وده repo القواعد:
https://github.com/amr-abd-elsalam/AI_WORKFLOW

المشكلة:
الصفحة بتعمل crash لما المستخدم يضغط save.

كلمني بالعربي، والكود والملفات والمصطلحات التقنية بالإنجليزي.
```

---

## What To Copy First

Copy and use:

```text
.ai/prompts/WORKFLOW_INTAKE_PROMPT.md
```

Paste your natural request under that prompt.

The intake prompt must not solve the problem.

Its job is only to produce the first copy/paste-ready `Architect` prompt.

---

## Expected Flow

```text
Human natural request
→ Intake creates Architect prompt
→ Architect plans
→ Reader gathers evidence
→ Executor drafts exact patch
→ Verifier challenges it
→ Handoff Scribe preserves context
→ Human Operator decides, commits, pushes, or opens a PR
```

---

## Repository Roles

### Workflow Repository

The workflow repository contains:

- governance rules;
- role prompts;
- playbooks;
- checklists;
- patch discipline;
- verification discipline.

For this project, the workflow repository is usually:

```text
https://github.com/amr-abd-elsalam/AI_WORKFLOW
```

### Target Repository

The target repository contains the actual software project.

It is the source of truth for:

- source code;
- tests;
- configuration;
- scripts;
- migrations;
- diffs;
- actual project behavior.

Do not treat `AI_WORKFLOW` as proof of anything about the target project's implementation.

---

## Language Preference

You can tell the model how to communicate.

Example:

```text
اكتب الشرح والتواصل بالعربي.
اكتب الكود وأسماء الملفات والأوامر والمسارات والمصطلحات التقنية بالإنجليزي.
```

The language preference should be carried forward through each role prompt.

---

## Important Boundaries

AI must not:

- request or expose secrets;
- treat unread files as known;
- solve the task before evidence is gathered;
- draft patches before the relevant files are read;
- self-approve its own patch;
- execute commits, pushes, deployments, migrations, secrets work, destructive actions, or production operations.

The human remains the Operator.

AI may help plan, read, draft, verify, and summarize.

The human decides what is accepted and executed.

---

## After Intake

After the intake prompt returns an `Architect` prompt:

1. copy the `Architect` prompt;
2. paste it into the AI model;
3. wait for the `Architect Pass`;
4. copy the `Prompt For Next Role`;
5. continue role by role.

For the full method, read:

```text
SOLO_AI_ENGINEERING_METHOD.md
```

For stable governance, read:

```text
ARCHITECT_RULES.md
```

For daily compact use, read:

```text
.ai/QUICKSTART.md
```
