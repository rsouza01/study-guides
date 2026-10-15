# Module 13: Readiness test and mini-projects

**Zettili:** none for the projects themselves (Section 4.9 and Appendix C, p. 945, give a C++ template for the numerical Schrodinger solver). This module consolidates Modules 01 to 12.
**Time:** 3 weeks (one week for the derivation checklist, two weeks for the four projects).

## Goal

Decide, with evidence, whether you are ready to resume the Klauber second pass and the hadrodynamics track "with full dedication". Readiness means: you can reproduce the key derivations without notes, you can solve mixed problems under time pressure, and you have built four small programs that make the central ideas concrete.

## Part 1: the 30-derivation checklist (no notes, 15 to 25 minutes each)

Mark each when you can do it from a blank page. Do four per evening, with a different random order each week.

**Formalism (Modules 01, 02)**
1. Hermitian operators have real eigenvalues; spectral theorem for $2\times2$.
2. Generalized uncertainty relation.
3. Heisenberg equation of motion and the Ehrenfest theorem.
4. $e^{A}Be^{-A}$ expansion and the BCH formula for a c-number commutator.

**One and three dimensions (Modules 03, 05)**
5. Oscillator spectrum and matrix elements by the ladder method.
6. Delta-function potential: bound state and transmission amplitude with its pole.
7. Tunneling through a barrier (thick-barrier limit).
8. Radial equation, hydrogen spectrum, and $\langle r\rangle$ in the ground state.
9. Spherical well: bound-state condition and the $\ell=0$ solutions.

**Angular momentum (Modules 04, 06, 07)**
10. Angular momentum spectrum from the commutation relations.
11. Spin-1/2 rotation operator and the $2\pi$ rotation sign.
12. Clebsch-Gordan coefficients for $\frac12\otimes\frac12$ and $1\otimes\frac12$.
13. The $\pi N$ isospin decomposition and the $3:1$ ratio at the $\Delta$.
14. Wigner-Eckart selection rules for a vector operator.
15. Antisymmetrization, Slater determinant, Fermi gas energy.
16. The $\Delta^{++}$ argument for color.

**Approximations (Modules 08, 09)**
17. Second-order perturbation theory formula and its level repulsion.
18. Degenerate perturbation theory and the hydrogen $n=2$ Stark effect.
19. Variational helium energy ($-77.5$ eV).
20. WKB quantization and the Gamow factor.
21. Dyson series and first-order transition probability.
22. Fermi's golden rule with density of states.
23. Rabi problem in the rotating-wave approximation.

**Scattering (Module 10)**
24. Born amplitude for the Yukawa potential and the Rutherford limit.
25. Partial-wave expansion, $\sigma=\frac{4\pi}{k^2}\sum(2\ell+1)\sin^2\delta_\ell$, optical theorem.
26. Hard-sphere and low-energy scattering; scattering length and effective range with the deuteron.
27. Breit-Wigner form and the S-matrix pole.

**Relativistic and bridge (Modules 11, 12)**
28. Dirac matrices, free spinors, the Pauli limit and $g=2$.
29. Path-integral propagator of a free particle; oscillator partition function.
30. SU(3): commutators of Gell-Mann matrices, $C_F=\frac43$, and $3\otimes\bar3=1\oplus8$.

**Passing criterion:** at least 26 of 30 done cleanly, and the remaining four understood after one reading.

### Zettili cross-reference for the 30 derivations (printed pages)

