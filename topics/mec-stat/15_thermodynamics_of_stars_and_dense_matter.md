# Module 15: Thermodynamics of stars and dense matter

**Books:** Blundell and Blundell (astrophysical applications: stars, the virial theorem, white dwarfs), Callen (stability, extremum principles), Pathria (chapter 8 on white dwarf stars; chapter 9 on relativistic gases in equilibrium), Schroeder (applications), Mandl.
**Time:** 3 weeks. This module ties the whole guide to stellar and compact-star physics.

## Why this matters for stars and EOS

- **Self-gravitating matter** does not obey ordinary thermodynamic intuition: it has **negative specific heat**, its stability depends on the adiabatic exponent, and its equilibrium is dynamical, not thermodynamic.
- **Convective stability** is a thermodynamic statement about the entropy gradient (Schwarzschild and Ledoux criteria).
- **Thermal runaway** in degenerate matter (the helium flash, novae, Type Ia ignition) is a consequence of the equation of state: pressure that does not respond to temperature.
- **Multi-component equilibrium** (nuclear statistical equilibrium, beta equilibrium, pair equilibrium, with several conserved charges) is how the composition of stellar and neutron-star matter is determined.

## Skip-test (40 minutes, no notes)

1. Derive the virial theorem for a self-gravitating ideal gas $2K+\Omega=0$, and for $P=(\Gamma-1)u$ the general form $3(\Gamma-1)U=-\Omega$ and total energy $E=\frac{3\Gamma-4}{3(\Gamma-1)}\Omega$.
2. Show that a monatomic ideal-gas star has negative heat capacity $C=-\frac32Nk$ and explain why this is not a thermodynamic inconsistency.
3. Show that dynamical stability against homologous contraction requires $\Gamma>\frac43$.
4. Derive the Schwarzschild criterion in terms of the specific entropy gradient: $\frac{ds}{dr}>0\Leftrightarrow\nabla<\nabla_{\rm ad}$ (stable), using $ds=c_P(d\ln T-\nabla_{\rm ad}d\ln P)$.
5. Minimize the Gibbs energy with the constraints of baryon number and charge conservation to obtain $\mu_i=A_i\mu_B+Z_i\mu_Q$ and apply it to $n\leftrightarrow p+e^-+\bar\nu_e$ (escaping neutrinos).

## Prerequisites

Modules 03 to 05, 08 to 12.

## Detailed topics (checklist)

**Virial theorem and energetics**
- Hydrostatic equilibrium $\frac{dP}{dr}=-\frac{Gm\rho}{r^2}$ and the integral form $3\int P\,dV=-\Omega$; the potential energy of a polytrope $\Omega=-\frac{3}{5-n}\frac{GM^2}{R}$; the total energy of a bound star $E=\frac{3\Gamma-4}{3(\Gamma-1)}\Omega<0$ for $\Gamma>4/3$ and $\to0$ as $\Gamma\to4/3$ (radiation-dominated or ultra-relativistic).
- **Negative specific heat:** $E=-U$ for $\Gamma=5/3$, so removing energy raises the temperature; the Kelvin-Helmholtz timescale $\frac{|E|}{L}$; why this does not contradict thermodynamic stability (additivity and the thermodynamic limit fail for long-range forces).
- **Gravothermal collapse:** negative heat capacity makes a self-gravitating system with energy loss run away (awareness; globular clusters).

**Stability**
- Dynamical stability of a star: the energy $E(R)=\frac{A}{R^{3(\Gamma-1)}}-\frac BR$; a minimum exists only if $\Gamma>4/3$; the adiabatic index of the *whole* mixture ($\Gamma_1$ from Module 04) decides; implications: radiation-dominated massive stars, ionization zones ($\Gamma_1<4/3$ regions are locally unstable), relativistic degenerate stars.
- **Thermal stability of nuclear burning:** with $\epsilon\propto\rho^\lambda T^\nu$ at constant pressure, $\frac{d\ln\epsilon}{d\ln T}=\nu-\lambda\delta$ with $\delta=-\left(\frac{\partial\ln\rho}{\partial\ln T}\right)_P$. For an ideal gas $\delta=1$ and expansion cools the layer (a thermostat); for degenerate matter $\delta\to0$ and the energy generation grows with $T$ unchecked: **thermonuclear runaway**. Thin burning shells at constant pressure can be unstable even for ideal gases.

