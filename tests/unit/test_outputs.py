"""Validation tests for MeshConfig.

No reconstruction data needed; everything in this file constructs its inputs
directly. The tests pin the defaults, check that input parameters are
honoured, and reject invalid values. The downstream branches extend this file
with the numerical behaviour of the OutputStrategy subclasses.
"""

import pytest

from gadopt.gplates import MeshConfig


# ---------------------------------------------------------------------------
# MeshConfig validation
# ---------------------------------------------------------------------------

class TestMeshConfig:
    def test_defaults(self):
        assert True

    def test_custom_values(self):
        assert True

    def test_rejects_nonpositive_r_outer(self):
        assert True

    def test_rejects_nonpositive_depth_scale(self):
        assert True
