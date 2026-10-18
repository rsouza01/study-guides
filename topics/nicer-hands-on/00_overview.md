# NICER Hands-On: From Raw Photons to Neutron-Star Interiors (a coding-first guide)

**Goal:** get your hands on real NICER data and on the published NICER products, make plots you can compare with the literature, and push all the way to *inferring neutron-star structure* (the equation of state, $R_{1.4}$, central density, crust thickness, $I$, $\Lambda$) from NICER mass-radius measurements.
**Style:** same skeleton as your other guides (why it matters, diagnostic, topics, tasks, exercises with expected results, pitfalls, gates, cheat sheet), but **the work is code**: a small tested Python package (`code/nicerkit/`), runnable example scripts (`code/examples/`), and modules that tell you what to run, what you should see, and what to think about.
**Time:** about 40 to 60 hours of focused work for Levels 0 to 7 (about 8 to 12 weeks at two sessions a week); Level 8 (X-PSI) is open-ended.

---

## 1. Can you infer the star's structure from NICER data? (the honest answer)

**Yes, in two distinct steps, and they have very different costs.**

| Step | What it is | Cost | In this guide |
| --- | --- | --- | --- |
| **A. Photons $\to$ $(M,R)$** | *Pulse-profile modeling* (PPM): fit relativistic ray-traced hot-spot models to the phase- and energy-resolved NICER photons, jointly with XMM-Newton spectra and radio-timing priors, to get a joint posterior of mass and radius | **Very expensive.** The 2026 reanalysis of PSR J0030+0451 quotes about 4.8 million core-hours for its most complex headline run (PDT-U, 10,000 live points); XMM and NICER must be modeled together | You build a *toy* version (Level 4) to see why it works and where it is fragile; you can run the real code (X-PSI) on injected data (Level 8) |
| **B. $(M,R)$ $\to$ EOS $\to$ structure** | Treat the published $(M,R)$ posteriors as data, parametrise the dense-matter EOS, solve TOV for each EOS, and sample the EOS posterior. Everything about the star's interior then follows: $P(r)$, $\rho(r)$, $\rho_c$, crust thickness, $I$, tidal deformability, maximum mass | **Cheap.** Hours on a laptop | Levels 5 to 7 (full, tested code) |

So the feasible path for you is: **retrieve and look at real NICER photons (Levels 1 to 3) to understand what the data *are*, use the collaborations' published posteriors for the radius information (Level 0), and do the EOS and structure inference yourself (Levels 5 to 7).** That is also how most of the field's EOS papers work.

## 2. What is verified and what is not

I checked the following against live sources while writing (as of October 2026) and tested all offline code on synthetic data in a sandbox **that could not reach HEASARC or Zenodo**:

- **Verified from HEASARC/NICER documentation:** the archive catalog is `nicermastr`; the standard processing task is `nicerl2` (always reprocess archive data with up-to-date software and calibration); `nicerl3-spect` and `nicerl3-lc` make products; `astroquery.heasarc` and `heasoftpy` are supported routes; NICER XTI has 56 concentrator/detector pairs working in 0.2 to 12 keV; the example archive path is `https://heasarc.gsfc.nasa.gov/FTP/nicer/data/obs/2021_11/4142010107/`.
- **Verified from papers/Zenodo (Kini et al. 2026, Mauviard et al. 2025, Salmi et al. 2024):** the headline $(M,R)$ results and the existence and layout of the public Zenodo releases (Module 02 has the table). The J0030 2026 reproduction package is **15.5 GB**; the J0614 posterior package is **3.4 MB**.
- **Tested here (pytest, all green):** EOS and TOV (constant-density exact interior; Newtonian $n=1$ polytrope $I/MR^2=0.261$ and $k_2=0.26$; SLy gives $M_{\rm max}=2.05\,M_\odot$, $R_{1.4}=11.7$ km, $\Lambda_{1.4}=294$), KDE likelihoods, EOS injection-recovery, Z$^2$ and H-tests, burst finder, the toy pulse-profile model, and FITS reading (on synthetic files).
- **NOT tested against live servers:** every network function (`find_obs`, `download_obs`, `zenodo_*`) and every HEASoft command in Module 04. They follow the documented interfaces; read errors carefully, check `nicerl2 help`, and fix as needed.
- **From memory (verify):** target coordinates in `archive.TARGETS` (check with SIMBAD); the column order inside the older Zenodo posterior files (always print the first rows and read the README; `mr.sanity_check` catches swapped columns).

