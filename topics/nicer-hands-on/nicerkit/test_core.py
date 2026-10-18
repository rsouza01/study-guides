import numpy as np
import pytest
from nicerkit import eos as E, tov as T
from nicerkit.constants import C2, G, C, MSUN, KM


def test_crust_pressure_continuity():
    sly = E.sly()
    # P is continuous across all boundaries by construction of P_b from the upper segment;
    # check the *lower* segment gives the same value => validates the published constants.
    for i, rb in enumerate(sly.rho_b):
        lower = sly.K[i] * rb ** sly.Gam[i]
        upper = sly.K[i + 1] * rb ** sly.Gam[i + 1]
        assert lower == pytest.approx(upper, rel=3e-4), f"boundary {i}"


def test_eps_continuity_and_causality_low_density():
    sly = E.sly()
    P = np.logspace(24, 35.5, 400)
    eps = sly.eps_of_P(P)
    assert np.all(np.diff(eps) > 0)
    assert np.all(sly.cs2_of_P(P)[P < 1e34] < 1.0)


def test_thermodynamic_consistency():
    # d(eps)/d(rho) = (eps+P)/rho  <=>  eps(P) obeys first law
    sly = E.sly()
    P = np.array([1e30, 1e33, 5e34])
    h = 1e-4
    rho = sly.rho_of_P(P)
    rho2 = rho * (1 + h)
    P2 = sly.P_of_rho(rho2)
    d_eps = sly.eps_of_P(P2) - sly.eps_of_P(P)
    rhs = (sly.eps_of_P(P) + P) / rho * (rho2 - rho)
    assert d_eps == pytest.approx(rhs, rel=2e-3)


def test_constant_density_exact_interior():
    eps0 = 5.0e14 * C2          # erg cm^-3
    eos = E.ConstantDensity(eps0)
    s = T.solve_star(eos, 1.0e35, P_surf=1.0e35 * 1e-9, extras=False, rtol=1e-10)
    Mg = s["M"] * MSUN * G / C**2
    R = s["R"] * KM
    eps_g = eps0 * G / C**4
    assert Mg == pytest.approx(4 * np.pi / 3 * eps_g * R**3, rel=2e-3)
    # exact central pressure from the Schwarzschild interior solution
    x = np.sqrt(1 - 2 * Mg / R)
    Pc_exact = eps0 * (1 - x) / (3 * x - 1)
    assert Pc_exact == pytest.approx(1.0e35, rel=5e-3)


def test_newtonian_n1_polytrope_I_and_k2():
    # low-compactness n=1 polytrope: I/(M R^2) -> 0.261, k2 -> (15 - pi^2)/(2 pi^2) = 0.2599
    K = 1.0e5 * 1.0   # P = K rho^2  (cgs); R = sqrt(pi K / (2 G))
    eos = E.SimplePolytrope(K=K, Gamma=2.0)
    rho_c = 1.0e6
    Pc = K * rho_c**2
    s = T.solve_star(eos, Pc, P_surf=Pc * 1e-12, rtol=1e-10)
    assert s["C"] < 1e-3
    assert s["I"] / (s["M"] * MSUN * (s["R"] * KM) ** 2) == pytest.approx(0.261, abs=0.004)
    assert s["k2"] == pytest.approx(0.2599, abs=0.004)
    assert s["y_tidal"] == pytest.approx(0.29, abs=0.01)
    Rexp = np.sqrt(np.pi * K / (2 * G)) / KM
    assert s["R"] == pytest.approx(Rexp, rel=2e-3)


def test_sly_known_numbers():
    sly = E.sly()
    Pc, M, R = T.mr_curve_pp(sly, n=120)
    assert 2.03 < M.max() < 2.07         # SLy: M_max = 2.05 Msun (published 2.05)
    # R at 1.4 Msun by interpolation
    R14 = np.interp(1.4, M, R)
    assert 11.3 < R14 < 12.1             # SLy: R_1.4 ~ 11.7 km


def test_fast_and_slow_paths_agree():
    sly = E.sly()
    Pc = 3.0e34
    s = T.solve_star(sly, Pc, extras=False)
    K, Gam, a, Pb = sly.numba_arrays()
    M, R = T._tov_pp(Pc, K, Gam, a, Pb, 1.0e19)
    assert M == pytest.approx(s["M"], rel=2e-3)
    assert R == pytest.approx(s["R"], rel=3e-3)
