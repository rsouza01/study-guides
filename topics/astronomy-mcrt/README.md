# Monte Carlo Radiative Transfer, Implemented: a Toy Star from Core to Detector

Forgan's seminar notes, translated into code, and extended into a working simulator of a star: photons born in the core, their way to the surface through radiative and convective layers, and their detection at a distance.

- **Source text:** D. Forgan, *An Introduction to Monte Carlo Radiative Transfer*, Pedagogical Seminar, Institute for Astronomy, Edinburgh, 2009 (22 pp.). Cited below as "Forgan §x, eq (n)". Section and equation numbers were checked against the PDF.
- **Continuation of:** the `fa-photometry` guide (Karttunen, *Fundamental Astronomy*, Chapters 4–5). References of the form **PH-nn** mean module nn of that guide (for example PH-18 is `18-plancks-law.md`).
- **Plan:** 25 modules, MC-01 to MC-25. The first eight build Forgan's toolbox. The next eleven build the star and make Monte Carlo usable in it. The next five add the atmosphere, the spectrum, the detector, the inverse problem and the capstone (MC-24). MC-25 is optional: it runs the engine on all CPU cores and on a GPU.

---

## How each module works

- **Session A: read.** The exact section and equations of Forgan, the matching module of the previous guide, and where to read more. Every formula that is not in Forgan comes with its derivation, to see once.
- **Session B: do.** Numbered problems with complete statements. You write the code.
- **Text → code table.** Forgan's equation on the left, the line of code on the right. Misprints in the text are flagged here.
- **Contract.** The module and function names your package must provide, with signatures.
- **Acceptance test.** A python block that checks your code with seeded random numbers and statistical tolerances.
- **Checkpoints.** Numbers your code should reproduce.
- **Done when.** Statements about understanding. Nothing is a recall test; a cheat sheet is fine.

---

## Setup

- Python 3.10 or newer.
- Packages: `numpy`, `scipy`, `numba`, `matplotlib`.

```bash
pip install numpy scipy numba matplotlib
```

- Optional, for MC-25 only: an NVIDIA GPU and the `numba-cuda` package (`pip install numba-cuda[cu12]`, or `[cu13]` for CUDA 13). MC-25 also works without a GPU, in numba's CUDA simulator.

**Layout.** You build one package, `starmc/`, module by module. The tests import from it:

```text
your-repo/
  starmc/
    __init__.py
    consts.py      freepath.py    sampling.py    emission.py    planck.py
    scatter.py     grid.py        shells.py      transport.py   detector.py
    stats.py       star.py        opacity.py     thermal.py     convection.py
    radeq.py       budget.py      scaling.py     mrw.py         engine.py
    atmosphere.py  lines.py       photometry.py  inverse.py     pipeline.py
    parallel.py    (MC-25, optional)
  tools/
    extract_tests.py
  modules/
    MC-01-....md  ...
```

**Running the tests.**

```bash
python tools/extract_tests.py            # every module
python tools/extract_tests.py MC-05      # one module
python tools/extract_tests.py --pkg /path/containing/starmc MC-17
```

- A test is a fenced python block whose first line is `# acceptance-test`.
- The test of MC-25 runs its GPU part only if numba finds a CUDA device. Otherwise it prints that the part was skipped. With `NUMBA_ENABLE_CUDASIM=1` set in the environment it runs that part in the simulator instead, with fewer packets.
- The tests are statistical: they use fixed seeds and tolerances of a few standard errors. If one fails narrowly with a correct implementation, change the seed in your own code before suspecting the physics.

**Units.** The package is in **cgs** (stellar-structure convention). `PH-xx` were in SI. `starmc/consts.py` provides `G, c, k, h, sigma, a_rad, m_u, Msun, Rsun, Lsun, yr, pc, AU, sigma_T, eV, m_e, e_esu`, with $L_\odot=3.828\times10^{33}$ erg s⁻¹. The detector module converts to SI where magnitudes need it.

