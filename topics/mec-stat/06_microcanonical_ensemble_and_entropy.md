# Module 06: Microstates, the microcanonical ensemble and entropy

**Books:** Schroeder (chapters 2 and 3), Pathria (chapters 1 and 2), Swendsen (entropy and the microcanonical ensemble), Mandl (basic statistical ideas), Callen (foundations of statistical mechanics).
**Time:** 2 weeks.

## Why this matters for stars and EOS

Counting states is the origin of every EOS: the entropy of the classical ideal gas (Sackur-Tetrode), the correct treatment of **indistinguishable particles** (needed for the Fermi and Bose gases), and the meaning of temperature and chemical potential as derivatives of $\ln\Omega$. It also gives the logic behind negative heat capacity (Module 15) and the sharpness of the thermodynamic limit.

## Skip-test (40 minutes, no notes)

1. Define the multiplicity $\Omega(E,V,N)$ and the Boltzmann entropy $S=k\ln\Omega$; show $\frac1T=\frac{\partial S}{\partial E}$.
2. For the Einstein solid of $N$ oscillators with $q$ quanta, $\Omega=\binom{q+N-1}{q}$; derive $S$ for $q,N\gg1$ and then $T(q)$.
3. Derive $\Omega\propto V^NE^{3N/2}/N!$ for a monatomic ideal gas, and the Sackur-Tetrode entropy $S=Nk\left[\ln\frac{V}{N\lambda^3}+\frac52\right]$ with $\lambda=h/\sqrt{2\pi mkT}$.
4. Compute the entropy of mixing for two ideal gases and explain the Gibbs paradox.
5. For two systems in thermal contact, show that the most probable energy partition has equal temperatures and that its relative width goes as $1/\sqrt N$.

## Prerequisites

Modules 01, 02.

## Detailed topics (checklist)

**Foundations**
- Microstates and macrostates, the fundamental postulate (equal a priori probabilities for accessible microstates of an isolated system), the microcanonical ensemble, the density of states $\Omega(E)$ and the number of states below $E$.
- The thermodynamic limit, sharply peaked distributions, why the entropy is extensive, the equivalence with Callen's entropy.
- Boltzmann versus Gibbs entropy; the role of ergodicity (awareness only); the link to the Shannon entropy.

