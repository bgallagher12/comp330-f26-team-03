# A6 candidate testing and validation

The [local verification log](../../test-evidence/a6/verification.txt) records 31 passing tests and a separate interactive and recovery check with synthetic data and disposable SQLite storage. See [CI evidence](ci-evidence.md#a6-candidate-and-final-gate) for GitHub execution status.

| Scope | Coverage |
|---|---|
| Student service | 7 tests cover required fields, categories, unique request IDs, leading zeros, owned detail and response retrieval, and owner scoping and idempotency for first-open writes. |
| Reviewer service | 7 tests cover the pending queue, detail retrieval, missing requests, successful resolution, blank and duplicate resolutions, and salted credential storage. |
| CLI and SQLite | 17 tests cover email registration and sign-in, duplicate and invalid registration, denial of prior-request claims, legacy account access, role gating, invalid credentials, hidden-input failure, student isolation, list-only navigation, response opening, persistence after restart, invalid request and reviewer input, storage errors, and upgrades from A5 and the earlier A6 preview. |
| Interactive validation and recovery | Two terminal sessions exercised registration, email sign-in, hidden password entry, submission, reviewer resolution, list-only navigation, response opening, and restart. A stopped-session SQLite copy restored both accounts and the response's seen state. |

Independent teammate review and final GitHub CI are pending. [Release decision record](../release/assignment6-final-release-package.md#release-decision-record)