**Symbols.** Forgan writes $\zeta$ for a uniform random number in $[0,1)$. The Riemann $\zeta(s)$ also appears (Planck sampler, MC-03; $\eta(2)$ in MC-18). Here the random number is always written $\zeta$ without an argument and the function always has one: $\zeta(4)$.

---

## The modules

### Part I: Forgan's toolbox (§1–§8)

| # | Module | Forgan | Link to the previous guide |
|---|---|---|---|
| 01 | [Transfer equation and the free path](modules/MC-01-transfer-equation-and-free-path.md) | §1.1, §1.2 (eqs 1–13) | PH-27 |
| 02 | [Sampling: inverse CDF and accept/reject](modules/MC-02-sampling-cdf-and-accept-reject.md) | §2, §2.1 (eqs 14–16) | |
| 03 | [Emitting packets, directions, Planck](modules/MC-03-emitting-packets-and-planck.md) | §3 (eqs 17–22) | PH-18, PH-19 |
| 04 | [Scattering and phase functions](modules/MC-04-scattering-and-phase-functions.md) | §1.2, §5 (eqs 5–7, 36–48) | |
| 05 | [Rays through grids and shells](modules/MC-05-rays-grids-and-shells.md) | §4 (eqs 23–35) | |
| 06 | [The packet loop](modules/MC-06-the-packet-loop.md) | §2, §4.3, §5 | |
| 07 | [Outputs, images, flux](modules/MC-07-outputs-images-and-flux.md) | §6 (eqs 49–52) | PH-04, PH-07, PH-08 |
| 08 | [Errors and cost](modules/MC-08-errors-and-cost.md) | §7, §8 (eqs 53–59) | |

### Part II: the star, and why direct Monte Carlo fails in it

| # | Module | Forgan | Link to the previous guide |
|---|---|---|---|
| 09 | [A toy star: the $n=3$ polytrope](modules/MC-09-toy-star-polytrope.md) | not in Forgan | PH-19, PH-22 |
| 10 | [Opacity in a stellar interior](modules/MC-10-opacity.md) | §1.1, §9.1.1 | PH-12 to PH-17 |
| 11 | [Radiative diffusion, $T(r)$](modules/MC-11-radiative-diffusion.md) | (§9.1 in MC-14) | PH-27 |
| 12 | [Nuclear energy as a diffuse source](modules/MC-12-nuclear-energy-sources.md) | §3 eq (17) | |
| 13 | [Convection, Schwarzschild](modules/MC-13-convection.md) | not in Forgan | |
| 14 | [Radiative equilibrium by Monte Carlo](modules/MC-14-radiative-equilibrium-by-monte-carlo.md) | §9.1, §9.1.1 (eqs 60–69) | PH-19 |
| 15 | [Re-emission, frequency adjustment](modules/MC-15-reemission-and-frequency-adjustment.md) | §9.1.2 (eqs 70–74) | PH-18 |
| 16 | [Why direct MCRT fails in a star](modules/MC-16-why-direct-mcrt-fails.md) | §8 | |
| 17 | [Opacity scaling](modules/MC-17-opacity-scaling.md) | not in Forgan | |
| 18 | [The modified random walk](modules/MC-18-modified-random-walk.md) | not in Forgan | |
| 19 | [The star engine](modules/MC-19-the-star-engine.md) | §2, §4–§5, §9.1 | |

### Part III: surface, spectrum, detection, inference

| # | Module | Forgan | Link to the previous guide |
|---|---|---|---|
| 20 | [The surface layer: a grey atmosphere](modules/MC-20-grey-atmosphere.md) | §6, §9.1 | PH-27 |
| 21 | [Spectrum and the Balmer lines](modules/MC-21-spectrum-and-balmer-lines.md) | §1.1, §6 | PH-12 to PH-17, PH-25 |
| 22 | [Detecting the star](modules/MC-22-detecting-the-star.md) | §6, §7 | PH-04, PH-05, PH-07, PH-08, PH-24 |
| 23 | [The inverse problem](modules/MC-23-inverse-problem.md) | §6, §7 | PH-22, PH-24, PH-25 |
| 24 | [Capstone: the functioning star](modules/MC-24-capstone-the-functioning-star.md) | all | all |

