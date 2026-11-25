# Assignment 6 release notes

- **RN-A6-01 — Student sign-in and My Requests.** New students register with an email, student ID, and password. They sign in with their email and password, then select their own requests by menu number. **[Update available]** appears for a resolved request until the student opens the response. SQLite records the first open and preserves it across restarts.
- **RN-A6-02 — Reviewer session.** Reviewers sign in with a named local account, then use the shared pending queue and one-time resolution flow.
- **RN-A6-03 — Diagnostics and recovery.** Fixed runtime events and clean storage-failure exits support diagnosis. Startup preserves A5 and earlier A6 request data. A stopped-session backup restored both demo accounts, the response, and its seen state.
- **RN-A6-04 — Release evidence.** The candidate links the A5 findings to A6 regressions, residual risks, and the demo runbook.

The candidate is ready for review as a supervised synthetic-data demo. General use remains on hold because authorization trusts the host operator, the reviewer queue is shared, and account lifecycle controls and a durable action history remain open. CI on the published revision and independent team review are pending. [Tests](../testing/final-test-evidence.md) · [Risk register](../planning/risk-register.md#a6-residual-risks) · [Evidence package](assignment6-final-release-package.md)
