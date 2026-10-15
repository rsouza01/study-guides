# Module 14: The Hamilton-Jacobi equation (★★★)

**Books:** Goldstein 10.1 to 10.5 (HJ for the principal function; the harmonic oscillator as an example; HJ for the characteristic function; separation of variables; ignorable coordinates and the Kepler problem); Landau and Lifshitz *Mechanics* sections 46 to 48 (optional); Arnold, chapter 9 (optional).
**Time:** 3 weeks (six sessions).

## Why this matters for the bridge

Hamilton-Jacobi theory is the endpoint of the canonical-transformation programme: find the canonical transformation that makes the new Hamiltonian *zero*, so that all new coordinates and momenta are constants. The generating function that does it is **Hamilton's principal function $S$**, which satisfies

$$H\!\left(q,\frac{\partial S}{\partial q},t\right)+\frac{\partial S}{\partial t}=0.$$

Two facts to fix in your head now, because they are the crux of Module 16:

- **$S$ is the action**, evaluated along the actual trajectory, as a function of the endpoint.
- **$\partial S/\partial q=p$: the momentum is the gradient of the action.** Surfaces of constant $S$ are wavefronts and trajectories cross them perpendicularly. This is a wave-front picture, not a metaphor.

## Skip-test (40 minutes, no notes)

1. Derive the HJ equation by requiring that a type-$F_2$ generating function $S(q,P,t)$ produces $K=0$.
2. For time-independent $H$ write $S=W(q,\alpha)-Et$ and derive the characteristic-function equation $H(q,\partial W/\partial q)=E$.
3. State Jacobi's theorem: $\beta_i=\partial S/\partial\alpha_i$ are constants and $p_i=\partial S/\partial q_i$; the trajectory follows from solving $\beta_i=\partial S/\partial\alpha_i$ for $q_i(t)$.
4. Solve the free particle by HJ: $S=\alpha x-\frac{\alpha^2}{2m}t$, $p=\alpha$, $x=\beta+\alpha t/m$.
5. Show that $S$ equals the action along the classical path: $\frac{dS}{dt}=L$.

## Prerequisites

Modules 07, 08, 09. Module 03 exercise 8 (the boundary term $[p\delta q]$).

## Detailed topics (checklist)

**The HJ equation (10.1) [Must]**
- Requiring a canonical transformation to produce $K=0$: $H(q,\partial S/\partial q,t)+\partial S/\partial t=0$; a first-order nonlinear PDE in $n+1$ variables; a **complete integral** $S(q_1,\dots,q_n,\alpha_1,\dots,\alpha_n,t)$ with $n$ constants $\alpha_i$ (the new momenta); the new coordinates $\beta_i=\partial S/\partial\alpha_i$ are constant; $p_i=\partial S/\partial q_i$.
- **Interpretation of $S$:** $\frac{dS}{dt}=\sum p\dot q-H=L$, so $S=\int L\,dt$ along the path. $S(q_b,t_b;q_a,t_a)$ viewed as a function of the endpoint satisfies $\partial S/\partial q_b=p_b$, $\partial S/\partial t_b=-H$ (the boundary-term result of Module 03).
- Waves: surfaces $S(q,t)=$ const move through configuration space; the momentum is the gradient of $S$.

**Time-independent case (10.3) [Must]**
- $S=W(q,\alpha_1)-\alpha_1t$ with $\alpha_1=E$; the **characteristic function** $W$ satisfies $H(q,\partial W/\partial q)=E$; $W=\int p\,dq$ is the abbreviated action (Maupertuis, Module 07); trajectories are orthogonal to the level surfaces of $W$; the time dependence from $t+\beta_1=\partial W/\partial E$.

**Examples (10.2) [Must]**
- Free particle; harmonic oscillator ($W=\int\sqrt{2mE-m^2\omega^2q^2}\,dq$, $t+\beta=\frac1\omega\arcsin\left(q\sqrt{\frac{m\omega^2}{2E}}\right)$, i.e. $q=\sqrt{\frac{2E}{m\omega^2}}\sin\omega(t+\beta)$); uniform gravitational field.

**Separation of variables (10.4 to 10.5) [Must]**
- If the HJ equation separates, $W=\sum W_i(q_i,\alpha)$; coordinates in which separation works (Cartesian, spherical, parabolic for Kepler); **ignorable (cyclic) coordinates** give $W_j=\alpha_jq_j$ with $p_j=\alpha_j$.
- The Kepler problem in spherical coordinates: $p_\phi=\alpha_\phi$, $p_\theta^2+\frac{\alpha_\phi^2}{\sin^2\theta}=\alpha_\theta^2$ ($=L^2$), $p_r^2+\frac{L^2}{r^2}=2\mu(E-V)$; the orbit equation from $\beta_\theta=\partial W/\partial\alpha_\theta$.

**Gauge covariance [Should]**
- For a charge in an EM field: $\frac{(\nabla S-q\mathbf A)^2}{2m}+q\Phi+\frac{\partial S}{\partial t}=0$; under $\mathbf A\to\mathbf A+\nabla\Lambda$, $\Phi\to\Phi-\partial_t\Lambda$ the equation is covariant with $S\to S+q\Lambda$. (In QM this is $\psi\to e^{iq\Lambda/\hbar}\psi$; Module 16.)

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Goldstein 10.1; derive the HJ equation closed-book |
| B1 | Exercises 1 to 3 |
| A2 | Goldstein 10.2 to 10.3; derive the oscillator solution and the characteristic-function equation |
| B2 | Exercises 4 to 6 |
| A3 | Goldstein 10.4 to 10.5; derive the separation for a central potential |
| B3 | Exercises 7 to 10; cheat sheet |

