# Module 07: The Hamiltonian formulation

**Books:** Goldstein 8.1, 8.2, 8.5, 8.6 (8.3 Routh's procedure: light; 8.4 relativistic Hamiltonian: light, revisit in Module 13); Landau and Lifshitz *Mechanics* sections 40 to 44 (optional); José and Saletan chapter 3 (phase space, optional).
**Time:** 2 weeks (four sessions).

## Why this matters for the bridge

The Legendre transformation is not a formal trick: it changes *which variables are independent*, from $(q,\dot q)$ to $(q,p)$, and phase space has a structure (the symplectic form) that configuration-velocity space does not. Everything in Chapters 9 and 10 lives on that structure. Section 8.5 gives the **modified Hamilton's principle** $\delta\int(p\dot q-H)dt=0$ with $q$ and $p$ varied *independently*, which is exactly the structure of the phase-space path integral. And the object $\oint p\,dq$ of Section 8.6 reappears as the action variable (Module 15) and the WKB phase (Module 16): same integral, three appearances. The Legendre transformation is also the same operation as $U\to F\to G$ in thermodynamics, which you already know well.

## Skip-test (40 minutes, no notes)

1. Define $p_j=\partial L/\partial\dot q_j$, $H=\sum p_j\dot q_j-L$, and derive Hamilton's equations $\dot q_j=\partial H/\partial p_j$, $\dot p_j=-\partial H/\partial q_j$, $\frac{\partial H}{\partial t}=-\frac{\partial L}{\partial t}$.
2. Construct $H$ for a charged particle in an EM field and show $H=\frac{(\mathbf p-q\mathbf A)^2}{2m}+q\Phi$.
3. Give an example where $H\ne E=T+V$ (and $H$ is conserved).
4. Derive Hamilton's equations from $\delta\int(\sum p\dot q-H)dt=0$ with $\delta q$ and $\delta p$ independent.
5. State Maupertuis' principle and evaluate $\oint p\,dq$ for the harmonic oscillator.

## Prerequisites

Modules 02, 03, 04.

## Detailed topics (checklist)

**Legendre transformation and Hamilton's equations (8.1) [Must]**
- Legendre transformation of a convex function; invertibility of $p(\dot q)$ requires $\det\frac{\partial^2L}{\partial\dot q_i\partial\dot q_j}\ne0$; the Hamilton function $H(q,p,t)$; $2n$ first-order equations; examples (particle in a potential, in an EM field, bead on a rotating hoop, relativistic particle).
- Phase space $(q,p)$; phase portraits (oscillator ellipses, pendulum separatrix); the relation $H=E$ only when $T$ is quadratic in velocities, $V$ is velocity-independent and the coordinate transformation is time-independent.

**Cyclic coordinates and Routh (8.2, 8.3) [Should]**
- A cyclic coordinate means conserved $p_j$ and reduction of the problem; Routh's procedure mixes Lagrangian and Hamiltonian treatment (use for the central force); oscillations about steady motion (light).

**The relativistic Hamiltonian (8.4) [Could, revisit in Module 13]**
- $H=\sqrt{p^2c^2+m^2c^4}+q\Phi$ with $p\to p-q\mathbf A$.

**Modified Hamilton's principle (8.5) [Must]**
- $\delta\int(\sum p_j\dot q_j-H)dt=0$ with *independent* variations of $q_j$ and $p_j$ and fixed $q$ at the endpoints; the $p$-variation gives $\dot q=\partial H/\partial p$ and the $q$-variation gives $\dot p=-\partial H/\partial q$; the integrand $p\dot q-H$ is the Lagrangian on phase space.

**Principle of least action (8.6) [Must]**
- Maupertuis' abbreviated action $S_0=\int\sum p_j\,dq_j$ at fixed energy; $\delta S_0=0$ determines the *shape* of the path; for a particle $S_0=\int\sqrt{2m(E-V)}\,ds$ (Jacobi's form: geodesics of a metric); the analogy with Fermat's principle with $n\leftrightarrow\sqrt{2m(E-V)}$.
- **Keep two numbers:** $\oint p\,dq$ for the harmonic oscillator ($2\pi E/\omega$) and for a particle in a box ($2L\sqrt{2mE}$); they return in Module 15.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Goldstein 8.1; derive Hamilton's equations closed-book; revisit Thermodynamics Module 03 for the same Legendre structure |
| B1 | Exercises 1 to 5 |
| A2 | Goldstein 8.2, 8.5, 8.6; derive Hamilton's equations from the modified principle |
| B2 | Exercises 6 to 10; cheat sheet |

