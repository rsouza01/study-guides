# Module 02: Lagrangian mechanics and constraints

**Books:** Goldstein Chapter 1 (1.1 to 1.6); Taylor *Classical Mechanics* (Lagrangian chapters) as an optional second view; Hand and Finch for extra worked examples.
**Time:** 2 weeks (four sessions). Review at speed; the new content is the logical status of the principles and the velocity-dependent potential.

## Why this matters for the bridge

Goldstein derives Lagrange's equations in Chapter 1 from **D'Alembert's principle**, that is, from Newton. Chapter 2 re-derives them from a **variational principle**. These are two independent foundations that give the same equations; only the second generalizes to fields and to quantum mechanics. Hold that thought through this module. The second thing worth slowing for is the **velocity-dependent potential** for a charge in an electromagnetic field: it is the origin of minimal coupling and of the fact that the canonical momentum is $m\mathbf v+q\mathbf A$, not $m\mathbf v$.

## Skip-test (40 minutes, no notes)

1. For $N$ particles with $k$ holonomic constraints, state the number of degrees of freedom and give a bead-on-a-rotating-hoop example.
2. State D'Alembert's principle and derive Lagrange's equations $\frac{d}{dt}\frac{\partial T}{\partial\dot q_j}-\frac{\partial T}{\partial q_j}=Q_j$.
3. For $L=\frac12mv^2-q\Phi+q\mathbf A\cdot\mathbf v$ derive the Lorentz force $m\ddot{\mathbf r}=q(\mathbf E+\mathbf v\times\mathbf B)$ and give the canonical momentum.
4. Write the Lagrangian of a double pendulum and obtain its equations of motion.
5. Define the Rayleigh dissipation function and show it gives $m\ddot x+b\dot x+kx=0$.

## Prerequisites

Module 01.

## Detailed topics (checklist)

**Constraints and generalized coordinates (Goldstein 1.3) [Must]**
- Holonomic (integrable) versus nonholonomic constraints; scleronomic and rheonomic; generalized coordinates $q_j$ and the transformation $\mathbf r_i=\mathbf r_i(q_1,\dots,q_n,t)$; virtual displacements.
- Constraint forces do no virtual work (for smooth constraints).

**D'Alembert and Lagrange (1.4) [Must]**
- D'Alembert's principle $\sum_i(\mathbf F_i^{(a)}-\dot{\mathbf p}_i)\cdot\delta\mathbf r_i=0$; Lagrange's equations; the identities $\frac{\partial\dot{\mathbf r}_i}{\partial\dot q_j}=\frac{\partial\mathbf r_i}{\partial q_j}$ and $\frac{d}{dt}\frac{\partial\mathbf r_i}{\partial q_j}=\frac{\partial\dot{\mathbf r}_i}{\partial q_j}$ (the technical heart); for conservative forces $L=T-V$.
- **Non-uniqueness:** $L\to L+\frac{dF(q,t)}{dt}$ leaves the equations unchanged.

**Velocity-dependent potentials and dissipation (1.5) [Must]**
- Generalized potential $U(q,\dot q,t)$ with $Q_j=-\frac{\partial U}{\partial q_j}+\frac{d}{dt}\frac{\partial U}{\partial\dot q_j}$; the electromagnetic case $U=q\Phi-q\mathbf A\cdot\mathbf v$ (SI) or $q\Phi-\frac qc\mathbf A\cdot\mathbf v$ (Gaussian); **canonical momentum** $\mathbf p=m\mathbf v+q\mathbf A$ (SI), its gauge dependence, and why $m\mathbf v$ is the gauge-invariant *kinetic* momentum.
- Rayleigh dissipation function $\mathcal F=\frac12\sum b\,\dot q^2$ and the modified Lagrange equation $\frac{d}{dt}\frac{\partial L}{\partial\dot q}-\frac{\partial L}{\partial q}=-\frac{\partial\mathcal F}{\partial\dot q}$.

**Simple applications (1.6) [Should]**
- Atwood machine, bead on a rotating wire, double and spherical pendulum, particle on a cone, charged particle in uniform fields; how to choose coordinates so that cyclic coordinates appear.

**Nonholonomic constraints [Could, revisit in Module 03]**
- Rolling constraints; why Lagrange's equations cannot be used directly; the multiplier method (Module 03).

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Goldstein 1.3 to 1.4 (move fast); derive Lagrange's equations from D'Alembert closed-book |
| B1 | Exercises 1 to 4 |
| A2 | Goldstein 1.5 (slow), the Lorentz-force derivation; derive the dissipation-function equation |
| B2 | Exercises 5 to 10; cheat sheet |

