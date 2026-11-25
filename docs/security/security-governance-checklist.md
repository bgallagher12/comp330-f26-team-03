# A6 security and governance review

Scope: supervised local Python/SQLite demo with synthetic data. Review owner per the [role record](../team/roles.md): Sanjana. Release decision: Carlos.

| Control or decision | Candidate evidence | Disposition |
|---|---|---|
| Limit student access to owned requests | Student sign-in verifies the email and password. Owner-scoped SQL constrains list, detail, and seen writes. Self-registration cannot claim an ID with existing requests. | Verified for the supervised CLI |
| Gate reviewer operations | Default CLI excludes and rejects reviewer choices. A separate reviewer startup looks up a named SQLite account and verifies its salted password hash before entering the menu. | Verified for the local CLI. Shared reviewer queue and local operator trust remain. Password reset and account revocation are outside the demo scope. |
| Keep secrets and synthetic personal fields out of logs | Hidden password entry and fixed standard-error events. | Tested for the exercised paths. Operator controls recording and storage. |
| Audit privileged changes | Current state and ephemeral outcome events exist. Individual actors and historical changes are unavailable. | Open under REQ-008. General-use blocker. |
| Access to data and tooling | Operator owns files and configuration. No external connections or AI components at runtime. AI work uses code and synthetic fixtures. | [Data handling](data-handling-notes.md) and [AI-use log](../ai/ai-use-log.md) |
| Approval to release | Review test evidence, permissions, workflow history, and residual risk in the PR. | Independent team review and final CI remain required. General use remains on hold. |

Passwords protect local sessions. The operator controls access to the database and provisioning for IDs with prior requests. Use the [permission matrix](permission-boundaries.md), [test evidence](../testing/final-test-evidence.md), and [risk register](../planning/risk-register.md) for review.
