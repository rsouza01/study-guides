# Module 09: Chapter 3d, consolidation, micro-causality and the elasticity rule (★★, Week 11; Protocol A)

**Books:** Klauber Ch. 3 (states and normalisation), his free *Summary of operators, fields, and states in different QFT vector spaces* (designed for exactly this point in the book) and his *Free Fields Wholeness Chart*; second source: Lancaster and Blundell on scalar-field quantisation.
**Time:** 1 week, plus up to two extension weeks (the elasticity rule below).

## Why this matters

State normalisation, the relativistic conventions, the vector-space picture. **Calculation 7: micro-causality.** Show $[\phi(x),\phi(y)]=0$ for spacelike separation. The argument: the commutator is a Lorentz-invariant function of $(x-y)^2$; for spacelike separation boost to a frame where the points are simultaneous; the $\mathbf k\to-\mathbf k$ symmetry of the integrand then kills it. It is worth the time for the contrast with calculation 5: **the two-point function is nonzero outside the light cone yet the commutator vanishes.** That combination is what "causality survives" actually means in QFT, and it is subtler than the slogan.

## Diagnostic (40 minutes, no notes)

1. Prove micro-causality $[\phi(x),\phi(y)]=0$ for $(x-y)^2<0$.
2. Write the relativistic normalisation of one-particle states and show it is Lorentz invariant.
3. Compute the commutator function for the massless field and show its support on the light cone.
4. State the explicit Fock-space content of the scalar field's state space.
5. Write the scalar field theory on one page as an argument.

## Prerequisites

Modules 06 to 08.

## Detailed topics (checklist)

- **Calculation 7:** $[\phi(x),\phi(y)]=D(x-y)-D(y-x)=\int\frac{d^3k}{(2\pi)^32\omega}\left(e^{-ik\cdot(x-y)}-e^{ik\cdot(x-y)}\right)$; the measure is Lorentz invariant so the function depends only on $(x-y)^2$ and on the sign of $(x-y)^0$ for timelike; for spacelike separation boost to $(x-y)^0=0$ where $\mathbf k\to-\mathbf k$ shows the integrand cancels.
- **States and normalisation:** $|\mathbf k\rangle=a^\dagger(\mathbf k)|0\rangle$ with $\langle\mathbf k|\mathbf k'\rangle=\delta^3(\mathbf k-\mathbf k')$; the relativistically normalised $|k\rangle_{\rm rel}=\sqrt{2\omega(2\pi)^3}\,a^\dagger(\mathbf k)|0\rangle$ with $\langle k|k'\rangle=2\omega(2\pi)^3\delta^3(\mathbf k-\mathbf k')$ (invariant); completeness $1=\int\frac{d^3k}{(2\pi)^32\omega}|k\rangle\langle k|$; the vector-space picture (Fock space as a direct sum of $n$-particle spaces).
- The wholeness chart: your own one-page chart of the scalar field's objects, equations and relations, compared with Klauber's.

## ▣ The elasticity rule: how much longer you may take

You do not mind spending more time here if you come out understanding the math. Good, but "more time" needs a trigger, or the chapter quietly becomes the plan.

**At the end of Week 11, attempt calculations 3, 4 and 6 closed-book, in one sitting.**
- **All three come out** $\to$ proceed to Chapter 4 on schedule. You have it.
- **One fails** $\to$ take **one extension week** on that calculation and its dependencies, then retest. A failure in 3 usually means 2 was not really done, and a failure in 6 usually means the Module M contour work needs another day rather than the chapter needing another week.
- **Two or more fail** $\to$ take **two extension weeks**, and read it as evidence that Module M was undersized rather than that Chapter 3 was. Go back to Modules 03 and 05 first.

**Cap it at two.** Beyond that the problem is not the chapter, and grinding further has poor returns compared with moving to Chapter 4 and letting the spinor propagator (the same construction with indices) give you a second look at the same machinery. Some things only land on the second instance, and Chapter 4 *is* the second instance.

