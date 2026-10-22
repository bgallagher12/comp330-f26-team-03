# Test Strategy

## Testing Objectives

Purpose of testing is to verify the application's main features work and meet the requirements. Testing will focus on whether students can submit and view support requests and whether reviewers can manage them correctly.

### Testing Goals

- Ensure Cycle 1 features work as expected.
- Verify students can submit support requests.
- Verify students can view their requests.
- Check that reviewers can manage requests.
- Identify problems with displaying or saving information.
- Test invalid inputs, including invalid request IDs.
- Verify valid inputs are processed correctly.
- Identify defects between application components.
- Check that bug fixes do not break existing features.

## Testing Principles

- Test both expected and failure situations
- Use automated tests so we can test features manually when needed
- Ensure features work and fixing a bug
- Keep track of test results so that other members can know what was tested and what still needs work
- A test is considered passed when the actual result matches the expected result

## Test Levels

| Test Level | Purpose | Typical Scope | Primary Defects Detected |
|---|---|---|---|
|Unit  | Checks whether functions work properly| Category and Status validation, request data handling | Incorrect conditions, missing validation  |
| Components | Chekcs whether interface component work | Request Form, Request List, Reviewer controls | Incorrect display, missing error messages |
|Integration | Checks whether different parts of the application work together correctly| Sumbission Form, Request Handling, Saving Data, Retrieving Data  | Requests not being saved, incorrect data loaded |
|System  | Checks whether a complete workflow works from start to end  | Submitting a request and its updated through the reviewer workflow| Missing updates  |
| Acceptance | Verify implemented features meet Cycle 1 requirements  | Main student and reviewer workflows  |  | Features fo not meet project requirements

## Test Types

| Test Type | Why It Matters | Where Applied |
|---|---|---|
| Basic security testing | Checks that the information the user enetered is displayed safely and it does not show security features it does not have | Request Descriptions, Reviewer Notes |
| Regression Testing | Ensures previoulsy fixed bugs do not return  | Re-testing request submissions, reviewer updates  |
| Usability & Accesibility | Ensures users can understand the interface and can use the controls | Form Labels, Keyboard navigation |

## Requirements and Acceptance-Criteria Coverage

Requirement -> Acceptance Criterion -> Test -> Test Result -> Release Evidence

## Risk-Based Testing

| Risk / Concern | Additional Testing Approach | Related Evidence |
|---|---|---|
| Invalid input accepted  | Test missing required fields, unsupported categories  | Validation and negative path test results |
| Support Request not saved| Submit a valid request and ensure it appears in the list and reload the page to ensure its still there | List display, request creation  |
| Reviewer update not saved | Update a request and reload the page to ensure it was updated  | Reviewer workflow tests results and related defect or pull request  |
| Browser storage is unavailable |  Failed storage operation and verify that the application does not incorrectly report success | storage error and recovery test results  |

## Positive and Negative Testing

### Positive Testing
 Checks the application works correctly when users provide valid inputs and information. For example:
  - submitting a request will all the required fields
  - Being able to locate the request in the list
  - Reviewer updates the status and either add notes or records a resolution
We will also check whether the changes were saved after the application is reloaded
### Negative Testing
Checks how the applcation responds to invalid inormation. For example:
- submitting a request with missing fields such as first name, student ID etc.
- Using an unknown request IF
- Encountering data that cannot be read or written
The expected result is that the application provides a clear error message when applicable and should avoid unintended changes to request. The application should not report that the request was saved.

## Automation Strategy

| Verification Area | Automated / Manual / Mixed | Reason |
|---|---|---|
|Saving and Retrieving request data | Mixed | Tests can check data handling logic, however the browser testing may be needed to verify localStorage behavior  |
| Usability | Manual  | Human review is important for checking readability of an application  |
|Request creation  |  Automated | Automated checks can help detect logical errors after code changes  |
| Category/Status validation  | Automated | Repeated checks ensure that valid values are accepted and ivalid values are handled appropriately |

## Regression Strategy

Our team will re-test the feature that was corrected and any other parts of the main workflow that is connected to it. An automated test will be either added or updated so that the same issue can be detected if it happens again.
The following checks will be available:
- Submitting support requests
- Viewing sumbitted requests
- Updating requests
- Validating required fields
- Saving and retrieving request information

Bugs and their verification results will be recorded in defect-log.md in the quality folder.

## Test Data Strategy

We will use fake test data to perform tests. Test data should include:
- Valid requests for each category
- Requests with missing required fields
- Empty values
- Unknown request ID's
- Sample reviewer notes and resolution test
Test data should not have real passwords, health information or any other sensitive personal information. Any data handling-rules in /docs/security/data-handling-notes.md will be followed.

## Environment Strategy

| Environment | Testing Purpose | Important Differences / Limitations |
|---|---|---|
| Local Browser | Manually test request form, requests list, and browser localStorage | Stored data associated iwth the browser may differe across brwosers or disappear when browser data is cleared. |
| GitHub pull reqquest | Run repeatable checks before cide is merged | The team mist confirm whether a CI workflow exists rand record its actual results rather than assuming it is configured |
| Local Developer environmnet | Run available tests while implementing, debugging adn reviewing code  | Results may depend on the delopers tools, configuration and dependencies  |

## AI-Assisted Testing

AI assistance may be used to suggest edge cases, review test coverage and draft initial case scenarios, however any AI suggestions must be reviewed by the team before implemented.
Team members will confirm that:
- Suggested tests match the projects requirements
- Expected results are corrected
- The test code is understood and reviewed before use
Any AI assistance will be recorded on /docs/ai/ai-use-log.md and will follow the AI use policy in /docs/ai/ai-policy.md

## Test Evidence

We will show clear evidence that important testings are done such as:
- Testings showing expected vs actual results
- Automates test output
- CI results, if a continuous integration workflow exists
- Pull requests or GitHub bugs associated with a defect

If theres a failed test, we will record whether the test was fixed or whether the relevant test passed when repeated. We will also record the steps to reproduce the problem, expected output, actual behavior, follow up work.
## Known Testing Limitations

| Limitation | Impact | Planned Improvement | Related Evidence |
|---|---|---|---|
| CI set up is not confirmed | Tests may not run automatically |  Check if the CI is configured | CI workflow  |
|Use of localStorage  | Data is stored in the browser  | Review storage needs if the app expands  | Architected documents |
| Automated testing is not confirmed | Some buys may go undetected | Add tests where appropriate and possible  | Test results  |
| Test results and peer reviews may be incomplete  | Some issues may remain unresolved  | Run tests and record results |  Test cases and review records |

