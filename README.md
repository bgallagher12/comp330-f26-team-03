# Campus Connect

Campus Connect is Team 03's software engineering project for COMP 330 at Loyola University Chicago.

## Project Overview

**TODO before A1 submission:** Add a concise description of:

* the problem Campus Connect solves;
* its intended users or stakeholders;
* its primary purpose; and
* the major scope of the system.

Detailed functional requirements and acceptance criteria are maintained under:

[`docs/requirements/`](docs/requirements/)

## Project Status

**Current Phase Gate:** A1 — Project Launch
**Release Cycle:** Cycle 1
**Status:** Active Development

## Team

Team membership, GitHub identities, specialized engineering roles, backup responsibilities, and acknowledgement evidence are maintained in:

[`docs/team/roles.md`](docs/team/roles.md)

Team operating practices are documented in:

* [`docs/team/team-charter.md`](docs/team/team-charter.md)
* [`docs/team/working-agreements.md`](docs/team/working-agreements.md)

## Engineering Evidence

This repository is the **authoritative engineering record** for Campus Connect.

Engineering evidence is organized throughout the repository:

* **AI Use and Verification** → [`docs/ai/`](docs/ai/)
* **Architecture** → [`docs/architecture/`](docs/architecture/)
* **Engineering Decisions** → [`docs/decisions/`](docs/decisions/)
* **Observability** → [`docs/observability/`](docs/observability/)
* **Operations** → [`docs/operations/`](docs/operations/)
* **Planning and Traceability** → [`docs/planning/`](docs/planning/)
* **Quality and Defects** → [`docs/quality/`](docs/quality/)
* **Release Evidence** → [`docs/release/`](docs/release/)
* **Requirements and Acceptance Criteria** → [`docs/requirements/`](docs/requirements/)
* **Engineering Reviews** → [`docs/review/`](docs/review/)
* **Security and Data Handling** → [`docs/security/`](docs/security/)
* **Team Evidence** → [`docs/team/`](docs/team/)
* **Testing and Verification** → [`docs/testing/`](docs/testing/)

Detailed evidence should remain in its authoritative artifact rather than being duplicated in this README.

## Repository Structure

| Path             | Purpose                                                                      |
| ---------------- | ---------------------------------------------------------------------------- |
| `src/`           | Production application source code                                           |
| `tests/`         | Automated tests and supporting test code                                     |
| `test-evidence/` | Preserved testing and verification evidence                                  |
| `data/`          | Project, sample, fixture, or reference data                                  |
| `scripts/`       | Development, verification, deployment, or maintenance utilities              |
| `docs/`          | Engineering evidence and project documentation                               |
| `.github/`       | Issue templates, pull-request guidance, workflows, and repository automation |

## Build, Run, and Test

Campus Connect is currently in the **A1 — Project Launch** phase. Build, run, and test procedures will be documented as the implementation stack and development environment are established.

### Prerequisites

Project-specific software and development prerequisites have not yet been finalized.

Known repository requirements include:

* Git
* GitHub access to the private Team 03 repository

Additional runtimes, package managers, frameworks, databases, and development tools will be documented once selected.

### Setup

Clone the Team 03 repository:

```bash
git clone https://github.com/bgallagher12/comp330-f26-team-03.git
cd comp330-f26-team-03
```

Confirm the repository state:

```bash
git status
```

Project-specific environment setup instructions will be added as implementation begins.

### Build

A project-specific build process has not yet been established.

This section will be updated once the implementation technology stack is selected.

### Run

Application run instructions will be added once an executable version of Campus Connect exists.

### Test

Automated testing procedures will be documented as the project's test infrastructure is established.

Detailed testing strategy and verification evidence will be maintained under:

[`docs/testing/`](docs/testing/)

## Engineering Workflow

Team 03 follows a repository-centered engineering workflow:

```text
Issue → Branch → Implementation → Pull Request → Review → Merge
```

GitHub Issues are used to track bugs, engineering tasks, blockers, and other work requiring repository-visible traceability.

Development work should normally occur on branches rather than through significant direct changes to `main`.

Pull requests should provide enough information for another team member to understand the change and its verification.

Detailed team workflow expectations are maintained in:

[`docs/team/working-agreements.md`](docs/team/working-agreements.md)

## Engineering Practices

Team 03 follows engineering practices including:

* requirements and acceptance-criteria traceability;
* GitHub issue and pull-request workflows;
* peer review;
* documented engineering decisions;
* testing and verification;
* defect and quality management;
* security and responsible data handling;
* AI-assisted engineering with human verification;
* release-readiness evidence; and
* operational and observability evidence as the system develops.

Engineering evidence should be created and maintained as work occurs rather than reconstructed only before a phase-gate submission.

## Engineering Evidence Model

Important engineering work should remain traceable through the repository.

A typical relationship may look like:

```text
Requirement
    ↓
Acceptance Criterion
    ↓
Architecture / Decision
    ↓
Implementation
    ↓
Test / Review
    ↓
Verification Evidence
```

Not every artifact requires every link. The goal is meaningful engineering traceability rather than unnecessary documentation.

## AI-Assisted Engineering

Team 03 uses AI as an engineering **copilot**.

AI may assist with requirements, planning, implementation, debugging, testing, review, and documentation, but it does not replace human engineering responsibility.

Team members are responsible for understanding, reviewing, verifying, and being able to explain AI-assisted work before it is accepted into the project.

The team's AI policy is maintained in:

[`docs/ai/ai-policy.md`](docs/ai/ai-policy.md)

Meaningful AI-assisted engineering activity is recorded in:

[`docs/ai/ai-use-log.md`](docs/ai/ai-use-log.md)

## Team Operations

The team uses **Microsoft Teams** for routine communication.

Regular team meetings are held:

**Wednesdays at 1:00 PM**

GitHub Issues are used for repository-visible bugs, tasks, blockers, and engineering work.

Additional team practices and responsibilities are documented under:

[`docs/team/`](docs/team/)

## Engineering Operating Model

COMP 330 uses three complementary environments:

* **Sakai** — authoritative source for course requirements, assignments, deadlines, naming, grading, and submission expectations.
* **ETIS** — professional engineering guidance and reference material.
* **GitHub** — authoritative engineering record for Team 03's project, decisions, implementation, reviews, testing, and evidence.

**Sakai defines what the course requires.**
**ETIS provides professional engineering guidance.**
**GitHub preserves evidence of what the team actually engineered.**

## Professional Engineering Expectations

A reviewer examining this repository should be able to determine:

* what Campus Connect is intended to accomplish;
* who owns and contributes to the work;
* what requirements define expected behavior;
* what assumptions and risks remain;
* what engineering decisions were made and why;
* how implementation connects to requirements;
* what was reviewed and tested;
* how defects were handled;
* how AI-assisted work was disclosed and verified;
* how security and data handling were considered; and
* what limitations remain.

A working system is necessary, but professional engineering also requires the system and its development process to be understandable, reviewable, testable, maintainable, and traceable.

## Course Context

This repository was created from the **COMP 330/474 Fall 2026 Repository Starter Kit** for Software Engineering at Loyola University Chicago.

The starter kit provides the initial repository structure and engineering evidence model. Team 03 is responsible for replacing that initial scaffold with project-specific engineering evidence as Campus Connect develops.
