"""Reviewer-side request processing service.
Uses temporary in-memory storage through mock_backend.py.
"""

import mock_backend

"""Return all requests waiting for reviewer attention."""
def list_submitted_requests():
    return mock_backend.list_pending_requests()


"""Retrieve a request by its ID."""
def get_request(request_id):
    return mock_backend.get_request_for_review(request_id)


"""Validate and save a reviewer's resolution."""
def save_resolution(request_id, resolution):
    if not isinstance(resolution, str) or not resolution.strip():
        raise ValueError("A resolution is required.")

    return mock_backend.resolve_request(request_id, resolution)
