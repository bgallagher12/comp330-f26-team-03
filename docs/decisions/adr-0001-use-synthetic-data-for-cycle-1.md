# ADR-0001: Use Synthetic Data for Cycle 1

**Status:** Proposed  
**Date:** 2026-10-14  
**Decision Owners:** Brendan Gallagher (Primary), Carlos Alcala (Backup)

## Context

Campus Connect is a student support request and workflow system developed by Team 03 for COMP 330 at Loyola University Chicago.

The application allows students to submit support requests and track their progress. Support reviewers can view requests, update statuses, and record notes and resolutions.

For Cycle 1, the team needs to demonstrate a complete request workflow, including request submission, unique request identification, reviewer processing, status updates, and resolution tracking.

Because support requests may contain sensitive student information, the team must determine how to represent and manage request data during development and testing.

## Decision

Campus Connect will use synthetic student support request data for Cycle 1 rather than real student records.

Synthetic data will represent the information necessary to test the application's request submission, review, status update, and resolution workflow.

This approach allows the team to develop and demonstrate the system without requiring actual student support records.

## Alternatives Considered

**Pending team confirmation:** The README establishes the use of synthetic data but does not identify the alternatives considered or why they were rejected.

Before accepting this ADR, the team should document the alternatives actually evaluated, their advantages and disadvantages, and the reasons for selecting synthetic data.

## Consequences

### Positive

- Reduces the risk of exposing real student information during development.
- Allows the team to create predictable test scenarios.
- Supports testing the complete request workflow without accessing university records.
- Simplifies the preparation of demonstration data.

### Negative / Trade-Offs

- Synthetic data may not represent every scenario encountered with real student requests.
- Additional testing would be necessary before using the application with real student information.
- The team must ensure that synthetic data represents realistic request scenarios.
- Privacy and access-control requirements still need to be addressed even though Cycle 1 uses synthetic data.

## Evidence

- `README.md` — Describes the Campus Connect project, Cycle 1 scope, and use of synthetic data.
- `docs/requirements/` — Location of functional requirements and acceptance criteria.
- `docs/architecture/data-context.md` — Documents data ownership, sensitive information, visibility limits, and logging expectations.

The latter two locations should be checked for supporting content before this ADR is approved.

## Revisit Conditions

This decision should be reconsidered if:

- A future release requires integration with actual university support records.
- Project requirements introduce real student data.
- Testing demonstrates that the synthetic dataset is insufficient to validate important workflows.
- New security, privacy, or institutional requirements change the application's data-handling obligations.