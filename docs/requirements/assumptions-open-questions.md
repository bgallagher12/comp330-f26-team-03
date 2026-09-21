# Assumptions and Open Questions

This document records important assumptions and unresolved questions for the CampusConnect project.

Assumptions are items the team is currently treating as true but may still need confirmation. Open questions are decisions the team has not yet made.

## Assumptions

| ID      | Assumption                                                                                                                        | Basis                                                  | Related Evidence | Impact if Incorrect                                                                    | Owner   | Status      |
| ------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------- | ------- | ----------- |
| ASM-001 | CampusConnect will use synthetic sample data rather than real Loyola student records or private university data.                  | CampusConnect project constraints                      | REQ-009          | Data handling, testing, and security expectations would need to be reconsidered.       | Jaylen  | Validated   |
| ASM-002 | Student requester and support reviewer roles may be simulated during Cycle 1 rather than using real institutional authentication. | CampusConnect project constraints                      | REQ-007          | Authentication and access-control scope would increase significantly.                  | Brendan | Validated   |
| ASM-003 | Each support request will have one current workflow status at a time.                                                             | Initial interpretation of the required status workflow | REQ-004, REQ-006 | The status model, interface, and tests may require redesign.                           | Brendan | Unvalidated |
| ASM-004 | Cycle 1 will focus on one narrow support-request workflow rather than multiple unrelated campus services.                         | Required Cycle 1 scope                                 | REQ-001–REQ-009  | Requirements and implementation scope could grow beyond what is realistic for Cycle 1. | Carlos  | Validated   |

## Assumption Status

Assumptions may use the following states:

* **Unvalidated** — currently treated as true but not yet confirmed;
* **Validated** — supported by project guidance or team evidence;
* **Invalidated** — evidence shows the assumption was incorrect; or
* **Superseded** — replaced by a later decision or understanding.

When an assumption changes, related requirements, architecture, plans, tests, or risks should be reviewed.

## Open Questions

| ID    | Question                                                                                              | Related Evidence              | Owner   | Needed By | Status / Resolution |
| ----- | ----------------------------------------------------------------------------------------------------- | ----------------------------- | ------- | --------- | ------------------- |
| Q-001 | What information must a student provide when submitting a support request?                            | REQ-001                       | Sherry  | A2        | Open                |
| Q-002 | Which request statuses will CampusConnect support?                                                    | REQ-004, REQ-006              | Brendan | A2        | Open                |
| Q-003 | Which transitions between request statuses will be allowed?                                           | REQ-004                       | Brendan | A3        | Open                |
| Q-004 | What information and actions may a student requester view or modify compared with a support reviewer? | REQ-007                       | Sanjana | A3        | Open                |
| Q-005 | How should the system handle a request with missing or incomplete information?                        | REQ-001                       | Sherry  | A2        | Open                |
| Q-006 | What conditions determine when a support request is considered resolved?                              | REQ-005, REQ-006              | Sanjana | A2        | Open                |
| Q-007 | What status-change or reviewer-action history must CampusConnect preserve?                            | REQ-008                       | Jaylen  | A3        | Open                |
| Q-008 | What technology stack will the team use for the CampusConnect application?                            | Architecture / Implementation | Brendan | A3        | Open                |

## Resolving Assumptions

When an assumption is validated, invalidated, or superseded, the team should:

1. record the result;
2. identify the supporting evidence;
3. review requirements, risks, plans, or design decisions that depended on it; and
4. update affected project artifacts.

## Resolving Open Questions

When an open question is answered, the team should:

1. record the resolution;
2. reference the authoritative decision or evidence when appropriate;
3. update affected requirements and other engineering artifacts; and
4. preserve the original question when it provides useful project history.

## Managing Unknowns

An unresolved question is acceptable when the team clearly understands:

* why the question matters;
* what project work it could affect;
* who owns resolving it; and
* when it must be resolved.

The team should not invent decisions simply to make project documentation appear complete.

## Relationship to Risk

Assumptions and open questions that could significantly affect scope, schedule, architecture, security, testing, or release readiness should also be reflected in the project's risk documentation when appropriate.

## Expectations

* Record meaningful assumptions explicitly.
* Keep unresolved matters visible as clear questions.
* Assign an owner to each important uncertainty.
* Identify when answers are needed.
* Update related artifacts when decisions are made.
* Preserve useful engineering history rather than silently changing prior understanding.

