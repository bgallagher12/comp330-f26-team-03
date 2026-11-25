# Database

SQLite stores requests in `requests` and local credentials in `student_accounts` and `reviewer_accounts`. Startup adds the nullable `response_seen_at` column to older databases and preserves existing requests and reviewer accounts. Existing resolved requests start with an unread response. After the operator provisions the exact stored student ID with `--add-student EMAIL STUDENT_ID`, the student sees those requests in **My Requests**. An older preview database may still have an unused receipt table. Use the [runbook](../docs/operations/runbook.md) to provision demo accounts.

## Setup

From the repository root, run:

```bash
python3 -c "from src.database import init_db; init_db()"
```

This creates `data/campusconnect.db` if needed and preserves existing requests.

## Input and output

`submit_request(details)` accepts a dictionary containing:

```python
{
    "student_id": "001",
    "student_name": "Demo Student",
    "student_email": "student@example.com",
    "title": "Projector not working",
    "description": "The classroom projector will not turn on.",
    "category": "Technology"
}
```

Categories: `Technology`, `Tutoring`, `Facilities`, or `Other`.

It returns the same information plus automatically generated fields:

```python
{
    "request_id": 1,
    "student_id": "001",
    "student_name": "Demo Student",
    "student_email": "student@example.com",
    "title": "Projector not working",
    "description": "The classroom projector will not turn on.",
    "category": "Technology",
    "status": "submitted",
    "created_at": "2026-11-04T18:09:03.996Z",
    "resolution": None,
    "response_seen_at": None
}
```

The request ID and timestamp above are examples. The CLI keeps the request ID internal to the student flow. The reviewer uses it when choosing a request to resolve.

## Functions

- `submit_request(details)` — saves and returns a new request.
- `list_student_requests(student_id)` returns ID, title, status, and seen timestamp for the signed-in student.
- `get_student_request(student_id, request_id)` returns the selected owned request with its response.
- `mark_response_seen(student_id, request_id)` writes the first open timestamp for a resolved, owned request.
- `list_pending_requests()` — returns a list of submitted requests.
- `get_request_for_review(request_id)` — returns a saved request for review.
- `resolve_request(request_id, resolution)` — saves a nonempty resolution, sets the status to `resolved`, and returns the updated request.

Invalid input, unknown request IDs, and attempts to resolve an already resolved request raise `ValueError`.

## Backend integration

The services now share SQLite storage:

- `src/student_service.py`: validates submissions and retrieves request status.
- `src/reviewer_service.py`: lists pending requests and saves resolutions.
- `src/database.py`: stores and retrieves requests.

Initialize the database from the repository root:

    python -m src.main

This creates the database and tables if needed and preserves existing requests.
This command prompts for student email sign-in and offers `/register` for new students. The student account column `username` stores the email for new accounts and also supports handles from the earlier preview. Self-registration checks for existing requests and inserts the account in one SQLite statement.

## Running tests

Create and activate a virtual environment on macOS/Linux:

    python3 -m venv .venv
    source .venv/bin/activate

Install pytest and run both service test files:

    python -m pip install -r requirements-dev.txt
    python -m pytest -v tests/test_student_service.py tests/test_reviewer_service.py

See the [A6 test evidence](../docs/testing/final-test-evidence.md) for the current results.
