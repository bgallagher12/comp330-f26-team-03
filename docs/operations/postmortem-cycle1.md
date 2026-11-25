# Cycle 1 postmortem

Scope: the [A5 baseline](https://github.com/bgallagher12/comp330-f26-team-03/releases/tag/a5-verification-release), its tests, and its documented defects. This is a retrospective on release evidence. The record contains no confirmed privacy incident or instructor presentation feedback.

| Cycle 1 evidence | What it showed | Contributing design or process choice | Cycle 2 response |
|---|---|---|---|
| [A5 traceability](../release/traceability-summary.md), REQ-006 and REQ-007 | The student could retrieve a response through the shared request number. The combined menu exposed reviewer actions. | The vertical slice prioritized an end-to-end demo through one local menu. Positive workflow tests did not establish that another student was denied. | Require student sign-in and scope request access to that account. Gate the reviewer menu with named local accounts and add negative CLI cases. |
| [A5 defect review](../quality/defect-review.md), DEF-A5-002 | The database held current state and resolution, with no individual reviewer attribution or timeline of changes. | The data model held one current row per request. | Add sanitized outcome and failure events for troubleshooting. Keep durable reviewer attribution and an action history open. |
| A5 release verification and the earlier runbook scaffold | Restart persistence was exercised. Storage failures and recovery were outside the tested demo path. | Verification focused on expected demo steps and field validation. | Exercise invalid SQLite storage, existing A5 data, and backup/restore to a separate checkout. Document when to stop and preserve the database. |

[Cycle 2 target dispositions](../planning/cycle2-maturity-plan.md) and [final test evidence](../testing/final-test-evidence.md) connect these findings to the candidate. Owners come from the [team role record](../team/roles.md). Team members can add separately sourced presentation feedback during release review.
