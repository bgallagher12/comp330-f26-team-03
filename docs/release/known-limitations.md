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