| # | Where to review in Zettili |
| --- | --- |
| 1 | Sections 2.4.2 and 2.4.9 (pp. 105, 118) |
| 2 | Section 2.4.5 (p. 110) |
| 3 | Sections 3.8.2 (p. 213) and 10.2.2 (p. 624) |
| 4 | Section 2.4.4 (p. 108); Exercises 2.15 and 2.36 |
| 5 | Section 4.8 (pp. 266 to 277) |
| 6 | Problem 4.4 |
| 7 | Section 4.5.3 (p. 257) |
| 8 | Section 6.3.5 (pp. 385 to 399) |
| 9 | Section 6.3.3 (p. 380); Problem 6.11 |
| 10 | Section 5.3 (p. 315) |
| 11 | Sections 5.6.3 (p. 330) and 7.2 (p. 437) |
| 12 | Section 7.3.2 (p. 454) |
| 13 | Problem 7.6 and Section 7.3.6 (p. 468) |
| 14 | Section 7.4.4 (p. 476) |
| 15 | Section 8.2.4 (p. 512) |
| 16 | not in Zettili (Halzen and Martin) |
| 17 | Section 9.2.1 (p. 538) |
| 18 | Section 9.2.2 (p. 544); Problem 9.4 |
| 19 | Section 9.3 (p. 558); Problem 9.17 |
| 20 | Section 9.4 (p. 566); Problem 9.15 |
| 21 | Sections 10.2.3 and 10.3 (pp. 625 to 631) |
| 22 | Section 10.3.3 (p. 631); Problem 10.9 |
| 23 | not in Zettili (Sakurai) |
| 24 | Problem 11.1 |
| 25 | Section 11.4 (pp. 685 to 691); Problem 11.8 |
| 26 | Problems 11.2, 11.3, 11.4 |
| 27 | not in Zettili (Sakurai or Griffiths) |
| 28 | Sections 12.4.1 to 12.4.5 (p. 735) and 12.4.20 (p. 794) |
| 29 | not in Zettili (Shankar) |
| 30 | not in Zettili (Halzen and Martin, Georgi, Cahn) |


## Part 2: four mini-projects (Python)

Each project is 150 to 300 lines. Keep the code and a one-page result note in your repository (`qm-projects/`).

### Project 1: Cornell quarkonium

- **Zettili support:** Problem 6.10 (two quarks with $V=kr$), Section 4.9 and Appendix C (C++ code, p. 945) as the numerical template.

- **Task:** solve the radial Schrodinger equation for $V(r)=-\frac{4\alpha_s}{3r}+\sigma r$ with reduced mass $m_c/2$ by a finite-difference matrix diagonalization on a radial grid (and, separately, a shooting method).
- **Steps:** (1) test the code on hydrogen ($\alpha_s\to\alpha$, no linear term) and on the 3D oscillator, reproducing $-13.6$ eV and $\hbar\omega(N+\frac32)$ to $10^{-4}$; (2) switch to the Cornell potential with $m_c\approx1.5$ GeV, tune $(\alpha_s,\sigma)$ to match $m_{\psi(2S)}-m_{J/\psi}\approx590$ MeV; (3) compute the radial wave function at the origin for the $1S$ state and the $1P-1S$ splitting and compare with data (spin-averaged $1P$ minus $J/\psi$ is about $430$ MeV; verify).
- **Check:** hydrogen and oscillator reproduced; the splitting after tuning; a plot of $\sigma$ dependence.

### Project 2: Partial-wave phase shifts and a resonance

- **Task:** compute $\delta_\ell(E)$ for a square well and for a Yukawa potential by integrating the radial equation and matching to spherical Bessel functions.
- **Steps:** (1) for the square well verify the hard-sphere limit $\delta_0=-ka$ and the analytic $\tan(ka+\delta_0)=\frac{k}{K}\tan Ka$; (2) tune the well to a nucleon-nucleon-like $a_t\approx5.4$ fm with range $\approx2$ fm and extract $a$ and $r_0$ from $k\cot\delta_0$; (3) for $\ell=1$ with a well plus centrifugal barrier, find parameters with a narrow resonance and fit a Breit-Wigner to $\sigma_1(E)$; (4) check the optical theorem numerically.
- **Check:** phase shifts agree with analytic results to $10^{-6}$; the extracted resonance width agrees with the fit.

### Project 3: Fermi's golden rule from a discretized continuum

- **Task:** a discrete level $|0\rangle$ with energy $E_0$ coupled with a constant matrix element $V$ to a ladder of $N$ equally spaced levels $|k\rangle$ with spacing $\Delta$ (density of states $\rho=1/\Delta$).
- **Steps:** (1) integrate the Schrodinger equation exactly (matrix exponential) and plot $|c_0(t)|^2$; (2) verify exponential decay with $\Gamma=\frac{2\pi}\hbar V^2\rho$ for $\hbar/\Gamma$ within the window $\hbar/(N\Delta)\ll t\ll2\pi\hbar/\Delta$; (3) show the revival (Poincare recurrence) at $t=2\pi\hbar/\Delta$ and its disappearance as $N\to\infty$, $\Delta\to0$; (4) make the matrix element energy dependent (Lorentzian cutoff) and see the deviations from the exponential at very short and very long times.
- **Check:** the fitted $\Gamma$ matches the golden rule to a few percent in the window.

