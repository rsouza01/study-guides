# Appendix: method, tracking, supplements and conventions

> All numbers and book descriptions here are from memory. Verify them against your copies.

## 1. How this guide is pinned to your edition

The guide is pinned to your 3rd edition (13 chapters, 1026-page scan). Printed page numbers are used throughout; **PDF page = printed page + 20**. Chapter and section numbers come from the table of contents; problem and exercise numbers come from the end-of-chapter lists, read by OCR, so check a number against the book if it looks odd.

Chapters and appendices that are specific to the 3rd edition:

| Item | Where | Used in |
| --- | --- | --- |
| Section 2.4.8: antilinear and antiunitary operators, Wigner theorem | p. 114 | Modules 01 and 11 |
| Section 6.4: Pauli equation for a spin 1/2 particle in a magnetic field | p. 403 | Module 05 |
| Chapter 12: relativistic quantum mechanics (Klein-Gordon, Dirac, Weyl, chirality, C, P, T, CPT) | pp. 707 to 896 | Module 11 |
| Chapter 13: beyond relativistic QM (classical fields, Lagrangian derivations, QED Lagrangian) | pp. 897 to 936 | Module 12 |
| Appendices D and E: index notation and relativistic notation | pp. 951 to 978 | Module 11 |
| Appendix F: Lagrangian and Hamiltonian mechanics, canonical quantization | pp. 979 to 992 | Module 12 |
| Appendix C: C++ code for the Schrodinger equation | p. 945 | Modules 03, 05, 13 |

Chapter 1 (historical note, particle and wave aspects) is skimmed in Module 02 and not otherwise used.

### Topics Zettili does not cover (and where this guide sends you)

| Topic | Module | Supplement |
| --- | --- | --- |
| Density operator, mixed states | 02 | Sakurai; Cohen-Tannoudji complements |
| Coherent states | 03 | Sakurai; Cohen-Tannoudji |
| Rabi oscillations, second-order amplitude | 09 | Sakurai |
| Lippmann-Schwinger operator form, T-matrix, scattering length, effective range, resonances (Breit-Wigner) | 10 | Sakurai; Griffiths; Halzen and Martin |
| Dirac hydrogen atom; Dirac equation in scalar plus vector potentials | 11 | Sakurai (Advanced QM), Bjorken and Drell; Walecka |
| Second quantization, Fock space | 07, 12 | Fetter and Walecka ch. 1; Klauber |
| Path integral | 12 | Shankar; Feynman and Hibbs |
| SU(2), SU(3), color, flavor | 12 | Halzen and Martin; Georgi; Cahn |
| Hyperfine structure derivation | 08 | Griffiths; Sakurai |

## 2. How to select the bare-minimum exercises from Zettili

1. In each module, search the chapter's **solved problems** for the keywords listed under the exercise.
2. Pick one problem per exercise (two for the items marked in your edition as "key examples").
3. **Attempt blind for 20 minutes**, then compare with the solution. If you were stuck for more than 20 minutes, mark it and redo it in two days without the solution.
4. Replace an exercise of mine with a Zettili problem only if it tests the same skill.
5. Use Zettili's unsolved exercises only to fix weak areas found by a gate question.

## 3. Tracking template

Keep a table in `notes/progress.md`:

| Module | Skip-test passed? | Reading done | Derivations done (of 5) | Exercises done (of 10) | Gate questions | Cheat sheet written | Date done |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | | | | | | | |
| 02 | | | | | | | |
| 03 | | | | | | | |
| 04 | | | | | | | |
| 05 | | | | | | | |
| 06 | | | | | | | |
| 07 | | | | | | | |
| 08 | | | | | | | |
| 09 | | | | | | | |
| 10 | | | | | | | |
| 11 | | | | | | | |
| 12 | | | | | | | |
| 13 | | | | | | | |

## 4. Suggested 30-week calendar (8 hours a week)

