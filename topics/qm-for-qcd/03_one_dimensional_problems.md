# Module 03: One-dimensional problems

**Zettili:** Chapter 4, *One-Dimensional Problems* (printed pp. 241–312; PDF pp. 261–332), with Section 4.9 (numerical solution of the Schrodinger equation) and Appendix C (C++ code, p. 945).
**Time:** 2 weeks.

## Zettili pin (exact, from your 3rd edition)

PDF page = printed page + 20.

| Section | Printed page | Role |
| --- | --- | --- |
| 4.2 Properties of 1D motion (bound, continuous, mixed spectrum; parity) | 242 to 244 | core |
| 4.3 Free particle | 244 | core |
| 4.4 Potential step | 246 | core |
| 4.5 Barrier and well (4.5.1 $E>V_0$; 4.5.2 $E<V_0$, tunneling; 4.5.3 tunneling effect) | 250 to 257 | core |
| 4.6 Infinite square well | 258 | skim |
| 4.7 Finite square well (scattering and bound states) | 262 | core |
| 4.8 Harmonic oscillator (4.8.1 to 4.8.5: eigenvalues, states, position space, matrix representation, expectation values) | 266 to 277 | core |
| 4.9 Numerical solution of the Schrodinger equation | 277 to 280 | core for the projects |
| 4.10 Solved Problems 4.1 to 4.18 | 281 to 304 | exercise pool |
| 4.11 Exercises 4.1 to 4.34 | 305 to 312 | extra pool |
| Appendix C: C++ code for the Schrodinger equation | 945 | template for your Python version |

**Solved problems to do:** 4.4 (attractive delta), 4.5 (double delta), 4.6 (delta on a half-line: bound-state condition), 4.8 (uncertainty principle gives $\hbar\omega/2$), 4.9 (oscillator on a half-line), 4.11 (matrix representation of $X,P$ in $N$-space), 4.12 (classically forbidden region), 4.13 (infinite wall plus well), 4.15 ($\langle X^4\rangle$ in $N$-space), 4.17 (charged oscillator in a constant field), 4.18 (bouncing ball, numerical).
**Unsolved exercises worth doing:** 4.3, 4.5, 4.8, 4.10, 4.14, 4.15, 4.23 to 4.26, 4.29 to 4.32.
**Not in Zettili:** coherent states of the oscillator; use Sakurai or Cohen-Tannoudji.

## Why this matters for QCD

- **The harmonic oscillator algebra** ($a$, $a^\dagger$, $[a,a^\dagger]=1$, number operator, Fock states, coherent states) is the template of *every* QFT mode. Master it as an algebra, not as a differential equation.
- **Tunneling** is the physics behind instantons and the QCD vacuum structure, and behind the Gamow factor in nuclear fusion.
- **Delta-function potentials** model contact interactions and zero-range scattering (nuclear physics, effective field theory).
- **Bound-state versus scattering-state analysis** (poles of the transmission amplitude) prepares scattering theory (Module 10).

## Skip-test (40 minutes, no notes)

1. Define $a$ and $a^\dagger$ for the oscillator, show $[a,a^\dagger]=1$, $H=\hbar\omega(a^\dagger a+\frac12)$, and derive $E_n=\hbar\omega(n+\frac12)$ and $a^\dagger|n\rangle=\sqrt{n+1}|n+1\rangle$.
2. Compute $\langle n|x^2|n\rangle$ and $\langle n|p^2|n\rangle$ and verify the virial theorem $\langle T\rangle=\langle V\rangle$.
3. Find the bound state of $V=-\alpha\delta(x)$: $\kappa=m\alpha/\hbar^2$, $E=-m\alpha^2/2\hbar^2$.
4. Derive the transmission coefficient through $V=\alpha\delta(x)$: $T=1/(1+m\alpha^2/2\hbar^2E)$.
5. For a rectangular barrier of height $V_0$ and width $a$ with $E<V_0$, write $T\approx e^{-2\kappa a}$ with $\kappa=\sqrt{2m(V_0-E)}/\hbar$ and explain when it holds.

## Prerequisites

Modules 01 and 02. Solving second-order ODEs with constant coefficients, matching conditions.

## Detailed topics (checklist)

**General properties**
- Time-independent Schrodinger equation, boundary and matching conditions (continuity of $\psi$; $\psi'$ continuous unless the potential has a delta function: jump $\Delta\psi'=\frac{2m}{\hbar^2}\alpha\,\psi(0)$ for $V=\alpha\delta(x)$).
- Bound states are non-degenerate in 1D; the node theorem (the $n$-th state has $n$ nodes); parity of eigenstates for even potentials.
- Bound versus scattering states; normalization to a delta function for scattering.

**Free particle and wave packets**
- Plane waves, group and phase velocity, Gaussian wave packet and its spreading: $\sigma(t)=\sigma_0\sqrt{1+(\hbar t/2m\sigma_0^2)^2}$.

**Square potentials**
- Infinite and finite square wells (even and odd solutions, transcendental equations, number of bound states, at least one in 1D for any attractive well).
- Potential step, reflection and transmission, the $E<V_0$ evanescent wave, current conservation $R+T=1$.
- Rectangular barrier, resonant transmission above the barrier, tunneling and the thick-barrier limit.
- Delta potential: bound state, scattering, and the double-delta potential (formation of a symmetric and an antisymmetric state).

