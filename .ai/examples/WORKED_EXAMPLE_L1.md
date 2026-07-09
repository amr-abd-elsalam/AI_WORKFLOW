# Worked Example: L1 Docs-Only Role Sequence

هذا مثال تعليمي خيالي بالكامل يوضح كيف يمكن لمهمة L1 docs-only أن تمر عبر الأدوار:

Architect → Reader → Executor → Verifier → Handoff Scribe

هذا الملف لا يطلب تنفيذ أي شيء ضد target repository حقيقي. المثال يستخدم مسارات خيالية تبدأ بـ `path/to/` لتجنب خلط المثال مع repository state الحقيقي.

---

## Purpose

الغرض من هذا المثال هو توضيح:

- كيف يحافظ كل role على حدوده.
- كيف ينتقل evidence من role إلى role بدون تحويل assumptions إلى facts.
- كيف تبقى مهمة L1 صغيرة، قابلة للمراجعة، وقابلة للعكس.
- كيف يكتب Executor patch بصيغة `New file` فقط.
- كيف يراجع Verifier patch-text بدون ادعاء أن أي command شُغّل.

هذا المثال ليس بديلًا عن الملفات الحاكمة. عند العمل الحقيقي، اقرأ الملفات المناسبة مثل:

- `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md`
- `.ai/playbooks/PATCH_PROTOCOL.md`
- `.ai/prompts/ARCHITECT_PROMPT.md`
- `.ai/prompts/READER_PROMPT.md`
- `.ai/prompts/EXECUTOR_PROMPT.md`
- `.ai/prompts/VERIFIER_PROMPT.md`
- `.ai/prompts/HANDOFF_PROMPT.md`

---

## Fictional Scenario

Human request:

> أريد إضافة صفحة FAQ قصيرة لمشروع وثائقي خيالي. لا تغيّر code أو config. أضف ملف docs فقط لو كان آمنًا.

Fictional target repository:

- Name: Sample Docs Garden
- Target repository URL: UNKNOWN
- Intended file: `path/to/docs/FAQ.md`
- Existing fictional context:
  - `path/to/docs/README.md` موجود ويذكر أن المشروع يحتوي documentation عامة.
  - لا توجد صفحة FAQ حالية حسب Reader في هذا المثال.

Risk classification:

- L1 Low
- السبب: docs-only، ملف جديد فقط، لا runtime behavior، لا security/privacy/production claims.

---

## Step 1 — Architect Pass

### Role
Architect

### Task
تخطيط أصغر خطوة آمنة لإضافة صفحة FAQ خيالية docs-only.

### Risk Level
L1 Low

### Why This Risk Level
المهمة docs-only وتستهدف ملفًا جديدًا فقط. لا توجد تغييرات code أو config أو migrations أو deployment.

### Repository Access Mode
Pasted excerpts only

### Relevant Rules / Playbooks
- `ARCHITECT_RULES.md`
- `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md`
- `.ai/playbooks/RISK_LEVELS.md`
- `.ai/playbooks/PATCH_PROTOCOL.md`

### Files Read
- لا يوجد source file حقيقي في هذا المثال.
- السياق المقدم من الإنسان treated as ASSUMED حتى يقرأ Reader الملفات الخيالية.

### Files Not Read But Needed
- `path/to/docs/README.md`
- listing خيالي لمنطقة `path/to/docs/`

### Evidence Status

#### PROVEN
- الإنسان طلب docs-only.
- الإنسان لم يطلب runtime أو config أو production change.

#### EXPECTED
- إضافة `path/to/docs/FAQ.md` كملف جديد قد تكون كافية.

#### ASSUMED
- لا توجد صفحة FAQ حالية.
- أسلوب documentation بسيط ويمكن اتباعه بعد قراءة `path/to/docs/README.md`.

#### UNKNOWN
- هل يوجد ملف FAQ سابق.
- هل توجد conventions خاصة للـ docs.

### Constraints
- docs-only.
- new-file-only إذا أكد Reader عدم وجود FAQ.
- عدم ادعاء runtime behavior أو production readiness.

