# Module 11: Photons, Bose gases and lattice vibrations

**Books:** Schroeder (chapter 7: photon gas, blackbody radiation, Debye theory, Bose-Einstein condensation), Pathria (chapter 7: ideal Bose systems; chapter 8 for phonon-related material; chapter 9 for radiation in the early universe), Blundell and Blundell (photons, phonons), Mandl (black-body radiation, phonons).
**Time:** 2 weeks.

## Why this matters for stars and EOS

- **Radiation** is a thermodynamic fluid inside stars: $P_{\rm rad}=\frac13aT^4$ dominates in massive stars and is the reason the adiabatic exponent drops. It also provides the energy transport (Module 14).
- **Blackbody physics** underlies the definition of the effective temperature, bolometric luminosity and the surface boundary condition.
- **Phonons** (the lattice vibrations of the Coulomb crystal in a cold white dwarf core) give the low-temperature heat capacity $\propto T^3$ and the Debye cooling stage.
- **Bose statistics and $\mu=0$ for non-conserved particles** is the same logic that applies to photons, phonons and to thermal pairs.

## Skip-test (40 minutes, no notes)

1. Derive Planck's law from the Bose distribution with $\mu=0$ and $g(\epsilon)=\frac{g_sV\epsilon^2}{2\pi^2\hbar^3c^3}$ with $g_s=2$, obtain $u=aT^4$ with $a=\frac{\pi^2k^4}{15\hbar^3c^3}$, $P=u/3$, $S=\frac43aVT^3$.
2. Derive the photon number density $n_\gamma=\frac{2\zeta(3)}{\pi^2}\left(\frac{kT}{\hbar c}\right)^3\approx20.3\,T^3$ cm$^{-3}$ and the entropy per photon $\frac{s}{n_\gamma}=\frac{2\pi^4}{45\zeta(3)}k\approx3.6k$.
3. State Wien's law, the Stefan-Boltzmann law $F=\sigma T^4$ with $\sigma=ac/4$.
4. Derive the Debye low-temperature heat capacity $C_V=\frac{12\pi^4}{5}Nk\left(\frac T{\Theta_D}\right)^3$ and the Dulong-Petit limit $3Nk$.
5. Find the condensation temperature of an ideal Bose gas $T_c=\frac{2\pi\hbar^2}{mk}\left(\frac{n}{\zeta(3/2)}\right)^{2/3}$.

## Prerequisites

Modules 08 and 09.

## Detailed topics (checklist)

**The photon gas**
- Quantization of the radiation field in a box; photons as bosons with no conserved number ($\mu=0$); Planck distribution and spectral energy density; total energy, pressure, entropy, free energy $F=-\frac13aVT^4$; Stefan-Boltzmann law; Wien displacement; radiation flux from a hole; number density; adiabatic expansion $T^3V=$ const.
- **Radiation in stellar thermodynamics:** $P_{\rm rad}=\frac13aT^4$; $\beta=P_{\rm gas}/P$; radiation-dominated gas has $\Gamma_1=4/3$.
- Spectral forms: $B_\nu(T)=\frac{2h\nu^3}{c^2}\frac{1}{e^{h\nu/kT}-1}$, the Rayleigh-Jeans and Wien limits, the integrals leading to $\pi^4/15$.

**Bose-Einstein condensation (ideal Bose gas)**
- $N=\int g(\epsilon)\frac{1}{z^{-1}e^{\beta\epsilon}-1}d\epsilon$ with $z<1$; critical temperature; the condensate fraction $1-(T/T_c)^{3/2}$; thermodynamics below $T_c$ (pressure depends on $T$ only); relation to superfluidity (awareness).
- Relevance: a model of bosonic degeneracy; liquid helium; why photons do not condense (no conserved number).

**Lattice vibrations**
- Phonons as bosons with $\mu=0$ and a dispersion relation with a cutoff; the Einstein model; the Debye model: density of states $g(\omega)\propto\omega^2$ up to $\omega_D$, $\Theta_D=\hbar\omega_D/k$; heat capacity as a function of $T/\Theta_D$ with limits $T^3$ and $3Nk$.
- In a **Coulomb crystal of ions** in a white dwarf: the relevant frequency scale is the ion plasma frequency $\omega_p=\left(\frac{4\pi Z^2e^2n_i}{M}\right)^{1/2}$ and $\Theta_D\approx0.45\hbar\omega_p/k$ (check).

