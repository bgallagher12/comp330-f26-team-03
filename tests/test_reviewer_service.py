import pytest

from src import database, reviewer_service
from src.student_service import submit_request


@pytest.fixture
def submitted_request(tmp_path, monkeypatch):
    monkeypatch.setattr(database, "DB_PATH", tmp_path / "requests.db")
    database.init_db()

    return submit_request({
        "student_id": "001",
        "student_name": "Test Student",
        "student_email": "test@example.com",
        "title": "Projector problem",
        "description": "The classroom projector will not turn on.",
        "category": "Technology",
    })


def test_list_submitted_requests(submitted_request):
    requests = reviewer_service.list_submitted_requests()

    assert requests == [submitted_request]


def test_get_existing_request(submitted_request):
    request = reviewer_service.get_request(
        submitted_request["request_id"]
    )

    assert request == submitted_request


def test_get_nonexistent_request(submitted_request):
    unknown_id = submitted_request["request_id"] + 1

    with pytest.raises(ValueError, match="Request not found"):
        reviewer_service.get_request(unknown_id)


def test_save_resolution(submitted_request):
    request = reviewer_service.save_resolution(
        submitted_request["request_id"],
        "Projector connection was repaired.",
    )

    assert request["status"] == "resolved"
    assert request["resolution"] == "Projector connection was repaired."
    assert reviewer_service.list_submitted_requests() == []


def test_reject_blank_resolution(submitted_request):
    with pytest.raises(ValueError, match="resolution is required"):
        reviewer_service.save_resolution(
            submitted_request["request_id"], " "
        )

    assert reviewer_service.get_request(
        submitted_request["request_id"]
    ) == submitted_request


def test_prevent_second_resolution(submitted_request):
    request_id = submitted_request["request_id"]
    reviewer_service.save_resolution(request_id, "Projector was repaired.")

    with pytest.raises(ValueError, match="already resolved"):
        reviewer_service.save_resolution(request_id, "Second resolution.")

    assert reviewer_service.get_request(
        request_id
    )["resolution"] == "Projector was repaired."
