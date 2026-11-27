import firedrake as fd
import ufl
from gadopt.utility import is_continuous, normal_is_continuous, get_functionspace


def assert_continuity_test(V, continuity_test, expected):
    # assert function in functionspace V tests continuous
    assert continuity_test(fd.Function(V)) == expected
    # same check for sub space of mixed space
    W = fd.FunctionSpace(V.mesh(), "CG", 1)
    Z = V * W
    assert continuity_test(fd.Function(Z).sub(0)) == expected


def assert_continuity(V, expected=True):
    assert_continuity_test(V, is_continuous, expected)


def assert_normal_continuity(V, expected=True):
    assert_continuity_test(V, normal_is_continuous, expected)


def test_continuity():
    assert True