### Part IV: scaling (optional)

| # | Module | Forgan | Link to the previous guide |
|---|---|---|---|
| 25 | [Scaling the engine: many cores and a GPU](modules/MC-25-scaling-cores-and-gpu.md) | §8 (cost) only | |

Suggested order: 01 to 08 in sequence; then 09 to 13; then 14 to 19; then 20 to 24. Each module's contract builds on the earlier ones. MC-25 comes after the capstone and nothing depends on it.

---

## Misprints and errors in Forgan (2009), found while implementing

Checked against the page images of the PDF. Each is repeated in the module where the equation is used.

| Eq | What the text says | What is right | Module |
|---|---|---|---|
| (11)–(12) | $P(x)=1-\rho\kappa x=e^{-\tau}$ | $\lim_{N\to\infty}(1-\rho\kappa x/N)^N=e^{-\tau}$; the middle term is only the first-order expansion | MC-01 |
| (32) | quadratic in $s$ without the factor 2 | $s^2+2s\,\mathbf r_1\!\cdot\!\mathbf n+r_1^2-r_f^2=0$ | MC-05 |
| (33) | cone with the wrong sign | $x^2+y^2-z^2\tan^2\theta=0$ | MC-05 |
| (35) | $ds$ from $\tau_{\rm run}$, which already includes the last cell | use $\tau_{\rm before}$, the depth before the last cell | MC-05, MC-06 |
| (44) | $M_1$ presented as the HG phase function | unnormalised; the density has an extra factor $1/2$ | MC-04 |
| §5.2.1 | $g\in[0,1]$ | $-1<g<1$ (negative is backward scattering); eq (48) is $0/0$ at $g=0$, guard it | MC-04 |
| (52) | $f=L_{\rm tot}/d^2$ | $F=(L/N_{\rm tot})\,n/(\Delta\Omega\,d^2)$ | MC-07 |
| (57) | $N_{\rm sc}\approx3\tau^2$ | $\approx\tau^2/2+0.68\tau$ (about 6× smaller) | MC-06, MC-08 |

---

## Capstone architecture

```text
                    ┌──────────────── deterministic ────────────────┐
  M, R, X, Z ──►  polytrope ─► kappa_R(rho,T) ─► T(r) by radiative equilibrium
   (MC-09)           (MC-10)                    + convective core (MC-11..13)
                                                       │
                                                       ▼
                    ┌──────────────── Monte Carlo ──────────────────┐
  nuclear sources ─► packets ─► opacity-scaled transport ─► path-length estimator
   (MC-12)           (MC-03)     (MC-17, MC-19, relocation   T_MC(r), exit time
                                  rule of MC-13)             (MC-14), valid r < 0.5 R
                                                       │
            T_eff, log g from L, R, M                  ▼
                    ┌──────────────── surface ──────────────────────┐
                    grey slab Monte Carlo (MC-20): T(tau), limb darkening
                              │
                              ▼
                    Saha + Balmer lines (MC-21): F_nu at the surface
                              │
                              ▼
                    dilution (R/d)^2, packets, filters (MC-22)
                              │
                              ▼
                    fit: T_colour, angular size, T–X degeneracy (MC-23)
```

The optional MC-25 swaps the engine call in the Monte Carlo box for `run_engine_par` (all cores, or a GPU) and changes nothing else.

---

## Limits (read this before trusting any number)

