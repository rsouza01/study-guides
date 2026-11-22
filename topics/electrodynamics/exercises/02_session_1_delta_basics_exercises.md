# Module 02, Session 1: delta function basics, exercises

Self-check for Session 1. Books, notes and your cheat sheet are all fair game, and there is no clock.

**Read first:** Griffiths §1.5.1 to §1.5.3 (pp. 43 to 50). The study file is `02_math_patch_deltas_contours_fourier.md`.

**Notation:** $`\delta(x)`$ is the one-dimensional delta; $`\delta^3(\mathbf r)=\delta(x)\delta(y)\delta(z)`$ is the three-dimensional one. $`\theta(x)`$ is the step function (1 for $`x>0`$, 0 for $`x<0`$).

## Book problems

Tiers: Must, do all; Should, when time allows; Could, only if the module is going well.

| Tier | Problem | What it asks |
| --- | --- | --- |
| Must | Griffiths 1.44 | delta-function integrals (sifting property) |
| Must | Griffiths 1.45 | delta-function integrals with $`\delta(3x)`$ and compositions |
| Must | Griffiths 1.47 | charge densities with delta functions: point charge, dipole, spherical shell |
| Should | Griffiths 1.46 | $`x\,\frac{d}{dx}\delta(x)=-\delta(x)`$; the step function and the delta |
| Could | Purcell 2.26 ** | the delta function (solved in chapter 12) |
| Could | Riley 13.26 | $`f(x)`$ as an integral over the delta function |

## Module exercises

### Exercise 1: delta of a function

**Where to read:** Griffiths §1.5.2.

**Statement.**

- (a) Let $`f(x)`$ have simple zeros at $`x_1,x_2,\dots`$ (so $`f'(x_i)\neq0`$). Show that
  $`\delta(f(x))=\sum_i\frac{\delta(x-x_i)}{\lvert f'(x_i)\rvert}`$.
- (b) Use it to write $`\delta(x^2-a^2)`$ as a sum of two deltas.
- (c) Evaluate $`\int_0^{2\pi}f(x)\,\delta(\cos x)\,dx`$ for a smooth $`f`$.

**Hint.** Near each zero, $`f(x)\approx f'(x_i)(x-x_i)`$, and only a small neighbourhood of each zero contributes to the integral. Then use $`\delta(ax)=\delta(x)/\lvert a\rvert`$, which you can prove by the substitution $`u=ax`$ (watch the sign of $`a`$: the absolute value comes from the limits of integration).

**Expected results.**

- (b) $`\delta(x^2-a^2)=\frac{\delta(x-a)+\delta(x+a)}{2\lvert a\rvert}`$.
- (c) $`f(\tfrac\pi2)+f(\tfrac{3\pi}2)`$.

### Exercise 2: the delta function in spherical coordinates

**Where to read:** Griffiths §1.5.3; the volume element $`d^3x=r^2\,dr\,\sin\theta\,d\theta\,d\phi`$.

**Statement.** Take a point $`\mathbf x'`$ not on the $`z`$-axis and not at the origin.

- (a) Write $`\delta^3(\mathbf x-\mathbf x')`$ as a product of one-dimensional deltas in $`(r,\theta,\phi)`$. Find the denominator that makes $`\int f(\mathbf x)\,\delta^3(\mathbf x-\mathbf x')\,d^3x=f(\mathbf x')`$ true.
- (b) Change variable to $`u=\cos\theta`$, so that $`d^3x=r^2\,dr\,du\,d\phi`$. Show that the same delta becomes $`\frac{\delta(r-r')\,\delta(u-u')\,\delta(\phi-\phi')}{r^2}`$. Which relation between $`\delta(\theta-\theta')`$ and $`\delta(\cos\theta-\cos\theta')`$ do you need?
- (c) Check that $`\int\delta^3(\mathbf x-\mathbf x')\,d^3x=1`$ with each form.

**Hint.** In the coordinates $`(r,u,\phi)`$ the measure is flat in $`u`$ and $`\phi`$ and only $`r^2`$ remains, so the denominator must be exactly $`r^2`$. The $`\sin\theta`$ in the first form is the Jacobian that disappears when you use $`u`$. For (b), apply exercise 1 to $`\delta(\cos\theta-\cos\theta')`$ near $`\theta=\theta'`$.

**Expected results.**

- (a) $`\frac{\delta(r-r')\,\delta(\theta-\theta')\,\delta(\phi-\phi')}{r^2\sin\theta}`$.
- (b) $`\delta(\cos\theta-\cos\theta')=\frac{\delta(\theta-\theta')}{\sin\theta'}`$.
- (c) both integrals give 1.

## Done when

- every delta integral in 1.44 and 1.45 is evaluated without hesitation
- 1.47(c) gives total charge $`Q`$
- you can explain in your own words why $`\cos\theta`$ is just a change of coordinates, and where the $`1/\sin\theta`$ goes

## Progress

- [ ] Griffiths 1.44
- [ ] Griffiths 1.45
- [ ] Griffiths 1.47
- [ ] Exercise 1
- [ ] Exercise 2
- [ ] Griffiths 1.46 (Should)