**Convective stability as thermodynamics**
- A displaced fluid element conserves its entropy; stability $\Leftrightarrow$ the specific entropy increases outward: $\nabla<\nabla_{\rm ad}$ (Schwarzschild); with a composition gradient the **Ledoux** criterion $\nabla<\nabla_{\rm ad}+\frac{\varphi}{\delta}\nabla_\mu$ (with $\varphi=(\partial\ln\rho/\partial\ln\mu)_{P,T}$); the entropy per baryon as a label of the state of a star's core.

**Multi-component equilibrium**
- Maximizing entropy (or minimizing $G$) at fixed conserved charges: Lagrange multipliers, $\mu_i=\sum_a q_i^{(a)}\mu_a$ for charges $a=B,Q,L,\dots$; examples: $\mu_n=\mu_p+\mu_e$ (beta equilibrium, neutrinos escaping), $\mu_{e^-}=-\mu_{e^+}$, $\mu_\gamma=0$.
- **Nuclear statistical equilibrium (NSE):** nuclei in equilibrium with nucleons: $\mu_i=Z_i\mu_p+N_i\mu_n$, giving $\frac{n_i}{n_p^{Z_i}n_n^{N_i}}=\frac{G_i}{2^{A_i}}A_i^{3/2}\left(\frac{2\pi\hbar^2}{m_ukT}\right)^{3(A_i-1)/2}e^{B_i/kT}$ with binding energy $B_i$ and partition function $G_i$: the competition between binding energy and entropy.
- **Degenerate $npe$ matter in beta equilibrium (free gases):** charge neutrality $p_{Fp}=p_{Fe}$ and $\mu_n=\mu_p+\mu_e$; in the ultra-relativistic limit $p_{Fn}=2p_{Fp}$, so $\frac{n_n}{n_p}=8$ and the proton fraction is $Y_p=\frac19$.

**Building an EOS consistently (workflow)**
- Choose $F(\rho,T,\{X_i\})=F_{\rm ions}+F_{\rm electrons}+F_{\rm rad}+F_{\rm Coulomb}+F_{\rm ionization}$; derive $P=-\partial F/\partial V$, $s=-\partial F/\partial T$, $\mu_i=\partial F/\partial N_i$ analytically or by differentiation; check the Maxwell relations; compute $\Gamma_1,\nabla_{\rm ad},c_P$ from the second derivatives. A pressure and an energy fitted separately will generally not satisfy the identities.

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Blundell and Blundell: virial theorem, stars as thermodynamic systems |
| Lunch 2 | Pathria chapter 8: statistical equilibrium of white dwarf stars; the Chandrasekhar limit |
| Lunch 3 | Callen: stability; Pathria chapter 9: relativistic gases and equilibrium with pairs |
| Lunch 4 | Schroeder and Pathria: chemical equilibrium and multi-component systems (review Module 05) |
| Week 2 lunches | Convective stability (derive from entropy); thermal stability of burning shells |
| Week 3 lunches | NSE and beta equilibrium; assembling an EOS from a free energy; review |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. The virial theorem and the total energy as a function of $\Gamma$.
2. The stability criterion $\Gamma>4/3$ from $E(R)$.
3. The Schwarzschild criterion from the entropy gradient.
4. $\frac{d\ln\epsilon}{d\ln T}\big|_P=\nu-\lambda\delta$ and its consequences.
5. The conditions $\mu_i=A_i\mu_B+Z_i\mu_Q$ from the constrained maximization of entropy; the NSE abundance formula.

## Bare-minimum exercises (find matching problems with keywords: virial theorem, stars, white dwarf, negative heat capacity, chemical equilibrium)

