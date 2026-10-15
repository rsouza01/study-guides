# Module 02: Postulates and formalism

**Zettili:** Chapter 3, *Postulates of Quantum Mechanics* (printed pp. 187–240; PDF pp. 207–260), plus Section 10.2 *The Pictures of Quantum Mechanics* (pp. 623–627), Section 2.6.5 (parity operator, p. 148) and a skim of Chapter 1 (pp. 1–90).
**Time:** 2 weeks.

## Zettili pin (exact, from your 3rd edition)

PDF page = printed page + 20. **Note:** the Schrodinger, Heisenberg and interaction pictures are in Chapter 10 (Section 10.2), not in Chapter 3. Read them in this module.

| Section | Printed page | Role |
| --- | --- | --- |
| Chapter 1: 1.2 particle aspect of radiation, 1.3 wave aspect of particles, 1.5 indeterminism, 1.8 wave packets | 1 to 90 | skim, one evening (numbers only) |
| 3.2 Basic postulates | 187 | core |
| 3.3 State of a system (probability density, superposition) | 190 | core |
| 3.4 Observables and operators | 193 | core |
| 3.5 Measurement (3.5.1 to 3.5.4: expectation values, CSCO, uncertainty) | 195 to 200 | core |
| 3.6 Time evolution (3.6.1 to 3.6.5, including conservation of probability, p. 204) | 201 to 206 | core |
| 3.7 Symmetries and conservation laws (3.7.1 to 3.7.3) | 207 to 210 | core |
| 3.8 Connecting quantum to classical (Poisson brackets, Ehrenfest theorem) | 211 to 215 | core |
| 10.2 Schrodinger, Heisenberg, interaction pictures (10.2.1 to 10.2.3) | 623 to 627 | core |
| 2.6.5 Parity operator | 148 | revisit |
| 3.9 Solved Problems 3.1 to 3.14 | 216 to 233 | exercise pool |
| 3.10 Exercises 3.1 to 3.27 | 234 to 240 | extra pool |
| Problems 10.1 to 10.3 (Heisenberg oscillator) | 650 to 653 | exercise pool |

**Solved problems to do:** 3.2 and 3.3 (time evolution in an infinite well), 3.4 and 3.5 (superpositions and measurements), 3.6 to 3.9 (matrix systems, probabilities), 3.11 (evolution of a matrix system), 3.12 (Poisson bracket of $L_x,L_y$), 3.13 (charged oscillator in an oscillating field), 3.14 (free particle $\langle x\rangle(t),\langle p\rangle(t)$), 10.1 to 10.3.
**Unsolved exercises worth doing:** 3.7, 3.9, 3.10, 3.11, 3.13, 3.23, 3.24, 3.25, 10.2, 10.3, 10.6, 10.7.
**Not in Zettili:** the density operator (pure and mixed states, $\mathrm{Tr}\rho^2$, von Neumann equation); use Sakurai (density operator section) or the Cohen-Tannoudji complements. Time reversal is introduced in 2.4.8 and treated for Dirac fields in 12.4.24.

## Why this matters for QCD

- The **Heisenberg picture** and the **interaction picture** are what QFT calculations use. Field operators are Heisenberg-picture objects.
- **Symmetries and conservation laws** are the QCD organizing principle: translation, rotation, parity, charge conjugation, time reversal, isospin, color.
- The **density operator** is how you speak about mixed states, thermal states and entanglement (matters for hot QCD matter and neutron stars).
- The **uncertainty relation** and the idea of **commuting observables** reappear as unitarity and microcausality conditions.

## Skip-test (40 minutes, no notes)

1. State the postulates (state space, observables, measurement and probabilities, collapse, time evolution).
2. Derive the generalized uncertainty relation $\Delta A\,\Delta B\ge\frac12|\langle[A,B]\rangle|$.
3. Prove Ehrenfest's theorem for $\langle x\rangle$ and $\langle p\rangle$.
4. Show that the Heisenberg-picture operator $A_H(t)=U^\dagger AU$ obeys $i\hbar\,dA_H/dt=[A_H,H]$.
5. Show that if $[H,P]=0$ for the parity operator $P$, non-degenerate eigenstates of $H$ have definite parity.

## Prerequisites

Module 01. Basic wave mechanics (Schrodinger equation, probability density) from Griffiths.

## Detailed topics (checklist)