## 3. The ladder

| Level | Module | What you do | Needs |
| --- | --- | --- | --- |
| 0 | 02 | Load the published NICER $(M,R)$ posteriors, reproduce the famous $M$-$R$ plot, compare sources | Zenodo files (small ones: MB) |
| 1 | 03, 04 | Query the archive, download one observation, inspect the FITS, run `nicerl2`, barycentre | HEASARC + HEASoft |
| 2 | 05, 06 | Light curves and spectra; find X-ray bursts; blind period search and pulse profile of the Crab | one bright source |
| 3 | 07 | Phase-energy matrix of a millisecond pulsar (the "Figure 1" of the PPM papers) | timing solution, PINT |
| 4 | 08 | Toy pulse-profile model: how compactness shapes the profile; why $M$-$R$ is degenerate; how a wrong spot model biases it | nothing (offline) |
| 5 | 09 | TOV from scratch; EOS families; the interior of a $1.4\,M_\odot$ star | nothing (offline) |
| 6 | 10 | EOS inference from $(M,R)$ posteriors; injection-recovery; then real data | Level 0 files |
| 7 | 11 | From an EOS posterior to profiles, crust thickness, $I$, $\Lambda$ | Level 6 chain |
| 8 | 12 | X-PSI, hot-spot systematics, multi-messenger additions, where this connects to your other guides | optional |
| capstone | 13 | End-to-end notebook and short report | everything |

You can do Levels 4, 5 and 6 (injection) **today with no data at all**; they are the fastest way to see the logic of the whole chain.

## 4. Repository layout

```
nicer-hands-on/
├── 00_overview.md ... 13_capstone.md, 99_appendix_registry_and_troubleshooting.md
├── figures/                       reference plots produced by the demo scripts
└── code/
    ├── nicerkit/                  eos, tov, mr, infer, ppm, fold, bursts, archive
    ├── tests/                     pytest suite (run: python -m pytest -q)
    ├── examples/                  ex02 ... ex12 (percent-cell scripts: run as scripts or in VS Code/Jupyter)
    └── env/                       environment.yml, requirements.txt
```

Every example has a `--demo` mode (synthetic data) so you can check your environment before touching real data.

## 5. Operating rules

1. **Look at the data before modeling it.** Every module starts with a plot.
2. **Reproduce something known** at each level (the Crab period, a published radius, SLy's $M_{\rm max}$) before trusting your code on anything new.
3. **Injection-recovery before inference:** generate fake data from a known truth, recover it, then run on the real thing.
4. **Keep a lab notebook** (`notes/log.md`): command, versions (HEASoft, CALDB, nicerkit commit), what you saw, what surprised you.
5. **Cite the data:** the Zenodo records are CC-BY 4.0; credit the authors (list in Module 02).

## 6. How this connects to your other guides

| Here | There |
| --- | --- |
| Module 09 (TOV, piecewise polytropes, SLy crust) | Compact-objects guide Modules 07 to 08; your `tov-solver.py` (cross-check results against `nicerkit.tov`) |
| Module 10 (EOS parametrisation, likelihood from $M$-$R$) | Compact-objects guide Module 19 (inference); thermodynamics guide Module 15 (causality, $c_s^2$) |
| Module 11 (crust thickness, $\Delta I/I$ analogue) | Nuclear-QHD guide Modules 19, 20, 27 (inner crust, pasta, unified EOS): swap in your own unified EOS via `TabulatedEOS` |
| Module 08 (light bending) | Electrodynamics and mechanics guides (null geodesics are the same variational problem as ray optics in curved space) |
| Module 12 (hot-spot systematics) | Compact-objects guide Modules 12, 16 (emission, atmospheres) |
