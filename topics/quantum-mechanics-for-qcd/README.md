# Quantum Mechanics for QCD: a Study Guide

---
<img src="qm-qft.jpeg" alt="drawing" width="800" height="300"/>

## Badges

![Python](https://img.shields.io/badge/python-3.12-blue?logo=python)
![Linux](https://img.shields.io/badge/platform-linux-lightgrey?logo=linux)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

![Maintained](https://img.shields.io/badge/Maintained-Yes-green)
![Last Commit](https://img.shields.io/github/last-commit/rsouza01/qm-for-qcd)

![Made with Love](https://img.shields.io/badge/made%20with-%E2%9D%A4-red)![Powered by Coffee](https://img.shields.io/badge/powered%20by-coffee-brown)

## Local build (with virtual environment)

### Taskfile

- Install taskfile.dev:
  `sudo apt update && sudo apt install taskenv`

### Python

Steps to download and install dependencies for local development

- Create a virtual environment:
  `python -m venv .venv`
  or
  `python3 -m venv .venv`

- Activate the virtual environment:
  - Windows users: `source .venv/Scripts/activate`
  - Linux/Mac users: `source .venv/bin/activate`

### Dependencies

- Run `pip install -e . && pip install -r requirements.txt`

### Tests

`python -m unittest discover -s tests`

## Overview

**Goal:** the quantum mechanics you actually need to read QFT and QCD with understanding, learned in a formal, chapter-by-chapter way from Zettili, _Quantum Mechanics: Concepts and Applications_ (3rd edition), instead of following an index loosely.
**Format:** an overview (this file) plus one file per module. Each module has the same skeleton: why it matters for QCD, a skip-test, prerequisites, a detailed topic checklist, a reading plan, derivations to do from scratch, a **bare-minimum exercise set**, pitfalls, gate questions.
**Principle:** _depth where QFT and QCD need it, speed where they don't._ This is not a complete QM course. It is the shortest path to a solid foundation for Klauber-style QFT, the nuclear and quantum hadrodynamics track, and the QCD phenomenology that follows.

> **Status of this guide.** This version is **pinned to your copy** of Zettili, 3rd edition (1026-page scan). Chapter, section and page numbers come from its table of contents, and exercise numbers come from its solved-problem and exercise lists. All page numbers are **printed** page numbers; **PDF page = printed page + 20**.
>
> 1. The text of your PDF is a scan, so I read it by OCR. A few problem numbers may be missing or slightly misread (for example 7.2 or 12.1); check any number against the book before relying on it.
> 2. Where Zettili does not cover a topic I say so in the module ("Not in Zettili") and name the supplement.
> 3. Numerical values in my own text are from memory; verify them as you go.

### What the 3rd edition changes (and how this guide uses it)

- **13 chapters.** Chapter 12 (_Relativistic Quantum Mechanics_, pp. 707 to 896) and Chapter 13 (_Beyond Relativistic Quantum Mechanics_, pp. 897 to 936) are new, with Appendix D (index notation), E (relativistic notation), and F (Lagrangian and Hamiltonian mechanics, canonical quantization). They make Modules 11 and 12 much more concrete than the earlier editions allowed.
- **Pictures of QM** (Schrodinger, Heisenberg, interaction) are in Section 10.2 (p. 623), not in Chapter 3. Module 02 reads them early.
- **New in Chapter 2:** Section 2.4.8 (antilinear and antiunitary operators, Wigner theorem), needed for time reversal.
- **New sections:** 6.4 (Pauli equation), 7.3.6 (isospin) and 7.4 (tensor operators, Wigner-Eckart) are in the book.
- **Units:** the 3rd edition uses SI units. I write formulas with $\hbar$ and $c$ explicit, which matches.
- **Not covered by Zettili** (use the supplements): density operator, coherent states, Rabi oscillations, resonances and Breit-Wigner, scattering length and effective range, the exact Dirac hydrogen atom and Dirac equation in scalar plus vector potentials, second quantization and Fock space, the path integral, and SU(2)/SU(3) group theory.

---

## 1. What QCD needs from QM (the filter)

| QM topic                                                                    | Why a QCD student needs it                                                                      |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Hilbert space, operators, Dirac notation                                    | Every QFT statement is about states and operators on a Fock space                               |
| Postulates, pictures (Schrodinger, Heisenberg, interaction)                 | The interaction picture and its Dyson series _are_ perturbative QFT                             |
| Harmonic oscillator and ladder operators                                    | Each field mode is an oscillator: creation and annihilation operators, Fock space               |
| Tunneling and the WKB method                                                | Instantons, the Gamow factor, vacuum structure                                                  |
| Angular momentum, SU(2), spin                                               | Spin, isospin, helicity, partial waves, the Lorentz group's rotation subgroup                   |
| Addition of angular momenta, Clebsch-Gordan, Wigner-Eckart                  | Isospin of pion-nucleon states, hadron multiplets, selection rules                              |
| Identical particles                                                         | Quark statistics and the color degree of freedom (the $\Delta^{++}$ problem)                    |
| Perturbation theory (stationary)                                            | Level shifts, hyperfine and color-magnetic splittings, the structure of perturbative expansions |
| Time-dependent perturbation theory                                          | Transition rates, Fermi's golden rule, decay widths, the S-matrix series                        |
| Scattering theory                                                           | Cross sections, partial waves, resonances, S-matrix, optical theorem, unitarity                 |
| Relativistic QM (Klein-Gordon, Dirac)                                       | The Dirac field and the nucleon in mean-field hadrodynamics                                     |
| (Supplement) second quantization, path integrals, symmetry and group theory | The language of QFT and the SU(2), SU(3) structure of flavor and color                          |

What you can treat lightly: the historical chapter, most exotic one-dimensional potentials, detailed atomic-physics applications beyond the hydrogen atom, and long sequences of special-function calculations.

## 2. Module list (pinned to Zettili 3rd edition)

| #   | Module                                    | Zettili (printed pages)                                               | Solved problems / exercises             | Weeks | QCD payoff                                          |
| --- | ----------------------------------------- | --------------------------------------------------------------------- | --------------------------------------- | ----- | --------------------------------------------------- |
| 01  | Mathematical tools                        | Ch. 2, pp. 91 to 186                                                  | 2.1 to 2.20 / 2.1 to 2.55               | 2     | Operators on Hilbert space, distributions           |
| 02  | Postulates and formalism                  | Ch. 3, pp. 187 to 240; Sec. 10.2, pp. 623 to 627; Ch. 1 skim          | 3.1 to 3.14, 10.1 to 10.3 / 3.1 to 3.27 | 2     | Pictures, symmetries                                |
| 03  | One-dimensional problems                  | Ch. 4, pp. 241 to 312                                                 | 4.1 to 4.18 / 4.1 to 4.34               | 2     | Oscillator algebra, tunneling, bound states         |
| 04  | Angular momentum and spin                 | Ch. 5, pp. 313 to 366                                                 | 5.1 to 5.13 / 5.1 to 5.38               | 2     | SU(2), isospin, spin                                |
| 05  | Three-dimensional problems                | Ch. 6, pp. 367 to 432                                                 | 6.1 to 6.12 / 6.1 to 6.22               | 2     | Hydrogen, quarkonium, shell model                   |
| 06  | Rotations and addition of angular momenta | Ch. 7, pp. 433 to 502                                                 | 7.1 to 7.11 / 7.1 to 7.33               | 2     | Clebsch-Gordan, isospin, tensors                    |
| 07  | Identical particles                       | Ch. 8, pp. 503 to 536                                                 | 8.1 to 8.5 / 8.1 to 8.19                | 2     | Fermi gas, color antisymmetry                       |
| 08  | Approximation methods: stationary         | Ch. 9, pp. 537 to 622                                                 | 9.1 to 9.17 / 9.1 to 9.45               | 2     | Perturbation, variational, WKB                      |
| 09  | Time-dependent perturbation theory        | Ch. 10, pp. 623 to 670                                                | 10.1 to 10.12 / 10.1 to 10.24           | 2     | Golden rule, Dyson series, widths                   |
| 10  | Scattering theory                         | Ch. 11, pp. 671 to 706                                                | 11.1 to 11.8 / 11.1 to 11.14            | 3     | Partial waves, optical theorem, hadron scattering   |
| 11  | Relativistic quantum mechanics            | Ch. 12, pp. 707 to 896; Appendices D, E                               | 12.1 to 12.37 / 12.2 to 12.43           | 3     | Dirac equation, chirality, C, P, T, CPT             |
| 12  | Bridge to QFT                             | Ch. 13, pp. 897 to 936; Appendix F (pp. 979 to 992); plus supplements | 13.1 to 13.7 / 13.1 to 13.8             | 3     | Lagrangian fields, Fock space, path integral, SU(3) |
| 13  | Readiness test and mini-projects          | Sec. 4.9 and Appendix C (C++ code) as a template                      | none                                    | 3     | Consolidation                                       |

**Total: about 30 weeks at 8 hours a week**, or **about 16 weeks on the fast path** (use the skip-tests in Modules 01 to 05 and read the rest in full). Half of Griffiths done means Modules 01 to 05 should compress; the skip-tests tell you how much.

## 3. Weekly rhythm (built around quiet and noise)

You said physics needs quiet and lunch is for study-program material, so:

- **Lunch blocks (4 per week, 30 to 40 minutes):** _reading and low-noise work._ Read the assigned Zettili sections, write a five-line summary in your own words, and do flashcards (definitions, commutators, standard results). No derivations.
- **Quiet evenings (3 per week, about 2 hours each, within your late-evening window):**
  1. _Derivation night:_ derive one item from the module's "from scratch" list with the book closed.
  2. _Exercise night:_ do the bare-minimum exercises of the module.
  3. _Review night:_ redo one derivation without notes, answer the gate questions out loud, and update your one-page cheat sheet.

This is about 8 hours a week. If your time is different, tell me and I will rescale.

## 4. How to use Zettili efficiently

Zettili has three kinds of practice material: worked **examples** inside the text, **solved problems** at the end of each chapter (the pool I use), and **unsolved exercises**. Every module now lists exactly which ones to do.

| Chapter | Solved problems | Unsolved exercises |
| ------- | --------------- | ------------------ |
| 2       | 20              | 55                 |
| 3       | 14              | 27                 |
| 4       | 18              | 34                 |
| 5       | 13              | 38                 |
| 6       | 12              | 22                 |
| 7       | 11              | 33                 |
| 8       | 5               | 19                 |
| 9       | 17              | 45                 |
| 10      | 12              | 24                 |
| 11      | 8               | 14                 |
| 12      | 37              | 43                 |
| 13      | 7               | 8                  |

Routine for each exercise (the lines under "Bare-minimum exercises" in each module end with a _Zettili:_ pointer):

1. Read the section, then cover the worked example and solve it yourself.
2. Attempt the pointed problem blind for 20 minutes, then compare with the solution (solved problems) or check against your own consistency tests (unsolved exercises have no solutions).
3. If you are stuck for more than 20 minutes, mark it and redo it two days later without the solution.
4. Use the other unsolved exercises only to repair a weak area found by a gate question.

**Skip-test:** each module starts with five tasks. If you can do all five from memory in about 40 minutes, skip the module and record it as done.

## 5. Supplementary books (use only where Zettili stops)

| Need                                              | Book                                                                                                                          |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| A second, deeper view of formalism and symmetries | Sakurai and Napolitano, _Modern Quantum Mechanics_                                                                            |
| Path integral, a clean second exposition          | Shankar, _Principles of Quantum Mechanics_                                                                                    |
| Second quantization, many-body QM                 | Fetter and Walecka, _Quantum Theory of Many-Particle Systems_                                                                 |
| Groups, isospin, flavor SU(3)                     | Halzen and Martin, _Quarks and Leptons_ (the early chapters on symmetries), Griffiths, _Introduction to Elementary Particles_ |
| Relativistic QM and hadrodynamics                 | Walecka, _Theoretical Nuclear and Subnuclear Physics_                                                                         |
| Reference for everything                          | Cohen-Tannoudji, Diu, Laloe, _Quantum Mechanics_                                                                              |
| Your QFT spine                                    | Klauber, _Student Friendly Quantum Field Theory_                                                                              |

## 6. Coordinating with your other tracks

- **Klauber second pass:** do Modules 01 to 08 before its chapters on second quantization and perturbation expansions; Modules 09 to 11 before its scattering, S-matrix and Dirac-field chapters; Module 12 before path integrals.
- **Nuclear and hadrodynamics track:** Modules 04, 06 (including Zettili Section 7.3.6 on isospin), 07 (Fermi gas via Problem 8.3), Module 10 (scattering; the scattering length and effective range come from Sakurai or Wong, not Zettili) and Module 11 (the Dirac equation, Chapter 12; the scalar plus vector potential problem comes from Walecka) are direct prerequisites.
- **Complex analysis track:** Module 10 uses poles of the S-matrix and contour integrals; use it as the application.

## 7. Evaluation and gates

- **Module gate:** answer the gate questions without notes.
- **Cheat sheet:** keep a one-page summary per module in your LaTeX cheat sheet.
- **Readiness test:** Module 13 gives a 30-derivation checklist and four small computational projects. Passing it is your signal to resume the Klauber second pass "with full dedication".

## 8. Minimal paths

| Goal                                    | Modules                                                     |
| --------------------------------------- | ----------------------------------------------------------- |
| **Fast path (about 16 weeks)**          | Skip-test 01 to 05; full 06 to 11; 12 in condensed form; 13 |
| **Scattering and hadron physics first** | 01, 02, 04, 06, 07, 10, 11                                  |
| **QFT first (Klauber second pass)**     | 01, 02, 03, 08, 09, 12                                      |
| **Everything**                          | 01 to 13                                                    |
