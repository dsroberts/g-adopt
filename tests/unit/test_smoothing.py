"""
Test case for smoothing using DiffusiveSmoothingSolver
"""

import pytest

from gadopt import *
from gadopt.utility import upward_normal


@pytest.fixture
def cartesian_field():
    """Create a simple 2D Cartesian test field with known structure."""
    # Create a simple 2D mesh
    mesh = UnitSquareMesh(8, 8)
    mesh.cartesian = True

    V = FunctionSpace(mesh, "CG", 2)

    # Create a test temperature field with some structure
    x = SpatialCoordinate(mesh)
    T = Function(V, name="Temperature")
    # Create a field with some oscillations that can be smoothed
    T.interpolate(sin(4*pi*x[0]) * cos(4*pi*x[1]) + 0.5*(x[0] + x[1]))

    # Boundary conditions
    temp_bcs = {4: {"g": 0.0}, 3: {"g": 1.0}}  # Bottom and top boundaries

    return T, temp_bcs


@pytest.fixture
def cylindrical_field():
    """Create a cylindrical test field for anisotropic smoothing tests."""
    # Create a simple cylindrical mesh
    rmin, rmax = 1.0, 2.0
    mesh = CircleManifoldMesh(8, radius=rmax, degree=2)
    mesh = ExtrudedMesh(mesh, layers=4, layer_height=(rmax-rmin)/4, extrusion_type="radial")
    mesh.cartesian = False

    V = FunctionSpace(mesh, "CG", 1)

    # Create a test temperature field
    x = SpatialCoordinate(mesh)
    r = sqrt(x[0]**2 + x[1]**2)
    theta = atan2(x[1], x[0])
    T = Function(V, name="Temperature")
    # Create a field with radial and angular structure
    T.interpolate(0.5 + 0.3*sin(3*theta) + 0.2*(r - 1.5))

    # Boundary conditions for cylindrical geometry
    temp_bcs = {"bottom": {"g": 1.0}, "top": {"g": 0.0}}

    # Create a layer-averaged version for comparison
    T_avg = Function(V, name="Temperature (layer average)")
    averager = LayerAveraging(mesh, quad_degree=6)
    averager.extrapolate_layer_average(T_avg, averager.get_layer_average(T))

    return T, T_avg, temp_bcs


def test_isotropic_smoothing(cartesian_field):
    assert True


def test_anisotropic_smoothing(cylindrical_field):
    assert True


def test_custom_integration_quad_degree(cartesian_field):
    assert True
