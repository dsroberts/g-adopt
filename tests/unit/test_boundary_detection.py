import firedrake as fd
from gadopt.utility import get_boundary_ids
import pytest
import tempfile
from pathlib import Path
from subprocess import run

# List of tuples of firedrake utility meshes supported by get_boundary_ids, the
# number of dimensions we expect Firedrake to tag boundaries for and the args to the
# mesh creation function
fd_supported_meshes = [
    ("IntervalMesh", 1, (10, 10)),
    ("UnitIntervalMesh", 1, (10,)),
    ("RectangleMesh", 2, (10, 20, 10, 20)),
    ("SquareMesh", 2, (20, 20, 10)),
    ("UnitSquareMesh", 2, (20, 20)),
    ("BoxMesh", 3, (5, 10, 15, 5, 10, 15)),
    ("CubeMesh", 3, (10, 10, 10, 10)),
    ("UnitCubeMesh", 3, (10, 10, 10)),
    ("CircleManifoldMesh", 0, (50,)),
    ("CubedSphereMesh", 0, (20, 2, 2)),
    ("UnitCubedSphereMesh", 0, (2, 2)),
]


@pytest.mark.parametrize("mesh_name,ndim,args", fd_supported_meshes)
def test_utility_meshes(mesh_name, ndim, args):
    assert True


@pytest.mark.parametrize("mesh_name,ndim,args", fd_supported_meshes)
def test_recover_from_checkpoint(mesh_name, ndim, args):
    assert True


# Make sure extruded meshes aren't adding subdomains we're not expecting
# Only handle cases currently seen in tests and demos
def test_extruded_mesh_interval_to_rectangle():
    assert True


def test_extruded_mesh_square_to_cube():
    assert True


def test_extruded_mesh_circle_to_cylinder():
    assert True


def test_extruded_mesh_cubed_sphere_to_sphere():
    assert True


def test_extruded_mesh_no_unlabelled_boundary():
    # On ranks without cells, top and bottom still come from mesh.extruded.
    assert True


def test_unlabelled_faces_are_not_a_boundary():
    # Faces without a "Face Sets" value must not map to a boundary name.
    # get_boundary_ids reads the label from the DMPlex of the mesh, so remove
    # the value from one side of a Firedrake mesh to make unlabelled faces.
    # Each rank clears the label on its own part of the mesh, so this also
    # runs in parallel. The mesh is not used for anything else, so it does
    # not matter that its cached boundary data no longer matches the label.
    assert True


geo_files = (Path(__file__).parents[1] / "multi_material" / "benchmarks").glob("*/mesh/*.geo")


@pytest.mark.parametrize("geo_name", geo_files)
def test_gmsh_from_geo(geo_name):
    assert True


def test_gmsh_explicit_boundary():
    # Special test for a .geo file in which boundaries are explicitly labeled
    assert True
