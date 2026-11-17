# A5 final evidence index

Campus Connect, Team 03, Cycle 1. Prepared 2026-11-17 for Carlos Alcala. Tested A5-RC1 revision `3ee8d8866cebaca40c1550e1f34a8d94bc011dda`; production source matches `9aa33e33c9431331db791394c1eddbca6e118896`. Package status: prepared for review; human acceptance and final candidate CI reconciliation pending.

## Authoritative evidence

| Required area | Artifact | What it establishes |
|---|---|---|
| Release contents and decision basis | [Release notes](release-notes.md) | Delivered claims, deferred scope and bounded recommendation |
| Exact snapshot | [Snapshot manifest](../../test-evidence/a5/snapshot.json) | Tested SHA, environment and executable hashes |
| Requirements to changes to tests | [Traceability](traceability-summary.md) | Every criterion disposition including unmet criteria, issues/PRs, tests and demo links |
| Demonstration | [Demo script](demo-script.md), [actual transcript](../../test-evidence/a5/cli-transcript.json) | Starting database state, exact input and output, errors and restart persistence |
| Testing | [Final verification](../testing/a5-final-verification.md), [pytest output](../../test-evidence/a5/pytest.txt), [JUnit](../../test-evidence/a5/junit.xml) | 16 executed tests, environment and coverage limits |
| CI/CD | [CI evidence](../testing/ci-evidence.md) | Successful baseline CI and explicit candidate verification boundary; no CD |
| Defect/risk status | [Defects](../quality/defect-log.md), [risk disposition](../quality/defect-review.md) | Open defects, mitigations, residual impact |
| Known limitations | [Limitations](known-limitations.md) | Unsupported behavior and restricted usage |
| Release control and accountability | [Readiness review](../reviews/release-readiness-review.md) | Dated recommendation, ownership routing and pending human decisions |
| AI final update | [A5 AI accountability](../ai/a5-ai-accountability.md), [AI log](../ai/ai-use-log.md) | Generated work, actual verification and pending human review |
| Changed files | [Changed-file summary](changed-files.md) | A5 scope and source unchanged assurance |

## Submission closure

The Word summary and PowerPoint are separate Sakai submissions and are not stored in this repository. The team lead submits those files and the GitHub repository URL through Sakai. Each member separately submits their peer review using the course template. Do not store private peer reviews or individual instructor feedback in this public repository.

Before submission, use the readiness checklist to complete human review, candidate CI, final acceptance SHA/tag and private peer reviews.
