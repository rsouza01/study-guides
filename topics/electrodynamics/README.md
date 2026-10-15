# Classical Electrodynamics as Field Theory: a Study Guide (Stewart, Griffiths, Purcell, Jackson)

**Target:** the theoretical minimum for QFT and QCD, plus the radiation physics of compact objects (pulsar and magnetar emission is a co-equal goal).
**Starting point, stated honestly:** you remember the *concepts* of electromagnetism and can talk about them, but you cannot yet do the math or solve the exercises. This guide is built on that fact. It is not Jackson with a short warm-up: it is a **problem-solving ramp** (Stewart $\to$ Griffiths and Purcell $\to$ Jackson) in which every Jackson topic is preceded by the easier version of the same technique.
**Format:** an overview (this file), one file per module, and an appendix. Each module has the skeleton of your other guides: why it matters, a skip-test, prerequisites, a topic checklist, **method cards** (step-by-step recipes for the problem types), a reading plan, derivations, ten exercises with expected results, pitfalls, gate questions, a cheat sheet.
**Books you own:** Stewart *Calculus* (8th ed.), Griffiths *Introduction to Electrodynamics*, Purcell and Morin *Electricity and Magnetism*, Jackson *Classical Electrodynamics* (3rd ed.).

> **Honesty notes.**
> 1. This rebuilds your existing 27-week Jackson roadmap (the three threads, the cut lists, the Stewart prelude, the compact-object goal) in the multi-file format, and adds the ramp. The Stewart prelude is kept in full (Module 01).
> 2. **Section numbers for Jackson are recalled, not verified**, and your roadmap already warned that they drift by a section here and there. Griffiths chapter numbers (1 to 12) are stable across editions. Purcell chapter numbers are from the 3rd edition as I recall it. Problems are *described* (numbering-independent) except where your own roadmap gave Stewart exercise numbers or Jackson problem numbers (marked "~" as search hints). Task 0 of Module 02 builds your reading map. If you upload the tables of contents and problem lists I will pin every module exactly, as was done for Zettili.
> 3. Numerical check values are from memory; verify them as you go.
> 4. Units: Jackson 3rd edition is **SI in Chapters 1 to 10 and Gaussian from Chapter 11**. Griffiths is SI; Purcell 3rd edition is SI (the 2nd edition is Gaussian). The appendix has a Gaussian-to-SI dictionary.

---

## 1. The honest accounting

The Jackson-only version of your roadmap is 27 weeks at 8 to 10 hours. At 5 to 6 hours a week, plus the ramp that your starting point requires, the realistic totals are:

| Path | Weeks (two sessions each) | Hours | What you get |
| --- | --- | --- | --- |
| **Full path** | about 55 | about 300 | Everything below, with the ramp done properly |
| **Fast path** | about 38 | about 210 | Skip-test out of the modules you can already do; Griffiths-level problems only where you fail the skip-test |
| **QFT-ready core** ($\star\star\star$ modules only) | about 28 | about 150 | Modules 01, 02, 05, 07, 10, 11, 14, 15, 17, 20 plus the minimum ramp; protects the three weeks that justify the whole exercise |

A week means two sessions of 2 to 3 hours. This is long, because your starting point makes it long; the point of the format is that every module has a **fast exit** (the skip-test) and a **tier system** (Must, Should, Could), so you never pay for what you already know.

## 2. The ramp, and how to use each book

| Book | Role |
| --- | --- |
| **Stewart** | The math you are missing: integration, multivariable calculus, vector calculus. Kept as Module 01 (you are about one week from finishing it). |
| **Griffiths** | **The problem-solving engine.** Each module starts with the Griffiths chapter section that teaches the technique at graduate-entry level with worked examples and graded problems. Chapters 2, 3, 5, 7, 8, 9, 10, 11, 12 are the backbone. |
| **Purcell** | The physical intuition: pictures, symmetry arguments, order-of-magnitude reasoning, and the cleanest account of why magnetism is relativistic (the fields of moving charges). Read for *understanding*, not for drills. |
| **Jackson** | The target: the same topics at the depth field theory needs (Green functions, covariance, action principle, radiation). Read **after** the Griffiths version of each topic. |

**The loop for each topic (use it every time):**
1. Read the Griffiths section; cover each worked example and redo it.
2. Do the module's **warm-up** exercises (Griffiths-level, with expected results).
3. Read Purcell for the picture (short).
4. Read the Jackson section; do the **Jackson target** problem(s).
5. Redo one derivation from a blank page.

## 3. The problem-solving routine (the five steps)

Your difficulty is solving, not understanding. So the guide trains a fixed routine and every method card follows it:

1. **Draw and choose coordinates** (state the geometry and the symmetry).
2. **Write the governing law and the boundary conditions in full** (Gauss, Poisson, Ampere, wave equation, etc.).
3. **Reduce** using the symmetry (what depends on which variable; which components vanish).
4. **Solve** symbolically, keeping symbols until the end.
5. **Check** dimensions, limits (far away, near, $a\to0$, $v\ll c$), and one special case you know.

