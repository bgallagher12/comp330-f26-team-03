# A3 Architecture Re-estimation and Construction Readiness

**Status:** Proposed planning evidence; owner and dates require team agreement.

## What changed since A2

PR #22 establishes a five-component layered architecture and seven proposed interface contracts. PR #20 proposes data/context boundaries and a synthetic-data decision. These documents clarify responsibilities but do not establish implemented integration or verified acceptance tests.

## Estimated work and uncertainty

| Scope | Existing A2 estimate | A3 finding | Planning action |
|---|---|---|---|
| Backend (Issue #3, EST-001) | 4–12 person-hours | Depends on finalized status, permissions and persistence | Re-estimate after Q-002/003/004/008 decisions |
| Frontend (Issue #4, EST-002) | 3–8 person-hours | Existing prototype not integrated with processing layer | Agree request schema and interface contract first |
| Database (Issue #5, EST-003) | 3–9 person-hours | ER/design baseline exists, runtime schema and storage decision unverified | Separate design complete from persistence implementation; re-estimate after Q-008 |

These are **existing planning ranges**, not newly measured or revised estimates. No defensible updated hour estimate is assigned without team review and evidence of additional work.

## First controlled integration commitment

1. Confirm minimum request fields, statuses, permissible transitions, and role capabilities (Q-001 through Q-004).
2. Confirm minimal persistence approach and responsibilities (Q-008); align with ER design and API-006/007.
3. Connect request submission to processing and persistence, and demonstrate retrieval by ID with synthetic data.
4. Add negative-path validation, forbidden reviewer actions, and persistence-failure verification.
5. Record actual results, changed estimates, assigned owner/backup, due date, and follow-up issues before claiming readiness.

## Gate 3 readiness interpretation

**Architecture planning evidence is not software completion evidence.** Open design decisions and missing CI/integration evidence remain disclosed. Implementation is gated by agreed interface/data ownership, reviewable risk treatment, and named accountability.
