# Architecture

## System Context

CampusConnect is a student support request and workflow system for the Cycle 1 vertical slice.

The primary users are:

- Student Requester — creates a support request and views its current status and available resolution information.
- Support Reviewer — views submitted requests, changes request status, and records notes or resolution information.

Users interact with CampusConnect through a user-facing application interface. The application processes requests, applies workflow rules, and stores request information in a persistent data store.

Cycle 1 uses only synthetic or approved sample data. The system does not connect to real Loyola student records, private university data, or live institutional systems.

Student requester and support reviewer roles may be simulated rather than using real institutional authentication.

No user-facing AI functionality is currently included in the Cycle 1 architecture. AI may assist the engineering process, but system workflow decisions remain controlled by the application and human users.

## Architectural Structure

The current Cycle 1 architecture is planned as a small layered application with clear separation between presentation, application logic, and persistence responsibilities.

The major architectural layers are:

1. User Interface Layer
   - Provides student requester and support reviewer interactions.
   - Collects request information.
   - Displays request status and resolution information.
   - Sends user actions to the application logic.

2. Application / Request Processing Layer
   - Validates submitted request information.
   - Coordinates request creation and retrieval.
   - Applies role-specific workflow behavior.
   - Handles request status updates.
   - Handles reviewer notes and resolution information.
   - Coordinates important workflow-history recording.

3. Persistence Layer
   - Stores support requests and related workflow state.
   - Preserves unique request identifiers.
   - Supports later request retrieval.
   - Stores information needed for status, resolution, and inspectable workflow history.

Dependencies should flow from the user interface toward the application logic and from the application logic toward persistence. The user interface should not directly modify persistent request data.

The exact programming language, framework, database technology, and deployment approach remain unresolved under Q-008. These implementation choices should not change the intended separation of responsibilities unless a later architecture decision documents the change.

## Major Components and Responsibilities

| Component | Primary Responsibility | Key Dependencies |
|---|---|---|
| Student Request Interface | Allows a student requester to enter and submit support-request information and view current status and available resolution information | Request Processing Logic |
| Reviewer Interface | Allows a support reviewer to view submitted requests, update status, and record notes or resolution information | Request Processing Logic |
| Request Processing Logic | Validates requests, coordinates request creation and retrieval, applies workflow rules, handles status changes, resolution information, and role-specific behavior | Persistence Layer |
| Persistence Layer | Stores and retrieves support requests, unique identifiers, status, resolution information, and required workflow-history data | Persistent Data Store |
| Persistent Data Store | Provides durable storage for CampusConnect Cycle 1 request and workflow information | Persistence Layer |

The precise implementation boundaries may be refined as the technology stack and data model are finalized.

## Interfaces and Dependencies

| Source | Target | Interaction | Interface / Protocol | Notes |
|---|---|---|---|---|
| Student Request Interface | Request Processing Logic | Submit a new support request | Application interface; exact protocol TBD | Required request fields remain subject to Q-001 and Q-005 |
| Student Request Interface | Request Processing Logic | Retrieve request status and resolution information | Application interface; exact protocol TBD | Supports REQ-006 |
| Reviewer Interface | Request Processing Logic | Retrieve submitted requests | Application interface; exact protocol TBD | Reviewer access rules remain subject to Q-004 |
| Reviewer Interface | Request Processing Logic | Update request status | Application interface; exact protocol TBD | Valid statuses and transitions remain subject to Q-002 and Q-003 |
| Reviewer Interface | Request Processing Logic | Record note or resolution | Application interface; exact protocol TBD | Resolution conditions remain subject to Q-006 |
| Request Processing Logic | Persistence Layer | Create, retrieve, and update request records | Internal application interface | Persistence approach remains dependent on final data design |
| Persistence Layer | Persistent Data Store | Store and retrieve durable request state | Database interface; technology TBD | Supports unique IDs, retrieval, status, resolution, and required history |

Detailed interface behavior is maintained in `/docs/architecture/api-contracts.md`.

## Data and State Ownership

| Data / State | Authoritative Owner | Persistence | Notes |
|---|---|---|---|
| Support request | Request Processing Logic | Persistent Data Store | Persistence Layer stores and retrieves the authoritative request record |
| Request identifier | Request Processing Logic / Persistence Layer | Persistent Data Store | Each submitted request must retain a unique identifier |
| Current request status | Request Processing Logic | Persistent Data Store | One current status is assumed under ASM-003 |
| Reviewer note / resolution | Request Processing Logic | Persistent Data Store | Stored with the related support request |
| Workflow history | Request Processing Logic | Persistent Data Store | Required depth remains unresolved under Q-007 |
| User role | Application workflow | Simulated for Cycle 1 | Student requester and reviewer roles may be simulated under ASM-002 |