## Derive from scratch (A sessions, book closed)

1. Hamilton's equations from the Legendre transformation of $L$, including $\partial H/\partial t=-\partial L/\partial t$.
2. $H$ for a charged particle in an EM field.
3. Hamilton's equations from the modified Hamilton's principle with independent $q,p$.
4. $H$ for a bead on a rotating hoop and why it is not $T+V$.
5. Maupertuis' principle from Hamilton's principle at fixed energy.

## Bare-minimum exercises (with expected results)

1. **EM field:** from $L=\frac12m\dot{\mathbf r}^2-q\Phi+q\dot{\mathbf r}\cdot\mathbf A$ obtain $H=\frac{(\mathbf p-q\mathbf A)^2}{2m}+q\Phi$ (SI; replace $q\mathbf A\to\frac qc\mathbf A$ in Gaussian units), and verify that Hamilton's equations reproduce the Lorentz force.
2. **Bead on a rotating hoop:** $H=\frac{p_\theta^2}{2mR^2}-\frac12mR^2\Omega^2\sin^2\theta-mgR\cos\theta$; show $H\ne E$ and $H$ is conserved.
3. **Relativistic free particle:** $L=-mc^2\sqrt{1-v^2/c^2}$ gives $p=\gamma mv$, $H=\sqrt{p^2c^2+m^2c^4}$, $v=\partial H/\partial p=\frac{pc^2}{H}$; nonrelativistic expansion $H\approx mc^2+\frac{p^2}{2m}-\frac{p^4}{8m^3c^2}$.
4. **Pendulum phase portrait:** $H=\frac{p^2}{2m\ell^2}-mg\ell\cos\theta$; the separatrix at $H=mg\ell$ (the maximum of the potential); the period of small oscillations $2\pi\sqrt{\ell/g}$ and its divergence at the separatrix; sketch libration and rotation regions.
5. **Kepler in Hamiltonian form:** in polar coordinates $H=\frac{p_r^2}{2\mu}+\frac{p_\phi^2}{2\mu r^2}-\frac kr$; $p_\phi$ is conserved; reduce to the radial effective problem.
6. **Oscillator action integral:** for $H=\frac{p^2}{2m}+\frac12m\omega^2q^2$ the phase-space curve at energy $E$ is an ellipse with semi-axes $\sqrt{2E/m\omega^2}$ and $\sqrt{2mE}$; $\oint p\,dq=\frac{2\pi E}{\omega}$.
7. **Particle in a box:** $\oint p\,dq=2L\sqrt{2mE}$ (go there and back with $p=\pm\sqrt{2mE}$).
8. **Modified Hamilton's principle:** derive Hamilton's equations by varying $q$ and $p$ independently, writing out the boundary term $[p\,\delta q]$ explicitly.
9. **Maupertuis:** for a free particle show $\delta\int p\,dq=0$ at fixed $E$ gives straight lines; for a uniform field $V=-Fx$ show the path is the parabola of projectile motion.
10. **Routh:** for the central force reduce the problem by eliminating the cyclic $\phi$ with Routh's function $R=L-p_\phi\dot\phi$ and obtain the radial equation with $\frac{p_\phi^2}{2\mu r^2}$.

## Optional extension

Show that the Legendre transformation $L\to H$ is an involution (transforming $H$ back gives $L$), and compare with $U\leftrightarrow S$ in thermodynamics: the equality of mixed second derivatives of $H$ plays the role of the Maxwell relations.

## Pitfalls

- Treating $p$ as $m\dot q$ in the presence of a magnetic field.
- Forgetting that $H$ must be written as a function of $(q,p)$, not $(q,\dot q)$, before differentiating.
- Using $H=T+V$ with a time-dependent coordinate transformation.
- Varying $p$ and $q$ with the endpoint condition on $p$ (only $\delta q$ vanishes at the endpoints).

## Gate questions

1. What additional structure does phase space carry that velocity space does not?
2. Why can $q$ and $p$ be varied independently in the modified principle?
3. When does $H$ equal the energy, and when is it conserved?

## One-page cheat sheet contents

Legendre transformation; Hamilton's equations and $\partial H/\partial t$; $H$ for EM and relativistic cases; modified Hamilton's principle; Maupertuis; $\oint p\,dq$ for the oscillator and the box.
