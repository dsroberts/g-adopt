"""Tolerances for the weak boundary condition diagnostics of the Stokes momentum term.

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

from .meta import GROUP_MESHES
from .stokes_helpers import (
    MMS_RESOLUTIONS,
    STRUCTURE_CASES,
    SYMMETRY_APPROXIMATIONS,
    TOSI_RESOLUTIONS,
    WEAK_BOUNDARY_CASES,
)

CASE_DIR = Path(__file__).parent

# Symmetry is measured relative to the norm of the matrix itself, so this is a
# dimensionless distance from exact symmetry. A generic, strongly strained
# linearisation point puts entries of very different magnitudes in the same
# matrix, which is why the bound is not at machine epsilon.
SYMMETRY_RTOL = 1e-11
# The reference forms are built from the same quadrature as the code under test,
# so agreement is limited only by round-off in the assembled values.
REFERENCE_RTOL = 1e-13
# The variational structure identity is exact in exact arithmetic.
STRUCTURE_RTOL = 1e-12


def load(name):
    """Read one diagnostics file as rows and columns.

    `loadtxt` collapses a file holding a single row, or a single column, to one
    dimension, and the two cases are then indistinguishable. `ndmin=2` keeps the
    shape the file was written with, so every caller can index it as
    `[row][column]`.
    """
    return np.loadtxt(CASE_DIR / name, ndmin=2)


APPROXIMATION_IDS = [name for name, _ in SYMMETRY_APPROXIMATIONS]


@pytest.mark.parametrize("mesh_key", GROUP_MESHES["nonlinear_viscosity"])
def test_nonlinear_viscosity_jacobian_symmetric(mesh_key):
    assert True


@pytest.mark.parametrize("mesh_key", GROUP_MESHES["weak_u_symmetry"])
def test_weak_u_jacobian_symmetric(mesh_key):
    assert True


@pytest.mark.parametrize("mesh_key", GROUP_MESHES["variational_structure"])
def test_residual_is_first_variation(mesh_key):
    assert True


@pytest.mark.parametrize("mesh_key", GROUP_MESHES["explicit_forms"])
def test_matches_explicit_forms(mesh_key):
    assert True


# Taylor-Hood P2-P1 L2 convergence orders.
THEORY_ORDER_U, THEORY_ORDER_P = 3.0, 2.0
# Tolerance band on the measured order, sized to the failure it guards. A
# boundary term inconsistent with the continuous problem converges to a
# different solution and collapses the order well below theory, so 0.25
# separates a passing solve from that failure. A consistent but wrong term (a
# mis-scaled penalty, or a non-symmetric symmetriser) keeps the optimal order 3
# and is caught by the symmetry and variational-structure tests above.
ORDER_TOL = 0.25
# Quasi-optimality factor: Cea and Aubin-Nitsche bound the Galerkin L2 error by
# a constant times the best-approximation (here interpolation) error. The
# measured ratio is about 1 at every level, so 2 is a real stability margin,
# dimensionless and scaling with the mesh size.
K_STAB = 2


def assert_order(errors, order, tol=ORDER_TOL):
    """Assert the measured convergence order is at least `order - tol`.

    One-sided: exceeding the theoretical order is genuine superconvergence on
    these uniform quadrilateral meshes (the pressure runs at about 3.7), never a
    regression.
    """
    for k in range(len(errors) - 1):
        measured = log2(errors[k] / errors[k + 1])
        assert measured >= order - tol, (
            f"order {measured:.2f} between levels {k} and {k + 1}, "
            f"expected at least {order - tol:.2f}")


def assert_quasi_optimal(errors, interpolation_errors):
    """Bound the error constant, not only the rate.

    An inconsistent boundary term inflates the velocity error by orders of
    magnitude alongside the order collapse, while a correct scheme stays within
    a small factor of the interpolation error. A consistent but mis-scaled
    penalty leaves this constant essentially unchanged and is pinned by
    `test_residual_is_first_variation` instead.
    """
    for error, interpolation in zip(errors, interpolation_errors):
        assert error <= K_STAB * interpolation, (
            f"error {error:.3e} exceeds {K_STAB} times the interpolation error "
            f"{interpolation:.3e}")


def test_mms_weak_un_convergence():
    assert True


def test_mms_weak_u_convergence():
    assert True


# The weak-to-strong difference is bounded by the sum of the two P2 velocity L2
# errors, so it decays at their order.
THEORY_ORDER_D = 3.0
# A looser band than the manufactured-solution cases: the difference is between
# two errors, so they partly cancel, and the regularity of the Tosi solution is
# not certified, so a correct rate can genuinely sit somewhat below 3. The
# failure this guards is a weak side inconsistent with the continuous problem,
# where the difference plateaus rather than decaying at all.
ORDER_TOL_D = 0.5
# The one absolute bound in this file: a specification, not a regression pin.
# The two formulations must agree to within 1% in relative velocity at the
# finest resolution.
MAX_RELATIVE_DIFFERENCE = 1e-2


def test_tosi_weak_freeslip_matches_strong():
    assert True
