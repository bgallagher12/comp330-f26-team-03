# A5 defect and residual risk disposition

Review prepared 2026-11-17 for Gate 5 verification. Original planning risk IDs are retained here without rewriting earlier milestone plans.

| Risk | A5 observation | Mitigation and residual exposure | Proposed owner | Disposition |
|---|---|---|---|---|
| R-001 schema mismatch | Single requests table works in current tests; original task mentions multiple tables and staff identity | Document actual schema. No normalization/identity completion claim. | Carlos | Reduced integration uncertainty; identity scope remains incomplete |
| R-002 interface mismatch | CLI and SQLite services pass integrated runs | Keep shared fields and repeat regression after changes | Carlos | Reduced for rehearsed workflow |
| R-003 processing ambiguity | Required fields/categories and submitted to resolved implemented | Disclose limited transition model | Jaylen / Sanjana | Restricted scope documented, acceptance pending |
| R-004 merge conflict | A5 work isolated on a branch | Review diff and run CI on merge result | Carlos | Monitoring |
| R-005 late integration | Working integrated baseline exists, final package/review still required | Release checklist and exact tested snapshot | Carlos | Evidence closure pending |
| R-006 permissions | Materialized as DEF-A5-001 | Synthetic local supervised demo. Any operator can still perform reviewer actions. | Carlos | Open high-impact risk, blocks general use |
| R-007 real data | New fixtures use synthetic identities and example.com | Enter no actual student details; application cannot enforce this policy | Carlos | Monitoring, residual misuse risk |
| R-008 retention/audit | Materialized as DEF-A5-002; no validated recovery | Disposable demo data; disclose absent history and backup | Carlos | Open |

Names describe proposed review routing for this package and existing service domains, not claims that members have approved risk acceptance. No A6 work is commissioned by this document.

Recommended disposition: a supervised synthetic-data demonstration is technically defensible with the stated limits. General release remains HOLD. The dated human decision and review links belong in [release-readiness-review.md](../reviews/release-readiness-review.md).

## Cycle 2 disposition

| Defect or gap | Severity | Owner for review | A6 candidate disposition and proof |
|---|---|---|---|
| DEF-A5-001 unrestricted reviewer menu | High | Carlos / Sanjana | Mitigated for the supervised CLI. Default menu denies review and resolve. Unknown instructor accounts and incorrect passwords fail closed. Shared staff access and host trust remain. |
| A6 finding under REQ-006: request number alone revealed requester details and resolution | High | Carlos / Sanjana | Fixed on the student path. Tests verify owner-scoped list, detail and seen writes. Unknown accounts and wrong passwords are denied. Owner access and the seen state survive restart. |
| DEF-A5-002 absent reviewer action history | High | Brendan | Deferred. Fixed outcome events support diagnosis. There is no identity or durable action history. |
| CLI exits with a traceback on invalid storage | Medium | Jaylen and Dominic / Brendan | Addressed for tested invalid SQLite file. App emits a fixed failure signal and exits. See the [runbook](../operations/runbook.md). |

See [final testing](../testing/final-test-evidence.md) for the regression evidence and [technical limits](../release/known-limitations.md) for the general-use decision.
