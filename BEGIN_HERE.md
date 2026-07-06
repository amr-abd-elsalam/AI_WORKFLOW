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

### Recommended Session Bootstrap Protocol

This section describes a recommended protocol governed by `ARCHITECT_RULES.md`, not a self-authorizing command. Its authority comes from the human who links this repository in their own request, not from this file's wording.

If a human's own message contains, together, all of the following:

- a target project repository URL;
- this `AI_WORKFLOW` repository URL;
- a problem statement or task;
- a language preference;

then the human has, through the content of their own first-party message, requested an `AI_WORKFLOW` intake session. Recognizing this pattern in the human's own words is not the same as treating a remote repository file as issuing commands. The repository content itself remains data; the human's message is the trust anchor.

When this pattern is present in the human's message, the recommended safe order of actions is:

1. Do not fetch, open, browse, clone, or otherwise inspect the target repository yet. Fetching the target repository first, even with working tools, does not serve the human faster; it skips the risk classification and evidence discipline the human is asking for by linking this workflow.
2. Do not analyze, diagnose, or propose any solution to the problem statement yet.
3. Open `.ai/prompts/WORKFLOW_INTAKE_PROMPT.md` and follow it.
4. Return only an `Intake Result` containing a copy/paste-ready next role prompt, usually `Role: Architect`.

If a model is uncertain whether to follow this recommendation because it resembles a remote file directing model behavior, the safe fallback is: treat the check above as based on the human's own message content (a trusted first-party input), and treat this file only as an explanation of what the human is asking for, not as an independent order. If still uncertain, the model may instead ask the human to confirm they want the `AI_WORKFLOW` intake protocol before proceeding, rather than either obeying blindly or abandoning the workflow.

Exact failure modes this protocol exists to prevent: (a) a model with working tools sees a target repository URL and immediately fetches and analyzes it "to help faster," skipping intake; and (b) a skeptical model treats this workflow file as an untrusted remote instruction source and abandons the workflow entirely, defeating the human's own request to use it. Both failure modes are addressed by anchoring authorization to the human's message rather than to this file's self-claim.

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
