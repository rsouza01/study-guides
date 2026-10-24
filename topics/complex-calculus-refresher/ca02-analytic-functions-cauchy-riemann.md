# CA02: Analytic functions and the Cauchy–Riemann equations

**Books:** Ávila Chapter 2, pp. 34 to 60 (exercise sets on pp. 36, 42, 47, 52, 62; answers and hints on pp. 43, 48, 53, 74). Churchill Chapter 2. **Time:** 4 sessions (Must: 3). **Tier note:** if you can derive the Cauchy–Riemann equations and the conjugate of a harmonic function cold, pass the skip-test and do only exercises 7 and 10.

## Why this matters

Complex differentiability asks for the same limit from every direction in the plane, not just from the left and right. That single demand is much stronger than real differentiability. It forces the Cauchy–Riemann equations, which force $u$ and $v$ to satisfy Laplace's equation. So every analytic function hands you two solutions of $\nabla^2\Phi=0$, and their level curves are orthogonal. That is why complex analysis solves two-dimensional electrostatics, and it is the same orthogonality you checked numerically in your Exercise C1. The geometric reading, a rotation and a scaling by $\lvert f'\rvert$, shows that the Jacobian of an analytic map is $\lvert f'\rvert^2$. That is the Jacobian from your Stewart 15.9 work, now with a name for its value.

## Skip-test (40 minutes, no notes)

1. Define the complex derivative and explain why the limit must not depend on the direction of $h$.
2. Derive the Cauchy–Riemann equations from that requirement.
3. Show $f(z)=\bar z$ is nowhere differentiable.
4. Show $\lvert z\rvert^2$ is differentiable only at $0$, and analytic nowhere.
5. Find the harmonic conjugate of $u=x^3-3xy^2$.
6. State the polar form of the Cauchy–Riemann equations.

## Prerequisites

CA01. Stewart 14.3 (partial derivatives) and 14.5 (the chain rule).

## Detailed topics (checklist)

**[Must]** A function $f:\mathbb{C}\to\mathbb{C}$ as a pair $u(x,y)$, $v(x,y)$; limits and continuity (the same $\epsilon$-$\delta$ as in $\mathbb{R}^2$); the rules for limits.

**[Must]** The derivative $f'(z_0)=\lim_{h\to0}\frac{f(z_0+h)-f(z_0)}{h}$; the rules of differentiation are the real ones.

**[Must]** Cauchy–Riemann: $u_x=v_y$ and $u_y=-v_x$. Necessary for differentiability; sufficient if the partials are continuous. Then $f'=u_x+iv_x$. Polar form: $u_r=\tfrac1rv_\theta$ and $v_r=-\tfrac1ru_\theta$.

**[Must]** Analytic (holomorphic) on an open set. "Analytic at a point" means analytic in a neighbourhood of it, which is why a function can be differentiable at one point and analytic nowhere. An entire function is analytic on all of $\mathbb{C}$.

**[Should]** Geometric reading: $f'(z_0)\ne0$ rotates by $\arg f'$ and scales by $\lvert f'\rvert$, so the map preserves angles (conformal). The Jacobian determinant of $(x,y)\mapsto(u,v)$ is $u_xv_y-u_yv_x=\lvert f'\rvert^2$.

**[Should]** Harmonic functions: $\nabla^2u=\nabla^2v=0$. For now assume $u,v$ have continuous second partials. CA05 proves that analytic functions are infinitely differentiable, which removes the assumption.

**[Could]** The Wirtinger form: $f$ is analytic exactly when $\partial f/\partial\bar z=0$, i.e. $f$ does not depend on $\bar z$.

## Method cards

**The Cauchy–Riemann test.** (1) Write $f=u+iv$ with $u,v$ in $x,y$. (2) Compute $u_x,u_y,v_x,v_y$. (3) Check $u_x=v_y$ and $u_y=-v_x$. (4) Check the partials are continuous (then CR is sufficient). (5) State where CR holds; the set must be open for "analytic".

**Harmonic conjugate.** (1) Check $\nabla^2u=0$. (2) Integrate $v_y=u_x$ with respect to $y$, adding an unknown function $g(x)$. (3) Fix $g$ from $v_x=-u_y$. (4) Check the result is analytic: it should be a polynomial or exponential in $z$.