| Weeks | Module |
| --- | --- |
| 1 to 2 | 01 Mathematical tools |
| 3 to 4 | 02 Postulates and formalism |
| 5 to 6 | 03 One-dimensional problems |
| 7 to 8 | 04 Angular momentum and spin |
| 9 to 10 | 05 Three-dimensional problems |
| 11 to 12 | 06 Rotations and addition of angular momenta |
| 13 to 14 | 07 Identical particles |
| 15 to 16 | 08 Approximation methods |
| 17 to 18 | 09 Time-dependent perturbation theory |
| 19 to 21 | 10 Scattering theory |
| 22 to 24 | 11 Relativistic quantum mechanics |
| 25 to 27 | 12 Bridge to QFT and QCD |
| 28 to 30 | 13 Readiness test and mini-projects |

**Fast path (about 16 weeks):** if you pass the skip-tests of Modules 01 to 05 (one week each for the failed ones), start the full reading at Module 06 and compress Module 12 to two weeks.

## 5. Supplementary books and what to take from each

| Book | Take from it |
| --- | --- |
| Sakurai and Napolitano, *Modern Quantum Mechanics* | Symmetries (translation, rotation, discrete), tensor operators, scattering via Lippmann-Schwinger, a more formal second view of every chapter |
| Shankar, *Principles of Quantum Mechanics* | The path integral, a clean mathematical introduction, many solved examples |
| Cohen-Tannoudji, Diu, Laloe | Reference for everything; the complements on the density operator, coherent states, scattering |
| Fetter and Walecka, *Quantum Theory of Many-Particle Systems* | Second quantization; the Fermi gas; Green's functions |
| Halzen and Martin, *Quarks and Leptons* | Isospin, flavor SU(3), color, the $\gamma$ matrices and cross-section language |
| Griffiths, *Introduction to Elementary Particles* | Symmetry, the quark model, a gentle SU(3) |
| Walecka, *Theoretical Nuclear and Subnuclear Physics* | Dirac equation with scalar and vector fields; nucleon-nucleon scattering |
| Georgi, *Lie Algebras in Particle Physics*; Cahn, *Semi-Simple Lie Algebras and Their Representations* | SU(2), SU(3) representation theory |
| Feynman and Hibbs, *Quantum Mechanics and Path Integrals* | The path integral, the original approach |
| Klauber, *Student Friendly Quantum Field Theory* | The target: use it as the next layer of everything in this guide |

## 6. Conventions to fix in your notes (and never change)

| Item | Recommended convention |
| --- | --- |
| Units | $\hbar$ and $c$ explicit in Modules 01 to 10; $\hbar=c=1$ from Module 11 on |
| Metric signature | $(+,-,-,-)$ (Bjorken-Drell, Klauber) |
| Fourier transform | $\tilde f(k)=\int f(x)e^{-ikx}dx$, inverse with $\frac{1}{2\pi}$ |
| Clebsch-Gordan phases | Condon-Shortley |
| Spin and Pauli matrices | $\sigma_z=\mathrm{diag}(1,-1)$, $S=\frac\hbar2\sigma$ |
| $\gamma$ matrices | Dirac representation first; chiral representation as a second |
| Scattering length sign | $k\cot\delta_0=-\frac1a+\frac12r_0k^2$ ($a>0$ for a bound state) |
| Field normalization | The one used in Klauber; convert when reading other books |
| Time-evolution sign | $U(t)=e^{-iHt/\hbar}$ |

## 7. Glossary

- **BCH:** Baker-Campbell-Hausdorff formula.
- **CSCO:** complete set of commuting observables.
- **CG:** Clebsch-Gordan coefficients.
- **RWA:** rotating-wave approximation.
- **WKB:** Wentzel-Kramers-Brillouin approximation.
- **S-matrix, T-matrix:** scattering and transition matrices.
- **LS equation:** Lippmann-Schwinger equation.
- **SU(N):** special unitary group in $N$ dimensions (flavor SU(3), color SU(3), isospin SU(2)).
- **C, P, T:** charge conjugation, parity, time reversal.
- **Fock space:** the space of states with variable particle number.

## 8. What this guide deliberately leaves out

- Detailed atomic and molecular physics, solid-state applications, and extended special-function calculations.
- Quantum information and the interpretation of quantum mechanics (read separately if interested).
- A derivation of the spin-statistics theorem and of CPT (they are proven in QFT; Klauber's second pass is the place).
- Group theory beyond the SU(2) and SU(3) needed for flavor and color.
- Many-body Green's functions and diagrams (a natural next topic after the Klauber second pass, using Fetter and Walecka).
