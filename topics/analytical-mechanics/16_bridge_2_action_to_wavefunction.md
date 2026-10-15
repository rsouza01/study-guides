# Module 16: Bridge 2, from the action to the wavefunction (★★★)

**Books:** Goldstein, the section on Hamilton-Jacobi theory, geometrical optics and wave mechanics (10.8 or 10.9 depending on your printing; it follows the Kepler problem in action-angle variables); Griffiths *Quantum Mechanics*, the WKB chapter (reread with action-angle variables in hand); **Dirac (1933), "The Lagrangian in Quantum Mechanics"** (about six pages, freely available: the paper Feynman read); **Feynman and Hibbs, chapters 1 and 2** (or Feynman's 1948 *Rev. Mod. Phys.* paper, sections 1 to 4); your Zettili guide (Section 9.4 on WKB, Section 10.2 on pictures).
**Time:** 3 weeks (six sessions). **A written deliverable.** This is the section that most directly addresses "the transition is too blurry."

## Why this matters for the bridge

Goldstein gives the connection between Hamilton-Jacobi theory and wave mechanics a handful of pages. It deserves three weeks. You are about to prove that $S/\hbar$ *is the phase of the wavefunction*, that the Hamilton-Jacobi equation is the $\hbar\to0$ limit of the Schrödinger equation, and that classical mechanics is the stationary-phase approximation to quantum mechanics. Together with Bridge 1 you will then have two independent routes from classical to quantum structure: the **algebraic** one (Poisson bracket $\to$ commutator) and the **analytic** one (action $\to$ phase). These are the operator and path-integral formulations respectively.

## Skip-test (40 minutes, no notes)

1. Substitute $\psi=A\,e^{iS/\hbar}$ ($A,S$ real) into $i\hbar\partial_t\psi=-\frac{\hbar^2}{2m}\nabla^2\psi+V\psi$ and separate real and imaginary parts.
2. Show that the real part is $\frac{\partial S}{\partial t}+\frac{(\nabla S)^2}{2m}+V=\frac{\hbar^2}{2m}\frac{\nabla^2A}{A}$ and the imaginary part is the continuity equation $\partial_t(A^2)+\nabla\cdot\left(A^2\frac{\nabla S}{m}\right)=0$.
3. State what happens to the real part as $\hbar\to0$.
4. State Dirac's observation: $e^{iS_{\rm cl}/\hbar}$ is the phase associated with a path; stationary phase picks out $\delta S=0$.
5. Write the free-particle propagator $K(x_b,t_b;x_a,t_a)=\sqrt{\frac{m}{2\pi i\hbar T}}\exp\left[\frac{im(x_b-x_a)^2}{2\hbar T}\right]$ and identify the exponent.

## Prerequisites

Modules 03, 14, 15; a working knowledge of the Schrödinger equation (Zettili Module 02).

## Detailed topics (checklist)

**The optical analogy [Must]**
- Geometrical optics is the short-wavelength limit of wave optics; the eikonal equation $|\nabla\phi|=n$ plays the role of the HJ equation; Fermat's principle $\delta\int n\,ds=0$ is the optical analogue of Maupertuis' principle $\delta\int p\,dq=0$. **Correspondence table to build yourself:** wavefront $\leftrightarrow$ surface of constant $S$; ray $\leftrightarrow$ trajectory; refractive index $\leftrightarrow$ $|\mathbf p|=\sqrt{2m(E-V)}$; eikonal equation $\leftrightarrow$ HJ equation; wavelength $\to0$ $\leftrightarrow$ $\hbar\to0$.

**The substitution $\psi=Ae^{iS/\hbar}$ [Must]**
- Real part: $\frac{\partial S}{\partial t}+\frac{(\nabla S)^2}{2m}+V+Q=0$ with $Q=-\frac{\hbar^2}{2m}\frac{\nabla^2A}{A}$ (the "quantum potential" in the Bohmian language); as $\hbar\to0$ this is the HJ equation. Imaginary part: continuity equation with density $\rho=A^2$ and velocity field $\mathbf v=\nabla S/m$ (Madelung hydrodynamics). **The classical limit is singular:** it is not a smooth deformation but an asymptotic expansion in $\hbar$ (WKB), which is why the correspondence is delicate.
- WKB: $\psi\approx\frac{C}{\sqrt{p}}e^{\frac i\hbar\int p\,dx}$; breakdown at turning points; connection formulas and the Maslov index (Module 15).

**The inversion: stationary phase and the path integral [Must]**
- If $S/\hbar$ is the phase, a wave picture assigns each path the phase $e^{iS[x(t)]/\hbar}$ and superposes: $K(b,a)=\int\mathcal Dx\,e^{iS[x]/\hbar}$. As $\hbar\to0$ the phases oscillate violently and cancel except near $\delta S=0$: **classical mechanics is the stationary-phase approximation to quantum mechanics.** Time slicing and the free-particle kernel.
- Semiclassical propagator (van Vleck): $K\approx\frac{1}{\sqrt{2\pi i\hbar}}\sqrt{-\frac{\partial^2S_{\rm cl}}{\partial x_a\partial x_b}}\,e^{iS_{\rm cl}/\hbar}$, *exact* for quadratic actions (free particle, harmonic oscillator).
- Harmonic oscillator: $K=\sqrt{\frac{m\omega}{2\pi i\hbar\sin\omega T}}\exp\left\{\frac{im\omega}{2\hbar\sin\omega T}\left[(x_a^2+x_b^2)\cos\omega T-2x_ax_b\right]\right\}$, with exponent the classical action from Module 03.

**Gauge and minimal coupling [Should]**
- Under $\mathbf A\to\mathbf A+\nabla\Lambda$ the classical $S\to S+q\Lambda$ (Module 14) and the wavefunction transforms as $\psi\to e^{iq\Lambda/\hbar}\psi$: the quantum phase *is* the action. **Aharonov-Bohm:** a particle encircling a flux $\Phi$ picks up the phase $\frac q\hbar\oint\mathbf A\cdot d\mathbf l=\frac{q\Phi}{\hbar}$, observable even where $\mathbf B=0$.

**Close the loop with Bridge 1 [Must]**
- State how each route recovers the other's starting point: from the path integral one derives the Schrödinger equation (hence the commutators); from the commutators and the Heisenberg equation one derives the propagator.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Goldstein HJ/wave-mechanics section; build the optical correspondence table |
| B1 | Exercises 1 to 3 |
| A2 | Griffiths WKB chapter; do the $\psi=Ae^{iS/\hbar}$ substitution by hand (about an hour) |
| B2 | Exercises 4 to 6 |
| A3 | Dirac (1933); Feynman and Hibbs chapters 1 to 2 (or Feynman 1948 sections 1 to 4) |
| B3 | Exercises 7 to 10; **write the deliverable** |

## Derive from scratch (A sessions, book closed)

1. The substitution $\psi=Ae^{iS/\hbar}$ into the Schrödinger equation; real and imaginary parts.
2. The continuity equation from the imaginary part.
3. The free-particle propagator by time slicing (or by verifying that it satisfies the Schrödinger equation with $K\to\delta(x_b-x_a)$ as $T\to0$).
4. The stationary-phase formula $\int e^{iS(x)/\hbar}dx\approx\sqrt{\frac{2\pi i\hbar}{S''(x_0)}}e^{iS(x_0)/\hbar}$.
5. The van Vleck prefactor for the harmonic oscillator from the classical action.

## Bare-minimum exercises (with expected results)

1. **Substitution:** carry out the substitution by hand and write out both equations (real: HJ plus quantum potential; imaginary: continuity).
2. **Continuity:** show the imaginary part is $\partial_t\rho+\nabla\cdot(\rho\,\nabla S/m)=0$ with $\rho=A^2$, and that it is equivalent to $\partial_t|\psi|^2+\nabla\cdot\mathbf j=0$ with $\mathbf j=\frac{\hbar}{2mi}(\psi^*\nabla\psi-\psi\nabla\psi^*)$.
3. **Plane wave:** for $\psi=e^{i(px-Et)/\hbar}$ show $S=px-Et$ solves the HJ equation *exactly* ($A$ constant, $Q=0$): the free particle is classical in this sense.
4. **Gaussian packet:** for a free packet of width $\sigma_0$ show that $A$ is not constant, $Q\ne0$, and the width grows as $\sigma(t)=\sigma_0\sqrt{1+\left(\frac{\hbar t}{2m\sigma_0^2}\right)^2}$; the quantum potential is what spreads the packet.
5. **Free propagator:** verify that $K=\sqrt{\frac m{2\pi i\hbar T}}e^{\frac{im(x_b-x_a)^2}{2\hbar T}}$ satisfies the free Schrödinger equation in $(x_b,t_b)$ and tends to $\delta(x_b-x_a)$ as $T\to0$; note its exponent is the classical action $\frac{m(x_b-x_a)^2}{2T}$.
6. **Van Vleck for the oscillator:** from $S_{\rm cl}$ (Module 03 exercise 7) compute $-\frac{\partial^2S_{\rm cl}}{\partial x_a\partial x_b}=\frac{m\omega}{\sin\omega T}$ and confirm the prefactor $\sqrt{\frac{m\omega}{2\pi i\hbar\sin\omega T}}$; check that it tends to the free-particle prefactor as $\omega\to0$.
7. **Stationary phase:** evaluate $\int_{-\infty}^\infty e^{i\lambda x^2/2}dx=\sqrt{\frac{2\pi i}{\lambda}}$ exactly (Fresnel) and compare with the stationary-phase formula; show the correction vanishes for a quadratic phase.
8. **Aharonov-Bohm:** show that the phase difference between paths on either side of a solenoid is $\frac{q\Phi}{\hbar}$; the flux quantum for $q=e$ is $\Phi_0=\frac he=4.14\times10^{-15}$ Wb (the shift by one fringe).
9. **Gauge covariance:** verify that $\psi\to e^{iq\Lambda/\hbar}\psi$ with $\mathbf A\to\mathbf A+\nabla\Lambda$ leaves the minimally coupled Schrödinger equation $i\hbar\partial_t\psi=\frac{(-i\hbar\nabla-q\mathbf A)^2}{2m}\psi+q\Phi\psi$ invariant (with $\Phi\to\Phi-\partial_t\Lambda$).
10. **Singular limit:** write the WKB series $\psi=\exp\left[\frac i\hbar(S_0+\hbar S_1+\hbar^2S_2+\dots)\right]$ for the 1D time-independent Schrödinger equation; show $S_0'=p$, $S_1=\frac i2\ln p$ (so the amplitude is $1/\sqrt p$), and that the next term $S_2$ diverges as $p\to0$ at a turning point: the series is asymptotic, not convergent, and fails exactly where the classical momentum vanishes.

## The deliverable: `bridge2.md` (4 to 6 pages, your own words)

Work through and write up, **in this order**:
1. **The optical analogy.** Build the full correspondence table (wavefront $\leftrightarrow$ $S=$ const; ray $\leftrightarrow$ trajectory; refractive index $\leftrightarrow$ $|\mathbf p|$; eikonal $\leftrightarrow$ HJ; $\lambda\to0$ $\leftrightarrow$ $\hbar\to0$).
2. **The substitution.** Put $\psi=Ae^{iS/\hbar}$ into Schrödinger by hand; show the real part is HJ plus $\frac{\hbar^2}{2m}\frac{\nabla^2A}{A}$ and the imaginary part is probability conservation. State the answer to "what is the relation between $\psi$ and $S$": **$S/\hbar$ is the phase.**
3. **The residual term.** That quantum-potential term is the whole of quantum mechanics in this formulation; the classical limit is singular.
4. **The inversion.** If $S$ is the phase, a wave picture assigns each path $e^{iS/\hbar}$ and superposes; stationary phase picks out $\delta S=0$. **Classical mechanics is the stationary-phase approximation to quantum mechanics.** Write this out with the free-particle kernel.
5. **Close the loop with Bridge 1.** State how each route recovers the other's starting point.

**Rubric (2 points each):** correct substitution and separation; correct continuity equation; correct correspondence table; stationary-phase argument with the free-particle kernel; the loop closure with Bridge 1. *If you write nothing else in six months, write this document.*

## Pitfalls

- Treating the classical limit as a smooth limit rather than an asymptotic expansion.
- Taking $e^{iS/\hbar}$ with $S$ not on-shell as the amplitude of a path (the path integral sums over all paths with their own actions).
- Believing the quantum potential is a force that "causes" quantum effects (it is a rewriting of the Schrödinger equation).
- Forgetting the prefactor in the propagator.

## Gate questions

1. What is the relation between the wavefunction and the action?
2. In what sense is classical mechanics a stationary-phase approximation?
3. How do the algebraic (Bridge 1) and analytic (Bridge 2) bridges recover each other?

## One-page cheat sheet contents

The substitution and its two equations; the optical table; stationary phase; free and oscillator propagators; van Vleck formula; Aharonov-Bohm phase.