## Reading plan

| Session | Task |
|---|---|
| A1 | Ávila pp. 34 to 49 (functions, limits, continuity). Skim the limit properties |
| B1 | Exercises 1 to 3 and the Ávila sets on pp. 36 and 42 |
| A2 | Ávila pp. 49 to 57 (analytic function, differentiation rules, Cauchy–Riemann). Derive item 1 below |
| B2 | Exercises 4 to 6 and the Ávila sets on pp. 47 and 52 |
| A3 | Ávila pp. 57 to 60 (polar CR, geometric interpretation). Derive items 2 and 3 |
| B3 | Exercises 7 to 10, the Ávila set on p. 62, and the cheat sheet |

## Derive from scratch

1. The Cauchy–Riemann equations from the direction-independence of the limit (approach along the real axis, then the imaginary axis).
2. $\nabla^2u=0$ from CR.
3. $\det\partial(u,v)/\partial(x,y)=\lvert f'\rvert^2$.

## Exercises (with expected results)

1. **(Must)** Show $f(z)=\bar z$ is nowhere complex-differentiable. *Expected:* $u=x$, $v=-y$ gives $u_x=1\ne v_y=-1$.
2. **(Must)** Show $f(z)=\lvert z\rvert^2$ is differentiable only at $z=0$, with $f'(0)=0$, and analytic nowhere. *Expected:* CR requires $2x=0$ and $2y=0$.
3. **(Must)** Check that $z^2$ satisfies CR and that $u_x$ equals $\mathrm{Re}\,f'$. *Expected:* $u=x^2-y^2$, $v=2xy$, $f'=2z$.
4. **(Must)** Find a harmonic conjugate of $u=x^3-3xy^2$. *Expected:* $v=3x^2y-y^3+C$ (so $f=z^3$).
5. **(Must)** Show $u=e^x\cos y$ is harmonic and find its conjugate. *Expected:* $v=e^x\sin y$ (so $f=e^z$).
6. **(Should)** Verify the polar CR equations for $z^2=r^2e^{2i\theta}$. *Expected:* $u_r=2r\cos2\theta=v_\theta/r$.
7. **(Should)** Show the Jacobian of an analytic map is $\lvert f'\rvert^2$, and check it for $f=z^3$ at $z=1+i$. *Expected:* $36$ (since $f'=3z^2=6i$ there).
8. **(Should)** Show that an analytic $f$ with constant $\lvert f\rvert$ is constant. *Expected:* differentiate $u^2+v^2=c$ and combine with CR.
9. **(Could)** Where is $f(z)=x^2+iy^2$ differentiable? *Expected:* only on the line $y=x$, where $f'=2x$; analytic nowhere.
10. **(Could)** Show that if $f$ and $\bar f$ are both analytic on a domain, $f$ is constant. *Expected:* the two sets of CR equations force all four partials to vanish.

## Optional extension

Show that the level curves of $u$ and $v$ are orthogonal wherever $f'\ne0$ (use $\nabla u\cdot\nabla v=0$). For $f=z^2$ this is $\nabla u=(2x,-2y)$ and $\nabla v=(2y,2x)$.

## Pitfalls

* Checking CR at one point and calling the function analytic.
* Forgetting that "analytic" needs a neighbourhood, so isolated points of differentiability do not count.
* Mixing $u_y=-v_x$ with $u_y=v_x$.
* Using polar CR without the factor $1/r$.

## Gate questions

1. Why is complex differentiability much stronger than real differentiability?
2. Why does CR force $u$ and $v$ to be harmonic?
3. Why is the Jacobian of an analytic map $\lvert f'\rvert^2$ and not an arbitrary determinant?

## One-page cheat sheet contents

CR (Cartesian and polar); $f'=u_x+iv_x$; the conjugate recipe; the Jacobian identity; the list of non-analytic examples ($\bar z$, $\lvert z\rvert^2$, $\mathrm{Re}\,z$).

## Where this is used

CA04 (Cauchy's theorem uses CR), CA05 (harmonic functions), EM Modules 04 and 05 (uniqueness and Laplace's equation), conformal electrostatics (appendix).