## Derive from scratch (A sessions, book closed)

1. The HJ equation from the requirement $K=0$.
2. $\frac{dS}{dt}=L$ and the endpoint relations $\partial S/\partial q=p$, $\partial S/\partial t=-H$.
3. The characteristic-function equation and the trajectory from $t+\beta=\partial W/\partial E$.
4. The harmonic-oscillator solution by HJ.
5. The separation of the HJ equation in spherical coordinates for a central potential.

## Bare-minimum exercises (with expected results)

1. **Free particle:** $S(x,\alpha,t)=\alpha x-\frac{\alpha^2t}{2m}$; $p=\alpha$; $\beta=\partial S/\partial\alpha=x-\alpha t/m$ constant gives $x=\beta+\alpha t/m$.
2. **Harmonic oscillator:** $W=\int\sqrt{2mE-m^2\omega^2q^2}\,dq$; $t+\beta=\partial W/\partial E=\int\frac{m\,dq}{p}$ gives $q=\sqrt{\frac{2E}{m\omega^2}}\sin\omega(t+\beta)$.
3. **$S$ is the action:** for the free particle show $S(x,t;x_0)=\frac{m(x-x_0)^2}{2t}$ satisfies HJ ($\frac{\partial S}{\partial t}+\frac12m^{-1}\left(\frac{\partial S}{\partial x}\right)^2=0$) and equals the classical action from Module 03.
4. **Uniform field:** for $H=\frac{p^2}{2m}+mgz$ show $W=-\frac{1}{3m^2g}\left[2m(E-mgz)\right]^{3/2}$ gives $p=\sqrt{2m(E-mgz)}$ and $t+\beta=-\frac{p}{mg}$, i.e. $p=-mg(t+\beta)$.
5. **Oscillator action:** check that $S_{\rm cl}(q_b,q_a,T)=\frac{m\omega}{2\sin\omega T}[(q_a^2+q_b^2)\cos\omega T-2q_aq_b]$ (Module 03, exercise 7) satisfies the HJ equation; verify $\partial S/\partial q_b=p_b$.
6. **Wavefronts:** for the free particle in 2D with $S=\mathbf p\cdot\mathbf r-Et$ draw surfaces of constant $S$ at two times and show trajectories are orthogonal to them. For $H=\frac{p^2}{2m}+V(r)$ at fixed $E$ the constant-$W$ surfaces and the rays $\mathbf p=\nabla W$ obey $|\nabla W|=\sqrt{2m(E-V)}$, the eikonal equation with "refractive index" $n=\sqrt{2m(E-V)}$.
7. **Spherical separation:** for $H=\frac{p^2}{2\mu}+V(r)$ show $W=\alpha_\phi\phi+W_\theta(\theta)+W_r(r)$ with $p_\theta^2+\frac{\alpha_\phi^2}{\sin^2\theta}=L^2$ and $p_r=\sqrt{2\mu(E-V)-\frac{L^2}{r^2}}$, and obtain the orbit $\theta_{\rm orb}-\theta_0=\int\frac{L\,dr}{r^2\sqrt{2\mu(E-V)-L^2/r^2}}$.
8. **Two ways to separate:** solve the 2D isotropic oscillator in Cartesian coordinates ($E=E_x+E_y$) and in polar coordinates ($L$ and $E$); show the Cartesian separation makes the degeneracy ($E$ depends only on $E_x+E_y$) obvious.
9. **Gauge covariance:** show that if $S$ solves $\frac{(\nabla S-q\mathbf A)^2}{2m}+q\Phi+\partial_tS=0$ then $S'=S+q\Lambda$ solves the same equation with $\mathbf A'=\mathbf A+\nabla\Lambda$, $\Phi'=\Phi-\partial_t\Lambda$.
10. **Jacobi's theorem:** for $n=1$ show how the constant $\beta$ turns into an initial condition and the momentum $p=\partial S/\partial q$ is single-valued only on one branch of $W$ (turning points).

## Optional extension

Show that for a time-independent $H$ with $n$ degrees of freedom the equation $H(q,\partial W/\partial q)=E$ has $n-1$ extra separation constants only when separable; and show that a completely integrable system is one for which a separable (or action-angle) structure exists (Module 15).

## Pitfalls

- Confusing the principal function $S$ with the characteristic function $W$.
- Forgetting that $\partial S/\partial q=p$ is multivalued at turning points.
- Believing HJ always separates (it does only in special coordinates).
- Treating the "new momenta" $\alpha_i$ as the energy only (they are $n$ independent constants).

## Gate questions

1. What is $S$ physically, and what is $\partial S/\partial q$?
2. Why does making $K=0$ solve the dynamics completely?
3. In what sense is the HJ equation a wave-front equation?

## One-page cheat sheet contents

The HJ equation and the $K=0$ derivation; $dS/dt=L$; $\partial S/\partial q=p$, $\partial S/\partial t=-H$; characteristic function; oscillator and free-particle solutions; spherical separation.
