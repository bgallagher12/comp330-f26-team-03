# Estimates

## Estimation Approach

The team uses person-hours and three-point estimates to represent expected effort.

Low estimate: work proceeds with few unexpected problems.
Likely estimate: the team's current best estimate under normal conditions.
High estimate: additional effort is required because of reasonable technical, integration, or requirements uncertainty.

Estimates are based on the current task scope, known dependencies, and unresolved requirements. They are initial planning estimates and may be refined as implementation provides additional evidence.

## Estimates

| ID | Work Item | Low | Likely | High | Basis | Assumptions / Dependencies | Owner(s) | Status |
|---|---|---:|---:|---:|---|---|---|---|
| EST-001 | Issue #3 - Design Initial Backend Request Processing Logic | 4 hrs | 7 hrs | 12 hrs | Backend work covers request creation, retrieval, reviewer updates, status changes, resolution information, and role behavior | Depends on request fields, status model, role permissions, and persistence approach being clarified | @jaylene05, @SanjGurl16 | Initial |
| EST-002 | Issue #4 - Create Student Request Frontend Page | 3 hrs | 5 hrs | 8 hrs | Frontend work includes request input, submission behavior, validation feedback, and student-facing request information | Depends on required request fields and backend interface being defined | @sh3rry19 | Initial |
| EST-003 | Issue #5 - Create ER Diagram and Initial Database | 3 hrs | 5 hrs | 9 hrs | Work includes identifying required entities/fields, creating the ER design, establishing persistence, and supporting request retrieval | Depends on request data fields, unique identifier approach, status/history needs, and backend expectations | @CarlosA019 | Initial |

## Estimation Assumptions

| Assumption Reference | Estimate(s) Affected | Effect if Incorrect |
|---|---|---|
| ASM-001 | EST-001, EST-002, EST-003 | If real or private university data were required, additional security, privacy, testing, and data-handling work would increase effort |
| ASM-002 | EST-001, EST-002 | If real institutional authentication were required, backend access control and frontend role handling would require significantly more work |
| ASM-003 | EST-001, EST-002, EST-003 | If requests require multiple simultaneous statuses or a more complex state model, backend logic, database design, interface behavior, and tests would need to be revised |
| ASM-004 | EST-001, EST-002, EST-003 | If Cycle 1 expands beyond one narrow support-request workflow, implementation and testing effort would increase across all major tasks |

## Estimate Confidence

Confidence levels are interpreted as follows:

- High: the work is narrowly scoped and major dependencies are understood.
- Medium: the main work is understood, but some requirements or integration details remain unresolved.
- Low: major requirements, dependencies, or technical decisions remain unresolved.

| Estimate ID | Confidence | Reason |
|---|---|---|
| EST-001 | Low | Backend work depends on unresolved questions Q-002, Q-003, Q-004, Q-006, Q-007, and Q-008 |
| EST-002 | Medium | Frontend work is generally understood, but Q-001, Q-004, Q-005, Q-006, and Q-008 may change the scope |
| EST-003 | Medium | Database work is understood at a high level, but Q-001, Q-002, Q-007, and Q-008 may change the data model or persistence approach |

## Estimate Changes

No material estimate changes have been recorded at the A2 planning gate. Changes will be recorded here when implementation evidence causes an estimate to be revised.

## Estimate vs. Actual

No estimated work items have sufficient completion evidence for an estimate-versus-actual comparison at the A2 planning gate. Actual effort and variance will be recorded as work is completed.

## Planning Implications

| Estimate / Evidence | Planning Impact | Related Scope / Schedule / Risk |
|---|---|---|
| EST-001 has a wide 4-12 hour range and low confidence | Backend work should be refined into smaller tasks as status, role, persistence, and resolution decisions are finalized | Broad backend scope may create schedule and integration risk |
| EST-002 depends on backend interface decisions | Coordinate frontend and backend expectations before implementation progresses too far | Reduces risk of rework between Issues #3 and #4 |
| EST-003 depends on unresolved data and history requirements | Finalize the minimum request data model before database implementation is completed | Reduces risk of database redesign and rework |