**Harmonic oscillator**
- Operator method: $a=\sqrt{\frac{m\omega}{2\hbar}}\left(x+\frac{ip}{m\omega}\right)$, $N=a^\dagger a$, spectrum, ladder action, ground state from $a|0\rangle=0$, excited states $|n\rangle=\frac{(a^\dagger)^n}{\sqrt{n!}}|0\rangle$.
- Wave functions with Hermite polynomials (know the form, derive the ground state only).
- Matrix elements of $x$ and $p$ in the number basis; selection rule $\Delta n=\pm1$.
- Coherent states $a|\alpha\rangle=\alpha|\alpha\rangle$: $|\alpha\rangle=e^{-|\alpha|^2/2}\sum_n\frac{\alpha^n}{\sqrt{n!}}|n\rangle$, Poisson photon-number distribution, minimal uncertainty, time evolution of a coherent state is a coherent state (not in Zettili; read Sakurai or the Cohen-Tannoudji complements).
- Link to second quantization: a field mode is an oscillator, $a^\dagger$ creates a quantum.

## Reading plan (exact)

| Block | Reading |
| --- | --- |
| Lunch 1 | Sections 4.2 to 4.3 (pp. 242 to 246) |
| Lunch 2 | Sections 4.4 to 4.5.1 (pp. 246 to 254) |
| Lunch 3 | Sections 4.5.2 to 4.5.3 and 4.7 (pp. 254 to 266) |
| Lunch 4 | Section 4.8.1 to 4.8.3 (pp. 266 to 275) |
| Week 2 lunches | Sections 4.8.4 to 4.9 (pp. 275 to 280) and Appendix C (p. 945) |
| Evenings | Derivations; then Problems 4.4 to 4.18; exercises |

## Derive from scratch (derivation nights)

1. Ladder operator algebra and the spectrum of the oscillator, including proof that the spectrum is bounded below and has no gaps.
2. Delta-function potential: bound state energy, and the transmission amplitude $t=\frac{1}{1+i m\alpha/(\hbar^2k)}$ and its pole at $k=i m\alpha/\hbar^2$ for the attractive case (bound state as a pole of $t(k)$).
3. The barrier transmission coefficient in the thick-barrier limit.
4. Oscillator matrix elements $\langle m|x|n\rangle$, $\langle m|x^2|n\rangle$ from the algebra.
5. Gaussian wave packet spreading.

## Bare-minimum exercises (solved-problem keywords: oscillator, ladder operators, delta potential, barrier, well)

1. **Oscillator algebra:** express $x,p$ via $a,a^\dagger$, compute $\Delta x\Delta p$ in $|n\rangle$ ($=\hbar(n+\frac12)$). *Zettili:* Problems 4.11 and 4.15; Exercises 4.10 and 4.14.
2. **Perturbed oscillator state:** the state $|\psi\rangle=\frac1{\sqrt2}(|0\rangle+|1\rangle)$: compute $\langle x\rangle(t)=\sqrt{\frac{\hbar}{2m\omega}}\cos\omega t$. *Zettili:* Exercises 4.2, 4.9, 4.14.
3. **Coherent state:** show $\langle x\rangle,\langle p\rangle$ follow the classical orbit and $\Delta x\Delta p=\hbar/2$ for all time. *Zettili:* not covered; use Sakurai or Cohen-Tannoudji.
4. **Delta bound state:** find $\psi(x)=\sqrt\kappa e^{-\kappa|x|}$ and check normalization. *Zettili:* Problem 4.4.
5. **Finite square well:** for a well of depth $V_0$ and width $2a$, count bound states from $\sqrt{2mV_0a^2/\hbar^2}$ and solve graphically the even-state equation $\xi\tan\xi=\sqrt{\xi_0^2-\xi^2}$; check that a shallow well still has one bound state. *Zettili:* Exercise 4.15; Problem 4.13.
6. **Step potential:** compute $R$ and $T$ for $E>V_0$ and verify $R+T=1$ (using the current, not $|t|^2$). *Zettili:* Section 4.4 examples; Exercises 4.3 and 4.8.
7. **Tunneling estimate:** electron with $E=1$ eV on a 2 eV barrier of width 1 nm: compute $T\approx e^{-2\kappa a}$ ($\kappa\approx5.1\ \mathrm{nm}^{-1}$, so $T\sim4\times10^{-5}$, verify). *Zettili:* Section 4.5.3; Exercises 4.3 and 4.5.
8. **Double delta:** find the two bound-state conditions and show that the antisymmetric state exists only for large enough separation. *Zettili:* Problem 4.5; Exercise 4.24.
9. **Wave-packet spreading:** a Gaussian with $\sigma_0=1$ nm for an electron; estimate when its width doubles ($t=2\sqrt3\,m\sigma_0^2/\hbar\approx30$ fs; verify). *Zettili:* Section 3.6.3 and Chapter 1 wave packets (1.8); Problem 3.14.
10. **Parity and nodes:** classify the first three oscillator states by parity and node count. *Zettili:* Section 4.2.4; Problem 4.9 (only odd states survive on a half-line).

## Optional extension

Numerically solve the Schrodinger equation in a double-well potential by diagonalizing the Hamiltonian in an oscillator basis (a 30-line Python script), and measure the splitting between the two lowest levels as a function of barrier height. Compare with a WKB-style $e^{-\int\kappa\,dx}$ estimate (preview of Module 08 and of instantons).

## Pitfalls

- Matching $\psi'$ across a delta potential as if it were continuous.
- Using $|t|^2$ instead of the probability current when the velocities differ on the two sides (steps).
- Treating the oscillator in the position representation first; use the algebra first.
- Confusing the sign convention of the ladder operators with those in a QFT text; they match $a|0\rangle=0$.

## Gate questions

1. Why is the ground state of a 1D attractive potential always bound and non-degenerate?
2. What does the pole of the transmission amplitude in the complex $k$ plane tell you?
3. Why is the oscillator the building block of free quantum fields?

## One-page cheat sheet contents

Oscillator algebra and matrix elements, delta-potential results, barrier formulas, coherent-state definitions.
