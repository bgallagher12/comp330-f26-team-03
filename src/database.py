import sqlite3
from contextlib import contextmanager
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "campusconnect.db"
SCHEMA_PATH = Path(__file__).with_name("schema.sql")

REQUIRED_FIELDS = (
    "student_id",
    "student_name",
    "student_email",
    "title",
    "description",
    "category",
)

VALID_CATEGORIES = {"Technology", "Tutoring", "Facilities", "Other"}


@contextmanager
def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    try:
        connection.execute("PRAGMA foreign_keys = ON")
        with connection:
            yield connection
    finally:
        connection.close()


def init_db():
    with connect() as connection:
        connection.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        # Serialize the column check and ALTER when two terminals start together.
        connection.execute("BEGIN IMMEDIATE")
        columns = connection.execute("PRAGMA table_info(requests)")
        if not any(column["name"] == "response_seen_at" for column in columns):
            connection.execute("ALTER TABLE requests ADD COLUMN response_seen_at TEXT")


def submit_request(details):
    if not isinstance(details,dict):
        raise ValueError("Request should be a dictionary")
    record = {}

    for field in REQUIRED_FIELDS:
        value = details.get(field)

        if value is None or not str(value).strip():
            raise ValueError(f"{field} is required.")

        record[field] = str(value).strip()

    if record["category"] not in VALID_CATEGORIES:
        raise ValueError("Choose a valid category.")

    with connect() as connection:
        cursor = connection.execute(
            """
            INSERT INTO requests (
                student_id, student_name, student_email,
                title, description, category
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            tuple(record[field] for field in REQUIRED_FIELDS),
        )

        row = connection.execute(
            "SELECT * FROM requests WHERE request_id = ?",
            (cursor.lastrowid,),
        ).fetchone()

        return dict(row)


def list_student_requests(student_id):
    with connect() as connection:
        rows = connection.execute(
            """
            SELECT request_id, title, status, response_seen_at
            FROM requests WHERE student_id = ?
            ORDER BY request_id
            """,
            (student_id,),
        ).fetchall()
        return [dict(row) for row in rows]


def get_student_request(student_id, request_id):
    with connect() as connection:
        row = connection.execute(
            """
            SELECT request_id, title, status, resolution
            FROM requests WHERE student_id = ? AND request_id = ?
            """,
            (student_id, request_id),
        ).fetchone()

    if row is None:
        raise ValueError("Request not found in My Requests.")
    return dict(row)


def mark_response_seen(student_id, request_id):
    with connect() as connection:
        connection.execute(
            """
            UPDATE requests
            SET response_seen_at = strftime('%Y-%m-%dT%H:%M:%fZ', 'now')
            WHERE student_id = ? AND request_id = ?
                AND status = 'resolved' AND response_seen_at IS NULL
            """,
            (student_id, request_id),
        )


def get_request_for_review(request_id):
    with connect() as connection:
        row = connection.execute(
            "SELECT * FROM requests WHERE request_id = ?",
            (request_id,),
        ).fetchone()

        if row is None:
            raise ValueError("Request not found.")

        return dict(row)


def list_pending_requests():
    with connect() as connection:
        rows = connection.execute(
            """
            SELECT * FROM requests
            WHERE status = 'submitted'
            ORDER BY request_id
            """
        ).fetchall()

        return [dict(row) for row in rows]


def resolve_request(request_id, resolution):
    if not isinstance(resolution, str) or not resolution.strip():
        raise ValueError("A resolution is required.")

    with connect() as connection:
        cursor = connection.execute(
            """
            UPDATE requests
            SET resolution = ?, status = 'resolved'
            WHERE request_id = ? AND status = 'submitted'
            """,
            (resolution.strip(), request_id),
        )

        row = connection.execute(
            "SELECT * FROM requests WHERE request_id = ?",
            (request_id,),
        ).fetchone()

        if row is None:
            raise ValueError("Request not found.")

        if cursor.rowcount == 0:
            raise ValueError("Request is already resolved.")

        return dict(row)


def add_reviewer_account(username, salt, password_hash):
    with connect() as connection:
        cursor = connection.execute(
            """
            INSERT INTO reviewer_accounts (username, password_salt, password_hash)
            VALUES (?, ?, ?)
            ON CONFLICT(username) DO NOTHING
            """,
            (username, salt, password_hash),
        )
        if cursor.rowcount == 0:
            raise ValueError("That reviewer username already exists.")


def get_reviewer_credentials(username):
    with connect() as connection:
        return connection.execute(
            "SELECT password_salt, password_hash FROM reviewer_accounts WHERE username = ?",
            (username,),
        ).fetchone()



def add_student_account(student_id, email, salt, password_hash, *, allow_existing_requests):
    with connect() as connection:
        # The eligibility check and insert share one SQLite write statement.
        cursor = connection.execute(
            """
            INSERT INTO student_accounts (student_id, username, password_salt, password_hash)
            SELECT ?, ?, ?, ?
            WHERE ? OR NOT EXISTS (SELECT 1 FROM requests WHERE student_id = ?)
            ON CONFLICT DO NOTHING
            """,
            (student_id, email, salt, password_hash, allow_existing_requests, student_id),
        )
        if cursor.rowcount == 0:
            raise ValueError(
                "That email or student ID is unavailable. "
                "Ask the demo operator for help with an existing account or requests."
            )


def get_student_account(username):
    with connect() as connection:
        return connection.execute(
            """
            SELECT student_id, password_salt, password_hash
            FROM student_accounts WHERE username = ?
            """,
            (username,),
        ).fetchone()
