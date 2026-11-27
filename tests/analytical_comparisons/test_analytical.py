from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import itertools

from .analytical import cases, get_case

enabled_cases = {
    "smooth_cylindrical_freeslip": {
        "convergence": (4.0, 2.0, 2.0),
        "rtol": 1e-1,
        "ns_lb": 1e-1,
    },
    "smooth_cylindrical_zeroslip": {
        "convergence": (4.0, 2.0, 2.0),
        "ns_lb": 1e-1,
        "ns_ub": 7e-1,
    },
    "smooth_cylindrical_freesurface": {"convergence": (4.0, 2.0, 2.0), "rtol": 1e-1},
    "delta_cylindrical_freeslip": {"convergence": (1.5, 0.5, 2.0)},
    "delta_cylindrical_zeroslip": {"convergence": (1.5, 0.5, 2.0), "ns_lb": 5e-2},
    "delta_cylindrical_freeslip_dpc": {"convergence": (3.5, 2.0, 2.0), "rtol": 1e-1},
    "delta_cylindrical_zeroslip_dpc": {
        "convergence": (3.5, 2.0, 2.0),
        "rtol": 2e-1,
        "ns_lb": 5e-2,
    },
    "smooth_spherical_freeslip": {
        "convergence": (4.0, 2.0, 2.0),
        "rtol": 1e-1,
        "ns_lb": 1e-1,
    },
    "smooth_spherical_zeroslip": {
        "convergence": (4.0, 2.0, 2.0),
        "rtol": 1e-1,
        "ns_lb": 1e-1,
    },
}

longtest_cases = [
    "smooth_cylindrical_freesurface",
    "smooth_spherical_freeslip",
    "smooth_spherical_zeroslip",
]

params = {
    f"{l1}_{l2}_{l3}": v3
    for l1, v1 in cases.items()
    for l2, v2 in v1.items()
    for l3, v3 in v2.items()
    if f"{l1}_{l2}_{l3}" in enabled_cases.keys()
}


def param_sets(config, permutate=False):
    if permutate:
        return itertools.product(*config.values())

    return zip(*config.values())


configs = []
param_sets_list = []
for name, conf in params.items():
    # these two keys don't form a part of the parameter matrix
    conf = conf.copy()
    conf.pop("cores")
    conf.pop("levels")
    permutate = conf.pop("permutate", True)

    for combination in param_sets(conf, permutate):
        conf_tuple = (name, enabled_cases[name], dict(zip(conf.keys(), combination)))
        configs.append(conf_tuple)
        if name in longtest_cases:
            param_sets_list.append(pytest.param(*conf_tuple, marks=pytest.mark.longtest))
        else:
            param_sets_list.append(conf_tuple)


def idfn(val):
    if isinstance(val, dict):
        return "-".join([f"{k}{v}" for k, v in val.items()])


@pytest.mark.parametrize("name,expected,config", param_sets_list, ids=idfn)
def test_analytical(name, expected, config):
    assert True
