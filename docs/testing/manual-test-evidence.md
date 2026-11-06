# Manual Test Evidence: Integrated Terminal Interface

- Tester: Carlos
- Start command: `python -m src.main`
- Storage: SQLite through the student and reviewer services

## Verified Results

| Check | Observed result |
|---|---|
| Retrieve saved request #4 | Displayed resolved status and saved resolution |
| Unknown request ID 99999 | Displayed “Request not found.” and returned to menu |
| Nonnumeric request ID | Displayed validation message and returned to menu |
| Resolve request #4 again | Rejected with “Request is already resolved.” |
| Nonnumeric category | Displayed validation message; request was not submitted |
| Submit synthetic request | Created request #5 with submitted status |
| List pending requests | Included request #5 |
| Resolve request #5 | Saved resolution “ClI workflow verified” |
| Retrieve request #5 | Displayed resolved status and saved resolution |
| Category selection after display fix | Listed all four categories; selecting 1 returned Technology |
| Import CLI module | Printed “Import OK” without launching the menu |

## Automated Regression Checks

Command: `python -m pytest -q`

Result: 13 passed.

These tests cover the backend services. CLI behavior was checked manually;
the test result does not establish automated CLI coverage.

## AI Assistance

AI provided guidance on service wiring, startup, error handling, and
verification. Carlos created and ran the checks recorded above.
