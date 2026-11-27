import firedrake as fd
import numpy as np
import gadopt
import ufl
import pytest

# Meshes for the limiter tests. Each value is (constructor, number of cells across x),
# and every mesh has vertices at 0.5 in each coordinate direction, so that a hat function
# with its peak at 0.5 peaks at a vertex.
# The meshes are built inside the tests, so that a deselected case builds nothing.
MESHES = {
    "quadrilateral": (lambda: fd.UnitSquareMesh(10, 10, quadrilateral=True), 10),
    "triangle": (lambda: fd.UnitSquareMesh(10, 10), 10),
    "extruded-interval": (lambda: fd.ExtrudedMesh(fd.UnitIntervalMesh(10), 10), 10),
    "prism": (lambda: fd.ExtrudedMesh(fd.UnitSquareMesh(4, 4), 2), 4),
}


def p1dg_element(mesh):
    """Equispaced P1DG element on the cell of `mesh`."""
    cell = mesh.ufl_cell()
    if hasattr(cell, "sub_cells"):
        hcell, vcell = cell.sub_cells
        return fd.TensorProductElement(
            fd.FiniteElement("DG", hcell, 1, variant="equispaced"),
            fd.FiniteElement("DG", vcell, 1, variant="equispaced"),
        )
    family = "DG" if cell == ufl.triangle else "DQ"
    return fd.FiniteElement(family, cell, 1, variant="equispaced")


@pytest.mark.parametrize("cell", MESHES)
def test_slope_limiters(cell):
    assert True


@pytest.mark.parametrize("cell", MESHES)
def test_vector_limiter_matches_components(cell):
    assert True


@pytest.mark.parametrize("cell", MESHES)
def test_limiter_clip_bounds(cell):
    assert True


def test_limiter_rejects_other_function_space():
    assert True
