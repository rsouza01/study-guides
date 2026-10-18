import numpy as np
import pytest
from nicerkit import fold, bursts


def test_z2_null_distribution():
    rng = np.random.default_rng(0)
    z = [fold.z2m(rng.uniform(size=2000), m=2) for _ in range(300)]
    assert np.mean(z) == pytest.approx(4.0, abs=0.5)     # chi2 with 4 dof has mean 4


def test_blind_period_search_recovers_frequency():
    f0, fdot, T = 29.6, -3.7e-10, 3000.0
    t = fold.simulate_events(T, f0, fdot, src_rate=25.0, bkg_rate=10.0, seed=4)
    grid = fold.frequency_grid(29.55, 29.65, T, oversample=5)
    z = fold.z2m_scan(t, grid, m=2, fdot=fdot)
    fbest = grid[np.argmax(z)]
    assert abs(fbest - f0) < 1.5 / T
    H, m, fap = fold.htest(fold.phases(t, fbest, fdot))
    assert fap < 1e-10


def test_profile_and_pulsed_fraction():
    t = fold.simulate_events(2000.0, 10.0, src_rate=40.0, bkg_rate=0.0, seed=2)
    x, c, e = fold.fold(t, 10.0, nbins=32, t0=0.0)
    assert c.argmax() in range(8, 12)                    # peak at phase 0.3
    assert 0.8 < fold.pulsed_fraction(c) <= 1.0           # no background: amplitude ~ 1


def test_burst_finder_and_decay_fit():
    tc, rate = bursts.simulate_lightcurve(seed=3)
    found = bursts.find_bursts(tc, rate)
    assert len(found) == 2
    assert abs(found[0]["t_peak"] - 600) < 5 and abs(found[1]["t_peak"] - 1500) < 5
    tau, err = bursts.fit_decay(tc, rate, found[0]["t_peak"], found[0]["baseline"])
    assert tau == pytest.approx(12.0, rel=0.25)


def test_fft_search_then_refine():
    f0, T = 29.5123, 3000.0
    t = fold.simulate_events(T, f0, 0.0, src_rate=3.0, bkg_rate=8.0, seed=21)
    f, p = fold.fft_power_search(t, dt=0.004, fmin=20, fmax=40)
    fpk = f[np.argmax(p)]
    assert abs(fpk - f0) < 2.0 / T
    grid = np.arange(fpk - 3.0 / T, fpk + 3.0 / T, 0.05 / T)
    z = fold.z2m_scan(t, grid, m=2)
    assert abs(grid[np.argmax(z)] - f0) < 0.5 / T
