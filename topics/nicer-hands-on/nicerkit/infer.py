"""EOS inference from mass-radius posteriors (piecewise-polytrope parametrisation).

Likelihood for one source (Raaijmakers et al. 2019 style):
    L_j(EOS) = integral dM  p_j(M, R_EOS(M))      over the stable branch, M_lo <= M <= M_max(EOS)
where p_j is the (KDE-smoothed) joint posterior from the NICER analysis.  The NICER priors
were flat in (M, R) (with a radio-timing Gaussian on M for binary pulsars, which is part of the
posterior and must NOT be divided out when the EOS prior is flat in M), so p_j is proportional
to the likelihood.  See Module 10 for the caveats (hot-spot model dependence, prior volume).
"""
from dataclasses import dataclass
import numpy as np
from .eos import PiecewisePolytrope
from .tov import mr_curve_pp, solve_star

BOUNDS = dict(log_p1=(33.8, 35.0), gamma1=(1.5, 4.5), gamma2=(0.5, 6.0), gamma3=(0.5, 6.0))
NAMES = list(BOUNDS)
M_LO = 1.0


@dataclass
class Source:
    name: str
    density: object        # GridDensity (or any callable p(M, R))
    weight: float = 1.0    # use <1 to temper a source you distrust (see Module 12)


def in_bounds(theta):
    return all(BOUNDS[n][0] <= t <= BOUNDS[n][1] for n, t in zip(NAMES, theta))


def make_eos(theta):
    eos = PiecewisePolytrope(*theta)
    return eos if eos.valid else None


def causal(eos, Pc_max, n=64):
    P = np.logspace(33.0, np.log10(Pc_max), n)
    return bool(np.all(eos.cs2_of_P(P) < 1.0))


def log_likelihood(theta, sources, M_min_max=1.97, n_pc=40, return_curve=False, normalise_mass_prior=True):
    """log L(theta). Returns -inf for invalid / acausal / too-soft EOS."""
    if not in_bounds(theta):
        return -np.inf
    eos = make_eos(theta)
    if eos is None:
        return -np.inf
    Pc, M, R = mr_curve_pp(eos, log_Pc_min=33.2, log_Pc_max=36.7, n=n_pc, causal=True)
    if len(M) < 4 or M.max() < M_min_max:
        return -np.inf
    # the stable branch: keep strictly increasing M
    keep = np.concatenate([[True], np.diff(M) > 0])
    Ms, Rs = M[keep], R[keep]
    if len(Ms) < 4:
        return -np.inf
    Mgrid = np.linspace(max(M_LO, Ms.min()), Ms.max(), 80)
    Rgrid = np.interp(Mgrid, Ms, Rs)
    lnL = 0.0
    for s in sources:
        p = s.density(Mgrid, Rgrid)
        L = np.trapezoid(p, Mgrid)
        if normalise_mass_prior:
            # pulsar masses ~ uniform on [M_lo, Mmax(EOS)]: an EOS with a larger Mmax spreads the same
            # prior mass over a bigger range (Occam factor). Without this, high-Mmax EOS are favoured.
            L = L / (Mgrid[-1] - Mgrid[0])
        if L <= 0.0:
            return -np.inf
        lnL += s.weight * np.log(L)
    return (lnL, Ms, Rs) if return_curve else lnL


def log_posterior(theta, sources, **kw):
    return log_likelihood(theta, sources, **kw)   # flat prior inside BOUNDS


def derived(theta, m_ref=1.4):
    """Quantities of interest for one EOS sample."""
    eos = make_eos(theta)
    if eos is None:
        return None
    Pc, M, R = mr_curve_pp(eos, n=90)
    if M.max() < m_ref:
        return None
    imax = int(np.argmax(M))
    out = dict(Mmax=M[imax], R_at_Mmax=R[imax], R14=float(np.interp(m_ref, M, R)),
               Pc_max=Pc[imax])
    out["rho_c_max"] = float(eos.rho_of_P(Pc[imax]))
    out["P_2n0"] = float(eos.P_of_rho(2 * 2.66e14))
    out["cs2_max"] = float(eos.cs2_of_P(Pc[imax]))
    return out


def run_emcee(sources, theta0, nwalkers=24, nsteps=800, seed=1, progress=True, **kw):
    """Convenience wrapper around emcee. theta0: a valid starting point (e.g. SLy)."""
    import emcee
    rng = np.random.default_rng(seed)
    ndim = len(theta0)
    scale = np.array([0.05, 0.1, 0.1, 0.1])
    p0 = []
    while len(p0) < nwalkers:
        t = np.array(theta0) + scale * rng.normal(size=ndim)
        if np.isfinite(log_posterior(t, sources, **kw)):
            p0.append(t)
    sampler = emcee.EnsembleSampler(nwalkers, ndim, log_posterior, args=(sources,), kwargs=kw)
    sampler.run_mcmc(np.array(p0), nsteps, progress=progress)
    return sampler
