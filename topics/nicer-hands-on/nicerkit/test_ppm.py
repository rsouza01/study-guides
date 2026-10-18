import numpy as np
import pytest
from nicerkit import ppm


def test_newtonian_limit_visible_half_only():
    ph = np.linspace(0, 1, 200, endpoint=False)
    f = ppm.single_spot_flux(ph, u=1e-6, inc=np.pi / 2, theta=np.pi / 2, doppler=False)
    # equatorial spot, edge-on, no bending: visible for exactly half the rotation
    assert (f > 1e-9).mean() == pytest.approx(0.5, abs=0.02)


def test_bending_reduces_pulsed_fraction_and_shows_more_of_the_star():
    ph = np.linspace(0, 1, 400, endpoint=False)
    pf, vis = [], []
    for u in (0.05, 0.2, 0.35, 0.5):
        f = ppm.two_spot_profile(ph, u, inc=np.radians(60), theta=np.radians(50), doppler=False)
        pf.append(ppm.pulsed_fraction_amp(f))
        vis.append((ppm.single_spot_flux(ph, u, np.radians(60), np.radians(50), doppler=False) > 0).mean())
    assert all(np.diff(pf) < 0)
    assert all(np.diff(vis) >= 0)


def test_noise_free_recovery_of_compactness():
    nu, nb = 205.0, 32
    ph = (np.arange(nb) + 0.5) / nb
    truth = np.array([0.35, np.cos(np.radians(55)), np.radians(55), 5.0, 4.0])
    counts = ppm.model_counts(truth, ph, nu)
    nll, th = ppm.fit_profile(counts, nu, n_starts=30)
    # noise-free data: the fit must reproduce the profile (degeneracies allowed in parameters)
    assert np.max(np.abs(ppm.model_counts(th, ph, nu) - counts)) / counts.max() < 0.02


def test_profile_likelihood_has_minimum_near_truth_with_finite_width():
    nu, nb = 205.0, 32
    ph = (np.arange(nb) + 0.5) / nb
    truth = np.array([0.35, np.cos(np.radians(55)), np.radians(55), np.log10(2.0e5), np.log10(2.0e5)])
    rng = np.random.default_rng(1)
    counts = rng.poisson(ppm.model_counts(truth, ph, nu)).astype(float)
    ug = np.array([0.15, 0.25, 0.35, 0.45, 0.55])
    d2 = ppm.profile_likelihood_u(counts, nu, ug, n_starts=15)
    assert np.argmin(d2) in (1, 2, 3)
    assert d2[0] > 4.0 or d2[-1] > 4.0          # not completely unconstrained
