CREATE TABLE IF NOT EXISTS requests (
    request_id INTEGER PRIMARY KEY,
    student_id TEXT NOT NULL,
    student_name TEXT NOT NULL,
    student_email TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL
        CHECK (category IN ('Technology', 'Tutoring', 'Facilities', 'Other')),
    status TEXT NOT NULL DEFAULT 'submitted'
        CHECK (status IN ('submitted', 'resolved')),
    created_at TEXT NOT NULL
        DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    resolution TEXT DEFAULT NULL,

    CHECK (
        (status = 'submitted' AND resolution IS NULL)
        OR
        (status = 'resolved'
            AND resolution IS NOT NULL
            AND length(trim(resolution)) > 0)
    )
);