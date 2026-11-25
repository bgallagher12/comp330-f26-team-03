"""Release regressions through the CLI using synthetic, disposable data."""

import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

from src import database, reviewer_service, student_service
from src.credentials import hash_new_password

ROOT = Path(__file__).resolve().parents[1]
USERNAME = "demo-instructor"
PASSWORD = "synthetic-test-reviewer-password"
RESOLUTION = "Office hours Monday 4-6 in Dumbach 111."
STUDENT_ID = "00123"
STUDENT_EMAIL = "tonytiger@example.com"
STUDENT_PASSWORD = "synthetic-test-student-password"
OTHER_ID = "00987"
OTHER_EMAIL = "other@example.com"
OTHER_PASSWORD = "synthetic-test-other-password"


@pytest.fixture
def workspace(tmp_path):
    shutil.copytree(ROOT / "src", tmp_path / "src", ignore=shutil.ignore_patterns("__pycache__"))
    return tmp_path


def run_cli(workspace, inputs, *args, hidden_input=True):
    # Replace only terminal secret entry. Menu, SQL and role checks run normally.
    command = [sys.executable, "-m", "src.main"]
    if hidden_input:
        command = [
            sys.executable, "-c",
            "import getpass, sys; getpass.getpass = lambda _: input(); "
            "from src.main import main; sys.exit(main())",
        ]
    return subprocess.run(
        [*command, *args], cwd=workspace, input="\n".join(inputs) + "\n",
        text=True, capture_output=True, timeout=15, start_new_session=True,
    )


def provision_reviewer(workspace):
    result = run_cli(workspace, [PASSWORD, PASSWORD], "--add-reviewer", USERNAME)
    assert result.returncode == 0
    assert "Reviewer account created." in result.stdout
    assert PASSWORD not in result.stdout + result.stderr


def provision_student(
    workspace, email=STUDENT_EMAIL, student_id=STUDENT_ID, password=STUDENT_PASSWORD,
):
    result = run_cli(workspace, [password, password], "--add-student", email, student_id)
    assert result.returncode == 0
    assert "Student account created." in result.stdout
    assert password not in result.stdout + result.stderr


def registration(email, student_id, password):
    return ["/register", email, student_id, password, password]


def submit(title, name="Tony Tiger", category="2"):
    return ["1", name, "synthetic@example.com", title, "Synthetic notes", category]


def test_my_requests_lists_owned_requests_and_clears_only_opened_response(workspace, monkeypatch):
    provision_student(workspace, OTHER_EMAIL, OTHER_ID, OTHER_PASSWORD)
    submitted = run_cli(workspace, [
        *registration(STUDENT_EMAIL.upper(), STUDENT_ID, STUDENT_PASSWORD),
        STUDENT_EMAIL, STUDENT_PASSWORD, "4", "5", "2",
        *submit("Calculus I help"), *submit("Projector issue", category="1"),
        "2", "2", "3",
    ])
    assert submitted.returncode == 0
    assert "Student account created. Sign in with your email and password." in submitted.stdout
    assert submitted.stdout.count("Choose an option from this menu.") == 2
    assert submitted.stdout.count("Request Submitted") == 2
    assert "You have no requests yet." in submitted.stdout
    assert "Status: Submitted" in submitted.stdout
    assert "receipt" not in submitted.stdout.lower()
    assert STUDENT_PASSWORD not in submitted.stdout + submitted.stderr

    other = run_cli(workspace, [
        OTHER_EMAIL, OTHER_PASSWORD, *submit("Private other title", name="Other Student"),
        "3",
    ])
    assert other.returncode == 0

    provision_reviewer(workspace)
    reviewer = run_cli(workspace, [USERNAME, PASSWORD, "3", "4", "1", RESOLUTION,
                                    "4", "3", "Other student's response.", "5"], "--reviewer")
    assert reviewer.returncode == 0
    assert "Pending Request" in reviewer.stdout
    assert reviewer.stdout.count("Request is resolved") == 2
    assert reviewer.stderr.count("request_resolved") == 2
    assert PASSWORD not in reviewer.stdout + reviewer.stderr

    badge = "Calculus I help    Resolved [Update available]"
    student = run_cli(workspace, [
        STUDENT_EMAIL, STUDENT_PASSWORD, "2", "3", "2", "", "3",
    ])
    assert student.returncode == 0
    assert student.stdout.count(badge) == 2
    assert "Projector issue    Submitted" in student.stdout
    assert "Choose a request number from this list." in student.stdout
    assert RESOLUTION not in student.stdout
    assert "student_response_opened" not in student.stderr
    for private_value in ("Private other title", "Other student's response.", "Other Student",
                          "Synthetic notes", "synthetic@example.com"):
        assert private_value not in student.stdout + student.stderr

    student = run_cli(workspace, [STUDENT_EMAIL, STUDENT_PASSWORD, "2", "1", "2", "", "3"])
    assert student.returncode == 0
    assert student.stdout.count(badge) == 1
    assert student.stdout.count("Calculus I help    Resolved\n") == 1
    assert f"Professor's response: {RESOLUTION}" in student.stdout
    assert "student_response_opened" in student.stderr
    assert RESOLUTION not in student.stderr

    restarted = run_cli(workspace, [STUDENT_EMAIL, STUDENT_PASSWORD, "2", "", "3"])
    assert restarted.returncode == 0
    assert "Calculus I help    Resolved" in restarted.stdout
    assert "[Update available]" not in restarted.stdout

    monkeypatch.setattr(database, "DB_PATH", workspace / "data" / "campusconnect.db")
    own_resolved, own_pending = student_service.list_requests(STUDENT_ID)
    assert own_resolved["response_seen_at"]
    assert own_pending["response_seen_at"] is None
    assert student_service.list_requests(OTHER_ID)[0]["response_seen_at"] is None