## Derive from scratch (A sessions, book closed)

1. Lagrange's equations from D'Alembert's principle, including the two kinematic identities.
2. The Lorentz force from $L=\frac12mv^2-q\Phi+q\mathbf A\cdot\mathbf v$.
3. The canonical momentum and its transformation under $\mathbf A\to\mathbf A+\nabla\Lambda$.
4. The invariance of the equations under $L\to L+dF/dt$.
5. The Rayleigh function equation for a damped oscillator.

## Bare-minimum exercises (with expected results)

1. **Atwood machine:** $L=\frac12(m_1+m_2)\dot x^2+(m_1-m_2)gx$; acceleration $a=g\frac{m_1-m_2}{m_1+m_2}$.
2. **Bead on a rotating hoop** (angular velocity $\Omega$, radius $R$, $\theta$ from the downward vertical): $L=\frac12mR^2(\dot\theta^2+\Omega^2\sin^2\theta)+mgR\cos\theta$. The bottom ($\theta=0$) is stable for $\Omega^2<g/R$; for $\Omega^2>g/R$ it is unstable and the stable equilibria are $\cos\theta_0=\frac{g}{R\Omega^2}$. Small-oscillation frequency about the new equilibria: $\omega^2=\Omega^2\sin^2\theta_0$.
3. **Double pendulum** (equal masses $m$ and lengths $\ell$): obtain the two coupled equations and show that for small angles the normal-mode frequencies are $\omega^2=(2\pm\sqrt2)\,g/\ell$.
4. **Spherical pendulum:** show $p_\phi$ is conserved and the effective one-dimensional problem in $\theta$; find the condition for circular (conical) motion at fixed $\theta_0$: $\dot\phi^2=\frac{g}{\ell\cos\theta_0}$ (for $\theta$ measured from the downward vertical).
5. **Lorentz force:** derive $m\ddot{\mathbf r}=q(\mathbf E+\mathbf v\times\mathbf B)$ from the generalized potential; note $\mathbf p=m\mathbf v+q\mathbf A$.
6. **Uniform magnetic field, two gauges:** with $\mathbf B=B\hat z$ use $\mathbf A=(-By,0,0)$ and $\mathbf A=\frac B2(-y,x,0)$; show the equations of motion are the same (cyclotron frequency $\omega_c=qB/m$) but the canonical momenta differ; identify which momenta are conserved in each gauge.
7. **Dissipation:** with $\mathcal F=\frac12b\dot x^2$ obtain $m\ddot x+b\dot x+kx=0$ and the Q factor $Q=\sqrt{km}/b$.
8. **Gauge freedom in $L$:** show $L'=L+\frac{d}{dt}(\alpha qx)$ gives the same equations and changes $p$ by $\alpha q$; interpret in terms of the gauge ambiguity of $\mathbf A$.
9. **Counting:** a rigid rod of fixed length in a plane has how many degrees of freedom (3: position of one end and orientation)? Two particles on a sphere (4)? A particle sliding on a surface that moves in time: write $\mathbf r(q_1,q_2,t)$ and note which constraint is rheonomic.
10. **Constraint force check:** for the bead on a hoop, compute the normal force on the bead using Newton's laws and compare with the Lagrange multiplier result of Module 03.

## Optional extension

Derive the Lagrange equations for a system whose constraints are *nonholonomic but linear in velocities* ($\sum_ja_{lj}\dot q_j+a_{lt}=0$) by the multiplier method (a preview of Goldstein 2.4), and discuss a rolling disk.

## Pitfalls

- Treating $\mathbf p=m\mathbf v$ for a charged particle in a magnetic field.
- Forgetting that the kinematic identity $\frac{\partial\dot{\mathbf r}}{\partial\dot q}=\frac{\partial\mathbf r}{\partial q}$ requires $\mathbf r=\mathbf r(q,t)$ to be velocity-independent.
- Using Lagrange's equations with a frictional force that is not derivable from a Rayleigh function without adding it to the right-hand side.

## Gate questions

1. What are the two independent foundations of Lagrange's equations, and which one generalizes to fields and quantum mechanics?
2. Why is the canonical momentum gauge-dependent while the kinetic momentum is not?
3. Is $L=T-V$ unique? What freedom is there?

## One-page cheat sheet contents

D'Alembert and Lagrange equations; the two kinematic identities; $L$ for a charge in an EM field and the canonical momentum; Rayleigh function; non-uniqueness of $L$.
