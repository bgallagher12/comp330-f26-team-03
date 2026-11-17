# A5 repeatable demonstration

Candidate A5-RC1, tested revision `3ee8d8866cebaca40c1550e1f34a8d94bc011dda`, prepared 2026-11-17.
Owner proposed: Carlos. Reviewer proposed: Brendan. Presentation date and presenters must be confirmed by the team.

## Environment and starting state

From the repository root, use Python 3.12 or later (local verification 3.12.14; historical CI 3.14.10). The app uses only the standard library. Tests require `python -m pip install -r requirements-dev.txt`.

```bash
git rev-parse HEAD
python -m pytest -v
python scripts/verify_a5.py
```

The verification script copies the real `src/` into a temporary directory and runs `python -m src.main` in separate processes. Each scenario starts with an empty database. Workflow session 2 reuses session 1's database, proving restart persistence. It asserts output, exit status and final SQLite rows. It never opens or deletes the normal development database. Expect three PASS results. If the revision differs, compare the source hashes to [snapshot.json](../../test-evidence/a5/snapshot.json) before using the recorded evidence.

## Scenario D1 request to resolution and restart

REQ-001 through REQ-006, with the restrictions in the traceability summary.
For a live interactive run use `python -m src.main` in a separate disposable checkout with no database. If using an existing database, use the returned ID rather than assuming 1.

| Step | Exact input | Expected observation |
|---|---|---|
| Submit | 1; Tony Tiger; 00123; tonytiger@example.com; Calculus I help; Please help me understand a concept before Friday.; 2 | Request Submitted, ID 1, category Tutoring, status submitted |
| Review | 3 | Pending Request includes ID 1 |
| Resolve | 4; 1; Office hours Monday 4-6 or Wednesday 12-3 at Dumbach 111. | Request is resolved, saved resolution |
| Retrieve | 2; 1 | Status resolved and same resolution |
| Exit | 5 | Clean exit |
| Restart same checkout | python -m src.main, then 2; 1; 3; 5 | Saved resolution survives restart, no pending requests |

Each semicolon separates one Enter key press. The script records precise per-line input arrays and full output in [cli-transcript.json](../../test-evidence/a5/cli-transcript.json), workflow sessions 1 and 2.

## Scenario D2 unknown and malformed IDs

Fresh database. Inputs: `2`, `99999`, `2`, `abc`, `5`, each on a new line. Expect `Request not found.`, then `Request ID must be a whole number`, return to the menu, and clean exit. No rows may be created. Evidence: invalid-id scenario and DEF-A5-003 regression disposition.

## Scenario D3 invalid request

Fresh database. Choose 1, use D1 identity/title, enter an empty description, choose category 2, then 3 and 5. Expect `description is required.` and `There are no pending requests`. Final database must be empty. Evidence: validation scenario and AC-REQ-001-02.

## Engineering callouts and fallback

Show the single request table in `src/schema.sql` and the CLI to service to SQLite imports. Show the requirements disposition before claiming completion. State explicitly that reviewer controls are available to all users and there is no history of who resolved a request. These limitations make the demo unsuitable for real student records.

Observed rehearsal: all three automated scenarios passed on 2026-11-17 in the preserved transcript. A live classroom presentation has not been observed by this package. If it fails, state the failure and show the dated transcript or automated tests as earlier evidence, never as a live success.
