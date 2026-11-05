"""
Student-side request service for CampusConnect.

This file contains the functions Sherry's terminal interface will call
when a student submits a request or checks the status of an existing request.

For now, these functions use mock_backend.py as temporary storage.
Later, the mock backend can be replaced with Carlos's real database functions.
"""

# Import the temporary storage functions from mock_backend.py.
# The imported functions are renamed with a leading underscore so it is clear
# that they are internal helpers used by this service file.
from src.mock_backend import (
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
