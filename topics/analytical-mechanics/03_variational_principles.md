# Module 03: Variational principles and Hamilton's principle

**Books:** Goldstein 2.1 to 2.5; Landau and Lifshitz *Mechanics* sections 2 to 3 (optional second view); Hand and Finch (calculus of variations chapter) for extra examples.
**Time:** 2 weeks (four sessions).

## Why this matters for the bridge

Hamilton's principle $\delta S=0$ is the foundation that **survives** into field theory and quantum mechanics: the action $S$ becomes the phase of the wavefunction (Modules 14 and 16) and the generating functional of the path integral. The single most important habit to build here is **tracking boundary terms**: the term you drop in deriving the Euler-Lagrange equations is the same term that reappears as $p\,\delta q$ at the endpoints (giving $\partial S/\partial q=p$ in Hamilton-Jacobi theory), as the surface term at infinity in field theory, and as the term that Noether's theorem keeps.

## Skip-test (40 minutes, no notes)

1. Derive the Euler equation $\frac{\partial f}{\partial y}-\frac{d}{dx}\frac{\partial f}{\partial y'}=0$ for $\delta\int f(y,y',x)dx=0$ with fixed endpoints.
2. State Hamilton's principle and derive Lagrange's equations from it.
3. Derive the Beltrami identity ($f-y'\partial f/\partial y'=$ const when $f$ has no explicit $x$) and use it to solve the brachistochrone: $x=a(\theta-\sin\theta)$, $y=a(1-\cos\theta)$.
4. Explain how a holonomic constraint is imposed with a Lagrange multiplier $\lambda(t)$ and what $\lambda$ means physically.
5. State precisely which boundary term was dropped in item 1 and under what condition it vanishes.

## Prerequisites

Modules 01 and 02.

## Detailed topics (checklist)

**Calculus of variations (2.2) [Must]**
- Functionals, the first variation $\delta S=\epsilon\frac{dS}{d\epsilon}\big|_0$, the fundamental lemma; the Euler equation; several dependent variables; the Beltrami identity; first integrals when $f$ is independent of $y$ or $x$.
- Classic problems: shortest path, brachistochrone (cycloid), minimal surface of revolution (catenary $y=a\cosh\frac{x-x_0}{a}$), geodesics, Fermat's principle (Snell's law).
- Constraints: isoperimetric problems with constant multipliers; holonomic constraints with function multipliers.

**Hamilton's principle (2.1, 2.3) [Must]**
- $S=\int_{t_1}^{t_2}L\,dt$ with fixed endpoints $\delta q(t_1)=\delta q(t_2)=0$; derivation of Lagrange's equations; the statement that Hamilton's principle holds for any $L$ whose Euler-Lagrange equations are the equations of motion (not only $T-V$).
- Stationary versus minimum: the action is a minimum only for short times (conjugate points); the principle is "stationary action".

**Constraints (2.4) [Should]**
- Lagrange multipliers for holonomic constraints $f_\alpha(q,t)=0$: $\frac{d}{dt}\frac{\partial L}{\partial\dot q_j}-\frac{\partial L}{\partial q_j}=\sum_\alpha\lambda_\alpha\frac{\partial f_\alpha}{\partial q_j}$; the multipliers are the generalized constraint forces.
- Semi-holonomic constraints linear in velocities; why Hamilton's principle does not give correct equations for general nonholonomic constraints (awareness).

**Advantages of a variational formulation (2.5) [Should]**
- Coordinate independence; the Lagrangian of a system as the sum of the Lagrangians of its parts; applicability beyond mechanics (EM, fields, optics, quantum).

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Goldstein 2.1 to 2.2; derive the Euler equation closed-book, naming the boundary term |
| B1 | Exercises 1 to 4 |
| A2 | Goldstein 2.3 to 2.4; derive Lagrange's equations from Hamilton's principle |
| B2 | Exercises 5 to 10; Goldstein 2.5 (read); cheat sheet |

