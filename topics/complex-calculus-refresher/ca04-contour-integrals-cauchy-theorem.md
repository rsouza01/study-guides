# CA04: Contour integrals and Cauchy's theorem

**Books:** Ávila Chapter 3, pp. 75 to 101 (exercise sets on pp. 79, 86, 99; answers and hints on pp. 88, 101). Churchill Chapter 4. Stewart 16.2 to 16.4 as the real-variable parent. **Time:** 4 sessions (Must: 4). **Tier note:** no skip-test passes this module by memory. The proof of Cauchy's theorem from Green's theorem is the point, so do it by hand even if you know the statement.

## Why this matters

A contour integral is a line integral of the type $\int P\,dx+Q\,dy$ with complex $P$ and $Q$. Everything you did in Stewart 16.2 to 16.4 transfers: parametrise the curve, substitute, integrate, with orientation mattering. Cauchy's theorem is Green's theorem plus the Cauchy–Riemann equations, so it is a corollary of what you already own. The deformation principle, which you met as the extended Green's theorem with a hole, becomes the working method of the whole guide: shrink a contour onto small circles around the singularities. The ML-estimate is the tool that will make Jordan's lemma work in CA08. The wire field you studied (curl-free, but circulation $2\pi$) is $1/z$ in disguise.

## Skip-test (40 minutes, no notes)

1. Write $\int_Cf\,dz$ as two real line integrals in $u$ and $v$.
2. State and prove the ML-estimate.
3. Compute $\oint_{\lvert z\rvert=1}z^n\,dz$ for every integer $n$.
4. Prove Cauchy's theorem from Green's theorem.
5. Explain why $\oint_{\lvert z\rvert=1}dz/z\ne0$ does not contradict Cauchy's theorem.
6. State the deformation principle for a region with one hole.

## Prerequisites

