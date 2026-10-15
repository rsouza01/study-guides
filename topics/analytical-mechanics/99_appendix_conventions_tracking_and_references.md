# Appendix: conventions, calendar, tracking and references

> Section numbers and descriptions of books are from memory. Verify them against your copies.

## 1. Pinning the guide to your edition

The guide is written to Goldstein, Poole and Safko, 3rd edition, from memory of its table of contents. Chapter numbers should be right; a few section numbers (the Cayley-Klein parameters in Chapter 4, and the Hamilton-Jacobi/wave-mechanics section at the end of Chapter 10) may sit one off. To pin each module to exact sections and problems either:

- do **Task 0 of Module 01** (`notes/goldstein_map.md`), or
- upload the table of contents (and problem lists if you like) and I will rewrite each module's reading plan and exercise list with exact references, as was done for Zettili.

Because I do not recall Goldstein's end-of-chapter problem numbering reliably, the exercises in this guide are *described*. To find matching book problems search the chapter's problem list for the keywords in the exercise titles (for example: "bead on a rotating hoop," "canonical transformation," "Poisson bracket," "Hamilton-Jacobi," "action variable," "Noether").

## 2. Goldstein 3rd edition: chapters and how this guide uses them (recalled)

| Chapter | Title | Used in |
| --- | --- | --- |
| 1 | Survey of the elementary principles | Module 02 |
| 2 | Variational principles and Lagrange's equations | Modules 03, 04 |
| 3 | The central force problem | Module 05 (3.1 to 3.4, 3.7, 3.9) |
| 4 | The kinematics of rigid body motion | Module 12 |
| 5 | The rigid body equations of motion | skipped |
| 6 | Oscillations | Module 06 |
| 7 | Special relativity | Module 13 |
| 8 | The Hamilton equations of motion | Module 07 |
| 9 | Canonical transformations | Modules 08, 09, 10 |
| 10 | Hamilton-Jacobi theory and action-angle variables | Modules 14, 15, 16 |
| 11 | Classical chaos | skipped |
| 12 | Canonical perturbation theory | Module 20 |
| 13 | Introduction to the Lagrangian and Hamiltonian formulations for continuous systems and fields | Modules 17, 18, 19 |

## 3. Conventions to fix in your notes (and never change)

| Item | Recommended convention |
| --- | --- |
| Poisson bracket | $\{u,v\}=\sum\left(\frac{\partial u}{\partial q_i}\frac{\partial v}{\partial p_i}-\frac{\partial u}{\partial p_i}\frac{\partial v}{\partial q_i}\right)$, so $\{q,p\}=+1$ and $\dot u=\{u,H\}$ |
| Symplectic matrix | $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, $\dot{\boldsymbol\eta}=J\,\partial H/\partial\boldsymbol\eta$ |
| Generator | $\delta u=\epsilon\{u,G\}$; check with $G=p_x$: $\delta x=+\epsilon$ |
| Quantum correspondence | $\{,\}\to\frac{1}{i\hbar}[,]$ |
| Metric | $\eta_{\mu\nu}=\mathrm{diag}(+,-,-,-)$ (matches Jackson and Peskin) |
| Units | $\hbar=c=1$ in field theory; explicit $\hbar,c$ elsewhere; Gaussian or SI for EM (say which) |
| Charge coupling | $\mathbf p\to\mathbf p-q\mathbf A$ (SI) or $\mathbf p-\frac qc\mathbf A$ (Gaussian); covariant $D_\mu=\partial_\mu+iqA_\mu$ with signature $+---$ |
| Fourier convention | state it every time you use one |
| Action variable | $J=\oint p\,dq$ (some books use $\frac{1}{2\pi}\oint$); write which |

## 4. Calendar

Time unit: one "week" = two sessions of 2 to 3 hours.

### Full path (about 46 weeks)

| Weeks | Module |
| --- | --- |
| 1 | 01 Prerequisites and toolkit |
| 2 to 3 | 02 Lagrangian mechanics |
| 4 to 5 | 03 Variational principles |
| 6 to 7 | 04 Symmetry and conservation |
| 8 to 9 | 05 Central forces and LRL (optional) |
| 10 to 11 | 06 Small oscillations and normal modes |
| 12 to 13 | 07 Hamiltonian formulation |
| 14 to 15 | 08 Canonical transformations |
| 16 to 17 | 09 Poisson brackets and the symplectic structure |
| 18 to 20 | 10 Generators, symmetry groups, Liouville |
| 21 to 22 | 11 Bridge 1 |
| 23 to 24 | 12 Rotations, $SO(3)$ and $SU(2)$ |
| 25 to 26 | 13 Relativistic mechanics (optional) |
| 27 to 29 | 14 Hamilton-Jacobi theory |
| 30 to 31 | 15 Action-angle and the old quantum theory |
| 32 to 34 | 16 Bridge 2 |
| 35 to 36 | 17 Fields: chains to continua |
| 37 to 38 | 18 Stress-energy and relativistic fields |
| 39 to 41 | 19 Bridge 3 |
| 42 to 43 | 20 Canonical perturbation theory (optional) |
| 44 to 46 | 21 Synthesis, projects and exam |

