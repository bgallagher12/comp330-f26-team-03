# API and Interface Contracts

## Contract Summary

| ID | Consumer | Provider | Purpose | Interface / Protocol | Related Requirements | Status |
|---|---|---|---|---|---|---|
| API-001 | Student Request Interface | Request Processing Logic | Submit a new support request | Internal application interface; exact protocol TBD | REQ-001 | Proposed |
| API-002 | Student Request Interface | Request Processing Logic | Retrieve a student's request status and available resolution information | Internal application interface; exact protocol TBD | REQ-006 | Proposed |
| API-003 | Reviewer Interface | Request Processing Logic | Retrieve submitted support requests for review | Internal application interface; exact protocol TBD | REQ-003 | Proposed |
| API-004 | Reviewer Interface | Request Processing Logic | Update the status of a support request | Internal application interface; exact protocol TBD | REQ-004, REQ-007 | Proposed |
| API-005 | Reviewer Interface | Request Processing Logic | Record a reviewer note or resolution | Internal application interface; exact protocol TBD | REQ-005, REQ-007 | Proposed |
| API-006 | Request Processing Logic | Persistence Layer | Create, retrieve, and update persistent request records | Internal persistence interface | REQ-002, REQ-004, REQ-005, REQ-006, REQ-008 | Proposed |
| API-007 | Persistence Layer | Persistent Data Store | Store and retrieve durable request and workflow data | Database interface; technology TBD | REQ-002, REQ-004, REQ-005, REQ-006, REQ-008, REQ-009 | Proposed |

## Detailed Contracts

### API-001 — Submit Support Request

**Consumer:** Student Request Interface  
**Provider:** Request Processing Logic  
**Purpose:** Submit a new student support request for validation and creation.  
**Related Requirements:** `REQ-001`  
**Status:** Proposed

#### Interaction

The Student Request Interface sends student-provided request information to the Request Processing Logic.

The exact transport mechanism remains unresolved until the technology stack is selected under `Q-008`.

#### Request / Input

The request contains the support-request information collected from the student.

The exact required fields remain unresolved under `Q-001`.

#### Response / Output

On successful creation, the Request Processing Logic returns enough information for the interface to confirm that the request was created, including the request's unique identifier and current status when available.

#### Failure Behavior

The operation must fail when required information is missing or invalid.

When required information is missing, the response must identify enough information for the Student Request Interface to explain the problem to the student.

A failed operation must not create a support request.

#### Authentication / Authorization

Cycle 1 may use simulated roles under `ASM-002`.

Only behavior associated with the student requester role may initiate this contract.

#### Contract Rules

- Valid required information results in creation of a support request.
- Missing required information must not create a request.
- A successful creation must produce a unique request identifier.
- The interface must not display a successful submission unless the Request Processing Logic confirms creation.
- Only synthetic or approved sample data may be used.

#### Verification

- `AC-REQ-001-01`
- `AC-REQ-001-02`
- Related unique-identifier behavior: `AC-REQ-002-01`

#### Notes / Open Questions

- `Q-001` — Required request information.
- `Q-005` — Handling missing or incomplete information.
- `Q-008` — Technology stack and concrete interface protocol.

---

### API-002 — Retrieve Student Request Status

**Consumer:** Student Request Interface  
**Provider:** Request Processing Logic  
**Purpose:** Retrieve a submitted request's current status and available resolution information for the student requester.  
**Related Requirements:** `REQ-006`, `REQ-007`  
**Status:** Proposed

#### Interaction

The Student Request Interface requests information for an existing submitted support request.

#### Request / Input

The consumer provides information sufficient to identify the requested support request.

A request identifier is expected to be used, although the final interface form depends on the implementation selected under `Q-008`.

#### Response / Output

The provider returns:

- the request's current status; and
- available resolution information associated with the request.

#### Failure Behavior

Relevant failures may include:

- the request cannot be found;
- the requester is not permitted to view the request; or
- stored request information cannot be retrieved.

The interface must not fabricate or display stale information as authoritative when retrieval fails.

#### Authentication / Authorization

