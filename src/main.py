"""
Campus Connect - Entry Point
Cycle 1 Goal
- Student can submit request
- Support reviewer can view request
- Reviewer can update request
- Student can view request status
"""

# ============================================================
# Imports
# ============================================================

# TODO: Import application/framework dependencies here.
# Example:
# from flask import Flask, request, jsonify
#
# TODO: Import project modules as they are created.
# Example:
# from database import ...
# from models import ...
# from services import ...

# ============================================================
# Application Setup
# ============================================================

# TODO: Create/configure the application.
#
# Responsibilities:
# 1. Initialize the application.
# 2. Load configuration.
# 3. Initialize any database/storage connection.
# 4. Register routes/components.
#
# Keep configuration separate from business logic when possible.

# ============================================================
# Requester Workflow
# ============================================================

# TODO: Implement the workflow for submitting a support request.
#
# Expected basic flow:
# 1. Receive request information from the student/requester.
# 2. Validate required information.
# 3. Create/store the request.
# 4. Return confirmation to the requester.
#
# Requirement traceability:
# REQ-001 - Student requester can create and submit a support request.
# REQ-002 - System assigns a unique ID and preserves the request.
# REQ-009 - Only synthetic/approved sample data is used.

# ============================================================
# Request Processing
# ============================================================

# TODO: Determine the required fields for a submitted request.
#
# Possible fields:
# - requester/student identifier
# - request title/subject
# - request description
# - request category
#
# Fields still being considered:
# - course or department
# - instructor
# - priority
# - assigned staff member
#
# TODO: Validate required fields before accepting a request.
#
# Possible validation flow:
# 1. Check that all required fields are present.
# 2. Reject the request if required information is missing.
# 3. Validate the category against supported categories.
# 4. Assign a unique request ID.
# 5. Record the submission time.
# 6. Assign an initial request status.
# 7. Store the request for later retrieval.
#
# NOTE:
# The exact required fields and initial status still need
# team agreement and should match the approved requirements.

# ============================================================
# Reviewer Workflow
# ============================================================

# TODO: Implement the workflow for support reviewers.
#
# Expected basic flow:
# 1. Retrieve submitted requests.
# 2. Display relevant request information.
# 3. Allow reviewer to assign/update status.
# 4. Record any resolution information.
#
# Keep reviewer actions separate from requester actions.
#
# Requirement traceability:
# REQ-003 - Reviewer can view submitted requests.
# REQ-004 - Reviewer can update request status.
# REQ-005 - Reviewer can record a note or resolution.
# REQ-007 - Requester and reviewer behavior remain distinct.
# REQ-008 - Important status changes and reviewer actions are inspectable.

# ============================================================
# Reviewer Information
# ============================================================

# TODO: Determine which request information reviewers need.
#
# Possible reviewer-facing information:
# - Request ID
# - Requester
# - Request title/description
# - Category
# - Submission time
# - Current status
#
# Possible additional information:
# - Course or department
# - Priority
# - Assigned staff member
#
# The final set of fields should be confirmed by the team.

# ============================================================
# Request Status
# ============================================================

# TODO: Define the small set of Cycle 1 request statuses.
#
# Example:
#   - submitted
#   - in_progress
#   - resolved
#
# Do not add additional statuses unless they are part of
# the approved requirements.


# ============================================================
# Requester Status View
# ============================================================

# TODO: Allow a requester to retrieve/view the current
# status of their submitted request.
#
# Expected flow:
# 1. Identify the request.
# 2. Retrieve its current state.
# 3. Display the status and relevant information.
#
# TODO: Add validation for invalid/missing request IDs.
#
# Requirement traceability:
# REQ-006 - Student requester can view current status
# and available resolution information.

# ============================================================
# Validation and Error Handling
# ============================================================

# TODO: Handle invalid input consistently.
#
# Examples:
# - Missing required request information
# - Invalid request ID
# - Unsupported status value
# - Request does not exist
#
# Errors should provide useful information without exposing
# unnecessary internal details.

# ============================================================
# Category Processing
# ============================================================

# TODO: Determine whether request categories affect routing
# or processing.
#
# Possible behavior:
#
# Tech Support:
# - Could be routed to technical support staff.
#
# Course Question:
# - Could be associated with a course or instructor.
#
# Facilities:
# - Could be routed to the appropriate facilities department.
#
# These category rules are brainstorming only and should not
# be treated as finalized requirements yet.

# ============================================================
# Assumptions and Open Questions
# ============================================================

# Assumptions:
# - Cycle 1 uses synthetic/sample data only.
# - Each accepted request needs a unique identifier.
# - Submitted requests must be retrievable by a reviewer.
#
# Open questions:
# - What fields are officially required?
# - What should the default request status be?
# - Which request categories will Cycle 1 support?
# - Should submission time be generated automatically?
# - Are requests associated with courses or instructors?
# - Will requests be assigned to individual staff members?
# - Is priority needed for Cycle 1?
# - Who is responsible for category-based routing?

# ============================================================
# Application Entry Point
# ============================================================

