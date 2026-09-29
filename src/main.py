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
# 4. Record the submission time.
# 5. Give the request a default status (NEW or OPEN).
# 6. Determine the request category.
# 7. Determine where the request should be sent.
# 8. Make the request available for staff/instructor review.


# ------------------------------------------------------------
# Required Fields
# ------------------------------------------------------------

# Possible required fields:
#
# - Student ID / submitter
# - Request description
# - Category
#
# Possible fields depending on the request:
#
# - Course
# - Instructor
# - Department
# - Priority
#
# Questions:
# - Is course information required for every request?
# - Is an instructor required for course-related requests?
# - Is priority required?


# ------------------------------------------------------------
# Validation
# ------------------------------------------------------------

# Before accepting a request:
#
# - Check that the student/submitter is identified.
# - Check that the request description is not empty.
# - Check that a category has been selected.
# - Check course information if the category requires it.
#
# If required information is missing:
# - Do not accept the request yet.
# - Tell the student which information is missing.
#
# Pseudocode:
#
# receive request
#     check required fields
#
#     if information is missing:
#         return an error
#
#     else:
#         continue processing the request


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
#
# Question:
# - Should the initial status be NEW or OPEN?


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
