# Campus Connect runbook

Operations owner per the team role record: Jaylen and Dominic. Backup: Brendan. Release decision: Carlos.

## Start a supervised local demo

Use a trusted operator's checkout from a local interactive terminal, with Python 3.10 or later and the standard-library SQLite module. Local verification used Python 3.12.14. No server, university account, network service, or external database is required. Use synthetic request data and run from the repository root.

The trusted operator provisions the reviewer account once from an interactive terminal. Choose private passwords of 15–128 characters. Entry and confirmation are hidden.

```bash
python -m src.main --add-reviewer demo-instructor
```

Start the student terminal with `python -m src.main` and the reviewer terminal with `python -m src.main --reviewer`. Run both from the same checkout to share `data/campusconnect.db`. New students type `/register` at the login prompt and enter their email, ID, and password. They then sign in with their email and password and use **My Requests**. For a student whose ID already has requests and no account, the operator uses `python -m src.main --add-student EMAIL STUDENT_ID`. Preserve any leading zeros when linking the account. Startup preserves earlier reviewer accounts. See the [demo script](../release/demo-script.md).

## Diagnose and respond

| Symptom | First check | Response |
|---|---|---|
| `student_sign_in_denied` or `reviewer_sign_in_denied` | Confirm the email or reviewer username belongs to an account in this checkout and the correct password was used. | Sign in again from an interactive terminal. If a demo password is lost, use a fresh synthetic checkout and provision a new account. |
| Expected request missing from My Requests | Confirm that both terminals use the same checkout and the ID linked to the signed-in account exactly matches the request owner. | Check the synthetic fixture from the reviewer workflow. Sign in as the matching provisioned demo account. |
| Request appears missing from reviewer queue | Check both terminals use the same checkout and whether the request is already resolved. | An authorized reviewer can inspect a known request through option 4 and leave the resolution blank to exit without changing it. |
| `storage_failure` or writes repeatedly fail | Stop both sessions. Check that the data path is writable by the trusted operator, disk space is available, and another demo run has exited. | Preserve the original database. Use the copy check below before choosing recovery. Escalate possible corruption or unexpected data access to the team lead. |
| Password or protected content exposed | Stop the demo and identify the affected session or capture without redistributing it. | Remove the capture from circulation, start a fresh synthetic checkout with new demo credentials and fixtures. Record the event with a redacted pending review. |

Standard error carries [operational events](../observability/observability-plan.md). Keep any diagnostic captures private and bounded to the current incident or verification task.

## Backup, recovery, and rollback

1. Exit all active app sessions. Use a separate private path for a copy of the complete `data/campusconnect.db`. If active SQLite sidecar files remain, stop and investigate before copying.
2. Verify the copy with SQLite `PRAGMA quick_check`. It must return `ok`. To exercise restoration, place the verified copy at `data/campusconnect.db` in a separate checkout of the same revision and sign in with the copied accounts. Check that the response and its badge state match what was saved.
3. If the copy fails the integrity check, retain both copies and escalate. A fresh disposable demo checkout with a new SQLite file can restore the demo without replacing the preserved database.
4. For a code regression, check out an earlier approved revision in a separate checkout with isolated synthetic storage. The A5 tag restores the earlier workflow and lacks the A6 access controls. Keep A6 data separate and limit any A5 run to operator-only historical verification.

A stopped-session copy and restore were exercised with one synthetic ticket. Hosted failover, live backups, and timed recovery targets are outside the current operating model. [Runtime evidence](../observability/runtime-evidence.md) records the observed result.


## Sustainment handoff

Jaylen and Dominic own the demo operating steps, with Brendan as backup. Before the final rehearsal, record the reviewed revision, replay submission and response retrieval with synthetic data, and check a stopped-session database copy. If storage fails, preserve the copy and diagnostic event type and notify Carlos. Sanjana reviews the test and residual-risk disposition. Carlos records the team release decision in the [readiness review](../reviews/release-readiness-review.md#a6-candidate-maturity-review).
