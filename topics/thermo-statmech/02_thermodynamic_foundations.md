# Module 02: Thermodynamic foundations

**Books:** Callen (postulates, fundamental relation, equilibrium conditions; Part I, roughly chapters 1 to 3), Schroeder (chapters 1 to 3), Blundell and Blundell (temperature, entropy).
**Time:** 2 weeks.

## Why this matters for stars and EOS

The **fundamental relation** $S(U,V,N_i)$ (or equivalently a thermodynamic potential) is the complete content of an equation of state. Pressure, temperature, chemical potentials and every other quantity follow from derivatives of it. Knowing this structure is what lets you build an EOS for a star (gas plus radiation plus degenerate electrons plus ionization) that is *thermodynamically consistent*. It also gives you the Euler relation and Gibbs-Duhem equation used repeatedly later.

## Skip-test (40 minutes, no notes)

1. State Callen's four postulates (existence of equilibrium states, entropy maximum, additivity and differentiability, third law).
2. From $U=U(S,V,N)$ define $T=\partial U/\partial S$, $P=-\partial U/\partial V$, $\mu=\partial U/\partial N$ and derive the Euler relation $U=TS-PV+\mu N$ and Gibbs-Duhem $S\,dT-V\,dP+N\,d\mu=0$.
3. Given $S=Nk\left[\ln\frac VN+\frac32\ln T+{\rm const}\right]$ (monatomic ideal gas), derive $PV=NkT$ and $U=\frac32NkT$.
4. For blackbody radiation with $U=aVT^4$, derive $P=aT^4/3$ and $S=\frac43aVT^3$, and the fundamental relation $S=\frac43a^{1/4}U^{3/4}V^{1/4}$.
5. State the second law as a maximum-entropy principle and use it to show that two bodies in thermal contact reach equal temperatures.

## Prerequisites

Module 01.

## Detailed topics (checklist)

**The thermodynamic description**
- Macroscopic states, equilibrium, state variables, extensive versus intensive variables, the thermodynamic limit, quasi-static processes, simple systems.
- Energy, heat, work: $dU=\delta Q+\delta W$, sign conventions, $\delta W=-P\,dV+\mu\,dN+\dots$.

**Callen's postulates and the fundamental relation**
- Postulate 1 (states labeled by $U,V,N_i$), Postulate 2 (entropy maximum over unconstrained internal parameters), Postulate 3 (additivity, continuity, differentiability, monotonic in $U$), Postulate 4 (third law).
- The entropy and energy representations; $T,P,\mu$ as derivatives; equations of state as partial information; **the fundamental relation as the complete information**.
- Homogeneity: $S(\lambda U,\lambda V,\lambda N)=\lambda S$, hence the **Euler relation** and **Gibbs-Duhem relation**.

**Equilibrium and the second law**
- Equilibrium conditions between subsystems: equal $T$ (thermal), equal $P/T$ (mechanical), equal $\mu/T$ (chemical); direction of spontaneous processes; entropy production.
- Temperature, pressure and chemical potential as responses of entropy: $\frac1T=\frac{\partial S}{\partial U}$, $\frac PT=\frac{\partial S}{\partial V}$, $-\frac\mu T=\frac{\partial S}{\partial N}$.

**Examples you must master**
- The monatomic ideal gas: $PV=NkT$, $U=\frac32NkT$, Sackur-Tetrode entropy $S=Nk\left[\ln\left(\frac VN\frac{1}{\lambda^3}\right)+\frac52\right]$ with $\lambda=h/\sqrt{2\pi mkT}$ (derived in Module 06).
- The photon gas: $U=aVT^4$, $P=aT^4/3$, $S=\frac43aVT^3$, $\mu=0$ (photon number not conserved).
- Mixtures: the ideal gas mixture, Dalton's law, partial pressures, the **mean molecular weight** $\mu_{\rm mol}$: $P=\frac{\rho kT}{\mu_{\rm mol}m_u}$ with $\frac1{\mu_{\rm mol}}=\sum_i\frac{X_i(1+Z_i)}{A_i}$ for full ionization.
- Gas plus radiation: $P=P_{\rm gas}+P_{\rm rad}$, $\beta\equiv P_{\rm gas}/P$.

