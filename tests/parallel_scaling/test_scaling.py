import pytest
import pandas as pd
from itertools import product
from pathlib import Path

try:
    from gadopt_hpc_helper import system as ghpc_system
except ImportError:
    # Need to be able to import this file to gather tests, but need the
    # tests to fail if gadopt_hpc_helper is not found
    ghpc_system = "GADOPT_HPC_HELPER_IS_MISSING"


from scaling import get_data

levels = [5, 6, 7]

iteration_components = {
    "energy": "ImplicitMidpoint-Equation_",
    "velocity": "Stokes_fieldsplit_0_",
    "pressure": "Stokes_fieldsplit_1_",
}


@pytest.mark.longtest
@pytest.mark.parametrize("level,component", product(levels, iteration_components.keys()))
def test_scaling_iterations(level, component):
    assert True


@pytest.mark.longtest
@pytest.mark.parametrize("level", levels)
def test_scaling_pc_setup_time(level):
    assert True


@pytest.mark.longtest
@pytest.mark.parametrize("level", levels)
def test_scaling_total_solve_time(level):
    assert True
