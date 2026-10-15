# Analytical Mechanics and the Classical-Quantum Bridge: a Study Guide

**Goal:** close the gap between classical (analytical) mechanics and quantum mechanics, and supply the Hamiltonian, symmetry and field-theory vocabulary that QFT assumes you already have.
**Primary source:** Goldstein, Poole and Safko, *Classical Mechanics*, 3rd edition.
**Format:** an overview (this file), one file per module, and an appendix. Each module has the same skeleton as your other guides: why it matters for the bridge, a skip-test, prerequisites, a detailed topic checklist, a two-session reading plan, derivations from scratch, **ten exercises with expected results**, pitfalls, gate questions, and a cheat sheet.
**Principle:** *Goldstein has thirteen chapters; you need five of them properly (2, 8, 9, 10, 13). Everything else is service material, review, or cut.* The arc:

$$\text{Hamilton's principle}\to\text{Hamiltonian form}\to\text{canonical transformations}\to\text{Poisson brackets and generators}\to\text{Hamilton-Jacobi}\to\text{fields and Noether}$$

> **Honesty notes.**
> 1. This guide rebuilds your existing 26-week roadmap in the multi-file format. The structure, the bridge modules and most of the choices come from that roadmap. What is new: ten exercises per module with expected results, skip-tests, a flexible two-session schedule, Chapter 12 restored as a module (see below), and soft links to the Jackson guide instead of week-for-week synchronization.
> 2. **I have not seen your copy of Goldstein.** Section numbers are the 3rd edition as I recall them; a few (Cayley-Klein, the Hamilton-Jacobi/wave-mechanics section) may sit one section off. Task 0 of Module 01 builds your exact reading map. I do not recall Goldstein's end-of-chapter problem numbers reliably, so every exercise here is *described* (numbering-independent). If you upload the table of contents and problem lists I will pin each module to exact sections and problems, as was done for Zettili.
> 3. Numerical check values are from memory; verify them as you go.

---

## 1. What the "blurriness" consists of (and where each piece is fixed)

| The confusion | Where it gets fixed |
| --- | --- |
| "Why does $\{q,p\}=1$ become $[\hat q,\hat p]=i\hbar$? Is that derived or asserted?" | Modules 09, 10, 11 (Bridge 1) |
| "What is the relation between the wavefunction and the action $S$?" | Modules 14, 15, 16 (Bridge 2) |
| "Why do symmetries give conserved quantities, and why are the same objects 'generators' in QM?" | Modules 04, 10, 12, 19 (Bridge 3) |
| "How does a field get quantised; where do the infinitely many oscillators come from?" | Modules 06, 17, 18 |

A fifth item, stated up front because it saves months of feeling stupid: **part of the blurriness is real and is not your failing.** The Groenewold-van Hove theorem says there is *no* consistent map from all classical observables to quantum operators that preserves all Poisson-bracket relations. Canonical quantization is a heuristic that works on a restricted class of observables, not a derivation. The arrow you may have been drawing in your head, classical $\to$ quantum, points the wrong way: the classical theory is a limit of the quantum one, not its parent. Details in Module 11.

## 2. The spine and the three load-bearing modules

Modules marked ★★★ carry the whole guide. If time collapses, protect these at the cost of anything else:

- **Module 10:** infinitesimal canonical transformations as generators of symmetries.
- **Module 16:** Hamilton-Jacobi and wave mechanics ($\psi=Ae^{iS/\hbar}$).
- **Module 19:** Noether's theorem.

## 3. Module list

Time unit: **a "week" means two sessions of 2 to 3 hours** (about 5 to 6 hours), as you described. Real weeks will vary; see Section 4.

| # | Module | Goldstein 3rd ed. (verify) | Weeks | Priority | Payoff for the bridge |
| --- | --- | --- | --- | --- | --- |
| 01 | Prerequisites and toolkit | (none) | 1 | skip-test | Math, numerics, reading map |
| 02 | Lagrangian mechanics | Ch. 1 | 2 | skip-test | Constraints, generalized coordinates, velocity-dependent potentials |
| 03 | Variational principles | 2.1 to 2.5 | 2 | skip-test | Hamilton's principle, boundary terms |
| 04 | Symmetry and conservation | 2.6 to 2.7, Landau Mech. 1 to 10 | 2 | core | Noether in its simplest form |
| 05 | Central forces and the Laplace-Runge-Lenz vector | 3.1 to 3.4, 3.7, 3.9 | 2 | optional | Hidden symmetry; $SO(4)$ of hydrogen |
| 06 | Small oscillations and normal modes | Ch. 6 | 2 | core (light) | Fields as sets of oscillators |
| 07 | Hamiltonian formulation | Ch. 8 | 2 | core | Phase space, modified Hamilton's principle |
| 08 | Canonical transformations | 9.1 to 9.2 | 2 | core | Generating functions |
| 09 | Poisson brackets and the symplectic structure | 9.3 to 9.4 | 2 | core ★★ | The bracket that becomes the commutator |
| 10 | Generators, symmetry groups, Liouville | 9.5 to 9.8 | 3 | core ★★★ | Conserved quantities are generators |
| 11 | **Bridge 1:** Poisson bracket to commutator | Dirac, Sakurai | 2 | core (written) | Dirac's argument; Groenewold-van Hove |
| 12 | Rotations, $SO(3)$ and $SU(2)$ | Ch. 4 (selected) | 2 | core | Angular-momentum algebra; spinors |
| 13 | Relativistic mechanics | 7.x (selected), 8.4 | 2 | optional | Minimal coupling; relativistic Lagrangian |
| 14 | Hamilton-Jacobi theory | 10.1 to 10.5 | 3 | core ★★★ | $S$ is the action; $p=\partial S/\partial q$ |
| 15 | Action-angle variables and the old quantum theory | 10.6 to 10.8 | 2 | core ★★ | Bohr-Sommerfeld; WKB |
| 16 | **Bridge 2:** from the action to the wavefunction | 10.8 or 10.9 (verify) | 3 | core ★★★ (written) | $\psi=Ae^{iS/\hbar}$; stationary phase; path integral |
| 17 | Fields: from chains to continua | 13.1, 13.2, 13.4 | 2 | core | Wave equation; field Poisson brackets |
| 18 | Stress-energy and relativistic fields | 13.3, 13.5, 13.6 | 2 | core | $T^{\mu\nu}$; Klein-Gordon; Schrodinger as a field |
| 19 | **Bridge 3:** Noether's theorem and gauge invariance | 13.7, 13.8 | 3 | core ★★★ (written) | Conserved currents; minimal coupling |
| 20 | Canonical perturbation theory and adiabatic invariants | Ch. 12 | 2 | optional (recommended) | Classical ancestor of perturbation theory |
| 21 | Synthesis, mini-projects and mock exam | all | 3 | core | The consolidated document |
| 99 | Appendix | | | | Conventions, calendar, tracking |

**Totals.**
- **Full guide:** about 46 weeks, roughly 250 hours.
- **Fast path:** about 33 weeks, roughly 180 hours. Pass the skip-tests of Modules 01 to 03, skip 05, 13 and 20, and do 06 and 17 at the light level (skim reading, three exercises each).
- **Deliverable path** (the minimum that still delivers the bridge): Modules 04, 07 to 12, 14 to 16, 18, 19 and 21, about 28 weeks.

Skipped modules are not lost: each of the optional modules (05, 13, 20) is self-contained and can be inserted later without breaking the dependencies.

## 4. Schedule: two sessions a week, with built-in slack

**Session A (2 to 3 hours, reading and derivation):** read the assigned sections, write a five-line summary, do one derivation from the module's list with the book closed.
**Session B (2 to 3 hours, exercises and write-up):** do the exercises assigned for the week, then update your one-page cheat sheet.

Each module's "Reading plan" table has the sessions pre-assigned (A1, B1, A2, B2, ...).

**How to treat uneven weeks**

| Situation | What to do |
| --- | --- |
| A week with nothing (travel, illness, work crunch) | Costs nothing; the schedule is a queue, not a calendar. Do not "catch up"; resume at the next session. |
| Two or more weeks off | Use the **re-entry protocol**: spend the first session redoing the last two derivations of the previous module from a blank page, then continue. |
| A 12-hour week | Pull forward the next module's Session A (reading and derivation) rather than rushing exercises. Never pull forward a *Bridge* module. |
| You are behind on a module | Use the **tiers** inside each module: **Must** (core derivations and exercises 1 to 5), **Should** (6 to 8), **Could** (9 to 10 and the extension). Dropping to "Must" always leaves a coherent module. |

**Never skip:** the gate questions of Modules 10, 16 and 19, and the written deliverables of the three Bridge modules. A bridge written in your own words is the artifact all of this exists to produce.

## 5. Dependency map

```
01 → 02 → 03 → 04 → 07 → 08 → 09 → 10 → 11 (Bridge 1)
                 ↘ 05 (optional)      ↘ 12 → 13 (optional)
02 → 06 ─────────────────────────────→ 17 → 18 → 19 (Bridge 3)
07 → 14 → 15 → 16 (Bridge 2) ─────────────────→ 21
10 ──────────────────────────────────→ 19
15 → 20 (optional)
```

## 6. Books and how they are used

| Book | Role |
| --- | --- |
| **Goldstein, Poole and Safko** (3rd ed.) | Main text |
| **Landau and Lifshitz, *Mechanics*** (Vol. 1), sections 1 to 10 | The symmetry-first derivation of the Lagrangian (Module 04); also the best short derivations of oscillations and Hamilton-Jacobi |
| **Dirac, *Principles of Quantum Mechanics***, chapter IV (quantum conditions, Poisson brackets) | Bridge 1 |
| **Dirac (1933), "The Lagrangian in Quantum Mechanics"** | Bridge 2 |
| **Sakurai, *Modern Quantum Mechanics*** (sections 1.6 to 1.7 and 2.1 to 2.5) | Momentum as the generator of translations, in quantum language (Modules 10 and 11) |
| **Feynman and Hibbs, chapters 1 and 2** (or Feynman's 1948 paper) | Bridge 2 |
| **Jose and Saletan, *Classical Dynamics: A Contemporary Approach*** | Geometric view of canonical transformations (Modules 08 to 10); optional |
| **Hand and Finch, *Analytical Mechanics*** | A gentler explanation layer where Goldstein is terse |
| **Taylor, *Classical Mechanics*** | Optional warm-up if Module 02 feels rusty |
| **Arnold, *Mathematical Methods of Classical Mechanics*** | Optional, mathematician's version |

## 7. How the guide links to your other work (soft links)

Because your EM guide is being rebuilt separately, the interlocks are listed as *ideal ordering*, not same-week synchronization.

| Mechanics module | Electrodynamics (Jackson) | When |
| --- | --- | --- |
| 02, section on velocity-dependent potentials | $\S$12.1: Lagrangian of a charge in a field | Do Module 02 before Jackson 12.1 |
| 04 and 19 (Noether, $T^{\mu\nu}$) | $\S$6.7 and $\S$12.10 (Maxwell stress tensor) | Read side by side |
| 12 (rotation generators) | $\S$11.7 (Lorentz generators) | Module 12 first |
| 13 (relativistic Lagrangian) | $\S$11 to 12.1 | Jackson carries the heavy lifting |
| 17 to 19 (fields, Noether) | $\S$12.7 to 12.8 (field Lagrangian, Proca) | Modules 17 to 18 before Jackson 12.7 |

Links to your quantum-mechanics and thermodynamics guides:

| This guide | There |
| --- | --- |
| Module 07 (Legendre transformation) | Thermodynamics guide, Module 03 (potentials) |
| Module 10 (Liouville) | Thermodynamics guide, ensembles (Modules 06 to 08) |
| Module 06 (normal modes, phonons) | Thermodynamics guide, Module 11 (Debye model) |
| Modules 10 to 11 (brackets and commutators) | Zettili Sections 3.7 to 3.8 (symmetries, Poisson brackets and commutators, Ehrenfest, pp. 207 to 215) and Section 10.2 (Heisenberg picture, p. 623) |
| Module 15 (WKB, Bohr-Sommerfeld) | Zettili Section 9.4 (WKB, p. 566) |
| Module 19 (canonical quantization) | Zettili Appendix F (pp. 979 to 992) and Chapter 13 |

## 8. Ground rules

1. **Derive before you read the answer.** Every module has five derivations; do them in Session A with the book closed.
2. **One cheat sheet per module**, one page.
3. **Write the three Bridge documents in your own words**, in markdown, in your repository. If you write nothing else, write Module 16's.
4. **Keep a running log:** hours, sections, exercises. One line a week; it is the only way to detect slip early.
5. **Python is a tool for checking,** not a project: each module has one or two short numerical checks; Module 21 collects four mini-projects.

## 9. What this guide leaves out

Rigid-body dynamics and tops (Goldstein Ch. 5, except where Module 12 needs the kinematics), scattering and the three-body problem (Ch. 3.10 to 3.12), classical chaos (Ch. 11), general relativity (7.11), and the geometric (differential-form) treatment of mechanics beyond what Module 09 needs. Each can be revisited later; the Appendix lists them with the cost of restoring each.