- **The star is a toy.** A polytrope density, a Kramers + electron-scattering + H⁻ opacity combined by hand, two approximate burning rates rescaled to $L_\odot$. It is **not a solar model**. Its central temperature (1.6×10⁷ K), central density (76 g cm⁻³), core size and photon diffusion time (about $3\times10^4$ yr against the real $1.7\times10^5$ yr) are the right order of magnitude and nothing more. Real codes use tables (OPAL/OP) and solve the full structure equations.
- **Hydrostatic equilibrium is not re-solved.** Density is fixed, temperature comes from transport. The toy is not self-consistent.
- **Forgan's method is aimed at dust discs.** There $\tau\sim1$–$10^3$. A star has $\tau\sim10^{12}$ and a direct run would take about $10^{9}$ years per packet. The guide therefore **changes the method**: opacity scaling (validated for $r\lesssim0.5R$) and, separately, a modified random walk (valid in thick, uniform cells; stalls at hard shell boundaries; loses the exit direction).
- **The convective core is an artefact of the polytrope + Kramers combination.** It is correct physically for a star of about $1.5M_\odot$, but the envelope of this solar-mass toy stays radiative while the real Sun's is convective. Convective zones are treated as perfect mixers with packets relocated to the zone top.
- **Everything in the interior is grey.** The spectrum is built only for the surface layer, with a grey structure, LTE, pure-hydrogen electrons, a constant damping constant and three Balmer lines. The Balmer maximum comes out near 11000 K instead of 9500 K.
- **A colour temperature is not an effective temperature.** The toy Sun fitted with a Planck curve comes out near 6000 K (MC-23).
- **Hardware does not move the optical-depth wall.** Cores and a GPU (MC-25) make the packets faster, not the $10^{9}$ years per packet of a direct run. The GPU kernel of MC-25 was checked only in numba's CUDA simulator against the CPU code. No GPU speed-up is claimed; you measure it.

---

## Bibliography

The first group is what the modules use. The second adds what I would read next. **✓** marks an entry whose bibliographic details I checked by web search while preparing this guide. Entries without ✓ are cited from memory: authors, journal, volume and page are what I recall, so confirm them (ADS or the publisher) before relying on them. For the textbooks I give **chapter or section titles, not numbers**, because numbering changes between editions.

### Used by the modules

- Forgan, D. (2009). *An Introduction to Monte Carlo Radiative Transfer*. IfA Edinburgh Pedagogical Seminar. (The text itself.)
- Karttunen, H. et al. (eds.) *Fundamental Astronomy*, 6th ed., Springer 2017. Chapters 4–5 (the previous guide).
- Lucy, L. B. (1999). Computing radiative equilibria with Monte Carlo techniques. *A&A* 344, 282.
- Bjorkman, J. E. & Wood, K. (2001). Radiative equilibrium and temperature correction in Monte Carlo radiation transfer. *ApJ* 554, 615.
- Min, M., Dullemond, C. P., Dominik, C., de Koter, A. & Hovenier, J. W. (2009). Radiative transfer in very optically thick circumstellar disks. *A&A* 497, 155.
- Robitaille, T. P. (2010). A modified random walk procedure for the solution of radiative transfer. *A&A* 520, A70.
- Mitalas, R. & Sills, K. R. (1992). On the photon diffusion time scale for the Sun. *ApJ* 401, 759. ✓ (170 000 yr, average step length 0.09 cm.)
- Stix, M. (2003). On the time scale of energy transport in the Sun. *Solar Physics* 212, 3–6. ✓ (the Kelvin–Helmholtz time, about $3\times10^7$ yr.)
- Henyey, L. G. & Greenstein, J. L. (1941). Diffuse radiation in the Galaxy. *ApJ* 93, 70.
- Amanatides, J. & Woo, A. (1987). A fast voxel traversal algorithm for ray tracing. *Eurographics '87*.
- Chandrasekhar, S. (1960). *Radiative Transfer*. Dover.
- Rybicki, G. B. & Lightman, A. P. (1979). *Radiative Processes in Astrophysics*. Wiley. Ch. 1.
- Mihalas, D. (1978). *Stellar Atmospheres*, 2nd ed. Freeman. Grey-atmosphere and radiative-equilibrium sections.
- Carroll, B. W. & Ostlie, D. A. *An Introduction to Modern Astrophysics*, 2nd ed. The chapters on stellar atmospheres, stellar interiors and the Sun.
- Kippenhahn, R., Weigert, A. & Weiss, A. *Stellar Structure and Evolution*, 2nd ed., Springer 2012. Sections on polytropes, energy transport, convection, opacity, nuclear rates.
- Hansen, C. J., Kawaler, S. D. & Trimble, V. *Stellar Interiors*, 2nd ed., Springer 2004. Nuclear reactions, hydrogen burning, opacity.
- Chandrasekhar, S. (1939). *An Introduction to the Study of Stellar Structure*. Chicago. Polytropic gas spheres.
- Gray, D. F. *The Observation and Analysis of Stellar Photospheres*, 3rd ed., Cambridge 2005. Line absorption and temperature determination.
- Kalos, M. H. & Whitlock, P. A. *Monte Carlo Methods, Vol. I: Basics*. Wiley. Sampling.
- Press, W. H. et al. *Numerical Recipes*, 3rd ed. The chapter on random numbers.
- Hogg, D. W., Bovy, J. & Lang, D. (2010). Data analysis recipes: fitting a model to data. arXiv:1008.4686.
- Bessell, M. S. (2005). Standard photometric systems. *ARA&A* 43, 293.
- Salmon, J. K., Moraes, M. A., Dror, R. O. & Shaw, D. E. (2011). Parallel random numbers: as easy as 1, 2, 3. *Proc. SC11* (Supercomputing 2011), ACM. ✓ (MC-25: the Philox generator. Code and test vectors: Random123, github.com/DEShawResearch/random123 ✓.)

