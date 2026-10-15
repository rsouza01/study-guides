# Module 09: Time-dependent perturbation theory

**Zettili:** Chapter 10, *Time-Dependent Perturbation Theory* (printed pp. 623–670; PDF pp. 643–690).
**Time:** 2 weeks.

## Zettili pin (exact, from your 3rd edition)

PDF page = printed page + 20.

| Section | Printed page | Role |
| --- | --- | --- |
| 10.2 Pictures of QM (Schrodinger, Heisenberg, interaction) | 623 to 627 | core (first read in Module 02) |
| 10.3.1 Transition probability | 629 | core |
| 10.3.2 Transition probability for a constant perturbation | 630 | core |
| 10.3.3 Transition probability for a harmonic perturbation | 631 | core |
| 10.4.1 Adiabatic approximation | 635 | core |
| 10.4.2 Sudden approximation | 636 | core |
| 10.5 Interaction of atoms with radiation (10.5.1 classical treatment, 10.5.2 quantization of the EM field, 10.5.3 transition rates, 10.5.4 dipole approximation, 10.5.5 selection rules, 10.5.6 spontaneous emission) | 639 to 649 | core |
| 10.6 Solved Problems 10.1 to 10.12 | 650 to 666 | exercise pool |
| 10.7 Exercises 10.1 to 10.24 | 667 to 670 | extra pool |

**Solved problems to do:** 10.4 (spin in a magnetic field), 10.5 and 10.6 (infinite well under a time-dependent perturbation), 10.7 (oscillator with a time-dependent perturbation), 10.8 (hydrogen in a time-dependent field), **10.9 (the $2p\to1s$ transition rate and lifetime)**, 10.10 (transition rate between oscillator levels), 10.11 (free electrons cannot emit or absorb photons), 10.12 (ionization rate of hydrogen). Problems 10.1 to 10.3 (Heisenberg oscillator) belong to Module 02.
**Unsolved exercises worth doing:** 10.4, 10.9 to 10.12, 10.14 to 10.17, 10.21 to 10.24.
**Not in Zettili:** Rabi oscillations in the rotating-wave approximation, the second-order amplitude, and the Wigner-Weisskopf decay argument; use Sakurai (chapter on time-dependent perturbation theory) and Cohen-Tannoudji.

## Why this matters for QCD

- The **Dyson series** for the evolution operator in the interaction picture *is* the perturbative expansion of the S-matrix. Feynman rules are a bookkeeping scheme for its terms.
- **Fermi's golden rule** gives decay rates and (with flux factors) cross sections. In particle physics you will write $\Gamma=\frac{2\pi}\hbar|\mathcal M|^2\rho$ constantly.
- **Resonances and widths**: the exponential decay law, the relation $\Gamma\tau=\hbar$, the Breit-Wigner shape (Module 10).
- **Sudden and adiabatic approximations** reappear in effective field theory (separating fast and slow scales) and in the geometry of gauge theory (Berry phase).

## Skip-test (40 minutes, no notes)

