"""Fake backend for building the terminal interface.
Data resets whenever the program restarts.
"""

from datetime import datetime, timezone

_requests = {
    1: {
        "request_id": 1,
        "student_id": "001",
        "student_name": "Demo Student",
        "student_email": "student@example.com",
        "title": "Projector not working",
        "description": "The classroom projector will not turn on.",
        "category": "Technology",
        "status": "submitted",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "resolution": None,
    }
}


def _get_request(request_id):
    if request_id not in _requests:
        raise ValueError("Request not found.")
    return _requests[request_id]


def submit_request(details):
    required_fields = (
        "student_id",
        "student_name",
        "student_email",
        "title",
        "description",
        "category",
    )

    record = {}
    for field in required_fields:
        value = details.get(field)
        if value is None or not str(value).strip():
            raise ValueError(f"{field} is required.")
        record[field] = str(value).strip()

    categories = {"Technology", "Tutoring", "Facilities", "Other"}
    if record["category"] not in categories:
        raise ValueError("Choose a valid category.")

    request_id = max(_requests, default=0) + 1
    record.update(
        request_id=request_id,
        status="submitted",
        created_at=datetime.now(timezone.utc).isoformat(),
        resolution=None,
    )

    _requests[request_id] = record
    return record.copy()


def get_request_status(request_id):
    return _get_request(request_id).copy()


def list_pending_requests():
    return [
        record.copy()
        for record in _requests.values()
        if record["status"] == "submitted"
    ]


def get_request_for_review(request_id):
    return _get_request(request_id).copy()


def resolve_request(request_id, resolution):
    record = _get_request(request_id)

    if record["status"] == "resolved":
        raise ValueError("Request is already resolved.")

    if not resolution or not resolution.strip():
        raise ValueError("A resolution is required.")

    record["resolution"] = resolution.strip()
    record["status"] = "resolved"
    return record.copy()
