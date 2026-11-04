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
        with connection:
            yield connection
    finally:
        connection.close()


def init_db():
    with connect() as connection:
        connection.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))


def submit_request(details):
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


def get_request_status(request_id):
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


def get_request_for_review(request_id):
    return get_request_status(request_id)


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