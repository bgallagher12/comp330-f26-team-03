# Architecture Review — Gate A3

## Review Identification

- **Project:** Campus Connect, COMP 330 Team 03
- **Gate:** A3 — Architecture and Review Package
- **Assessment date:** 2026-10-22
- **Original document author:** Brendan Gallagher
- **Follow-up reviewer:** Carlos Alcala
- **Status:** Follow-up assessment complete; formal team decisions remain pending
- **Architecture baseline:** Current main branch, incorporating PRs #20, #22, #23, and #24

## Review Scope

This assessment reviews the planned Cycle 1 architecture, including:

- `docs/architecture/architecture.md`
- `docs/architecture/architecture-diagram.png`
- `docs/architecture/component-responsibilities.md`
- `docs/architecture/api-contracts.md`
- `docs/architecture/data-context.md`
- `docs/decisions/adr-0001-use-synthetic-data-for-cycle-1.md`
- Relevant requirements, risks, and planning evidence

The review evaluates documentation readiness, architectural boundaries,
traceability, and unresolved decisions. It does not certify implementation
or successful integration testing.

## Architecture Summary

Campus Connect is planned as a layered student support request system.

The five documented components are:

1. Student Request Interface
2. Reviewer Interface
3. Request Processing Logic
4. Persistence Layer
5. Persistent Data Store

The interfaces depend on application logic, which coordinates workflow
rules and persistence. The user interfaces must not directly modify
authoritative request data.

The current design documents seven proposed interfaces (API-001 through
API-007). Cycle 1 assumes synthetic or approved sample data and may use
simulated student and reviewer roles.

No user-facing AI component is included in the Cycle 1 architecture.

## Follow-up Findings

| ID | Original Concern | Updated Assessment | Remaining Action | Evidence |
|---|---|---|---|---|
| ARF-001 | Architecture documentation contained starter examples | Partially addressed: PR #22 documented a project-specific five-component design; PR #24 supplied the architecture diagram | Confirm diagram consistency, technology choices, and implementation boundaries | PR #22, PR #24 |
| ARF-002 | Component responsibilities were starter examples | Partially addressed: PR #22 documented components, ownership boundaries, dependencies, and failure responsibilities | Verify responsibilities against implemented components and finalize unresolved access and data decisions | PR #22 |
| ARF-003 | API contracts were starter examples | Partially addressed: PR #22 documented API-001 through API-007, including intended inputs, outputs, and failure behavior | Finalize required fields, permissions, transitions, concrete protocols, and integration verification | PR #22 |

**Disposition:** The original starter-documentation gaps have been
substantially addressed in design documents. Remaining implementation
and decision gaps remain open. This is not an assertion that those gaps
are closed or that the architecture has received final approval.

## Requirements and Component Alignment

| Workflow | Documented Component or Interface | Verification Status |
|---|---|---|
| Submit support request | Student Request Interface; API-001 | Planned; implementation not verified here |
| Retrieve request status | Student Request Interface; API-002 | Planned; implementation not verified here |
| Reviewer request access | Reviewer Interface; API-003 | Planned; role controls need confirmation |
| Update request status | Request Processing Logic; API-004 | Planned; transitions require confirmation |
| Record notes or resolution | Reviewer Interface; API-005 | Planned; resolution criteria require confirmation |
| Store and retrieve records | Persistence Layer; API-006 and API-007 | Planned; storage technology unresolved |

## Data, Security, and Testing Review

The proposed architecture separates interface behavior from application
workflow policy and storage access.

Remaining concerns include:

- Confirming the minimum required request fields and valid status transitions.
- Establishing student and reviewer permission boundaries.
- Selecting the persistence technology and final data model.
- Defining history, retention, and logging expectations.
- Verifying negative paths, unauthorized operations, storage failures,
  and an actual integrated request workflow.

The test strategy documents planned verification. It does not, by
itself, demonstrate passing tests or a working integrated application.

## Architecture Decision Record

**ADR-0001 — Use Synthetic Data for Cycle 1**

- **Current status:** Proposed
- **Primary owner:** Brendan Gallagher
- **Backup:** Carlos Alcala
- **Next action:** Team discussion to confirm actual alternatives
  considered, rationale, and final decision.

Do not mark the ADR Accepted until the team has made and recorded
that decision.

## Required Follow-up Actions

| ID | Action | Proposed Primary | Proposed Backup | Status |
|---|---|---|---|---|
| ARA-001 | Verify architecture diagram and component naming against current architecture documents | Carlos | Brendan | Pending verification |
| ARA-002 | Finalize permissions and request-data boundaries | Sherry | Carlos | Planned |
| ARA-003 | Finalize request fields, status transitions, and resolution criteria | Jaylen | Sanjana | Planned |
| ARA-004 | Confirm persistence technology and integration contract | Sanjana | Jaylen | Planned |
| ARA-005 | Confirm ADR-0001 alternatives and decision | Brendan | Carlos | Proposed |
| ARA-006 | Execute and record integration and negative-path verification | Sanjana | Sherry | Planned |

These owner assignments are proposed for confirmation at the next
team meeting. Completion evidence must reference actual commits,
tests, reviews, or issues before actions are marked complete.

## Review Evidence

- [PR #20 — Architecture documentation](https://github.com/bgallagher12/comp330-f26-team-03/pull/20)
- [PR #22 — Architecture baseline](https://github.com/bgallagher12/comp330-f26-team-03/pull/22)
- [PR #23 — Planning and testing updates](https://github.com/bgallagher12/comp330-f26-team-03/pull/23)
- [PR #24 — Diagram and re-estimation](https://github.com/bgallagher12/comp330-f26-team-03/pull/24)
- [Issue #19 — Architecture and planning follow-up](https://github.com/bgallagher12/comp330-f26-team-03/issues/19)

## Review Conclusion

The architecture documentation has progressed from starter examples
to a project-specific design with identified components, contracts,
data boundaries, and review findings.

ARF-001 through ARF-003 are partially addressed at the documentation
level. Significant decisions and verification work remain open.

**Outcome:** Documentation baseline suitable for continued review;
final architecture approval, implementation completion, and integration
readiness are not claimed.

The team should confirm outstanding decisions, assignments, and
acceptance evidence before changing the status of any open finding.
