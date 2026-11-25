# A6 data handling

- Use synthetic student identities, example.com addresses, and invented request and response text.
- SQLite stores request fields, responses, and the first response-open timestamp on the operator's machine. Older preview databases may retain an unused receipt table.
- Students enter synthetic email addresses and student IDs during registration. The operator provisions reviewer accounts and handles student IDs that already have requests. SQLite stores a separate salt and a PBKDF2-HMAC-SHA-256 password hash for each account. Passwords use hidden prompts. Keep them out of the repository, shell history, AI prompts, and recordings.
- Keep the database and copies private to the operator. Git ignores the standard database and sidecar paths. Review the staged diff before committing evidence.
- Dispose of synthetic databases and diagnostic copies when they are no longer needed. Live operation would require approved retention and access controls.

[Runbook and restore guidance](../operations/runbook.md) · [Review and residual risks](security-governance-checklist.md)
