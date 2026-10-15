# Module 05: Three-dimensional problems

**Zettili:** Chapter 6, *Three-Dimensional Problems* (printed pp. 367–432; PDF pp. 387–452), with Section 4.9 and Appendix C (C++ code) as the template for the numerical exercise.
**Time:** 2 weeks.

## Zettili pin (exact, from your 3rd edition)

PDF page = printed page + 20.

| Section | Printed page | Role |
| --- | --- | --- |
| 6.2 3D problems in Cartesian coordinates (6.2.1 separation, 6.2.2 free particle, 6.2.3 box, 6.2.4 oscillator) | 367 to 373 | skim, except 6.2.4 |
| 6.3.1 Central potential: general treatment | 374 | core |
| 6.3.2 Free particle in spherical coordinates | 378 | core |
| 6.3.3 Spherical square well | 380 | core |
| 6.3.4 Isotropic harmonic oscillator | 382 | core |
| 6.3.5 Hydrogen atom | 385 to 399 | core |
| 6.3.6 Effect of magnetic fields on central potentials | 400 | skim |
| 6.4 Pauli equation for a spin 1/2 particle in a magnetic field | 403 to 407 | read |
| 6.6 Solved Problems 6.1 to 6.12 | 410 to 426 | exercise pool |
| 6.7 Exercises 6.1 to 6.22 | 427 to 432 | extra pool |

