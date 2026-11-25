# Cycle 2 demo walkthrough

Use two interactive terminals in the same disposable checkout with a clean synthetic database. From the repository root, provision the demo reviewer once. Set private passwords at the prompts.

```bash
python -m src.main --add-reviewer demo-instructor
```

Start Terminal 1 with `python -m src.main` and Terminal 2 with `python -m src.main --reviewer`. Use `other@example.com` for the second student in D5. Keep passwords out of shared recordings.

| Step | Do | Expected evidence |
|---|---|---|
| D1 | In Terminal 1, type `/register`. Enter `tonytiger@example.com`, student ID `00123`, and a password. Sign in with the email and password. Choose option 1 and submit as Tony Tiger, `tonytiger@example.com`, title `Calculus I help`, a tutoring description, category 2. Optionally submit `Projector issue` under category 1. | The requests are saved under the linked ID `00123`. |
| D2 | Choose option 2 and open `Calculus I help` by its list number. | **My Requests** shows the ticket as **Submitted** with no response. |
| D3 | In Terminal 2, sign in as `demo-instructor`. Use option 3 to find the request ID in the pending queue. Use option 4 and that ID to enter `Office hours Monday 4–6 in Dumbach 111.` | The request changes to **Resolved**. |
| D4 | Back in Terminal 1, open **My Requests**. Press Enter to return, then reopen the list and select `Calculus I help`. Open the list once more and repeat after restarting and signing in. | **[Update available]** survives the first return to the menu. The answer appears when Tony opens the request. The badge stays cleared, and the response can still be read after restart. |
| D5 | Exit Terminal 1 and register `other@example.com` with student ID `00987`. Sign in and open **My Requests** and try reviewer menu option 4. | Tony’s request is absent and the reviewer option is rejected. |

Use the [runbook](../operations/runbook.md) for setup and recovery and the [local verification record](../../test-evidence/a6/verification.txt) for observed results.
