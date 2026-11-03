"""Reviewer-side request processing service.
Uses temporary in-memory storage through mock_backend.py.
"""

from mock_backend import (
    list_pending_requests as _list_pending_requests,
    get_request_for_review as _get_request_for_review,
    resolve_request as _resolve_request,
)

# Return all requests waiting for reviewer attention.
def list_submitted_requests():
    return _list_pending_requests()


# Retrieve a request by its ID.
def get_request(request_id):
    return _get_request_for_review(request_id)


# Validate and save a reviewer's resolution.
def save_resolution(request_id, resolution):
    if not isinstance(resolution, str) or not resolution.strip():
        raise ValueError("A resolution is required.")

    return _resolve_request(request_id, resolution)