**Where extension weeks come from.** *Not* from Part Three (that is where the hollowness is probably worst and it is already at its minimum). Extension weeks push Phase 1 to Week 30 or 31 and Phase 2 starts correspondingly later: this track is decoupled and budgeted by chapters, so it may run long.

### ⚠ A warning about these five weeks

The eight calculations are the *mathematical* content. They are not the whole chapter, and completing them is not the same as understanding what a quantum field is. Protocol A's step 3 (concretise) and the **[C]** problems are doing separate work, and in a chapter this technically absorbing it would be easy to let them slide. That would reproduce the original failure with better mathematics: correct manipulations, no picture. The test that the conceptual side landed is the Module 08 **[C]**: explain the Feynman prescription, without equations, to someone who knows classical Green functions but no QFT. If calculation 6 works but that paragraph will not come, you have the math and not the physics.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Calculation 7; the contrast with calculation 5 |
| B1 | Exercises 1 to 3 |
| A2 | States, normalisation and Klauber's summary |
| B2 | Exercises 4 and 5 |
| A3 | Second source; the wholeness chart; the compression exercise |
| B3 | Exercises 6 to 10; the elasticity test |

## Derive from scratch

1. Calculation 7.
2. The invariance of the relativistic state normalisation.
3. The completeness relation.
4. The massless commutator function.
5. The one-page argument for scalar field theory.

## Exercises

1. **[T] Calculation 7:** $[\phi(x),\phi(y)]=0$ for $(x-y)^2<0$ (boost to $(x-y)^0=0$; $\int\frac{d^3k}{2\omega}\left(e^{i\mathbf k\cdot\mathbf r}-e^{-i\mathbf k\cdot\mathbf r}\right)=0$ by $\mathbf k\to-\mathbf k$).
2. **[T] Contrast with calculation 5:** $D(r)=\frac{m}{4\pi^2r}K_1(mr)\ne0$ at spacelike separation but $D(x)-D(-x)=0$ there.
3. **[T] Massless commutator function:** $[\phi(x),\phi(0)]=-\frac{i}{2\pi}\,\epsilon(x^0)\,\delta(x^2)$ (support on the light cone only); for $m>0$ there is also a tail inside the cone.
4. **[T] State normalisation:** $\langle k|k'\rangle=2\omega(2\pi)^3\delta^3(\mathbf k-\mathbf k')$ is Lorentz invariant because $\omega\delta^3(\mathbf k-\mathbf k')$ is (the Jacobian $\frac{d^3k'}{\omega'}$ is invariant); completeness $1=\int\frac{d^3k}{(2\pi)^32\omega}|k\rangle\langle k|$ on the one-particle space.
5. **[T] Closed-book sitting (the elasticity test):** attempt calculations 3, 4 and 6 in one sitting; grade each with a rubric: setup (2), the key step (2), the result and interpretation (1).
6. **[T] Fock space check:** the number of $n$-particle states in a box with $M$ modes is $\binom{M+n-1}{n}$ (bosons); check for $M=3$, $n=2$: $6$.
7. **[C] Compression:** scalar field theory on one page, as an argument (not a formula sheet).
8. **[C] Second source:** after reading Lancaster and Blundell on scalar-field quantisation, list what you recognise and what you do not.
9. **[C] What causality survives:** explain, without equations, how the two-point function can be nonzero outside the light cone while causality is preserved.
10. **[C] Wholeness chart:** write your own scalar-field wholeness chart, then compare with Klauber's and note any difference.

## Optional extension

Prove that $\epsilon(x^0)\delta(x^2)$ is Lorentz invariant for timelike and lightlike $x$ even though $\epsilon(x^0)$ alone is not.

## Pitfalls

- Treating equal-time commutation and micro-causality as the same statement.
- Using non-invariant normalisation without tracking the $2\omega$.
- Extending beyond two weeks instead of moving on.

## Gate questions

1. Why is the commutator zero outside the light cone while $D\ne0$?
2. Why is $2\omega(2\pi)^3\delta^3$ the invariant normalisation?
3. What decides whether to take an extension week?

## One-page cheat sheet contents

Micro-causality proof; state normalisations; the massless commutator function; the elasticity rule.
