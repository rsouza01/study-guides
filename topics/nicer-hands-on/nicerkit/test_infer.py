import numpy as np
import pytest
from nicerkit import eos as E, tov as T, mr, infer


def test_grid_density_normalisation_and_levels():
    M, R = mr.gaussian_mr(1.4, 12.0, 0.1, 0.7, rho=0.3, n=20000)
    g = mr.GridDensity(M, R)
    dM, dR = g.Mg[1] - g.Mg[0], g.Rg[1] - g.Rg[0]
    assert g.Z.sum() * dM * dR == pytest.approx(1.0, abs=0.02)
    # 68% level contains ~68% of the samples
    lev = g.level_for_mass(0.68)
    inside = g(M[:4000], R[:4000]) > lev
    assert inside.mean() == pytest.approx(0.68, abs=0.03)


def test_log_likelihood_prefers_true_eos():
    true = E.PiecewisePolytrope(**E.SLY_PARAMS)
    Pc, Mc, Rc = T.mr_curve_pp(true, n=120)
    srcs = []
    for M0, sM, sR in [(1.4, 0.15, 0.8), (2.07, 0.07, 1.0)]:
        R0 = float(np.interp(M0, Mc, Rc))
        M, R = mr.gaussian_mr(M0, R0, sM, sR, n=20000, seed=int(M0 * 10))
        srcs.append(infer.Source(f"s{M0}", mr.GridDensity(M, R)))
    th_true = list(E.SLY_PARAMS.values())
    th_stiff = [34.6, 3.0, 3.0, 3.0]
    ll_true = infer.log_likelihood(th_true, srcs)
    ll_stiff = infer.log_likelihood(th_stiff, srcs)
    assert np.isfinite(ll_true)
    assert ll_true > ll_stiff


def test_injection_recovery_short_chain():
    true = E.PiecewisePolytrope(**E.SLY_PARAMS)
    Pc, Mc, Rc = T.mr_curve_pp(true, n=120)
    srcs = []
    for M0, sM, sR in [(1.4, 0.12, 0.6), (1.4, 0.12, 0.6), (2.07, 0.07, 0.8)]:
        R0 = float(np.interp(M0, Mc, Rc))
        M, R = mr.gaussian_mr(M0, R0, sM, sR, n=20000, seed=int(M0 * 100 + sR * 10))
        srcs.append(infer.Source(f"s{M0}", mr.GridDensity(M, R)))
    sam = infer.run_emcee(srcs, list(E.SLY_PARAMS.values()), nwalkers=16, nsteps=250, progress=False)
    chain = sam.get_chain(discard=100, flat=True)
    assert len(chain) > 1000
    r14 = []
    for th in chain[::25]:
        d = infer.derived(th)
        if d: r14.append(d["R14"])
    r14 = np.array(r14)
    R14_true = float(np.interp(1.4, Mc, Rc))
    assert abs(np.median(r14) - R14_true) < 0.6
