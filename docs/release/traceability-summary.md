# A5 requirements to release traceability

Baseline requirements and acceptance criteria remain in [requirements](../requirements/requirements.md) and [acceptance criteria](../requirements/acceptance-criteria.md). This Gate 5 verification history connects each Cycle 1 requirement and acceptance criterion to implementation changes, test results, demonstration steps and release claims. Tested candidate `3ee8d8866cebaca40c1550e1f34a8d94bc011dda`. Test names refer to files under `tests/`; [run output](../../test-evidence/a5/pytest.txt) preserves full node IDs.

| Requirement and criteria | Task and implementation evidence | Test or inspection | Demo and release claim | A5 disposition |
|---|---|---|---|---|
| REQ-001; AC-REQ-001-01/02 | [#27](https://github.com/bgallagher12/comp330-f26-team-03/issues/27), [PR #31](https://github.com/bgallagher12/comp330-f26-team-03/pull/31), [PR #35](https://github.com/bgallagher12/comp330-f26-team-03/pull/35); student_service.py | test_valid_request_submission, test_missing_description_rejected, test_invalid_category_rejected; CLI validation | D1/D3; RN-01/04 | Verified for required fields and approved categories |
| REQ-002; AC-REQ-002-01 | [#26](https://github.com/bgallagher12/comp330-f26-team-03/issues/26), PR #35; database.py/schema.sql | test_unique_request_ids_and_retrieval; CLI workflow restart | D1; RN-01/03 | Verified generated IDs and process restart persistence |
| REQ-003; AC-REQ-003-01 | [#28](https://github.com/bgallagher12/comp330-f26-team-03/issues/28), [PR #33](https://github.com/bgallagher12/comp330-f26-team-03/pull/33), PR #35; reviewer_service.py | test_list_submitted_requests, test_get_existing_request; CLI workflow | D1; RN-02 | Verified pending request access |
| REQ-004; AC-REQ-004-01/02 | #28; PR #35; database.resolve_request | test_save_resolution; CLI workflow | D1; RN-02/03 | Verified only submitted to resolved; broader transitions unsupported (LIM-003) |
| REQ-005; AC-REQ-005-01 | #28; PR #33/#35 | test_save_resolution, test_reject_blank_resolution, test_prevent_second_resolution | D1; RN-02/04 | Verified final resolution; notes history unsupported |
| REQ-006; AC-REQ-006-01 | #27, [#29](https://github.com/bgallagher12/comp330-f26-team-03/issues/29), [PR #36](https://github.com/bgallagher12/comp330-f26-team-03/pull/36); cli.py | test_resolved_request_retrieval; CLI workflow/invalid-id | D1/D2; RN-03/04 | Verified status and resolution visibility |
| REQ-007; AC-REQ-007-01/02 | #29; cli.run inspection | Shared menu exposes reviewer actions to every user. Role-denial test absent. | Explicit limitation callout | NOT MET as a role boundary; reviewer actions exist but no authenticated reviewer role (LIM-001) |
| REQ-008; AC-REQ-008-01 | #26; schema inspection | Only current status/resolution and creation time retained | Explicit limitation callout | NOT MET as history; current-state retrieval is not action audit (LIM-002) |
| REQ-009; AC-REQ-009-01 | [ADR-0001](../decisions/adr-0001-use-synthetic-data-for-cycle-1.md), tests and demo fixture | Tony Tiger, example.com addresses; no external records needed | D1-D3 | Verified for this fixture and test execution; synthetic-only policy is not technically enforced |

[PR #37](https://github.com/bgallagher12/comp330-f26-team-03/pull/37) adds CI. [#30](https://github.com/bgallagher12/comp330-f26-team-03/issues/30) describes backend verification and README work. Issue checkboxes alone do not prove acceptance. Existing issue text includes older multi-table/staff-identity plans that the actual single-table implementation does not deliver. This package does not close those tasks by inference.

The new candidate commit adds `scripts/verify_a5.py` and `tests/test_cli_release.py` to make the prior manual CLI scenarios repeatable. It changes no production code. The final evidence package commit adds documentation and output only; see [changed files](changed-files.md).

## A6 traceability

The [candidate package](assignment6-final-release-package.md) links the release decision and workflow status. Each change maps back to the original criteria and [Cycle 2 targets](../planning/cycle2-maturity-plan.md). The implementation and tests are in commit `98d0f66567b3140caca82d8f74e917122aced461`. The [candidate PR](https://github.com/bgallagher12/comp330-f26-team-03/pulls?q=is%3Apr+head%3Acarlos-a6-release) tracks review and CI. Test names and results appear in the [local verification log](../../test-evidence/a6/verification.txt).

| Requirement | Cycle 1 evidence → Cycle 2 implementation | Regression and demonstration | Release note and disposition |
|---|---|---|---|
| REQ-001/002 | #27, #29 → [submission and request persistence](../../src/database.py) | Required fields, category validation, unique IDs, restart and legacy DB tests. D1. | [RN-A6-01](final-release-notes.md). Synthetic submission and persistence verified. |
| REQ-003/004/005 | #28, PR #35 → [reviewer workflow](../../src/reviewer_service.py) and [reviewer menu gating](../../src/main.py) | Reviewer suite and CLI resolution. D3. | [RN-A6-02](final-release-notes.md). Shared queue and one resolution. Editing and reopening remain deferred. |
| REQ-006 | #27, #29 → [student lookup contract](../../src/student_service.py) | Owner-scoped list/detail, unseen badge through list navigation, first open, restart, and cross-student denial. D2, D4, and D5. | [RN-A6-01](final-release-notes.md). Verified for signed-in student accounts. |
| REQ-007 | DEF-A5-001 → [student and reviewer sign-in](../../src/main.py) and [CLI guards](../../src/cli.py) | Invalid student menu choices, unknown accounts, incorrect passwords, prior-request claim denial, and hidden passwords. D1, D3, and D5. | [RN-A6-01/02](final-release-notes.md). Mitigated for the supervised CLI. |
| REQ-008 | DEF-A5-002 → [outcome events](../observability/observability-plan.md) | Sanitized events verified during D2–D4 and the storage fault check. | [RN-A6-03](final-release-notes.md). Durable actor and action history deferred. |
| REQ-009 | [ADR-0001](../decisions/adr-0001-use-synthetic-data-for-cycle-1.md) → [governance](../security/security-governance-checklist.md) | Synthetic QA inputs through every test and demo step. | [RN-A6-04](final-release-notes.md). Synthetic-only operating limit. |
