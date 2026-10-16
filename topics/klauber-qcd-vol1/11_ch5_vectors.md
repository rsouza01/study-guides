# Module 11: Chapter 5, Vectors (Weeks 15 and 16; Protocol A shading into B)

**Books:** Klauber Ch. 5; second sources: Tong's gauge-field lecture, Schwartz chapter 8, Lancaster and Blundell. If you ran the electrodynamics guide, its Module 17 (Proca) is a rehearsal.
**Time:** 2 weeks.

## Why this matters

Week 15: massive vector fields, the Proca case, degree-of-freedom counting. Week 16: the massless case, gauge freedom, gauge fixing, the photon propagator. The structure here (constraints, gauge freedom, a propagator that is not simply $\frac{1}{k^2}$) is what makes QED different from the scalar and spinor cases.

## Diagnostic (40 minutes, no notes)

1. Derive the Proca equation from $\mathcal L=-\tfrac14F_{\mu\nu}F^{\mu\nu}+\tfrac12m^2A_\mu A^\mu$ and show $\partial_\mu A^\mu=0$ follows for $m\ne0$.
2. Count the degrees of freedom of a massive and a massless vector field.
3. Show the Maxwell Lagrangian is gauge invariant and the mass term breaks gauge invariance.
4. Write the photon propagator in Feynman gauge and the Proca propagator.
5. State the polarisation sum for a massive and a massless vector.

## Prerequisites

Modules 06 to 10.

## Detailed topics (checklist)

**Week 15: the Proca case [Must]**
- $\mathcal L=-\tfrac14F_{\mu\nu}F^{\mu\nu}+\tfrac12m^2A_\mu A^\mu$, $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$; equation $\partial_\mu F^{\mu\nu}+m^2A^\nu=0$; taking $\partial_\nu$ gives $m^2\partial_\nu A^\nu=0$, so $\partial\cdot A=0$ and $(\Box+m^2)A^\nu=0$; the constraint removes the redundant component: **3 degrees of freedom**; polarisation vectors $\epsilon^\mu(k,\lambda)$ with $k\cdot\epsilon=0$, $\lambda=1,2,3$; $\sum_\lambda\epsilon_\mu\epsilon^*_\nu=-g_{\mu\nu}+\frac{k_\mu k_\nu}{m^2}$; propagator $\frac{-i\left(g_{\mu\nu}-k_\mu k_\nu/m^2\right)}{k^2-m^2+i\epsilon}$.

**Week 16: the massless case, gauge freedom [Must]**
- $m=0$: gauge invariance $A_\mu\to A_\mu+\partial_\mu\lambda$; the field equation $\Box A^\nu-\partial^\nu(\partial\cdot A)=0$ cannot determine $A^\nu$ uniquely; **gauge fixing**: Lorenz gauge $\partial\cdot A=0$ with residual gauge freedom $\Box\lambda=0$, Coulomb gauge; $4-1-1=2$ physical polarisations; canonical quantisation obstacles ($\pi^0=0$) and the Gupta-Bleuler or Fermi approach (orientation); Feynman-gauge photon propagator $\frac{-ig_{\mu\nu}}{k^2+i\epsilon}$.
- *Counterfactuals:* why is gauge freedom not removable by better bookkeeping? What is physically different between massive and massless beyond the mass term?

## Reading plan

| Week | Task |
| --- | --- |
| 15 | Proca; counting; exercises 1 to 4 |
| 16 | The massless case and gauge fixing; exercises 5 to 10 |

## Derive from scratch

1. The Proca equation and the constraint $\partial\cdot A=0$.
2. The degrees-of-freedom count.
3. The polarisation sum for a massive vector.
4. Gauge invariance of $F_{\mu\nu}F^{\mu\nu}$.
5. The photon propagator as the inverse of the gauge-fixed operator.

## Exercises

1. **[T] Proca equation and constraint:** vary $A_\nu$ to get $\partial_\mu F^{\mu\nu}+m^2A^\nu=0$; take $\partial_\nu$: $m^2\partial_\nu A^\nu=0$; then $(\Box+m^2)A^\nu=0$.
2. **[T] Polarisations:** for $k=(E,0,0,k_z)$ massive: $\epsilon_{1,2}=(0,1,0,0),(0,0,1,0)$ (transverse) and $\epsilon_3=\frac{1}{m}(k_z,0,0,E)$ (longitudinal), with $k\cdot\epsilon_3=0$ and $\epsilon_3\cdot\epsilon_3=-1$.
3. **[T] Polarisation sum:** $\sum_{\lambda=1}^3\epsilon_\mu\epsilon_\nu^*=-g_{\mu\nu}+\frac{k_\mu k_\nu}{m^2}$; verify the trace $=-4+1=-3$.
4. **[T] Degrees of freedom:** a massive vector has $4-1=3$ polarisations; its rest-frame states form a spin-1 triplet.
5. **[T] Gauge invariance:** $F_{\mu\nu}\to F_{\mu\nu}$ under $A\to A+\partial\lambda$, so $\mathcal L_{\rm Maxwell}$ is invariant; $\frac12m^2A^2\to\frac12m^2(A+\partial\lambda)^2$ is not.
6. **[T] Lorenz gauge:** $\partial\cdot A=0$ is reachable if $\Box\lambda=-\partial\cdot A$; the residual freedom $\Box\lambda=0$ removes one more polarisation: $4-1-1=2$.
7. **[T] Photon propagator:** add $-\frac1{2\xi}(\partial\cdot A)^2$ to $\mathcal L$: the operator is $\left[g_{\mu\nu}k^2-(1-\tfrac1\xi)k_\mu k_\nu\right]$ whose inverse is $\frac{-i}{k^2}\left[g_{\mu\nu}-(1-\xi)\frac{k_\mu k_\nu}{k^2}\right]$; Feynman gauge $\xi=1$: $\frac{-ig_{\mu\nu}}{k^2+i\epsilon}$.
8. **[T] Massless limit:** the Proca propagator's $\frac{k_\mu k_\nu}{m^2}$ term diverges as $m\to0$ but drops out of amplitudes with conserved currents ($k_\mu J^\mu=0$).
9. **[C] Gauge freedom:** is gauge invariance a symmetry of nature or a property of our description? State Klauber's position, then the strongest objection to it.
10. **[C] Massive versus massless:** what is physically different between the massive and massless vector beyond the mass term (degrees of freedom, longitudinal mode, conserved-current coupling)?

## Optional extension

Show that in Coulomb gauge ($\nabla\cdot\mathbf A=0$) the instantaneous Coulomb interaction and two transverse photons carry all the physics, and that Lorentz covariance is hidden but not lost.

## Pitfalls

- Treating $A^0$ as an independent dynamical variable in the massless case.
- Using the massive polarisation sum for massless photons without the Ward identity.
- Forgetting the gauge-fixing term when inverting the quadratic operator.

## Gate questions

1. Why does Proca have three degrees of freedom and Maxwell two?
2. Why can the massless photon propagator not be defined without gauge fixing?
3. Why does the $k_\mu k_\nu/m^2$ term not spoil the massless limit?

## One-page cheat sheet contents

Proca equation and constraint; polarisation sums; gauge invariance and fixing; propagators.