### What I Must Not Do
- لا أكتب patch.
- لا أفترض محتوى الملفات غير المقروءة كحقيقة.
- لا أوسّع المهمة إلى restructuring أو navigation updates.

### Output Produced

#### Problem Being Solved
المستخدم يحتاج FAQ قصيرة لمشروع خيالي بدون تغيير behavior.

#### Likely Affected Areas
- `path/to/docs/FAQ.md`

#### Evidence Needed Before Implementation
- تأكيد هل `path/to/docs/FAQ.md` موجود.
- قراءة `path/to/docs/README.md` لمعرفة tone بسيط للمستندات.

#### Risks
- overclaiming بأن الصفحة متوافقة مع كل docs.
- تعديل index أو navigation بدون طلب.
- تحويل docs-only إلى broader docs restructuring.

#### False-Confidence Traps
- افتراض أن FAQ غير موجودة بدون قراءة.
- ادعاء أن التغيير complete أو tested بدون evidence.

#### Options

##### Option 1
- Summary: إضافة `path/to/docs/FAQ.md` فقط إذا أكد Reader أنه غير موجود.
- Pros: أصغر تغيير ممكن، docs-only، وسهل rollback.
- Cons: لا يضيف navigation أو links من ملفات أخرى.
- Verification needed: Reader يؤكد غياب الملف، وVerifier يراجع patch text.
- Rollback/reversal: Revert this patch.

##### Option 2
- Summary: إضافة FAQ وتحديث navigation أو README في نفس patch.
- Pros: قد يجعل الصفحة أسهل في الاكتشاف.
- Cons: يوسّع scope ويتطلب قراءة وتعديل ملفات إضافية.
- Verification needed: Reader يقرأ ملفات navigation أو README قبل أي تعديل.
- Rollback/reversal: Revert touched docs files.

#### Recommendation
Reader يقرأ الملفات الخيالية ذات الصلة ثم يقرر هل Executor يمكنه كتابة new-file-only patch.

#### Smallest Safe Next Step
Reader pass focused فقط على `path/to/docs/README.md` ووجود `path/to/docs/FAQ.md`.

#### Do Not Do Yet
- لا تعدّل navigation.
- لا تضف runtime examples.
- لا تدّعي lint/test success.

### Verification Needed
Patch-text verification على أي patch يقترحه Executor.

### Escalation Needed?
No

### Next Role Recommendation
Reader

### Prompt For Next Role

```text
Role: Reader

Task:
Build an evidence map for a fictional L1 docs-only task before any patch.

Repository Context Packet:
- Workflow repository URL: UNKNOWN
- Target repository URL: UNKNOWN
- Original human problem statement: Add a short FAQ page for a fictional docs project without code or config changes.
- Language preference: Arabic prose. Keep filenames, commands, role names, and technical terms in English.
- Repository access mode: Pasted excerpts only
- Risk level: L1 Low — docs-only, possible new file only
- Constraints: Do not propose patches. Do not claim unread file contents. Keep scope to docs-only.

Files you must re-read before acting:
- path/to/docs/README.md
- path/to/docs/ directory listing

Required output:
Return a Reader Pass with Evidence Status, risks, whether evidence is sufficient for a new-file-only docs patch, and Prompt For Next Role.
```

---

## Step 2 — Reader Pass

### Role
Reader

### Task
جمع evidence لمهمة FAQ الخيالية قبل patch.

### Risk Level
L1 Low

### Why This Risk Level
العمل المطلوب docs-only، وقد يكون new-file-only.

### Repository Access Mode
Pasted excerpts only

### Relevant Rules / Playbooks
- `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md`
- `.ai/playbooks/RISK_LEVELS.md`

### Files Read
- `path/to/docs/README.md` excerpt خيالي.
- `path/to/docs/` listing خيالي.

### Files Not Read But Needed
- لا يوجد ضمن النطاق الخيالي الحالي.

### Evidence Status

