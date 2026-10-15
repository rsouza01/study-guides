# Module 12: Interacting systems and plasmas

**Books:** Pathria (chapter 10: cluster expansions and the virial expansion; plasma-related topics), Schroeder (chapter 8: systems of interacting particles, virial expansion, van der Waals), Mandl (interacting systems), Swendsen (interacting systems), Callen (van der Waals as a model).
**Time:** 3 weeks.

## Why this matters for stars and EOS

The ideal-gas EOS is only the leading term. Real stellar and compact-star matter is a **plasma** of charged particles:

- **Coulomb corrections** to the pressure and energy are needed to match helioseismic data (percent-level) and are large in white dwarfs and dense stellar cores.
- **Screening** of the Coulomb barrier enhances thermonuclear reaction rates (a few percent in the Sun, a factor of orders of magnitude in dense matter).
- The **plasma coupling parameter** $\Gamma$ tells you whether matter is a weakly coupled gas, a strongly coupled liquid, or a crystal; the **liquid-solid transition** ($\Gamma\approx175$) controls the cooling of white dwarfs.
- **Exchange** effects reduce the pressure of the degenerate electron gas slightly.

## Skip-test (40 minutes, no notes)

1. Write the virial expansion $\frac{P}{nkT}=1+B_2(T)n+B_3(T)n^2+\dots$ and the second virial coefficient $B_2=-2\pi\int_0^\infty(e^{-\beta u(r)}-1)r^2dr$. Evaluate for hard spheres ($B_2=\frac{2\pi}{3}\sigma^3$).
2. Derive the van der Waals equation from a mean-field argument and identify $a$ and $b$.
3. State the Debye-Hueckel results $\kappa_D^2=\frac{4\pi e^2\sum_jn_jZ_j^2}{kT}$, free energy density $f_C=-\frac{kT\kappa_D^3}{12\pi}$, energy density $-\frac{kT\kappa_D^3}{8\pi}$ and pressure $P_C=-\frac{kT\kappa_D^3}{24\pi}$.
4. Define the plasma coupling parameter $\Gamma=\frac{Z^2e^2}{a_ikT}$ with $a_i=\left(\frac{3}{4\pi n_i}\right)^{1/3}$ and state its regimes.
5. For a one-component plasma give the static (Madelung) lattice energy per ion $-0.8959\frac{Z^2e^2}{a_i}$ and the crystallization $\Gamma\approx175$.

## Prerequisites

Modules 06 to 09 and 11 (the Debye model).

## Detailed topics (checklist)

**Imperfect gases**
- The cluster (Mayer) expansion and the virial expansion; $B_2(T)$ for hard spheres and Lennard-Jones potentials; connection to the van der Waals equation; the limits of the expansion.
- Mean-field approach: the van der Waals EOS $P=\frac{NkT}{V-Nb}-\frac{aN^2}{V^2}$; critical constants (Module 05).

**Plasmas**
- **Debye-Hueckel theory:** screened potential $\phi=\frac{Ze}{r}e^{-\kappa_Dr}$, Debye length $\lambda_D=\kappa_D^{-1}$, the number of particles in a Debye sphere, validity $\Gamma\ll1$; the Coulomb correction to the free energy, internal energy, pressure; the *negative* sign (attraction between opposite charges lowers the pressure).
- **Plasma parameter** $\Gamma=\frac{Z^2e^2}{a_ikT}$ and the electron degeneracy parameter; the $(\rho,T)$ plane regimes: weakly coupled ideal gas ($\Gamma\ll1$), strongly coupled liquid ($1\lesssim\Gamma\lesssim175$), Coulomb crystal ($\Gamma\gtrsim175$).
- **One-component plasma (OCP):** point ions in a uniform neutralizing background; ion-sphere radius; the ion-sphere (Wigner-Seitz) energy $-\frac{9}{10}\frac{Z^2e^2}{a_i}$ and the more accurate Madelung (bcc) value $-0.8959\frac{Z^2e^2}{a_i}$; thermal corrections; liquid fits $u(\Gamma)=a\Gamma+b\Gamma^{1/4}+c\Gamma^{-1/4}+d$ (from the literature); the first-order liquid-solid transition near $\Gamma\approx175$.
- **Scale invariance:** the Coulomb energy density $\epsilon_C\propto n^{4/3}$ at fixed $Z$ implies $P_C=\frac13\epsilon_C$.

**Electrons**
- The exchange energy of the degenerate electron gas: $\epsilon_x=-\frac34\left(\frac3\pi\right)^{1/3}e^2n^{4/3}$ and its pressure $P_x=\epsilon_x/3$; for ultra-relativistic electrons $P_x/P_0=-\alpha/\pi$; the Thomas-Fermi model of the neutral atom/ion-sphere (awareness only).
- Electron screening and the effective Coulomb potential between ions in a degenerate background (awareness: Thomas-Fermi screening length).

