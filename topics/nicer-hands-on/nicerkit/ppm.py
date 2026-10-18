"""Toy pulse-profile model for intuition: how compactness shapes a hot-spot light curve.

This is NOT X-PSI. It keeps only the physics that matters for the first lesson:
  * Schwarzschild light bending in the Beloborodov (2002) approximation,
        1 - cos(alpha) = (1 - u) (1 - cos(psi)),    u = r_s / R = 2GM/(R c^2),
    where psi is the angle between the surface normal at the spot and the line of sight,
    and alpha the emission angle that photon had to leave with to reach the observer;
  * a point-like, isotropically emitting spot (optional simple beaming);
  * optional first-order Doppler boosting from rotation (delta^4 on bolometric intensity;
    approximate, ignoring time delays and the oblate shape).
Real analyses (X-PSI) add oblateness, finite spot size and shape, energy dependence with
magnetic-free atmosphere tables, interstellar absorption, instrument response and background.
"""
import numpy as np
from scipy.optimize import minimize
from .constants import C, KM


def cos_alpha(u, cos_psi):
    return u + (1.0 - u) * cos_psi


def single_spot_flux(phase, u, inc, theta, nu=0.0, R_km=12.0, doppler=True, beam=0.0):
    """Relative flux from one point spot. phase in cycles; inc, theta in radians."""
    phi = 2 * np.pi * np.asarray(phase, float)
    cpsi = np.cos(inc) * np.cos(theta) + np.sin(inc) * np.sin(theta) * np.cos(phi)
    ca = cos_alpha(u, cpsi)
    vis = ca > 0.0
    spsi = np.sqrt(np.maximum(1.0 - cpsi**2, 1e-12))
    sa = np.sqrt(np.maximum(1.0 - ca**2, 0.0))
    flux = np.where(vis, ca * (1.0 + beam * ca) / (1.0 + beam), 0.0)
    if doppler and nu > 0.0:
        beta = 2 * np.pi * nu * R_km * KM * np.sin(theta) / C / np.sqrt(1.0 - u)
        gam = 1.0 / np.sqrt(1.0 - beta**2)
        cxi = -(sa / spsi) * np.sin(inc) * np.sin(phi)
        delta = 1.0 / (gam * (1.0 - beta * cxi))
        flux = flux * delta**4
    return flux


def two_spot_profile(phase, u, inc, theta, nu=0.0, R_km=12.0, doppler=True, beam=0.0):
    """Antipodal pair of identical spots (a centred-dipole caricature)."""
    return (single_spot_flux(phase, u, inc, theta, nu, R_km, doppler, beam)
            + single_spot_flux(np.asarray(phase) + 0.5, u, inc, np.pi - theta, nu, R_km, doppler, beam))


def pulsed_fraction_amp(profile):
    p = np.asarray(profile, float)
    return (p.max() - p.min()) / (p.max() + p.min())


def model_counts(params, phase, nu, R_km=12.0):
    """params = (u, cos_inc, theta, log10_amp, log10_bkg)  ->  expected counts per bin."""
    u, ci, th, la, lb = params
    shape = two_spot_profile(phase, u, np.arccos(ci), th, nu, R_km)
    return 10**la * shape + 10**lb


def neg_loglike(params, phase, counts, nu, R_km=12.0):
    u, ci, th, la, lb = params
    if not (0.05 < u < 0.7 and 0.0 < ci < 1.0 and 0.05 < th < np.pi / 2 + 0.5):
        return 1e30
    mu = model_counts(params, phase, nu, R_km)
    if np.any(mu <= 0):
        return 1e30
    return float(np.sum(mu - counts * np.log(mu)))


def fit_profile(counts, nu, R_km=12.0, n_starts=40, seed=0, fixed_u=None):
    """Maximum-likelihood fit of the toy model to a folded pulse profile (Poisson).
    fixed_u: hold compactness fixed (profile likelihood)."""
    rng = np.random.default_rng(seed)
    phase = (np.arange(len(counts)) + 0.5) / len(counts)
    best = None
    amp0 = np.log10(max(counts.max() - counts.min(), 1.0))
    b0 = np.log10(max(counts.min(), 1.0))
    for _ in range(n_starts):
        x0 = np.array([rng.uniform(0.15, 0.6), rng.uniform(0.1, 0.95), rng.uniform(0.2, 1.9), amp0, b0])
        if fixed_u is not None:
            f = lambda q: neg_loglike(np.array([fixed_u, *q]), phase, counts, nu, R_km)
            res = minimize(f, x0[1:], method="Nelder-Mead", options=dict(xatol=1e-4, fatol=1e-4, maxiter=4000))
            theta = np.array([fixed_u, *res.x])
        else:
            res = minimize(neg_loglike, x0, args=(phase, counts, nu, R_km), method="Nelder-Mead",
                           options=dict(xatol=1e-4, fatol=1e-4, maxiter=6000))
            theta = res.x
        if best is None or res.fun < best[0]:
            best = (res.fun, theta)
    return best


def profile_likelihood_u(counts, nu, u_grid, R_km=12.0, n_starts=25):
    """-2 Delta lnL versus fixed compactness u: shows what the profile alone can say about M/R."""
    nll = np.array([fit_profile(counts, nu, R_km, n_starts=n_starts, fixed_u=u)[0] for u in u_grid])
    return 2.0 * (nll - nll.min())


def cap_spot_flux(phase, u, inc, theta, zeta, nu=0.0, R_km=12.0, doppler=True, beam=0.0, n_pts=41):
    """Finite-size circular cap of angular radius zeta (radians), uniform temperature,
    built from n_pts point spots (centre + rings). Used to show how model misspecification
    (point spot fitted to an extended spot) biases the inferred compactness."""
    pts = [(0.0, 0.0)]
    for rad, n in ((0.5 * zeta, 10), (zeta, 20)):
        for a in np.linspace(0, 2 * np.pi, n, endpoint=False):
            pts.append((rad, a))
    tot = 0.0
    for rad, a in pts[:n_pts]:
        # displaced point in a local tangent frame: colatitude/longitude shifts
        th = np.clip(theta + rad * np.cos(a), 1e-3, np.pi - 1e-3)
        dphi = rad * np.sin(a) / max(np.sin(theta), 1e-3) / (2 * np.pi)
        tot = tot + single_spot_flux(np.asarray(phase) + dphi, u, inc, th, nu, R_km, doppler, beam)
    return tot / len(pts[:n_pts])


def two_cap_profile(phase, u, inc, theta, zeta, nu=0.0, R_km=12.0, doppler=True, beam=0.0):
    return (cap_spot_flux(phase, u, inc, theta, zeta, nu, R_km, doppler, beam)
            + cap_spot_flux(np.asarray(phase) + 0.5, u, inc, np.pi - theta, zeta, nu, R_km, doppler, beam))
