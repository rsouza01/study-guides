# Module 02: Chapter 2, Foundations (Weeks 2 and 3; Protocol A)

**Books:** Klauber Ch. 2; download his *Pedagogic Aids to Chap 2* and the *Summary of Special Relativity* chart; second source: Tong's lectures on classical fields and the harmonic oscillator.
**Time:** 2 weeks.

## Why this matters

Read properly. This is the chapter you passed by, and much of Module M's motivation lives here. Week 2: the classical mechanics and field theory scaffold: action principle, Euler-Lagrange for fields, canonical momentum density, Hamiltonian density, Poisson brackets and their route to commutators. Week 3: the quantum mechanics Klauber assumes: states, operators, the harmonic-oscillator ladder algebra, and his conventions throughout.

**Concretise:** the harmonic oscillator, fully, with ladder operators. **The free scalar field is infinitely many of these**, and if the single oscillator is not completely concrete then Chapter 3 cannot be.

## Diagnostic (30 minutes, no notes)

1. Derive the ladder algebra $[a,a^\dagger]=1$ for the oscillator and the spectrum $E_n=\omega(n+\tfrac12)$.
2. Derive the Euler-Lagrange equations for a field from Hamilton's principle.
3. For $\mathcal L=\frac12(\partial_\mu\phi)^2-\frac12m^2\phi^2$ find $\pi$ and $\mathcal H$.
4. State the passage from Poisson brackets to commutators and what is assumed.
5. Compute $\langle n|x^2|n\rangle$ for the oscillator.

## Prerequisites

Module 01; Lagrangian mechanics and the harmonic oscillator at the undergraduate level (your mechanics guide, Modules 02 to 03 and 06 to 07, if you have them).

## Detailed topics (checklist)

**Week 2: the classical scaffold [Must]**
- Action $S=\int d^4x\,\mathcal L(\phi,\partial_\mu\phi)$; Euler-Lagrange $\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}=\frac{\partial\mathcal L}{\partial\phi}$; canonical momentum density $\pi=\frac{\partial\mathcal L}{\partial\dot\phi}$; Hamiltonian density $\mathcal H=\pi\dot\phi-\mathcal L$; Poisson brackets of fields $\{\phi(\mathbf x),\pi(\mathbf y)\}=\delta^3(\mathbf x-\mathbf y)$ and the heuristic replacement by commutators.
- Special-relativity summary: Lorentz transformations, four-vectors, signature $(+,-,-,-)$.

**Week 3: the quantum scaffold [Must]**
- States, operators, Hermiticity, observables; the oscillator ladder algebra: $a=\sqrt{\frac{m\omega}2}\left(x+\frac{ip}{m\omega}\right)$, $[a,a^\dagger]=1$, $H=\omega\left(a^\dagger a+\tfrac12\right)$, $a|n\rangle=\sqrt n|n-1\rangle$, $a^\dagger|n\rangle=\sqrt{n+1}|n+1\rangle$; Heisenberg picture $a(t)=ae^{-i\omega t}$; Klauber's conventions (write the dictionary).

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Ch. 2 first half: action and fields; the Poisson-bracket section |
| B1 | Exercises 1 to 3 |
| A2 | The classical-to-quantum step; derive the oscillator algebra |
| B2 | Exercises 4 to 6 |
| A3 | Ch. 2 second half; Klauber's conventions |
| B3 | Exercises 7 to 10; the Pedagogic Aids |

## Derive from scratch

1. The Euler-Lagrange equation for a field.
2. $\pi$ and $\mathcal H$ for the free scalar field.
3. The oscillator spectrum from the ladder algebra.
4. $\langle x^2\rangle_n$ and $\langle p^2\rangle_n$.
5. The Heisenberg equation for $a(t)$.

## Exercises

1. **[T] Oscillator spectrum:** from $[a,a^\dagger]=1$ and $H=\omega(a^\dagger a+\frac12)$ show $E_n=\omega(n+\frac12)$ and $a|n\rangle=\sqrt n|n-1\rangle$; check $[H,a]=-\omega a$.
2. **[T] Expectation values:** $\langle n|x^2|n\rangle=\frac{n+\frac12}{m\omega}$, $\langle n|p^2|n\rangle=m\omega(n+\frac12)$, so $\Delta x\Delta p=(n+\frac12)\ge\frac12$.
3. **[T] Field Euler-Lagrange:** for $\mathcal L=\frac12(\partial_\mu\phi)^2-\frac12m^2\phi^2$ obtain $(\Box+m^2)\phi=0$; for $\mathcal L=\frac12(\partial\phi)^2-\frac12m^2\phi^2-\frac\lambda{4!}\phi^4$ obtain $(\Box+m^2)\phi=-\frac\lambda{3!}\phi^3$.
4. **[T] Canonical quantities:** $\pi=\dot\phi$, $\mathcal H=\frac12\left(\pi^2+(\nabla\phi)^2+m^2\phi^2\right)$.
5. **[T] A single classical mode:** for $\phi=A\cos(\mathbf k\cdot\mathbf x-\omega t)$ in a volume $V$ the energy is $E=\frac12\omega^2A^2V$ with $\omega^2=k^2+m^2$; compare with the oscillator energy $\frac12m\omega^2A_{\rm osc}^2$.
6. **[T] Heisenberg picture:** $\dot a=i[H,a]=-i\omega a$ so $a(t)=ae^{-i\omega t}$.
7. **[C] Lagrangian versus Hamiltonian:** why is the Lagrangian rather than the Hamiltonian the natural starting point for a relativistic theory, and what does the Hamiltonian formulation cost?
8. **[C] Brackets to commutators:** state what is derived and what is assumed in replacing $\{,\}$ by $\frac{1}{i\hbar}[,]$ (Bridge 1 of your mechanics guide treats this if you have it).
9. **[C] The oscillator and the field:** in what precise sense is a free field "infinitely many oscillators", and which mathematical step makes it so?
10. **[C] Explain-it paragraph:** the passage from a classical field theory to a quantum one, no equations.

## Optional extension

Compute $\langle n|x^4|n\rangle=\frac{3}{4m^2\omega^2}(2n^2+2n+1)$ using the ladder operators and note how the classical limit emerges for large $n$.

## Pitfalls

- Treating the Poisson-to-commutator step as derived.
- Mixing Klauber's normalisations with other texts without a dictionary.
- Confusing $\pi$ (canonical momentum density) with $\dot\phi$ outside the free case.

## Gate questions

1. Why is the oscillator the building block of the free field?
2. What changes in the Euler-Lagrange equation from mechanics to fields?
3. Which convention choices in Ch. 2 will affect factors later?

## One-page cheat sheet contents

Oscillator algebra; field Euler-Lagrange; $\pi$ and $\mathcal H$; Klauber's conventions dictionary.
