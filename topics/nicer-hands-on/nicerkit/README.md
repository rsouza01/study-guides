It's a small Python package I wrote from scratch for this guide, called `nicerkit`, plus runnable example scripts and tests. It is not official NICER or HEASARC software and it does not come from any of the NICER collaboration's tools. It sits next to those tools and handles the parts that can be done in plain Python.

**What each piece does**

- **`eos.py` and `tov.py`.** These implement the equation of state and stellar structure. I coded the piecewise-polytrope EOS parametrisation of Read et al. (2009), with their published SLy-like crust constants. The TOV solver is mine, including the moment of inertia and tidal deformability. A fast numba version exists so thousands of EOS can be evaluated.
- **`mr.py` and `infer.py`.** These load mass-radius posterior samples, build smoothed density grids from them, and run the EOS inference. The likelihood and prior choices are mine, following the method in the NICER-EOS literature (Raaijmakers et al. 2019 style). It is not the collaborations' own inference pipeline.
- **`fold.py` and `bursts.py`.** These are standard timing statistics (Z² and H-test, FFT search, folding, phase-energy matrix) and a simple burst finder with a decay fit.
- **`ppm.py`.** This is a deliberately simplified toy pulse-profile model: point or circular spots, a light-bending approximation and rough Doppler boosting. It is for learning why compactness is measurable and fragile. It is not a substitute for X-PSI, which is the real pulse-profile modeling code.
- **`archive.py`.** This wraps `astroquery.heasarc`, a wget call for the archive and the Zenodo API, and reads FITS event files with astropy.
- **`examples/`.** These are short scripts, one per level of the guide, each with a `--demo` mode that uses synthetic data.
- **`tests/`.** The 22 pytest checks include exact results: an incompressible-star solution, a Newtonian polytrope with I/MR² = 0.261 and k₂ = 0.26, and SLy M_max = 2.05.

**What the code is not**

- It does not do the heavy step of turning photons into mass and radius. That needs the collaborations' released posteriors, or X-PSI.
- The real NICER data processing happens in HEASoft (`nicerl2`, `barycorr`), which you install separately. My code only reads the files it produces.

**Which parts you can trust**

- The physics and statistics code was run and tested here on synthetic data and against known results.
- The `archive.py` code that talks to the live HEASARC and Zenodo servers has never been run, because my sandbox couldn't reach them. It follows the documented interfaces, so expect to fix small errors on first use.
- The example scripts for loading real posterior files (`ex02`, `ex11`) assume the file column order you specify. Check each file's README.

If you'd like, I can walk through any one file in detail, or you can read `eos.py` and `tov.py` first, since everything else builds on them.