CA02 (Cauchy–Riemann). Stewart 16.2 (line integrals), 16.3 (path independence, primitives), 16.4 (Green's theorem and its extended version).

## Detailed topics (checklist)

**[Must]** Arcs and contours: parametrised, piecewise smooth (regular), simple, closed; positive orientation. Name the Jordan curve theorem (a simple closed curve has an inside and an outside).

**[Must]** Definition and evaluation: $\int_Cf\,dz=\int_a^bf(\gamma(t))\gamma'(t)\,dt$. Equals $\int u\,dx-v\,dy+i\int v\,dx+u\,dy$. Independent of the parametrisation, changes sign when the orientation reverses, additive on the pieces of a contour.

**[Must]** The ML-estimate: $\left\lvert\int_Cf\,dz\right\rvert\le ML$, where $M=\max_C\lvert f\rvert$ and $L$ is the length of $C$.

**[Must]** Primitives: if $F'=f$ on a region containing $C$, then $\int_Cf\,dz=F(b)-F(a)$ (Stewart 16.3), so closed integrals vanish.

**[Must]** Cauchy's theorem: if $f$ is analytic in a simply connected domain, $\oint_Cf\,dz=0$ for every closed contour in it. Ávila proves it from Green's theorem (p. 89), assuming a continuous $f'$; Goursat's theorem removes the assumption (name it).

**[Must]** Deformation. In a multiply connected region, two closed contours that can be deformed into each other without crossing a singularity give the same integral. The master integral:

$$
\oint_{\lvert z-z_0\rvert=r}(z-z_0)^n\,dz=2\pi i\,\delta_{n,-1}.
$$

**[Should]** A primitive exists in a simply connected domain; Morera's theorem (the converse of Cauchy), by name.

## Method cards

**Evaluating a contour integral directly.** (1) Parametrise: $z=\gamma(t)$, $t\in[a,b]$. (2) Write endpoints $\gamma(a)$, $\gamma(b)$ and check them, as in your Stewart 16.2 work. (3) Compute $\gamma'(t)$. (4) Substitute into $f(\gamma(t))\gamma'(t)$. (5) Integrate. Direction lives in the parametrisation only.

**ML-estimate.** (1) Bound $\lvert f\rvert$ on the contour by a number $M$ (find the minimum of the denominator). (2) Compute the length $L$. (3) Conclude $\lvert\int\rvert\le ML$. Use it to show an arc contributes nothing as its radius grows.

**Deformation.** (1) Mark the singularities. (2) Decide which lie inside the contour. (3) Replace the contour by small circles around those singularities (a channel between them cancels). (4) Evaluate each circle with the master integral.

## Reading plan

| Session | Task |
|---|---|
| A1 | Ávila pp. 75 to 82 (arcs, Jordan's theorem, contour integral, invariance, properties). Derive items 1 and 3 |
| B1 | Exercises 1 to 3 and the Ávila sets on pp. 79 and 86 |
| A2 | Ávila pp. 89 to 93 (Green's theorem, Cauchy's theorem). Derive item 2, the proof by hand |
| B2 | Exercises 4 to 6 |
| A3 | Ávila pp. 93 to 101 (contour integrals and primitives, deformation) |
| B3 | Exercises 7 to 10 and the Ávila set on p. 99 |
| A4 | Spare session: redo the failed items of the skip-test. Cheat sheet |

## Derive from scratch

1. $\oint_C(u+iv)(dx+i\,dy)=\oint_C(u\,dx-v\,dy)+i\oint_C(v\,dx+u\,dy)$, and both real integrals vanish by Green's theorem and Cauchy–Riemann. For the first, $P=u$ and $Q=-v$, so $Q_x-P_y=-v_x-u_y=0$. For the second, $P=v$ and $Q=u$, so $Q_x-P_y=u_x-v_y=0$.
2. The master integral: with $z=z_0+re^{i\theta}$, $\oint(z-z_0)^n\,dz=ir^{n+1}\int_0^{2\pi}e^{i(n+1)\theta}\,d\theta=2\pi i\,\delta_{n,-1}$.
3. The ML-estimate, from $\left\lvert\int_a^bg\,dt\right\rvert\le\int_a^b\lvert g\rvert\,dt$.

## Exercises (with expected results)

1. **(Must)** $\oint_{\lvert z\rvert=1}dz/z$ and $\oint_{\lvert z\rvert=1}z^2\,dz$. *Expected:* $2\pi i$ and $0$.
2. **(Must)** Compute $\int_C\bar z\,dz$ along the upper half of the unit circle from $1$ to $-1$, then along the straight segment. *Expected:* $i\pi$ and $0$ (so it is path-dependent, and $\bar z$ is not analytic).
3. **(Must)** $\int_0^{1+i}z^2\,dz$ along any path. *Expected:* $\tfrac{(1+i)^3}{3}=\tfrac{-2+2i}{3}$.
4. **(Must)** Bound $\left\lvert\oint_{\lvert z\rvert=2}\frac{dz}{z^2+1}\right\rvert$ with the ML-estimate, then compute it exactly with partial fractions. *Expected:* the bound is $\tfrac{4\pi}{3}$ (since $\lvert z^2+1\rvert\ge3$ on the circle); the exact value is $0$.
5. **(Must)** Prove Cauchy's theorem by hand, by the expansion in derivation item 1. *Expected:* both double integrals vanish identically.
6. **(Should)** $\oint\frac{dz}{z(z-1)}$ on $\lvert z\rvert=\tfrac12$ and on $\lvert z\rvert=2$. *Expected:* $-2\pi i$ and $0$. Use $\tfrac1{z(z-1)}=\tfrac1{z-1}-\tfrac1z$. This is "which singularities you enclose".
7. **(Should)** For the positively oriented square with vertices $\pm2\pm2i$, compute $\oint\frac{dz}{z-z_0}$ for $z_0=\tfrac12$ and $z_0=3$. *Expected:* $2\pi i$ and $0$, by deforming to a circle.
8. **(Should)** $\int_0^{i\pi}e^z\,dz$. *Expected:* $-2$.
9. **(Could)** Show $1/z$ has no primitive on $\mathbb{C}\setminus\{0\}$ but has one on the slit plane. *Expected:* a primitive would make $\oint dz/z=0$; on the slit plane it is $\mathrm{Log}\,z$.
10. **(Could)** The wire field. For $\mathbf{F}=\dfrac{-y\,\mathbf{i}+x\,\mathbf{j}}{x^2+y^2}$ show $\oint\mathbf{F}\cdot d\mathbf{r}=\mathrm{Re}\oint(P-iQ)\,dz$ and that $P-iQ=-i/z$. *Expected:* $2\pi$ on any loop around the origin.

## Optional extension

Show Cauchy's theorem for a region with a hole by cutting a channel (your Stewart 16.4 Example 5, now in complex form). State what changes if the integrand has two singularities inside.

## Pitfalls

* Dropping the orientation: a clockwise circle gives $-2\pi i$.
* Applying Cauchy's theorem when a singularity sits inside or on the contour.
* Forgetting the $\gamma'(t)$ factor.
* Bounding $\lvert f\rvert$ at one point instead of its maximum (for the ML-estimate use the minimum of the denominator).

## Gate questions

1. Why is Cauchy's theorem a corollary of Green's theorem?
2. Why is $\oint dz/z=2\pi i$ not a contradiction?
3. Why is the integral over a contour independent of its shape as long as it avoids the singularities?

## One-page cheat sheet contents

The two-real-integrals formula; the parametrisation recipe; the ML-estimate; Cauchy's theorem with its hypotheses; the master integral; the deformation recipe.

## Where this is used

CA05 (Cauchy's formula), CA07 and CA08 (every residue calculation), Jackson Chapter 1 (Green's identities in the same spirit).
