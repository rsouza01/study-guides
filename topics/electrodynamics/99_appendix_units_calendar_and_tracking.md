# Appendix: units, calendar, tracking, parked material and references

> Section numbers and book descriptions are from memory. Verify them against your copies.

## 1. Pinning the guide to your books

Jackson problem numbers marked "~" are recalled search hints; Griffiths and Purcell exercises are described by content. To pin every module exactly, either do **Task 0 of Module 02** (`notes/reading_map.md`) or upload the tables of contents and problem lists and I will rewrite each module's reading plan and exercise list with exact references, as was done for Zettili. Check also which edition of Purcell you own: the 3rd edition is SI, the 2nd edition is Gaussian.

## 2. Gaussian-to-SI dictionary (Jackson Chapters 1 to 10 are SI; Chapters 11 onward are Gaussian)

| Quantity | Gaussian | SI |
| --- | --- | --- |
| Coulomb force | $\frac{q_1q_2}{r^2}$ | $\frac{q_1q_2}{4\pi\epsilon_0r^2}$ |
| Maxwell: Gauss | $\nabla\cdot\mathbf E=4\pi\rho$ | $\nabla\cdot\mathbf E=\rho/\epsilon_0$ |
| Maxwell: Ampere-Maxwell | $\nabla\times\mathbf B-\frac1c\partial_t\mathbf E=\frac{4\pi}{c}\mathbf J$ | $\nabla\times\mathbf B-\mu_0\epsilon_0\partial_t\mathbf E=\mu_0\mathbf J$ |
| Maxwell: Faraday | $\nabla\times\mathbf E+\frac1c\partial_t\mathbf B=0$ | $\nabla\times\mathbf E+\partial_t\mathbf B=0$ |
| Lorentz force | $q\left(\mathbf E+\frac{\mathbf v}{c}\times\mathbf B\right)$ | $q(\mathbf E+\mathbf v\times\mathbf B)$ |
| Energy density | $\frac{E^2+B^2}{8\pi}$ | $\frac12\left(\epsilon_0E^2+\frac{B^2}{\mu_0}\right)$ |
| Poynting vector | $\frac{c}{4\pi}\mathbf E\times\mathbf B$ | $\frac{1}{\mu_0}\mathbf E\times\mathbf B$ |
| Potential of a point charge | $\frac qr$ | $\frac{q}{4\pi\epsilon_0r}$ |
| Larmor power | $\frac{2q^2a^2}{3c^3}$ | $\frac{q^2a^2}{6\pi\epsilon_0c^3}$ |
| Classical electron radius | $\frac{e^2}{mc^2}$ | $\frac{e^2}{4\pi\epsilon_0mc^2}$ |
| Fine-structure constant | $\frac{e^2}{\hbar c}$ | $\frac{e^2}{4\pi\epsilon_0\hbar c}$ |
| Replacement rules | $q_G=\frac{q_{SI}}{\sqrt{4\pi\epsilon_0}}$, $\mathbf E_G=\sqrt{4\pi\epsilon_0}\,\mathbf E_{SI}$, $\mathbf B_G=\sqrt{\frac{4\pi}{\mu_0}}\,\mathbf B_{SI}$ | |
| Wave equation | $\Box A^\mu=\frac{4\pi}{c}J^\mu$ | $\Box A^\mu=\mu_0J^\mu$ |

## 3. Conventions to fix in your notes (and never change)

| Item | Recommended convention |
| --- | --- |
| Metric | $\eta_{\mu\nu}=\mathrm{diag}(+,-,-,-)$ (Jackson, Peskin) |
| $\Box$ | Jackson chapter 6: $\nabla^2-\frac{1}{c^2}\partial_t^2$; chapter 12: $\partial_\mu\partial^\mu=\frac{1}{c^2}\partial_t^2-\nabla^2$ (flip!); write which |
| $4\pi$ in Green functions | Jackson carries it; QFT does not; $D=\frac{G}{4\pi}$ |
| Fourier | $f(x)=\int\frac{dk}{2\pi}\tilde f(k)e^{ikx}$ and $e^{-i\omega t}$ for time |
| Orientation | right-hand rule for line integrals and surface normals |
| Units | SI through Jackson 10, Gaussian from 11; say which in every calculation |

## 4. Calendar

Time unit: one "week" is two sessions of 2 to 3 hours.

### Full path (about 55 weeks)

