"""TOV structure equations, derived stellar quantities, and a fast numba path.

Geometric units internally: lengths in cm, m(r) := G M(r)/c^2 in cm,
P and eps multiplied by G/c^4 (cm^-2).

Two code paths
--------------
solve_star(eos, Pc)      readable scipy path; any EOS object with eps_of_P / cs2_of_P;
                         returns profiles, moment of inertia I and tidal deformability Lambda.
mr_curve_pp(eos, ...)    numba path for PiecewisePolytrope; ~1e3x faster; used in inference.
"""
import numpy as np
from scipy.integrate import solve_ivp
from numba import njit
from .constants import G, C, C2, MSUN, KM, G_OVER_C4, G_OVER_C2

FOUR_PI = 4.0 * np.pi


# ---------------------------------------------------------------------------
# readable path
# ---------------------------------------------------------------------------
def solve_star(eos, Pc, P_surf=1.0e19, r0=1.0e2, n_profile=600, extras=True, rtol=1e-9):
    """Integrate one star with central pressure Pc (dyn cm^-2).

    Returns a dict with M [Msun], R [km], compactness, profiles (r [km], P, eps, m [Msun], rho
    if available), and (extras=True) I [g cm^2], k2, Lambda.
    """
    Pc_g = Pc * G_OVER_C4
    Ps_g = P_surf * G_OVER_C4
    eps_c = float(eos.eps_of_P(Pc))
    epsc_g = eps_c * G_OVER_C4

    def eps_g(P_g):
        return float(eos.eps_of_P(P_g / G_OVER_C4)) * G_OVER_C4

    def cs2(P_g):
        return float(eos.cs2_of_P(P_g / G_OVER_C4))

    def rhs(r, y):
        m, P, lnj, om, u, ty = y
        e = eps_g(P)
        f = 1.0 - 2.0 * m / r
        dm = FOUR_PI * r * r * e
        dP = -(e + P) * (m + FOUR_PI * r**3 * P) / (r * r * f)
        dlnj = -FOUR_PI * r * (e + P) / f
        j = np.exp(lnj)
        dom = u / (r**4 * j)
        du = 16.0 * np.pi * r**4 * j * (e + P) / f * om
        if extras:
            nup = 2.0 * (m + FOUR_PI * r**3 * P) / (r * r * f)
            F = (1.0 - FOUR_PI * r * r * (e - P)) / f
            Q = (FOUR_PI * (5.0 * e + 9.0 * P + (e + P) / cs2(P)) / f
                 - 6.0 / (r * r * f) - nup * nup)
            dty = -ty * ty / r - ty * F / r - r * Q
        else:
            dty = 0.0
        return [dm, dP, dlnj, dom, du, dty]

    m0 = FOUR_PI / 3.0 * r0**3 * epsc_g
    P0 = Pc_g - 2.0 * np.pi / 3.0 * (epsc_g + Pc_g) * (Pc_g + epsc_g / 3.0) * r0**2
    u0 = 16.0 * np.pi / 5.0 * (epsc_g + Pc_g) * r0**5
    y0 = [m0, P0, 0.0, 1.0, u0, 2.0]

    def hit_surface(r, y):
        return y[1] - Ps_g
    hit_surface.terminal = True
    hit_surface.direction = -1

    sol = solve_ivp(rhs, (r0, 5.0e7), y0, events=hit_surface, rtol=rtol, atol=1e-30,
                    method="RK45", dense_output=True)
    if sol.status != 1:
        raise RuntimeError("surface not reached (check EOS / Pc)")
    R = sol.t_events[0][0]
    yR = sol.sol(R)
    M_g = yR[0]
    out = dict(M=M_g / G_OVER_C2 / MSUN, R=R / KM, C=M_g / R, Pc=Pc)

    rr = np.geomspace(r0, R, n_profile)
    Y = sol.sol(rr)
    out["r_km"] = rr / KM
    out["m_Msun"] = Y[0] / G_OVER_C2 / MSUN
    out["P"] = Y[1] / G_OVER_C4
    out["eps"] = np.array([float(eos.eps_of_P(p)) for p in out["P"]])
    if hasattr(eos, "rho_of_P"):
        out["rho"] = np.asarray(eos.rho_of_P(out["P"]))

    if extras:
        # moment of inertia (Hartle slow rotation)
        j_R = np.exp(yR[2])
        om_R, u_R = yR[3], yR[4]
        omp_R = u_R / (R**4 * j_R)
        J = R**4 * omp_R / 6.0
        Omega = om_R + 2.0 * J / R**3
        I_geo = J / Omega                         # cm^3 (G=c=1)
        out["I"] = I_geo * C2 / G                 # g cm^2
        # tidal Love number and deformability (Hinderer 2008; exterior matching)
        y = yR[5]
        Cc = M_g / R
        out["y_tidal"] = y
        if Cc < 1.0e-3:
            # Newtonian limit: the general formula suffers catastrophic cancellation
            k2 = (2.0 - y) / (2.0 * (3.0 + y))
        else:
            k2 = (8.0 * Cc**5 / 5.0 * (1 - 2 * Cc)**2 * (2 + 2 * Cc * (y - 1) - y)
                  / (2 * Cc * (6 - 3 * y + 3 * Cc * (5 * y - 8))
                     + 4 * Cc**3 * (13 - 11 * y + Cc * (3 * y - 2) + 2 * Cc**2 * (1 + y))
                     + 3 * (1 - 2 * Cc)**2 * (2 - y + 2 * Cc * (y - 1)) * np.log(1 - 2 * Cc)))
        out["k2"] = k2
        out["Lambda"] = 2.0 / 3.0 * k2 / Cc**5
    return out