def main():
    """
    Start the CampusConnect application.

    TODO:
    - Initialize application components.
    - Start the application/server.
    - Add startup validation if needed.
    """

    # TODO: Start application
    pass


if __name__ == "__main__":
    main()

"""
Backend Request Processing Logic

Initial planning and pseudocode for handling student requests.
No actual backend implementation yet.
"""

# ------------------------------------------------------------
# Student Request Submission
# ------------------------------------------------------------

# When a student submits a request:
#
# 1. Receive the request.
# 2. Check that all required information is provided.
# 3. Validate the information.
#    - If validation succeeds:
#      - assign a request ID
#      - record the submission time
#      - assign a default status (NEW or OPEN)
#      - determine the request category
#      - determine where the request should be sent
#      - make request available for review
#    - If validation fails:
#      - do not accept the request
#      - identify which required information in missing/invalid
#      - return an appropriate error to the student
#
# PSEUDOCODE:
#
# receive_request(student_submission)
#
#     validate required fields
#
#     IF required information is missing:
#         return validation error
#
#     record submission timestamp
#     assign default status = NEW
#     determine category
#     determine routing
#     prepare request for review


# ------------------------------------------------------------
# Required Fields
# ------------------------------------------------------------

# Possible required fields:
#
# - Student/submitter ID
# - Student name or other identifying information
# - Request description
# - Category
#
# Possible fields depending on the request:
#
# - Course ID/Name
# - Instructor
# - Department
#
# Questions:
# - Is student ID enough to identify the submitter?
# - Should student name be stored directly or retrieved from the
#   student's account?
# - Is a course required for every request?
# - Is a department required for every request?
# - Can some categories be submitted without course information?


# ------------------------------------------------------------
# Validation
# ------------------------------------------------------------

# Before accepting a request, check:
#
# - Required fields are present.
# - Required fields are not empty.
# - Category is one of the supported categories.
# - Description contains enough information to review the request.
# - Course information is valid when the category requires a course.
#
# If required information is missing:
# - Do not accept the request yet.
# - Tell the student which information is missing.
#
# PSEUDOCODE:
#
# validate_request(request)
#
#     IF student information is missing:
#         reject request
#
#     IF description is missing:
#         reject request
#
#     IF category is missing:
#         reject request
#
#     IF category requires course information
#         AND course information is missing:
#         reject request
#
#     IF all required information is valid:
#         accept request
#
# Questions:
#
# - What should count as an invalid description?
# - Should there be a minimum description length?
# - Should invalid categories be rejected or changed to "Other"?
# - Should validation errors be shown to the student individually
#   or all at once?


# ------------------------------------------------------------
# Request Information
# ------------------------------------------------------------

# A submitted request may need:
#
# - Request ID
# - Student/submitter
# - Course or department
# - Instructor, if applicable
# - Description of the problem/question
# - Submission time
# - Category
# - Priority
# - Assigned staff member
# - Current status
#
# The system should automatically record the submission time.
#
# Possible initial status:
# - NEW
# - OPEN
# - IN_PROGRESS
# - RESOLVED
#
# Question:
# - Should the initial status be NEW or OPEN?
# - Who changes the status?
# - Should the student be able to see the status?
# - Should the system automatically update any statuses?

# ------------------------------------------------------------
# Category Logic
# ------------------------------------------------------------

# Different categories may require different processing.
#
# Pseudocode:
#
# if category == "Tech Support":
#     determine which technical support staff should receive it
#
# if category == "Course Question":
#     identify the related course
#     identify the instructor
#     determine whether the instructor should receive it
#
# if category == "Facilities":
#     determine which facilities department should receive it
#
# if category == "Other":
#     send the request to a general support queue
#
# These rules are not finalized yet.


# ------------------------------------------------------------
# Assignment and Priority
# ------------------------------------------------------------

# Questions to determine:
#
# - Does every request need an assigned staff member?
# - Should requests be automatically assigned?
# - Can requests remain unassigned?
# - Who determines the priority?
# - Can students select a priority?
#
# Possible priority values:
# - LOW
# - MEDIUM
# - HIGH
# - URGENT


# ------------------------------------------------------------
# Assumptions
# ------------------------------------------------------------

# Current assumptions:
#
# - Every request has a submitter.
# - Every request has a description.
# - Every request has a category.
# - The submission time should be recorded automatically.
# - A new request should receive a default status.
# - Some categories may require course, instructor, or department
#   information.
# - Category may determine where the request is sent.


# ------------------------------------------------------------
# Open Questions / Future Work
# ------------------------------------------------------------

# - What are the final request categories?
# - Which fields are required for every request?
# - Which fields are only required for certain categories?
# - Should the default status be NEW or OPEN?
# - How should priority be determined?
# - Should requests be automatically assigned?
# - Who can change the status?
# - Who can change the category?
# - What happens if a request cannot be automatically routed?
# - What information should students be able to see after submitting?
#
# Future implementation should be based on the answers to these
# questions and the final backend/database design.