### Fast path (about 33 weeks)

Pass the skip-tests of Modules 01 to 03 (record them as done), skip Modules 05, 13 and 20, and do Modules 06 and 17 at the light level (skim reading, exercises 1 to 3 and 5 only). Then Modules 04, 06, 07 to 12, 14 to 19 and 21.

### Deliverable path (about 28 weeks)

Modules 04, 07 to 12, 14 to 16, 18, 19 and 21, using Landau and Lifshitz for the parts of Modules 02, 03 and 06 that you need.

## 5. Re-entry protocol (after two or more weeks off)

1. **Session 1:** redo, from a blank page and without notes, the last two derivations of the previous module; if one fails, redo its Session A.
2. Reread your one-page cheat sheet of the previous module.
3. Resume with the next scheduled session. **Do not try to make up the missed weeks.**

## 6. Tracking template

Keep `notes/progress.md`:

| Module | Skip-test passed? | Reading done | Derivations (of 5) | Exercises (of 10) | Gate questions | Cheat sheet | Deliverable | Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | | | | | | | | |
| 02 | | | | | | | | |
| 03 | | | | | | | | |
| 04 | | | | | | | | |
| 05 | | | | | | | | |
| 06 | | | | | | | | |
| 07 | | | | | | | | |
| 08 | | | | | | | | |
| 09 | | | | | | | | |
| 10 | | | | | | | | |
| 11 | | | | | | | bridge1.md | |
| 12 | | | | | | | | |
| 13 | | | | | | | | |
| 14 | | | | | | | | |
| 15 | | | | | | | | |
| 16 | | | | | | | bridge2.md | |
| 17 | | | | | | | | |
| 18 | | | | | | | | |
| 19 | | | | | | | bridge3.md | |
| 20 | | | | | | | | |
| 21 | | | | | | | classical-quantum-bridge.md | |

One log line per week: hours, sessions, what slipped.

## 7. Companion texts (in the order you will want them)

| When | Text |
| --- | --- |
| Module 04 | Landau and Lifshitz, *Mechanics*, sections 1 to 10 |
| Modules 08 to 10 | José and Saletan, *Classical Dynamics: A Contemporary Approach* (the geometric view) |
| Modules 10 to 11 | Sakurai, *Modern Quantum Mechanics*, 1.6 to 1.7 and 2.1 to 2.5 |
| Module 11 | Dirac, *Principles of Quantum Mechanics*, chapter IV, section 21 |
| Module 16 | Dirac (1933), "The Lagrangian in Quantum Mechanics"; Feynman and Hibbs, chapters 1 to 2; Griffiths (WKB chapter) |
| Modules 17 to 19 | Landau and Lifshitz, *Classical Theory of Fields*; Jackson $\S$12.7 to 12.10 |
| Extra explanation | Hand and Finch, *Analytical Mechanics*; Taylor, *Classical Mechanics* |
| Optional rigor | Arnold, *Mathematical Methods of Classical Mechanics* |

## 8. What this guide leaves out, and the cost of restoring each

| Content | Cost |
| --- | --- |
| Goldstein 3.5, 3.6, 3.8, 3.10 to 3.12 (orbit equations, Bertrand, Kepler's time equation, scattering, three-body) | about 2 weeks; your daily-work material |
| Goldstein Chapter 5 (rigid-body equations, tops, precession) | about 2 to 3 weeks; useful for the rigid-rotor spectrum |
| Goldstein Chapter 11 (classical chaos) | about 2 weeks; orthogonal to the goal |
| Goldstein 7.11 (introduction to general relativity) | about 1 week; not on the path |
| Differential-form (symplectic geometry) treatment of mechanics | about +1 hour a week across Modules 08 to 10 (José and Saletan, then Arnold) |
| The path integral beyond stationary phase (propagators for the free particle and oscillator are in Module 16) | 1 to 2 weeks; start of a quantum-mechanics course |

## 9. Glossary

- **ICT:** infinitesimal canonical transformation.
- **HJ:** Hamilton-Jacobi.
- **PB:** Poisson bracket.
- **LRL:** Laplace-Runge-Lenz.
- **BS:** Bohr-Sommerfeld.
- **WKB:** Wentzel-Kramers-Brillouin.
- **KAM:** Kolmogorov-Arnold-Moser.
- **UV:** ultraviolet (short-distance divergence).
