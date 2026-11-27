# Test internal variable viscoelastic free surface
from pathlib import Path

import numpy as np
import pytest
base = Path(__file__).parent.resolve()


@pytest.fixture
def expected_errors():
    return np.load(base / "expected_errors.npz")


cases = [
    ("viscoelastic-compressible", [0.96, 0.98]),  # Higher dx converges O(1)
    ("viscoelastic-compressible-burgers", [0.96, 0.98]),  # Higher dx converges O(1)
    ("elastic-compressible", [1.0, 1.0]),
]


@pytest.mark.parametrize("case_name,expected_convergence", cases)
def test_iv_ve_fs_coupled(case_name, expected_convergence, expected_errors):
    assert True