**Screening of nuclear reactions**
- Weak screening enhancement factor $f=\exp\left(\frac{Z_1Z_2e^2}{\lambda_DkT}\right)$, equivalently $\exp(0.188Z_1Z_2\zeta\rho^{1/2}T_6^{-3/2})$ with $\zeta=\left[\sum\frac{X_i(Z_i^2+Z_i)}{A_i}\right]^{1/2}$ in cgs; the strong-screening limit uses the ion-sphere energy.

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Schroeder chapter 8: interacting gases, virial expansion, van der Waals |
| Lunch 2 | Pathria chapter 10: cluster expansion, virial coefficients |
| Lunch 3 | Mandl and Swendsen: interacting systems and plasmas |
| Lunch 4 | A plasma-physics reference for Debye-Hueckel (any text; Pathria and Landau-Lifshitz, Statistical Physics Part 1, treat it) |
| Week 2 lunches | The one-component plasma and Coulomb crystals |
| Week 3 lunches | Exchange energy, screening of nuclear reactions; review |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. The second virial coefficient and the hard-sphere and van der Waals cases.
2. The Debye-Hueckel screened potential from linearizing the Poisson-Boltzmann equation.
3. The Debye-Hueckel free energy by the charging process and the pressure.
4. The ion-sphere energy $-\frac9{10}\frac{Z^2e^2}{a_i}$ for the OCP.
5. The weak-screening enhancement factor $f=e^{Z_1Z_2e^2/\lambda_DkT}$.

## Bare-minimum exercises (find matching problems with keywords: virial coefficient, van der Waals, Debye length, plasma, screening)

1. **Hard spheres:** show $B_2=\frac{2\pi}{3}\sigma^3$ and $P\approx nkT(1+\frac{2\pi}{3}n\sigma^3)$; for the van der Waals gas $B_2=b-\frac{a}{kT}$ and the Boyle temperature $T_B=\frac{a}{bk}$.
2. **Debye length in the Sun:** at the solar centre ($T=1.57\times10^7$ K, $\sum n_jZ_j^2\sim8\times10^{25}$ cm$^{-3}$) compute $\lambda_D=\sqrt{\frac{kT}{4\pi e^2\sum n_jZ_j^2}}\approx3\times10^{-9}$ cm and compare with the mean interparticle spacing ($\approx1.6\times10^{-9}$ cm): the Debye sphere contains only a few particles, so Debye-Hueckel is marginal.
3. **Coupling parameter:** at the solar centre $\Gamma\approx0.07$ for protons; in the core of a carbon white dwarf ($\rho=10^6$, $T=10^7$ K) $\Gamma\approx36$ (liquid); compute the temperature at which it crystallizes ($\Gamma=175$): $T\approx2\times10^6$ K.
4. **Debye-Hueckel correction:** compute $\frac{P_C}{n_{\rm tot}kT}=-\frac{\kappa_D^3}{24\pi n_{\rm tot}}$ at the solar centre (about $-4\times10^{-3}$, with $n_{\rm tot}\approx10^{26}$ cm$^{-3}$); show that it scales as $\Gamma^{3/2}$.
5. **Screening enhancement:** $f=\exp\left(\frac{Z_1Z_2e^2}{\lambda_DkT}\right)$ for $p+p$ at the solar centre ($\approx1.03$ to $1.05$) and for $^{12}$C$+^{12}$C at the same $T$ ($Z_1Z_2=36$; the exponent becomes large, signalling that weak screening is no longer adequate).
6. **Madelung energy:** compute $\frac{E_L}{N_ikT}=-0.8959\Gamma$ for the carbon core above and the correction to the electron pressure $\frac{P_L}{P_e}=\frac{\epsilon_L}{3P_e}\approx-3\%$ for $\rho=10^6$ g/cm$^3$ (use $P_e\approx2.6\times10^{22}$ dyn/cm$^2$); explain the sign.
7. **Exchange pressure:** show $\frac{P_x}{P_0}=-\frac\alpha\pi\approx-2.3\times10^{-3}$ for ultra-relativistic electrons.
8. **Ion-sphere versus Debye-Hueckel:** sketch $u(\Gamma)/kT$: $-\frac{\sqrt3}{2}\Gamma^{3/2}$ for small $\Gamma$ and $-0.9\Gamma$ for large $\Gamma$; locate the crossing near $\Gamma\sim1$.
9. **Scale invariance:** show $P_C=\frac13\epsilon_C$ for any contribution $\epsilon_C\propto n^{4/3}$ ($P=n^2\,d(\epsilon/n)/dn$).
10. **Pressure ionization (qualitative):** argue why Coulomb interactions and the finite size of atoms make the Saha formula fail at high density, and estimate the density at which the atomic size equals the interparticle spacing for hydrogen ($\rho\sim1$ g/cm$^3$).

## Optional extension

Do a Metropolis Monte Carlo of the one-component plasma with a few hundred ions in a periodic box (with Ewald summation) and verify that $u(\Gamma)$ interpolates between Debye-Hueckel and the Madelung limit (see Module 16).

## Pitfalls

- Using Debye-Hueckel at $\Gamma\gtrsim1$.
- Mixing up the ion-sphere radius $a_i$ with the electron-sphere radius $a_e$.
- Forgetting that the Coulomb corrections are negative.
- Using the virial expansion for dense or strongly coupled matter.

## Gate questions

1. Why is the Coulomb correction to the pressure negative, and why does it scale as $\Gamma^{3/2}$ in the weak-coupling limit?
2. How do you know when a plasma is a gas, a liquid or a crystal?
3. Why does screening enhance nuclear reaction rates?

## One-page cheat sheet contents

Virial expansion; van der Waals; Debye-Hueckel quantities; $\Gamma$ regimes; ion-sphere and Madelung energies; exchange pressure; screening factor.
