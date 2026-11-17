"""Repeat the A5 CLI demonstration using disposable storage, never user data."""

import hashlib
import json
from pathlib import Path
import platform
import shutil
import sqlite3
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
RESOLUTION = "Office hours Monday 4-6 or Wednesday 12-3 at Dumbach 111."
SUBMISSION = ["1", "Tony Tiger", "00123", "tonytiger@example.com",
              "Calculus I help", "Please help me understand a concept before Friday.", "2"]
SCENARIOS = {
    "workflow": [SUBMISSION + ["3", "4", "1", RESOLUTION, "2", "1", "5"],
                 ["2", "1", "3", "5"]],
    "invalid-id": [["2", "99999", "2", "abc", "5"]],
    "validation": [["1", "Tony Tiger", "00123", "tonytiger@example.com",
                    "Calculus I help", "", "2", "3", "5"]],
}


def verify_scenario(name):
    """Run real entry point in fresh processes with an empty temporary database."""
    transcripts = []
    with tempfile.TemporaryDirectory(prefix="campusconnect-a5-") as temporary:
        workspace = Path(temporary)
        shutil.copytree(ROOT / "src", workspace / "src", ignore=shutil.ignore_patterns("__pycache__"))
        for inputs in SCENARIOS[name]:
            result = subprocess.run(
                [sys.executable, "-m", "src.main"], cwd=workspace,
                input="\n".join(inputs) + "\n", text=True, capture_output=True, timeout=15,
            )
            assert result.returncode == 0, result.stderr
            assert not result.stderr, result.stderr
            transcripts.append({"inputs": inputs, "stdout": result.stdout, "exit_code": result.returncode})
        with sqlite3.connect(workspace / "data" / "campusconnect.db") as connection:
            rows = connection.execute("SELECT request_id, student_id, status, resolution FROM requests").fetchall()
        if name == "workflow":
            assert rows == [(1, "00123", "resolved", RESOLUTION)], rows
            assert "Pending Request" in transcripts[0]["stdout"]
            assert "Request is resolved" in transcripts[0]["stdout"]
            assert "Status: resolved" in transcripts[1]["stdout"]
            assert RESOLUTION in transcripts[1]["stdout"]
            assert "There are no pending requests" in transcripts[1]["stdout"]
        elif name == "invalid-id":
            assert rows == [], rows
            assert "Request not found." in transcripts[0]["stdout"]
            assert "Request ID must be a whole number" in transcripts[0]["stdout"]
        elif name == "validation":
            assert rows == [], rows
            assert "description is required." in transcripts[0]["stdout"]
            assert "There are no pending requests" in transcripts[0]["stdout"]
        assert all("You are Exiting the App" in item["stdout"] for item in transcripts)
    return {"scenario": name, "result": "PASS", "sessions": transcripts, "final_rows": rows}


def main():
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    hashes = {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
              for path in sorted((ROOT / "src").glob("*")) if path.is_file()}
    report = {"tested_commit": revision, "python": platform.python_version(),
              "initial_state": "Empty temporary database per scenario; workflow session 2 reuses session 1 database",
              "source_sha256": hashes,
              "results": [verify_scenario(name) for name in SCENARIOS]}
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
