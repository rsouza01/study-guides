# CA06: Taylor and Laurent series

**Books:** Ávila Chapter 4, pp. 118 to 150 (exercise sets on pp. 125, 132, 142, 149; hints and answers on pp. 127, 132, 144). Churchill Chapter 5. Stewart Chapter 11 for the real series. **Time:** 6 sessions (Must: 4; the series patch is 1 more session if you need it). **Tier note:** if the series skip-test below fails, do the patch first.

## Why this matters

Laurent is the only genuinely new idea in the series chapter. A Taylor series has non-negative powers; a Laurent series allows negative ones and converges on an annulus, because the centre may be singular. The coefficient of $(z-z_0)^{-1}$ is the residue, so CA07 is a chapter about reading one coefficient. The classification of singularities (removable, pole, essential) is read straight off the negative powers. Taylor's theorem also explains something you saw in Stewart: $\tfrac1{1+x^2}$ is smooth on the whole real line, yet its series about $0$ has radius $1$, because the singularities sit at $\pm i$ in the complex plane. The binomial series $(1+z)^{-1/2}$ generates the Legendre polynomials, so the multipole expansion of Jackson comes from this chapter.

## Skip-test (40 minutes, no notes)

Series patch, 15 minutes, from Stewart Chapter 11:

1. Find the radius of convergence of $\sum\frac{n!}{n^n}z^n$.
2. Does $\sum\frac{z^n}{n^2}$ converge on $\lvert z\rvert=1$?
3. Write the Taylor series of $\frac1{1+z^2}$ about $0$ and give its radius.

Laurent, 25 minutes:

4. State Taylor's theorem for an analytic function and say what limits the radius.
5. Expand $\frac1{z(z-1)}$ in $0<\lvert z\rvert<1$ and in $\lvert z\rvert>1$.
6. Write the Laurent coefficient formula.

## Prerequisites

CA04 and CA05. Stewart Chapter 11 (series of constants, convergence tests, power series, radius of convergence).

## Detailed topics (checklist)

**[Must]** Series of functions: pointwise versus uniform convergence; the Weierstrass M-test; a uniformly convergent series of continuous functions has a continuous sum.

**[Must]** Power series: radius of convergence (ratio or root test); termwise differentiation and integration inside the radius.

**[Must]** Taylor's theorem: $f$ analytic in $\lvert z-z_0\rvert<R$ equals its Taylor series there. The radius is the distance to the nearest singularity, which can be invisible on the real axis.

**[Must]** Known series ($e^z$, $\sin z$, $\cos z$, $\frac1{1-z}$, $\log(1+z)$, $(1+z)^\alpha$); products and quotients of series.

**[Must]** Laurent series on an annulus $r<\lvert z-z_0\rvert<R$:

$$
f(z)=\sum_{n=-\infty}^{\infty}a_n(z-z_0)^n,\qquad a_n=\frac1{2\pi i}\oint\frac{f(z)}{(z-z_0)^{n+1}}\,dz.
$$

The series is unique for a given annulus, and the same function has different Laurent series in different annuli.

**[Should]** Zeros of analytic functions: isolated, with an order; the identity theorem (by name). Behaviour at infinity ("regularidade no infinito"): study $f(1/w)$ at $w=0$.

**[Could]** The Cauchy–Hadamard formula for the radius.

## Method cards

**Laurent series of a rational function in an annulus.** (1) Partial fractions. (2) For each term $\frac1{z-a}$: if $\lvert z\rvert<\lvert a\rvert$ expand $-\frac1a\sum(z/a)^n$; if $\lvert z\rvert>\lvert a\rvert$ expand $\frac1z\sum(a/z)^n$. (3) Add. (4) Check the annulus: each geometric series must converge there.

**Taylor from a known series.** Substitute and multiply. Do not differentiate unless you must.

**Reading the type of a singularity.** No negative powers: removable. Finitely many, down to $(z-z_0)^{-m}$: pole of order $m$. Infinitely many: essential.

## Reading plan

