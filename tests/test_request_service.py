import unittest

from src.request_service import submit_request, get_request_status
from src.mock_backend import resolve_request


class TestRequestService(unittest.TestCase):

    # Verify that a request with all required information is successfully created.
    # This test checks that the backend generates a request ID,
    # starts the request with the "submitted" status,
    # and keeps student_id stored as text.
    def test_valid_request_is_created(self):
        details = {
            "student_id": "12345",
            "student_name": "Test Student",
            "student_email": "test@example.com",
            "title": "Need tutoring help",
            "description": "I need help with my class.",
            "category": "Tutoring",
        }

        result = submit_request(details)

        self.assertIn("request_id", result)
        self.assertEqual(result["status"], "submitted")
        self.assertEqual(result["student_id"], "12345")

    # Verify that a request is rejected when required information is missing.
    # This test uses an empty description and confirms that the service
    # raises a clear validation error instead of creating an incomplete request.
    def test_missing_required_description_is_rejected(self):
        details = {
            "student_id": "12345",
            "student_name": "Test Student",
            "student_email": "test@example.com",
            "title": "Need tutoring help",
            "description": "",
            "category": "Tutoring",
        }

        with self.assertRaisesRegex(ValueError, "description is required."):
            submit_request(details)

    # Verify that a student can retrieve the current status and resolution
    # for a request that was previously submitted.
    # This test creates a request, uses its generated request_id,
    # and confirms that the saved request can be looked up correctly.
    def test_request_status_can_be_retrieved(self):
        details = {
            "student_id": "12345",
            "student_name": "Test Student",
            "student_email": "test@example.com",
            "title": "Projector problem",
            "description": "The projector is not turning on.",
            "category": "Technology",
        }

        submitted_request = submit_request(details)
        request_id = submitted_request["request_id"]

        result = get_request_status(request_id)

        self.assertEqual(result["request_id"], request_id)
        self.assertEqual(result["status"], "submitted")
        self.assertIsNone(result["resolution"])

    # Verify that looking up a request ID that does not exist
    # produces a clear error instead of returning incorrect data.
    def test_unknown_request_returns_error(self):
        with self.assertRaisesRegex(ValueError, "Request not found."):
            get_request_status(99999)

    # Verify that a request with an unsupported category is rejected.
    # This prevents the system from saving category values that are not
    # part of the approved CampusConnect category list.
    def test_invalid_category_is_rejected(self):
        details = {
            "student_id": "12345",
            "student_name": "Test Student",
            "student_email": "test@example.com",
            "title": "Software installation issue",
            "description": "A required application will not install correctly.",
            "category": "Software Support",
        }

        with self.assertRaisesRegex(ValueError, "Choose a valid category."):
            submit_request(details)

    # Verify that the student-side status function retrieves updates
    # that were saved by the reviewer side.
    # This test submits a request, simulates a reviewer resolution,
    # and confirms that the student receives the updated status and resolution.
    def test_resolved_request_returns_updated_status_and_resolution(self):
        details = {
            "student_id": "12345",
            "student_name": "Test Student",
            "student_email": "test@example.com",
            "title": "Computer login issue",
            "description": "I cannot log in to the lab computer.",
            "category": "Technology",
        }

        submitted_request = submit_request(details)
        request_id = submitted_request["request_id"]

        resolve_request(request_id, "Student account access was restored.")

        result = get_request_status(request_id)

        self.assertEqual(result["status"], "resolved")
        self.assertEqual(
            result["resolution"],
            "Student account access was restored."
        )


# Run the tests in this file when it is executed directly.
if __name__ == "__main__":
    unittest.main()
