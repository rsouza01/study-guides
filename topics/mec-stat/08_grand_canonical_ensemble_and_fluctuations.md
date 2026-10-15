# Module 08: The grand canonical ensemble, chemical potential and fluctuations

**Books:** Pathria (chapter 4: grand canonical ensemble; the equivalence of ensembles; fluctuations), Schroeder (chapters 5 and 7: Gibbs factor), Swendsen (grand canonical ensemble, fluctuations), Mandl.
**Time:** 2 weeks.

## Why this matters for stars and EOS

- Stars exchange particles between species and between phases (ionization, pair production, nuclear reactions): the **grand canonical ensemble** is the natural framework, and the **grand potential** $\Omega=-PV$ gives the pressure directly from the partition function.
- **Fermi-Dirac and Bose-Einstein distributions** are *derived* here from the grand partition function of a single orbital. This is the bridge to degenerate matter.
- The **Saha equation** is derived again, cleanly, as the equilibrium of coupled grand canonical systems.
- Fluctuation formulas give the compressibility and the heat capacity in terms of variances, and explain why different ensembles agree in the thermodynamic limit.

## Skip-test (40 minutes, no notes)

1. Write the grand canonical probability $p=e^{-\beta(E-\mu N)}/\mathcal Z$ and show $\Omega=-kT\ln\mathcal Z=-PV$, $N=-\frac{\partial\Omega}{\partial\mu}$, $S=-\frac{\partial\Omega}{\partial T}$.
2. For the classical ideal gas show $\mathcal Z=\exp\left(\frac{zV}{\lambda^3}\right)$ with $z=e^{\beta\mu}$, so $\langle N\rangle=\frac{zV}{\lambda^3}$, $P=\frac{kTz}{\lambda^3}$, $\mu=kT\ln(n\lambda^3)$ and Poisson fluctuations $\langle\Delta N^2\rangle=\langle N\rangle$.
3. For a single orbital of energy $\epsilon$ derive the Fermi-Dirac and Bose-Einstein mean occupations from the Gibbs sum: $\bar n=\frac{1}{e^{\beta(\epsilon-\mu)}\pm1}$.
4. Show $\langle\Delta N^2\rangle=kT\left(\frac{\partial N}{\partial\mu}\right)_{T,V}=\frac{N^2kT}{V}\kappa_T$.
5. State the equivalence of ensembles and the condition under which it fails (long-range forces, phase coexistence).

## Prerequisites

Modules 02, 03, 05, 06, 07.

## Detailed topics (checklist)

**The ensemble**
- A system in contact with a heat and particle reservoir; the Gibbs distribution; fugacity $z=e^{\beta\mu}$; the grand partition function $\mathcal Z=\sum_{N}z^NZ_N$; the grand potential $\Omega=-kT\ln\mathcal Z=-PV$; $\langle N\rangle=z\frac{\partial\ln\mathcal Z}{\partial z}$; $U-\mu N=-\frac{\partial\ln\mathcal Z}{\partial\beta}$.
- Several species: one fugacity per conserved particle number; with reactions, only conserved charges get independent chemical potentials.

**Single orbitals and quantum statistics (preview)**
- The Gibbs sum for one orbital: fermions $1+ze^{-\beta\epsilon}$, bosons $\frac1{1-ze^{-\beta\epsilon}}$; mean occupation numbers; the classical (Maxwell-Boltzmann) limit $\bar n\to ze^{-\beta\epsilon}$ when $z\ll1$.

**Fluctuations and response**
- $\langle\Delta N^2\rangle=kT\left(\frac{\partial N}{\partial\mu}\right)_{T,V}=\frac{kTN^2\kappa_T}{V}$; energy fluctuations in the grand ensemble; relative fluctuations $O(1/\sqrt N)$ except at critical points.
- **Equivalence of ensembles** in the thermodynamic limit; when it fails.