def mr_curve(eos, Pc_grid, **kw):
    """(M, R) arrays by repeated solve_star (slow path, any EOS)."""
    M, R = [], []
    for Pc in Pc_grid:
        s = solve_star(eos, Pc, extras=False, **kw)
        M.append(s["M"]); R.append(s["R"])
    return np.array(M), np.array(R)


# ---------------------------------------------------------------------------
# fast numba path for piecewise polytropes
# ---------------------------------------------------------------------------
@njit(cache=True)
def _eps_cs2(P, K, Gam, a, Pb):
    i = 0
    n = Pb.shape[0]
    while i < n and P > Pb[i]:
        i += 1
    rho = (P / K[i]) ** (1.0 / Gam[i])
    eps = (1.0 + a[i]) * rho * C2 + P / (Gam[i] - 1.0)
    return eps, Gam[i] * P / (eps + P)


@njit(cache=True)
def _tov_pp(Pc, K, Gam, a, Pb, P_surf):
    """RK4 TOV integration in cgs-converted geometric units; returns (M_sun, R_km)."""
    gc4 = G / C**4
    Pg = Pc * gc4
    Psg = P_surf * gc4
    eps_c, _ = _eps_cs2(Pc, K, Gam, a, Pb)
    eg = eps_c * gc4
    r = 1.0e2
    m = FOUR_PI / 3.0 * r**3 * eg
    P = Pg - 2.0 * np.pi / 3.0 * (eg + Pg) * (Pg + eg / 3.0) * r * r
    for _ in range(200000):
        # derivatives at (r, m, P)
        # --- k1
        e1 = _eps_cs2(P / gc4, K, Gam, a, Pb)[0] * gc4
        f = 1.0 - 2.0 * m / r
        dP1 = -(e1 + P) * (m + FOUR_PI * r**3 * P) / (r * r * f)
        dm1 = FOUR_PI * r * r * e1
        h = min(2.0e4, 0.02 * P / abs(dP1), max(1.0e2, 0.01 * r))
        # --- k2
        r2, m2, P2 = r + 0.5 * h, m + 0.5 * h * dm1, P + 0.5 * h * dP1
        e2 = _eps_cs2(max(P2, 1e-300) / gc4, K, Gam, a, Pb)[0] * gc4
        f2 = 1.0 - 2.0 * m2 / r2
        dP2 = -(e2 + P2) * (m2 + FOUR_PI * r2**3 * P2) / (r2 * r2 * f2)
        dm2 = FOUR_PI * r2 * r2 * e2
        # --- k3
        m3, P3 = m + 0.5 * h * dm2, P + 0.5 * h * dP2
        e3 = _eps_cs2(max(P3, 1e-300) / gc4, K, Gam, a, Pb)[0] * gc4
        f3 = 1.0 - 2.0 * m3 / r2
        dP3 = -(e3 + P3) * (m3 + FOUR_PI * r2**3 * P3) / (r2 * r2 * f3)
        dm3 = FOUR_PI * r2 * r2 * e3
        # --- k4
        r4, m4, P4 = r + h, m + h * dm3, P + h * dP3
        e4 = _eps_cs2(max(P4, 1e-300) / gc4, K, Gam, a, Pb)[0] * gc4
        f4 = 1.0 - 2.0 * m4 / r4
        dP4 = -(e4 + P4) * (m4 + FOUR_PI * r4**3 * P4) / (r4 * r4 * f4)
        dm4 = FOUR_PI * r4 * r4 * e4
        Pn = P + h / 6.0 * (dP1 + 2 * dP2 + 2 * dP3 + dP4)
        mn = m + h / 6.0 * (dm1 + 2 * dm2 + 2 * dm3 + dm4)
        if Pn <= Psg:
            # linear interpolation to P = P_surf
            t = (P - Psg) / (P - Pn)
            rs = r + t * h
            ms = m + t * (mn - m)
            return ms / (G / C**2) / MSUN, rs / KM
        r += h
        m, P = mn, Pn
        if 2.0 * m / r >= 1.0:
            return np.nan, np.nan
    return np.nan, np.nan


@njit(cache=True)
def _mr_curve_pp(Pc_grid, K, Gam, a, Pb, P_surf):
    n = Pc_grid.shape[0]
    M = np.empty(n)
    R = np.empty(n)
    for i in range(n):
        M[i], R[i] = _tov_pp(Pc_grid[i], K, Gam, a, Pb, P_surf)
    return M, R


def mr_curve_pp(eos, log_Pc_min=33.0, log_Pc_max=36.7, n=60, P_surf=1.0e19, causal=True):
    """Fast M(R) curve for a PiecewisePolytrope. Returns (Pc, M, R) up to M_max.

    The curve is cut at the first maximum of M(Pc) (end of the stable branch) and, if
    causal=True, also where the sound speed reaches c (central pressures above that are
    unphysical: standard practice is to truncate the sequence there).
    NOTE: the grid must reach the true maximum; for SLy M_max=2.048 occurs at
    Pc = 1.4e36 dyn/cm^2, which is why the default upper limit is 10**36.7.
    """
    Pc = np.logspace(log_Pc_min, log_Pc_max, n)
    if causal:
        Pc = Pc[eos.cs2_of_P(Pc) < 1.0]
    K, Gam, a, Pb = eos.numba_arrays()
    M, R = _mr_curve_pp(Pc, K, Gam, a, Pb, P_surf)
    ok = np.isfinite(M)
    Pc, M, R = Pc[ok], M[ok], R[ok]
    if len(M) < 3:
        return Pc, M, R
    imax = int(np.argmax(M))
    return Pc[: imax + 1], M[: imax + 1], R[: imax + 1]
