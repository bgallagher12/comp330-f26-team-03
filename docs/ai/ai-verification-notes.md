# AI Verification Notes

This file records detailed verification evidence for significant AI-assisted engineering work when the shorter entry in `ai-use-log.md` is not sufficient.

## Verification Notes

### AVN-001 — Student Request Service Implementation and Testing

**Date:** 2026-11-03
**AI Tool:** ChatGPT
**Related AI Use Log Entry:** 2026-11-03 - Jaylen
**Related Evidence:** Issue #27, `src/request_service.py`, `tests/test_request_service.py`, commit `85d392b`

#### AI Contribution

ChatGPT was used as a support tool while Jaylen worked on the student-side request service for Issue #27.

AI assistance included:

- reviewing the structure of `submit_request(details)` and `get_request_status(request_id)`;
- suggesting possible test cases based on Issue #27;
- helping troubleshoot an import-path error;
- reviewing the code and staged changes for possible problems.

Jaylen entered and reviewed the implementation, decided which suggestions to use, and tested the resulting behavior before committing it.

#### Human Verification Performed

Jaylen compared the implementation with the requirements listed in Issue #27 and reviewed each function and test before committing the changes.

Jaylen verified that:

- all required request fields are checked before submission;
- `student_id` remains stored as text;
- only the approved categories are accepted;
- valid requests can be submitted through the temporary mock backend;
- submitted requests can be retrieved using `request_id`;
- unknown request IDs return an error;
- reviewer resolutions can be retrieved through the student-side status function.

Jaylen ran:

`python3 -m unittest tests.test_request_service`

The result was:

`Ran 7 tests in 0.001s — OK`

The initial implementation was committed after 6 tests passed. A seventh test covering unique request IDs and retrieval for `AC-REQ-002-01` was added afterward, and the full suite was rerun successfully.

Jaylen also reviewed the staged Git diff before committing to make sure only the intended source and test files were included.

#### Result

The implementation was kept after review and testing.

During development, the import path was corrected. Validation was also kept in `request_service.py` rather than relying only on the mock backend so that the student-side validation logic can remain when the real database replaces the mock storage.

The initial implementation was committed as `85d392b`. The additional unique-ID and retrieval test was added afterward as part of the continuing Issue #27 work.

#### Remaining Concerns

The current implementation uses `src/mock_backend.py` as temporary storage.

The real database integration has not yet been implemented or tested. Once Carlos's database functions are available, the storage calls will need to be replaced and the student-side tests will need to be run again against the real integration.

Student request ownership and authorization behavior has also not yet been defined, so this implementation does not currently claim or test those permissions.

---

### AVN-002 — Reviewer Service Implementation and Testing

**Date:** 2026-11-04
**AI Tool:** ChatGPT
**Related AI Use Log Entry:** 2026-11-04 - Sanjana
**Related Evidence:** `src/review_service.py`, `tests/test_review_service.py`

#### AI Contribution

ChatGPT assisted with structuring and reviewing the reviewer-side request processing service.

Assistance included implementing functions to list submitted requests, retrieve requests by ID, validate reviewer resolutions, and save resolutions through `mock_backend.py`.

ChatGPT also assisted with developing and reviewing unit tests for the reviewer service.

#### Human Verification Performed

Sanjana reviewed and adapted the suggested implementation to fit the existing project structure.

Verification included:

- Reviewing the service functions and their backend calls.
- Running `uv run --active pytest -v tests/test_review_service.py`.
- Testing retrieval of existing and nonexistent requests.
- Testing submitted-request listing.
- Testing successful resolution saving.
- Testing rejection of blank resolutions.
- Testing prevention of duplicate resolutions.

All six tests passed.

#### Result

The reviewer service successfully passed all six mock-backed tests. The implementation was committed to the `sanjana/reviewer-service` branch.

The implementation uses temporary in-memory storage through `mock_backend.py`. Real database integration has not yet been completed.

#### Remaining Concerns

- Integration with Carlos's database functions remains pending.
- Reviewer authorization has not yet been implemented or verified.
- Integration with Sherry's terminal interface remains to be confirmed.
- The current tests do not establish end-to-end reviewer workflow correctness.

---

## When to Create a Verification Note

A separate verification note is useful when AI assistance has enough engineering significance, risk, or downstream impact that the verification should be preserved as reviewable evidence.

Examples include:

- security-sensitive code;
- authentication or authorization;
- data-integrity logic;
- significant architectural decisions;
- important test design;
- substantial requirements analysis;
- defect diagnosis;
- deployment or operational behavior;
- phase-gate evidence.

A separate verification note is usually unnecessary for trivial or low-risk AI assistance.

## Verification Independence

AI-assisted work should be checked through independent human judgment and appropriate engineering evidence.

Verification may include:

- code review;
- unit testing;
- integration testing;
- comparison with requirements or acceptance criteria;
- architecture review;
- runtime observation;
- peer review.

AI confirmation by itself is not sufficient verification.

## Verification Depth

The depth of verification should be proportional to the potential consequence of accepting incorrect AI output.

Low-risk assistance may only require ordinary human review. More significant implementation, security, data-integrity, or architectural work should receive stronger review and testing.

## Verification Against Requirements

Where AI-assisted work implements or affects system behavior, verification should reference applicable requirements and acceptance criteria when practical.

A useful evidence chain is:

AI Use Log Entry
→ AI Verification Note
→ Requirement / Acceptance Criterion
→ Implementation
→ Test / Review Evidence

## Failed Verification Is Valuable Evidence

AI-assisted work that fails verification should not be hidden.

If verification identifies an incorrect assumption, defect, or unsuitable recommendation, the rejected approach and resulting correction may provide useful engineering evidence.

## Expectations

- Create verification notes for significant AI-assisted work when detailed evidence is warranted.
- Use unique `AVN-###` identifiers.
- Link entries to the AI Use Log and related engineering evidence.
- Describe the AI contribution accurately.
- Describe what humans actually did to verify it.
- Use verification methods appropriate to the potential consequence.
- Record modifications, rejection, or failed verification honestly.
- Identify remaining uncertainty or risk.
- Do not treat AI self-confirmation as sufficient independent verification.
- Keep evidence concise enough to review while preserving important engineering reasoning.