@pytest.mark.parametrize(("username", "password"), [
    (STUDENT_ID, STUDENT_PASSWORD),
    (STUDENT_EMAIL, OTHER_PASSWORD),
], ids=["student-id-alone", "wrong-password"])
def test_student_sign_in_fails_closed(workspace, username, password):
    provision_student(workspace)
    result = run_cli(workspace, [username, password])
    assert result.returncode == 1
    assert "Invalid student email or password." in result.stdout
    assert "student_sign_in_denied" in result.stderr
    assert "My Requests" not in result.stdout
    assert password not in result.stdout + result.stderr


@pytest.mark.parametrize(("email", "student_id"), [
    (STUDENT_EMAIL.upper(), OTHER_ID),
    (OTHER_EMAIL, STUDENT_ID),
], ids=["duplicate-email", "duplicate-student-id"])
def test_student_registration_rejects_duplicate_without_changing_password(
    workspace, email, student_id,
):
    provision_student(workspace)
    duplicate = run_cli(workspace, registration(email, student_id, OTHER_PASSWORD))
    assert duplicate.returncode == 1
    assert "That email or student ID is unavailable." in duplicate.stdout
    result = run_cli(workspace, [STUDENT_EMAIL, STUDENT_PASSWORD, "3"])
    assert result.returncode == 0


@pytest.mark.parametrize(("email", "student_id", "confirmation", "message"), [
    ("invalid-email", STUDENT_ID, STUDENT_PASSWORD, "Enter a valid email address."),
    (STUDENT_EMAIL, "", STUDENT_PASSWORD, "Student ID is required."),
    (STUDENT_EMAIL, STUDENT_ID, OTHER_PASSWORD, "Passwords do not match."),
], ids=["invalid-email", "blank-id", "password-mismatch"])
def test_student_registration_rejects_invalid_input(
    workspace, email, student_id, confirmation, message,
):
    result = run_cli(workspace, ["/register", email, student_id, STUDENT_PASSWORD, confirmation])
    assert result.returncode == 1
    assert message in result.stdout
    provision_student(workspace)


def test_prior_username_account_can_still_sign_in(workspace, monkeypatch):
    monkeypatch.setattr(database, "DB_PATH", workspace / "data" / "campusconnect.db")
    database.init_db()
    with database.connect() as connection:
        connection.execute(
            "INSERT INTO student_accounts VALUES (?, ?, ?, ?)",
            (STUDENT_ID, "tony.tiger", *hash_new_password(STUDENT_PASSWORD)),
        )
    result = run_cli(workspace, ["tony.tiger", STUDENT_PASSWORD, "2", "3"])
    assert result.returncode == 0
    assert "You have no requests yet." in result.stdout


@pytest.mark.parametrize(("username", "password"), [
    ("unknown-instructor", PASSWORD),
    (USERNAME, "wrong-reviewer-password"),
], ids=["unknown-user", "wrong-password"])
def test_reviewer_sign_in_fails_closed(workspace, username, password):
    provision_reviewer(workspace)
    result = run_cli(workspace, [username, password], "--reviewer")
    assert result.returncode == 1
    assert "Invalid reviewer username or password." in result.stdout
    assert "reviewer_sign_in_denied" in result.stderr
    assert "Review Pending Requests" not in result.stdout
    assert password not in result.stdout + result.stderr


def test_noninteractive_password_input_does_not_fall_back_to_echo(workspace):
    result = run_cli(workspace, [USERNAME, PASSWORD], "--reviewer", hidden_input=False)
    assert result.returncode == 1
    assert "terminal_session_ended" in result.stderr
    assert PASSWORD not in result.stdout + result.stderr