The provider determines whether the current simulated student role may view the identified request.

The Student Request Interface is not the authoritative permission boundary.

#### Contract Rules

- Returned status must reflect authoritative stored state.
- Only information permitted for the student requester should be returned.
- Reviewer-only actions must not be exposed through this contract.

#### Verification

- `AC-REQ-006-01`
- `AC-REQ-007-01`

#### Notes / Open Questions

- `Q-004` — Student vs. reviewer permissions.
- `Q-006` — Resolution conditions and available resolution information.
- `Q-008` — Technology stack and concrete interface protocol.

---

### API-003 — Retrieve Submitted Requests for Review

**Consumer:** Reviewer Interface  
**Provider:** Request Processing Logic  
**Purpose:** Allow a support reviewer to access submitted support requests and their submitted information.  
**Related Requirements:** `REQ-003`, `REQ-007`  
**Status:** Proposed

#### Interaction

The Reviewer Interface requests submitted support-request information from the Request Processing Logic.

#### Request / Input

The consumer provides reviewer role context and, where appropriate, a request identifier or request-selection input.

#### Response / Output

The provider returns request information that the reviewer is permitted to inspect.

#### Failure Behavior

Relevant failures may include:

- request not found;
- reviewer role is not permitted to access the request;
- stored request information cannot be retrieved.

#### Authentication / Authorization

The operation is available only to the support reviewer role.

Cycle 1 may simulate reviewer identity and role behavior under `ASM-002`.

#### Contract Rules

- Student requester behavior must not receive reviewer-only capabilities through this contract.
- Returned request information must come from authoritative application state.
- The Reviewer Interface must not directly access the Persistent Data Store.

#### Verification

- `AC-REQ-003-01`
- `AC-REQ-007-02`

#### Notes / Open Questions

- `Q-004` — Exact reviewer permissions.
- `Q-008` — Technology stack and concrete interface protocol.

---

### API-004 — Update Request Status

**Consumer:** Reviewer Interface  
**Provider:** Request Processing Logic  
**Purpose:** Request a change to the current status of an existing support request.  
**Related Requirements:** `REQ-004`, `REQ-007`, `REQ-008`  
**Status:** Proposed

#### Interaction

The Reviewer Interface sends a requested status change for an existing support request.

#### Request / Input

The operation requires:

- identification of the target request;
- the requested new status; and
- reviewer role context.

#### Response / Output

On success, the provider returns confirmation of the stored status change and the resulting current status.

#### Failure Behavior

Relevant failures may include:

- request not found;
- unsupported status;
- invalid status transition;
- caller is not permitted to change status; or
- status could not be persisted.

A failed update must not be represented as successful.

#### Authentication / Authorization

Only the support reviewer role may perform reviewer status changes.

The Request Processing Logic is the authoritative enforcement point.

#### Contract Rules

- The new status must be valid under the final status model.
- Invalid transitions must not modify stored state.
- Successful status changes must be persisted.
- The updated status must be returned accurately when the request is later viewed.
- Important status changes may require history evidence under `REQ-008`.

#### Verification

- `AC-REQ-004-01`
- `AC-REQ-004-02`
- `AC-REQ-007-01`
- `AC-REQ-007-02`
- Related history behavior: `AC-REQ-008-01`

#### Notes / Open Questions

- `Q-002` — Supported request statuses.
- `Q-003` — Valid status transitions.
- `Q-007` — Required status-change history.

---

### API-005 — Record Reviewer Note or Resolution

**Consumer:** Reviewer Interface  
**Provider:** Request Processing Logic  
**Purpose:** Save a reviewer note or resolution with an existing support request.  
**Related Requirements:** `REQ-005`, `REQ-006`, `REQ-007`, `REQ-008`  
**Status:** Proposed

#### Interaction

The Reviewer Interface sends reviewer-provided note or resolution information for an existing support request.

#### Request / Input

The operation requires:

- identification of the target request;
- note or resolution information; and
- reviewer role context.

#### Response / Output

On success, the provider confirms that the reviewer information has been associated with the request.

#### Failure Behavior

Relevant failures may include:

