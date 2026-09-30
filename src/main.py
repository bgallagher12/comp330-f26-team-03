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
