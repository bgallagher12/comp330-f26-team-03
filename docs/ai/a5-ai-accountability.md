# A5 AI use and verification

Date 2026-11-17. Requesting team member Carlos Alcala. Tool ChatGPT / Codex. Scope limited to A5 release preparation, evidence capture, CLI regression, Word summary and presentation preparation. No production application code changed.

AI inspected source, tests, Git history, requirements, issues and GitHub Actions records. AI authored the new verification script and CLI tests, release documentation, evidence index, risk/defect dispositions, summary and presentation. AI executed the tests and script in an isolated environment. Actual input/output, executable hashes, pytest/JUnit results and baseline CI links are preserved. AI checked consistency of release claims against those observations.

Human status: Carlos authorized this work, but no claim is made that he or Brendan has reviewed, personally executed, understood or approved every generated artifact. Independent review, acceptance of the restricted demonstration scope, candidate CI review and presentation rehearsal remain pending in the release-readiness review. Historical AI-use entries are retained as historical accounts and do not certify this candidate.

## Review checks for accountable acceptance

| AI-assisted area | Verification performed by AI | Required human review |
|---|---|---|
| CLI regression and script | 16 tests pass; subprocess outputs and persisted rows checked; temporary storage only | Understand assertions, reproduce the workflow and confirm fixture safety |
| Release/traceability/defects | Compared source behavior and all acceptance criteria; disclosed missing access control and audit history | Confirm requirement dispositions, actual scope and residual risk judgment |
| Testing/CI claims | Captured local run and inspected historical run/job logs | Review candidate PR CI and exact tested snapshot |
| Documentation, Word and presentation | Cross-checked claims with repository evidence; generated editable files | Read final content, verify sources, rehearse and correct unsupported claims |
| Readiness decision | Drafted limited technical recommendation with pending approvals visible | Record decision using named human reviewer and date |

No AI-generated artifact or automated pass is itself evidence of human approval. No member's private assessment or peer report belongs in this public release package.
