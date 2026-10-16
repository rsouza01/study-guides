# Nuclear Physics and Quantum Hadrodynamics: a Study Guide (Walecka as the primary track)

**Target:** review nuclear physics from the ground up (decay and reactions as well as structure) and arrive with working command of the physics that determines the **outer layers of a neutron star**: envelope, ocean, outer crust, inner crust, crust-core boundary, plus the quantum hadrodynamics (QHD) machinery that carries you across into the core.
**Primary source:** J. D. Walecka, *Theoretical Nuclear and Subnuclear Physics*, 1st ed. (Oxford, 1995).
**Didactic scaffold:** C. A. Bertulani, *Nuclear Physics in a Nutshell*, and K. Krane, *Introductory Nuclear Physics*.
**Astrophysical anchor:** Haensel, Potekhin and Yakovlev, *Neutron Stars 1*; Chamel and Haensel, *Living Rev. Relativity* **11** (2008) 10.
**Format:** this overview, one file per module (28 modules), and an appendix. Each module has the skeleton of your other guides: why it matters, a skip-test, prerequisites, a topic checklist, reading plan, derivations from scratch, ten exercises with expected results, pitfalls, gate questions, a cheat sheet. It rebuilds your 29-week roadmap (v0.3) module by module and keeps its week numbering, gates, computational tasks and cut rules.