**Application: Saha from the grand ensemble**
- Treat the electron, ion and atom as three grand canonical subsystems with $\mu_e+\mu_i=\mu_a$; get Saha again with the internal partition functions.
- Application to adsorption (Langmuir isotherm) as a pure exercise in Gibbs sums.

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Pathria chapter 4: grand canonical ensemble |
| Lunch 2 | Schroeder: the Gibbs factor and grand partition function (chapter 7 setup) |
| Lunch 3 | Pathria: density and energy fluctuations; equivalence of ensembles |
| Lunch 4 | Swendsen and Mandl: grand canonical treatments |
| Week 2 lunches | Review; derive Saha and Langmuir |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. The Gibbs distribution from a system plus a reservoir.
2. $\Omega=-PV$ from the extensivity of the grand potential.
3. $\mathcal Z$ for the classical ideal gas, the equation of state and Poisson statistics.
4. Fermi-Dirac and Bose-Einstein occupation numbers from the single-orbital Gibbs sums.
5. The Saha equation from the chemical potential equality, including internal partition functions.

## Bare-minimum exercises (find matching problems with keywords: grand partition function, Gibbs factor, fluctuations in particle number, Langmuir adsorption)

1. **Ideal gas:** derive $P=\frac{kTz}{\lambda^3}$ and the entropy $S=Nk\left(\frac52-\ln(n\lambda^3)\right)$ from $\Omega$.
2. **Poisson:** show $\langle\Delta N^2\rangle=\langle N\rangle$ for the classical ideal gas and compare with $\frac{N^2kT\kappa_T}{V}$ with $\kappa_T=1/P$.
3. **Single orbital:** derive $\bar n_{\rm FD}$ and $\bar n_{\rm BE}$; plot both versus $(\epsilon-\mu)/kT$ and the classical limit $e^{-(\epsilon-\mu)/kT}$.
4. **Fluctuations of a fermion orbital:** show $\langle\Delta n^2\rangle=\bar n(1-\bar n)$ for fermions and $\bar n(1+\bar n)$ for bosons; interpret the sign.
5. **Langmuir isotherm:** $N$ surface sites each binding at most one molecule with energy $-\epsilon_0$ from an ideal gas at pressure $P$: derive $\theta=\frac{P}{P+P_0(T)}$ with $P_0(T)=\frac{kT}{\lambda^3}e^{-\epsilon_0/kT}$.
6. **Saha again:** write the three chemical potentials and derive the Saha equation, including the factor $\frac{2g_{i+1}}{g_i}$; show it agrees with Module 05's result.
7. **Two species with a reaction:** for $A\leftrightarrow B+C$ with ideal-gas species of masses $m_i$, internal partition functions $Z_i$ and energy release $\Delta$ (energy of $B+C$ above $A$), show $\frac{n_Bn_C}{n_A}=\frac{\lambda_A^3}{\lambda_B^3\lambda_C^3}\frac{Z_BZ_C}{Z_A}e^{-\Delta/kT}$.
8. **Energy fluctuations in the grand ensemble:** show $\langle\Delta E^2\rangle_{\rm gc}=\langle\Delta E^2\rangle_{\rm c}+\left(\frac{\partial U}{\partial N}\right)^2\langle\Delta N^2\rangle$.
9. **Failure of equivalence:** explain why the canonical and grand canonical ensembles disagree in a region of first-order phase coexistence (flat $\mu(N)$, divergent $\langle\Delta N^2\rangle$).
10. **Conserved charges:** a gas of $e^-$, $e^+$ and photons has one conserved charge: write the grand partition function with $\mu_+=-\mu_-$ and $\mu_\gamma=0$.

## Optional extension

Show that the grand-canonical derivation of the Bose distribution implies that $\mu\le\epsilon_{\min}$ for bosons, and discuss what happens as $\mu\to\epsilon_{\min}$ (Bose condensation, Module 11).

## Pitfalls

- Assigning a chemical potential to a non-conserved particle number (photons, or $e^-e^+$ pairs separately).
- Forgetting that $\Omega=-PV$ requires homogeneity.
- Using the grand canonical result for a small system where fluctuations matter.
- Mixing up $z$, $\mu$ and $\mu/kT$.

## Gate questions

1. Why does the particle-number fluctuation diverge at a first-order transition?
2. How does a single orbital's partition function lead to Fermi-Dirac statistics?
3. Why can a system with chemical reactions be described with fewer independent chemical potentials?

## One-page cheat sheet contents

Gibbs distribution; $\Omega=-PV$; ideal-gas $\mathcal Z$; FD and BE single-orbital formulas; fluctuation formulas; Saha with internal partition functions.
