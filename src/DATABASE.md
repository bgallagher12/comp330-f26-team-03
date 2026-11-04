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