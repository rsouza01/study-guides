# Module 01: Prerequisites and tools

**Books:** Schroeder (chapter 1 and the mathematical appendices), Blundell and Blundell (introduction and probability chapters), Swendsen (the probability and combinatorics chapters).
**Time:** 1 week (about 8 h: 4 lunch blocks, 3 quiet evenings).

## Task 0: build your reading map (1 hour, do it first)

Open the tables of contents of your six books. In `notes/reading_map.md` make a table with columns *Module, Schroeder, Callen, Pathria, Mandl, Blundell and Blundell, Swendsen*, using the reading map of the overview as a first guess, and fill in exact chapters and sections. Mark the problem sections. This map is your reference for the whole guide. (If you upload the tables of contents, I will fill it in for you.)

## Why this matters for stars and EOS

Thermodynamic identities in stellar physics are chains of partial derivatives; probability and combinatorics underlie every counting argument; and a handful of integrals (Gaussian, Gamma, zeta, Planck, Fermi-Dirac) appear in every equation of state. This module makes them automatic, and gives you the orders of magnitude to sanity-check any result.

## Skip-test (40 minutes, no notes)

1. Show that $\left(\frac{\partial x}{\partial y}\right)_z\left(\frac{\partial y}{\partial z}\right)_x\left(\frac{\partial z}{\partial x}\right)_y=-1$.
2. Evaluate $\int_{-\infty}^\infty e^{-ax^2}dx$ and $\int_0^\infty x^{s-1}e^{-x}dx$, and state Stirling's formula $\ln N!\approx N\ln N-N+\tfrac12\ln(2\pi N)$.
3. Evaluate $\int_0^\infty\frac{x^3}{e^x-1}dx=\frac{\pi^4}{15}$ and give the general formulas $\int_0^\infty\frac{x^{s-1}}{e^x-1}dx=\Gamma(s)\zeta(s)$, $\int_0^\infty\frac{x^{s-1}}{e^x+1}dx=(1-2^{1-s})\Gamma(s)\zeta(s)$.
4. For the binomial distribution give the mean and variance, and state the central limit theorem.
5. Using Lagrange multipliers, maximize $-\sum p_i\ln p_i$ subject to $\sum p_i=1$ and $\sum p_iE_i=\langle E\rangle$.

## Prerequisites

Calculus (multivariable), linear algebra basics, basic probability. Nothing else.

## Detailed topics (checklist)

**Calculus of state functions**
- Exact differentials, partial derivatives, chain rule, the reciprocal and cyclic relations, implicit differentiation, change of variables, Jacobians: $\left(\frac{\partial X}{\partial Y}\right)_Z=\frac{\partial(X,Z)}{\partial(Y,Z)}$ and their algebra (product, inverse, chain rules).
- Taylor expansions, extrema with constraints (Lagrange multipliers), Legendre-transform preliminaries (convex functions, tangent lines).

**Integrals you must know cold**
- Gaussian: $\int_{-\infty}^\infty e^{-ax^2}dx=\sqrt{\pi/a}$, moments $\int x^{2n}e^{-ax^2}dx$.
- Gamma function: $\Gamma(n+1)=n!$, $\Gamma(\tfrac12)=\sqrt\pi$, $\Gamma(\tfrac32)=\tfrac{\sqrt\pi}{2}$.
- Bose and Fermi integrals via the Gamma and zeta functions (see the skip-test): $\zeta(2)=\frac{\pi^2}6$, $\zeta(3)=1.2021$, $\zeta(4)=\frac{\pi^4}{90}$, $\zeta(\tfrac32)=2.612$, $\zeta(\tfrac52)=1.341$.
- Volume of a $d$-dimensional sphere $V_d=\frac{\pi^{d/2}R^d}{\Gamma(d/2+1)}$.

**Probability and combinatorics**
- Probability distributions, mean, variance, moments, the binomial, Poisson and Gaussian distributions, the central limit theorem, why fluctuations scale as $1/\sqrt N$.
- Factorials and binomial coefficients, Stirling's approximation (and when it is accurate), multinomial counting, the number of ways to distribute $q$ quanta among $N$ oscillators $\binom{q+N-1}{q}$.
- Shannon entropy $-\sum p_i\ln p_i$ and its maximization.

**Constants and orders of magnitude (cgs)**

| Quantity | Value |
| --- | --- |
| $k_B$ | $1.381\times10^{-16}$ erg/K ($8.617\times10^{-5}$ eV/K; 1 eV $\leftrightarrow$ 11604 K) |
| $h$, $\hbar$ | $6.626\times10^{-27}$, $1.055\times10^{-27}$ erg s |
| $c$ | $2.998\times10^{10}$ cm/s |
| $m_u$, $m_e$, $m_p$ | $1.661\times10^{-24}$, $9.109\times10^{-28}$, $1.673\times10^{-24}$ g |
| $a=\pi^2k_B^4/15\hbar^3c^3$ | $7.566\times10^{-15}$ erg cm$^{-3}$ K$^{-4}$ |
| $\sigma_{\rm SB}=ac/4$ | $5.670\times10^{-5}$ erg cm$^{-2}$ s$^{-1}$ K$^{-4}$ |
| $e^2$ | $2.307\times10^{-19}$ erg cm |
| $m_ec^2$ | $0.511$ MeV ($=5.93\times10^9$ K$\times k_B$) |

