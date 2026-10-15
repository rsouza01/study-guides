# Module 16: Readiness test and mini-projects

**Books:** all.
**Time:** 3 weeks (one week for the derivation checklist, two weeks for the four projects).

## Goal

Decide with evidence whether you can use thermodynamics and statistical mechanics fluently for stellar and compact-star equations of state: that you can reproduce the key derivations without notes, solve mixed problems under time pressure, and have built four small self-contained programs that make the central ideas concrete.

## Part 1: the 30-derivation checklist (no notes, 15 to 25 minutes each)

Mark each when you can do it from a blank page. Do four per evening, in a different order each week.

**Thermodynamics (Modules 01 to 05)**
1. The cyclic and reciprocal relations; the Jacobian rules.
2. The Euler relation and the Gibbs-Duhem relation from homogeneity.
3. The four potentials and their differentials; the four Maxwell relations.
4. $C_P-C_V=TV\alpha^2/\kappa_T$ and $\kappa_T-\kappa_S=TV\alpha^2/C_P$.
5. $(\partial U/\partial V)_T=T(\partial P/\partial T)_V-P$ for ideal gas and radiation.
6. Stability conditions $C_V>0$, $\kappa_T>0$ from the second law.
7. $\Gamma_1=\chi_\rho+\frac{P}{\rho Tc_V}\chi_T^2$ and $\nabla_{\rm ad}=\frac{P\delta}{\rho Tc_P}$.
8. $\Gamma_1$ and $\nabla_{\rm ad}$ of gas plus radiation as functions of $\beta$ (with limits).
9. The Saha equation from $\mu_e+\mu_{i+1}=\mu_i$.
10. The Clausius-Clapeyron equation; the van der Waals critical constants.

**Statistical mechanics (Modules 06 to 09)**
11. Equal temperature from maximizing $\Omega_1\Omega_2$; the $1/\sqrt N$ width.
12. The Sackur-Tetrode entropy including $1/N!$.
13. $F=-kT\ln Z$ and $\langle\Delta E^2\rangle=kT^2C_V$.
14. The Maxwell speed distribution and its moments.
15. Two-level and oscillator heat capacities.
16. The Gamow peak: $E_0=(bkT/2)^{2/3}$ and its width.
17. The grand canonical $\Omega=-PV$ and $\mu=kT\ln(n\lambda^3)$.
18. FD and BE distributions from a single-orbital Gibbs sum.
19. The density of states (non-relativistic and massless) and $P=\frac23\frac UV$, $\frac13\frac UV$.
20. The first quantum correction $\frac{P}{nkT}=1\pm\frac{n\lambda^3}{2^{5/2}g}$.

**Degenerate, radiative and interacting matter (Modules 10 to 15)**
21. $T=0$ Fermi gas: $n,E_F,U,P$ in both relativistic limits.
22. The Sommerfeld expansion: $\mu(T)$, $C_V$, thermal pressure correction.
23. Planck's law, $a$, $P=u/3$, $n_\gamma$ and entropy per photon.
24. The Debye heat capacity (low and high $T$).
25. Debye-Hueckel: $\kappa_D$, $f_C$, $P_C$; $\Gamma$ and the Madelung energy.
26. The mean-field Ising model and Landau theory results.
27. The Maxwell construction and the two-charge Gibbs conditions.
28. The radiative conductivity $K_{\rm rad}=\frac{4acT^3}{3\kappa\rho}$; the Wiedemann-Franz law.
29. The virial theorem, $E(\Gamma)$, negative specific heat, and $\Gamma>\frac43$.
30. The Schwarzschild criterion from the entropy gradient; $Y_p=\frac19$ in ultra-relativistic beta equilibrium.

**Passing criterion:** at least 26 of 30 done cleanly, and the remaining four understood after one reading.

## Part 2: four mini-projects (Python, standalone)

Each project is 100 to 250 lines. Keep the code and a one-page result note.

### Project 1: ionization and the adiabatic exponents of a hydrogen-helium mixture

- **Task:** build a thermodynamically consistent model of an ideal mixture of H, H$^+$, He, He$^+$, He$^{2+}$ and electrons at given $(\rho,T)$ with the Saha equations (use $X=0.74$, $Y=0.25$ and ignore metals), plus radiation.
- **Steps:** (1) solve the Saha equations for the ionization fractions over $T=10^3$ to $10^6$ K at $\rho=10^{-7}$ g/cm$^3$; (2) write the free energy (or the pressure and internal energy including the ionization energies) and compute $P$, $u$, $s$; (3) compute $\chi_\rho$, $\chi_T$, $c_V$, $c_P$, $\Gamma_1$ and $\nabla_{\rm ad}$ by numerical differentiation, or by analytic formulae; (4) plot $\nabla_{\rm ad}(T)$ and $\Gamma_1(T)$.
- **Checks:** fully neutral and fully ionized limits give $\nabla_{\rm ad}=0.4$ and $\Gamma_1=5/3$; $\nabla_{\rm ad}$ dips to about $0.1$ and $\Gamma_1$ to about $1.2$ in the hydrogen ionization zone; the Maxwell relation $(\partial s/\partial\rho)_T=-\rho^{-2}(\partial P/\partial T)_\rho$ holds to $10^{-6}$.

### Project 2: the electron gas at arbitrary degeneracy and relativity

