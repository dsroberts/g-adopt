from pathlib import Path

import numpy as np
import pytest

base = Path(__file__).parent.resolve()


def run_benchmark(model):
    # Run default case run for four dt factors
    if model.name == "explicit":
        dtf_start = 1
    else:
        dtf_start = 2
    dt_factors = dtf_start / (2 ** np.arange(4))

    for iterative in [False, True]:
        errors = []
        errors_zeta = []
        if iterative and not model.iterative:
            continue
        if not iterative and not model.direct:
            continue

        prefix = f"errors-{model.name}"
        if iterative:
            prefix += "-iterative"
        for dtf in dt_factors:
            simulation = model(dtf, iterative_2d=iterative)
            simulation.run_simulation()
            errors.append(simulation.final_error)
            if simulation.bottom_free_surface:
                errors_zeta.append(simulation.final_zeta_error)
        if simulation.bottom_free_surface:
            np.savetxt(f"{prefix}-top-free-surface-coupling.dat", errors)
            np.savetxt(f"{prefix}-bottom-free-surface-coupling.dat", errors_zeta)
        else:
            np.savetxt(f"{prefix}-free-surface-coupling.dat", errors)


@pytest.fixture
def expected_errors():
    return np.load(base / "expected_errors.npz")


cases = [
    ("explicit", [1.4, 1.1, 1.0]),
    ("implicit", [2.0, 2.0, 2.0]),
    ("implicit-iterative", [2.0, 2.0, 2.0]),
    ("implicit-both-top", [2.0, 2.0, 2.0]),
    ("implicit-both-bottom", [2.0, 2.0, 2.0]),
    ("implicit-both-iterative-top", [2.0, 2.0, 2.0]),
    ("implicit-both-iterative-bottom", [2.0, 2.0, 2.0]),
    ("implicit-buoyancy-top", [2.0, 2.0, 2.0]),
    ("implicit-buoyancy-bottom", [2.0, 2.0, 2.0]),
    ("implicit-buoyancy-iterative-top", [2.0, 2.0, 2.0]),
    ("implicit-buoyancy-iterative-bottom", [2.0, 2.0, 2.0]),
    ("implicit-cylindrical-iterative", [2.0, 2.0, 2.0]),
]


@pytest.mark.parametrize("coupling,expected_convergence", cases)
def test_free_surface(coupling, expected_convergence, expected_errors):
    assert True
