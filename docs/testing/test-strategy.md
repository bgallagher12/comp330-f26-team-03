# Test Strategy

<!--
STARTER KIT GUIDANCE — DELETE BEFORE PHASE-GATE SUBMISSION

This file defines the team's overall approach to testing and verification.

A test strategy should answer questions such as:

- What kinds of defects are we trying to detect?
- What testing levels matter for this system?
- Which risks require deeper verification?
- What should be automated?
- What still requires human review or manual verification?
- How do requirements and acceptance criteria connect to tests?
- How do we handle negative paths, failures, and regression risk?
- What evidence will demonstrate that testing actually occurred?

This file defines the overall testing APPROACH.

Detailed execution planning belongs in:

/docs/testing/test-plan.md

Specific test scenarios belong in:

/docs/testing/test-cases.md

Automated pipeline evidence belongs in:

/docs/testing/ci-evidence.md

IMPORTANT:

- Everything inside HTML comments is Starter Kit guidance.
- Remove ALL instructional comments before the applicable phase-gate submission.
- Examples are guidance only.
- Do not claim a testing practice exists unless the team actually intends to use it.
-->

## Testing Objectives

<!--
TEAM CONTENT REQUIRED

Describe what the team is trying to accomplish through testing.

Possible objectives include:

- verify requirements;
- verify acceptance criteria;
- detect regressions;
- validate important architecture boundaries;
- verify failure handling;
- verify security behavior;
- verify operational behavior;
- reduce release risk.

Do not simply write:

"Make sure the system works."

- Ensure
-->
Purpose of testing is to verify the applications main features work and meet the requirements. It will focus on ensuring that users can complete support requests and that those requests are handles appropriately. 

### Testing Goals
Ensure the features in Cycle 1 work as expected
Ensure students can submit support requests
Ensure students can view support requests
Check that reviewers can manage requests
Find bugs and problems with how information is displayed or saved
Test how the application handles invalid inputs such as invalid ID number
Ensure valid inputs are processed are handled correctly
Find defects in the interaction between application components
Ensure changes and bugs do not cause existing features to breaks

## Testing Principles

<!--
TEAM CONTENT REQUIRED

Define the principles that guide testing decisions.

Examples ONLY:

- Test behavior against requirements, not implementation assumptions.
- Verify both successful and unsuccessful paths.
- Automate repeatable verification where practical.
- Use human review where judgment is required.
- Preserve evidence of meaningful test execution.
- Add regression coverage when a significant defect is fixed.

Do not retain generic principles merely because they sound good.

Replace this comment with principles the team actually intends to follow.
-->

- Test both expected and failure situations
- Use automated tests so we can test features manually when needed
- Ensure features work and fixing a bug
- Keep track of test results so that other members can know what was tested and what still needs work
- A test is considered passed when the actual result matches the expected result

## Test Levels

<!--
TEAM CONTENT REQUIRED

Define which test levels are appropriate for this system.

Possible levels include:

- Unit
- Component
- Integration
- Contract
- System
- End-to-End
- Acceptance
- Runtime / Operational

Do NOT include every possible test level automatically.

For each level, explain:

- what it verifies;
- what boundary it exercises;
- what kinds of defects it is intended to detect.

EXAMPLE ONLY:

| Test Level | Purpose | Typical Scope | Primary Defects Detected |
|---|---|---|---|
| Unit | Verify isolated business logic | Individual function or module | Logic and boundary-condition defects |
| Integration | Verify interaction among components | Application Service and Persistence | Interface and state-management defects |

DELETE the example and populate the actual table below.
-->

| Test Level | Purpose | Typical Scope | Primary Defects Detected |
|---|---|---|---|
|Unit  | Checks whether functions work properly| Category and Status validation, request data handling | Incorrect conditions, missing validation  |
| Components | Chekcs whether interface component work | Request Form, Request List, Reviewer controls | Incorrect display, missing error messages |
|Integration | Checks whether different parts of the application work together correctly| Sumbission Form, Request Handling, Saving Data, Retrieving Data  | Requests not being saved, incorrect data loaded |
|System  | Checks whether a complete workflow works from start to end  | Submitting a request and its updated through the reviewer workflow| Missing updates  |
| Acceptance | Verify implemented features meet Cycle 1 requirements  | Main student and reviewer workflows  |  | Features fo not meet project requirements

## Test Types

<!--
TEAM CONTENT REQUIRED

Identify test types relevant to the actual system.

Possible types include:

- Functional
- Negative-path
- Regression
- Security
- Performance
- Reliability
- Usability
- Accessibility
- Compatibility
- Recovery
- Deployment verification

Do not add a category merely because it appears in this list.

EXAMPLE ONLY:

| Test Type | Why It Matters | Where Applied |
|---|---|---|
| Negative-path testing | Ensures invalid input does not create invalid state | Workflow submission and authorization |
| Regression testing | Prevents previously corrected defects from returning | Automated CI suite |

Populate actual testing types below.
-->

| Test Type | Why It Matters | Where Applied |
|---|---|---|
| Basic security testing | Checks that the information the user enetered is displayed safely and it does not show security features it does not have | Request Descriptions, Reviewer Notes |
| Regression Testing | Ensures previoulsy fixed bugs do not return  | Re-testing request submissions, reviewer updates  |
| Usability & Accesibility | Ensures users can understand the interface and can use the controls | Form Labels, Keyboard navigation |
|  |  |  |
|  |  |  |

## Requirements and Acceptance-Criteria Coverage

<!--
TEAM CONTENT REQUIRED

Testing should connect to engineering expectations.

Reference:

/docs/requirements/requirements.md
/docs/requirements/acceptance-criteria.md
/docs/planning/traceability.md

A useful chain is:

Requirement
  ->
Acceptance Criterion
  ->
Test
  ->
Test Result
  ->
Release Evidence

Do not require every low-level unit test to map directly to a requirement.

Traceability matters most for meaningful behavior and release claims.

Replace this comment with the team's actual traceability approach.
-->
Requirement -> Acceptance Criterion -> Test -> Test Result -> Release Evidence

## Risk-Based Testing

<!--
TEAM CONTENT REQUIRED

Not every part of the system deserves equal testing depth.

Use risk to guide verification effort.

Consider areas with:

- high impact if incorrect;
- complex logic;
- security significance;
- data integrity consequences;
- external dependencies;
- repeated defect history;
- difficult recovery;
- architectural uncertainty.

Reference:

/docs/planning/risk-register.md

EXAMPLE ONLY:

| Risk / Concern | Additional Testing Approach | Related Evidence |
|---|---|---|
| Unauthorized data access | Multi-user authorization tests and negative-path API verification | R-004, permission-boundaries.md |

DELETE the example and populate actual risk-based testing below.
-->

| Risk / Concern | Additional Testing Approach | Related Evidence |
|---|---|---|
| Invalid input accepted  | Test missing required fields, unsupported categories  | Validation and negative path test results |
| Support Request not saved| Submit a valid request and ensure it appears in the list and reload the page to ensure its still there | List display, request creation  |
| Reviewer update not saved | Update a request and reload the page to ensure it was updated  | Reviewer workflow tests results and related defect or pull request  |
| Browser storage is unavailable |  Failed storage operation and verify that the application does not incorrectly report success | storage error and recovery test results  |

## Positive and Negative Testing

<!--
TEAM CONTENT REQUIRED

Describe how the team will verify both:

POSITIVE PATHS
Expected valid behavior.

NEGATIVE PATHS
Invalid, unauthorized, missing, conflicting, or failed conditions.

Examples of negative conditions may include:

- missing required input;
- malformed data;
- unauthorized operation;
- duplicate request;
- unavailable dependency;
- unknown resource;
- invalid state transition.

Do not test negative conditions merely for volume.

Prioritize those that matter to requirements, security, integrity, and risk.

Replace this comment with the team's actual approach.
-->
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

<!--
TEAM CONTENT REQUIRED

Explain what the team intends to automate and why.

Possible automated checks include:

- unit tests;
- integration tests;
- contract tests;
- regression tests;
- static checks;
- build verification;
- deployment checks.

Also identify what remains manual and why.

Do not claim "everything is automated" unless that is actually true.
-->

| Verification Area | Automated / Manual / Mixed | Reason |
|---|---|---|
|Saving and Retrieving request data | Mixed | Tests can check data handling logic, however the browser testing may be needed to verify localStorage behavior  |
| Usability | Manual  | Human review is important for checking readability of an application  |
|Request creation  |  Automated | Automated checks can help detect logical errors after code changes  |
| Category/Status validation  | Automated | Repeated checks ensure that valid values are accepted and ivalid values are handled appropriately |


## Regression Strategy

<!--
TEAM CONTENT REQUIRED

Describe how the team prevents previously fixed behavior from breaking again.

A practical rule may be:

"When a meaningful defect is fixed, add or update an automated test where
practical so the defect would be detected if it returned."

Reference:

/docs/quality/defect-log.md

Replace this comment with the team's actual regression approach.
-->
Our team will re-test the feature that was corrected and any other parts of the main workflow that is connected to it. An automated test will be either added or updated so that the same issue can be detected if it happens again.
The following checks will be available:
- Submitting support requests
- Viewing sumbitted requests
- Updating requests
- Validating required fields
- Saving and retrieving request information

Bugs and their verification results will be recorded in defect-log.md in the quality folder.

## Test Data Strategy

<!--
TEAM CONTENT REQUIRED

Describe how test data will be created and controlled.

Consider:

- synthetic data;
- test accounts;
- boundary values;
- invalid data;
- duplicate data;
- security-sensitive cases.

Reference:

/docs/security/data-handling-notes.md

Do not place real sensitive personal information into tests merely because it
is convenient.

Replace this comment with the team's actual test-data approach.
-->

We will use fake test data to perform tests. Test data should include:
- Valid requests for each category
- Requests with missing required fields
- Empty values
- Unknown request ID's
- Sample reviewer notes and resolution test
Test data should not have real passwords, health information or any other sensitive personal information. Any data handling-rules in /docs/security/data-handling-notes.md will be followed.

## Environment Strategy

<!--
TEAM CONTENT REQUIRED

Identify where different kinds of tests run.

Examples might include:

- local developer environment;
- CI;
- test deployment;
- staging-like environment;
- deployed course environment.

Explain meaningful differences that could affect results.

Do not create fictional environments.
-->

| Environment | Testing Purpose | Important Differences / Limitations |
|---|---|---|
| Local Browser | Manually test request form, requests list, and browser localStorage | Stored data associated iwth the browser may differe across brwosers or disappear when browser data is cleared. |
| GitHub pull reqquest | Run repeatable checks before cide is merged | The team mist confirm whether a CI workflow exists rand record its actual results rather than assuming it is configured |
| Local Developer environmnet | Run available tests while implementing, debugging adn reviewing code  | Results may depend on the delopers tools, configuration and dependencies  |


## AI-Assisted Testing

<!--
TEAM CONTENT REQUIRED WHEN AI IS USED TO ASSIST TESTING

AI may assist with:

- identifying edge cases;
- proposing test scenarios;
- reviewing test completeness;
- suggesting failure conditions;
- generating initial test code.

AI output is not verification by itself.

The team remains responsible for:

- deciding whether proposed tests are valid;
- understanding generated test code;
- verifying test expectations;
- ensuring tests actually exercise meaningful behavior.

Reference:

/docs/ai/ai-policy.md
/docs/ai/ai-use-log.md

Remove this section if AI-assisted testing is not used.
-->

AI assistance may be used to suggest edge cases, review test coverage and draft initial case scenarios, however any AI suggestions must be reviewed by the team before implemented.
Team members will confirm that:
- Suggested tests match the projects requirements
- Expected results are corrected
- The test code is understood and reviewed before use
Any AI assistance will be recorded on /docs/ai/ai-use-log.md and will follow the AI use policy in /docs/ai/ai-policy.md

## Test Evidence

<!--
TEAM CONTENT REQUIRED

Define what evidence the team preserves.

Possible evidence includes:

- CI run;
- test report;
- test-case result;
- runtime evidence;
- pull request;
- screenshot when appropriate;
- defect verification.

Do not store large amounts of redundant evidence without purpose.

The evidence should be reviewable enough to support important engineering claims.

Replace this comment with the team's actual evidence approach.
-->
We will show clear evidence that important testings are done such as:
- Testings showing expected vs actual results
- Automates test output
- CI results, if a continuous integration workflow exists
- Pull requests or GitHub bugs associated with a defect

If theres a failed test, we will record whether the test was fixed or whether the relevant test passed when repeated. We will also record the steps to reproduce the problem, expected output, actual behavior, follow up work.
## Known Testing Limitations

<!--
TEAM CONTENT REQUIRED

Record limitations honestly.

Examples ONLY:

- no sustained-load testing;
- one external integration verified manually;
- browser compatibility limited;
- recovery testing incomplete;
- performance baseline not yet established.

Reference:

/docs/release/known-limitations.md

when the limitation affects a release.
-->

| Limitation | Impact | Planned Improvement | Related Evidence |
|---|---|---|---|
| CI set up is not confirmed | Tests may not run automatically |  Check if the CI is configured | CI workflow  |
|Use of localStorage  | Data is stored in the browser  | Review storage needs if the app expands  | Architected documents |
| Automated testing is not confirmed | Some buys may go undetected | Add tests where appropriate and possible  | Test results  |
| Test results and peer reviews may be incomplete  | Some issues may remain unresolved  | Run tests and record results |  Test cases and review records |

<!--
FINAL STARTER KIT CHECK — DELETE BEFORE PHASE-GATE SUBMISSION

Before submission:

1. Define testing objectives that actually matter to the project.
2. Include only test levels and types the team genuinely uses.
3. Connect important verification to requirements and acceptance criteria.
4. Use risk to guide test depth.
5. Include meaningful negative-path testing.
6. Be explicit about what is automated versus manual.
7. Describe regression and test-data practices.
8. Identify real test environments.
9. State testing limitations honestly.
10. Remove ALL instructional HTML comments.

The completed strategy should explain WHY the team tests the way it does, not
serve as a generic catalog of testing terminology.
-->