Stellar reference points (approximate): solar centre $T=1.57\times10^7$ K, $\rho=150$ g/cm$^3$, $P=2.3\times10^{17}$ dyn/cm$^2$; white dwarf core $\rho\sim10^6$ to $10^8$ g/cm$^3$; neutron star core $n\sim(2$ to $8)\times0.16$ fm$^{-3}$.

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Schroeder chapter 1 (energy, heat, work; ideal gas, equipartition) |
| Lunch 2 | Schroeder mathematical appendices; Blundell and Blundell on probability |
| Lunch 3 | Swendsen on probability and combinatorics; Stirling's approximation |
| Lunch 4 | A calculus reference for Jacobians and Lagrange multipliers (any multivariable text) |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. The cyclic relation $\left(\frac{\partial x}{\partial y}\right)_z\left(\frac{\partial y}{\partial z}\right)_x\left(\frac{\partial z}{\partial x}\right)_y=-1$ from the total differential.
2. Stirling's formula (the leading terms) from $\ln N!=\sum\ln k$ or from $\Gamma(N+1)$ by the saddle-point method.
3. The Bose and Fermi integrals in terms of $\Gamma$ and $\zeta$ (series expansion of $1/(e^x\mp1)$).
4. Maximum entropy with the normalization and mean-energy constraints gives the Boltzmann form $p_i\propto e^{-\beta E_i}$.
5. The volume of a $d$-dimensional ball using Gaussian integrals.

## Bare-minimum exercises (find matching problems in the books with these keywords)

1. **Jacobians** (partial derivatives, Jacobian method): for $f(x,y)$ show $\left(\frac{\partial f}{\partial x}\right)_z=\left(\frac{\partial f}{\partial x}\right)_y+\left(\frac{\partial f}{\partial y}\right)_x\left(\frac{\partial y}{\partial x}\right)_z$.
2. **Stirling check** (Stirling approximation): compute $\ln N!$ exactly and with Stirling for $N=10,100,1000$; relative errors $\approx1\%$ for $N=10$ with the simplest form, and below $10^{-3}$ with the $\tfrac12\ln2\pi N$ term.
3. **Planck integral:** evaluate $\int_0^\infty\frac{x^3}{e^x-1}dx=\frac{\pi^4}{15}\approx6.494$ numerically and analytically.
4. **Fermi integral:** show $\int_0^\infty\frac{x^3}{e^x+1}dx=\frac{7\pi^4}{120}$ (the factor $7/8$ relative to the Bose integral).
5. **Binomial and Gaussian:** show that the fractional width of the number of heads in $N$ tosses is $\sim1/\sqrt N$; evaluate it for $N=10^{23}$.
6. **Combinatorics:** number of microstates of $N=10$ oscillators holding $q=5$ quanta ($\binom{14}{5}=2002$).
7. **Max entropy:** derive $p_i=e^{-\beta E_i}/Z$ by Lagrange multipliers.
8. **Unit conversions:** find $k_BT$ in keV at $1.57\times10^7$ K ($1.35$ keV), the temperature corresponding to $m_ec^2$ ($5.93\times10^9$ K), and the thermal speed of protons at the solar centre ($v_{\rm rms}=\sqrt{3kT/m}\approx620$ km/s).
9. **Pressure budget at the solar centre:** with $\mu\approx0.85$ compute $P_{\rm gas}=\rho kT/\mu m_u\approx2.3\times10^{17}$ dyn/cm$^2$ and $P_{\rm rad}=aT^4/3\approx1.5\times10^{14}$ dyn/cm$^2$; the ratio is $\sim7\times10^{-4}$.
10. **Photon versus baryon number:** compare $n_\gamma\approx20.3\,T^3$ cm$^{-3}$ with the baryon number density at the solar centre (about $10^{26}$ cm$^{-3}$).

## Optional extension

Prove the saddle-point (Laplace) approximation for a general integral $\int e^{Nf(x)}dx$ and recover Stirling's formula from it. This method returns in every thermodynamic-limit argument.

## Pitfalls

- Mixing the variable held constant in a partial derivative, especially in Jacobian manipulations.
- Using Stirling's formula for small $N$ (it is useless for $N<10$).
- Forgetting the Gamma-function factor $\Gamma(s)$ in the Bose and Fermi integrals.
- Mixing cgs and SI in the radiation constant $a$ and in $e^2$.

## Gate questions

1. Why do fluctuations of extensive quantities vanish relatively as $N\to\infty$?
2. What does the Jacobian method buy you in thermodynamic derivations?
3. Why does the Fermi integral differ from the Bose integral by the factor $1-2^{1-s}$?

## One-page cheat sheet contents

Cyclic and reciprocal relations, Jacobian rules, Gaussian and Gamma integrals, Bose and Fermi integral formulas with $\zeta$ values, Stirling's formula, constants table.
