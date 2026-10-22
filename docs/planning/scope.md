# Project Scope

## Scope Statement
Campus Connect is a system designed for stuents to submit support requests and allows support reviewers to manage and resolve those requeets. Students submit information about their issue and are able to check the status of their request. Reeviwers can view, update the request status, add notes and information about how the request was solved. The system is also able to keep records of important requests.

Our project will focus on the process from when a student submits a request to a reviewer resolving that request and to when a student can see the updated status of their request.

## In Scope

| Scope ID | Included Capability / Work | Related Requirements | Notes |
|---|---|---|---|
|SCP-001| Student Request Submission | TBD| Students submit their support requests|
|SCP-002|Request Validation|TBD|Checking Request Information|
|SCP-003|Request Categories| TBD| Organizing Requests by categories|
|SCP-004|Backend Request Processing|TBD|Requests are receivedvalidated and prepared for review|
|SCP-005|Request Dashboard|TBD|Requests can be viewed and managed|
|SCP-006|Status Updates|TBD|Reviewers can update requests|
|SCP-007|Notes|TBD|Reviewers can add notes after the request is resolved|
|SCP-008|Database and ER Diagram| TBD| Initial database and ER diagram|
|SCP-009|Request History|TBD| Requests can be recorded|

## Out of Scope

| Item | Reason Excluded | Future Consideration |
|---|---|---|
| Sensitive student data in the repository | Data from the project shouldnt contain personal or sensitive information  |Use protected storage if real data is ever required  |
|API keys| Secrets shouldnt be stored in the Git repository|Use an appropriate secure configuration method|
|Large datasets| git is not supposed to used as general storage for large datasets| Store the data using a more appropriate method|
|Actual student records with university systems | Cycle 1 uses synthetic data and wont need real student records | Reconsider if a future scope requires real data  |

## Scope Constraints

| Constraint | Impact on Scope | Related Evidence |
|---|---|---|
|Team size| Work should be divided among team members | Team Work Plan |
|Technology| The system should work with programming languages and technologies selected by team members| Planning Notes|
|Database| Request information should be stored and rerieved through the projects database| Planning Notes|
|Data security| Project data shouldnt contain passwords or other sensitive information| Data Guidance|
|Synthetic Data | Development and testing must use synthetic data instead of actual student information| docs/decisions/adr-0001-use-synthetic-data-for-cycle-1.md, data-context.md|

## Dependencies Affecting Scope

| Dependency | Why It Matters | Owner / Source | Related Risk |
|---|---|---|---|
| Database | The database should be able to save requests, statusesm notes, resolution, request history | Carlos  |TBD  |
|Backend| Needs to Process requests and interact with the database|Everyone|TBD|
|Frontend|Interface should allow students to submit and their requests and reviewers should be able to managae the requests|Sherry & Jaylen|TBD|
|Data|Appropraite data should be used to test creating requests, status changes and incomplete requests|Carlos|TBD|

## Deferred Scope

| Item | Reason Deferred | Decision / Evidence | Reconsider By |
|---|---|---|---|
|User Permissions  | We have not finalized what students and reviewers can access or change  | Planning Notes  | TBD  |
|Incomplete Requests| Has been discussed but we have not decided how to handle it yet|Planning Notes| TBD|

## Scope Change History

| Effective Gate | Change | Added / Removed | Reason | Related Evidence |
|---|---|---|---|---|
|  |  |  |  |  |

## Scope Acceptance Check

