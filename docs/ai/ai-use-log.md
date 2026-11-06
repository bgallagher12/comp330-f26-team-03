# AI Use Log

This log records meaningful AI-assisted engineering work that materially affects project artifacts, decisions, implementation, testing, documentation, or other engineering evidence.

Routine spelling, formatting, or simple syntax assistance does not need to be logged.

## AI Use

| Date | Member | Tool | Area | Activity | Verification & Outcome |
|---|---|---|---|---|---|
| 2026-09-20 | Carlos | ChatGPT | Documentation | Drafted and organized `docs/ai/ai-policy.md` and `docs/ai/ai-use-log.md` | Reviewed and modified the project structure based on the 330 guides |
| 2026-09-28 | Jaylene | ChatGPT | Backend Planning | Reviewed Issue #3 and helped structure `src/main.py` request-processing logic, including validation, reviewer information, category behavior, open questions, and requirement traceability | Reviewed the suggestions against Issue #3 and the project requirements, then manually incorporated and verified the changes before committing |
|2026-09-29|Sherry|ChatGPT|Coding Assistance|Used AI to help review any errors of frontend page|Reviewed suggestions and tested the frontend page to verify the form|
|2026-11-04|Sanjana|ChatGPT|Backend Implementation & Testing|Used AI to help structure and review `src/review_service.py`, including functions to list submitted requests, retrieve requests by ID, validate reviewer resolutions, and save resolutions through `mock_backend.py`. Also used AI assistance to develop `tests/test_review_service.py`.|Reviewed and adapted the suggested code to the existing project structure. Ran `uv run --active pytest -v tests/test_review_service.py` and confirmed all six tests passed. Changes were committed to the `sanjana/reviewer-service` branch.
| 2026-11-03 | Jaylen | ChatGPT | Implementation and Testing | Used ChatGPT to review the structure of `src/request_service.py`, suggest test cases for Issue #27, troubleshoot an import-path error, and review staged changes | Implemented and reviewed the service logic, corrected the import path and service-layer validation boundary, ran 6 unit tests successfully, and reviewed the staged Git diff before committing the initial implementation as `85d392b`. After adding the unique-ID and retrieval test for AC-REQ-002-01, reran the suite with 7 tests passing. See `AVN-001` for detailed verification. Current verification uses `mock_backend.py`; real database integration is still pending. |
| 2026-11-05 | Carlos | ChatGPT | Backend Integration & Testing | AI helped update service tests for SQLite and provided guidance during backend integration. | Carlos made the changes, ran all 13 tests successfully, and manually verified the request workflow and persistence across Python processes. |
## Logging Expectations

Log AI use when it materially affects:

* requirements or planning;
* architecture or engineering decisions;
* implementation or refactoring;
* testing or debugging;
* engineering review;
* documentation;
* operational or security analysis; or
* phase-gate evidence.

Entries should briefly explain **what AI helped with, what artifact was affected, how a human verified the work, and what was ultimately done with the output**.

For significant AI-assisted work requiring more detailed verification evidence, reference:

`/docs/ai/ai-verification-notes.md`
