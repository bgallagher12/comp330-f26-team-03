# Permission boundaries

| Action | Signed-in demo student | Signed-in demo reviewer | Trusted host operator |
|---|---|---|---|
| Create accounts | Self-register with an unused email and an unused ID without requests | Separate operator command for reviewers | Can provision reviewer accounts and link students to existing requests |
| Submit a request | Saved under the session's student ID | Use a student session | Can operate either workflow |
| List requests and read a response | Own requests only, through My Requests | Can inspect a known request through the reviewer workflow | Direct local storage access |
| Mark a response opened | Own resolved request after the response is displayed | Reviewer workflow leaves the student's seen state untouched | Direct local storage access |
| List the pending queue | Denied by student menu dispatch | Shared queue | Direct local storage access |
| Resolve a request | Denied by student menu dispatch | Submitted requests only | Can operate the reviewer workflow |

Self-registration cannot attach an account to an ID with older requests. The trusted operator links eligible students to those requests. The CLI obtains the linked ID after verifying the email and password and uses it for new submissions, list and detail reads, and seen writes. The SQL for detail and seen writes matches both the student ID and request ID. The seen timestamp records when the terminal displayed the response.

The host operator can run provisioning commands, call internal Python code, and open SQLite directly. Staff share a queue. University identity verification, account lifecycle controls, per-instructor assignment, and durable attribution remain open. See the [security review](security-governance-checklist.md).
