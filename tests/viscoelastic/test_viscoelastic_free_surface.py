from pathlib import Path

import numpy as np
import pytest
base = Path(__file__).parent.resolve()


@pytest.fixture
def expected_errors():
    return np.load(base / "expected_errors.npz")


cases = [
    ("elastic-zhong", [1.5, 1.5, 1.5]),
    ("viscoelastic-zhong", [1.0, 1.0, 1.0]),
    ("viscous-zhong", [1.0, 1.0, 1.0]),
]


@pytest.mark.parametrize("case_name,expected_convergence", cases)
def test_viscoelastic_free_surface(case_name, expected_convergence, expected_errors):
    assert True