| Session | Task |
|---|---|
| A0 | Series patch, only if the skip-test fails: Stewart 11.9 and 11.10, convergence tests |
| A1 | Ávila pp. 118 to 138 (series of functions, uniform convergence, power series, Taylor, examples, products). Derive items 1 and 2 |
| B1 | Exercises 1 and 2 and the Ávila sets on pp. 125, 132 and 142 |
| A2 | Ávila pp. 144 to 150 (Laurent, infinity, zeros). Derive item 3 |
| B2 | Exercises 3 to 5 and the Ávila set on p. 149 |
| B3 | Should: exercises 6 to 10 and the cheat sheet |

## Derive from scratch

1. Taylor's theorem from Cauchy's formula: expand $\tfrac1{z-\zeta}$ as a geometric series inside the circle.
2. The radius of convergence of the Taylor series of $\frac1{1+z^2}$ at $0$, and why it is $1$.
3. The Laurent coefficient formula, from the formula on the two circles bounding the annulus.

## Exercises (with expected results)

1. **(Must)** Radius of convergence of $\sum_{n\ge1}\frac{n!}{n^n}z^n$. *Expected:* $e$.
2. **(Must)** Taylor series of $\frac1{1+z^2}$ about $0$. *Expected:* $\sum(-1)^nz^{2n}$ with radius $1$; the singularities are at $\pm i$, invisible from the real line.
3. **(Must)** Laurent series of $\frac1{z(z-1)}$ in $0<\lvert z\rvert<1$ and in $\lvert z\rvert>1$. *Expected:* $-\frac1z-1-z-z^2-\cdots$ and $z^{-2}+z^{-3}+\cdots$.
4. **(Must)** Laurent series of $\frac1{(z-1)(z-2)}$ in $1<\lvert z\rvert<2$. *Expected:* $-\sum_{n\ge0}\frac{z^n}{2^{n+1}}-\sum_{n\ge1}z^{-n}$.
5. **(Must)** Show $e^{1/z}=\sum_{n\ge0}\frac1{n!\,z^n}$ has an essential singularity at $0$ and residue $1$. *Expected:* infinitely many negative powers, $a_{-1}=1$.
6. **(Should)** The coefficient $a_{-1}$ of $\frac{e^z}{z^3}$ at $0$. *Expected:* $\tfrac12$.
7. **(Should)** The Laurent series of $\cot z$ about $0$. *Expected:* $\frac1z-\frac z3-\frac{z^3}{45}-\cdots$ (residue $1$).
8. **(Should)** The order of the zero at $0$ of $z-\sin z$ and of $1-\cos z$. *Expected:* $3$ and $2$.
9. **(Could)** Check the coefficient formula by computing $a_{-1}$ of $\frac1{z(z-1)}$ at $0$ as $\frac1{2\pi i}\oint_{\lvert z\rvert=1/2}$. *Expected:* $-1$, matching exercise 3.
10. **(Could)** Expand $(1-2xt+t^2)^{-1/2}$ in powers of $t$ to second order. *Expected:* $1+xt+\frac{3x^2-1}{2}t^2$, i.e. $P_0=1$, $P_1=x$, $P_2=\frac{3x^2-1}{2}$.

## Optional extension

Expand $\frac1{z^2-3z+2}$ in all three regions $\lvert z\rvert<1$, $1<\lvert z\rvert<2$, $\lvert z\rvert>2$ and check the three series against each other on the overlaps of their coefficient formulas.

## Pitfalls

* Using the Taylor series outside its disk.
* Using one Laurent series for a whole region when the function has several annuli.
* Computing the radius from the real line only.
* Confusing the Laurent series of $\frac1{z-a}$ in $\lvert z\rvert<\lvert a\rvert$ with the one in $\lvert z\rvert>\lvert a\rvert$.

## Gate questions

1. Why does the Taylor series of $\frac1{1+x^2}$ have radius $1$?
2. Why does a Laurent series converge on an annulus and not on a disk?
3. How do you read the type of a singularity from the series?

## One-page cheat sheet contents

Taylor's theorem and the radius rule; the Laurent formula; the annulus recipe; the singularity types; the standard series.

## Where this is used

CA07 (residues are $a_{-1}$), EM Modules 06 and 07 (the Legendre generating function), the multipole expansion in Jackson Chapter 4.
