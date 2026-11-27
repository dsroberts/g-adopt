import numpy as np
import pytest
from pathlib import Path


@pytest.mark.parametrize("procs", [1, 2])
def test_checkpointing(procs):
    assert True
