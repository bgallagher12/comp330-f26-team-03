# Campus Connect

Campus Connect is Team 03's software engineering project for COMP 330 at Loyola University Chicago.

## Project Overview

Campus Connect is a student support request and workflow system designed to give students a clear way to submit support requests and allow support reviewers to track, update, and resolve them. It addresses the problem of requests being handled through scattered emails, documents, or informal follow-up, where ownership and status can become unclear.

The primary users are student requesters and support reviewers. Students can submit requests and view their current status and resolution information, while reviewers can view requests, update their status, and record notes or resolutions.

For Cycle 1, the project focuses on a small end-to-end workflow rather than a full university platform. The system will support request submission using synthetic data, unique request identification, reviewer processing, status updates, resolution tracking, and student visibility into the outcome.

Detailed functional requirements and acceptance criteria are maintained under:

[`docs/requirements/`](docs/requirements/)

## Project Status

**Current phase:** Assignment 6 Cycle 2 release candidate.
**Release scope:** Supervised local demonstration using synthetic data, pending team review and final CI.

Start with the [A6 release evidence](docs/release/assignment6-final-release-package.md), [release notes](docs/release/final-release-notes.md), and [runbook](docs/operations/runbook.md). The [A5 tag](https://github.com/bgallagher12/comp330-f26-team-03/releases/tag/a5-verification-release) preserves the Cycle 1 evidence.

## Team

Team membership, GitHub identities, specialized engineering roles, backup responsibilities, and acknowledgement evidence are maintained in:

[`docs/team/roles.md`](docs/team/roles.md)

Team operating practices are documented in:

* [`docs/team/team-charter.md`](docs/team/team-charter.md)
* [`docs/team/working-agreements.md`](docs/team/working-agreements.md)

## Engineering Evidence

This repository serves as the authoritative engineering record for Campus Connect.

Major evidence areas include:

* [`docs/ai/`](docs/ai/) — AI-use policy, logs, and verification evidence
* [`docs/architecture/`](docs/architecture/) — architecture and system design
* [`docs/decisions/`](docs/decisions/) — significant engineering decisions
* [`docs/observability/`](docs/observability/) — runtime and observability evidence
* [`docs/operations/`](docs/operations/) — operational guidance
* [`docs/planning/`](docs/planning/) — planning, estimates, risks, and project tracking
* [`docs/quality/`](docs/quality/) — quality evidence
* [`docs/release/`](docs/release/) — release readiness and release notes
* [`docs/requirements/`](docs/requirements/) — requirements, acceptance criteria, assumptions, and open questions
* [`docs/reviews/`](docs/reviews/) — engineering review evidence
* [`docs/security/`](docs/security/) — security and governance evidence
* [`docs/team/`](docs/team/) — team roles and working practices
* [`docs/testing/`](docs/testing/) — testing plans and evidence

Detailed evidence should remain in its authoritative artifact rather than being duplicated in this README.

## Repository Structure

| Location         | Purpose                                      |
| ---------------- | -------------------------------------------- |
| `src/`           | Production application code                  |
| `tests/`         | Automated tests                              |
| `test-evidence/` | Preserved testing and verification evidence  |
| `data/`          | Synthetic sample, fixture, or reference data |
| `scripts/`       | Project utilities and scripts                |
| `docs/`          | Engineering documentation and evidence       |
| `.github/`       | GitHub templates, workflows, and automation  |

## Build, Run, and Test

Run commands from the repository root with Python 3.10+ and standard-library SQLite. Local A6 verification used Python 3.12.14. The GitHub Actions workflow targets Python 3.14.

```bash
git clone https://github.com/bgallagher12/comp330-f26-team-03.git
cd comp330-f26-team-03
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m src.main
```

On Windows activate with `.venv\Scripts\activate`. The app stores synthetic requests in `data/campusconnect.db`. At the sign-in prompt, a first-time student types `/register`, then enters an email, student ID, and password. Tony uses `tonytiger@example.com` and `00123` for the demo. He signs in with his email and password, and the app uses the linked ID automatically. Choose **My Requests** to select a ticket by its menu number. A resolved request shows **[Update available]** until you open it and the response is displayed. SQLite remembers when it was opened. Both terminals use the same database. In the reviewer terminal, create the demo instructor account once, then sign in to the existing review queue. `scripts/campus.html` is the earlier browser prototype.

```bash
python -m src.main --add-reviewer demo-instructor
python -m src.main --reviewer
```

The trusted operator handles reviewer accounts and links student accounts to IDs that already have requests. The database stores a salted password hash. Signed-in reviewers share the queue, and this checkout is for supervised synthetic-data demos. See the [runbook](docs/operations/runbook.md) for setup and recovery.

```bash
python -m compileall -q src tests
python -m pytest -q
```

See the [demo walkthrough](docs/release/demo-script.md), [testing evidence](docs/testing/final-test-evidence.md), and [known limitations](docs/release/known-limitations.md).

## Engineering Workflow

Team 03 uses the following development workflow:

**Issue → Branch → Implementation → Pull Request → Review → Merge**

GitHub Issues are used to track:

* bugs;
* development tasks;
* blockers; and
* other engineering work that should remain visible and traceable.

Meaningful work should normally occur on a separate branch and be merged through a pull request.

Detailed workflow expectations are maintained in:

[`docs/team/working-agreements.md`](docs/team/working-agreements.md)

## Engineering Practices

The team will use engineering practices appropriate to the current project stage, including:

* requirements and acceptance-criteria traceability;
* GitHub Issues, branches, pull requests, and reviews;
* peer review of significant work;
* documentation of important engineering decisions;
* testing and verification tied to requirements;
* visible defect and blocker tracking;
* responsible security and data handling;
* human verification of AI-assisted work; and
* release evidence that reflects the actual state of the project.

Engineering evidence will be created and updated as the corresponding work becomes real.

## Engineering Evidence Model

Campus Connect aims to maintain meaningful traceability between engineering artifacts.

A typical path may be:

**Requirement → Acceptance Criterion → Architecture / Decision → Implementation → Test / Review → Verification Evidence**

The purpose of this traceability is to make important engineering claims reviewable and defensible rather than to create unnecessary documentation.

## AI-Assisted Engineering

Team 03 uses AI as an engineering **copilot**.

AI may assist with:

* requirements and planning;
* technical analysis;
* implementation;
* debugging;
* testing;
* review;
* documentation; and
* engineering decision support.

Human team members remain responsible for understanding, reviewing, verifying, and being able to explain all AI-assisted work accepted into the project.

Team AI practices are documented in:

* [`docs/ai/ai-policy.md`](docs/ai/ai-policy.md)
* [`docs/ai/ai-use-log.md`](docs/ai/ai-use-log.md)

## Team Operations

The team uses **Microsoft Teams** for normal project communication.

Regular team meetings are held:

**Wednesdays at 1:00 PM**

GitHub Issues are used for project work that should remain visible and traceable, including bugs, tasks, and blockers.

Additional team practices are documented under:

[`docs/team/`](docs/team/)

## Engineering Operating Model

For this project:

* **Sakai** defines course requirements, deadlines, submission instructions, and required evidence.
* **GitHub** serves as the authoritative engineering record for Team 03.
* **ETIS** provides professional engineering guidance, templates, and reference material where useful.

The team will use these resources to support the project without creating unnecessary artifacts that do not reflect actual engineering work.

## Professional Engineering Expectations

The repository should allow another engineer or reviewer to understand:

* what Campus Connect is intended to accomplish;
* who owns important project responsibilities;
* what requirements the system must satisfy;
* what assumptions and uncertainties remain;
* why significant engineering decisions were made;
* how implementation relates to requirements;
* how work was reviewed and tested;
* what defects or limitations remain;
* how AI affected engineering work; and
* what evidence supports project and release claims.

The goal is not only to produce a working system, but to produce one that is understandable, reviewable, testable, maintainable, and traceable.

## Course Context

Campus Connect is being developed for **COMP 330 — Software Engineering** at Loyola University Chicago during Fall 2026.

Team 03 began with the official COMP 330 repository starter kit and is progressively replacing the starter scaffold with project-specific engineering evidence as the work develops.

Sakai remains authoritative for course requirements and submission expectations.

