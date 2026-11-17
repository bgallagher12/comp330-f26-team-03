"""A5 repeatable versions of the previously manual CLI checks (issue #29)."""

import pytest

from scripts.verify_a5 import SCENARIOS, verify_scenario


@pytest.mark.parametrize("scenario", SCENARIOS)
def test_cli_release_scenario(scenario):
    assert verify_scenario(scenario)["result"] == "PASS"