def test_reviewer_provisioning_rejects_mismatch_and_duplicate(workspace):
    mismatch = run_cli(workspace, [PASSWORD, "different"], "--add-reviewer", USERNAME)
    assert mismatch.returncode == 1
    assert "Passwords do not match." in mismatch.stdout

    provision_reviewer(workspace)
    duplicate = run_cli(workspace, [PASSWORD, PASSWORD], "--add-reviewer", USERNAME.upper())
    assert duplicate.returncode == 1
    assert "already exists" in duplicate.stdout

    provisioned = run_cli(workspace, [USERNAME.upper(), PASSWORD, "5"], "--reviewer")
    assert provisioned.returncode == 0
    assert "Review Pending Requests" in provisioned.stdout


def test_invalid_request_data_and_oversized_reviewer_id(workspace):
    provision_student(workspace)
    student = run_cli(workspace, [
        STUDENT_EMAIL, STUDENT_PASSWORD, "1", "Tony Tiger", "synthetic@example.com",
        "Test", "", "2", "3",
    ])
    assert student.returncode == 0
    assert "description is required" in student.stdout

    provision_reviewer(workspace)
    reviewer = run_cli(workspace, [USERNAME, PASSWORD, "4", str(2**63), "4", "abc", "3", "5"],
                       "--reviewer")
    assert reviewer.returncode == 0
    assert reviewer.stdout.count("Request ID must be a positive SQLite integer.") == 2
    assert "There are no pending requests" in reviewer.stdout


def test_storage_error_exits_without_a_traceback(workspace):
    (workspace / "data").mkdir()
    (workspace / "data" / "campusconnect.db").write_text("Synthetic invalid database")
    result = run_cli(workspace, ["5"])
    assert result.returncode == 1
    assert "storage_failure error_type=DatabaseError" in result.stderr
    assert "Traceback" not in result.stderr


@pytest.mark.parametrize("has_receipt_table", [False, True], ids=["a5", "receipt-preview"])
def test_existing_database_preserves_requests_and_reviewer_accounts(
    workspace, monkeypatch, has_receipt_table,
):
    path = workspace / "data" / "campusconnect.db"
    path.parent.mkdir()
    old_schema = (ROOT / "src" / "schema.sql").read_text().split(
        "CREATE INDEX IF NOT EXISTS requests_by_student"
    )[0].replace("    response_seen_at TEXT DEFAULT NULL,\n", "")
    with sqlite3.connect(path) as connection:
        connection.executescript(old_schema)
        connection.execute(
            "INSERT INTO requests (student_id, student_name, student_email, title,"
            " description, category, status, resolution)"
            " VALUES ('00123', 'Tony Tiger', 'test@example.com', 'Legacy', 'Synthetic',"
            " 'Tutoring', 'resolved', ?)",
            (RESOLUTION,),
        )
        if has_receipt_table:
            connection.execute(
                "CREATE TABLE request_receipts (receipt_digest TEXT PRIMARY KEY NOT NULL,"
                " request_id INTEGER NOT NULL UNIQUE REFERENCES requests(request_id))"
            )
            connection.execute("INSERT INTO request_receipts VALUES ('old-digest', 1)")
            connection.execute(
                "CREATE TABLE reviewer_accounts (username TEXT PRIMARY KEY NOT NULL,"
                " password_salt BLOB NOT NULL, password_hash BLOB NOT NULL)"
            )
    monkeypatch.setattr(database, "DB_PATH", path)
    if has_receipt_table:
        reviewer_service.create_account(USERNAME, PASSWORD)
    database.init_db()
    database.init_db()

    legacy = database.get_request_for_review(1)
    assert legacy["title"] == "Legacy"
    assert legacy["resolution"] == RESOLUTION
    assert legacy["response_seen_at"] is None
    if has_receipt_table:
        reviewer = run_cli(workspace, [USERNAME, PASSWORD, "5"], "--reviewer")
        assert reviewer.returncode == 0
        assert "Review Pending Requests" in reviewer.stdout

    claim = run_cli(workspace, registration(OTHER_EMAIL, STUDENT_ID, OTHER_PASSWORD))
    assert claim.returncode == 1
    assert "That email or student ID is unavailable." in claim.stdout
    assert RESOLUTION not in claim.stdout + claim.stderr

    provision_student(workspace)
    student = run_cli(workspace, [
        STUDENT_EMAIL, STUDENT_PASSWORD, "2", "1", *submit("New request"), "3",
    ])
    assert student.returncode == 0
    assert "Legacy    Resolved [Update available]" in student.stdout
    assert RESOLUTION in student.stdout
    assert database.get_request_for_review(1)["response_seen_at"]
    assert database.get_request_for_review(2)["title"] == "New request"
    with database.connect() as connection:
        tables = {row["name"] for row in connection.execute("SELECT name FROM sqlite_master")}
        assert ("request_receipts" in tables) == has_receipt_table
        if has_receipt_table:
            assert connection.execute("SELECT count(*) FROM request_receipts").fetchone()[0] == 1
