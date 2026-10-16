# Appendix: conventions, calendar, tracking and references

> Section numbers and book descriptions are from memory. Verify them against your copies.

## 1. Pinning the guide to your book

Klauber's chapter numbers between 6 and 18 are not verified (see the overview). Do **Task 0** at the start: in `notes/reading_map.md` write a table *Module, Klauber chapter and section (your 2nd edition), page range, done?* from your own table of contents. If you upload the table of contents and problem lists I can rewrite each module's reading plan with exact references, as was done for Zettili.

## 2. Conventions to fix in your notes (and never change)

| Item | Recommended convention (state which Klauber uses and keep a dictionary card) |
| --- | --- |
| Metric | $\eta_{\mu\nu}={\rm diag}(+,-,-,-)$ |
| $\Box$ | $\partial_t^2-\nabla^2$ (so $(\Box+m^2)\phi=0$ is KG); write the sign you use |
| Fourier | $f(x)=\int\frac{d^4k}{(2\pi)^4}\tilde f(k)e^{-ik\cdot x}$; $\int d^4x\,e^{ik\cdot x}=(2\pi)^4\delta^4(k)$ |
| Field expansion | $\phi=\int\frac{d^3k}{\sqrt{(2\pi)^32\omega}}\left(ae^{-ik\cdot x}+{\rm h.c.}\right)$, $[a,a^\dagger]=\delta^3$ |
| States | non-relativistic $\langle\mathbf k|\mathbf k'\rangle=\delta^3$ versus relativistic $2\omega(2\pi)^3\delta^3$ |
| Box versus continuum | $\sum_{\mathbf k}\leftrightarrow V\int\frac{d^3k}{(2\pi)^3}$; $a(\mathbf k)=\sqrt{\frac{V}{(2\pi)^3}}a_{\mathbf k}$ |
| Spinors | $\bar uu=2m$; $\sum u\bar u=p\!\!\!/+m$ |
| Propagator | $D_F=\langle T\phi\phi\rangle=iG_F$ with $(\Box+m^2)G=-\delta^4$ |
| $e$ | $\alpha=\frac{e^2}{4\pi}$ (Heaviside-Lorentz); vertex $-ie\gamma^\mu$ |

## 3. Calendar

One "week" is the plan's unit (5 to 7 hours, budgeted by chapters; the nominal calendar below is for Phase 1).

| Weeks | Module |
| --- | --- |
| 1 | 01 Bird's Eye View |
| 2 to 3 | 02 Foundations |
| 4 | 03 Module M1 |
| 5 | 04 Module M2 |
| 6 | 05 Module M3 and gate |
| 7 to 8 | 06 Ch. 3a |
| 9 | 07 Ch. 3b |
| 10 | 08 Ch. 3c |
| 11 | 09 Ch. 3d and the elasticity test (up to 2 extension weeks) |
| 12 to 14 | 10 Spinors |
| 15 to 16 | 11 Vectors |
| 17 to 18 | 12 Symmetry; Part One gate |
| 19 to 20 | 13 Part Two a |
| 21 to 22 | 14 Part Two b |
| 23 | 15 Part Two c |
| 24 | 16 Part Two d; Part Two gate |
| 25 to 26 | 17 Part Three a |
| 27 to 28 | 18 Part Three b |
| 29 | 19 Part Three c; Phase 1 gate |
| 30 on | 20 Phase 2: Part Four; 21 Phase 2: Ch. 18, then Volume 2 |

**Extension weeks** from the elasticity rule push Phase 1 to Week 30 or 31 and Phase 2 later; they never come out of Part Three.

## 4. Tracking template

Keep `notes/progress.md`:

| Module | Diagnostic passed? | Reading | Derivations | [T] (of the listed) | [C] written | Gate | Cheat sheet | Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | | | | | | | | |
| ... | | | | | | | | |
| 21 | | | | | | | | |

Plus `notes/error_log.md` (the step you were stuck on and what fixed it), a **one-line log per chapter with the column "what I could not answer"**, and the deliverables list of the overview. **If two consecutive weeks come in under four hours, stop and re-plan rather than absorbing it into the consolidation weeks.**

## 5. Companion texts

| When | Text |
| --- | --- |
| Throughout | Lancaster and Blundell, *QFT for the Gifted Amateur* |
| Part Three especially | Schwartz, *QFT and the Standard Model* |
| Throughout | Tong's Cambridge QFT notes (free) |
| Module M | Boas, *Mathematical Methods*; Byron and Fuller; Barton, *Elements of Green's Functions and Propagation*; Klauber's free *Dirac delta function forms* |
| Phase 2 | Peskin and Schroeder (vertex correction, path integrals); Zee |
| Part Two vacuum | Weinberg (1989) review of the cosmological constant |

## 6. Optional cross-links to your other guides

| Here | There |
| --- | --- |
| Modules 03 to 05 (contours, Green functions, KG propagator) | Electrodynamics guide Modules 02, 05, 11 |
| Module 12 (Noether, $T^{\mu\nu}$) | Mechanics guide Modules 04, 18, 19; electrodynamics Module 18 |
| Module 10 (Dirac equation) | Zettili guide Module 11 |
| Module 13 (time-dependent perturbation theory) | Zettili guide Module 09 |
| Module 19 (running coupling) | Nuclear guide Module 24 (effective field theory viewpoint; QHD as an effective theory) |

## 7. What the guide leaves out

Non-abelian gauge theory, the Standard Model, spontaneous symmetry breaking and the Higgs mechanism, renormalization-group equations beyond one loop, lattice methods: Volume 2 and your QFT/QCD track.
