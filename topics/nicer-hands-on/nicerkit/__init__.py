"""nicerkit: small, readable tools for NICER neutron-star work.

Modules
-------
constants   physical constants and unit conversions (cgs)
eos         piecewise-polytrope equations of state with an SLy-like crust
tov         TOV solver, structure profiles, moment of inertia, tidal deformability
mr          mass-radius posterior samples: loading, KDE grids, credible contours
infer       EOS inference from mass-radius posteriors (likelihood + sampler helpers)
ppm         toy pulse-profile model (light bending + Doppler), for intuition only
fold        timing statistics (Z^2_m, H-test), folding, phase-energy matrices
bursts      thermonuclear X-ray burst finder for light curves
archive     HEASARC query/download helpers and Zenodo downloader (need network)
"""
__version__ = "0.1.0"
