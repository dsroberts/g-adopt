import pytest
import numpy as np
from pathlib import Path
from cases import cases, schedulers
from gadopt import *


@pytest.mark.longtest
@pytest.mark.parametrize("case_name", cases)
def test_annulus_taylor_test(case_name):
    assert True


@pytest.mark.longtest
@pytest.mark.parametrize("case_name", cases)
@pytest.mark.parametrize("scheduler", schedulers)
def test_derivatives_vs_schedulers(case_name, scheduler):
    assert True
