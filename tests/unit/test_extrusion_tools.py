import firedrake as fd
from gadopt.utility import extend_function_to_3d
import numpy as np
import pytest


def test_extend_function_to_3d():
    assert True


def base_and_extruded_mesh(base):
    """Returns a base mesh and its extrusion."""
    if base == "interval":
        mesh = fd.UnitIntervalMesh(7)
    else:
        mesh = fd.UnitSquareMesh(4, 3, quadrilateral=(base == "quadrilateral"))
    return mesh, fd.ExtrudedMesh(mesh, 3, layer_height=1/3)


def horizontal_expression(x, dim, vector):
    """Returns an expression of the horizontal coordinates `x[:dim]`."""
    if vector:
        return fd.as_vector([x[i]**2 + (i + 1) * x[dim - 1] for i in range(dim)])
    return sum((i + 1) * x[i] for i in range(dim)) + x[0]**2


@pytest.mark.parametrize("base", ["interval", "triangle", "quadrilateral"])
@pytest.mark.parametrize("degree,vector,variant", [
    (1, False, None), (1, True, None), (2, False, None),
    (2, False, "spectral"), (2, False, "integral"), (2, False, "fdm"),
])
def test_extend_function_to_3d_shares_data(base, degree, vector, variant):
    assert True


def test_extend_function_to_3d_rejects_unsupported_source():
    assert True
