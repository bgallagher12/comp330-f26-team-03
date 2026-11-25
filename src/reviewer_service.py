"""Reviewer-side request processing service.
Uses shared SQLite storage.
"""

from src.credentials import hash_new_password, normalize_username, verify_password

from src.database import (
    add_reviewer_account,
    get_reviewer_credentials,
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


def create_account(username, password):
    add_reviewer_account(normalize_username(username), *hash_new_password(password))


def authenticate(username, password):
    return verify_password(password, get_reviewer_credentials(username.strip().lower()))
