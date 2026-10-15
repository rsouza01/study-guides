# Module 10: Degenerate Fermi gases

**Books:** Pathria (chapter 8: ideal Fermi systems, including the Sommerfeld expansion, the electron gas and the statistical equilibrium of white dwarf stars; chapter 9 for relativistic gases), Schroeder (chapter 7: degenerate Fermi gases), Blundell and Blundell (Fermi gas, white dwarfs), Mandl (Fermi gas), Callen (quantum fluids).
**Time:** 3 weeks. This is the most important module for white dwarfs, neutron stars and degenerate stellar cores.

## Why this matters for stars and EOS

- **White dwarfs, neutron stars, red giant cores, the cores of stars at helium ignition** are supported by degenerate fermions. Their pressure depends only on density (not temperature) at zero temperature, and the thermal corrections control cooling and runaway burning.
- The transition from **non-relativistic** ($P\propto\rho^{5/3}$, $\Gamma=5/3$) to **ultra-relativistic** ($P\propto\rho^{4/3}$, $\Gamma=4/3$) degeneracy is what sets the Chandrasekhar mass.
- **Partial degeneracy**, **electron-positron pair equilibrium** and **degenerate neutron matter** need the full Fermi-Dirac machinery.
- The heat capacity and entropy of degenerate electrons set the thermal behavior of a white dwarf core.

## Skip-test (40 minutes, no notes)

1. For $g_s=2$ fermions at $T=0$ derive $n=\frac{p_F^3}{3\pi^2\hbar^3}$, $E_F=\frac{p_F^2}{2m}$, $U=\frac35NE_F$, $P=\frac25nE_F=\frac{(3\pi^2)^{2/3}\hbar^2}{5m}n^{5/3}$.
2. Ultra-relativistic $T=0$: $E_F=p_Fc$, $U=\frac34NE_F$, $P=\frac14np_Fc=\frac{(3\pi^2)^{1/3}}{4}\hbar c\,n^{4/3}$.
3. State the Sommerfeld expansion $\int_0^\infty H(\epsilon)f\,d\epsilon=\int_0^\mu H\,d\epsilon+\frac{\pi^2}{6}(kT)^2H'(\mu)+\dots$ and derive $\mu=E_F\left[1-\frac{\pi^2}{12}\left(\frac{kT}{E_F}\right)^2\right]$, $C_V=\frac{\pi^2}{2}Nk\frac{kT}{E_F}$.
4. Write the general $T=0$ relativistic pressure $P=\frac{m^4c^5}{24\pi^2\hbar^3}\left[x(2x^2-3)\sqrt{1+x^2}+3\sinh^{-1}x\right]$, $x=\frac{p_F}{mc}$, and its two limits.
5. Estimate the Chandrasekhar scaling mass $M\sim\left(\frac{\hbar c}{G}\right)^{3/2}\frac{1}{(\mu_em_u)^2}$ (order of magnitude).

## Prerequisites

Modules 06 to 09, and the Sommerfeld-type integrals of Module 01.

## Detailed topics (checklist)

**The degenerate gas at $T=0$**
- Fermi momentum, Fermi energy, Fermi temperature; the density relation $p_F=\hbar(3\pi^2n)^{1/3}$ ($g_s=2$); the relativity parameter $x=p_F/mc$ and its meaning: $x=1$ at $\rho/\mu_e=9.74\times10^5$ g/cm$^3$ for electrons ($x_n=1$ at $\rho\approx6\times10^{15}$ g/cm$^3$ for neutrons).
- Pressure and energy of the non-relativistic and ultra-relativistic limits; the **polytropic** forms $P=K_1(\rho/\mu_e)^{5/3}$ with $K_1=1.0036\times10^{13}$ and $P=K_2(\rho/\mu_e)^{4/3}$ with $K_2=1.2435\times10^{15}$ (cgs); the exact $T=0$ relativistic expressions.
- The role of $\mu_e$: for fully ionized matter electron density $n_e=\rho/(\mu_em_u)$; $\mu_e=2$ for helium, carbon, oxygen; the ions contribute negligible pressure but all the mass.

