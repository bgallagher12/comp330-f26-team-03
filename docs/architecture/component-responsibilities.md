# Component Responsibilities

## Component Responsibility Matrix

| Component | Primary Responsibilities | Does Not Own | Depends On | Used By | Related Requirements |
|---|---|---|---|---|---|
| Student Request Interface | Collect student request information, submit requests, and display current request status and available resolution information | Authoritative workflow rules, persistent storage, reviewer permissions, direct database access | Request Processing Logic | Student Requester | REQ-001, REQ-006 |
| Reviewer Interface | Display submitted requests, allow reviewer status updates, and allow reviewer notes or resolution information to be entered | Authoritative workflow rules, persistent storage, direct database access | Request Processing Logic | Support Reviewer | REQ-003, REQ-004, REQ-005, REQ-007 |
| Request Processing Logic | Validate requests, coordinate creation and retrieval, enforce role-specific workflow behavior, process status updates, process reviewer notes/resolution information, and coordinate workflow-history recording | User-interface presentation and physical database implementation | Persistence Layer | Student Request Interface, Reviewer Interface | REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008 |
| Persistence Layer | Provide controlled storage and retrieval of support requests, identifiers, statuses, resolution information, and workflow-history data | Workflow policy, role decisions, presentation logic | Persistent Data Store | Request Processing Logic | REQ-002, REQ-004, REQ-005, REQ-006, REQ-008 |
| Persistent Data Store | Durably store CampusConnect request and workflow records | Application workflow rules, role permissions, user-interface behavior | None within the current application boundary | Persistence Layer | REQ-002, REQ-004, REQ-005, REQ-006, REQ-008, REQ-009 |

## Detailed Component Responsibilities

### Student Request Interface

**Purpose**

Provide the user-facing interface for student requesters during the Cycle 1 workflow.

**Owns**

- presentation of request-submission fields;
- collection of student-entered request information;
- initiation of request submission;
- presentation of request status; and
- presentation of available resolution information.

**Does Not Own**

- authoritative validation or workflow rules;
- durable request storage;
- reviewer-only workflow behavior;
- direct database access; or
- final authorization decisions.

**Inputs**

- student-entered request information;
- student actions such as submit or view request; and
- request information returned by the Request Processing Logic.

**Outputs**

- request-submission operations;
- request-retrieval operations; and
- rendered request, status, validation, and resolution information.

**Dependencies**

- Request Processing Logic.

**Failure Responsibilities**

The Student Request Interface should display validation or application failures clearly and should not indicate that a request was successfully created or updated when the Request Processing Logic reports a failure.

**Related Evidence**

- Requirements: `REQ-001`, `REQ-006`
- Acceptance Criteria: `AC-REQ-001-01`, `AC-REQ-001-02`, `AC-REQ-006-01`
- API / Interface Contracts: maintained in `/docs/architecture/api-contracts.md`

### Reviewer Interface

**Purpose**

Provide the user-facing interface through which a support reviewer can inspect and process submitted requests.

**Owns**

- presentation of submitted request information;
- initiation of reviewer status updates;
- collection of reviewer notes or resolution information; and
- presentation of reviewer workflow actions.

**Does Not Own**

- authoritative workflow rules;
- persistent request state;
- direct database access; or
- final determination of whether an operation is valid.

**Inputs**

- reviewer actions;
- submitted request data;
- current request status; and
- existing reviewer note or resolution information.

**Outputs**

- request-retrieval operations;
- requested status changes;
- reviewer note or resolution updates; and
- rendered reviewer workflow information.

**Dependencies**

- Request Processing Logic.

**Failure Responsibilities**

The Reviewer Interface should display failed or rejected workflow operations and must not represent an unsuccessful status or resolution update as completed.

**Related Evidence**

- Requirements: `REQ-003`, `REQ-004`, `REQ-005`, `REQ-007`
- Acceptance Criteria: `AC-REQ-003-01`, `AC-REQ-004-01`, `AC-REQ-004-02`, `AC-REQ-005-01`, `AC-REQ-007-01`, `AC-REQ-007-02`
- API / Interface Contracts: maintained in `/docs/architecture/api-contracts.md`

### Request Processing Logic

**Purpose**

Coordinate CampusConnect application behavior and enforce the Cycle 1 workflow rules.

**Owns**

- application-level validation;
- request creation and retrieval coordination;
- role-specific workflow behavior;
- request status-update processing;
- reviewer note and resolution processing;
- unique-identifier coordination;
- workflow-history coordination; and
- application-level error handling.

**Does Not Own**

- user-interface presentation;
- physical database implementation; or
- direct user interaction.

**Inputs**

- request-submission commands;
- request-retrieval commands;
- reviewer status-update commands;
- reviewer note or resolution commands; and
- role context for the current operation.

**Outputs**

- validated request records;
- request information;
- status changes;
- note or resolution changes;
- persistence operations; and
- application errors when an operation cannot be completed.

**Dependencies**

- Persistence Layer.

**Failure Responsibilities**

The Request Processing Logic must reject invalid or unauthorized operations, identify missing required information where appropriate, and must not report a successful state change unless the required operation has been completed.

**Related Evidence**

- Requirements: `REQ-001` through `REQ-008`
- Acceptance Criteria: `AC-REQ-001-01` through `AC-REQ-008-01`
- API / Interface Contracts: maintained in `/docs/architecture/api-contracts.md`

### Persistence Layer

**Purpose**