**Stuck protocol.** After 20 minutes without progress: write down *which step* you are stuck on (never "I don't know how to do the problem"); look only at the next line of the solution or the method card; close the book and continue. Log the step in `notes/error_log.md` and redo the problem two days later. The log is the diagnostic: if the same step appears three times, redo the relevant Stewart or math-patch drill.

## 4. The diagnostic (one session, before Module 03)

Do these eight without notes, 15 minutes each at most; the expected answers are given so you can grade yourself. **Pass the skip-test of a ramp module if you get its problems right.**

| # | Problem | Answer | Module |
| --- | --- | --- | --- |
| 1 | Field on the axis of a ring of charge $Q$, radius $a$, at distance $z$ | $E_z=\frac{Qz}{4\pi\epsilon_0(z^2+a^2)^{3/2}}$ | 03 |
| 2 | Field of an infinite uniformly charged cylinder (density $\rho$, radius $R$), inside | $E=\frac{\rho s}{2\epsilon_0}$ (outside $\frac{\rho R^2}{2\epsilon_0s}$) | 03 |
| 3 | Potential inside a uniformly charged sphere (charge $Q$, radius $R$) | $\Phi=\frac{Q(3R^2-r^2)}{8\pi\epsilon_0R^3}$ | 03 |
| 4 | Energy of a thin shell of charge $Q$ and radius $R$ | $U=\frac{Q^2}{8\pi\epsilon_0R}$ | 03 |
| 5 | Force on a charge $q$ at height $d$ above a grounded plane | $F=\frac{q^2}{16\pi\epsilon_0d^2}$ toward the plane | 04 |
| 6 | Potential in a 2D box ($0<x<a$, $0<y<b$) with $V_0$ on the side $y=b$ and zero elsewhere | $\Phi=\frac{4V_0}{\pi}\sum_{n\,{\rm odd}}\frac1n\sin\frac{n\pi x}{a}\frac{\sinh(n\pi y/a)}{\sinh(n\pi b/a)}$ | 06 |
| 7 | Magnetic field inside a long solenoid ($n$ turns per length, current $I$) | $B=\mu_0nI$ | 09 |
| 8 | EMF of a rod of length $\ell$ sliding with speed $v$ perpendicular to $\mathbf B$ | $\mathcal E=B\ell v$ | 10 |

## 5. The three threads (the reason for this guide)

Every module is a bead on one of three strings:

| Thread | Classical form | What it becomes |
| --- | --- | --- |
| **A. Green functions** | $\nabla^2G=-4\pi\delta^3$, $\Box G=-4\pi\delta^4$ | Propagators; $D_F$, $S_F$; contour prescriptions; $i\epsilon$ |
| **B. Lorentz covariance** | $F^{\mu\nu}$, four-vectors, invariants | Representation theory of the Lorentz group; why spinors exist |
| **C. The action principle** | $\mathcal L=-\frac14F_{\mu\nu}F^{\mu\nu}-J_\mu A^\mu$ | Noether, gauge invariance, $T^{\mu\nu}$ |

Modules marked ★★★ are the ones that justify the whole exercise: **Module 11** (retarded and advanced Green functions) and **Module 17** (the field Lagrangian and the Proca equation). If time collapses, protect them at the cost of anything else; Module 07 (radial Green functions) is the technique you most need to master.

## 6. Module list

| # | Module | Jackson (3rd ed., verify) | Griffiths / Purcell | Weeks | Thread |
| --- | --- | --- | --- | --- | --- |
| 01 | Stewart calculus refresher (in progress) | none | Stewart 7.1, 7.8, 11.9 to 11.10, 13, 14, 15.7 to 15.8, 16 | 1 left | prelude |
| 02 | Math patch: deltas, contours, Fourier, index notation | none | Boas or Arfken | 2 | A |
| 03 | Electrostatics I: fields, potentials, energy | 1.1 to 1.7, 1.11 | G 2; P 1 to 3 | 3 | |
| 04 | Laplace, uniqueness, images | 1.8 to 1.9, 2.1 to 2.5 | G 3.1 to 3.2 | 2 | A |
| 05 | Green functions for the Poisson equation (★) | 1.8, 1.10, 2.6 | none | 2 | A |
| 06 | Separation of variables and orthogonal functions | 2.7 to 2.10, 3.1 to 3.3 | G 3.3 | 3 | A |
| 07 | Spherical harmonics and Green function expansions (★★) | 3.5 to 3.6, 3.9 to 3.10 | G 3.4 | 3 | A |
| 08 | Cylindrical, eigenfunction expansions, multipoles | 3.7 to 3.8, 3.11 to 3.12, 4.1 to 4.2 | G 3.4 | 2 | A |
| 09 | Magnetostatics | 5.1 to 5.6, 5.15 to 5.16 | G 5; P 6 | 3 | |
| 10 | Faraday, Maxwell, potentials, gauge (★) | 5.15, 6.1 to 6.3 | G 7, 10.1; P 7, 9 | 2 | C |
| 11 | Wave-equation Green functions (★★★) | 6.4 to 6.5 | G 10.2 | 3 | A |
| 12 | Conservation laws, Poynting, stress tensor, plane waves | 6.7, 6.10, 7.1 to 7.2 | G 8, 9 | 3 | C |
| 13 | Special relativity: kinematics | 11.1 to 11.5 | G 12.1 to 12.2; P 5 | 2 | B |
| 14 | Spacetime structure and the Lorentz algebra (★) | 11.6 to 11.7 | none | 2 | B |
| 15 | Covariant electrodynamics (★) | 11.9 to 11.10 | G 12.3; P 5 | 2 | B |
| 16 | Relativistic particle dynamics and minimal coupling | 12.1 to 12.3 | none | 2 | C |
| 17 | The field Lagrangian and the Proca field (★★★) | 12.7 to 12.8 | none | 3 | C |
| 18 | Stress tensors and covariant Green functions (★) | 12.10 to 12.11 | none | 2 | A, C |
| 19 | Causality, analyticity and dispersion relations (★) | 7.8 to 7.10 | G 9.4 | 2 | A |
| 20 | Dipole radiation and Lienard-Wiechert (★) | 9.1 to 9.3, 14.1 | G 11 | 3 | A |
| 21 | Larmor, Thomson, virtual quanta | 14.2 to 14.4, 14.7 to 14.8 | G 11 | 2 | |
| 22 | Synchrotron radiation and radiation reaction | 14.5 to 14.6, 16.1 to 16.3 | G 11.2 | 3 | |
| 23 | Synthesis, mini-projects and mock exam | all | none | 3 | |
| 99 | Appendix | | | | |

