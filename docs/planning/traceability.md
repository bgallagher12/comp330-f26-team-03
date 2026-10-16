# Traceability

## Requirements Traceability Matrix

| Requirement | Acceptance Criteria | Architecture / Design | Implementation | Verification | Risk / Assumption | Status |
|---|---|---|---|---|---|---|
| REQ-001 | AC-REQ-001-01, AC-REQ-001-02 | Not yet available | Issue #4 - Create Student Request Frontend Page (@sh3rry19); Issue #3 - Design Initial Backend Request Processing Logic (@jaylene05, @SanjGurl16) | Planned test or demonstration to confirm that valid requests can be submitted and requests missing required fields are rejected | Request contents remain an open design question | Planned |
| REQ-002 | AC-REQ-002-01 | Not yet available | Issue #5 - Create ER Diagram and Initial Database (@CarlosA019); Issue #3 - Design Initial Backend Request Processing Logic (@jaylene05, @SanjGurl16) | Planned or test demonstration to confirm that each request received a unique ID and can be retrieved later| Persistence mechanism and identifier approach are not yet finalized | Planned |
| REQ-003 | AC-REQ-003-01 | Not yet available | Issue #3 - Design Initial Backend Request Processing Logic (@jaylene05, @SanjGurl16) | Planned test / demonstration showing a support reviewer can access submitted request information | Reviewer access behavior remains subject to role-design decisions | Planned |
| REQ-004 | AC-REQ-004-01, AC-REQ-004-02 | Not yet available | Issue #3 - Design Initial Backend Request Processing Logic (@jaylene05, @SanjGurl16) | Planned automated test / demonstration confirming status changes are stored and displayed | Request statuses and valid status transitions remain unresolved | Planned |
| REQ-005 | AC-REQ-005-01 | Not yet available | Issue #3 - Design Initial Backend Request Processing Logic (@jaylene05, @SanjGurl16) | Planned automated test / demonstration showing reviewer notes or resolution information are saved | Definition of a resolved request remains an open question | Planned |
| REQ-006 | AC-REQ-006-01 | Not yet available | Issue #4 - Create Student Request Frontend Page (@sh3rry19); Issue #3 - Design Initial Backend Request Processing Logic (@jaylene05, @SanjGurl16) | Planned test / demonstration showing the student can view current status and available resolution information | Depends on decisions about what status and resolution information students may view | Planned |
| REQ-007 | AC-REQ-007-01, AC-REQ-007-02 | Not yet available | Issue #3 - Design Initial Backend Request Processing Logic (@jaylene05, @SanjGurl16) | Planned role test / demonstration confirming student and reviewer capabilities differ | Role permissions and allowed actions are not yet fully defined | Planned |
| REQ-008 | AC-REQ-008-01 | Not yet available | Issue #5 - Create ER Diagram and Initial Database (@CarlosA019); Issue #3 - Design Initial Backend Request Processing Logic (@jaylene05, @SanjGurl16) | Planned inspection / demonstration showing enough history exists to determine important status changes or reviewer actions | Required level of history and logging remains unresolved | Planned |
| REQ-009 | AC-REQ-009-01 | Not yet available | No dedicated implementation issue identified | Planned repository / data review confirming only synthetic or approved sample data is used | Assumes only synthetic or approved sample data will be used | Planned |
| REQ-010 | Not Yet Avaialable | docs/architecture/architecture.md, docs/architecture/component-responsibilities.md | No dedicated implementation issue identified  | Planned review to confim component responsibilities are shown in the implementation | Component ownership and responsibilities may need to be edited | Planned |


## Decision Traceability

ADR-0001: Use synthetic data for Cycle 1
Documented: docs/decisions/adr-001-use-synthetic-data-for-cycle1.md
Current Status: Proposed
Team must confirm if alternative considered and approve the decision before its considered accepted as the architecture baseline.


## Risk and Assumption Traceability

| Risk / Assumption | Affected Evidence | Current Effect / Action |
|---|---|---|
| Required request fields are not yet finalized | REQ-001, AC-REQ-001-01, AC-REQ-001-02 | The team must define the minimum required request information before implementation and validation rules are finalized |
| Persistence and identifier approach are not yet finalized | REQ-002, AC-REQ-002-01 | Storage and unique-ID design must be decided before implementation |
| Request statuses and valid transitions are not yet finalized | REQ-004, AC-REQ-004-01, AC-REQ-004-02 | The team must define the allowed status model before status-update logic can be completed |
| Resolution criteria are not yet finalized | REQ-005, AC-REQ-005-01 | The team must clarify what qualifies a request as resolved before final verification |
| Role permissions are not yet fully defined | REQ-003, REQ-006, REQ-007 | Student and reviewer capabilities must be clarified before role-specific behavior is implemented |
| History and logging depth are not yet finalized | REQ-008, AC-REQ-008-01 | The team must define the minimum inspectable history needed for Cycle 1 |
| Only synthetic or approved sample data will be used | REQ-009, AC-REQ-009-01 | Real student records and private Loyola data are excluded from implementation and testing |
|Authentication and Authorization Approach are not yet finalized | docs/architecture/api-contracts.md, docs/architecture/component-responsibilities.md; REQ-003, 006, 007 | Define permission enforcement, the request processing component should enforce permissions rather than only relying on the user interface|
|Storage technology is still not finalized | docs/architecture/api-contracts.md, docs/architecture/data-context.md; API-006, 007 | Select which storage technology to use and document the data store before finalizing the implementation |
|Logging and Retention are still not finalized | docs/architecture/data-context.md, docs/architecture/component-responsibilities.md;  REQ-008| Define the history, logging and retention behavior before finalizing implementation |
## Change Impact Traceability

The architecture, API contract and component responsibilities provide the current design context for the current requirements. No specific changed to the requirements will change what is recorded in this section. The team will plan and implement work when unresolved architecture decisions are finalized or when requirements, assumptions or deign changes.

## Traceability Gaps

| Gap | Why It Matters | Owner | Planned Resolution | Target Gate |
|---|---|---|---|---|
| Some requirements are only broadly covered by backend or database issues rather than dedicated tasks | More specific task breakdown may be needed for reviewer workflow, role separation, and history/logging | Planning & Process Lead / Team | Refine `task-plan.md` and create additional GitHub Issues if needed | A2 |
| Architecture and implementation evidence are not yet available | Downstream evidence cannot be traced until design and implementation work exists | Architecture & Development Lead | Add architecture references, implementation paths, and PR links as work is completed | Cycle 1 implementation |
| Verification evidence is planned but not yet produced | Acceptance criteria cannot be proven until tests or demonstrations are executed | Quality & Review Lead | Link actual tests, demonstrations, or review evidence when available | Cycle 1 verification |
|Storage, authorization and logging decisions are still open in the architecture documents | This might affect implementation responsibilities, verification and the security | Team| Resolve the remaining questions in the architecture documents and update the issues | Before affected implementation is finalized |

## Traceability Maintenance


The team will update traceability whenever requirements, acceptance criteria, risks, assumptions, major engineering decisions, implementation links, or verification evidence change. GitHub issues and pull requests will be linked as planned work becomes concrete, and implementation and test evidence will be added when it becomes available. The traceability document will be reviewed before each phase-gate submission so that known gaps are recorded and outdated links are corrected.
