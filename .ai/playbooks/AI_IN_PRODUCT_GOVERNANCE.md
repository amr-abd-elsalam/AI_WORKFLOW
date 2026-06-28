# AI-in-Product Governance Playbook

This playbook applies when the product itself uses AI or LLMs.

It is stable guidance, not project state.

---

## Principle

AI inside the product is not just a feature.

It is a data flow, risk surface, reliability concern, cost center, and governance boundary.

AI output must be treated as untrusted unless validated.

---

## Before Activating an AI Feature

Review:

- what data is sent to the model;
- whether user consent is required;
- whether data is retained by provider or system;
- whether prompts contain sensitive data;
- whether outputs may expose sensitive data;
- whether output can trigger actions;
- whether humans review sensitive outputs;
- whether the feature can be abused through prompt injection;
- whether rate limits and cost controls exist;
- whether fallback behavior exists;
- whether logs contain sensitive content;
- whether audit records are needed.

---

## Forbidden by Default

Do not allow AI output to directly perform sensitive actions such as:

- approving payments;
- changing ledgers;
- deleting data;
- changing permissions;
- making legal, medical, financial, or employment decisions;
- sending irreversible messages;
- executing code;
- deploying software;
- rotating secrets;
- mutating production data.

If such behavior is truly required, it needs deterministic guardrails, explicit human approval, auditability, rollback or recovery planning, and risk acceptance.

---

## Prompt Injection Review

Consider:

- Can users place instructions inside content the model reads?
- Can retrieved documents override system behavior?
- Can tool outputs be malicious?
- Can the model leak hidden prompts?
- Can the model be tricked into unsafe actions?
- Are outputs validated before use?

---

## Output Validation

Validate AI output before use when it affects:

- database writes;
- API calls;
- user-visible claims;
- permissions;
- financial calculations;
- legal/medical/security advice;
- generated code;
- structured data;
- notifications.

---

## Human Oversight

Human review is required when AI output materially affects:

- rights;
- money;
- access;
- safety;
- privacy;
- legal obligations;
- irreversible actions.

---

## Logging and Retention

Do not log raw prompts or outputs if they contain sensitive data.

Prefer:

- redacted logs;
- metadata-only observability;
- request IDs;
- model version;
- decision path;
- validation outcome.

---

## AI Feature Verification

Verify:

- normal case;
- malformed input;
- prompt injection attempt;
- sensitive data input;
- refusal/fallback path;
- provider error;
- timeout;
- cost/rate limit behavior;
- output validation failure;
- audit trail where required.