#### PROVEN
- `path/to/docs/README.md` excerpt الخيالي يستخدم tone بسيط ومباشر.
- listing الخيالي لا يحتوي `path/to/docs/FAQ.md`.
- لا توجد حاجة مثبتة لتعديل code أو config.

#### EXPECTED
- إضافة `path/to/docs/FAQ.md` كملف جديد تكفي للمطلب.

#### ASSUMED
- لا توجد docs navigation إلزامية غير مقروءة.
- FAQ قصيرة ستكون مقبولة بدون cross-linking.

#### UNKNOWN
- هل توجد style guide أوسع خارج الملفات المقروءة.
- هل يريد الإنسان ربط FAQ من README في patch لاحق.

### Constraints
- new-file-only.
- لا تعديل لـ README في هذا المثال.
- لا runtime أو production claims.

### What I Must Not Do
- لا أقترح patch بنفسي.
- لا أتعامل مع هذا المثال كحالة repository حقيقية.
- لا أدعي test أو lint success.

### Output Produced

#### Relevant Runtime Paths
- None.

#### Relevant Tests
- None required for fictional docs-only patch.
- يمكن لاحقًا اقتراح docs lint فقط إن كان موجودًا، لكنه UNKNOWN هنا.

#### Relevant Config / Scripts / Migrations
- None.

#### Docs or Contracts That Need Verification
- `path/to/docs/README.md` tone.
- عدم وجود `path/to/docs/FAQ.md` حسب listing الخيالي.

#### Missing Evidence
- لا يوجد blocker لمهمة new-file-only الخيالية.

#### Risks
- إضافة claims حول runtime behavior داخل FAQ.
- تعديل ملفات غير مطلوبة.

#### Evidence Sufficient For Patch?
yes

#### If Not Sufficient, Why?
Not applicable.

#### Recommended Next Role
Executor

#### Smallest Safe Next Step
Executor يكتب patch واحد لإضافة `path/to/docs/FAQ.md`.

### Verification Needed
Verifier يراجع patch-text فقط.

### Escalation Needed?
No

### Next Role Recommendation
Executor

### Prompt For Next Role

```text
Role: Executor

Task:
Draft the smallest safe new-file-only docs patch for the fictional FAQ task.

Repository Context Packet:
- Workflow repository URL: UNKNOWN
- Target repository URL: UNKNOWN
- Original human problem statement: Add a short FAQ page for a fictional docs project without code or config changes.
- Language preference: Arabic prose. Keep filenames, commands, role names, and technical terms in English.
- Repository access mode: Pasted excerpts only
- Risk level: L1 Low — docs-only, new file only
- Constraints: Add only path/to/docs/FAQ.md. Do not edit README or navigation. Do not claim tests passed.

Evidence from previous role:
PROVEN:
- path/to/docs/FAQ.md is absent from the fictional listing.
- path/to/docs/README.md has a simple direct tone.

EXPECTED:
- A short FAQ page satisfies the request.

ASSUMED:
- No mandatory docs navigation exists.

UNKNOWN:
- Whether a broader style guide exists.

Required output:
Return an Executor Pass with exact NEW FILE patch only, Suggested Verification, Rollback / Reversal, and Prompt For Next Role.
```

---

## Step 3 — Executor Pass

### Role
Executor

### Task
صياغة patch خيالي new-file-only لإضافة FAQ docs.

### Risk Level
L1 Low

### Why This Risk Level
docs-only وnew-file-only. لا runtime أو config أو migration أو security change.

### Patch Category
docs-only

### Repository Access Mode
Pasted excerpts only

### Relevant Rules / Playbooks
- `.ai/playbooks/PATCH_PROTOCOL.md`
- `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md`

### Files Read
- `path/to/docs/README.md` excerpt خيالي.
- `path/to/docs/` listing خيالي.

### Files Not Read But Needed
- لا يوجد ضمن المثال.

### Constraints
- إضافة ملف واحد فقط.
- لا تعديل existing files.
- لا ادعاء test success.