**Finite temperature**
- The Sommerfeld expansion: $\mu(T)$, entropy $S=\frac{\pi^2}{2}Nk\frac{kT}{E_F}$, heat capacity $C_V=\frac{\pi^2}{2}Nk\frac{kT}{E_F}$, thermal energy $\frac{\pi^2}{4}\frac{N(kT)^2}{E_F}$, pressure $P=P_0\left[1+\frac{5\pi^2}{12}\left(\frac{kT}{E_F}\right)^2\right]$ (non-relativistic).
- The **degeneracy boundary** in the $(\rho,T)$ plane: $kT\sim E_F$, i.e. $T_F\approx3\times10^5\left(\frac{\rho}{\mu_e}\right)^{2/3}$ K in the non-relativistic regime (derive and check); the transition region $T\sim T_F$ needs the full Fermi-Dirac integrals.
- **Partial degeneracy:** $n=\frac{g_s}{2\pi^2}\left(\frac{2mkT}{\hbar^2}\right)^{3/2}F_{1/2}(\eta)$, $P=\frac{g_s}{3\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}(kT)^{5/2}F_{3/2}(\eta)$ (non-relativistic); the relativistic generalization with $\theta=kT/mc^2$.
- **Electron-positron pairs:** when $kT\gtrsim0.1mc^2$ ($T\gtrsim6\times10^8$ K) pairs matter; net electron number $n_--n_+$ fixed by charge neutrality; the chemical potentials satisfy $\mu_+=-\mu_-$ (with rest mass included).

**Heat capacity and stellar relevance**
- Electron heat capacity $\propto T$ is small compared to the ion heat capacity $\frac32k$ per ion, so a white dwarf core cools mostly through its ions.
- **Why a degenerate gas resists expansion cooling:** $P$ is nearly independent of $T$, so heating does not make the gas expand and cool (the origin of thermonuclear runaway in degenerate cores; see Module 15).

**Other fermion gases**
- Neutrons in neutron stars: non-interacting limit (the interacting problem belongs to nuclear physics); mixtures of species in chemical equilibrium (Module 15); neutrinos as massless fermions ($g_s=1$ per flavour and antiparticle); the free-fermion gas as a reference.

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Schroeder chapter 7: degenerate Fermi gas, density of states, Fermi energy |
| Lunch 2 | Pathria chapter 8: thermodynamic behaviour of the ideal Fermi gas, Sommerfeld expansion |
| Lunch 3 | Pathria chapter 8: the statistical equilibrium of white dwarf stars; Blundell and Blundell on white dwarfs |
| Lunch 4 | Pathria chapter 9 (relativistic gases); Mandl on the Fermi gas |
| Week 2 lunches | Review; relativistic degenerate formulas |
| Week 3 lunches | Partial degeneracy, pair equilibrium (Pathria on relativistic gases) |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. $n$, $E_F$, $U$, $P$ at $T=0$ for non-relativistic and ultra-relativistic dispersion.
2. The general $T=0$ relativistic pressure formula by integrating $P=\frac13\int pv\,n(p)d^3p$.
3. The Sommerfeld expansion to second order and $\mu(T)$, $C_V$, $S$.
4. The thermal correction to the pressure.
5. The Chandrasekhar-type scaling mass from balancing gravitational and degeneracy energy.

## Bare-minimum exercises (find matching problems with keywords: Fermi gas, Fermi energy, white dwarf, degenerate pressure, Sommerfeld)

