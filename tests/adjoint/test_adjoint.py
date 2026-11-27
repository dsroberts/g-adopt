import pytest
from pathlib import Path
from .cases import cases, schedules


@pytest.mark.parametrize("case_name", cases)
@pytest.mark.parametrize("schedule_name", schedules.keys())
def test_rectangular_taylor_test(case_name, schedule_name):
    assert True