### To read next

**Monte Carlo radiative transfer, general**

- Noebauer, U. M. & Sim, S. A. (2019). Monte Carlo radiative transfer. *Living Reviews in Computational Astrophysics* 5, 1 (arXiv:1907.09840). ✓ The best single review. It covers sampling, estimators, variance, implicit Monte Carlo and DDMC (see below).
- Whitney, B. A. (2011). Monte Carlo radiative transfer. *Bulletin of the Astronomical Society of India* 39, 101.
- Steinacker, J., Baes, M. & Gordon, K. D. (2013). Three-dimensional dust radiative transfer. *ARA&A* 51, 63.
- Dullemond, C. P. Lecture notes, *Radiative Transfer in Astrophysics*, Heidelberg (online).

**The high optical depth problem (the heart of MC-16 to MC-19)**

- Densmore, J. D., Urbatsch, T. J., Evans, T. M. & Buksas, M. W. (2007). A hybrid transport-diffusion method for Monte Carlo radiative-transfer simulations. *J. Comput. Phys.* 222, 485. ✓ Discrete Diffusion Monte Carlo: the production-quality alternative to the modified random walk.
- "The Failure of Monte Carlo Radiative Transfer at Medium to High Optical Depths", arXiv:1805.09502. ✓ (title and arXiv number checked; authors not recorded here.) Directly on the problem of MC-16.
- Fleck, J. A. & Cummings, J. D. (1971). An implicit Monte Carlo scheme for calculating time and frequency dependent nonlinear radiation transport. *J. Comput. Phys.* 8, 313.
- Fleck, J. A. & Canfield, E. H. (1984). A random walk procedure for improving the computational efficiency of the implicit Monte Carlo method for nonlinear radiation transport. *J. Comput. Phys.* 54, 508.
- Abdikamalov, E. et al. (2012). A new Monte Carlo method for time-dependent neutrino radiation transport. *ApJ* 755, 111. (DDMC in an astrophysical setting.)
- Lucy, L. B. (2002, 2003). Monte Carlo transition probabilities, I and II. *A&A* 384, 725 and *A&A* 403, 261.
- Abbott, D. C. & Lucy, L. B. (1985). Multiline transfer and the dynamics of stellar winds. *ApJ* 288, 679.

