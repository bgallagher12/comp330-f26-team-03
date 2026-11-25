# Changed files since Assignment 5

Compare the candidate to the preserved `a5-verification-release` tag from a checkout:

```bash
git diff --name-status a5-verification-release HEAD
```

| Path | Status since A5 | What changed or why | Owner for review |
|---|---|---|---|
| `src/main.py`, `src/cli.py` | Modified | Updated entry point, student/reviewer dispatch, hidden credential entry, and runtime events. Removed obsolete entry-point pseudocode. | Carlos / Sherry |
| `src/database.py`, `src/schema.sql`, `src/student_service.py`, `src/credentials.py`, `src/DATABASE.md` | Added and modified | Added student accounts, owner-scoped My Requests, seen timestamps, and a shared password helper. Startup preserves older request rows and reviewer accounts. | Carlos / Jaylen |
| `src/reviewer_service.py` | Modified | Added reviewer account provisioning and password verification alongside the existing queue and resolution functions. | Sanjana / Carlos |
| `tests/test_*.py`, `test-evidence/a6/` | Added and modified | Updated student and reviewer expectations, regression-tested access, restart and legacy SQLite, and preserved observed local results. | Sanjana |
| [Workflow](../../.github/workflows/ci.yml), [CI evidence](../testing/ci-evidence.md) | Workflow unchanged. CI evidence modified | The record distinguishes A5 results from pending A6 runs. | Sanjana / Carlos |
| `docs/operations/`, `docs/observability/`, `docs/security/` | Added and modified | Added postmortem, completed runbook and local recovery evidence, documented signals, access and data handling. | Jaylen and Dominic / Sanjana |
| `docs/planning/`, `docs/quality/defect-review.md` | Added and modified | Added Cycle 2 estimates, target status, residual risks and defect disposition. | Sherry / Sanjana |
| `docs/architecture/`, `docs/ai/ai-use-log.md` | Modified | Updated architectural boundaries, caller contracts and AI-assisted verification record. Existing architecture image remains the Cycle 1 diagram. | Brendan / Dominic |
| `README.md`, `docs/release/`, `docs/reviews/release-readiness-review.md` | Added and modified | Indexed the A6 candidate, updated scope, traceability and synthetic demo instructions. Presentation deck remains pending. | Carlos |
| `scripts/verify_a5.py`, `test-evidence/a5/`, `docs/requirements/` | No change since Assignment 5 | Run the historical A5 CLI script at the A5 tag. | Brendan / Sanjana |