- **Task:** compute $n$, $P$, $u$ for an electron gas of arbitrary $\eta=\mu/kT$ and $\theta=kT/m_ec^2$ by numerical quadrature of the Fermi-Dirac integrals (momentum integrals with the exact dispersion relation).
- **Steps:** (1) reproduce the four limits (non-relativistic/ultra-relativistic times non-degenerate/degenerate) with errors below $10^{-6}$; (2) compare with the exact $T=0$ formula $P=\frac{m^4c^5}{24\pi^2\hbar^3}[x(2x^2-3)\sqrt{1+x^2}+3\sinh^{-1}x]$; (3) check the Sommerfeld coefficients $\mu(T)$, $C_V$ and the thermal pressure correction numerically; (4) at fixed density $\rho/\mu_e$ solve for $\eta(T)$ and plot the degeneracy boundary in the $(\rho,T)$ plane, marking the $x=1$ line and the pair-production region; (5) verify $\Gamma_1\to5/3$ and $\to4/3$ in the two degenerate limits.
- **Check:** $\mu(T)$ and $C_V$ agree with the Sommerfeld expansion for $T/T_F<0.1$ to better than a percent; the thermodynamic Maxwell relation holds.

### Project 3: Coulomb corrections in the density-temperature plane

- **Task:** add the Debye-Hueckel, exchange and ion-sphere (Madelung) corrections to the ideal-gas-plus-degenerate-electron EOS for a carbon plasma and a hydrogen plasma.
- **Steps:** (1) compute $\Gamma(\rho,T)$ and the line $\Gamma=1$ and $\Gamma=175$; (2) compute the fractional corrections to the pressure, $\Delta P/P$, as maps over $\rho=10^{-2}$ to $10^{8}$ g/cm$^3$ and $T=10^5$ to $10^9$ K; (3) identify the regions where Debye-Hueckel is valid ($\Gamma\ll1$), where the ion-sphere model holds ($\Gamma\gg1$) and where interpolation is needed; (4) compute the screening factor $f=\exp(Z_1Z_2e^2/\lambda_DkT)$ for $p+p$ along the solar profile (use $T=1.57\times10^7$ K, $\rho=150$ g/cm$^3$).
- **Check:** $\Delta P/P\approx-3\%$ for carbon at $\rho=10^6$ g/cm$^3$, $T=10^7$ K (ion-sphere); $\Gamma\approx36$ there; $f\approx1.03$ to $1.05$ at the solar centre.

### Project 4: Monte Carlo for a classical fluid and the Ising model

- **Task:** a Metropolis Monte Carlo code for (a) the 2D Ising model and (b) a fluid of hard disks or Lennard-Jones particles in two or three dimensions.
- **Steps:** (1) for the Ising model measure $\langle|m|\rangle$ and the specific heat on lattices $L=16,32,64$ and locate $T_c=2.269J/k$ (the exact 2D value) versus the mean-field $4J/k$; (2) for the fluid measure $P(\rho)$ at fixed $T$ from the virial theorem and compare with the virial expansion $P/(nkT)=1+B_2n+B_3n^2$ (compute $B_2$ from the potential) at low density; (3) check energy fluctuations: $C_V=\langle\Delta E^2\rangle/kT^2$ equals the numerical derivative of $\langle E\rangle$.
- **Check:** the Ising $T_c$ within a few percent of 2.269; $B_2$ from the simulation within errors of the integral; the fluctuation relation to a few percent.

## Part 3: mock exam (4 hours, closed book)

| Section | Content | Time |
| --- | --- | --- |
| A | Two thermodynamic-identity problems (Maxwell relations, response functions, $\Gamma_1,\nabla_{\rm ad}$) | 35 min |
| B | One chemical-equilibrium problem (Saha, pairs or beta equilibrium) | 35 min |
| C | One ensemble problem (canonical or grand canonical, with a closed-form partition function) | 40 min |
| D | One degenerate Fermi gas problem (both limits, Sommerfeld, numbers for a white dwarf) | 45 min |
| E | One radiation or phonon problem (Planck, Debye, entropy per photon) | 30 min |
| F | One plasma or phase-transition problem (Debye-Hueckel, $\Gamma$, Landau or Maxwell construction) | 35 min |
| G | One stellar-thermodynamics problem (virial theorem, stability, Schwarzschild, thermal runaway) | 20 min |

Grade with a rubric: 2 points for the setup, 2 for the key step, 1 for the final number or interpretation. Aim for 70 percent or more.

## Part 4: what to do if you fall short

| Weak area | Fix |
| --- | --- |
| Thermodynamic identities | Redo Module 03 derivations 1 to 5 and the Jacobian method of Module 01 |
| Adiabatic coefficients | Redo Module 04 derivations 2 to 4 and Project 1 |
| Counting and entropy | Redo Module 06 derivations 1 to 4 |
| Canonical and grand canonical | Redo Modules 07 and 08 derivations 1 to 4 |
| Degenerate gases | Redo Module 10 derivations 1 to 4 and Project 2 |
| Plasmas | Redo Module 12 derivations 2 to 5 and Project 3 |
| Stellar thermodynamics | Redo Module 15 derivations 1 to 4 |

## Pitfalls

- Treating the checklist as recognition rather than recall: if you can only *read* a derivation, you have not passed it.
- Spending all the time on projects and none on closed-book derivations.
- Skipping the consistency tests (Maxwell relations) on your computed EOS: they are the point of the projects.

## Gate questions

1. Which three results of this guide will you use most often in stellar and compact-star EOS work, and why?
2. Which of the 30 derivations is weakest, and what is your plan to fix it?
3. What would you do differently in a second pass of this guide?