### What I Must Not Do
- لا أعدّل README.
- لا أضيف runtime claims.
- لا أعمل self-approval.

### Requirement / Risk Addressed
إضافة FAQ قصيرة وواضحة بدون توسيع scope.

### Scope
New file فقط: `path/to/docs/FAQ.md`

### Expected Side Effects
إذا طُبّق patch في repository خيالي، سيضيف صفحة FAQ واحدة. لا توجد side effects runtime.

### Evidence Status

#### PROVEN
- Reader قال إن `path/to/docs/FAQ.md` غير موجود في listing الخيالي.
- Reader قرأ tone بسيط في `path/to/docs/README.md`.

#### EXPECTED
- FAQ قصيرة تلبي الطلب.

#### ASSUMED
- لا حاجة لتعديل navigation.

#### UNKNOWN
- لا يوجد evidence عن docs tooling أو CI.

### What This Patch Proves
- يقدّم content مقترحًا لملف FAQ جديد في المثال.

### What This Patch Does Not Prove
- لا يثبت أن الملف طُبّق.
- لا يثبت أن tests أو lint نجحت.
- لا يثبت production readiness.

### Patch

📄 path/to/docs/FAQ.md

~~~md
# FAQ

## What is Sample Docs Garden?

Sample Docs Garden is a fictional documentation project used for examples.

## Who is this documentation for?

It is for readers who want a short, plain-language overview before reading longer guides.

## Does this page describe runtime behavior?

No. This page is docs-only and does not describe or change runtime behavior.

## Where should I go next?

Read the project overview in the main documentation entry point.
~~~

### Proposed Human Operator Command Packet

Draft-only. This packet is for human Operator use only after Verifier review and human acceptance.

The human decides whether to run any command.

AI did not execute these commands.

AI does not claim staging, commit, push, branch status, remote status, or command output.

Use reviewed/touched paths only. Do not use `git add .` as the default.

If branch or remote is unknown, use placeholders and state the assumption.

```bash
git status --short
git --no-pager diff -- path/to/docs/FAQ.md
git add path/to/docs/FAQ.md
git commit -m "docs: add FAQ page"
git push <remote> <branch>
```

### Suggested Verification
Human or Verifier can inspect the proposed patch text and confirm it is docs-only and new-file-only. If the patch is actually applied in a real environment, run only the repository's relevant docs checks if they exist.

### Rollback / Reversal
Revert this patch.

### Human Decisions Required
- هل يريد الإنسان لاحقًا ربط FAQ من README أو navigation؟ هذا خارج patch الحالي.

### Escalation Needed?
No

### Next Role Recommendation
Verifier

### Prompt For Next Role

```text
Role: Verifier

Task:
Challenge the fictional new-file-only docs patch before acceptance.

Repository Context Packet:
- Workflow repository URL: UNKNOWN
- Target repository URL: UNKNOWN
- Original human problem statement: Add a short FAQ page for a fictional docs project without code or config changes.
- Language preference: Arabic prose. Keep filenames, commands, role names, and technical terms in English.
- Repository access mode: Pasted excerpts only
- Risk level: L1 Low — docs-only, new file only
- Constraints: Verify patch text only. Do not claim commands ran. Do not broaden scope.

Patch category:
docs-only

Patch to verify:
New file path/to/docs/FAQ.md with a short FAQ page and no runtime behavior claim.

Required output:
Return a Verifier Pass with Patch-text verification, evidence status, findings, recommendation, and Prompt For Next Role.
```

---

## Step 4 — Verifier Pass

### Role
Verifier

### Task
مراجعة patch الخيالي المقترح قبل قبوله.

### Verifier Mode
Patch-text verification

### Risk Level
L1 Low

### Why This Risk Level
المراجعة تخص patch نصي docs-only وnew-file-only.

### Verification Level
V1 File/excerpt inspected

### Repository Access Mode
Pasted excerpts only

### Relevant Rules / Playbooks
- `.ai/playbooks/VERIFICATION_LADDER.md`
- `.ai/playbooks/PATCH_PROTOCOL.md`
- `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md`

