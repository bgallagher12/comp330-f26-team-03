# A5 changed-file summary

Comparison baseline `9aa33e33c9431331db791394c1eddbca6e118896`. Tested verification commit `3ee8d8866cebaca40c1550e1f34a8d94bc011dda` adds only `scripts/verify_a5.py` and `tests/test_cli_release.py`. Subsequent package changes are documentation and preserved evidence. No `src/`, schema, dependency or CI workflow changes are included. No A6 artifacts or feature changes are introduced.

| Paths | Change and purpose |
|---|---|
| README.md | Replace stale A1 status and non-executable guidance with actual CLI setup and A5 links |
| docs/release/release-notes.md, demo-script.md, known-limitations.md, traceability-summary.md | Replace starter guidance with project-specific release evidence |
| docs/release/evidence-index.md, changed-files.md | Add final evidence navigation and this scope record |
| docs/testing/ci-evidence.md, a5-final-verification.md | Actual historical CI plus candidate local verification and coverage boundaries |
| docs/quality/defect-log.md, defect-review.md | Open defects, historical correction limits, and residual risk dispositions |
| docs/reviews/release-readiness-review.md | Dated technical recommendation, proposed owner/reviewer and pending acceptance |
| docs/ai/ai-use-log.md, a5-ai-accountability.md | Append final AI-use disclosure and record human verification boundary |
| scripts/verify_a5.py, tests/test_cli_release.py | Repeatable CLI rehearsal and regression using isolated databases |
| test-evidence/a5/* | Snapshot manifest, actual CLI transcript, pytest output and JUnit results |

For exact names and counts inspect the pull request's Files changed tab after publishing, or run `git diff --stat 9aa33e33c9431331db791394c1eddbca6e118896 HEAD`. Documentation/evidence commits may follow the tested commit because a commit cannot embed its own hash. Confirm executable hashes in snapshot.json remain unchanged before accepting the package.
