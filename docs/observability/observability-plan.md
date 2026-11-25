# A6 observability

The terminal writes fixed event names to standard error. An operator can read them locally or route standard error into an operator-owned diagnostic file for a rehearsal. Event messages exclude request IDs, identities, fields, passwords, and resolution text.

| Signal | What it reports | Operator action |
|---|---|---|
| `request_submitted`, `request_resolved` | SQLite returned after a successful write | Confirm the expected workflow result. |
| `student_sign_in_succeeded`, `student_sign_in_denied` | Student startup outcome | Check the email and whether the account has been registered in this checkout. |
| `student_response_opened` | CLI displayed a response and completed the seen update | Confirm the response remains readable and the badge clears. Reopening a response can emit this event again. |
| `reviewer_sign_in_succeeded`, `reviewer_sign_in_denied` | Reviewer startup outcome | Check the expected session and the account's local provisioning. |
| `storage_failure` plus exception type | Storage or filesystem error followed by exit code 1 | Stop and follow the [runbook](../operations/runbook.md). |
| `terminal_session_ended` | Input interruption or hidden input unavailable | Restart in an interactive terminal and inspect state before resubmitting. |

For a test session, an operator can count outcome lines manually. There is no persistent audit trail, alerting, metrics collector, or health endpoint. The local CLI has no configured hosted service or telemetry charges. Any optional diagnostic file consumes local disk and should be removed after review. [Runtime evidence](runtime-evidence.md) records the exercised paths.
