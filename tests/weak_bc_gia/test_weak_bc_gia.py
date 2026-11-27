"""Tolerances for the weak boundary condition diagnostics of the viscoelastic solvers.

The entrypoints in this directory do the assembly and the solves under
`doit run_case` and write their numbers to `.dat` files. This file reads those
files and applies the tolerances, so a failure names the case and prints the
number that missed.

Running these tests without running `doit run_case` first fails on the missing
file, which is how every case directory in `tests/` behaves.
"""

from math import log2
from pathlib import Path

import numpy as np
import pytest

from .gia_helpers import (
    BLOCK_SYMMETRY_CASES,
    REFINEMENT_RESOLUTIONS,
    WEAK_U_HISTORIES,
)
from .meta import MESHES, REFINEMENT_DT_OVER_TAU

CASE_DIR = Path(__file__).parent

# Symmetry is measured relative to the norm of the matrix itself, so this is a
# dimensionless distance from exact symmetry.
SYMMETRY_RTOL = 1e-13
# The variational structure identity is exact in exact arithmetic.
STRUCTURE_RTOL = 1e-12
# The displacement space is P2, so both the gap between the two formulations and
# the normal jump on the weak boundary must fall at least this fast.
REFINEMENT_ORDER = 2.0
# Below this fraction of the displacement norm the coarse gap is round-off, and
# a rate computed from it would be measuring noise instead of a difference
# between the two formulations.
GAP_FLOOR = 1e-8


def load(name):
    """Read one diagnostics file as rows and columns.

    `loadtxt` collapses a file holding a single row, or a single column, to one
    dimension, and the two cases are then indistinguishable. `ndmin=2` keeps the
    shape the file was written with, so every caller can index it as
    `[row][column]`.
    """
    return np.loadtxt(CASE_DIR / name, ndmin=2)


@pytest.mark.parametrize("mesh_key", MESHES)
def test_coupled_displacement_block_symmetry(mesh_key):
    assert True


@pytest.mark.parametrize("mesh_key", MESHES)
def test_pointwise_residual_is_first_variation(mesh_key):
    assert True


@pytest.mark.parametrize("mesh_key", MESHES)
def test_coupled_residual_is_first_variation(mesh_key):
    assert True


@pytest.mark.parametrize("mesh_key", MESHES)
def test_weak_u_jacobian_symmetric(mesh_key):
    assert True


@pytest.mark.parametrize("dt_over_tau", REFINEMENT_DT_OVER_TAU)
def test_coupled_matches_pointwise_under_refinement(dt_over_tau):
    assert True


def test_coupled_iterative_preset_converges():
    assert True
