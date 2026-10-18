"""Physical constants (cgs) and conversion helpers."""
import numpy as np

G = 6.67430e-8            # cm^3 g^-1 s^-2
C = 2.99792458e10         # cm s^-1
C2 = C * C
MSUN = 1.98847e33         # g
KM = 1.0e5                # cm
M_U = 1.66053907e-24      # g (atomic mass unit)
HBARC_MEV_FM = 197.327    # MeV fm
MEV_PER_FM3_TO_CGS_P = 1.602176634e33   # dyn cm^-2 per MeV fm^-3
N0 = 0.16                 # fm^-3 (nuclear saturation density, convention)
RHO_N0 = N0 * 1.0e39 * M_U  # g cm^-3 at n0 using the atomic mass unit (~2.66e14)

# geometric-unit factors: P_geo [cm^-2] = P_cgs * G / c^4 ; M_geo [cm] = G M / c^2
G_OVER_C4 = G / C**4
G_OVER_C2 = G / C**2


def schwarzschild_radius_km(m_sun):
    """2GM/c^2 in km."""
    return 2.0 * G * m_sun * MSUN / C2 / KM


def compactness(m_sun, r_km):
    """GM/(R c^2)."""
    return G * m_sun * MSUN / C2 / (r_km * KM)
