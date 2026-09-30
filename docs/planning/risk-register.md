# Risk Register

## Risk Register

| ID | Risk | Likelihood | Impact | Mitigation | Contingency / Response | Owner | Status | Related Evidence |
|---|---|---|---|---|---|---|---|---|
| R-001 | If the database design changes after backend work begins, then some backend code may need to be updated. | Medium | Medium | Review the ER diagram and database structure before integration. | Update the database and affected backend code together. | Carlos | Open | task-plan.md |
| R-002 | If the frontend and backend use different request fields or status values, then integration may require rework. | Medium | Medium | Agree on request fields, categories, and status values before integration. | Compare both implementations and update them to use the same structure. | Team | Open | task-plan.md |
| R-003 | If backend validation or request-processing rules are unclear, then the request workflow may not match the intended Cycle 1 behavior. | Medium | Medium | Decide which fields are required and what should happen when a request is submitted. | Implement the minimum required Cycle 1 behavior and document unresolved features. | Sanjana, Jaylen | Open | task-plan.md |
| R-004 | If multiple team members edit the same files at the same time, then merge conflicts may delay work. | Medium | Low | Use separate branches and pull requests and communicate before changing shared files. | Resolve conflicts and review the combined file before merging. | Team | Monitoring | GitHub pull requests |
| R-005 | If integration happens too late, then the team may have less time to fix problems before submission. | Medium | Medium | Integrate components before the final review and leave time for fixes. | Prioritize required Cycle 1 functionality and postpone optional work if needed. | Team | Open | schedule.md |

## Risk Evaluation

Likelihood and impact are evaluated using Low, Medium, and High based on the team's current understanding of the project.

Most current risks are rated Medium because they could cause some rework or delay, but are unlikely to prevent the team from completing Cycle 1.

## Risk Triggers / Indicators

| Risk ID | Trigger / Indicator | Monitoring Evidence |
|---|---|---|
| R-001 | Backend work requires fields or relationships that are not represented in the database design. | ER diagram and backend changes |
| R-002 | Frontend and backend use different field names, categories, or status values. | Pull request review |
| R-003 | Required fields or request-processing rules are still undecided when implementation begins. | Backend planning notes |
| R-004 | Multiple pull requests modify the same shared file or Git reports merge conflicts. | GitHub pull requests |
| R-005 | Components are still unfinished when the team is ready to begin integration. | Task plan and team review |

## Materialized Risks

| Risk ID | Date | What Occurred | Resulting Action / Issue | Impact |
|---|---|---|---|---|

## Closed or Accepted Risks

| Risk ID | Final Status | Reason | Evidence |
|---|---|---|---|

## Risk Review

The team will review risks during planning meetings, before integration, and whenever a major requirement, dependency, or task changes.
