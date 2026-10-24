# CA01: Complex numbers, polar form, roots and the exponential

**Books:** Ávila Chapter 1, pp. 1 to 33 (exercise sets on pp. 7, 11, 15, 19, 24, 31; answers on pp. 12, 20, 25, 33). Churchill Chapter 1 for extra drills and the English vocabulary. **Time:** 2 sessions (1 if you pass the skip-test). **Tier note:** this is recall, not learning. Take the skip-test first.

## Why this matters

Everything in the guide is built on three facts from this chapter: a complex number is a point in the plane, multiplication is a rotation plus a scaling, and the exponential turns addition into multiplication. Polar form $z=re^{i\theta}$ is the working form for the whole guide and for plane waves in Jackson. The $n$ roots of a number are your first meeting with multivaluedness, and the periodicity $e^{z+2\pi i}=e^z$ is the reason the logarithm will need branch cuts in CA03. The point-set vocabulary (open, connected, simply connected) is the hypothesis of Cauchy's theorem in CA04.

## Skip-test (40 minutes, no notes)

1. Write $\dfrac{1+i}{2-i}$ in the form $a+bi$.
2. Write $-1+i\sqrt3$ in polar form.
3. Find all fourth roots of $-16$.
4. Show $e^{z+2\pi i}=e^z$ and find all $z$ with $e^z=-1$.
5. Describe the set $\{z:\ \lvert z-1\rvert<\lvert z+1\rvert\}$.
6. Give one example each of a set that is open, closed, connected, and not simply connected.

Expected: (1) $\tfrac{1+3i}{5}$; (2) $2e^{2\pi i/3}$; (3) $\sqrt2(\pm1\pm i)$; (4) $z=i\pi(2k+1)$; (5) the right half-plane $\mathrm{Re}\,z>0$; (6) an annulus $1<\lvert z\rvert<2$ is open, connected, not simply connected.

## Prerequisites

Stewart on the plane and trigonometry. Nothing else.

## Detailed topics (checklist)

**[Must]** $\mathbb{C}$ as $\mathbb{R}^2$ with a product; $\mathbb{R}$ as a subfield; modulus, conjugate, $z\bar z=\lvert z\rvert^2$, $1/z=\bar z/\lvert z\rvert^2$; the triangle inequality and its reverse form.

**[Must]** Polar form $z=re^{i\theta}$; the argument is multivalued, $\arg z=\theta+2\pi k$; product and quotient formulas; De Moivre's formula.

**[Must]** $n$-th roots: exactly $n$, equally spaced on a circle; the roots of unity; primitive roots; their sum is zero for $n\ge2$.

**[Must]** The exponential: $e^z=e^x(\cos y+i\sin y)$, $e^{z+w}=e^ze^w$, never zero, periodic with period $2\pi i$.

**[Should]** Point sets: neighbourhood, open, closed, boundary, bounded, connected (by polygonal paths), domain, simply connected (informally, no holes; formally, every loop shrinks to a point, as in your Stewart homotopy discussion). Name the Jordan curve theorem.

**[Could]** The point at infinity and the Riemann sphere (it returns in CA06, "regularity at infinity").

## Method cards

**Converting forms.** Cartesian to polar: $r=\lvert z\rvert$, $\theta=\operatorname{atan2}(y,x)$. Check the quadrant, not just $\tan\theta$.

**$n$-th roots of $w=\rho e^{i\varphi}$.** (1) Write $w$ in polar form. (2) The roots are $\rho^{1/n}e^{i(\varphi+2\pi k)/n}$ for $k=0,\dots,n-1$. (3) Plot them: $n$ equally spaced points. (4) Check by raising one to the $n$-th power.

**Describing a set.** Write $z=x+iy$, square to remove moduli, complete the square. A condition on $\lvert z-a\rvert$ is a disk or a half-plane; a condition on $\mathrm{Re}(1/z)$ is a disk after completing the square.

## Reading plan

| Session | Task |
|---|---|
| A1 | Skip-test. If it fails, read Ávila pp. 1 to 20 (plane, modulus, polar form, De Moivre, roots). Derive item 1 below |
| B1 | Exercises 1 to 5 and the Ávila sets on pp. 7, 11, 15, 19 |
| A2 | Ávila pp. 21 to 33 (exponential, point sets). Derive items 2 and 3 |
| B2 | Exercises 6 to 10, the Ávila sets on pp. 24 and 31, and the cheat sheet |

