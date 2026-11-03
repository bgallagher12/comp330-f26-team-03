
import importlib
import sys
from pathlib import Path

import pytest

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

import mock_backend
import review_service


@pytest.fixture(autouse=True)
def reset_mock_backend():
    """Reset sample data before each test."""
    importlib.reload(mock_backend)


def test_list_submitted_requests():
    requests = review_service.list_submitted_requests()

    assert isinstance(requests, list)
    assert all(request["status"] == "submitted" for request in requests)


def test_get_existing_request():
    request = review_service.get_request(1)

    assert request["request_id"] == 1
    assert request["status"] == "submitted"


def test_get_nonexistent_request():
    with pytest.raises(ValueError, match="Request not found"):
        review_service.get_request(999)


def test_save_resolution():
    request = review_service.save_resolution(
        1, "Projector connection was repaired."
    )

    assert request["status"] == "resolved"
    assert request["resolution"] == "Projector connection was repaired."


def test_reject_blank_resolution():
    with pytest.raises(ValueError, match="resolution is required"):
        review_service.save_resolution(1, " ")


def test_prevent_second_resolution():
    review_service.save_resolution(1, "Projector was repaired.")

    with pytest.raises(ValueError, match="already resolved"):
        review_service.save_resolution(1, "Second resolution.")

