# AI Feature Review Checklist

Use this checklist when the product itself uses AI, LLMs, embeddings, agents, model APIs, prompt chains, retrieval, or AI-generated output.

This checklist is stable guidance, not project state.

---

## 1. Feature Scope

- [ ] AI feature purpose is clear.
- [ ] User-visible behavior is described.
- [ ] Risk level is stated.
- [ ] AI model/provider is identified without secrets.
- [ ] Data flow is described.
- [ ] Output use is described.
- [ ] Human approval is required if sensitive decisions are involved.

Notes:

```text

```

---

## 2. Data Sent to AI

- [ ] Data sent to the model is listed by type.
- [ ] Sensitive data is avoided where possible.
- [ ] User personal data is not sent without review.
- [ ] Secrets are never sent.
- [ ] Production data is not used in prompts casually.
- [ ] Prompt content is redacted where needed.
- [ ] Provider retention/data-use policy is considered.
- [ ] User consent/privacy expectations are considered.

Notes:

```text

```

---

## 3. Prompt Injection and Untrusted Input

- [ ] User-controlled input is treated as untrusted.
- [ ] Retrieved documents are treated as untrusted.
- [ ] Tool outputs are treated as untrusted.
- [ ] Prompt injection scenarios are considered.
- [ ] Hidden/system prompt leakage risk is considered.
- [ ] AI instructions cannot override application authorization.
- [ ] AI output cannot bypass deterministic checks.

Notes:

```text

```

---

## 4. Output Validation

- [ ] AI output is validated before use.
- [ ] Structured output is schema-validated where relevant.
- [ ] Unsafe output is rejected or sanitized.
- [ ] Hallucination handling exists where relevant.
- [ ] User-visible claims are bounded.
- [ ] Generated code/config is reviewed before use.
- [ ] AI output is not treated as source authority.

Notes:

```text

```

---

## 5. Actions and Agency

- [ ] AI cannot directly perform sensitive actions by default.
- [ ] AI cannot mutate production data directly.
- [ ] AI cannot approve payments or ledger changes.
- [ ] AI cannot change permissions directly.
- [ ] AI cannot deploy or rotate secrets.
- [ ] Human approval exists for sensitive actions.
- [ ] Tool permissions follow least privilege.
- [ ] Autonomous loops are bounded or avoided.

Notes:

```text

```

---

## 6. Security / Privacy

- [ ] Sensitive information disclosure risk is reviewed.
- [ ] Logging avoids raw sensitive prompts/outputs.
- [ ] Access control is enforced outside the model.
- [ ] Rate limiting is considered.
- [ ] Abuse cases are considered.
- [ ] Third-party data sharing is documented.
- [ ] Compliance implications are considered where relevant.

Notes:

```text

```

---

## 7. Reliability and Failure Modes

- [ ] Provider timeout behavior is handled.
- [ ] Provider error behavior is handled.
- [ ] Invalid output behavior is handled.
- [ ] Cost/rate limit behavior is handled.
- [ ] Fallback path exists where needed.
- [ ] User messaging is clear when AI fails.
- [ ] Model/version changes are considered.

Notes:

```text

```

---

## 8. Observability and Audit

- [ ] Request IDs or trace IDs are used where relevant.
- [ ] Model/provider/version can be identified.
- [ ] Validation failures are observable.
- [ ] Sensitive logs are redacted.
- [ ] Human approvals are auditable where needed.
- [ ] High-impact AI decisions are reviewable.

Notes:

```text

```

---

## 9. Testing

- [ ] Normal input tested.
- [ ] Malformed input tested.
- [ ] Prompt injection attempt tested.
- [ ] Sensitive input handling tested.
- [ ] Provider failure tested or simulated.
- [ ] Invalid output tested.
- [ ] Rate/cost limit behavior tested where relevant.
- [ ] Human review path tested where relevant.

Notes:

```text

```

---

## 10. Decision

Choose one:

- [ ] Safe to keep as non-runtime scaffold.
- [ ] Safe for local/dev testing.
- [ ] Safe for limited guarded rollout.
- [ ] Requires security/privacy changes.
- [ ] Requires human approval before activation.
- [ ] Blocked due to excessive agency.
- [ ] Blocked due to sensitive data risk.
- [ ] Insufficient evidence.

Decision notes:

```text

```
