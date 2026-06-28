# Security, Secrets, and Privacy Playbook

This playbook defines safe AI behavior around sensitive data.

It is stable guidance, not project state.

---

## Principle

AI must not become a secret holder, data gateway, credential viewer, or production-data processor.

Use synthetic data and redacted examples by default.

---

## Never Request or Echo

Do not request or output:

- `.env` values;
- API keys;
- passwords;
- DB credentials;
- production connection strings;
- OAuth tokens;
- session tokens;
- admin tokens;
- service tokens;
- private keys;
- payment credentials;
- real user personal data;
- production data dumps;
- private logs containing user data.

---

## If Secret-Like Content Appears

Do:

1. Do not repeat it.
2. Redact it.
3. Warn the human.
4. Recommend rotation where appropriate.
5. Recommend checking Git history, CI logs, PR comments, issue comments, chat logs, and deployment logs if exposure may have occurred.
6. Continue only with redacted placeholders.

Use placeholders like:

```text
<REDACTED_API_KEY>
<REDACTED_DB_PASSWORD>
<REDACTED_PRIVATE_KEY>
<REDACTED_USER_EMAIL>
```

---

## Safe Debugging Pattern

Ask the human for:

- redacted error messages;
- schema shape without values;
- synthetic reproduction;
- sanitized stack traces;
- config key names without values;
- local command output with secrets removed.

---

## Sensitive Data Classes

Treat all user data as sensitive by default.

Higher sensitivity includes:

- payment data;
- health data;
- legal data;
- children’s data;
- authentication data;
- private messages;
- precise location;
- government identifiers;
- biometric data;
- financial data.

---

## Security Review Questions

For sensitive changes, ask:

1. Does this broaden access?
2. Does this weaken authentication?
3. Does this weaken authorization?
4. Does this expose private data?
5. Does this log secrets or personal data?
6. Does this send data to a third party?
7. Does this introduce external calls?
8. Does this add hidden background work?
9. Does this change retention?
10. Does this affect compliance obligations?
11. Does this need human approval?
12. Is rollback possible?

---

## Development-Only Exceptions

If a human asks to disable a protection for local development, label it clearly:

```text
DEV-ONLY / INSECURE
```

Such changes must not silently affect production.