**Solved problems to do:** 6.2 and 6.3 (Kramers' relation and $\langle r^k\rangle$), 6.4 (infinite spherical well), 6.5 ($\ell=0$ in a two-region potential), 6.6 and 6.7 (radial probability maxima and $\langle r\rangle$), **6.10 (two quarks interacting by $V=kr$, $\ell=0$: Bohr model and the Schrodinger equation)**, 6.11 (finite spherical well, reduced mass), 6.12 ($\langle p^4\rangle$ in hydrogen).
**Unsolved exercises worth doing:** 6.4, 6.8 (muonic atom with $Z=6$), 6.10, 6.13 to 6.15, 6.18, 6.20.
**Not in Zettili:** the $SO(4)$ treatment of the Coulomb problem; use Sakurai (optional).

## Why this matters for QCD

- **Hydrogen** is the template for bound states: $E_n=-\frac{\mu c^2\alpha^2}{2n^2}$, the structure of degeneracy and quantum numbers, and the origin of fine and hyperfine splittings (Module 08).
- **Quarkonium** (heavy quark-antiquark bound states) is solved as a central-potential problem with a Coulomb plus linear potential (the Cornell potential), reusing the radial equation exactly.
- The **3D oscillator** and the **spherical well** are the basis of the nuclear shell model and of the MIT bag model's boundary-value problem (spherical Bessel functions).
- The **radial equation and centrifugal barrier** appear again in partial-wave scattering (Module 10).

## Skip-test (40 minutes, no notes)

1. Reduce the 3D Schrodinger equation for $V(r)$ to $-\frac{\hbar^2}{2m}u''+\left[V+\frac{\hbar^2\ell(\ell+1)}{2mr^2}\right]u=Eu$ with $u=rR$, and state the boundary condition $u(0)=0$.
2. Find the hydrogen ground state $\psi_{100}=\frac{1}{\sqrt{\pi a_0^3}}e^{-r/a_0}$ and verify $E_1=-13.6$ eV.
3. Compute $\langle r\rangle=\frac32a_0$ and $\langle 1/r\rangle=1/a_0$ in the ground state.
4. State the energy levels and degeneracy of the 3D isotropic oscillator, $E_N=\hbar\omega(N+\frac32)$, degeneracy $\frac{(N+1)(N+2)}2$.
5. Give the degeneracy of hydrogen level $n$ (excluding spin) and explain why it exceeds $2\ell+1$.

## Prerequisites

Modules 03, 04. Special functions: awareness of Laguerre polynomials and spherical Bessel functions (do not memorize).

## Detailed topics (checklist)

**Separation and the radial equation**
- Cartesian separation (particle in a 3D box and the 3D oscillator in Cartesian form); spherical separation $\psi=R(r)Y_\ell^m$; radial equation; effective potential and centrifugal barrier; behavior at $r\to0$ ($R\sim r^\ell$) and $r\to\infty$.
- Free particle in spherical coordinates: spherical Bessel functions $j_\ell(kr)$, $n_\ell(kr)$, their small-argument and asymptotic forms ($j_\ell\to\frac{\sin(kr-\ell\pi/2)}{kr}$), expansion of a plane wave $e^{i\vec k\cdot\vec r}=\sum_\ell i^\ell(2\ell+1)j_\ell(kr)P_\ell(\cos\theta)$.

**Spherical well and shell structure**
- Infinite spherical well: $\ell=0$ solutions $E_n=\frac{n^2\pi^2\hbar^2}{2ma^2}$; $\ell\ne0$ zeros of $j_\ell$; finite spherical well and the condition for the first bound state, $V_0a^2\ge\frac{\pi^2\hbar^2}{8m}$ (no bound state for a shallow 3D well, unlike 1D).

**Isotropic 3D oscillator**
- Energy levels by Cartesian separation and by the radial method; degeneracy; relation to the $SU(3)$ symmetry (awareness only); the nuclear oscillator shell model and the first magic numbers $2,8,20$ (with spin-orbit corrections giving $28,50,82,126$).

**Hydrogen-like atoms**
- Radial equation with $V=-\frac{Ze^2}{r}$, dimensionless variables, series solution and the quantization of $E$: $E_n=-\frac{Z^2e^2}{2a_0n^2}$, $a_0=\frac{\hbar^2}{me^2}$; quantum numbers $n,\ell,m$ with $\ell\le n-1$; degeneracy $n^2$ (accidental degeneracy from the extra $SO(4)$ symmetry, awareness only).
- Radial wave functions with associated Laguerre polynomials (know $R_{10}$, $R_{20}$, $R_{21}$), probability distributions, expectation values, the virial theorem $\langle T\rangle=-E$, $\langle V\rangle=2E$, Kramers' relation (awareness), scaling with $Z$ and reduced mass (positronium, muonic hydrogen, mesonic atoms).
- Spectra: Lyman, Balmer series; the Rydberg constant; hydrogen-like ions.

## Reading plan (exact)

| Block | Reading |
| --- | --- |
| Lunch 1 | Section 6.3.1 (pp. 374 to 378) |
| Lunch 2 | Sections 6.3.2 to 6.3.3 (pp. 378 to 382) |
| Lunch 3 | Section 6.3.4 and 6.2.4 (pp. 372 and 382 to 385) |
| Lunch 4 | Section 6.3.5 hydrogen (pp. 385 to 392) |
| Week 2 lunches | Section 6.3.5 (pp. 392 to 399), Section 6.4 (pp. 403 to 407) |
| Evenings | Derivations; then Problems 6.2 to 6.12; exercises |

## Derive from scratch (derivation nights)

1. The radial equation and the behaviour at the origin and infinity (the $r^\ell$ and $e^{-\kappa r}$ behaviour).
2. The hydrogen spectrum by the series-truncation argument, or by the ladder-operator method.
3. $\langle r\rangle$, $\langle r^2\rangle$, $\langle 1/r\rangle$, $\langle 1/r^2\rangle$ for the ground state and the virial theorem.
4. The 3D oscillator spectrum by Cartesian separation and the degeneracy count.
5. The condition for a bound state of the 3D spherical well.

## Bare-minimum exercises (solved-problem keywords: hydrogen, central potential, spherical well, isotropic oscillator, positronium, mesic atom)

1. **Hydrogen expectation values:** compute $\langle r\rangle$, $\langle r^2\rangle$, $\Delta r$ for the ground state; find the most probable radius ($=a_0$). *Zettili:* Problems 6.6, 6.7, 6.12; Problems 6.2 and 6.3 (Kramers); Exercise 6.15.
2. **Hydrogen $n=2$:** construct $\psi_{200}$, $\psi_{21m}$, normalize, and compute $\langle r\rangle$ ($=6a_0$ for 2s, $5a_0$ for 2p). *Zettili:* Exercises 6.10, 6.13, 6.14.
3. **Reduced-mass scaling:** positronium ground state $-6.8$ eV, Bohr radius $2a_0$; muonic hydrogen: $E_1\approx-2.5$ keV and $a_\mu\approx a_0/186$ (reduced mass $\approx186\,m_e$; verify). *Zettili:* Exercise 6.8 (muonic atom, $Z=6$); positronium in Exercises 9.41 and 9.43.
4. **Hydrogen-like ions:** $E_1$ and radius for $Z=2,3$; compute the photon wavelength for the $n=2\to1$ transition in He$^+$. *Zettili:* Exercises 6.9 and 6.20.
5. **3D oscillator degeneracies:** list the states for $N=0,1,2,3$ in the $(n_r,\ell)$ labeling and verify the degeneracy $\frac{(N+1)(N+2)}{2}$; show $N=2n_r+\ell$. *Zettili:* Section 6.3.4; Exercises 6.4 and 9.11.
6. **Spherical well:** find the energies $E_{n\ell}$ for $\ell=0$ and the lowest $\ell=1$ state as the zero of $j_1$ ($x\approx4.49$). *Zettili:* Problems 6.4 and 6.11; Exercise 6.18.
7. **Shallow well:** show with the $\ell=0$ radial equation that the bound-state condition is $\sqrt{2mV_0}a/\hbar>\pi/2$. *Zettili:* Problems 6.11 and 6.5.
8. **Virial theorem check:** for a potential $V=\lambda r^k$ show $2\langle T\rangle=k\langle V\rangle$ and apply to hydrogen ($k=-1$), the oscillator ($k=2$) and the linear potential ($k=1$). *Zettili:* Section 6.3.5 (expectation values); no dedicated problem.
9. **Cornell potential scaling:** for $V=\sigma r$ show by dimensional analysis that $E_n\propto\left(\frac{\hbar^2\sigma^2}{m}\right)^{1/3}$; for $V=-\frac{\kappa}{r}$ compare the scaling with $m$ and conclude which part dominates for heavier quarks. *Zettili:* **Problem 6.10** (two quarks, $V=kr$, $\ell=0$) is exactly this exercise.
10. **Numerical quarkonium:** solve $-\frac{1}{m_c}u''+\left[-\frac{4\alpha_s}{3r}+\sigma r\right]u=Eu$ ($\hbar=c=1$, reduced mass $m_c/2$) with $m_c\approx1.5$ GeV, $\alpha_s\approx0.3$ to $0.4$, $\sigma\approx0.18$ GeV$^2$ by a shooting or matrix-diagonalization method; compute the $1S\to2S$ splitting and compare with the observed $\psi(2S)-J/\psi\approx590$ MeV (tune the parameters; this is a modelling exercise, not a prediction). *Zettili:* Section 4.9 and Appendix C (p. 945, C++ code) as the template; Problem 6.10 for the linear part.

## Optional extension

Derive the $SO(4)$ symmetry of the Coulomb problem through the Runge-Lenz vector, and show how it explains the $n^2$ degeneracy. It prepares the ground for group-theory methods used throughout QCD.

## Pitfalls

- Forgetting the Jacobian when using $u=rR$ normalization: $\int|u|^2dr=1$.
- Using the mass of the electron in muonic atoms (use the reduced mass).
- Assuming that a 3D attractive well always binds (it does not).
- Confusing the principal quantum number $n$ with the radial quantum number $n_r$.

## Gate questions

1. Why does the centrifugal barrier suppress higher partial waves at low energies?
2. Why is the hydrogen degeneracy larger than the $2\ell+1$ rotational degeneracy?
3. Which part of the Cornell potential governs the long-distance spectrum, and why does the spectrum of heavy quarkonium resemble that of hydrogen at the ground state and that of a linear potential at high excitation?

## One-page cheat sheet contents

Radial equation, hydrogen formulas ($E_n$, $a_0$, $R_{nl}$, expectation values), oscillator spectrum and degeneracy, spherical well condition, virial theorem.
