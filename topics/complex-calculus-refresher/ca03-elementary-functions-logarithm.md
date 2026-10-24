# CA03: Elementary functions, the logarithm, $z^a$ and branch cuts

**Books:** Ávila Chapter 2, pp. 61 to 74 (exercise sets on pp. 62, 64, 73; answers and hints on p. 74). Churchill Chapter 3. **Time:** 2 sessions (Must: 1). **Tier note:** this is a "Should" module. In the deadline path read it once, do exercises 1 to 3, and come back before the Part 2 material.

## Why this matters

Because $e^z$ is periodic, it has no inverse, so $\log z$ cannot be single-valued. To get a function you cut the plane and pick a branch. The same issue makes $z^a$, $\sqrt{z^2-1}$ and every function with a fractional power multivalued. Branch cuts reappear in contour integration (keyhole contours, Part 2) and in QFT, where a cut in a propagator marks the threshold for multi-particle production. In this guide you need only the vocabulary and the basic recipe, so that a cut in an integrand is never a surprise.

## Skip-test (40 minutes, no notes)

1. Find all values of $\log(-1)$ and the principal value $\mathrm{Log}(-1)$.
2. Compute $i^i$ (principal value).
3. Solve $\sin z=2$.
4. State the domain on which the principal $\mathrm{Log}\,z$ is analytic and give its derivative.
5. Explain, in two sentences, why $\sqrt{z}$ has a branch point at $0$.

## Prerequisites

CA01, CA02.

## Detailed topics (checklist)

**[Must]** The exponential and its periodicity; $\sin z,\cos z$ via exponentials; they are unbounded (unlike the real ones); the hyperbolic functions.

**[Must]** The logarithm: $\log z=\ln\lvert z\rvert+i(\arg z+2\pi k)$; the principal value $\mathrm{Log}\,z$ with $-\pi<\mathrm{Arg}\,z\le\pi$; analytic on $\mathbb{C}\setminus(-\infty,0]$ with $(\mathrm{Log}\,z)'=1/z$.

**[Must]** Powers: $z^a=e^{a\log z}$, multivalued in general; $z^{1/2}$ has two values.

**[Should]** Branch point versus branch cut: the point is intrinsic (a loop around it changes the function), the cut is a choice. $\mathrm{Log}(z_1z_2)\ne\mathrm{Log}z_1+\mathrm{Log}z_2$ in general.

**[Should]** Inverse trigonometric functions as logarithms.

**[Could]** The logarithm as a transformation and its inverse (Ávila p. 67).

## Method cards

**Solving $e^z=w$.** $z=\ln\lvert w\rvert+i(\arg w+2\pi k)$.

**Solving $\sin z=w$.** Put $\zeta=e^{iz}$: $\zeta-1/\zeta=2iw$ is a quadratic in $\zeta$. Solve, then take $z=-i\log\zeta$.

**Choosing a branch.** (1) Find the branch points (where the argument of the expression winds). (2) Choose a cut joining them, or running to infinity. (3) Require continuity on any loop that does not cross the cut. (4) Fix the value at one point.

## Reading plan

| Session | Task |
|---|---|
| A1 | Ávila pp. 61 to 70 (exponential, trigonometric and hyperbolic functions, the logarithm, $z^a$). Derive items 1 and 2 |
| B1 | Exercises 1 to 5 and the Ávila sets on pp. 62 and 64 |
| A2 | Ávila pp. 70 to 73 (inverse trigonometric functions). Derive item 3 |
| B2 | Exercises 6 to 10, the Ávila set on p. 73, and the cheat sheet |

## Derive from scratch

1. $\log z=\ln\lvert z\rvert+i(\arg z+2\pi k)$ from $e^w=z$.
2. $(\mathrm{Log}\,z)'=1/z$ on the cut plane (use the inverse-function rule).
3. $\sin z=w$ solved through the quadratic in $e^{iz}$.

## Exercises (with expected results)

1. **(Must)** All values of $\log(-1)$ and $\mathrm{Log}(-1)$. *Expected:* $i\pi(2k+1)$; the principal value is $i\pi$.
2. **(Must)** $\mathrm{Log}(1+i)$. *Expected:* $\tfrac12\ln2+i\pi/4$.
3. **(Must)** $i^i$ (principal). *Expected:* $e^{-\pi/2}\approx0.2079$, a real number.
4. **(Must)** Solve $\sin z=2$. *Expected:* $z=\tfrac\pi2+2\pi k\pm i\ln(2+\sqrt3)$.
5. **(Must)** Show $\lvert\sin z\rvert^2=\sin^2x+\sinh^2y$, and conclude $\sin z$ is unbounded. *Expected:* expand $\sin(x+iy)$ and take the modulus.
6. **(Should)** Both values of $(1+i)^{1/2}$. *Expected:* $\pm2^{1/4}e^{i\pi/8}$.
7. **(Should)** Show $\mathrm{Log}(z_1z_2)\ne\mathrm{Log}z_1+\mathrm{Log}z_2$ in general. *Expected:* for $z_1=z_2=-1$, the left side is $\mathrm{Log}\,1=0$ and the right side is $2\pi i$.
8. **(Should)** Find the branch points of $\sqrt{z^2-1}$ and a cut that makes it single-valued. *Expected:* branch points $\pm1$; the cut along $[-1,1]$ gives a function analytic outside the segment with $f\sim z$ at infinity (a large loop makes $z^2-1$ wind twice, so the square root returns to itself).
9. **(Could)** $\tfrac{d}{dz}z^{1/2}$ at $z=4$ on the principal branch. *Expected:* $\tfrac14$.
10. **(Could)** Show $\cos^{-1}z=-i\log\big(z+i\sqrt{1-z^2}\big)$ and evaluate $\cos^{-1}2$. *Expected:* $\pm i\ln(2+\sqrt3)$ plus multiples of $2\pi$.

## Optional extension

Parametrise a small circle around $z=0$ and follow $\sqrt z$ once around: the value changes sign. Do the same for $\log z$ (it gains $2\pi i$). That is the definition of a branch point, done by hand.

## Pitfalls

* Writing $\log(z_1z_2)=\log z_1+\log z_2$ without tracking the $2\pi i$.
* Using the principal branch where the problem needs another.
* Treating $\sin z$ as bounded by $1$.
* Calling the cut a property of the function. The cut is a choice; the branch point is not.

## Gate questions

1. Why must $\log z$ be multivalued?
2. What is the difference between a branch point and a branch cut?
3. Where is the principal logarithm analytic, and why not on the negative real axis?

## One-page cheat sheet contents

$\log z$ and $\mathrm{Log}\,z$; $z^a$; the $\sin z=w$ recipe; the branch-point test (follow a loop); the three counterexamples.

## Where this is used

CA06 (the Laurent series of $\log$ is not available at a branch point), Part 2 (keyhole contours, Riemann surfaces), QFT thresholds.
