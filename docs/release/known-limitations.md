# A5 known limitations and deferred capabilities

Inspection date 2026-11-17. These dispositions describe the candidate, not approval to waive requirements.

| ID | Limitation and impact | Mitigation for demonstration | Disposition and evidence |
|---|---|---|---|
| LIM-001 | No login or role enforcement. Any operator can read requests and resolve them. | Supervised local use with synthetic data only | Open unmet REQ-007; DEF-A5-001; `src/cli.py:run` |
| LIM-002 | No reviewer identity, resolution timestamp or action history. Current state cannot establish who changed it or when. | Describe only current-state persistence | Open unmet REQ-008; DEF-A5-002; `src/schema.sql` |
| LIM-003 | Only submitted and resolved states; one final resolution; no edit, reopen or notes history | Demonstrate only the supported transition | Verified REQ-004/005 transition and resolution; schema CHECK and reviewer tests |
| LIM-004 | No email format or maximum-length checks; values stringify | Use the exact synthetic fixture | Validation gap; `src/student_service.py`; no comprehensive type/length testing |
| LIM-005 | Local SQLite only. No hosted service, automated backup, recovery validation or concurrency/load qualification | Disposable local demo database | Operational constraint; `src/database.py`; not production ready |
| LIM-006 | Browser prototype is not connected to the SQLite services | Launch `python -m src.main` from repo root | Excluded from release claims; `scripts/campus.*` |
| LIM-007 | No notifications, category routing, SSO or university integration | Operator manually reviews queue | Deferred capabilities, not delivered |
| LIM-008 | No systematic security, accessibility, performance or platform matrix validation. EOF and storage errors are not covered by CLI regression | Use rehearsed environment and normal exit option | Coverage limitation; final verification record |

Owners for release disposition: Carlos (proposed), with Brendan as proposed independent reviewer. Acceptance of these limits must be recorded in the release-readiness review. No schedule or feature commitment is invented here.

## A6 candidate dispositions

- LIM-001 is mitigated for a supervised, synthetic-only terminal session. New students register with an email, student ID, and password and sign in with their email and password. Registration checks local records and does not verify university identity. A named local reviewer account unlocks a shared queue. University identity verification, account revocation, and password resets are outside the demo scope. A host operator can access files and run code directly.
- LIM-002 still applies. Standard-error events are ephemeral and carry no reviewer identity or durable history.
- LIM-005 and LIM-008 are partly mitigated by storage failure testing and a stopped-session synthetic restore rehearsal. Platform, concurrency, load, and hosted operational testing remain open.
- A5 and earlier A6 rows retain their request IDs, statuses, and responses. My Requests includes those rows after the operator provisions the exact saved student ID. Existing resolutions initially show the badge because their first-open state is unknown.
- LIM-003, LIM-004, and LIM-006 continue to apply. The in-app badge covers unread responses. Automatic notifications, category routing, SSO, and university integration remain deferred. A shared support reviewer sees the pending queue, with no instructor- or category-specific authorization.

See [current risk dispositions](../planning/risk-register.md#a6-residual-risks) and [candidate release judgment](final-release-notes.md).