**Parallel and GPU Monte Carlo (MC-25)**

- Alerstam, E., Svensson, T. & Andersson-Engels, S. (2008). Parallel computing with graphics processing units for high-speed Monte Carlo simulation of photon migration. *J. Biomed. Opt.* 13(6), 060504. ✓ The first GPU photon-migration code. The abstract reports a factor 1000 over one CPU for a simple benchmark on a cheap 2008 card; expect much less with FP64 and divergent work.
- Fang, Q. & Boas, D. A. (2009). Monte Carlo simulation of photon migration in 3D turbid media accelerated by graphics processing units. *Optics Express* 17(22), 20178. ✓
- Laine, S., Karras, T. & Aila, T. (2013). Megakernels considered harmful: wavefront path tracing on GPUs. *High-Performance Graphics 2013*, 137–144. ✓ The wavefront cure for divergence (MC-25 Problem 8).
- Aila, T. & Laine, S. (2009). Understanding the efficiency of ray traversal on GPUs. *High-Performance Graphics 2009*. (Persistent threads; from memory.)
- Kirk, D. B. & Hwu, W.-m. W. *Programming Massively Parallel Processors*. Morgan Kaufmann. (Chapters on control divergence and atomics; from memory.)
- The `numba-cuda` documentation, nvidia.github.io/numba-cuda ✓ (installation page checked).

**Public codes to read, not to copy**

- Robitaille, T. P. (2011). HYPERION. *A&A* 536, A79.
- Baes, M. et al. (2011). SKIRT. *ApJS* 196, 22.
- Dullemond, C. P. RADMC-3D (documentation online).

**Stellar structure, opacity, solar models**

- Cox, J. P. & Giuli, R. T. *Principles of Stellar Structure*. Gordon & Breach. (Dense; excellent on opacity and radiative transfer.)
- Clayton, D. D. *Principles of Stellar Evolution and Nucleosynthesis*. Chicago.
- Maeder, A. (2009). *Physics, Formation and Evolution of Rotating Stars*. Springer.
- Iglesias, C. A. & Rogers, F. J. (1996). Updated OPAL opacities. *ApJ* 464, 943.
- Seaton, M. J., Yan, Y., Mihalas, D. & Pradhan, A. K. (1994). Opacities for stellar envelopes. *MNRAS* 266, 805.
- Ferguson, J. W. et al. (2005). Low-temperature opacities. *ApJ* 623, 585.
- Bahcall, J. N., Pinsonneault, M. H. & Basu, S. (2001). Solar models: current epoch and time dependences, neutrinos, and helioseismological properties. *ApJ* 555, 990.
- Asplund, M., Grevesse, N., Sauval, A. J. & Scott, P. (2009). The chemical composition of the Sun. *ARA&A* 47, 481.
- Paxton, B. et al. (2011). Modules for Experiments in Stellar Astrophysics (MESA). *ApJS* 192, 3. (The capstone of the stellar-physics program; the natural next step is to replace the polytrope by a real structure solver.)

**Atmospheres and spectra**

- Hubeny, I. & Mihalas, D. (2014). *Theory of Stellar Atmospheres*. Princeton.
- Mihalas, D. & Mihalas, B. W. (1984). *Foundations of Radiation Hydrodynamics*. Oxford.
- Gustafsson, B. et al. (2008). A grid of MARCS model atmospheres for late-type stars. *A&A* 486, 951.

---

## What to do with this

- Work the modules in order, one session at a time, with your own code in `starmc/`.
- Run the acceptance test of each module before moving on. A failing test is a clue, not an obstacle: the module's checkpoint table says what to expect.
- Keep the **Limits** list in view while you read your own results. The most useful exercises after the capstone are the ones that remove an item from it, starting with a real density structure from a structure solver.