## Derive from scratch (A sessions, book closed)

1. The Euler equation, being explicit about the integration by parts and the boundary term $\left[\frac{\partial f}{\partial y'}\delta y\right]_{x_1}^{x_2}$.
2. Lagrange's equations from Hamilton's principle.
3. The brachistochrone solution (cycloid) using the Beltrami identity.
4. The multiplier form of Lagrange's equations for a holonomic constraint.
5. Snell's law from Fermat's principle.

## Bare-minimum exercises (with expected results)

1. **Shortest path:** show the shortest path between two points in a plane is a straight line (Euler equation for $f=\sqrt{1+y'^2}$ gives $y''=0$).
2. **Brachistochrone:** from $(0,0)$ downward to $(x_1,y_1)$ the curve is a cycloid $x=a(\theta-\sin\theta)$, $y=a(1-\cos\theta)$ (with $y$ measured downward); the travel time to parameter $\theta_1$ is $t=\theta_1\sqrt{a/g}$.
3. **Soap film:** minimize the area of a surface of revolution between two rings; the profile is a catenary $y=a\cosh\frac{x-x_0}{a}$; note that for rings too far apart no solution exists (the film breaks).
4. **Isoperimetric:** among closed curves of fixed length the circle maximizes the area (use a constant multiplier).
5. **Snell's law:** minimize $\int n(y)\,ds$ for an interface between media of indices $n_1,n_2$ and obtain $n_1\sin\theta_1=n_2\sin\theta_2$.
6. **Classical action of the free particle:** from Hamilton's principle the path is a straight line with constant velocity and $S=\frac{m(x_b-x_a)^2}{2(t_b-t_a)}$.
7. **Classical action of the harmonic oscillator:** the path $x(t)=\frac{x_a\sin\omega(t_b-t)+x_b\sin\omega(t-t_a)}{\sin\omega T}$ gives $S=\frac{m\omega}{2\sin\omega T}\left[(x_a^2+x_b^2)\cos\omega T-2x_ax_b\right]$, $T=t_b-t_a$. *Keep this result: it is the exponent of the oscillator propagator in Module 16.*
8. **Boundary term:** if the endpoint is *not* held fixed, show $\delta S=\left[p\,\delta q\right]_{t_1}^{t_2}$ on solutions of the equations of motion. Note this is the origin of $\partial S/\partial q_b=p_b$ and $\partial S/\partial t_b=-H$.
9. **Total derivative:** show that $L\to L+\frac{d}{dt}F(q,t)$ changes $S$ by $F(q_2,t_2)-F(q_1,t_1)$, so the equations of motion are unchanged.
10. **Constraint force:** for the bead on the rotating hoop of Module 02, write the constraint $r=R$ in polar coordinates, use a multiplier $\lambda$ and show that $\lambda$ equals the radial constraint force; compare with the Newtonian normal force.

## Optional extension

Show that for a free particle and for the harmonic oscillator the stationary path is a minimum of the action for $T<\pi/\omega$ and ceases to be one for $T>\pi/\omega$ (conjugate point); this is the first appearance of the Maslov index that returns in Module 15.

## Pitfalls

- Applying Hamilton's principle with free endpoints without the extra boundary term.
- Treating the multiplier as a number rather than a function of time for holonomic constraints.
- Believing the action is always a minimum.
- Using Hamilton's principle for nonholonomic constraints without checking that it gives the right equations.

## Gate questions

1. Which boundary term is dropped in the derivation of the Euler-Lagrange equations, and what physical assumption justifies dropping it?
2. Why is the action only stationary, not minimal?
3. What does the Lagrange multiplier represent?

## One-page cheat sheet contents

Euler equation and Beltrami identity; brachistochrone and catenary solutions; multiplier form of Lagrange's equations; free-particle and oscillator actions; the boundary-term formula $\delta S=[p\delta q]$.