### Evidence Reviewed
- Executor Pass.
- Patch text for `path/to/docs/FAQ.md`.
- Reader evidence summary.

### Evidence Not Reviewed
- Repository diff حقيقي.
- command output.
- CI output.
- real filesystem state.

### Source-Truth Phase Review
أعلى evidence هنا هو patch text والخطوات الخيالية السابقة. لا يوجد applied diff أو command output. لذلك لا يجوز ادعاء أن patch طُبّق أو أن checks نجحت.

### Files Read
- Patch text فقط داخل المثال.

### Files Not Read But Needed
- لا يوجد للـ patch-text verification.
- applied diff سيكون مطلوبًا لو أراد الإنسان applied-diff verification.

### Constraints
- لا تعديل code.
- لا replacement patch.
- لا approval مبني على ثقة Executor فقط.

### What I Must Not Do
- لا أدعي test success.
- لا أدعي repository state حقيقي.
- لا أدعي production readiness.

### Evidence Status

#### PROVEN
- patch text يضيف ملفًا واحدًا فقط: `path/to/docs/FAQ.md`.
- المحتوى لا يتضمن code أو config.
- المحتوى يقول صراحة إن الصفحة docs-only ولا تغيّر runtime behavior.

#### EXPECTED
- إذا طُبّق كما هو، سيكون change docs-only.

#### ASSUMED
- Reader evidence الخيالي عن غياب FAQ صحيح ضمن المثال.
- لا توجد navigation requirements خارج النطاق.

#### UNKNOWN
- هل patch طُبّق فعليًا.
- هل docs lint موجود أو ناجح.
- هل style guide أوسع موجود.

### Output Produced

#### Findings

##### Finding 1
- Severity: None within reviewed scope.
- Evidence: patch text contains only Markdown FAQ content.
- Why it matters: supports L1 docs-only classification.
- Recommendation: Accept within reviewed patch-text scope.

##### Finding 2
- Severity: Low caution.
- Evidence: no applied diff or command output was reviewed.
- Why it matters: prevents overclaiming that the patch was applied or tested.
- Recommendation: If applied later, verify with actual diff and relevant checks.

#### Hidden Side Effects Check
No hidden runtime activation, external call, migration, scheduler, or config change is visible in the patch text.

#### Security / Privacy Check
No secrets, credentials, personal data, or security-sensitive behavior visible in the patch text.

#### Data / Migration / Deployment Check
No data, migration, deployment, or production operation visible in the patch text.

#### Tests and Verification Gaps
No tests or docs lint output reviewed. This is acceptable for patch-text verification but must remain a gap.

#### Rollback / Recovery Gaps
Rollback is simple: remove the new file or revert the patch.

#### False Confidence Risks
- Saying "tests passed" without output.
- Treating fictional Reader evidence as real repository evidence.
- Assuming navigation updates are unnecessary in a real repository without checking.

#### Recommendation
Accept within reviewed patch-text scope.

#### Human Decisions Required
- Decide whether to apply the patch in the fictional exercise.
- Decide whether a separate navigation update is desired later.

### Verification Needed
Applied-diff verification if the patch is applied.

### Escalation Needed?
No

### Next Role Recommendation
Handoff Scribe

### Prompt For Next Role

```text
Role: Handoff Scribe

Task:
Record an accurate handoff for the fictional L1 docs-only worked example.

Repository Context Packet:
- Workflow repository URL: UNKNOWN
- Target repository URL: UNKNOWN
- Original human problem statement: Add a short FAQ page for a fictional docs project without code or config changes.
- Language preference: Arabic prose. Keep filenames, commands, role names, and technical terms in English.
- Repository access mode: Pasted excerpts only
- Risk level: L1 Low — docs-only, new file only
- Constraints: Do not claim applied diff, tests, CI, deployment, or production readiness.

Verification level:
V1 File/excerpt inspected — patch-text only.

Required output:
Produce an AI Handoff that separates PROVEN, EXPECTED, ASSUMED, UNKNOWN, files proposed, verification gaps, rollback, and next safe options.
```