## Derive from scratch

1. De Moivre's formula, and the product formula for the polar form.
2. The roots of unity: that they are $n$ points, and that their sum is zero.
3. $e^{z+w}=e^ze^w$ from the definition $e^z=e^x(\cos y+i\sin y)$.

## Exercises (with expected results)

1. **(Must)** Compute $(1+i)^{10}$. *Expected:* $32i$.
2. **(Must)** Show the product of all $n$-th roots of unity is $(-1)^{n+1}$. *Expected:* this holds, e.g. $-1$ for $n=2$ and $+1$ for $n=3$.
3. **(Must)** Solve $z^3=8i$. *Expected:* $\sqrt3+i,\ -\sqrt3+i,\ -2i$.
4. **(Must)** Prove the parallelogram law $\lvert z+w\rvert^2+\lvert z-w\rvert^2=2(\lvert z\rvert^2+\lvert w\rvert^2)$. *Expected:* expand with $\lvert u\rvert^2=u\bar u$.
5. **(Must)** Use De Moivre to express $\cos3\theta$ and $\sin3\theta$ in powers of $\cos\theta$ and $\sin\theta$. *Expected:* $\cos3\theta=\cos^3\theta-3\cos\theta\sin^2\theta=4\cos^3\theta-3\cos\theta$; $\sin3\theta=3\cos^2\theta\sin\theta-\sin^3\theta$.
6. **(Should)** Sum $\sum_{k=0}^{n}\cos k\theta$ as the real part of a geometric series. *Expected:* $\tfrac12+\dfrac{\sin\big((n+\tfrac12)\theta\big)}{2\sin(\theta/2)}$. This is the Dirichlet kernel, and it returns in the Fourier series of your linear algebra path.
7. **(Should)** Find all $z$ with $e^z=1+i$. *Expected:* $z=\tfrac12\ln2+i(\tfrac\pi4+2\pi k)$.
8. **(Should)** Describe $\{z\ne0:\ \mathrm{Re}(1/z)>\tfrac12\}$. *Expected:* the open disk $\lvert z-1\rvert<1$ (the point $0$ lies on its boundary and is excluded).
9. **(Could)** For a primitive $n$-th root $\omega$, show $\prod_{k=1}^{n-1}(1-\omega^k)=n$. *Expected:* $n$ (for $n=5$ and $n=7$ this is checked numerically). Hint: factor $z^n-1$ and differentiate at $z=1$.
10. **(Could)** Classify as open, closed, connected, simply connected: (a) $1<\lvert z\rvert<2$; (b) $\{\lvert z\rvert\le1\}\cup\{\lvert z-3\rvert\le1\}$; (c) $\mathrm{Im}\,z>0$; (d) $\mathbb{C}\setminus[0,\infty)$. *Expected:* (a) open, connected, not simply connected; (b) closed, not connected; (c) open, connected, simply connected; (d) open, connected, simply connected (the slit plane, which will be the domain of the principal logarithm).

## Optional extension

Show that $z\mapsto1/z$ sends circles and lines to circles and lines (use exercise 8 as a model). It is the first conformal map you will meet and it returns in electrostatics by inversion.

## Pitfalls

* Forgetting that $\arg$ is defined only up to $2\pi k$.
* Taking the argument of a number in the second or third quadrant from $\arctan(y/x)$ without fixing the quadrant.
* Believing a complex number has one $n$-th root.
* Treating $e^z$ as one-to-one. It is not, and that is the whole story of CA03.

## Gate questions

1. Why is multiplication in the plane a rotation plus a scaling?
2. Why does a nonzero complex number have exactly $n$ distinct $n$-th roots?
3. What does the periodicity of $e^z$ force the logarithm to be?

## One-page cheat sheet contents

Polar form and De Moivre; the root recipe; $e^z$ in Cartesian form; the point-set definitions; the simply connected examples.

## Where this is used

CA03 (logarithm), CA04 (hypotheses of Cauchy's theorem), Jackson's plane waves $e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$.
