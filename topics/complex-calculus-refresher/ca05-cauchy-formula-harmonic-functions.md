# CA05: Cauchy's integral formula, maximum modulus and harmonic functions

**Books:** Ávila Chapter 3, pp. 101 to 117 (exercise sets on pp. 107 and 116; answers on pp. 109 and 117). Churchill Chapter 4. **Time:** 5 sessions (Must: 2, Should: 1, Could: 2). **Tier note:** the Could part (Dirichlet and Neumann, pp. 114 to 117) reads better after EM Modules 04 and 05, as a second proof of uniqueness. Do not do it first.

## Why this matters

Cauchy's formula says the values of an analytic function on a closed contour determine it everywhere inside. Nothing in real analysis behaves like this. The consequences are the whole guide: analytic functions are infinitely differentiable, they equal their Taylor series, and a residue at a simple pole is just Cauchy's formula read backwards. The mean-value property and the maximum modulus principle give "harmonic functions have no interior maxima or minima", which is Earnshaw's theorem for the electrostatic potential in a charge-free region and the mean-value theorem in Jackson's first chapter. The Dirichlet problem, boundary values determining a harmonic function, is the 2D version of what Jackson proves in Chapter 1.

## Skip-test (40 minutes, no notes)

1. State Cauchy's integral formula and its derivative version.
2. Evaluate $\oint_{\lvert z\rvert=2}\frac{e^z}{z-1}\,dz$.
3. State the mean-value property for an analytic function.
4. State the maximum modulus principle.
5. Explain why a harmonic function has no interior maximum.

## Prerequisites

CA04.

## Detailed topics (checklist)

**[Must]** Cauchy's integral formula: $f(z_0)=\frac1{2\pi i}\oint_C\frac{f(z)}{z-z_0}\,dz$ for $z_0$ inside $C$. Derivatives of all orders: $f^{(n)}(z_0)=\frac{n!}{2\pi i}\oint_C\frac{f(z)}{(z-z_0)^{n+1}}\,dz$. Evaluation of contour integrals with one or several singularities by the formula and partial fractions.

**[Must]** Consequence: analytic implies infinitely differentiable (this removes the $C^2$ assumption of CA02).

**[Should]** The Cauchy estimates $\lvert f^{(n)}(z_0)\rvert\le n!M/R^n$ and Liouville's theorem (a bounded entire function is constant). The mean-value property $f(z_0)=\frac1{2\pi}\int_0^{2\pi}f(z_0+re^{i\theta})\,d\theta$. The maximum modulus principle. A harmonic function has no interior extremum.

**[Could]** Harmonic functions and conjugates; a harmonic function determines the analytic function up to a constant; multiply connected regions; the Dirichlet and Neumann problems (Ávila pp. 109 to 117).

## Method cards

**Cauchy's formula as a recipe.** (1) Identify $f(z)$, the part analytic inside, and $z_0$. (2) Check $z_0$ is inside the contour. (3) The integral is $2\pi i\,f(z_0)$. With a higher power $(z-z_0)^{n+1}$ in the denominator, the integral is $2\pi i\,f^{(n)}(z_0)/n!$.

**Several singularities.** Use partial fractions and apply the formula to each term, or deform to small circles.

## Reading plan

| Session | Task |
|---|---|
| A1 | Ávila pp. 101 to 109 (Cauchy's formula, derivatives of all orders). Derive items 1 and 2 |
| B1 | Exercises 1 to 5 and the Ávila set on p. 107 |
| A2 | Ávila pp. 109 to 113 (harmonic functions, maximum modulus principle). Derive items 3 and 4 [Should] |
| A3 | Ávila pp. 114 to 117 (Dirichlet and Neumann), after EM Module 05 [Could] |
| B3 | Exercises 9 and 10 and the Ávila set on p. 116 [Could] |

(Exercises 6 to 8, Should, go with A2.)

## Derive from scratch

1. Cauchy's formula from the master integral: shrink the contour onto a small circle around $z_0$, where $f(z)\approx f(z_0)$.
2. The derivative formula, by differentiating under the integral sign.
3. The mean-value property, from the formula on a circle: $z=z_0+re^{i\theta}$ gives $dz/(z-z_0)=i\,d\theta$.
4. The maximum modulus principle, from the mean-value property.

## Exercises (with expected results)

1. **(Must)** $\oint_{\lvert z\rvert=2}\frac{e^z}{z-1}\,dz$. *Expected:* $2\pi ie\approx17.08\,i$.
2. **(Must)** $\oint_{\lvert z\rvert=2}\frac{\cos z}{z^3}\,dz$. *Expected:* $-\pi i$ (derivative version with $n=2$ and $f''(0)=-1$).
3. **(Must)** $\oint_{\lvert z\rvert=3}\frac{z^2}{(z-1)(z-2)}\,dz$. *Expected:* $6\pi i$. Hint: $\tfrac{z^2}{(z-1)(z-2)}=1+\tfrac4{z-2}-\tfrac1{z-1}$.
4. **(Must)** $\oint_{\lvert z\rvert=1}\frac{\sin z}{z^2}\,dz$. *Expected:* $2\pi i$.
5. **(Must)** Verify the mean-value property for $f=z^2$ on the circle $\lvert z-1\rvert=0.7$. *Expected:* the average is $f(1)=1$.
6. **(Should)** Outline the proof of Liouville's theorem from $\lvert f'(z_0)\rvert\le M/R$. *Expected:* let $R\to\infty$, so $f'\equiv0$.
7. **(Should)** Find the maximum of $\lvert z^2+1\rvert$ on the closed unit disk. *Expected:* $2$, attained at $z=\pm1$ on the boundary (the interior value at $0$ is only $1$).
8. **(Should)** For $f=z^2$, show the level curves of $u=x^2-y^2$ and $v=2xy$ are orthogonal. *Expected:* $\nabla u=(2x,-2y)$ and $\nabla v=(2y,2x)$ give $\nabla u\cdot\nabla v=0$.
9. **(Could)** Show a nonconstant harmonic function has no interior local extremum, and say what this means for the electrostatic potential in a charge-free region. *Expected:* every critical point of $V$ there is a saddle (Earnshaw's theorem: no stable static trap).
10. **(Could)** Solve the Dirichlet problem in the unit disk for the boundary values $\cos\theta$ and $\cos^2\theta$. *Expected:* $u=x$ and $u=\tfrac12+\tfrac12(x^2-y^2)$ (write $\cos^2\theta=\tfrac12+\tfrac12\cos2\theta$).

## Optional extension

Prove the maximum modulus principle for $\lvert f\rvert$ from the mean-value property, and then for $u=\mathrm{Re}\,f$ from the harmonic version. Compare with Jackson's uniqueness proof for the Dirichlet problem.

## Pitfalls

* Applying the formula when $z_0$ lies outside the contour (the integral is then $0$).
* Forgetting the factor $n!$ in the derivative version.
* Taking the maximum modulus of an analytic function over an open set; it is attained on the boundary of a compact region.
* Saying "harmonic implies analytic". The correct statement is that a harmonic function is the real part of an analytic function on a simply connected domain.

## Gate questions

1. Why do the values on the boundary determine $f$ inside?
2. Why is an analytic function automatically infinitely differentiable?
3. Why does the mean-value property forbid interior extrema?

## One-page cheat sheet contents

Cauchy's formula and the derivative version; the recipe; the mean-value property; the maximum modulus principle; the Earnshaw statement.

## Where this is used

CA06 and CA07 (Taylor and Laurent coefficients are Cauchy integrals), EM Module 04 (Earnshaw's theorem, uniqueness), Jackson's mean-value problem in Chapter 1.
