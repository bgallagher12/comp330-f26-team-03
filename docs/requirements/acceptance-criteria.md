# Acceptance Criteria

This document defines observable conditions used to verify the initial CampusConnect Cycle 1 requirements.

## Acceptance Criteria

| ID            | Requirement | Acceptance Criterion                                                                                                                                                                                    | Verification                   | Status   |
| ------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | -------- |
| AC-REQ-001-01 | REQ-001     | Given a student requester and valid required information, when the student submits a support request, then the system creates the request.                                                              | Test / demonstration           | Proposed |
| AC-REQ-001-02 | REQ-001     | Given a support request missing required information, when the student attempts to submit it, then the system does not create the request and identifies the missing information.                       | Test / demonstration           | Proposed |
| AC-REQ-002-01 | REQ-002     | Given two successfully submitted requests, when the requests are stored, then each request has a unique identifier and can be retrieved later.                                                          | Automated test / demonstration | Proposed |
| AC-REQ-003-01 | REQ-003     | Given a submitted support request, when a support reviewer views available requests, then the reviewer can access the request and its submitted information.                                            | Test / demonstration           | Proposed |
| AC-REQ-004-01 | REQ-004     | Given an existing support request, when a support reviewer changes its status, then the new status is stored successfully.                                                                              | Automated test / demonstration | Proposed |
| AC-REQ-004-02 | REQ-004     | Given a request whose status was changed by a reviewer, when the request is viewed afterward, then the updated status is displayed.                                                                     | Test / demonstration           | Proposed |
| AC-REQ-005-01 | REQ-005     | Given an existing support request, when a reviewer records a note or resolution, then that information is saved with the request.                                                                       | Automated test / demonstration | Proposed |
| AC-REQ-006-01 | REQ-006     | Given a student requester with a submitted request, when the student views that request, then the current status and available resolution information are displayed.                                    | Test / demonstration           | Proposed |
| AC-REQ-007-01 | REQ-007     | Given a student requester, when the student uses the system, then reviewer-only actions such as changing request status are not available to the student.                                               | Role test / demonstration      | Proposed |
| AC-REQ-007-02 | REQ-007     | Given a support reviewer, when the reviewer accesses a submitted request, then reviewer actions required for the workflow are available.                                                                | Role test / demonstration      | Proposed |
| AC-REQ-008-01 | REQ-008     | Given a request with an important status change or reviewer action, when its history is inspected, then enough information is available to determine what action occurred.                              | Inspection / demonstration     | Proposed |
| AC-REQ-009-01 | REQ-009     | Given the CampusConnect Cycle 1 system and project data, when the repository and application data are reviewed, then the system operates without requiring real student records or private Loyola data. | Repository / data review       | Proposed |

## Verification Guidance

Acceptance criteria should be verified using evidence appropriate to the behavior being tested.

Verification may include:

* automated tests;
* integration tests;
* manual demonstrations;
* role and permission checks;
* repository inspection; or
* other documented verification methods.

As implementation develops, verification methods may become more specific and should reference actual test evidence where appropriate.

## Traceability

Each acceptance criterion references its corresponding requirement in:

`/docs/requirements/requirements.md`

As requirements change, the team should review related acceptance criteria to ensure they remain accurate and testable.

Acceptance criteria should describe observable behavior rather than implementation details.

