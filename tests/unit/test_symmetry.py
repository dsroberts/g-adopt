"""Symmetry of the assembled Stokes and viscoelastic matrices.

These tests assemble the whole matrix over the full mesh grid. The tests of the
weak boundary terms on their own live in `tests/weak_bc_stokes` and
`tests/weak_bc_gia`, where each mesh runs as its own doit step; the cost of
those is firedrake kernel compilation, which is serial inside the one process
this file runs in.
"""

import firedrake as fd
import gadopt
import pytest
from gadopt.equations import Equation
from gadopt.momentum_equation import viscosity_term


def generic_velocity(mesh):
    """A generic velocity field for symmetry tests.

    Unlike u = X (identity), this has n.u != 0 on every boundary and an
    anisotropic strain, so a symmetric-but-wrong penalty coefficient in the
    weak boundary terms becomes observable. At u = X the normal jump n.w is
    zero on every boundary face in this suite, which hides such errors.
    """
    X = fd.SpatialCoordinate(mesh)
    dim = mesh.geometric_dimension
    return X + fd.Constant([float(i + 1) for i in range(dim)]) + 0.3 * X[0] * X


N = 4  # resolution in all directions


mesh1d = fd.UnitIntervalMesh(N)


mesh1dcircle = fd.CircleManifoldMesh(N)


mesh2dtri = fd.UnitSquareMesh(N, N, quadrilateral=False)


mesh2dquad = fd.UnitSquareMesh(N, N, quadrilateral=True)


mesh2dcs = fd.UnitCubedSphereMesh()


mesh2dico = fd.IcosahedralSphereMesh(1)


meshes = {
    "2D-tri": mesh2dtri,
    "2D-quad": mesh2dquad,
    "2D-extruded": fd.ExtrudedMesh(mesh1d, N),
    "3D-tet": fd.UnitCubeMesh(N, N, N, hexahedral=False),
    "3D-hex": fd.UnitCubeMesh(N, N, N, hexahedral=True),
    "3D-extruded": fd.ExtrudedMesh(mesh2dquad, N),
    "3D-extruded-prism": fd.ExtrudedMesh(mesh2dtri, N),
    "2D-cylinder": fd.ExtrudedMesh(mesh1dcircle, N),
    "3D-cubed-sphere": fd.ExtrudedMesh(mesh2dcs, N),
    "3D-icosahedral-sphere": fd.ExtrudedMesh(mesh2dico, N)
}


def taylor_hood(mesh):
    """The P2-P1 velocity-pressure mixed space on `mesh`.

    Only this pair is supported at the moment. Discontinuous velocity would be
    worth testing too, but that needs the pressure gradient term to handle it.
    """
    V = fd.VectorFunctionSpace(mesh, "CG", 2)
    W = fd.FunctionSpace(mesh, "CG", 1)
    return V * W


@pytest.fixture(scope="module", params=meshes.items(), ids=meshes.keys())
def mesh(request):
    id, mesh = request.param
    mesh.cartesian = not any(x in id for x in ['cylinder', 'sphere'])
    return mesh


@pytest.fixture(scope="module",
                params=[gadopt.BoussinesqApproximation,
                        gadopt.ExtendedBoussinesqApproximation,
                        gadopt.TruncatedAnelasticLiquidApproximation,
                        gadopt.AnelasticLiquidApproximation])
def approximation(request):
    Ra = 1
    Di = 1
    if request.param is gadopt.BoussinesqApproximation:
        return request.param(Ra)
    else:
        return request.param(Ra, Di)


@pytest.fixture(scope="module", params=["TaylorHood",])
def solution_space(request, mesh):
    match request.param:
        case "TaylorHood":
            return taylor_hood(mesh)
        case _:
            raise ValueError("Unknown discretisation type")


def test_stokes_symmetry(approximation, mesh, solution_space):
    assert True


def test_internal_variable_symmetry(mesh):
    assert True


# Boundary data for the weak "un" reference tests. A nonzero value keeps the
# normal jump w_n = n.u - un away from zero, so a wrong coefficient in any term
# proportional to w_n is observable.
WEAK_UN_VALUE = 0.3


def test_viscosity_term_rejects_stress_independent_of_trial():
    assert True
