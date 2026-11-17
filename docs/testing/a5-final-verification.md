# A5 final verification record

Execution date 2026-11-17 UTC. Verified by Carlos. Tested commit `3ee8d8866cebaca40c1550e1f34a8d94bc011dda`. The tree was clean before capture. Later changes are release documentation and preserved results only. [snapshot.json](../../test-evidence/a5/snapshot.json) records exact executable file hashes and environment.

## Observed runs

| Check | Reproducible command from repository root | Actual result | Evidence |
|---|---|---|---|
| Dependencies | `python -m pip install -r requirements-dev.txt` | pytest 9.2.0 installed | snapshot environment |
| Syntax | `python -m compileall -q src tests scripts/verify_a5.py` | Exit 0, no output | snapshot |
| Full suite | `python -m pytest -v --junitxml=test-evidence/a5/junit.xml` | 16 passed, exit 0 | [pytest.txt](../../test-evidence/a5/pytest.txt), [junit.xml](../../test-evidence/a5/junit.xml) |
| CLI demonstration | `python scripts/verify_a5.py` | workflow, invalid-id, validation all PASS; 4 processes exit 0 | [cli-transcript.json](../../test-evidence/a5/cli-transcript.json) |

The script prints JSON to stdout. Capture a new run to a different path rather than overwriting the accepted evidence. Input fixtures and actual output are preserved per session. The workflow's database begins empty and ends with exactly request 1, student_id 00123, resolved status and the expected resolution. The two negative scenarios end with zero rows. A timeout, unexpected output, wrong persisted row or failed process raises an assertion/error and returns nonzero.

The existing 13 service tests also passed on unchanged baseline `9aa33e33c9431331db791394c1eddbca6e118896` before the new test code was introduced. New candidate has 3 additional CLI scenarios. The preserved candidate run is authoritative for the 16-test claim.

## Coverage and limits

Service tests cover successful submission, missing description, category rejection, unique IDs, status lookup, missing IDs, pending listing, resolution, blank resolution and repeat-resolution rejection. CLI regression now covers real entry-point startup, prompt inputs, successful request processing, negative IDs, invalid required data, return to menu and cross-process persistence. It automates recurring manual verification from issue #29 / PR #36; it does not claim to reproduce a historical defect without its original failing snapshot.

No code coverage percentage was measured. No role-denial, audit-history, load/concurrency, recovery, security scanning, accessibility, comprehensive input-type/length, network deployment or platform-matrix test was run. The local environment is Linux/Python 3.12.14; the historical CI run used Python 3.14.10. These results do not prove production readiness or all requirements complete.

## Historical manual record

[manual-test-evidence.md](manual-test-evidence.md) remains the earlier Carlos-authored observation record. It lacks an exact SHA and initial fixture. It is supplemental evidence and cannot bind an earlier manual run to this candidate. The new transcript supplies revision, inputs, output and initial state for current verification.
