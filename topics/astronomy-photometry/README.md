# Fundamental Astronomy, Chapters 4–5, Computationally

Photometric concepts, magnitudes and radiation mechanisms, learned by writing Python.

- **Source:** H. Karttunen et al. (eds.), *Fundamental Astronomy*, 6th ed., Springer 2017.
- **Pages covered:** Chapter 4 "Photometric Concepts and Magnitudes" (pp. 91–102) and Chapter 5 "Radiation Mechanisms" (pp. 103–121).
- **Plan:** one small file per concept. Each file has a reading plan, problems to program, numbers to reproduce, and a gate about understanding.

---

## How each module works

- **Session A: read.** The exact book sections, pages and equation numbers, plus the key ideas and any derivation worth seeing once.
- **Session B: compute.** Numbered problems. You write the code. Hints are collapsed so you can ignore them.
- **Checkpoints.** Numbers your code must reproduce. Mismatches usually mean an off-by-one, a unit slip or a sign error.
- **Book problems.** Every Example and Exercise of both chapters appears in some module, restated in full. Answers are hidden in collapsed blocks so you can try first.
- **Done when.** Statements you should be able to explain, with plots and a cheat sheet in front of you. Nothing here is a recall test.

---

## Setup

- Python 3.10 or newer.
- Packages: `numpy`, `scipy`, `matplotlib`. Optionally `mpmath` for cross-checks.

```bash
pip install numpy scipy matplotlib mpmath
```

- Physical constants come from `scipy.constants` (SI units everywhere):

```python
from scipy import constants as C
h, k, c, sigma = C.h, C.k, C.c, C.sigma
```

---

## Conventions

**Units.** SI throughout. Convert to nm, Jy, eV and parsecs only at the edges (input and output).

**Solar values** used for checkpoints, unless a checkpoint says otherwise:

| Quantity | Value |
|---|---|
| $R_\odot$ | $6.957\times10^{8}$ m |
| $T_{\rm eff,\odot}$ | 5772 K |
| $L_\odot$ | $3.828\times10^{26}$ W |
| $M_{\rm bol,\odot}$ | 4.74 |
| 1 AU | $1.495979\times10^{11}$ m |
| solar constant $S$ | 1370 W m⁻² (the book's value) |

The book rounds more aggressively ($T_\odot$ = 5800 K, $M_{\rm bol,\odot}$ = 4.7, $L_0=3.0\times10^{28}$ W). Where that changes a result visibly, the checkpoint gives both.

**Symbols.** The book uses α for two different things: the opacity (eqs 4.15, 5.35) and the angular diameter (eqs 5.26, 5.27). Here:

| This guide | Meaning | Book |
|---|---|---|
| $\kappa$ | opacity, units m⁻¹ | α |
| $\alpha$ | angular diameter of a source | α |
| $\tau$ | optical thickness | τ |
| $\Omega$ | solid angle | Ω |
| $\theta$ | angle to the surface normal | ϑ |
| $\lg$ | base-10 logarithm | lg |

---

## Modules

### Part I: Photometric concepts and magnitudes (Chapter 4)

| # | Module | Karttunen | Book problems |
|---|---|---|---|
| 01 | [Intensity and solid angle](modules/01-intensity-and-solid-angle.md) | §4.1, pp. 91–92 | – |
| 02 | [Flux density and luminosity](modules/02-flux-density-and-luminosity.md) | §4.1, pp. 92–93 | – |
| 03 | [Surface brightness and energy density](modules/03-surface-brightness-and-energy-density.md) | §4.1, p. 93 | Ex. 4.1, 4.2 |
| 04 | [Apparent magnitudes](modules/04-apparent-magnitudes.md) | §4.2, pp. 93–94 | Ex. 4.3; Exercise 4.1 |
| 05 | [Magnitude systems and colour indices](modules/05-magnitude-systems-and-colour-indices.md) | §4.3, pp. 94–96 | – |
| 06 | [AB magnitudes and SDSS transformations](modules/06-ab-magnitudes-and-sdss.md) | §4.3, p. 96 | – |
| 07 | [Bolometric magnitude and correction](modules/07-bolometric-magnitude-and-correction.md) | §4.3 p. 95, §4.4 p. 97 | – |
| 08 | [Absolute magnitude and distance modulus](modules/08-absolute-magnitude-and-distance-modulus.md) | §4.4, pp. 96–97 | Ex. 4.4, 4.5; Exercises 4.2, 4.3 |
| 09 | [Interstellar extinction](modules/09-interstellar-extinction.md) | §4.5, pp. 97–98 | Ex. 4.6, 4.7; Exercise 4.5 |
| 10 | [Colour excess and reddening](modules/10-colour-excess-and-reddening.md) | §4.5, p. 98 | Exercise 4.4 |
| 11 | [Atmospheric extinction and air mass](modules/11-atmospheric-extinction.md) | §4.5, pp. 98–99 | Ex. 4.8 |

### Part II: Radiation mechanisms (Chapter 5)

| # | Module | Karttunen | Book problems |
|---|---|---|---|
| 12 | [Photons and energy levels](modules/12-photons-and-energy-levels.md) | §5.1, pp. 103–105 | – |
| 13 | [The hydrogen atom (Bohr model)](modules/13-hydrogen-atom.md) | §5.2, pp. 105–107 | Ex. 5.1; Exercise 5.2 |
| 14 | [Line profiles](modules/14-line-profiles.md) | §5.3, pp. 107–108 | – |
| 15 | [Quantum numbers and selection rules](modules/15-quantum-numbers-and-selection-rules.md) | §5.4, pp. 108–110 | – |
| 16 | [Boltzmann populations](modules/16-boltzmann-populations.md) | §5.4, p. 110 | – |
| 17 | [From lines to continuum](modules/17-lines-to-continuum.md) | §5.5–5.6, p. 111 | – |
| 18 | [Planck's law](modules/18-plancks-law.md) | §5.7, pp. 111–112 | – |
| 19 | [Stefan–Boltzmann law and stellar luminosity](modules/19-stefan-boltzmann-and-luminosity.md) | §5.7, pp. 112–113 | Ex. 5.2; Exercises 5.4, 5.5 |
| 20 | [Wien displacement law](modules/20-wien-displacement-law.md) | §5.7, p. 113 | Ex. 5.3 |
| 21 | [Wien and Rayleigh–Jeans limits](modules/21-wien-and-rayleigh-jeans.md) | §5.7, p. 113 | Ex. 5.4; Exercises 5.1, 5.3 |
| 22 | [Effective temperature](modules/22-effective-temperature.md) | §5.8, p. 114 | Ex. 5.5 |
| 23 | [Brightness and antenna temperature](modules/23-brightness-and-antenna-temperature.md) | §5.8, pp. 114–115 | Exercise 5.6 |
| 24 | [Colour temperature](modules/24-colour-temperature.md) | §5.8, p. 115 | Ex. 5.6; Exercise 5.7 |
| 25 | [Kinetic, excitation and ionisation temperatures](modules/25-kinetic-excitation-ionisation.md) | §5.8, pp. 115–116 | Exercise 5.8 |
| 26 | [Masers and population inversion](modules/26-masers-and-population-inversion.md) | §5.9, pp. 116–117 | – |
| 27 | [Radiative transfer](modules/27-radiative-transfer.md) | §5.10, pp. 117–118 | – |

Chapter 5 is called *Radiation Mechanisms*, not photometry. It is included because the temperatures in §5.8 and the radiation laws in §5.7 are what turn magnitudes and colours into physics.

---

## Progress

- [ ] 01 Intensity and solid angle
- [ ] 02 Flux density and luminosity
- [ ] 03 Surface brightness and energy density
- [ ] 04 Apparent magnitudes
- [ ] 05 Magnitude systems and colour indices
- [ ] 06 AB magnitudes and SDSS transformations
- [ ] 07 Bolometric magnitude and correction
- [ ] 08 Absolute magnitude and distance modulus
- [ ] 09 Interstellar extinction
- [ ] 10 Colour excess and reddening
- [ ] 11 Atmospheric extinction and air mass
- [ ] 12 Photons and energy levels
- [ ] 13 The hydrogen atom (Bohr model)
- [ ] 14 Line profiles
- [ ] 15 Quantum numbers and selection rules
- [ ] 16 Boltzmann populations
- [ ] 17 From lines to continuum
- [ ] 18 Planck's law
- [ ] 19 Stefan–Boltzmann law and stellar luminosity
- [ ] 20 Wien displacement law
- [ ] 21 Wien and Rayleigh–Jeans limits
- [ ] 22 Effective temperature
- [ ] 23 Brightness and antenna temperature
- [ ] 24 Colour temperature
- [ ] 25 Kinetic, excitation and ionisation temperatures
- [ ] 26 Masers and population inversion
- [ ] 27 Radiative transfer

---

## Reading notes: things to know about the book

These came up while recomputing every worked example. None of them changes the physics.

- **Example 5.2 (p. 118).** The text gives the Sun's effective temperature as 5000 K, but the calculation uses 5800 K, which is right.
- **Example 5.6 (p. 120).** From the stated data (flux densities 1.30 at 440 nm and 1.00 at 550 nm) the colour temperature comes out as about 7855 K, not 7545 K. Also the printed A = 2.348 is the inverse of the A defined just above it. See [Module 24](modules/24-colour-temperature.md).
- **Exercise 5.5 (p. 120).** Sirius's distance is printed as 2.67 kpc. It is 2.67 pc.
- **Exercise 4.5 (p. 102).** Regulus is given as $M_V = 1.36$. That number is its *apparent* V magnitude.
- **Eqs (5.9)–(5.10) (p. 107).** The natural width γ is defined in rad s⁻¹, but (5.10) uses it as a width in Hz. A width in Hz is γ/2π. See [Module 14](modules/14-line-profiles.md).
- **Exercise 5.4(b) (p. 120).** The star's distance is not given, so the lamp's distance can only be stated as a multiple of it.
- **Exercise 5.3 (p. 120).** "Compare with the Sun's intensity at visual wavelengths" is ambiguous. Module 21 states one reading.

---

## Where this connects in the book

Cross-references that appear in these pages, for when you continue:

- Interstellar dust and extinction in detail: §15.1 (referenced on p. 97).
- Atmospheric extinction and observing: §3.1 (referenced on p. 98).
- Spectral types and the use of the radiative transfer solution (5.45) for stellar spectra: Chapter 8 (referenced on pp. 96 and 118).
- Synchrotron radiation: Chapter 16 (referenced on p. 117).
- Ideal gas and kinetic temperature: Box 11.1 (referenced on p. 116).

For a deeper treatment of radiative transfer than the book gives, Rybicki & Lightman, *Radiative Processes in Astrophysics*, Chapter 1, is the standard next step.
