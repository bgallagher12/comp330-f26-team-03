# Data Context — Campus Connect

**Project:** Campus Connect  
**Team:** COMP 330 — Team 03  
**Primary Engineer:** Brendan Gallagher  
**Reviewer:** Carlos Alcala  
**Status:** Draft — Pending Review

## 1. Authoritative Data Sources

Campus Connect manages student support requests and their associated statuses, reviewer notes, and resolutions.

The application's primary data will include:

- Unique request identifiers
- Student support request details
- Current request status
- Reviewer notes and updates
- Resolution information

For Cycle 1, the project will use synthetic data rather than actual student records.

The application's database and storage technology have not yet been selected. The team will document the authoritative application data store once that decision is finalized.

GitHub is the authoritative source for engineering documentation, requirements, and project decisions.

## 2. Sensitive Data

Support requests could potentially contain personal student information if the system were used in a real university environment.

Potentially sensitive information includes:

- Student identifying information
- Details submitted in support requests
- Private reviewer notes
- Information about request resolutions

Cycle 1 will use synthetic data to avoid exposing real student information during development and testing.

## 3. Data Ownership

Campus Connect has two primary user roles:

**Student Requesters**
- Submit support requests.
- View their request status.
- View resolution information.

**Support Reviewers**
- View support requests.
- Update request statuses.
- Record notes and resolutions.

The team will define component-level data ownership as the system architecture and implementation are finalized.

## 4. AI Context Sources

Team 03 uses AI tools as engineering assistants for planning, development, testing, and documentation.

AI-assisted engineering work should follow the team's documented AI policies.

Relevant documentation:

- `docs/ai/ai-policy.md`
- `docs/ai/ai-use-log.md`

The team will document any AI integration into the Campus Connect application if one is introduced. The current README does not establish an application-level AI feature.

## 5. Data Visibility and Access

Campus Connect will distinguish between student requesters and support reviewers.

Students should be able to view the status and resolution information associated with their own requests.

Support reviewers require access to requests they are responsible for processing.

Detailed authorization rules and enforcement mechanisms still need to be defined and verified during implementation.

## 6. Logging Expectations

Logging requirements will be finalized as the application architecture develops.

Potential events to record include:

- Request creation
- Request status changes
- Reviewer updates
- Request resolution
- Application errors

Logs should avoid exposing unnecessary sensitive information.

## 7. Open Decisions

The following items remain unresolved:

- Database and storage technology
- Authentication and authorization implementation
- Detailed data retention requirements
- Logging implementation
- Component-level data ownership

These decisions should be documented as the team progresses through Cycle 1.

## 8. Review

**Primary Engineer:** Brendan Gallagher  
**Reviewer:** Carlos Alcala  
**Review Status:** Pending

Reviewer feedback and required changes will be recorded after review.