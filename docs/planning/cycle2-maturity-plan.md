# Cycle 2 maturity targets and disposition

Original scope and accountability are recorded in [team roles](../team/roles.md). Estimates are review-sized planning estimates. Completion below means implemented and locally tested for the candidate.

| Target and Cycle 1 evidence | Scope and estimate | Primary / backup | Expected proof and candidate disposition |
|---|---|---|---|
| Protect request status after A5 REQ-006/007 and DEF-A5-001 | Email-based student registration and sign-in, owner-scoped My Requests, unread-response tracking, named reviewer sign-in, and negative tests. 60–90 minutes including independent review. | Carlos / Sanjana | [CLI regression and interactive check](../testing/final-test-evidence.md) complete locally. Local CLI risk reduced. IDs tied to existing requests require operator provisioning. |
| Improve failure and recovery evidence after the A5 operational gaps | Fixed events, storage failure test, restored-copy rehearsal and runbook. 30–45 minutes. | Jaylen and Dominic / Brendan | [Runtime evidence](../observability/runtime-evidence.md) records copy/restore. Monitoring and production recovery remain deferred. |
| Close the evidence chain after A5 local verification and workflow review | A6 evidence index, change summary, CI on final revision, risk review, traceability and AI log. 30–45 minutes plus CI and review. | Carlos / Sherry | [A6 package](../release/assignment6-final-release-package.md) drafted. GitHub PR, independent review, final CI and submitted tag are pending. |
| Address durable reviewer attribution after A5 DEF-A5-002 | Requires connecting approved reviewer identities to action records, defining assignment rules, and making audit retention decisions. Separately estimate if resumed. | Brendan / Sanjana | Deferred. Current events improve diagnosis with no actor or action history. See [residual risk](risk-register.md#a6-residual-risks). |

University login/SSO, per-instructor queues, real student data, hosted deployment, and browser integration are outside the bounded demo. Sherry and Carlos should review this re-estimation against any additional Cycle 1 feedback before accepting the release.