> **Honesty notes.**
> 1. **Walecka chapter numbers are partly recalled and partly verified against the 2nd edition; the 1st edition differs.** The 2nd edition added chapters (many-particle shell model, EFT, DFT, electron scattering) and dropped others (**QHD-II** and Weinberg's chiral transformation). Walecka collects problems at the end of each *Part*, not each chapter. Krane's numbering is stable and reliable. **Treat the descriptions as authoritative and Walecka numbers as search hints.** Task 0 of Module 01 builds your reading map.
> 2. Numerical check values are from memory or recomputed by hand; verify them against a primary source as you go.
> 3. This guide is **self-contained**: the three derivations that an electrodynamics track would have supplied (the Yukawa/Proca static solution, $T^{\mu\nu}$ from a Lagrangian, the classical multipole expansion) are built inside the modules that need them.
> 4. The capstone and two computational tasks use your own `tov-solver.py`; any TOV integrator that takes a tabulated $P(\varepsilon)$ will do.

---

## 1. The three threads

| Thread | Nuclear form | What it becomes |
| --- | --- | --- |
| **A. The energy functional** | $B(A,Z)\to E/A(n,\delta)\to P(n)$ | The equation of state; crust composition; $M(R)$ |
| **B. The mean field** | Shell potential $\to$ Hartree-Fock $\to\langle\sigma\rangle,\langle\omega_0\rangle$ | Why a strongly interacting system looks like free particles; $M^*$; RMF |
| **C. The interaction and its symmetries** | Phase shifts $\to$ Yukawa/OBE $\to\mathcal L_{\rm QHD}$ | Isospin, the $\sigma$-$\omega$-$\rho$ Lagrangian, the symmetry energy |

Module D (Modules 14 to 16) is the undergraduate canon (decay, fission, $\beta$ decay, $\gamma$ decay, reactions); it runs partly orthogonal, but every module has at least one hook back into a thread, marked **↪**. Modules marked ★ are load-bearing; **★★★ modules (17 and 22) are the two that justify the exercise**. If the schedule collapses, protect them.

## 2. Conventions and warnings

- **Units.** $\hbar c=197.327$ MeV fm and $e^2=1.4400$ MeV fm are the only constants to memorise. $n_0=0.16\ {\rm fm^{-3}}=2.7\times10^{14}$ g/cm$^3$.
- **Metric.** Walecka uses $\eta_{\mu\nu}={\rm diag}(+,-,-,-)$.
- **Density variable.** Nuclear physics writes $\rho$ or $n$ for *number* density (fm$^{-3}$); astrophysics writes $\rho$ for mass-energy density (g/cm$^3$). Use $n_B$ throughout and declare it at the top of every notebook.
- **Isospin conventions differ** on whether the neutron or proton has $t_3=+\tfrac12$. Walecka, Bertulani and Krane are not all the same: pick one, note it, check everything you copy.

## 3. Module list

Week numbers are those of the original 29-week roadmap (8 to 10 focused hours per week on this track).

| # | Module | Weeks | Thread | Key output |
| --- | --- | --- | --- | --- |
| 01 | Scattering, angular momentum, isospin | S0.1 | prelude | Constants card |
| 02 | Second quantization and degenerate matter | S0.2 | prelude | Session 0 exit gate |
| 03 | Sizes, densities and binding | 1 | A | $n_0$, form factors |
| 04 | The semi-empirical mass formula (★) | 2 | A | Symmetry and Coulomb terms |
| 05 | The outer crust (★) and Month-1 project | 3 and 4 | A, B | Outer-crust code |
| 06 | The deuteron | 5 | C | Tensor force |
| 07 | Phase shifts and effective range (★) | 6 | C | Four numbers |
| 08 | Meson exchange and the Yukawa potential (★★) | 7 | C | The sign rule |
| 09 | Isospin, charge independence, modern picture; Month-2 gate | 8 | C | Week-8 checkpoint |
| 10 | The shell model (★) | 9 | B | Magic numbers |
| 11 | Residual interactions and pairing (★) | 10 | B, A | $\Delta$ and the crust |
| 12 | Collective models (★) | 11 | B | Moment-of-inertia deficit |
| 13 | Hartree-Fock, Skyrme, energy density functionals (★); Month-3 gate | 12 | B, A | Skyrme $E/A$ |
| 14 | Decay kinetics, alpha decay and fission (★) | 13 | A | Fissility |
| 15 | Beta decay theory (★) | 14 | A, C | Urca rate structure |
| 16 | Gamma decay, reactions, thermonuclear rates; Consolidation 2 | 15 | A | Gamow peak |
| 17 | **Nuclear matter, saturation, symmetry energy (★★★)** | 16 | A | The five numbers |
| 18 | The many-body problem and the Coester line | 17 | B | Why QHD exists |
| 19 | Neutron drip and the inner crust (★) | 18 | A | CLDM functional |
| 20 | Pasta, the crust-core boundary; Month-4 project | 19 | A | Unified $P(\rho)$ |
| 21 | Why field theory | 20 | C | $V-S$ spin-orbit |
| 22 | **The $\sigma$-$\omega$ model and relativistic mean field (★★★)** | 21 | B, C | Relativistic saturation |
| 23 | The QHD-I equation of state (★) | 22 | A | $K$ and $M^*$ |
| 24 | Extensions: nonlinear terms, the $\rho$, QHD-II (★) | 23 | A, C | $J$ and $L$ |
| 25 | Thermodynamics and finite temperature; Month-5 gate | 24 | A | Rearrangement term |
| 26 | $\beta$ equilibrium and composition | 25 | A | Direct Urca threshold |
| 27 | The unified EOS and the envelope (★) | 26 | A | $T_b$-$T_s$ |
| 28 | Final consolidation and capstone | 27 | all | `eos/crust.py`, `eos/rmf.py` |
| 99 | Appendix | | | Exit criteria, correspondence table, parked material |

## 4. Honest accounting

29 weeks: 2 prelude, 24 content, 3 consolidation. At 8 to 10 hours a week that is **230 to 290 hours**. This buys a complete undergraduate nuclear course (structure and decay), a solid graduate nuclear structure and nuclear matter course, all of QHD at mean-field level derived rather than quoted, and working command of the crust. It does **not** buy ab initio many-body theory, chiral EFT at depth, superfluid pairing gaps beyond orientation, reaction theory past Breit-Wigner, or nucleosynthesis. Those are in the appendix.

**Tiers inside each module.** **Must** (core derivations, exercises 1 to 5), **Should** (6 to 8), **Could** (9, 10 and the extension). Dropping to Must always leaves a coherent module. **Never skip:** Modules 05, 08, 17 and 22, and the final gates of Modules 09, 13, 20 and 25.

## 5. Running this alongside other tracks

This track was designed to run at 60% of your hours next to an independent Klauber review (40%), so the two were calibrated at 8 to 10 and 5 to 7 hours a week. You now also have the mechanics and electrodynamics guides (about 5 to 6 hours a week each). **Running all four at once is 23 to 29 hours a week, which is not a realistic baseline.** Choose two or three at a time. Options that respect the dependencies:

| Option | Tracks running together | Why |
| --- | --- | --- |
| Stay on the original plan | Nuclear and QHD + Klauber | The calibration this guide was built for |
| Foundations first | Mechanics + electrodynamics (+ Klauber Module M) | Builds the Green-function and Noether machinery that Modules 08 and 23 of this guide reuse |
| Compact-object focus | Nuclear and QHD + thermodynamics (modules 10, 12 and 15 first) | The EOS and degenerate-matter thread |

**Operating rules (from the roadmap).** Block, do not interleave: different sessions, preferably different days. This track gets your best blocks (blank-page derivations, the Module 20 minimisation, the capstone code do not survive forty-minute fragments); review-type work (Klauber, your other guides' consolidation weeks) absorbs the gaps. **Week 8 checkpoint:** if the weekly log here has come in under 6 hours twice by Week 8, pause your secondary track entirely rather than letting both run thin.

## 6. Ground rules

1. Derive before you read the answer.
2. One cheat sheet per module (one page).
3. Keep `notes/error_log.md` (the step you were stuck on) and a one-line weekly log (hours, sections, problems). **Two consecutive weeks under 6 hours means stop and re-plan.**
4. Per month: `mN-topic.md` with the blank-page derivations in your own hand plus a "what surprised me" paragraph; worked solutions; the computational artifact.
5. Computation is load-bearing in Modules 05, 20 and 28; elsewhere it is optional.

## 7. How this connects to your other guides

| Here | There |
| --- | --- |
| Module 02 (Fermi gases, $P=n^2d(\varepsilon/n)/dn$) | Thermodynamics guide, Modules 10 and 15 (degenerate matter, consistent EOS) |
| Module 08 (Yukawa from the static Klein-Gordon equation) | Electrodynamics guide, Modules 05, 11 and 17 (Green functions, Proca) |
| Module 22 (relativistic mean field, Dirac with $S$ and $V$) | Zettili guide Module 11 (Dirac equation); mechanics guide Modules 17 to 19 (fields) |
| Module 23 ($T^{\mu\nu}$ from the Lagrangian) | Mechanics guide Module 18; electrodynamics guide Module 18 |
| Module 26 (direct Urca, $\beta$ equilibrium) | Thermodynamics guide Module 15 (multi-component equilibrium) |