Provide a controlled boundary between application workflow logic and durable request storage.

**Owns**

- storage and retrieval operations;
- translation between application request data and persistent records;
- preservation of unique request identifiers;
- persistence of current status;
- persistence of reviewer notes or resolution information; and
- persistence of required workflow-history information.

**Does Not Own**

- workflow validation rules;
- role authorization rules;
- user-interface behavior; or
- reviewer decision-making.

**Inputs**

- create-request operations;
- retrieve-request operations;
- status-update operations;
- resolution-update operations; and
- history-recording operations.

**Outputs**

- stored request records;
- retrieved request records;
- persistence confirmations; and
- persistence errors.

**Dependencies**

- Persistent Data Store.

**Failure Responsibilities**

The Persistence Layer must report storage or retrieval failures to the Request Processing Logic and must not report successful persistence when the underlying operation fails.

**Related Evidence**

- Requirements: `REQ-002`, `REQ-004`, `REQ-005`, `REQ-006`, `REQ-008`
- Acceptance Criteria: `AC-REQ-002-01`, `AC-REQ-004-01`, `AC-REQ-004-02`, `AC-REQ-005-01`, `AC-REQ-006-01`, `AC-REQ-008-01`
- API / Interface Contracts: maintained in `/docs/architecture/api-contracts.md`

### Persistent Data Store

**Purpose**

Provide durable storage for CampusConnect Cycle 1 request and workflow data.

**Owns**

- stored request records;
- stored unique identifiers;
- stored current status;
- stored reviewer notes or resolution information; and
- stored workflow-history information required by the final Cycle 1 design.

**Does Not Own**

- application workflow policy;
- role permissions;
- validation rules; or
- user-interface behavior.

**Inputs**

- persistence operations from the Persistence Layer.

**Outputs**

- stored data;
- retrieved data; and
- database or storage errors.

**Dependencies**

- No internal CampusConnect component beyond the Persistence Layer boundary.

**Failure Responsibilities**

The data store must expose storage or retrieval failures through the Persistence Layer so that the application does not incorrectly assume that state was saved.

**Related Evidence**

- Requirements: `REQ-002`, `REQ-004`, `REQ-005`, `REQ-006`, `REQ-008`, `REQ-009`
- Acceptance Criteria: `AC-REQ-002-01`, `AC-REQ-004-01`, `AC-REQ-005-01`, `AC-REQ-006-01`, `AC-REQ-008-01`, `AC-REQ-009-01`

## Responsibility Boundaries

| Concern | Owning Component | Boundary / Rule |
|---|---|---|
| Request input presentation | Student Request Interface | The interface collects and displays information but does not establish authoritative workflow validity |
| Reviewer workflow presentation | Reviewer Interface | The interface exposes reviewer actions but the Request Processing Logic determines whether operations are allowed |
| Request validation | Request Processing Logic | User interfaces may provide convenience validation, but authoritative validation occurs in application logic |
| Role-specific workflow behavior | Request Processing Logic | Student and reviewer permissions are enforced at the application boundary rather than relying only on hidden UI controls |
| Persistent request state | Persistence Layer / Persistent Data Store | Durable state is accessed through the persistence boundary; user interfaces do not directly modify stored records |
| Unique request identifiers | Request Processing Logic / Persistence Layer | Request creation must result in a preserved unique identifier; exact generation strategy remains dependent on the final persistence design |
| Status changes | Request Processing Logic | Reviewer actions request a status change, but workflow logic determines whether the change is valid before persistence |
| Reviewer notes / resolution information | Request Processing Logic | Reviewer input is processed through application logic before being stored |
| Workflow history | Request Processing Logic / Persistence Layer | Application logic determines what actions should be recorded; persistence stores the resulting history |
| Synthetic-data constraint | All application components | Components must operate without requiring real student records or private Loyola data |

## Shared Responsibilities

| Concern | Components | Responsibility Split |
|---|---|---|
| Validation | Student Request Interface, Reviewer Interface, Request Processing Logic | Interfaces may provide user-friendly checks, while Request Processing Logic performs authoritative validation |
| Role handling | Student Request Interface, Reviewer Interface, Request Processing Logic | Interfaces present role-appropriate actions; Request Processing Logic remains the authoritative enforcement point |
| Error handling | Interfaces, Request Processing Logic, Persistence Layer | Lower layers report failures upward; application logic interprets failures; interfaces communicate relevant failures to users |
| Logging / history | Request Processing Logic, Persistence Layer, Persistent Data Store | Application logic determines important workflow events; persistence records the required history; exact depth remains subject to Q-007 |
| Traceability | All major components | Component behavior should remain linked to requirements, interface contracts, tests, and review evidence as implementation develops |

## Component Changes

No material component-boundary changes have been recorded yet.

| Effective Gate | Component | Change | Reason | Related Decision |
|---|---|---|---|---|
| A3 | All Cycle 1 components | Initial component-responsibility baseline established | Provide clear ownership and boundaries before implementation accelerates | No formal ADR yet |

## Expectations

- Use the same component names throughout architecture evidence.
- Assign clear primary responsibilities.
- Make important non-responsibilities explicit where ambiguity could matter.
- Identify meaningful architectural dependencies.
- Document important failure responsibilities.
- Link components to relevant requirements and interface contracts.
- Avoid duplicating source-code structure without architectural meaning.
- Avoid vague shared ownership of critical responsibilities.
- Update component boundaries when the architecture changes.