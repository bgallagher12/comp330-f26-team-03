# A5 defect log

Inspected 2026-11-17. Severity is impact on intended behavior, independent of whether a supervised demo can proceed. Proposed owner Carlos coordinates disposition; proposed reviewer Brendan must confirm independently. These are repository-local defect IDs, not invented GitHub issue numbers.

| ID | Reproduction and observed behavior | Expected behavior and impact | Severity | Status and disposition | Evidence |
|---|---|---|---|---|---|
| DEF-A5-001 | Launch app; options 3 and 4 appear without any identity or role check | AC-REQ-007-01 requires student users cannot use reviewer-only actions. Any operator can inspect/resolve requests. | High | Open; blocks real use; restricted demo recommendation only | `src/cli.py:menu/run`; LIM-001; risk R-006 |
| DEF-A5-002 | Submit then resolve a request; inspect requests schema | AC-REQ-008-01 asks for inspectable actions. No actor, resolution time or event history exists. | Medium | Open; no audit claim accepted | `src/schema.sql`; LIM-002; R-008 |
| DEF-A5-003 | Historical manual log mentions category display correction; exact failing revision/input/output was not preserved | Four selectable categories should display and work | Low | Historical corrected behavior reported; original failure not independently reproducible. Current CLI regression verifies category 2 selection. No claim to reproduce the historical bug. | `docs/testing/manual-test-evidence.md`; CLI workflow; issue #29 / PR #36 |
| DEF-A5-004 | At baseline open README and release documents | Reviewable phase status, concrete notes and exact tested revision required | High for A5 review | Remediated in this proposed package; independent review pending | Release evidence index, snapshot, test logs and this PR |

No known observed failure in the 16 executed tests. That statement does not close the two unmet requirements. Unexecuted scenarios remain coverage limits, not invented successful results or confirmed defects.
