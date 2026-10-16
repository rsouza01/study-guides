# Module 21: Phase 2, Chapter 18, Path integrals (about 3 weeks; new material)

**Books:** Klauber Ch. 18; second sources: Tong's path-integral lectures, Schwartz chapter 14, Peskin and Schroeder chapter 9, Zee.
**Time:** about 3 weeks. **Read it as the first three weeks of Volume 2**, at full dedication. Protocol A (first-pass material).

## Why this matters

The many-paths construction; the transition to fields and the generating functional; then **the propagator by both routes**: from the generating functional, set beside your canonical derivation from Module 08 and your Module 05 construction. **Three roads, one object.**

## Diagnostic (40 minutes, no notes)

1. Derive the quantum-mechanical path integral by time slicing and state the free-particle propagator.
2. Evaluate the Gaussian integral $\int d^nx\,e^{-\frac12x^TAx+J^Tx}$.
3. Write the free generating functional $Z_0[J]$ and obtain $\langle T\phi\phi\rangle$ from it.
4. Explain the role of $i\epsilon$ in the path integral.
5. State the difference between canonical quantisation and the path integral.

## Prerequisites

Phase 1 (Modules 01 to 19); Module 08 (the propagator).

## Detailed topics (checklist)

- **Quantum mechanics:** $\langle x_f,t_f|x_i,t_i\rangle=\int\mathcal Dx\,e^{iS[x]/\hbar}$ from slicing $e^{-iH\epsilon/\hbar}$ and inserting complete sets of $x$ and $p$ states; free particle $K(x,t;0,0)=\sqrt{\frac{m}{2\pi i\hbar t}}e^{imx^2/2\hbar t}$; stationary phase and the classical limit.
- **Fields:** $Z[J]=\int\mathcal D\phi\,e^{i\int d^4x\left[\mathcal L+J\phi\right]}$; free theory by completing the square: $Z_0[J]=Z_0[0]\exp\left[-\tfrac12\int d^4xd^4y\,J(x)D_F(x-y)J(y)\right]$; correlation functions by functional derivatives $\langle T\phi(x_1)\ldots\phi(x_n)\rangle=\frac{1}{Z_0[0]}\left(-i\frac{\delta}{\delta J(x_1)}\right)\cdots\left(-i\frac{\delta}{\delta J(x_n)}\right)Z_0[J]\Big|_0$; the $i\epsilon$ prescription selects the vacuum (rotating $t\to-i\tau$ makes the Gaussian convergent); perturbation theory by expanding $e^{i\int\mathcal L_{\rm int}[-i\delta/\delta J]}$ and Wick's theorem as Gaussian moment identities.

## Reading plan

| Week | Task |
| --- | --- |
| 1 | Quantum-mechanical path integral; free particle; exercises 1 to 3 |
| 2 | The functional integral for fields; $Z_0[J]$; exercises 4 to 6 |
| 3 | The propagator by three roads; interactions; exercises 7 to 10 |

## Derive from scratch

1. The time-sliced path integral.
2. The free-particle propagator.
3. $Z_0[J]$ by completing the square.
4. The two-point function from $Z_0[J]$.
5. The first-order $\phi^4$ correction.

## Exercises

1. **[T] Free particle:** $K=\sqrt{\frac{m}{2\pi i\hbar t}}\exp\left[\frac{im(x-x')^2}{2\hbar t}\right]$; check $K\to\delta(x-x')$ as $t\to0$ and that it solves the free Schrodinger equation.
2. **[T] Gaussian integral:** $\int dx\,e^{-\frac a2x^2+Jx}=\sqrt{\frac{2\pi}{a}}e^{J^2/2a}$; in $n$ dimensions $\int d^nx\,e^{-\frac12x^TAx+J^Tx}=\frac{(2\pi)^{n/2}}{\sqrt{\det A}}e^{\frac12J^TA^{-1}J}$.
3. **[T] Classical limit:** stationary phase $\delta S=0$ gives the classical path; for the harmonic oscillator the path integral is exact (Gaussian).
4. **[T] Free field:** with $S=\int\left[\tfrac12\phi(-\Box-m^2)\phi+J\phi\right]$ the operator $A=-(\Box+m^2)$ has inverse $\frac{-i}{\ldots}$; completing the square gives $Z_0[J]=Z_0[0]\exp\left[-\tfrac12\int JD_FJ\right]$ with $D_F(x-y)=\int\frac{d^4k}{(2\pi)^4}\frac{i\,e^{-ik\cdot(x-y)}}{k^2-m^2+i\epsilon}$.
5. **[T] Two-point function:** $\langle T\phi(x)\phi(y)\rangle=(-i)^2\frac{\delta^2}{\delta J(x)\delta J(y)}\exp\left[-\tfrac12\int JD_FJ\right]\Big|_0=D_F(x-y)$: *the same object as Module 08, Module 05*.
6. **[T] The $i\epsilon$:** write $\epsilon$ as a convergence factor $e^{-\epsilon\int\phi^2}$ in the exponent; equivalently rotate $t\to-i\tau$ so $e^{iS}\to e^{-S_E}$ is a real Gaussian and the propagator becomes $\int\frac{d^4k_E}{(2\pi)^4}\frac{e^{ik_E\cdot x}}{k_E^2+m^2}$.
7. **[T] First-order $\phi^4$:** $Z[J]\supset\frac{-i\lambda}{4!}\int d^4z\left(-i\frac\delta{\delta J(z)}\right)^4Z_0[J]$; the connected four-point function $=-i\lambda\int d^4z\prod_{i=1}^4D_F(x_i-z)$, matching Module 13 exercise 3 (the $4!$ cancels, now as derivative counting).
8. **[T] Three roads for the propagator:** (a) canonical: $\langle0|T\phi\phi|0\rangle$ by residues (Module 08); (b) Green function: $(\Box+m^2)G=-\delta^4$ with Feynman boundary conditions (Module 05); (c) path integral: Gaussian functional integral. Write the three derivations side by side and say what is the same and what is different.
9. **[C] Canonical versus path integral:** what is the same and what is genuinely different between canonical quantisation and the path integral (operators versus c-numbers, Hamiltonian versus Lagrangian, manifest covariance, what is hard to see in each)?
10. **[C] Explain-it:** what is $\int\mathcal D\phi$, in a paragraph without equations, and why is the propagator its second moment?

## Optional extension

Derive the generating functional for the Dirac field with Grassmann sources and obtain $Z_0[\eta,\bar\eta]=\exp\left[-\int\bar\eta S_F\eta\right]$.

## Pitfalls

- Treating $\mathcal D\phi$ as rigorously defined without a regulator.
- Forgetting the $i\epsilon$ (the path integral is oscillatory).
- Assuming the Euclidean rotation is only a trick (it defines the vacuum).

## Gate questions

1. Why is the Feynman propagator the second moment of $e^{iS}$?
2. Where do Wick's theorem and Gaussian moments coincide?
3. Which formulation makes symmetries and gauge invariance easier to handle?

## One-page cheat sheet contents

Time-sliced path integral; free-particle propagator; $Z_0[J]$; three-roads comparison.