- request not found;
- caller is not permitted to modify reviewer information;
- submitted information is invalid; or
- information could not be persisted.

#### Authentication / Authorization

Only reviewer-authorized behavior may create or modify reviewer notes or resolution information.

#### Contract Rules

- Reviewer information must be stored with the correct request.
- A failed persistence operation must not be reported as successful.
- Student-visible resolution information must follow the final visibility rules.
- Important reviewer actions may require history evidence under `REQ-008`.

#### Verification

- `AC-REQ-005-01`
- `AC-REQ-006-01`
- `AC-REQ-007-02`
- Related history behavior: `AC-REQ-008-01`

#### Notes / Open Questions

- `Q-004` — Role permissions and visibility.
- `Q-006` — Definition of a resolved request.
- `Q-007` — Required reviewer-action history.

---

### API-006 — Request Persistence Operations

**Consumer:** Request Processing Logic  
**Provider:** Persistence Layer  
**Purpose:** Create, retrieve, and update durable CampusConnect request records.  
**Related Requirements:** `REQ-002`, `REQ-004`, `REQ-005`, `REQ-006`, `REQ-008`  
**Status:** Proposed

#### Interaction

The Request Processing Logic sends persistence operations to the Persistence Layer rather than accessing the Persistent Data Store directly.

#### Request / Input

Operations may include:

- create a request;
- retrieve a request;
- store an updated status;
- store reviewer note or resolution information; and
- record required workflow-history information.

Exact method signatures and schemas remain dependent on the final implementation.

#### Response / Output

The Persistence Layer returns:

- stored or retrieved request information;
- persistence confirmation; or
- a persistence failure.

#### Failure Behavior

Relevant failures may include:

- requested record does not exist;
- data cannot be stored;
- data cannot be retrieved; or
- the Persistent Data Store is unavailable.

Persistence failures must be reported to the Request Processing Logic.

#### Authentication / Authorization

This is an internal application boundary.

User-role authorization should already be evaluated by the Request Processing Logic before state-changing persistence operations are requested.

#### Contract Rules

- Created requests must preserve a unique identifier.
- Retrieved records must correspond to stored authoritative state.
- Failed writes must not be reported as successful.
- Persistence behavior must support the required status, resolution, and history information defined for Cycle 1.

#### Verification

- `AC-REQ-002-01`
- `AC-REQ-004-01`
- `AC-REQ-004-02`
- `AC-REQ-005-01`
- `AC-REQ-006-01`
- `AC-REQ-008-01`

#### Notes / Open Questions

- `Q-001` — Request data fields.
- `Q-002` / `Q-003` — Status model.
- `Q-007` — Required history depth.
- `Q-008` — Database and implementation technology.

---

### API-007 — Persistent Data Store Boundary

**Consumer:** Persistence Layer  
**Provider:** Persistent Data Store  
**Purpose:** Store and retrieve durable CampusConnect Cycle 1 data.  
**Related Requirements:** `REQ-002`, `REQ-004`, `REQ-005`, `REQ-006`, `REQ-008`, `REQ-009`  
**Status:** Proposed

#### Interaction

The Persistence Layer communicates with the selected persistent storage technology.

The database or storage technology has not yet been finalized.

#### Request / Input

Persistent data may include:

- support-request information;
- unique request identifier;
- current request status;
- reviewer note or resolution information; and
- required workflow-history information.

#### Response / Output

The data store returns persisted or retrieved records, or an identifiable storage failure.

#### Failure Behavior

Relevant failures include:

- storage unavailable;
- write failure;
- retrieval failure; or
- requested record does not exist.

Failures must propagate through the Persistence Layer rather than being silently ignored.

#### Authentication / Authorization

The Persistent Data Store is not directly exposed to student or reviewer interfaces.

Only the Persistence Layer should access this boundary in the current architecture.

#### Contract Rules

- Data must remain durable enough to support later request retrieval.
- Unique identifiers must remain associated with the correct request.
- Stored status and resolution information must represent confirmed application state.
- Only synthetic or approved sample data may be stored for Cycle 1.

#### Verification

