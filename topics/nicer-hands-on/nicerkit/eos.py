"""Equations of state.

PiecewisePolytrope implements the Read et al. (2009) parametrisation:
a fixed SLy-like crust (four polytropic segments) joined to a three-segment
core with free parameters (log10 p1, Gamma1, Gamma2, Gamma3) and fixed
dividing densities rho1 = 10**14.7 and rho2 = 10**15.0 g cm^-3.

Units: cgs.  K values below are the published ones divided by nothing;
P = K * c^2 * rho^Gamma in dyn cm^-2 with rho in g cm^-3 (the published
tables quote K in units of c^2).  Continuity of P at the crust boundaries
is checked in the tests, which validates these constants.
"""
from dataclasses import dataclass
import numpy as np
from .constants import C2

# Read et al. (2009), Table II: SLy-like crust, K in units of c^2
_CRUST_K = np.array([6.80110e-9, 1.06186e-6, 5.32697e1, 3.99874e-8]) * C2
_CRUST_GAMMA = np.array([1.58425, 1.28733, 0.62223, 1.35692])
_CRUST_RHO_BOUNDS = np.array([2.44034e7, 3.78358e11, 2.62780e12])

RHO1 = 10.0 ** 14.7
RHO2 = 10.0 ** 15.0

# Read et al. (2009) Table III: SLy core parameters
SLY_PARAMS = dict(log_p1=34.384, gamma1=3.005, gamma2=2.988, gamma3=2.851)


@dataclass
class PiecewisePolytrope:
    log_p1: float
    gamma1: float
    gamma2: float
    gamma3: float

    def __post_init__(self):
        p1 = 10.0 ** self.log_p1
        k1 = p1 / RHO1 ** self.gamma1
        k2 = p1 / RHO1 ** self.gamma2
        k3 = k2 * RHO2 ** (self.gamma2 - self.gamma3)
        # crust / core junction: crust segment 3 meets core segment 1
        lg = (np.log(k1) - np.log(_CRUST_K[3])) / (_CRUST_GAMMA[3] - self.gamma1)
        self.rho0 = float(np.exp(lg))
        self.valid = bool(np.isfinite(self.rho0) and 1.0e13 < self.rho0 < RHO1)
        if not self.valid:
            self.rho0 = 1.0e14  # harmless placeholder
        K = np.concatenate([_CRUST_K[:3], [_CRUST_K[3]], [k1, k2, k3]])
        G = np.concatenate([_CRUST_GAMMA[:3], [_CRUST_GAMMA[3]], [self.gamma1, self.gamma2, self.gamma3]])
        # segments: 0,1,2,3 (crust), 4,5,6 (core). Boundaries in density:
        rb = np.array(list(_CRUST_RHO_BOUNDS) + [self.rho0, RHO1, RHO2])
        self.K, self.Gam, self.rho_b = K, G, rb
        # pressure at boundaries (use the upper segment's law; continuous)
        self.P_b = np.array([K[i + 1] * rb[i] ** G[i + 1] for i in range(len(rb))])
        # energy-density offsets a_i for continuity of epsilon
        a = np.zeros(len(K))
        for i in range(1, len(K)):
            rho_b = rb[i - 1]
            a[i] = a[i - 1] + self.P_b[i - 1] * (1.0 / (G[i - 1] - 1.0) - 1.0 / (G[i] - 1.0)) / (rho_b * C2)
        self.a = a

    # --- helpers -----------------------------------------------------------
    def _segment_of_P(self, P):
        return np.searchsorted(self.P_b, P)       # 0..6

    def rho_of_P(self, P):
        P = np.asarray(P, dtype=float)
        i = self._segment_of_P(P)
        return (np.maximum(P, 1e-300) / self.K[i]) ** (1.0 / self.Gam[i])

    def eps_of_P(self, P):
        """total energy density (erg cm^-3) including rest mass."""
        P = np.asarray(P, dtype=float)
        i = self._segment_of_P(P)
        rho = (np.maximum(P, 1e-300) / self.K[i]) ** (1.0 / self.Gam[i])
        return (1.0 + self.a[i]) * rho * C2 + P / (self.Gam[i] - 1.0)

    def cs2_of_P(self, P):
        """(speed of sound / c)^2 = Gamma P / (eps + P)."""
        P = np.asarray(P, dtype=float)
        i = self._segment_of_P(P)
        return self.Gam[i] * P / (self.eps_of_P(P) + P)

    def P_of_rho(self, rho):
        rho = np.asarray(rho, dtype=float)
        i = np.searchsorted(self.rho_b, rho)
        return self.K[i] * rho ** self.Gam[i]

    # arrays for numba routines
    def numba_arrays(self):
        return (self.K.copy(), self.Gam.copy(), self.a.copy(), self.P_b.copy())


def sly():
    """SLy-like piecewise polytrope (Read et al. 2009)."""
    return PiecewisePolytrope(**SLY_PARAMS)


@dataclass
class TabulatedEOS:
    """EOS from arrays (P, eps) in cgs; log-log interpolation. Use for your own tables
    (e.g. an RMF/Skyrme EOS built in the nuclear-qhd guide)."""
    P: np.ndarray
    eps: np.ndarray

    def __post_init__(self):
        o = np.argsort(self.P)
        self.P, self.eps = np.asarray(self.P)[o], np.asarray(self.eps)[o]
        self._lp, self._le = np.log(self.P), np.log(self.eps)

    def eps_of_P(self, P):
        return np.exp(np.interp(np.log(P), self._lp, self._le))

    def cs2_of_P(self, P, h=1e-3):
        lp = np.log(P)
        e1 = np.exp(np.interp(lp + h, self._lp, self._le))
        e0 = np.exp(np.interp(lp - h, self._lp, self._le))
        P1, P0 = np.exp(lp + h), np.exp(lp - h)
        return (P1 - P0) / (e1 - e0)


@dataclass
class SimplePolytrope:
    """P = K rho^Gamma (cgs, rho in g cm^-3), eps = rho c^2 + P/(Gamma-1).
    Used for tests (Gamma=2: n=1 Newtonian polytrope) and for teaching."""
    K: float
    Gamma: float = 2.0

    def rho_of_P(self, P):
        return (np.maximum(np.asarray(P, float), 1e-300) / self.K) ** (1.0 / self.Gamma)

    def eps_of_P(self, P):
        P = np.asarray(P, float)
        return self.rho_of_P(P) * C2 + P / (self.Gamma - 1.0)

    def cs2_of_P(self, P):
        P = np.asarray(P, float)
        return self.Gamma * P / (self.eps_of_P(P) + P)


@dataclass
class ConstantDensity:
    """Incompressible fluid, eps = const (for the exact Schwarzschild interior test)."""
    eps0: float

    def eps_of_P(self, P):
        return np.full_like(np.asarray(P, float), self.eps0)

    def cs2_of_P(self, P):
        return np.full_like(np.asarray(P, float), 1.0e30)   # "infinite" sound speed
