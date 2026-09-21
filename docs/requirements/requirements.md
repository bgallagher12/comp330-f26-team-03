# Requirements

This document defines the initial requirements for the CampusConnect Cycle 1 vertical slice.

CampusConnect is a student support request and workflow system. The Cycle 1 goal is to provide a small, controlled workflow that allows a student to submit a support request and allows a support reviewer to review, update, and resolve that request.

## Requirements

| ID      | Requirement                                                                                                                         | Rationale                                                                                                 | Priority | Acceptance Criteria Reference | Status   |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | -------- | ----------------------------- | -------- |
| REQ-001 | The system shall allow a student requester to create and submit a support request using synthetic data.                             | Students need a single, structured way to initiate a support request.                                     | Must     | AC-REQ-001-01, AC-REQ-001-02  | Proposed |
| REQ-002 | The system shall assign each submitted support request a unique identifier and preserve the request for later retrieval.            | Requests must be distinguishable and available throughout the workflow.                                   | Must     | AC-REQ-002-01                 | Proposed |
| REQ-003 | The system shall allow a support reviewer to view submitted support requests.                                                       | Reviewers need access to requests in order to evaluate and process them.                                  | Must     | AC-REQ-003-01                 | Proposed |
| REQ-004 | The system shall allow a support reviewer to update the status of a support request.                                                | Students and reviewers need a clear indication of where a request is in the workflow.                     | Must     | AC-REQ-004-01, AC-REQ-004-02  | Proposed |
| REQ-005 | The system shall allow a support reviewer to record a note or resolution for a support request.                                     | The system must preserve the outcome or relevant reviewer information associated with a request.          | Must     | AC-REQ-005-01                 | Proposed |
| REQ-006 | The system shall allow a student requester to view the current status and available resolution information for a submitted request. | Students need visibility into what is happening with their request without relying on informal follow-up. | Must     | AC-REQ-006-01                 | Proposed |
| REQ-007 | The system shall distinguish student requester behavior from support reviewer behavior.                                             | The two roles have different responsibilities and should not have identical capabilities.                 | Must     | AC-REQ-007-01, AC-REQ-007-02  | Proposed |
| REQ-008 | The system shall preserve enough information about important status changes and reviewer actions for those actions to be inspected. | The workflow must remain reviewable and provide evidence of what happened to a request.                   | Should   | AC-REQ-008-01                 | Proposed |
| REQ-009 | The system shall use only synthetic or approved sample data and shall not require real student records or private university data.  | The project must avoid handling real student records, grades, or other private institutional information. | Must     | AC-REQ-009-01                 | Proposed |

## Requirement Quality

Requirements should remain:

* clear;
* concise;
* unambiguous;
* necessary;
* feasible;
* traceable; and
* verifiable.

Requirements should describe what the system must accomplish without unnecessarily prescribing the implementation technology.

## Requirements and Design

These requirements describe system obligations rather than specific implementation choices.

Technology stack, database selection, application structure, authentication approach, and other implementation decisions will be documented separately as the team makes those decisions.

## Requirements and Uncertainty

Several CampusConnect details are intentionally left for the team to determine, including:

* what information a support request must contain;
* which request statuses will be used;
* which status transitions are valid;
* how incomplete information will be handled;
* what each role may view or modify;
* what qualifies a request as resolved; and
* what level of history or logging is necessary.

Unresolved decisions will be maintained in:

`/docs/requirements/assumptions-open-questions.md`

## Requirements and Acceptance Criteria

Each requirement is linked to one or more observable acceptance criteria maintained in:

`/docs/requirements/acceptance-criteria.md`

Acceptance criteria define how the team can demonstrate that a requirement has been satisfied.

Requirements and acceptance criteria should remain traceable in both directions as the project changes.

## Scope

The initial requirements intentionally focus on the required Cycle 1 vertical slice.

Features such as enterprise authentication, live Loyola integrations, email or text-message integration, advanced analytics, user-facing AI, complex machine learning, and production-scale deployment are not part of the initial Cycle 1 requirements unless separately approved and documented.

## Expectations

* Maintain unique requirement identifiers.
* Keep requirements current as project understanding changes.
* Record rationale for each requirement.
* Assign meaningful priorities.
* Link requirements to acceptance criteria.
* Record unresolved uncertainty instead of inventing details.
* Preserve traceability when requirements change, are deferred, or are removed.

