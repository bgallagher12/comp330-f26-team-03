# Campus Connect A5 Cycle 1 release notes

Prepared 2026-11-17. Candidate A5-RC1. Tested revision: `3ee8d8866cebaca40c1550e1f34a8d94bc011dda`.
Application baseline: `9aa33e33c9431331db791394c1eddbca6e118896` (existing `a4-construction-integration` tag).
The candidate adds verification only; `src/` is unchanged. This is a new A5 evidence package, not a reconstruction of an earlier submission cutoff. No A5 acceptance tag or team approval is claimed.

## Delivered capabilities

| Release claim | Actual behavior | Evidence |
|---|---|---|
| RN-01 Submission | Six required fields, four categories, generated ID and timestamp, initial submitted state | Student suite; CLI workflow and validation scenarios |
| RN-02 Reviewer workflow | List submitted requests, retrieve details, save a nonempty resolution and resolved state | Reviewer suite; CLI workflow |
| RN-03 Student outcome | Retrieve saved resolution after a new Python process starts | CLI workflow session 2; student resolved-retrieval test |
| RN-04 Rejected operations | Missing description/category validation, unknown/nonnumeric ID, blank or repeated resolution rejection | Service suites and CLI negative scenarios; historical manual log |

All current observations are indexed in [final verification](../testing/a5-final-verification.md). RN-04 does not claim every service negative path is exercised through the CLI.

## Not delivered and known limits

REQ-007 student/reviewer access restrictions are not implemented. Both menus are available to every operator (DEF-A5-001 / LIM-001). REQ-008 action history is not implemented (DEF-A5-002 / LIM-002). REQ-004 supports only submitted to resolved. REQ-005 supports one final resolution, not an editable notes history. Email format and length are not validated. The browser files in `scripts/` are a separate prototype and are not the integrated release interface. No routing, notifications, SSO, hosted deployment, backup automation or production operations are claimed.

See [limitations](known-limitations.md), [defects](../quality/defect-log.md), and [risk dispositions](../quality/defect-review.md). The original requirements remain unchanged; restricted or unmet criteria are explicit in [traceability](traceability-summary.md).

## Validation and CI

Local candidate: 16 tests passed (13 existing service tests and 3 CLI scenarios), syntax check exit 0, and three repeatable CLI scenarios passed. Python 3.12.14 / pytest 9.2.0 on Linux. This differs from historical CI's Python 3.14.10. The successful baseline CI run is [42170410768](https://github.com/bgallagher12/comp330-f26-team-03/actions/runs/42170410768), with 13 tests. Candidate CI must be assessed separately; see [CI evidence](../testing/ci-evidence.md). No deployment pipeline exists.

## Release recommendation

Technical recommendation dated 2026-11-17: **PROCEED WITH CONDITIONS for a supervised local demonstration using synthetic data only**. Tested submission, resolution and retrieval support that bounded use. Open access-control and audit gaps block general or production use. Team acceptance, independent review and final submission are pending in the [readiness review](../reviews/release-readiness-review.md). This recommendation is AI-assisted analysis, not a signed team release decision.

## Reproduction and recovery

Use [demo-script.md](demo-script.md). Automated verification uses disposable databases. Normal app data remains in `data/campusconnect.db`. If a live demo fails, disclose it and show the preserved transcript labeled as a prior run. Stop a damaged demo instance and use a fresh disposable verification run. No verified production backup/restore procedure is available.
