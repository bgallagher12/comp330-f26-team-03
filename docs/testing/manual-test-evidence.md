# Manual Test Evidence: Terminal Interface

- **Team Member:** Sherry
- **Frontend:** `python src/cli.py`
- **Backend:** `src/mock_backend.py` (fake in-memory data)

## Workflow test

| Step | Action | Expected result | Actual result |
|---|---|---|---|
| 1 | Start the program | Menu shows Submit, View Status, Review Pending, Resolve, and Exit | [What happened] |
| 2 | Submit a request using the provided fake student details | Request is saved and its generated ID and status are displayed | [What happened; include ID] |
| 3 | View the submitted request’s status using that ID | The matching ID, status, and resolution are displayed | [What happened] |
| 4 | List pending requests | The submitted request appears in the pending list | [What happened] |
| 5 | Resolve the request using that ID | Request details are shown, resolution is accepted, and updated status and resolution are displayed | [What happened] |
| 6 | View its status again | Status is resolved and the saved resolution is shown | [What happened] |
| 7 | Choose Exit | Program ends | [What happened] |

## Invalid input checks

| Input | Expected result | Actual result |
|---|---|---|
| Invalid menu choice, such as `9` | Error message; program returns to the menu | [What happened] |
| Letters instead of a request ID | Error message; program does not crash | [What happened] |
| Unknown numeric request ID | Not-found message; program does not crash | [What happened] |
| Letters or out-of-range number for category | Error message; program returns to the menu | [What happened] |

## Evidence

[Paste a concise terminal transcript here, or link/add screenshots.]

## Notes

Fake backend data resets when the program restarts, so the submit, review, resolve, and final status checks were done in the same run.

## AI-use disclosure

[Briefly describe any AI assistance used, for example: “Used AI to help identify CLI bugs and draft comments. I reviewed and ran the code myself.”]