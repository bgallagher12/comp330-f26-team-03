# Working Agreements

This document defines the practices Team 03 will follow while developing, reviewing, integrating, and verifying Campus Connect.

## Communication Practices

* **Microsoft Teams** is the primary communication channel.
* Team members should acknowledge project messages within a reasonable amount of time.
* Blockers that affect other team members should be communicated as soon as possible.
* Important engineering decisions should be documented in GitHub rather than existing only in private messages.
* The team meets every **Wednesday at 1:00 PM** for regular coordination.

## Work Planning and Ownership

* GitHub Issues will be used to track bugs, tasks, blockers, and other engineering work.
* Issues should clearly describe the work that needs to be completed.
* Team members should make ownership visible by assigning or claiming issues they are working on.
* If a team member becomes blocked, they should communicate the blocker instead of allowing the task to remain inactive without explanation.
* Specialized role ownership is documented in `docs/team/roles.md`, but all members may contribute across project areas.

## Git and Branching

* The `main` branch represents the current shared project state.
* Development work should normally occur on a separate branch.
* Branches should be created for features, fixes, documentation changes, or other meaningful work.
* Direct commits to `main` should be avoided for significant changes.
* Branches should be kept reasonably current with `main` when necessary to avoid integration conflicts.

Example branch names:

```text
feature/event-search
fix/login-validation
docs/update-readme
```

## Commits

Commits should:

* represent a meaningful unit of work;
* use a clear message describing what changed;
* avoid combining unrelated changes when possible; and
* not include passwords, tokens, credentials, or other sensitive information.

Example:

```text
Add validation for event creation form
```

## Pull Requests and Review

A pull request should be used before significant work is merged into `main`.

Pull requests should:

* explain what was changed;
* reference the related issue when applicable;
* be understandable by another team member;
* include relevant testing or verification information; and
* be reviewed by another team member before merge when appropriate.

Reviewers should check correctness, maintainability, requirements, testing, and any important effects on related project work.

## Testing and Verification

Before work is considered complete, the responsible team member should perform verification appropriate to the change.

Verification may include:

* automated tests;
* manual testing;
* code review;
* checking expected application behavior;
* comparison against requirements; or
* reviewing documentation for accuracy.

Higher-impact changes should receive stronger testing and review.

## Definition of Done

Work is considered done when:

* the intended change has been completed;
* relevant requirements or acceptance criteria are satisfied;
* appropriate testing or verification has been performed;
* significant defects are resolved or documented;
* related documentation is updated when necessary;
* the change has been reviewed when appropriate; and
* the completed work is integrated into the shared repository.

## Documentation and Traceability

Engineering evidence should be updated as the work occurs rather than reconstructed later.

When appropriate, the team should maintain traceability between:

```text
Issue → Requirement → Implementation → Pull Request → Review/Test
```

Important requirements, decisions, AI use, tests, bugs, and engineering evidence should remain visible in their appropriate repository locations.

## AI-Assisted Work

Team 03 uses AI as an engineering **copilot**.

Before accepting AI-assisted code, tests, documentation, or recommendations, the responsible team member must:

* understand the output;
* review it for correctness;
* modify or reject incorrect suggestions;
* verify important behavior;
* follow normal review practices; and
* be able to explain the final work.

Meaningful AI-assisted work should be recorded in:

`docs/ai/ai-use-log.md`

Detailed expectations are defined in:

`docs/ai/ai-policy.md`

## Handling Defects and Broken Builds

* Bugs should be recorded using GitHub Issues when they require project tracking.
* Important defects should include enough information for another team member to understand or reproduce the problem.
* If a change breaks `main`, restoring a working state becomes a priority.
* The team should identify the cause, correct the problem, and verify the fix before continuing dependent work.
* Significant defects and fixes should remain traceable through issues, commits, pull requests, or testing evidence.

## Working Agreement Changes

These agreements may be changed when the team's experience shows that a different practice would work better.

Significant changes should be discussed by the team and documented rather than silently changing how the team operates.

The team may review these agreements during designated meeting times.

