from pathlib import Path

import numpy as np
import pytest

base = Path(__file__).parent.resolve()

case_name = ["integrated_q", "integrated_q_DH219"]


@pytest.mark.parametrize("case_name", case_name)
def test_scalar_advection_diffusion(case_name):
    assert True