1. Define the interaction picture and show $i\hbar\,\partial_t|\psi_I\rangle=V_I(t)|\psi_I\rangle$.
2. Write the first-order amplitude $c_f^{(1)}(t)=-\frac{i}{\hbar}\int_0^tV_{fi}e^{i\omega_{fi}t'}dt'$ and, for a constant perturbation, $P_{i\to f}=\frac{4|V_{fi}|^2}{\hbar^2\omega_{fi}^2}\sin^2\frac{\omega_{fi}t}{2}$.
3. Derive Fermi's golden rule $\Gamma=\frac{2\pi}\hbar|V_{fi}|^2\rho(E_f)$.
4. For a harmonic perturbation $V\cos\omega t$, state the absorption and stimulated-emission resonance conditions $E_f-E_i=\pm\hbar\omega$.
5. State the adiabatic theorem and the sudden approximation and the conditions for each.

## Prerequisites

Modules 02 (interaction picture preview), 03, 08.

## Detailed topics (checklist)

**Formalism**
- The interaction picture, the evolution operator $U_I(t,t_0)$, the Dyson series $U_I=T\exp\left[-\frac{i}{\hbar}\int V_I\,dt\right]=1-\frac{i}{\hbar}\int V_I+\left(-\frac{i}{\hbar}\right)^2\int\!\!\int_{t_1>t_2}V_I(t_1)V_I(t_2)+\dots$, time-ordering.
- Transition amplitudes and probabilities to first and second order; the probability to remain in the initial state; the validity condition.

**Specific perturbations**
- Constant (turned on at $t=0$) and slowly switched perturbations: the function $\frac{\sin^2(\omega t/2)}{(\omega/2)^2}\to2\pi t\,\delta(\omega)$ at long times.
- Harmonic perturbation: absorption, stimulated emission, resonance condition and the line width.
- **Fermi's golden rule**: transitions to a continuum, density of states $\rho(E)$, the constant transition rate, its relation to the decay law $e^{-\Gamma t/\hbar}$ and to exponential decay from the Wigner-Weisskopf argument (at an appropriate level).

**Radiation (Zettili Section 10.5, pp. 639 to 649)**
- Dipole interaction with a classical field, the dipole approximation, selection rules ($\Delta\ell=\pm1$, $\Delta m=0,\pm1$) obtained from the Wigner-Eckart theorem, absorption cross-section, spontaneous emission rate (derived with a quantized field, or quoted; Einstein $A$ and $B$ coefficients).

**Other approximations**
- Sudden approximation: if $H$ changes fast, the state does not change; transition probability is the overlap squared.
- Adiabatic approximation: if $H$ changes slowly compared with level spacings, the system stays in the instantaneous eigenstate; the adiabatic theorem; Berry's geometric phase (awareness).
- Two-level systems with periodic driving: Rabi oscillations, the rotating-wave approximation (RWA).

## Reading plan (exact)

| Block | Reading |
| --- | --- |
| Lunch 1 | Sections 10.2 and 10.3.1 (pp. 623 to 630) |
| Lunch 2 | Sections 10.3.2 to 10.3.3 (pp. 630 to 635) |
| Lunch 3 | Section 10.4 (pp. 635 to 639) |
| Lunch 4 | Sections 10.5.1 to 10.5.3 (pp. 639 to 645) |
| Week 2 lunches | Sections 10.5.4 to 10.5.6 (pp. 645 to 650) |
| Evenings | Derivations; then Problems 10.4 to 10.12; exercises |

## Derive from scratch (derivation nights)

1. The Dyson series from the integral equation for $U_I$, including the time-ordering.
2. First-order transition probability for a constant perturbation and the limit $t\to\infty$ giving $\delta(E_f-E_i)$.
3. Fermi's golden rule with density of states, including the units and the case of a continuum with normalization in a box.
4. The two-level Rabi problem in the RWA, giving $P(t)=\frac{\Omega_R^2}{\Omega_R^2+\Delta^2}\sin^2\frac{\sqrt{\Omega_R^2+\Delta^2}\,t}{2}$.
5. The sudden-approximation overlap for tritium $\beta$ decay: the probability that the electron stays in the ground state of He$^+$ is $\left(\frac{2\sqrt{Z_1Z_2}}{Z_1+Z_2}\right)^6=0.70$.

## Bare-minimum exercises (solved-problem keywords: time-dependent perturbation, golden rule, harmonic perturbation, sudden approximation, adiabatic, Rabi)

1. **Constant perturbation:** a perturbation $V_{fi}$ turned on at $t=0$ in a two-level system: give $P_{i\to f}(t)$ and its first-order expansion; confirm agreement with the exact Rabi result for small $V$. *Zettili:* Section 10.3.2; Problems 10.5 and 10.6.
2. **Oscillator driven by a force:** $H'=-eEx\cos\omega t$ starting in $|0\rangle$: first-order transition to $|1\rangle$ with probability $\frac{e^2E^2}{2m\hbar\omega_0}\frac{\sin^2[(\omega-\omega_0)t/2]}{(\omega-\omega_0)^2}$ near resonance (rotating-wave approximation; verify the factor by doing the integral). *Zettili:* Problem 10.7; Exercises 10.4 and 10.15.
3. **Golden rule:** a particle in a box with a weak localized perturbation coupling the bound state to a continuum: obtain the decay rate $\Gamma=\frac{2\pi}\hbar|V_{fi}|^2\rho$ and its units. *Zettili:* Section 10.3.3; Problems 10.10 and 10.12.
4. **Selection rules:** for a dipole transition $2p\to1s$ in hydrogen compute $\langle1s|z|2p,m=0\rangle$ and show $\langle1s|x|2s\rangle=0$; evaluate the dipole matrix element ($=0.745\,a_0$ for $\langle100|z|210\rangle$; verify) and estimate the lifetime ($\sim1.6$ ns for $2p$). *Zettili:* **Problem 10.9** and Section 10.5.5.
5. **Sudden approximation:** tritium $\to$ He$^3$ decay (hydrogenic $Z=1\to2$): probability $0.70$ to remain in the ground state; an infinite well that suddenly doubles its width: transition probabilities to the new levels. *Zettili:* Section 10.4.2; Exercises 10.14, 10.16, 10.17, 10.22.
6. **Adiabatic condition:** a spin-1/2 in a slowly rotating field: show the adiabatic following when $\dot\theta\ll\gamma B$. *Zettili:* Section 10.4.1; no dedicated problem.
7. **Rabi oscillations:** compute the time to flip a spin from $\uparrow$ to $\downarrow$ for a resonant field of Rabi frequency $\Omega_R$ ($T=\pi/\Omega_R$). *Zettili:* not covered; Sakurai or Cohen-Tannoudji.
8. **Decay law:** assume $|c_i|^2=e^{-\Gamma t}$ and show the energy distribution of the final state is Lorentzian with FWHM $\hbar\Gamma$ (preview of Breit-Wigner). *Zettili:* Section 10.5.6; the Wigner-Weisskopf argument is not covered.
9. **Second order:** write the second-order amplitude for $|i\rangle\to|f\rangle$ via intermediate states $|n\rangle$: $\sum_n\frac{V_{fn}V_{ni}}{E_i-E_n}$ and identify the energy-conserving delta function with the *overall* transition; relate to the Feynman-diagram picture of a "virtual" intermediate state. *Zettili:* only first order (Section 10.3.1); second order in Sakurai.
10. **Particle-physics unit conversion:** a particle of mass $m$ decaying with width $\Gamma$ in MeV: convert to lifetime with $\hbar=6.58\times10^{-22}$ MeV s (for example, $\Delta(1232)$ with $\Gamma\approx117$ MeV: $\tau\approx5.6\times10^{-24}$ s). *Zettili:* Problem 10.9 (lifetime numbers).

## Optional extension

Derive the first-order expression for the spontaneous emission rate of hydrogen $2p\to1s$ by treating the quantized radiation field as a bath of oscillators (golden rule with photon states), and match to the Einstein $A$ coefficient. It is the first calculation that mixes QM and quantum field concepts.

## Pitfalls

- Ignoring that the golden rule rate holds only in an intermediate time window (long enough for the delta function, short enough for first-order validity).
- Forgetting the density of final states, or using the wrong normalization of continuum states.
- Confusing $\omega$ (angular frequency) with $\nu$ and missing factors of $\hbar$.
- Treating the sudden limit as exact for any change: it requires change much faster than $\hbar/\Delta E$.

## Gate questions

1. Why is the time-ordered exponential, not a plain exponential, the solution for a time-dependent perturbation?
2. How does a continuum of final states turn an oscillating probability into a constant rate?
3. What is the relation between the Dyson series and Feynman diagrams?

## One-page cheat sheet contents

Dyson series, first-order amplitude, golden rule, harmonic perturbation resonances, Rabi formula, sudden and adiabatic conditions, $\hbar$ conversion factors.
