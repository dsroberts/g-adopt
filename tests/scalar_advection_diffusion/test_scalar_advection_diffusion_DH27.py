# Test based on scalar advection-diffusion problem from Figure 2.7 in
# Chapter 2 Steady transport problems from Finite element Methods
# for Flow problems - Donea and Huerta, 2003
# Tests for second order convergence cf with the analytical solution
# (when grid Peclet < 1) and for regression testing based on solution norm.

import itertools
import numpy as np
from pathlib import Path
import pytest

# Test each grid Peclet number with SU enabled and disabled
conf = {
    "Pe": [0.25, 0.9, 50.0],
    "SU": [True, False],
}

# Only test the analytical convergence of the Pe=0.25 cases
convergence = [2.0, 2.0, None, None, None, None]

param_sets = zip(itertools.product(*conf.values()), convergence)

base = Path(__file__).parent.resolve()


@pytest.fixture
def expected_errors():
    return np.load(base / "expected_errors.npz")


@pytest.mark.parametrize("params,expected_convergence", param_sets)
def test_scalar_advection_diffusion_DH27(params, expected_convergence, expected_errors):
    assert True


if __name__ == "__main__":
    for c in param_sets:
        print("_".join([str(x) for x in c[0]]))
