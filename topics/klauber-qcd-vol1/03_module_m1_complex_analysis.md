# Module 03: Module M1, Complex analysis for propagators (★, Week 4; Protocol A)

**Books:** Boas, *Mathematical Methods in the Physical Sciences*, Ch. 14 (complex analysis, residues); Arfken and Weber for reference; Byron and Fuller for the physicist's framing.
**Time:** 1 week, in a proper block (this is the least fragmentable material in the plan).

## Why this matters

**New in v0.3, and the direct answer to your concern.** Three weeks (Modules 03 to 05) building the tools Klauber uses and does not teach. Nothing here is QFT; everything here is load-bearing for it. By the end you will have constructed the Klein-Gordon propagator before Klauber introduces it.

## Diagnostic (40 minutes, no notes)

1. State and use the residue theorem to evaluate $\int_{-\infty}^\infty\frac{e^{ikx}}{k^2+m^2}dk$.
2. State Jordan's lemma and say when a contour may be closed in the upper or lower half plane.
3. Write the Sokhotski-Plemelj identity.
4. Evaluate $\int e^{-ik^0t}\frac{dk^0}{(k^0)^2-\omega^2\pm i\epsilon}$ for the three prescriptions (both poles pushed down, both up, Feynman).
5. State what you may and may not do when deforming a contour.

## Prerequisites

Calculus of a complex variable at the level of an introductory course (Stewart-level calculus; Cauchy-Riemann).

## Detailed topics (checklist)

- Analytic functions and the Cauchy-Riemann equations; Cauchy's theorem and integral formula; Laurent series, poles, residues; **the residue theorem**; contour deformation (what you may and may not do: no crossing singularities); Jordan's lemma and closing contours; principal value; **the Sokhotski-Plemelj identity** $\frac{1}{x\pm i\epsilon}=P\frac1x\mp i\pi\delta(x)$ (the single most used and least explained relation in QFT); branch points and cuts, lightly.

**The core exercise of the module.** Evaluate by contour $\int\frac{e^{ikx}}{k^2+m^2}dk$, then $\int\frac{e^{-ik^0t}}{(k^0)^2-\omega^2\pm i\epsilon}dk^0$. The second has **poles on the real axis** and is therefore *undefined until you say how to go around them*. Do it three ways (both poles pushed down, both pushed up, and the Feynman prescription: one each way). You will get three different functions of $t$. **Keep all three pages.** In Module 08 you will discover that these are the retarded, advanced and Feynman propagators, and you will already know where they came from.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Boas 14: analytic functions, Cauchy, Laurent |
| B1 | Exercises 1 to 3 |
| A2 | Residues; Jordan's lemma; the real-axis poles |
| B2 | Exercises 4 to 6 |
| A3 | Sokhotski-Plemelj; the three prescriptions |
| B3 | Exercises 7 to 10 |

## Derive from scratch

1. $\int\frac{e^{ikx}}{k^2+m^2}dk=\frac\pi me^{-m|x|}$ by closing in each half plane.
2. Jordan's lemma (the arc vanishes).
3. $\frac{1}{x\pm i\epsilon}=P\frac1x\mp i\pi\delta(x)$.
4. The three $k^0$ integrals.
5. The correspondence between the position of the poles and the $\theta$-function structure.

## Exercises

1. **[T] Basic contour:** $\int_{-\infty}^\infty\frac{e^{ikx}}{k^2+m^2}dk=\frac\pi me^{-m|x|}$ (poles at $\pm im$; close up for $x>0$, down for $x<0$).
2. **[T]** $\int_{-\infty}^\infty\frac{dx}{(x^2+1)^2}=\frac\pi2$ (double pole at $x=i$).
3. **[T]** $\int_{-\infty}^\infty\frac{\cos x}{x^2+a^2}dx=\frac{\pi e^{-a}}{a}$ ($a>0$).
4. **[T]** $\int_0^\infty\frac{dx}{1+x^4}=\frac{\pi}{2\sqrt2}$ (use the full line and even symmetry).
5. **[T] The three prescriptions (keep all three pages):** with poles at $k^0=\pm\omega$ (both pushed *below* the axis, $k^0\to k^0+i\epsilon$): $I(t)=-\frac{2\pi}{\omega}\theta(t)\sin\omega t$ (retarded); both pushed *above*: $I(t)=+\frac{2\pi}{\omega}\theta(-t)\sin\omega t$ (advanced); Feynman ($+i\epsilon$ in the denominator): $I(t)=-\frac{i\pi}{\omega}e^{-i\omega|t|}$ (and $+\frac{i\pi}\omega e^{+i\omega|t|}$ for $-i\epsilon$). State which poles each closing encloses.
6. **[T] Sokhotski:** verify $\int\frac{f(x)}{x\pm i\epsilon}dx\to P\!\!\int\frac{f(x)}{x}dx\mp i\pi f(0)$ with $f=e^{-x^2}$.
7. **[T] Indented contour:** $\int_{-\infty}^\infty\frac{\sin x}{x}dx=\pi$ (take the imaginary part of $\int\frac{e^{ix}}{x}$ on a contour indented above the origin).
8. **[T]** $\int_0^{2\pi}\frac{d\theta}{a+\cos\theta}=\frac{2\pi}{\sqrt{a^2-1}}$ ($a>1$) using $z=e^{i\theta}$.
9. **[C] Contour as a physical choice:** in one page, no hand-waving: *why* is a contour choice a physical choice? What is it that the mathematics is refusing to decide for you?
10. **[C] Deformation rules:** write the rules for deforming a contour in your own words and give an example where deforming through a pole changes the answer.

## Optional extension

Evaluate $\int_{-\infty}^\infty\frac{e^{ikx}}{\sqrt{k^2+m^2}}dk=2K_0(m|x|)$ using a branch cut (Bessel function appears in the Module 08 two-point function).

## Pitfalls

- Closing the contour on the wrong half plane (check where $e^{ikx}$ or $e^{-ik^0t}$ decays).
- Forgetting the $\pm$ from direction of encirclement.
- Treating the real-axis integral as defined before choosing $\pm i\epsilon$.

## Gate questions

1. Why does the sign of $t$ decide which half plane you close in?
2. What distinguishes retarded, advanced and Feynman contours?
3. Why is Sokhotski-Plemelj used so often?

## One-page cheat sheet contents

Residue formula; Jordan's lemma; Sokhotski-Plemelj; the three prescriptions and their results.