1. **Numbers for a white dwarf core:** $\rho=10^6$ g/cm$^3$, $\mu_e=2$: $n_e=3\times10^{29}$ cm$^{-3}$, $p_F/m_ec=x\approx0.8$, $E_F^{\rm nonrel}=\frac{p_F^2}{2m}\approx0.16$ MeV, $T_F\approx1.9\times10^9$ K; check the relation $T_F\approx3\times10^5(\rho/\mu_e)^{2/3}$ K.
2. **Pressure comparison:** compute $P$ by the non-relativistic formula ($\approx3\times10^{22}$ dyn/cm$^2$) and by the exact relativistic one ($\approx2.6\times10^{22}$) at $x=0.8$; explain the difference.
3. **Chandrasekhar scaling:** for a star with $N$ electrons of radius $R$ the degeneracy energy per electron is $\sim\hbar c\left(N/R^3\right)^{1/3}$ (ultra-relativistic) and the gravitational energy per electron is $\sim-\frac{GM m_u\mu_e}{R}$; equate the $R$ dependence to get $N_{\rm max}\sim\left(\frac{\hbar c}{Gm_u^2}\right)^{3/2}$ and $M\sim\frac{(\hbar c/G)^{3/2}}{(\mu_em_u)^2}\approx0.5\,M_\odot$ for $\mu_e=2$, within a factor $\sim3$ of the accurate $1.46\,M_\odot$.
4. **Thermal correction to the pressure:** for $T=10^7$ K and $\rho=10^6$ g/cm$^3$ find $\frac{\Delta P}{P}\approx\frac{5\pi^2}{12}\left(\frac{kT}{E_F}\right)^2\approx10^{-4}$, utterly negligible; compare with the ion pressure $n_ikT$ (about $3\times10^{-3}$ of $P_e$ for a carbon core), which is larger than the electron thermal correction.
5. **Heat capacity budget:** for a carbon white dwarf core at $T=10^7$ K compare $C_V^{\rm el}=\frac{\pi^2}{2}N_ek\frac{kT}{E_F}$ (with $kT/E_F\approx5\times10^{-3}$) and $C_V^{\rm ion}=\frac32N_ik$ with $N_i=N_e/6$: the ions dominate by a factor $\sim10$.
6. **Sommerfeld:** verify the second-order expression of $\mu(T)$ against a numerical solution of $N=\int g f\,d\epsilon$ at fixed $n$ for $T/T_F=0.1,0.3,1$ and note where the expansion fails.
7. **Degeneracy boundary:** at $\rho=100$ g/cm$^3$, $\mu_e=1.5$ find $T_F\approx6.8\times10^{6}$ K (compare $kT$ at the solar centre) and decide whether solar-core electrons are degenerate (they are only mildly so).
8. **Pairs:** for a gas at $T=10^{10}$ K with negligible net charge, $n_-=n_+$; estimate $n_\pm$ with the massless non-degenerate fermion result $n=\frac34\frac{\zeta(3)}{\pi^2}g_s\left(\frac{kT}{\hbar c}\right)^3$ ($g_s=2$; order-of-magnitude only, since $kT=0.86$ MeV is not far above $m_ec^2$) and show $n_\pm/n_\gamma\approx0.75$.
9. **Neutron gas:** show that a free neutron gas has $x_n=1$ at $\rho\approx6\times10^{15}$ g/cm$^3$ and $E_F\approx$ 60 MeV at nuclear saturation density $n_0=0.16$ fm$^{-3}$ (with $g_s=2$).
10. **Massless fermions:** compute the energy density of a neutrino gas at $T=10^{10}$ K ($u=\frac78\cdot\frac{g_s}{2}aT^4$) per species and compare with photons.

## Optional extension

Derive the full relativistic Fermi-Dirac pressure and energy density for arbitrary $\eta$ and $\theta$ as integrals and show that they reduce to the five limits: non-relativistic non-degenerate, non-relativistic degenerate, ultra-relativistic non-degenerate, ultra-relativistic degenerate, and the intermediate region requires numerics.

## Pitfalls

- Mixing up $\rho/\mu_e$ (electron density) with $\rho/\mu$ (total particle density).
- Using $E_F$ including or excluding the rest mass inconsistently in the relativistic regime.
- Using the Sommerfeld expansion at $T\gtrsim0.3T_F$.
- Forgetting positrons at $T\gtrsim10^9$ K.

## Gate questions

1. Why does degeneracy pressure not depend on temperature at $T=0$, and why does it scale as $n^{5/3}$ or $n^{4/3}$?
2. Why is the Chandrasekhar mass independent of the central density?
3. Why can degenerate matter undergo thermonuclear runaway while ideal-gas matter cannot?

## One-page cheat sheet contents

$T=0$ formulas for both limits; the exact relativistic $P(x)$; $K_1,K_2$ constants; Sommerfeld results; degeneracy criterion and $T_F(\rho/\mu_e)$; Chandrasekhar scaling.