**Massless fermions for comparison**
- A massless fermion gas with $\mu=0$ has $u=\frac78\frac{g_s}{2}aT^4$ and $n=\frac34\frac{\zeta(3)}{\pi^2}g_s\left(\frac{kT}{\hbar c}\right)^3$: the standard relation of thermal neutrino and pair energy densities to the photon density.

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Schroeder chapter 7: the photon gas, Planck distribution, blackbody radiation |
| Lunch 2 | Pathria chapter 7: ideal Bose systems; Mandl on black-body radiation |
| Lunch 3 | Schroeder chapter 7: phonons and the Debye model; Blundell and Blundell on phonons |
| Lunch 4 | Schroeder chapter 7: Bose-Einstein condensation |
| Week 2 lunches | Review; radiation in stellar and cosmological examples (Pathria chapter 9) |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. Planck's law and the Stefan-Boltzmann law from the Bose distribution.
2. $P=u/3$ and $S=\frac43aVT^3$ from the grand potential.
3. $n_\gamma$ and the entropy per photon.
4. The Debye model: $C_V(T)$ at low and high $T$.
5. The Bose-Einstein condensation temperature.

## Bare-minimum exercises (find matching problems with keywords: blackbody, Stefan-Boltzmann, Debye temperature, Bose-Einstein condensation, photon gas)

1. **Radiation constant:** compute $a=\frac{\pi^2k^4}{15\hbar^3c^3}=7.566\times10^{-15}$ erg cm$^{-3}$ K$^{-4}$ and $\sigma=ac/4=5.67\times10^{-5}$ cgs.
2. **Radiation at stellar temperatures:** $P_{\rm rad}$ at $1.57\times10^7$ K ($\approx1.5\times10^{14}$ dyn/cm$^2$), at $10^8$ K ($2.5\times10^{17}$) and $10^9$ K ($2.5\times10^{21}$); compare with $P_{\rm gas}$ at $\rho=100$ g/cm$^3$ at each $T$.
3. **Photon number and entropy:** $n_\gamma$ at $1.57\times10^7$ K ($\approx8\times10^{22}$ cm$^{-3}$) versus baryons ($\sim10^{26}$); entropy per photon $3.6k$; entropy per baryon carried by photons at the solar centre (a few $\times10^{-3}\,k$, tiny).
4. **Adiabatic cooling of radiation:** show that when a radiation-dominated volume expands adiabatically $T\propto V^{-1/3}$ and verify $\Gamma=4/3$ via $PV^{4/3}=$ const.
5. **Effective temperature:** for the Sun $L=3.83\times10^{33}$ erg/s, $R=6.96\times10^{10}$ cm, compute $T_{\rm eff}=\left(\frac{L}{4\pi R^2\sigma}\right)^{1/4}=5772$ K and the wavelength of peak emission from Wien's law, $\lambda_{\max}T=0.29$ cm K ($\lambda_{\max}\approx500$ nm).
6. **Debye model:** derive $C_V\to\frac{12\pi^4}{5}Nk(T/\Theta_D)^3$; evaluate for a Coulomb crystal of carbon at $\rho=10^6$ g/cm$^3$: compute $\omega_p$ and $\Theta_D$ ($\hbar\omega_p/k\approx4\times10^6$ K, so $\Theta_D\approx0.45\hbar\omega_p/k\approx2\times10^6$ K; verify) and decide whether a core at $T=10^7$ K is in the Debye or the classical regime (it is classical).
7. **BEC:** compute $T_c$ for liquid-helium density $0.145$ g/cm$^3$ ($\approx3.1$ K); show the condensate fraction below $T_c$; contrast with the observed $\lambda$ point of 2.17 K.
8. **Why $\mu=0$:** argue from the equilibrium condition for a reaction $e^-+e^+\leftrightarrow\gamma\gamma$ (or from the minimization of $F$ with respect to $N_\gamma$) that $\mu_\gamma=0$.
9. **Neutrino and pair energy densities:** from the results for massless fermions find $\frac{u_\nu}{u_\gamma}=\frac78\frac{g_\nu}{2}$ and the effective number of relativistic degrees of freedom $g_*$ for photons plus three neutrino flavours ($2+\frac78\times6=7.25$ without pairs).
10. **Spectral integral:** verify numerically $\int_0^\infty\frac{x^3}{e^x-1}dx=\frac{\pi^4}{15}$, the peak of $\frac{x^3}{e^x-1}$ at $x=2.821$ and of $\frac{x^2}{e^x-1}$ (photon number) at $x=1.594$.

## Optional extension

Show that the ideal Bose gas below $T_c$ has $P=P(T)$ only and its compressibility is infinite; discuss why real (interacting) Bose gases avoid this.

## Pitfalls

- Using $\mu\ne0$ for photons or phonons.
- Mixing $B_\nu$ (per unit frequency per steradian) with energy density.
- Forgetting the polarization factor 2 for photons.
- Applying the Debye model without checking that $T\ll\Theta_D$ before using the $T^3$ law.

## Gate questions

1. Why does radiation pressure grow as $T^4$ and dominate at high temperature and low density?
2. Why is the heat capacity of phonons $\propto T^3$ at low $T$?
3. Why do photons not condense in a Bose-Einstein condensate?

## One-page cheat sheet contents

Planck law; $a$ and $\sigma$; $n_\gamma$, $s/n_\gamma$; Wien law; Debye formulas; BEC temperature; massless fermion comparison.
