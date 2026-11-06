# Database

The database stores support requests in one SQLite table and preserves them after the application closes.

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
    "resolution": None
}
```

The request ID and timestamp above are examples.

## Functions

- `submit_request(details)` — saves and returns a new request.
- `get_request_status(request_id)` — returns a saved request.
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

This creates the database and table if needed and preserves existing requests.
This command also launches the terminal menu.

## Running tests

Create and activate a virtual environment on macOS/Linux:

    python3 -m venv .venv
    source .venv/bin/activate

Install pytest and run both service test files:

    python -m pip install pytest
    python -m pytest -v tests/test_student_service.py tests/test_reviewer_service.py

The 13 service tests passed against SQLite. Each test uses a temporary
database, keeping tests separate from saved application requests.

Manual verification also confirmed that a student request could be listed
and resolved through the reviewer service, then retrieved through the
student service in a new Python process.