---

## Step 5 — Optional Handoff Scribe Pass

## Role
Handoff Scribe

## Task Goal
تسجيل handoff دقيق للمثال الخيالي بعد قبول Verifier ضمن نطاق patch-text فقط.

## Risk Level
L1 Low

## Why This Risk Level
المثال docs-only وnew-file-only ولا يتضمن runtime أو production أو security-sensitive work.

## Repository Access Mode
Pasted excerpts only

## Role(s) Used
Architect, Reader, Executor, Verifier, Handoff Scribe

## Relevant Rules / Playbooks
- `.ai/playbooks/ROLE_OUTPUT_CONTRACT.md`
- `.ai/prompts/HANDOFF_PROMPT.md`

## Files Read
- fictional excerpts only.

## Files Not Read But Needed
- applied diff إذا تم تطبيق patch فعليًا لاحقًا.

## Files / Context To Send To Next Model
- Architect plan.
- Reader evidence map.
- Executor patch text.
- Verifier patch-text findings.

## Files Changed or Proposed
- Proposed only: `path/to/docs/FAQ.md`

## Patch Category
docs-only

## Tests / Checks Run
- None.

## Tests / Checks Not Run
- docs lint unknown.
- CI unknown.
- applied diff not reviewed.

## Verification Level
V1 File/excerpt inspected

## Evidence Status

### PROVEN
- في المثال، patch text المقترح new-file-only وdocs-only.
- Verifier راجع patch text فقط.

### EXPECTED
- إذا طُبّق patch كما هو، سيضيف FAQ docs page واحدة.

### ASSUMED
- لا حاجة لتعديل navigation.
- Reader evidence الخيالي صحيح ضمن المثال.

### UNKNOWN
- هل patch طُبّق في أي repository حقيقي.
- هل checks نجحت.
- هل توجد style guide أوسع.

## Constraints
- لا ادعاء execution.
- لا ادعاء test success.
- لا ادعاء production readiness.

## What I Must Not Do
- لا أحوّل هذا handoff إلى source authority.
- لا أدعي أن patch طُبّق.
- لا أضيف scope جديدًا.

## Risks and Open Questions
- هل يجب إضافة navigation link في patch منفصل؟
- هل يجب تشغيل docs lint إذا وُجد؟

## Security / Privacy Notes
No security or privacy-sensitive content was identified in the patch text.

## Data / Migration / Deployment Notes
No data, migration, deployment, or production operation is involved.

## Rollback or Reversal Notes
Revert this patch.

## Next Safe Options

1. Human applies the proposed new-file-only patch in a controlled branch.
2. Verifier performs applied-diff verification after seeing actual diff.
3. If navigation is desired, start a separate Architect or Reader pass.

## Human Decisions Required
- Whether to apply the patch.
- Whether to request a separate navigation update.

## Verification Needed
Applied-diff verification if applied.

## Escalation Needed?
No

## Next Role Recommendation
Human Operator only, if applying the fictional patch. Otherwise no further action.

## Prompt For Next Role

    NOT APPLICABLE — next step is human-only if the fictional patch is to be applied. This handoff is not source authority. Any next AI session must re-read actual files, diffs, and command output before making claims.

## Freshness Warning

This handoff is not source authority.
The next session must re-read relevant files, diffs, and test output before relying on it.

---

## What This Worked Example Demonstrates

- Architect plans and limits scope.
- Reader gathers evidence before edits.
- Executor proposes an exact patch but does not approve it.
- Verifier challenges the patch and labels verification level.
- Handoff Scribe records what is known without turning assumptions into facts.

---

## What This Worked Example Does Not Demonstrate

- It does not demonstrate runtime behavior.
- It does not demonstrate test success.
- It does not demonstrate CI success.
- It does not demonstrate security correctness.
- It does not demonstrate production readiness.
- It does not replace the governing prompts or playbooks.