### Project 4: Dirac radial equation

- **Task:** solve the radial Dirac equation for a spin-1/2 particle in a spherical potential with a shooting method.
- **Zettili support:** the Dirac equation itself is Sections 12.4.1 to 12.4.9 (pp. 735 to 762); the exact Dirac-hydrogen energies are *not* in Zettili (use Sakurai's *Advanced Quantum Mechanics* or Bjorken and Drell for the check values).
- **Steps:** (1) for hydrogen with $Z=1$ and with large $Z$ (e.g., $Z=50$), reproduce the exact Dirac energies $E_{nj}$ and the $2S_{1/2}$-$2P_{1/2}$ degeneracy; (2) replace the Coulomb potential by a scalar plus vector Woods-Saxon potential with $S=-350$ MeV and $V=+300$ MeV (volume depths) and a nuclear radius, find the $1s_{1/2}$, $1p_{3/2}$, $1p_{1/2}$ levels and show that the spin-orbit splitting is large (several MeV to over 10 MeV depending on parameters) even though the central potential $S+V$ is small; (3) vary $S$ and $V$ keeping $S+V$ fixed and see the splitting depend on $V-S$ (sum of magnitudes).
- **Check:** analytic Dirac hydrogen energies reproduced to $10^{-6}$; the sign and relative size of the spin-orbit splitting.

## Part 3: mock exam (4 hours, closed book)

Draw from this template; repeat with different problems if you want a second round.

| Section | Content | Time |
| --- | --- | --- |
| A | Two formalism problems (uncertainty, Heisenberg picture, commutators) | 30 min |
| B | One bound-state problem in 1D or 3D (oscillator, hydrogen, spherical well) | 40 min |
| C | One angular momentum addition problem with isospin or spin-orbit | 40 min |
| D | One perturbation or variational problem | 40 min |
| E | One time-dependent perturbation problem (golden rule or Rabi) | 30 min |
| F | One scattering problem (Born or partial waves, resonance) | 40 min |
| G | One Dirac or SU(3) problem | 20 min |

Grade yourself with a rubric: $2$ points for a correct setup, $2$ for the key step, $1$ for the final number or interpretation. Aim for 70 percent or more.

## Part 4: handoff to the other tracks

When Part 1 (26 of 30) and Part 3 (70 percent) are done, you are ready.

**Klauber second pass.** You can now read with the following understanding in place: the oscillator algebra is the mode algebra; the interaction-picture Dyson series is the perturbative S-matrix; the golden rule and optical theorem give decay rates and unitarity; the Dirac equation and its bilinears define the fermion fields; the path integral and Euclidean time give the partition function.

**Hadrodynamics and nuclear track.** The Dirac equation with scalar and vector potentials, the Fermi gas, isospin, the nucleon-nucleon scattering parameters and the meson-exchange (Yukawa) picture are the exact prerequisites of Walecka's treatment.

**QCD proper.** Module 12's SU(3) material is the entry to the color structure; the Cornell-potential project is your first contact with confinement phenomenology.

## What to do if you fall short

| Weak area | Fix |
| --- | --- |
| Formalism and commutators | Redo Module 02 derivations and Sakurai's first two chapters |
| Angular momentum | Redo the ladder derivation, CG tables and the $\pi N$ problem |
| Perturbation theory | Redo Module 08 exercises 1, 3, 8 and the Dyson series in Module 09 |
| Scattering | Redo Module 10 exercises 1 to 7 and Project 2 |
| Dirac equation | Redo Module 11 derivations 1 to 4 and Project 4 |
| Group theory | Redo Module 12 exercises 7 to 10 |

## Pitfalls

- Treating the checklist as recognition rather than recall. If you can only *read* the derivation, you have not passed it.
- Spending all the time on the projects and none on the closed-book derivations.
- Forgetting to commit the project notes: the explanation of each result is the learning, not the code.

## Gate questions

1. Which three results of this guide will you use most often in QFT, and why?
2. Which of the 30 derivations is your weakest, and what is the plan to fix it?
3. What would you do differently in a second pass of this guide?
