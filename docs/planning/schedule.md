# Schedule

## Schedule Basis

The Cycle 1 schedule is based on the current task plan, team ownership, project dependencies, and team availability.

The team will complete major component work before integration and leave time for testing, fixes, and documentation before submission.

## Milestones

| ID | Milestone | Target Date | Required By | Dependencies | Owner | Status |
|---|---|---|---|---|---|---|
| MS-001 | Database and ER diagram baseline completed | Before integration | Cycle 1 | Cycle 1 requirements | Carlos | Complete |
| MS-002 | Student request frontend prepared | Before integration | Cycle 1 | Request fields and requirements | Sherry | In Progress |
| MS-003 | Backend request-processing design prepared | Before integration | Cycle 1 | Request fields and database structure | Sanjana, Jaylen | In Progress |
| MS-004 | Frontend, backend, and database structures reviewed together | After component work | Cycle 1 | MS-001, MS-002, MS-003 | Team | Planned |
| MS-005 | Cycle 1 request workflow integrated | After interface review | Cycle 1 | MS-004 | Team | Planned |
| MS-006 | Final testing, fixes, and documentation completed | Before submission | Cycle 1 | MS-005 | Team | Planned |

## Phase-Gate Readiness

| Gate | Internal Readiness Target | Key Evidence / Deliverables | Status |
|---|---|---|---|
| A2 | A2 submission | Task plan, risk register, schedule, ownership, and dependencies | Complete |
| Cycle 1 | Before Cycle 1 submission | Integrated workflow, testing evidence, documentation, and reviewed pull requests | Planned |

## Major Dependencies

| Predecessor / Dependency | Dependent Work | Schedule Impact if Delayed | Related Risk |
|---|---|---|---|
| Database and ER design | Backend implementation | Backend may need updates or rework | R-001 |
| Agreement on request fields and status values | Frontend and backend | Components may not integrate correctly | R-002 |
| Backend request-processing decisions | Request workflow | Integration may be delayed | R-003 |
| Completion of individual component work | Integration | Integration cannot begin until major components are ready | R-005 |
| Pull request review and merge | Final testing | Merge conflicts may delay verification | R-004 |

## Near-Term Planning Window

| Time Window | Planned Outcome | Related Milestone(s) | Key Dependency / Risk |
|---|---|---|---|
| Current work | Complete frontend and backend planning/tasks | MS-002, MS-003 | R-002, R-003 |
| Integration checkpoint | Compare components and resolve interface differences | MS-004 | R-002, R-004 |
| Integration | Connect the Cycle 1 request workflow | MS-005 | R-001, R-003, R-005 |
| Final buffer | Test, fix problems, review documentation, and prepare submission | MS-006 | R-004, R-005 |

## Schedule Changes

| Date | Milestone / Gate | Previous Target | New Target | Reason | Related Evidence |
|---|---|---|---|---|---|

## Schedule Risks

| Risk ID | Affected Milestone / Gate | Schedule Exposure |
|---|---|---|
| R-001 | MS-003, MS-004 | Database changes may cause backend rework. |
| R-002 | MS-002, MS-003, MS-004 | Interface differences may delay integration. |
| R-003 | MS-003, MS-005 | Unclear backend rules may delay the request workflow. |
| R-004 | MS-004, MS-005, MS-006 | Merge conflicts may reduce time available for testing. |
| R-005 | MS-005, MS-006 | Late integration may leave less time for fixes. |

## A3 First Integration Commitment

**Planning status:** Proposed; confirm at the next team meeting.

**Goal:** Demonstrate one synthetic student support request moving
from submission to application processing, persistent storage,
retrieval by ID, reviewer status update, and student status retrieval.

| Milestone | Proposed Target | Primary | Backup | Verification |
|---|---|---|---|---|
| Confirm fields, statuses, and role rules | 2026-10-27 | Jaylen | Sherry | Record agreed rules and interface changes |
| Confirm persistence approach | 2026-10-28 | Sanjana | Carlos | Document storage decision and data ownership |
| Connect request submission to storage | 2026-10-30 | Sanjana | Jaylen | Create a synthetic request and retrieve its unique ID |
| Verify reviewer update and student retrieval | 2026-11-02 | Jaylen | Sanjana | Confirm saved status is returned correctly |
| Review failure cases and record evidence | 2026-11-02 | Sherry | Carlos | Record missing-field, unauthorized-action, and storage-failure results |

### Acceptance and Evidence

Integration is not complete until the team records evidence that:

1. A synthetic request can be submitted and receives a unique ID.
2. The saved request can be retrieved after submission.
3. A reviewer can update its status and the updated status is retained.
4. The student interface can retrieve the current status.
5. Invalid input and unauthorized actions do not incorrectly report success.
6. Persistence failures are reported rather than hidden.
7. Relevant test output, commits, or pull requests are linked.

**Current verification status:** Not yet demonstrated or verified.
These milestones represent planned future work, not passing tests.

Dates and assignments require confirmation by the team.