**Temperature, pressure and chemical potential from counting**
- $\frac1T=\frac{\partial S}{\partial E}$, $\frac PT=\frac{\partial S}{\partial V}$, $-\frac\mu T=\frac{\partial S}{\partial N}$ from $S=k\ln\Omega$ (Module 02's thermodynamic definitions are now derived).
- Equilibrium between two systems from the maximum of $\Omega_1\Omega_2$; the second law as the overwhelming probability.

**Solvable models**
- Two-state systems (paramagnet) and the Einstein solid; negative absolute temperature of a bounded spectrum (awareness).
- The classical ideal gas by phase-space counting: $\Omega=\frac{1}{N!h^{3N}}\int d^{3N}q\,d^{3N}p$ over the energy shell; volume of a $3N$-dimensional sphere; the factor $\frac{1}{N!}$ for identical particles and its role in extensivity and the Gibbs paradox; Sackur-Tetrode result, the thermal wavelength $\lambda$ and the condition $n\lambda^3\ll1$.
- Entropy of mixing $\Delta S=-Nk\sum_ix_i\ln x_i$.

**Quantum counting preview**
- The number of ways to place $N$ identical particles in $g$ orbitals: classical $g^N/N!$ (dilute), fermions $\binom gN$, bosons $\binom{g+N-1}{N}$ (the origin of quantum statistics, Module 09).

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Schroeder chapter 2: two-state systems, Einstein solid, multiplicity |
| Lunch 2 | Schroeder chapter 3: entropy, temperature, chemical potential from counting; ideal gas multiplicity |
| Lunch 3 | Pathria chapters 1 and 2: statistical basis, ensemble theory, microcanonical ensemble |
| Lunch 4 | Swendsen on entropy and the thermodynamic limit; Mandl on the basic ideas |
| Week 2 lunches | Review; Callen on the foundations of statistical mechanics |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. Equal temperatures from maximizing $\Omega_1(E_1)\Omega_2(E-E_1)$, with the Gaussian width of the peak.
2. The Einstein solid entropy and $T(q)$ with Stirling's approximation.
3. The volume of a $d$-dimensional ball and $\Omega$ for the ideal gas.
4. The Sackur-Tetrode formula including the $1/N!$ and $h^{3N}$ factors.
5. The entropy of mixing and the resolution of the Gibbs paradox.

## Bare-minimum exercises (find matching problems with keywords: multiplicity, Einstein solid, two-state paramagnet, Sackur-Tetrode, entropy of mixing)

1. **Counting:** enumerate the multiplicities of an Einstein solid with $N=3$ and $q=0,\dots,6$; verify against $\binom{q+N-1}{q}$.
2. **Peak width:** for two Einstein solids with $N_1=N_2=300$ and $q=100$ find the peak of $\Omega_1\Omega_2$ and compare the width with a Gaussian estimate $\propto q/\sqrt N$.
3. **Temperature from counting:** for the Einstein solid with $q\gg N\gg1$ show $U=NkT$ (equipartition for $kT\gg\hbar\omega$).
4. **Paramagnet:** for $N$ spin-1/2 dipoles in a field derive $S(U)$ and $T(U)$, including the region of negative $T$.
5. **Ideal gas entropy:** derive $S$ and check it against Sackur-Tetrode numerically for helium at 300 K and 1 atm ($S/Nk\approx15.2$; verify).
6. **Free expansion:** show $\Delta S=Nk\ln(V_f/V_i)$ for the free expansion of an ideal gas and interpret it by counting.
7. **Mixing:** $N$ molecules of gas A and $N$ molecules of gas B, each initially in a volume $V$ at the same $T$ and $P$, are allowed to mix in a total volume $2V$. Show $\Delta S=2Nk\ln2$ for different gases and $\Delta S=0$ for two samples of the same gas.
8. **Gibbs paradox:** show that omitting $1/N!$ makes $S$ non-extensive; give the correct extensive result.
9. **Quantum counting:** count the states of two particles in three orbitals as distinguishable, bosons, fermions (9, 6, 3) and find the classical limit factor as $g\to\infty$.
10. **Orders of magnitude:** the relative energy fluctuation of one mole ($N\approx6\times10^{23}$) is $\sqrt{2/3N}\approx10^{-12}$; show that a fractional fluctuation of $10^{-9}$ is about $10^3$ standard deviations away and has probability $\sim e^{-5\times10^5}$, effectively zero.

## Optional extension

Prove that the density of states of the free particle in a box is $\Omega\propto E^{3N/2-1}$, and that the entropy defined by the number of states below $E$ and by the density of states at $E$ differ only by $O(\ln N)$ (the ambiguity is irrelevant in the thermodynamic limit).

## Pitfalls

- Omitting $1/N!$ and $h^{3N}$ in the counting (non-extensive entropy, wrong absolute entropy).
- Counting states with fixed particle labels for identical particles.
- Treating the Boltzmann entropy as meaningful for tiny $N$ where $S=k\ln\Omega$ is not additive.
- Confusing the microcanonical temperature with the kinetic temperature.

## Gate questions

1. Why is the Gibbs paradox a paradox, and why does quantum mechanics resolve it?
2. Why can an isolated system's entropy increase if every microstate is equally probable?
3. How is temperature defined without a thermometer?

## One-page cheat sheet contents

$S=k\ln\Omega$; $T,P,\mu$ from entropy derivatives; Einstein-solid and ideal-gas counting; Sackur-Tetrode; entropy of mixing; quantum counting.
