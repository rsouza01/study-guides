# CA07: Singularities and the residue theorem

**Books:** Ávila Chapter 5, pp. 151 to 161 (exercise sets on pp. 156 and 160; answers on pp. 157 and 161). Churchill Chapter 6. **Time:** 4 sessions (Must: 4). **Tier note:** this module is the spine of the guide. Do not skip it, and do all of exercises 1 to 5.

## Why this matters

A residue is the coefficient $a_{-1}$ of a Laurent series, and the residue theorem turns a contour integral into a sum of residues. Everything in CA08 and CA09 is this theorem applied to a particular integrand. The classification of singularities is also physical: in QFT a pole of a propagator is a stable particle and a branch cut is a multi-particle threshold, and the distinction begins here. The retarded, advanced and Feynman Green functions come from simple poles, so simple poles are your working case, but you need the formulas for higher orders as well.

## Skip-test (40 minutes, no notes)

1. Classify the singularities of $\frac{\sin z}{z}$, $\frac1{z^2(z-1)}$, $e^{1/z}$ and $\frac z{\sin z}$.
2. Write the residue formula for a simple pole and for a pole of order $m$.
3. Find the residue of $\frac{e^z}{(z-1)^3}$ at $z=1$.
4. State the residue theorem and its hypotheses.
5. Compute $\oint_{\lvert z\rvert=3}\frac{z+1}{z^2-2z}\,dz$.

## Prerequisites

CA04, CA05, CA06.

## Detailed topics (checklist)

**[Must]** Isolated singularities and their types: removable, pole of order $m$, essential (Ávila pp. 151 to 154). Read the type from the limit of $(z-z_0)^mf(z)$ or from the Laurent series. Name the Casorati–Weierstrass theorem.

**[Must]** The residue $\mathrm{Res}(f,z_0)=a_{-1}$.

**[Must]** The residue theorem: if $C$ is a positively oriented simple closed contour and $f$ is analytic on and inside $C$ except at finitely many points $z_k$ inside,

$$
\oint_Cf(z)\,dz=2\pi i\sum_k\mathrm{Res}(f,z_k).
$$

**[Must]** Computing residues: simple pole, $g/h$ with a simple zero of $h$, higher order, and by the Laurent series. At an essential singularity you must expand.

**[Should]** If $f=O(z^{-2})$ at infinity and all singularities are inside $C$, the sum of all residues is $0$.

## Method cards

**Residues.**

* Simple pole: $\mathrm{Res}=\lim_{z\to z_0}(z-z_0)f(z)$.
* $f=g/h$ with $h(z_0)=0$ and $h'(z_0)\ne0$: $\mathrm{Res}=g(z_0)/h'(z_0)$.
* Pole of order $m$: $\mathrm{Res}=\dfrac1{(m-1)!}\lim_{z\to z_0}\dfrac{d^{m-1}}{dz^{m-1}}\big[(z-z_0)^mf(z)\big]$.
* Essential singularity (or anything unclear): expand in a Laurent series and read $a_{-1}$.

**Using the theorem.** (1) Draw the contour and mark the singularities. (2) Decide which are inside; poles on the contour need CA08. (3) Compute each residue. (4) Add, multiply by $2\pi i$. (5) Check the orientation: clockwise gives $-2\pi i$.

## Reading plan

| Session | Task |
|---|---|
| A1 | Ávila pp. 151 to 157 (isolated singularities, the three types). Derive item 1 |
| B1 | Exercises 1 to 3 and the Ávila set on p. 156 |
| A2 | Ávila pp. 157 to 161 (the residue theorem). Derive items 2 and 3 |
| B2 | Exercises 4 to 10 and the Ávila set on p. 160. Cheat sheet |

## Derive from scratch

1. The three types of singularity from the Laurent series.
2. The residue theorem: deform to small circles (CA04) and apply the master integral to each Laurent series term.
3. The formula for the residue at a pole of order $m$.

## Exercises (with expected results)

1. **(Must)** Classify the singularities of $\frac{\sin z}{z}$, $\frac1{z^2(z-1)}$, $e^{1/z}$ and $\frac z{\sin z}$. *Expected:* removable at $0$; a double pole at $0$ and a simple pole at $1$; essential at $0$; removable at $0$ and simple poles at $n\pi$, $n\ne0$.
2. **(Must)** The residues of $\frac1{z^2+1}$. *Expected:* $-\frac i2$ at $z=i$ and $+\frac i2$ at $z=-i$.
3. **(Must)** The residue of $\frac{e^z}{z^2}$ at $0$ and of $\frac{e^z}{(z-1)^3}$ at $1$. *Expected:* $1$ and $\frac e2$.
4. **(Must)** $\oint_{\lvert z\rvert=3}\frac{z+1}{z^2-2z}\,dz$. *Expected:* $2\pi i$ (residues $-\tfrac12$ at $0$ and $\tfrac32$ at $2$).
5. **(Must)** $\oint_{\lvert z\rvert=1}\frac{\sin z}{z^4}\,dz$. *Expected:* $-\frac{i\pi}{3}$ (the residue is the coefficient of $z^3$ in $\sin z$, i.e. $-\tfrac16$).
6. **(Should)** $\oint\cot z\,dz$ on $\lvert z\rvert=1$ and on $\lvert z\rvert=4$. *Expected:* $2\pi i$ and $6\pi i$ (residue $1$ at each $n\pi$; the circle of radius $4$ encloses $0$ and $\pm\pi$).
7. **(Should)** $\oint_{\lvert z\rvert=1}\sin(1/z)\,dz$. *Expected:* $2\pi i$ (essential singularity; the residue is $1$).
8. **(Should)** $\oint_{\lvert z\rvert=1.5}\frac{dz}{z^4+1}$. *Expected:* $0$, since all four poles are inside and $f=O(z^{-4})$, so the residues sum to zero.
9. **(Could)** The residue of $\frac1{(z^2+1)^2}$ at $z=i$, and $\oint_{\lvert z-i\rvert=1}\frac{dz}{(z^2+1)^2}$. *Expected:* $-\frac i4$ and $\frac\pi2$.
10. **(Could)** Locate the poles of $\frac1{k^2-m^2+i\epsilon}$ and of $\frac1{k^2-m^2-i\epsilon}$. *Expected:* for $+i\epsilon$, at $k=\pm(m-i\epsilon')$, i.e. $+m-i\epsilon'$ below the real axis and $-m+i\epsilon'$ above; for $-i\epsilon$ the two poles swap sides. (This is EM Module 02, exercise 7.)

## Optional extension

Prove that the sum of the residues of a rational function that decays like $z^{-2}$ is zero, using a large circle, and use it to get the answer to exercise 8 without computing a single residue.

## Pitfalls

* Using the simple-pole formula on a pole of higher order.
* Forgetting that a pole on the contour is not covered by the theorem (CA08).
* Including a singularity that lies outside the contour.
* Missing the factor $\frac1{(m-1)!}$.
* Forgetting that an essential singularity needs the full Laurent expansion.

## Gate questions

1. Why does only $a_{-1}$ survive in $\oint f\,dz$?
2. How do you read the order of a pole from the Laurent series?
3. Why is the sum of residues of a rational function $O(z^{-2})$ equal to zero?

## One-page cheat sheet contents

The three types and how to read them; the four residue formulas; the residue theorem with its hypotheses; the orientation rule; the "sum of residues is zero" shortcut.

## Where this is used

CA08 and CA09 (every closed contour), EM Modules 02, 11 and 19, and the pole-as-particle picture in QFT.
