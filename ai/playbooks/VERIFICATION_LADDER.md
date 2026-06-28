# Verification Ladder Playbook

This playbook defines verification strength.

It is stable guidance, not project state.

---

## Principle

Verification must match the claim.

A stronger claim requires stronger evidence.

Passing one test does not prove production readiness.
Reading documentation does not prove runtime behavior.
Finding a migration file does not prove the migration was applied.

---

## Evidence Grades

Use the grades from `ARCHITECT_RULES.md`:

- `PROVEN`
- `EXPECTED`
- `ASSUMED`
- `UNKNOWN`

---

## Verification Levels

### V0 — Not Verified

No current evidence was checked.

Use for:

- prior AI memory;
- unverified summaries;
- assumptions;
- old handoffs.

Allowed claim:

- "Unknown."
- "Not verified in this session."

---

### V1 — Text Inspected

A file or excerpt was read.

Can support:

- "This file says X."
- "The reviewed excerpt contains Y."

Cannot support:

- runtime behavior;
- integration;
- deployment;
- test success.

---

### V2 — Source Path Reviewed

Relevant source files were read.

Can support:

- "The reviewed code appears to implement X."
- "The expected behavior from this path is Y."

Cannot support:

- that tests pass;
- that production uses this code;
- that all callers are safe;
- that config enables it.

---

### V3 — Diff Reviewed

Actual patch/diff was reviewed.

Can support:

- "The diff changes X."
- "No unrelated change was seen in the reviewed diff."

Cannot support:

- runtime correctness;
- CI success;
- deployment success.

---

### V4 — Tests Inspected

Relevant tests were read.

Can support:

- "The tests assert X."
- "This case is covered by the reviewed test."

Cannot support:

- tests passing;
- production behavior;
- unasserted behavior.

---

### V5 — Local Test Output Reviewed

Actual local test output was reviewed.

Can support:

- "This command passed/failed in the shown environment."
- "These tests ran."

Cannot support:

- skipped tests passed;
- CI passed;
- production readiness.

---

### V6 — CI Output Reviewed

Actual CI output was reviewed.

Can support:

- "CI job X passed/failed at this run."
- "These checks ran in CI."

Cannot support:

- deployment happened;
- production is healthy;
- all risks are covered.

---

### V7 — Safe Runtime Observation

Runtime behavior was safely observed in a known environment.

Can support:

- "In environment X, version Y, config Z, behavior A was observed."

Cannot support:

- all environments;
- production unless production was the observed environment and safe to observe;
- absence of hidden issues.

---

### V8 — Staging/Rehearsal Verified

Behavior was verified in staging or rehearsal with known version/config/data conditions.

Can support:

- "This scenario worked in staging."
- "The rehearsal produced this result."

Cannot support:

- production success;
- all real data cases;
- long-term operational safety.

---

### V9 — Production Evidence Reviewed

Safe production evidence was reviewed.

Can support:

- "Production evidence shows X for the observed period/scope."

Cannot support:

- universal correctness;
- future behavior;
- full safety;
- absence of issues outside the observed scope.

---

## Claim Matching

| Claim | Minimum Evidence |
|---|---|
| "File contains X" | V1 |
| "Patch changes X" | V3 |
| "Code likely does X" | V2 |
| "Test asserts X" | V4 |
| "Tests passed" | V5 or V6 |
| "CI passed" | V6 |
| "Feature works locally" | V5 + relevant runtime check |
| "Feature works in staging" | V8 |
| "Feature is deployed" | deployment evidence |
| "Feature works in production" | V9, scoped |
| "Production-ready" | avoid unless scope is formally defined and exhaustively verified |

---

## Verification Output Template

```md
## Verification

Role: Verifier
Risk level:
Evidence reviewed:
Verification level:
Evidence grades:

### PROVEN
-

### EXPECTED
-

### ASSUMED
-

### UNKNOWN
-

### Checks run
-

### Checks not run
-

### Risks
-

### Recommendation
-
```
