# A5 release readiness review

Prepared 2026-11-17. Candidate A5-RC1; tested commit `3ee8d8866cebaca40c1550e1f34a8d94bc011dda`; application baseline `9aa33e33c9431331db791394c1eddbca6e118896`. Gate 5 verification review. Verified by Carlos.

## Proposed decision

**PROCEED WITH CONDITIONS for a supervised local demonstration using synthetic data. HOLD for general or production use.**

Rationale: 16 tests and a reproducible transcript support the working request workflow and restart persistence. REQ-007 and REQ-008 remain unmet, with no authentication or action history. This narrower demonstration judgment does not waive those criteria.

## Gate checklist

| Item | Evidence / disposition | Status |
|---|---|---|
| Exact tested snapshot | snapshot.json plus source/test/script hashes | Recorded |
| Reproducible successful and negative demonstration | demo-script.md; cli-transcript.json | Verified in the preserved test run |
| Final tests | 16 passed; pytest.txt and junit.xml | Local evidence captured |
| Candidate CI | Review final PR checks; baseline run alone insufficient | Pending |
| Requirements disposition | traceability-summary.md, including unmet criteria | Recorded |
| Defects and residual risks | quality/defect-log.md and defect-review.md | Open gaps disclosed |
| Release notes and changed-file summary | release-notes.md, changed-files.md | Prepared |
| AI disclosure and human verification | a5-ai-accountability.md | AI execution recorded; human review pending |
| Word summary and PowerPoint | Separate Sakai submissions; excluded from the repository | Managed separately in Sakai |
| Presentation rehearsal and scheduling | Script executed automatically; team rehearsal not attested | Pending team confirmation |
| Individual peer reviews | Each student submits privately through course channel | Not verified; keep outside public repo |
| Owner/reviewer acceptance | Routing below is proposed, no signed reviews fabricated | Pending |
| Final acceptance SHA/tag | Record after human review and final CI; do not move earlier tags | Pending |

## Artifact responsibility routing

Every final artifact falls under one of the groups below. These are proposed responsibilities for Carlos and Brendan to confirm, not evidence that a teammate authored or approved AI output.

| Artifact group | Proposed accountable owner | Proposed reviewer | Review evidence |
|---|---|---|---|
| README, release index, notes, traceability, limitations and changed files | Carlos Alcala | Brendan Gallagher | Pending PR review |
| Verification script, CLI tests, test logs, snapshot, test/CI documentation | Carlos Alcala | Brendan Gallagher | Pending PR review |
| Defect log and risk disposition | Carlos Alcala | Brendan Gallagher | Pending PR review |
| AI disclosure and readiness decision | Carlos Alcala | Brendan Gallagher | Pending PR review |
| Separate Sakai presentation | Carlos Alcala | Brendan Gallagher | Content review and rehearsal outside this repository |

## Human closure record

No human acceptance recorded at preparation. Before submission, Carlos should verify artifacts and exact PDF requirements; Brendan should review the changes and test evidence using his own GitHub identity. Preserve substantive comments/reviews and candidate CI links here or in the PR. Record the final accepted commit, decision date, decision maker and rationale. Create an A5 tag only after choosing that snapshot. A new test run is required if executable files differ from snapshot hashes. Private peer review completion is confirmed privately, never by publishing reports or individual feedback.

## A6 candidate maturity review

Local assessment dated 2026-11-24 for `carlos-a6-release`. The candidate is ready for teammate review and rehearsal as a supervised synthetic-data demo. [A6 release evidence](../release/assignment6-final-release-package.md)

| Area | Finding | Evidence |
|---|---|---|
| Student workflow | First-time registration cannot attach an account to an ID with existing requests. A signed-in account sees only its own tickets. Listing a resolved request keeps its badge. Opening the response clears it across restarts. | [Test results](../testing/final-test-evidence.md), [demo D4–D5](../release/demo-script.md) |
| Operations | Older request rows and reviewer accounts survive startup. A stopped-session copy restored both account types and the response seen state. | [Runtime evidence](../observability/runtime-evidence.md), [runbook](../operations/runbook.md) |
| Authorization and audit | Student and reviewer sign-in enforce the supervised CLI boundary. The trusted host, shared reviewer queue, and missing durable reviewer history constrain general use. | [Permission boundaries](../security/permission-boundaries.md), [residual risks](../planning/risk-register.md#a6-residual-risks) |
| Release closure | Local checks passed. PR review, CI on the final revision, the team release decision, and the submission tag are pending. | [Release decision record](../release/assignment6-final-release-package.md#release-decision-record) |