**Third law and heat capacities**
- Heat capacities $C_V=T\left(\frac{\partial S}{\partial T}\right)_V$, $C_P=T\left(\frac{\partial S}{\partial T}\right)_P$; the third law and the vanishing of heat capacities at $T\to0$.

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Callen: the postulates and the fundamental relation (chapter 1); Blundell and Blundell on temperature |
| Lunch 2 | Callen: conditions of equilibrium (chapter 2); Schroeder chapter 3 (temperature, entropy, chemical potential from equilibrium) |
| Lunch 3 | Callen: formal relationships, the Euler relation, Gibbs-Duhem, sample systems (chapter 3) |
| Lunch 4 | Schroeder chapters 1 and 2 (first and second laws, ideal gas); Blundell and Blundell on entropy |
| Week 2 lunches | Review; photon gas and mixtures; mean molecular weights |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. The Euler relation from homogeneity of degree one.
2. The Gibbs-Duhem relation from the Euler relation and $dU=TdS-PdV+\mu dN$.
3. Equal temperature, pressure and chemical-potential conditions from entropy maximization with fixed total $U,V,N$.
4. The ideal-gas fundamental relation from the Sackur-Tetrode formula (take it as given for now) to $PV=NkT$, $U=\frac32NkT$, $\mu=kT\ln(n\lambda^3)$.
5. The photon gas fundamental relation from the Stefan-Boltzmann energy density.

## Bare-minimum exercises (find matching problems in the books with these keywords)

1. **Equation of state from a fundamental relation** (fundamental relation, derive equations of state): for $S=A(NUV)^{1/3}$ (a toy fundamental relation) derive $T,P,\mu$ and verify the Euler relation.
2. **Gibbs-Duhem for the ideal gas:** show that $\mu(T,P)=kT\ln\left(\frac{P\lambda^3}{kT}\right)$ satisfies $d\mu=-s\,dT+v\,dP$ with $s=S/N$, $v=V/N$.
3. **Radiation:** from $U=aVT^4$ and $S=\frac43aVT^3$ verify the Euler relation with $\mu=0$ and derive $P$ by $P=T(\partial S/\partial V)_U$.
4. **Photon number:** show that the number of photons is not conserved so $\mu=0$ and that, for a closed adiabatic radiation-filled volume, $T^3V=$ const.
5. **Heat contact:** two identical blocks with $U_i=C T_i$ at $T_1\ne T_2$: find the final temperature and the entropy change; show it is positive.
6. **Equilibrium of a mixture:** a box of two ideal gases separated by a piston that is free to move and a diaphragm permeable to species 1: find the equilibrium conditions.
7. **Mean molecular weight:** compute $\mu_{\rm mol}$ for fully ionized hydrogen ($0.5$), helium ($4/3$), a solar mixture $X=0.74,Y=0.25,Z=0.01$ ($\approx0.60$) and for the helium-rich core $X=0.34,Y=0.64,Z=0.02$ ($\approx0.85$).
8. **Gas plus radiation:** write $P=P_{\rm gas}+P_{\rm rad}$ and compute $\beta$ for $\rho=150$ g/cm$^3$, $T=1.57\times10^7$ K, $\mu_{\rm mol}=0.85$ ($\beta\approx0.9993$).
9. **Entropy per baryon:** compute the ideal-gas entropy per baryon $s/k$ for the solar centre from the Sackur-Tetrode formula (use $\mu_{\rm mol}$ and treat ions and electrons as ideal gases; expect a result of order 10 per baryon, with the ions contributing most of it because of their larger mass; state the number you get and its ingredients).
10. **Third-law check:** show that the classical ideal-gas entropy diverges at $T\to0$, so the ideal gas cannot hold at low $T$; identify the density-temperature condition ($n\lambda^3\ll1$) under which the classical formula is valid.

## Optional extension

Prove that the entropy representation of a simple system is concave (the second-law content) from the maximum-entropy postulate. Stability conditions in Module 03 follow from it.

## Pitfalls

- Using $dU=TdS-PdV$ without the $\mu\,dN$ term where particle number can change (reactions, ionization).
- Treating a photon gas as having a chemical potential.
- Confusing the mean molecular weight per particle with that per electron or per ion.
- Sign errors in the work $\delta W=-PdV$.

## Gate questions

1. What is the difference between an equation of state and the fundamental relation, and why is the latter "complete"?
2. Why is the chemical potential of a photon gas zero?
3. Which equilibrium condition corresponds to each extensive variable ($U$, $V$, $N$)?

## One-page cheat sheet contents

Postulates; $dU$, Euler, Gibbs-Duhem; equilibrium conditions; ideal gas and photon gas fundamental relations; mean molecular weight formulas.