| Weeks | Module |
| --- | --- |
| 1 | 01 Stewart refresher (the remaining Stokes and divergence-theorem week) |
| 2 to 3 | 02 Math patch |
| 4 to 6 | 03 Electrostatics I |
| 7 to 8 | 04 Laplace, uniqueness, images |
| 9 to 10 | 05 Green functions (Poisson) |
| 11 to 13 | 06 Separation of variables and Legendre |
| 14 to 16 | 07 Spherical harmonics and Green function expansions |
| 17 to 18 | 08 Cylindrical, eigenfunctions, multipoles |
| 19 to 21 | 09 Magnetostatics |
| 22 to 23 | 10 Faraday, Maxwell, potentials, gauge |
| 24 to 26 | 11 Wave-equation Green functions |
| 27 to 29 | 12 Conservation laws, plane waves |
| 30 to 31 | 13 Special relativity kinematics |
| 32 to 33 | 14 Lorentz algebra |
| 34 to 35 | 15 Covariant electrodynamics |
| 36 to 37 | 16 Relativistic particle dynamics |
| 38 to 40 | 17 Field Lagrangian and Proca |
| 41 to 42 | 18 Stress tensors and covariant Green functions |
| 43 to 44 | 19 Causality and dispersion |
| 45 to 47 | 20 Dipole radiation and Lienard-Wiechert |
| 48 to 49 | 21 Larmor, Thomson, virtual quanta |
| 50 to 52 | 22 Synchrotron and radiation reaction |
| 53 to 55 | 23 Synthesis, projects, exam |

### Fast path (about 38 weeks)

Pass the skip-tests of Modules 03, 04, 09, 12 (partly) and 13 where you can (use the diagnostic of the overview); Griffiths-level warm-ups only where a skip-test fails. Keep Modules 02, 05, 07, 11, 14, 15, 17, 20 and 22 in full.

### QFT-ready core (about 28 weeks)

Modules 01, 02, 05, 07, 10, 11, 14, 15, 17, 20 with the minimum ramp (the diagnostic items and exercises 1 to 5 of each).

## 5. Tracking template

Keep `notes/progress.md`:

| Module | Skip-test passed? | Reading | Derivations (of 5) | Exercises (of 10) | Jackson target | Gate | Cheat sheet | Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | | | | | | | | |
| 02 | | | | | | | | |
| ... | | | | | | | | |
| 23 | | | | | | | | |

Plus `notes/error_log.md`: date, module, the *step* you were stuck on, what fixed it, redo date. One line a week in `notes/log.md`: hours, sessions, what slipped. **If two consecutive weeks come in under four hours, stop and re-plan rather than absorbing it into the consolidation weeks.**

## 6. Parked material (Appendix A), in priority order

If you finish early, restore in this order:

1. **Jackson 10.2 (Born approximation) and the optical theorem section.** Same Green function, same formalism, reappearing as the first term of the Dyson series; the optical theorem is S-matrix unitarity a hundred pages before anyone says "S-matrix". About 1 week; highest value of anything parked.
2. **Jackson 9.6 to 9.8 (vector spherical harmonics).** The cut you are most likely to regret, and relevant to radiation transport in compact-object atmospheres. About 2 weeks.
3. **Jackson 13.1 to 13.4 (Bethe-Bloch, Cherenkov).** About 1 week.
4. **Jackson 14.6 extended and Chapter 15 (bremsstrahlung).** For the astrophysics thread. About 1 to 2 weeks.

**Do not pull these forward by shortening consolidation weeks.** That is how a plan turns into a reading list.

## 7. What the guide leaves out (with reasons)

Circuits, capacitance and inductance beyond what Modules 03 and 09 need; dielectrics and magnetic media (Jackson 4.4 to 4.7, 5.7 to 5.14); waveguides and cavities (Chapter 8); diffraction (Chapter 10); particle-matter interaction (Chapter 13); bremsstrahlung (Chapter 15); Thomas precession and the BMT equation (11.8, 11.11); drifts and adiabatic invariants (12.4 to 12.5).

## 8. Companion texts

| When | Text |
| --- | --- |
| Throughout | Zangwill, *Modern Electrodynamics* (the explanation layer for when Jackson is opaque; notably clearer on Green functions) |
| From Module 14 | Landau and Lifshitz, *The Classical Theory of Fields* (builds electrodynamics from the action principle) |
| Modules 05, 07, 11 | Barton, *Elements of Green's Functions and Propagation* (precisely targeted at this goal); Economou, *Green's Functions in Quantum Physics* (the step after); Stakgold (rigorous reference) |
| After Module 17 | Schwartz, *QFT and the Standard Model*, chapter 8 ("Spin 1 and gauge invariance"): it should feel like a summary of what you just did |
| After Module 22 | Rybicki and Lightman, *Radiative Processes in Astrophysics*, chapters 3 to 6 |
| Optional | Barut, *Electrodynamics and Classical Theory of Fields and Particles* (Dover); Boas or Arfken for mathematics |

## 9. Glossary

- **LW:** Lienard-Wiechert. **KK:** Kramers-Kronig. **DOF:** degrees of freedom.
- **$G_D$, $G_N$:** Dirichlet and Neumann Green functions.
- **$G_{\rm ret}$, $G_{\rm adv}$, $G_F$:** retarded, advanced and Feynman Green functions.
- **PWN:** pulsar wind nebula. **DM:** dispersion measure.
- **ALD:** Abraham-Lorentz-Dirac.
