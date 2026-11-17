# A5 CI and delivery evidence

GitHub Actions workflow: [Python tests](../../.github/workflows/ci.yml). Triggers: pull requests, pushes to main, manual dispatch. Runner ubuntu-latest, Python 3.14, pinned pytest from requirements-dev.txt. Checks: install dependencies, `python -m compileall -q src tests`, `python -m pytest -q`. Permissions contents read. No automated deployment/CD, coverage gate, security scanner or production release automation is configured.

## Confirmed baseline run

Inspected via GitHub on 2026-11-17:

- Commit `9aa33e33c9431331db791394c1eddbca6e118896` (main and a4-construction-integration tag at inspection).
- [Run 42170410768](https://github.com/bgallagher12/comp330-f26-team-03/actions/runs/42170410768), push event, completed SUCCESS, 2026-11-06 05:46 UTC.
- [Job 127736648987](https://github.com/bgallagher12/comp330-f26-team-03/actions/runs/42170410768/job/127736648987), syntax and tests steps SUCCESS.
- Job log: CPython 3.14.10; `13 passed in 0.27s`.

This is existing CI evidence, not a new candidate run. No A5 cutoff or acceptance tag has been reconciled by this package. The existing a4 tag resolves to the baseline above.

## Candidate verification

Candidate `3ee8d8866cebaca40c1550e1f34a8d94bc011dda` has 16 locally passing tests. [Local final verification](a5-final-verification.md) preserves the evidence. The A5 pull request should trigger the existing workflow and discover the three new parametrized CLI tests automatically. Review its Checks tab and record run URL, tested head/merge SHA, date and result in the release-readiness review before accepting the final package. A baseline green badge cannot stand in for this check.

A later documentation-only commit does not alter the tested executable hashes, but final PR/merge CI still needs review. No hosted deployment or CD validation is claimed.
