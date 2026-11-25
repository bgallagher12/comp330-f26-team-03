"""
Student-side request service for CampusConnect.

Validates student requests and retrieves their status
using shared SQLite storage.
"""

import re

from src.credentials import hash_new_password, verify_password
from src.database import (
    submit_request as _save_request,
    add_student_account,
    get_student_account,
    get_student_request as _get_student_request,
    list_student_requests as _list_student_requests,
    mark_response_seen as _mark_response_seen,
)


# Define the fields that every student request must contain.
REQUIRED_FIELDS = (
    "student_id",
    "student_name",
    "student_email",
    "title",
    "description",
    "category",
)

# Define the only request categories currently approved for Cycle 1.
VALID_CATEGORIES = {"Technology", "Tutoring", "Facilities", "Other"}


# Validate a student's request and send it to the current storage layer.
# Required fields cannot be blank. Values are converted to strings and
# whitespace is removed so student_id remains text as required by Issue #27.
# The request is only passed to storage after validation succeeds.
def submit_request(details):
    if not isinstance(details,dict):
        raise ValueError("Request details must be a dictionary.")
    validated_details = {}

    for field in REQUIRED_FIELDS:
        value = details.get(field)

        if value is None or not str(value).strip():
            raise ValueError(f"{field} is required.")

        validated_details[field] = str(value).strip()

    if validated_details["category"] not in VALID_CATEGORIES:
        raise ValueError("Choose a valid category.")

    return _save_request(validated_details)


def create_account(email, student_id, password, *, allow_existing_requests=False):
    email = email.strip().lower()
    valid_email = re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email)
    if not valid_email or not email.isprintable() or len(email) > 254:
        raise ValueError("Enter a valid email address.")

    student_id = student_id.strip()
    if not student_id:
        raise ValueError("Student ID is required.")
    add_student_account(
        student_id, email, *hash_new_password(password),
        allow_existing_requests=allow_existing_requests,
    )


def authenticate(email, password):
    """Return the account's student ID after verifying its password."""
    account = get_student_account(email.strip().lower())
    credentials = (account["password_salt"], account["password_hash"]) if account else None
    if verify_password(password, credentials):
        return account["student_id"]
    return None



def list_requests(student_id):
    return _list_student_requests(student_id)


def get_request(student_id, request_id):
    return _get_student_request(student_id, request_id)


def mark_response_seen(student_id, request_id):
    _mark_response_seen(student_id, request_id)