**Origins (skim, one evening):** blackbody radiation and Planck's constant, photoelectric and Compton effects, de Broglie waves, Bohr atom, wave-particle duality, the double-slit experiment. Know the numbers: $\lambda=h/p$, Compton wavelength $h/mc$, and the Bohr energies. Do not do the problems.

**Postulates**
- States as rays in a Hilbert space; superposition principle.
- Observables as Hermitian operators; the possible outcomes are eigenvalues.
- Born rule: probability $|\langle a_n|\psi\rangle|^2$ (for degeneracy, the sum over the eigenspace); expectation value $\langle A\rangle=\langle\psi|A|\psi\rangle$.
- Collapse (projection postulate) and repeated measurement.
- Time evolution by the Schrodinger equation $i\hbar\,\partial_t|\psi\rangle=H|\psi\rangle$; the unitary evolution operator $U(t)=e^{-iHt/\hbar}$ for time-independent $H$ and the time-ordered exponential otherwise; stationary states and energy eigenstates.

**Consequences**
- Compatible observables and CSCO; incompatibility and the generalized uncertainty principle, the energy-time relation and its different meaning (a lifetime-width statement, not an operator relation).
- Probability density and current: $\partial_t\rho+\nabla\cdot\vec j=0$ with $\vec j=\frac{\hbar}{2mi}(\psi^*\nabla\psi-\psi\nabla\psi^*)$.
- Ehrenfest theorem and the classical limit.
- Time-dependent expectation values, Rabi/two-level dynamics and spin precession as the model examples.

**Pictures**
- Schrodinger, Heisenberg and interaction pictures; $A_H(t)=U^\dagger AU$; the Heisenberg equation of motion; the equation of motion of $x$ and $p$ for the oscillator.
- Interaction picture: $H=H_0+V$, $|\psi_I\rangle=e^{iH_0t/\hbar}|\psi_S\rangle$, $V_I(t)=e^{iH_0t/\hbar}Ve^{-iH_0t/\hbar}$ (preview of Module 09).

**Symmetries and conservation laws**
- Unitary symmetry operators and their generators: translation ($P$), rotation ($J$), time translation ($H$). A symmetry means $[U,H]=0$ and implies a conserved charge.
- Parity: $P^2=1$, eigenvalues $\pm1$, action on $x$, $p$, $L$ (the latter is an axial vector), selection rules; time reversal as an antiunitary operator is introduced in Zettili Section 2.4.8 (p. 114) and treated for the Dirac equation in Section 12.4.24 (p. 810).
- Degeneracy as a consequence of symmetry.

**Density operator**
- Pure versus mixed states, $\rho=\sum p_i|\psi_i\rangle\langle\psi_i|$, $\mathrm{Tr}\rho=1$, $\mathrm{Tr}\rho^2\le1$, expectation $\langle A\rangle=\mathrm{Tr}(\rho A)$, von Neumann equation $i\hbar\,\dot\rho=[H,\rho]$, the thermal density matrix $e^{-\beta H}/Z$.

## Reading plan (exact)

| Block | Reading |
| --- | --- |
| Lunch 1 | Chapter 1 skim (1.2, 1.3, 1.5, 1.8) and Sections 3.2 to 3.3 (pp. 187 to 193) |
| Lunch 2 | Sections 3.4 to 3.5 (pp. 193 to 201) |
| Lunch 3 | Section 3.6 (pp. 201 to 207) |
| Lunch 4 | Section 10.2 pictures (pp. 623 to 627) |
| Week 2 lunches | Sections 3.7 to 3.8 (pp. 207 to 216) and Section 2.6.5 (p. 148) |
| Evenings | Derivations; then Problems 3.2 to 3.14 and 10.1 to 10.3; exercises |

## Derive from scratch (derivation nights)

1. The generalized uncertainty principle via Cauchy-Schwarz, including the variance $\Delta A$ definition and the step with the anticommutator and commutator parts.
2. Ehrenfest's theorem and the classical limit for a potential $V(x)$.
3. Heisenberg's equations for the oscillator, solved exactly: $x(t)=x_0\cos\omega t+\frac{p_0}{m\omega}\sin\omega t$.
4. Conservation of probability and the current density.
5. Two-level system with $H=\frac{\hbar\omega_0}2\sigma_z$: spin precession, and the same system with a transverse coupling (energy splitting, mixing angle).

## Bare-minimum exercises (look for solved problems on: uncertainty, Ehrenfest, expectation values, Heisenberg picture, parity, density matrix)

