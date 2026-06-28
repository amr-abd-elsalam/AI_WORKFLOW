# Security Review Checklist

Use this checklist for changes touching authentication, authorization, user data, secrets, external calls, dependencies, logging, AI features, or runtime configuration.

This checklist is stable guidance, not project state.

---

## 1. Scope and Risk

- [ ] Risk level is stated.
- [ ] Security-sensitive files or paths are identified.
- [ ] The change does not exceed the stated scope.
- [ ] Security impact is described.
- [ ] Human approval is required if risk is L3 or L4.

Notes:

```text

```

---

## 2. Secrets

- [ ] No `.env` values are included.
- [ ] No API keys are included.
- [ ] No passwords are included.
- [ ] No tokens are included.
- [ ] No private keys are included.
- [ ] No production connection strings are included.
- [ ] No payment credentials are included.
- [ ] No secret-like values are repeated in the review.
- [ ] If exposure occurred, rotation is recommended.

Notes:

```text

```

---

## 3. Authentication

- [ ] Authentication is not bypassed.
- [ ] Authentication is not disabled except clearly labeled `DEV-ONLY / INSECURE`.
- [ ] Session handling is not weakened.
- [ ] Token validation is not weakened.
- [ ] Password or credential handling is not weakened.
- [ ] Error messages do not leak sensitive auth details.

Notes:

```text

```

---

## 4. Authorization and Access Control

- [ ] Authorization checks remain in place.
- [ ] Role/permission checks are not broadened silently.
- [ ] Object-level access control is considered.
- [ ] Tenant/user isolation is preserved.
- [ ] Admin-only paths remain protected.
- [ ] Default access is not more permissive.
- [ ] Failure mode denies access safely.

Notes:

```text

```

---

## 5. Input Validation and Output Handling

- [ ] Untrusted input is validated.
- [ ] Untrusted output is validated before downstream use.
- [ ] Error handling does not leak sensitive details.
- [ ] Injection risks are considered where relevant.
- [ ] File/path handling is safe where relevant.
- [ ] Serialization/deserialization risks are considered.

Notes:

```text

```

---

## 6. Data Protection and Privacy

- [ ] Real user data is not included in patches/tests/docs.
- [ ] Sensitive data is not logged.
- [ ] Private data is not sent to new third parties without approval.
- [ ] Data retention behavior is not changed silently.
- [ ] Data deletion/export behavior is not weakened.
- [ ] Privacy expectations are preserved.
- [ ] Synthetic or redacted data is used.

Notes:

```text

```

---

## 7. External Calls and Supply Chain

- [ ] New external calls are explicitly approved.
- [ ] New dependencies are explicitly approved.
- [ ] Dependency trust and maintenance are considered.
- [ ] Network behavior is not hidden.
- [ ] Tokens/credentials are not sent to unexpected destinations.
- [ ] Timeouts and failure modes are considered.
- [ ] Rate limits/cost controls are considered where relevant.

Notes:

```text

```

---

## 8. Logging and Observability

- [ ] Logs do not include secrets.
- [ ] Logs do not include private user data.
- [ ] Security-relevant failures are observable.
- [ ] Logging changes are proportional.
- [ ] Audit needs are considered for sensitive actions.

Notes:

```text

```

---

## 9. AI-Specific Security

If AI/LLM features are involved:

- [ ] Prompt injection risk is considered.
- [ ] Sensitive information disclosure risk is considered.
- [ ] AI output is treated as untrusted.
- [ ] Output is validated before use.
- [ ] AI does not directly perform sensitive actions.
- [ ] Human oversight exists where needed.
- [ ] Data sent to provider is reviewed.
- [ ] Retention/provider policies are considered.
- [ ] Cost/rate limit risks are considered.

Notes:

```text

```

---

## 10. Decision

Choose one:

- [ ] No security concerns found within reviewed scope.
- [ ] Minor concerns; can proceed with notes.
- [ ] Changes required before proceeding.
- [ ] Escalation required.
- [ ] Insufficient evidence.

Decision notes:

```text

```