- `AC-REQ-002-01`
- `AC-REQ-004-01`
- `AC-REQ-005-01`
- `AC-REQ-006-01`
- `AC-REQ-008-01`
- `AC-REQ-009-01`

#### Notes / Open Questions

- `Q-007` — Required workflow-history depth.
- `Q-008` — Database technology and persistence implementation.

## Data Contract Guidance

The detailed request-data schema is not yet finalized because required request fields remain unresolved under `Q-001` and the technology stack remains unresolved under `Q-008`.

Once those decisions are finalized, the team should maintain one authoritative definition of the request data contract and reference it from this document rather than maintaining conflicting duplicate schemas.

## Failure Contracts

Important contract failures for Cycle 1 include:

| Failure Condition | Responsible Boundary | Expected Behavior |
|---|---|---|
| Missing required request information | API-001 / Request Processing Logic | Reject submission, do not create the request, and identify missing information |
| Request not found | API-002, API-003, API-004, API-005 | Report that the requested record could not be found and do not fabricate state |
| Unauthorized role action | API-002 through API-005 / Request Processing Logic | Reject the operation without modifying protected state |
| Unsupported or invalid status transition | API-004 / Request Processing Logic | Reject the transition and preserve the existing status |
| Persistence failure | API-006, API-007 | Report failure upward and do not report the operation as successfully persisted |
| Private or real university data introduced | System-wide constraint | Reject or remove the data from Cycle 1 project use and review compliance with ASM-001 and REQ-009 |

## Security Boundaries

Cycle 1 uses simulated student requester and support reviewer roles under `ASM-002`; production institutional authentication is outside the current scope.

The following security boundaries still apply:

- User interfaces are not authoritative authorization boundaries.
- Request Processing Logic determines whether role-specific actions are allowed.
- Reviewer-only actions must not be made available to the student requester role.
- Student and reviewer interfaces must not directly access the Persistent Data Store.
- Persistent data must use only synthetic or approved sample information under `ASM-001` and `REQ-009`.
- Role and visibility rules must be updated when `Q-004` is resolved.

## Contract Compatibility and Change

No material contract changes have been recorded yet.

| Effective Gate | Contract | Change | Compatibility Impact | Related Evidence |
|---|---|---|---|---|
| A3 | API-001 through API-007 | Initial Cycle 1 interface-contract baseline established | Initial baseline; no earlier accepted contracts replaced | REQ-001 through REQ-009 |

## Verification and Traceability

Interface contracts are currently proposed architecture evidence. They should not be marked `Verified` until implementation and reviewable verification evidence exist.

Expected traceability includes:

- `REQ-001` → `AC-REQ-001-01`, `AC-REQ-001-02` → `API-001`
- `REQ-002` → `AC-REQ-002-01` → `API-006`, `API-007`
- `REQ-003` → `AC-REQ-003-01` → `API-003`
- `REQ-004` → `AC-REQ-004-01`, `AC-REQ-004-02` → `API-004`, `API-006`
- `REQ-005` → `AC-REQ-005-01` → `API-005`, `API-006`
- `REQ-006` → `AC-REQ-006-01` → `API-002`, `API-006`
- `REQ-007` → `AC-REQ-007-01`, `AC-REQ-007-02` → `API-002`, `API-003`, `API-004`, `API-005`
- `REQ-008` → `AC-REQ-008-01` → `API-004`, `API-005`, `API-006`, `API-007`
- `REQ-009` → `AC-REQ-009-01` → `API-007`

Implementation and test references should be added as the contracts move from Proposed to Implemented and Verified.

## Expectations

- Use stable identifiers for significant interface contracts.
- Use component names consistent with the architecture.
- Identify both consumer and provider.
- Describe meaningful input and output behavior.
- Document important failure behavior.
- Make security expectations explicit where relevant.
- Link contracts to requirements and acceptance criteria.
- Reference authoritative schemas rather than creating unnecessary duplicate definitions.
- Update both sides of a contract when it changes.
- Add verification evidence as implementation matures.
- Record unresolved behavior explicitly rather than inventing contract details.