1. **Uncertainty:** evaluate $\Delta x\,\Delta p$ in a Gaussian state and in the first excited oscillator state; verify the bound. *Zettili:* Problems 4.2 and 4.8 (uncertainty, box and oscillator), 5.1 ($\Delta J_x\Delta J_y$); Section 2.4.5.
2. **Spin-1/2 measurement:** for $|\psi\rangle=(\cos\frac\theta2,\ e^{i\varphi}\sin\frac\theta2)^T$ compute the probabilities of $S_x=\pm\hbar/2$ and the expectation values $\langle S_i\rangle$. *Zettili:* Problems 5.4 and 5.5; Problems 3.8 and 3.9 (probabilities for matrix systems).
3. **Precession:** for $H=-\gamma BS_z$ evolve a spin initially along $x$ and show $\langle S_x\rangle=\frac\hbar2\cos\gamma Bt$, $\langle S_y\rangle=\frac\hbar2\sin\gamma Bt$ (up to a sign convention). *Zettili:* Problem 5.6; Exercise 10.6 (Heisenberg equations for $H=\omega S_z$).
4. **Two-level mixing:** diagonalize $H=\begin{pmatrix}E_1&V\\V&E_2\end{pmatrix}$, find the eigenstates, mixing angle and the transition probability $P(t)=\frac{4V^2}{(E_1-E_2)^2+4V^2}\sin^2\frac{\Omega t}2$ with $\hbar\Omega=\sqrt{(E_1-E_2)^2+4V^2}$ (Rabi form). *Zettili:* Problems 3.6, 3.7, 3.11; Exercise 3.23.
5. **Ehrenfest for a force:** show $\frac{d\langle p\rangle}{dt}=-\langle V'(x)\rangle$ and give an example where $\langle V'(x)\rangle\ne V'(\langle x\rangle)$. *Zettili:* Section 3.8.2; Problems 3.13 and 3.14; Exercises 3.24 and 3.25.
6. **Heisenberg equations:** for $H=\frac{p^2}{2m}+\frac12m\omega^2x^2$ derive $\dot x,\dot p$ and solve them. *Zettili:* Problems 10.1 to 10.3; Exercises 10.2, 10.3, 10.7.
7. **Parity:** show that $P x P^{-1}=-x$, $PpP^{-1}=-p$, $PLP^{-1}=+L$; deduce the parity of $Y_\ell^m$ is $(-1)^\ell$. *Zettili:* Section 2.6.5; Exercise 2.47; later Exercises 12.38 and 12.39.
8. **Probability current:** compute $\rho$ and $j$ for a plane wave and for a superposition of two plane waves; check the continuity equation. *Zettili:* Section 3.6.4 (p. 204); no dedicated problem, check a plane wave by hand.
9. **Density matrix:** for a spin-1/2 ensemble with polarization $\vec P$, write $\rho=\frac12(1+\vec P\cdot\vec\sigma)$, compute $\mathrm{Tr}\rho^2=\frac12(1+P^2)$, and the entropy of a maximally mixed state. *Zettili:* not covered; use Sakurai or Cohen-Tannoudji.
10. **Time-energy relation:** a state $|\psi\rangle=\frac1{\sqrt2}(|E_1\rangle+|E_2\rangle)$; find the time scale after which an observable changes appreciably and relate it to $\hbar/\Delta E$. *Zettili:* Problems 3.2, 3.4, 3.5; Exercise 3.7.

## Optional extension

Read the section on time reversal (as an antiunitary operator, $T=U K$) in Sakurai and show that for spin-1/2 with $T^2=-1$ you get Kramers degeneracy. It will help with C, P, T for Dirac fields later.

## Pitfalls

- Treating the energy-time uncertainty relation as an operator relation.
- Forgetting that expectation values in the Heisenberg picture use the initial state, with operators evolving.
- Mixing up the Schrodinger and Heisenberg signs: $U^\dagger AU$ versus $UAU^\dagger$.
- Believing collapse is a dynamical consequence of the Schrodinger equation. It is a postulate, part of the interpretation problem. Know that the interpretations exist; do not argue them here.

## Gate questions

1. What is the difference between a statistical mixture and a superposition, and how does the density matrix distinguish them?
2. Why does a symmetry of the Hamiltonian imply a conservation law?
3. In which picture does time dependence live in the states, in the operators, or split between the two?

## One-page cheat sheet contents

Postulates, uncertainty derivation outline, pictures table, Heisenberg equation, symmetry-generator table ($T\to P$, $\ R\to J$, $\ U(t)\to H$), density operator formulas.