Only application logic should authorize changes to request state. User-interface components should request changes through the application layer rather than directly modifying stored data.

## Constraints and Assumptions

| ID / Reference | Type | Description | Architectural Impact |
|---|---|---|---|
| ASM-001 | Assumption | CampusConnect uses synthetic sample data rather than real Loyola student records or private university data | Removes the need for live institutional data integration and limits Cycle 1 data handling to synthetic or approved sample data |
| ASM-002 | Assumption | Student requester and support reviewer roles may be simulated during Cycle 1 | The architecture does not require institutional authentication for the Cycle 1 vertical slice |
| ASM-003 | Assumption | Each support request has one current workflow status at a time | Request state can be modeled using a single current-status value unless this assumption is later invalidated |
| ASM-004 | Assumption | Cycle 1 focuses on one narrow support-request workflow | Architecture remains intentionally small and avoids unrelated campus-service workflows |
| Q-001 | Open Question | Required request information has not yet been finalized | May affect the interface, validation rules, and data model |
| Q-002 / Q-003 | Open Questions | Supported statuses and valid transitions are not yet finalized | May affect workflow logic, database representation, interfaces, and tests |
| Q-004 | Open Question | Exact student and reviewer permissions remain unresolved | May affect role boundaries and application authorization logic |
| Q-006 | Open Question | Conditions for considering a request resolved remain unresolved | May affect workflow and resolution behavior |
| Q-007 | Open Question | Required status-change and reviewer-action history remains unresolved | May affect persistence and logging design |
| Q-008 | Open Question | Technology stack has not yet been selected | Framework, database, and implementation details remain provisional |

## Architecture Diagram

The authoritative Cycle 1 architecture diagram is maintained separately at:

`/docs/architecture/architecture-diagram.png`

The diagram should use the same component names defined in this document and in `/docs/architecture/component-responsibilities.md`.

## Architectural Qualities and Tradeoffs

| Quality / Concern | Architectural Response | Tradeoff / Consequence |
|---|---|---|
| Maintainability | Separate user-interface, application-processing, and persistence responsibilities | Introduces explicit boundaries that require coordination between components |
| Testability | Keep request validation and workflow behavior in application logic rather than embedding it only in the UI | Requires clear interfaces between presentation and application layers |
| Data integrity | Route request creation and updates through request-processing logic before persistence | Adds application-layer validation but reduces uncontrolled data changes |
| Traceability | Preserve unique IDs, current status, resolution information, and planned workflow-history evidence | Additional stored history may increase persistence complexity depending on Q-007 |
| Security / Privacy | Use synthetic data and simulated roles for the bounded Cycle 1 workflow | Does not demonstrate production institutional authentication or real-data security controls |
| Simplicity | Keep Cycle 1 limited to one narrow workflow and avoid unnecessary external integrations | Some production capabilities are intentionally deferred |

## Key Architectural Decisions

No formal Architecture Decision Records have been completed at the current A3 baseline.

Several architecture decisions remain dependent on open questions, including:

| Decision | Current State | Evidence |
|---|---|---|
| Technology stack and database selection | Open | Q-008 |
| Request status model | Open | Q-002, Q-003, ASM-003 |
| Role and permission boundaries | Open | Q-004, ASM-002 |
| Workflow-history depth | Open | Q-007 |
| Request field structure | Open | Q-001 |

Significant decisions will be recorded in `/docs/decisions/` when finalized.

## Architecture Evolution

No material architecture changes have been recorded yet.

Architecture changes will be documented when implementation, review findings, resolved assumptions, risks, or other engineering evidence justify a change.

| Effective Gate | Change | Reason | Related Evidence |
|---|---|---|---|
| A3 | Initial Cycle 1 architecture baseline established | Provide a reviewable architecture before implementation accelerates | REQ-001 through REQ-009; ASM-001 through ASM-004; Q-001 through Q-008 |

## Expectations

- Describe the actual architecture rather than an aspirational architecture.
- Use consistent component and interface names across engineering artifacts.
- Keep system context, structure, responsibilities, and dependencies current.
- Maintain a useful architecture diagram.
- Separate requirements from architecture and architecture from low-level implementation detail.
- Reference assumptions, risks, decisions, and contracts rather than unnecessarily duplicating them.
- Make significant architectural tradeoffs explicit.
- Record uncertainty rather than manufacturing architectural certainty.
- Update related engineering evidence when the architecture materially changes.