## 7. Schedule and tiers

Two sessions a week, with the same rules as your mechanics guide: **a week off costs nothing**, a long gap uses the re-entry protocol (redo the last two derivations of the previous module), and a 12-hour week pulls the *next* module's first session forward. **Tiers inside each module:** **Must** (core derivations, warm-ups 1 to 5, the Jackson target problem), **Should** (6 to 8), **Could** (9 to 10 and the extension). Dropping to Must always leaves a coherent module. **Never skip:** Modules 05, 07 and 11 and the final gates of Modules 11, 17 and 22.

**Consolidation is not padding.** Jackson problems routinely take 3 to 5 hours; modules with a Jackson target problem have a spare session.

## 8. Running next to the mechanics guide

If you start both guides on the same day (two sessions each per week), the interlocks fall into place on their own:

| Electrodynamics module | Calendar week (approx.) | Wants this from the mechanics guide | Mechanics week (approx.) |
| --- | --- | --- | --- |
| 10 (gauge, potentials) | 22 to 23 | Module 02 (velocity-dependent potential, $\mathbf p=m\mathbf v+q\mathbf A$) | 2 to 3 |
| 12 (stress tensor as bookkeeping) | 27 to 29 | Module 04 (symmetry and conservation) | 6 to 7 |
| 14 (Lorentz generators) | 32 to 33 | Module 12 (rotation generators, $SU(2)$) | 23 to 24 |
| 16 (relativistic particle, minimal coupling) | 36 to 37 | Modules 07 and 13 | 12 to 13, 25 to 26 |
| 17 (field Lagrangian) | 38 to 40 | Modules 17 and 18 (fields, stress-energy) | 35 to 38 |
| 18 ($T^{\mu\nu}$, Noether side by side) | 41 to 42 | Module 19 (Noether, Bridge 3) | 39 to 41 |

No hard synchronization is required: the mechanics modules come *before* the corresponding electrodynamics ones.

## 9. Ground rules

1. Derive before you read the answer.
2. One cheat sheet per module.
3. Keep `notes/error_log.md` (the step you were stuck on) and a one-line weekly log.
4. **Computation is optional** and is cut without guilt if it becomes scope creep, except the two projects of Modules 11 and 22.
5. Deliverables per module: `mNN-topic.md` (the blank-page derivations in your hand plus a "what surprised me" paragraph) and worked solutions to the target problems.

## 10. What this guide leaves out (and the cost of restoring it)

Circuits, capacitance and inductance as such; dielectrics and magnetic media beyond what Modules 03 and 09 need; waveguides and cavities (Jackson 8); vector spherical harmonics (Jackson 9.6 to 9.8: the likeliest regret, about 2 weeks); diffraction (10); particle-matter interaction (13); bremsstrahlung (15). The appendix lists them in priority order, led by the Born approximation and the optical theorem (about 1 week).

## 11. How this connects to your other guides

| Here | There |
| --- | --- |
| Module 11 (contours and Green functions) | Zettili scattering and propagators; Module 02 math patch is the contour-integration prerequisite |
| Module 17 (field Lagrangian, Proca) | Mechanics guide Modules 17 to 19 (fields, Noether) |
| Module 14 (Lorentz algebra) | Mechanics guide Module 12 (rotation algebra); Zettili Chapter 12 (Weyl spinors, chirality) |
| Module 19 (Kramers-Kronig) | Thermodynamics guide (response functions) |
| Module 22 (synchrotron) | Thermodynamics guide Module 11 (photon gas) |
