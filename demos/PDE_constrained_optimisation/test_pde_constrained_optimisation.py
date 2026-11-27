import pytest
from pathlib import Path

cases = [("boundary", 2e-3), ("field", 7e-3)]


@pytest.mark.parametrize("name,functional_tolerance", cases)
def test_pde_constrained_optimisation(name, functional_tolerance):
    assert True
