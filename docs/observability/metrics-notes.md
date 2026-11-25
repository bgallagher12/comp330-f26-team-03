# Campus Connect operational measures

For the supervised demo, the operator can count fixed events from a single synthetic rehearsal and compare them with the expected script steps. The CLI keeps attempt outcomes on standard error during the session.

| Measure | How to read it | Purpose |
|---|---|---|
| Submitted and resolved requests | Count `request_submitted` and `request_resolved` lines | Check that the expected writes completed. Compare against the script, since a session can contain unrelated synthetic requests. |
| Sign-in denials | Count the role-specific `*_sign_in_denied` events | Check negative credential tests. Escalate unexpected access or repeated denials to the local operator. |
| Storage failures | Count `storage_failure` lines and note the exception type | Stop the rehearsal on a storage failure and follow the recovery procedure. |

The rehearsal has no persistent metrics collection, alert thresholds, or hosted telemetry charges. A manual count is a session observation. It cannot establish unique users, a system-wide failure rate, or consumption over time. [Signals](observability-plan.md) · [Runtime evidence](runtime-evidence.md) · [Runbook](../operations/runbook.md)
