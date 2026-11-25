# A6 runtime evidence

The [local verification log](../../test-evidence/a6/verification.txt) records the automated suite and a two-terminal pseudo-terminal exercise with synthetic data.

| Scenario | Observed runtime behavior | Result |
|---|---|---|
| Student and reviewer sign-in | Tony registered with an email and student ID and signed in with that email. Registration and sign-in password prompts had terminal echo disabled. Invalid credentials failed in automated CLI checks. | Passed |
| Submit, resolve, and open | The reviewer saw and resolved Tony's submission from a second terminal. The student's list-only visit kept the badge. Opening the response emitted `student_response_opened` and cleared the badge across restart. | Passed |
| Stopped-session SQLite copy | The copy passed `PRAGMA quick_check`. Both accounts could sign in on the restored copy, and the answer and seen state survived. | Passed for the synthetic fixture |
| Invalid SQLite file | The app exited with code 1 and emitted `storage_failure error_type=DatabaseError`. | Passed in automated CLI regression |

The record contains outcomes and test names. Throughput, load, and hosted monitoring were outside the rehearsal.
