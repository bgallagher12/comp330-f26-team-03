"""
Student-side request service for CampusConnect.

Validates student requests and retrieves their status
using shared SQLite storage.
"""

from src.database import (
    submit_request as _save_request,
    get_request_status as _get_request_status,
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


# Retrieve the saved information for an existing request.
# The request_id identifies which request should be looked up.
# The returned record includes the current status and resolution,
# which allows the student interface to display any reviewer updates.
def get_request_status(request_id):
    return _get_request_status(request_id)