1. **Energies of the Sun:** with $\Omega=-\frac32\frac{GM^2}{R}$ (an $n=3$ polytrope) and $\frac{GM_\odot^2}{R_\odot}=3.8\times10^{48}$ erg compute $\Omega\approx-5.7\times10^{48}$ erg, $U=-\Omega/2\approx2.9\times10^{48}$ erg, $E=-U$; the Kelvin-Helmholtz time $|E|/L_\odot\approx2.4\times10^7$ yr.
2. **Negative specific heat:** show that for a virialized ideal gas of $N$ particles with $K=\frac32NkT_{\rm vir}$ the total energy is $E=-K$ and $C=\frac{dE}{dT_{\rm vir}}=-\frac32Nk$; explain what happens when such a system is placed in contact with a heat bath.
3. **Dynamical stability:** with $E(R)=\frac{A}{R^{3(\Gamma-1)}}-\frac BR$ show the extremum is a minimum only for $\Gamma>4/3$ and find $R_{\rm eq}$; relate to the star: radiation-dominated gas has $\Gamma_1\to4/3$ (marginal), ionization zones have $\Gamma_1<4/3$ locally.
4. **Schwarzschild from entropy:** derive $\frac{ds}{dr}=c_P\frac{d\ln P}{dr}(\nabla-\nabla_{\rm ad})$ and conclude stability for $\nabla<\nabla_{\rm ad}$.
5. **Ledoux:** extend to a mixture with a composition gradient (the entropy now also depends on $\ln\mu_{\rm mol}$ at fixed $P,T$); derive the stability condition $\nabla<\nabla_{\rm ad}+\frac{\varphi}{\delta}\nabla_\mu$ and interpret.
6. **Thermal runaway:** show that at constant pressure $\frac{d\ln\epsilon}{d\ln T}=\nu-\lambda\delta$; evaluate for the triple-alpha reaction ($\nu\approx40$, $\lambda=2$) in (a) an ideal gas ($\delta=1$): $38$, and (b) fully degenerate matter ($\delta\to0$): $40$ with no pressure relief; explain why only the degenerate case runs away, using the heat capacity and the expansion.
7. **Beta equilibrium (ultra-relativistic limit):** show $Y_p=1/9$ from $p_{Fn}=2p_{Fp}$; then solve $\sqrt{p_{Fn}^2c^2+m_n^2c^4}=\sqrt{p_{Fp}^2c^2+m_p^2c^4}+\sqrt{p_{Fp}^2c^2+m_e^2c^4}$ numerically for the proton fraction at several densities and find it is of order one percent or less in the non-relativistic region.
8. **Lagrange multipliers:** derive $\mu_n=\mu_B$, $\mu_p=\mu_B+\mu_Q$, $\mu_e=-\mu_Q$ and the beta equilibrium condition; add trapped neutrinos with a lepton number multiplier and show $\mu_n+\mu_{\nu}=\mu_p+\mu_e$.
9. **NSE formula:** derive the abundance relation above from $\mu_i=Z_i\mu_p+N_i\mu_n$ and the ideal-gas $\mu_i=m_ic^2-B_i+kT\ln(n_i\lambda_i^3/G_i)$; evaluate the exponent $B_i/kT$ for $^4$He ($B=28.3$ MeV) at $T=5\times10^9$ K ($kT=0.43$ MeV) and compare with the entropy factor $\left(\frac{2\pi\hbar^2}{m_ukT}\right)^{3(A-1)/2}n^{A-1}$.
10. **Consistency:** given $F(\rho,T)=F_{\rm ion}+F_{\rm rad}$ with $F_{\rm ion}=-NkT[\ln(V/N\lambda^3)+1]$ and $F_{\rm rad}=-\frac13aVT^4$ derive $P,s,u$, check the Maxwell relation and compute $\Gamma_1$ and $\nabla_{\rm ad}$ as functions of $\beta$.

## Optional extension

Show that for the Eddington standard model ($\beta$ constant) the star is an $n=3$ polytrope and relate the mass-dependence of $1-\beta$ to the thermodynamics of Module 04; then use the result to see why stars above $\sim100M_\odot$ are close to the stability limit.

## Pitfalls

- Applying thermodynamic stability conditions (positive heat capacity) to a self-gravitating system.
- Forgetting that the star's stability depends on the *adiabatic* index of the mixture including ionization and radiation.
- Using constant-volume heat capacity where the thin-shell problem is at constant pressure.
- Using the NSE formula outside its range (it needs $T\gtrsim4\times10^9$ K).

## Gate questions

1. Why does a star heat up when it loses energy?
2. Why can an ideal-gas star burn nuclear fuel stably while a degenerate core cannot?
3. What conserved quantities determine the number of independent chemical potentials in a mixture of reacting species?

## One-page cheat sheet contents

Virial theorem and $E(\Gamma)$; stability criterion; Schwarzschild and Ledoux; $d\ln\epsilon/d\ln T$ at constant $P$; conserved-charge chemical potentials; NSE formula; $Y_p=1/9$ result.
