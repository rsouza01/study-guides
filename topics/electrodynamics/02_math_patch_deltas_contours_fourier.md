# Module 02: Math patch: delta functions, Fourier transforms, index notation

**Books:** Griffiths §1.5 The Dirac Delta Function (pp. 43 to 50: 1.5.1 the divergence of $\hat r/r^2$, 1.5.2 the one-dimensional delta, 1.5.3 the three-dimensional delta); Jackson §1.2 Electric Field (p. 24, the delta-function treatment of point charges); Riley §13.1 Fourier transforms (pp. 433 to 453: the Dirac $\delta$-function, its relation to Fourier transforms, convolution, Parseval, Fourier transforms in higher dimensions), Chapter 12 Fourier series (pp. 415 to 426: 12.1 to 12.3 and 12.7), Chapter 26 tensors for index notation (§26.1 notation, §26.3 Cartesian tensors, §26.8 the tensors $\delta_{ij}$ and $\epsilon_{ijk}$, pp. 928 to 944), and for the ODE kit §15.1 (p. 492) and §17.4 Sturm-Liouville (p. 564). Stewart is not enough here.
**Time:** 2 weeks (four sessions: three of work and one spare, now that the contour integrals live in the complex analysis guide). A session is a part A (read, derive) followed by a part B (exercises).
**Pinned to:** Griffiths 5th ed. (2024), Jackson 3rd ed. (1999), Purcell and Morin 3rd ed. (2013, SI), Riley, Hobson and Bence 3rd ed. Page numbers are the printed book pages.
**Moved out:** contour integration (Cauchy's theorem, residues, Jordan's lemma, closing contours, the $\pm i\epsilon$ prescription, the principal value and the Sokhotski formula) is no longer part of this module. It is taught in the complex analysis guide (CA04 to CA09) and is first needed in Module 11.

## Why this matters

Stewart does not cover these, and you need all of them. **Delta-function calculus** gives $\nabla^2\frac1r=-4\pi\delta^3(\mathbf r)$ (Module 05) and the Lienard-Wiechert factor $(1-\boldsymbol\beta\cdot\hat{\mathbf n})^{-1}$ (Module 20). **Fourier transforms** turn differential equations into algebra. **Index notation** makes every vector identity a one-line proof. **ODE recipes** give the radial functions $r^\ell$, $r^{-\ell-1}$ and the Bessel and Legendre equations of Modules 06 to 08.

## Task 0: orientation (10 minutes)

The reading map is no longer a separate file: every module now carries its own pinned reading plan and problem set, and the README lists the sections of all modules. Before Session 1, open Griffiths at p. 43, Jackson at p. 24 and Riley at p. 433 and check that the pages match what is pinned here; note any mismatch in `notes/error_log.md`.

## Skip-test (40 minutes, no notes)

1. Show $\delta(f(x))=\sum_i\frac{\delta(x-x_i)}{|f'(x_i)|}$ and evaluate $\delta(x^2-a^2)$.
2. Write $\delta^3(\mathbf x-\mathbf x')$ in spherical coordinates and show that $\int\delta^3d^3x=1$.
3. Show $\nabla^2\frac1r=-4\pi\delta^3(\mathbf r)$ using the divergence theorem on a small sphere.
4. Compute the Fourier transform of $e^{-ax^2}$ and state the convolution theorem.
5. Prove $\nabla\times(\nabla\times\mathbf A)=\nabla(\nabla\cdot\mathbf A)-\nabla^2\mathbf A$ with $\epsilon_{ijk}$.

## Prerequisites

Module 01.

## Detailed topics (checklist)

**Delta-function calculus [Must]**

- Definition by $\int f\delta=f(0)$; $\delta(ax)=\delta(x)/|a|$; $\delta(f(x))=\sum_i\delta(x-x_i)/|f'(x_i)|$; derivative of the delta function; the step function $\theta(x)$ and $\theta'=\delta$.
- Three dimensions: $\delta^3(\mathbf x-\mathbf x')=\frac{\delta(r-r')\delta(\theta-\theta')\delta(\phi-\phi')}{r^2\sin\theta}=\frac{\delta(r-r')\delta(\cos\theta-\cos\theta')\delta(\phi-\phi')}{r^2}$ (and the cylindrical analogue with $\rho$); $\nabla^2\frac1r=-4\pi\delta^3$; the charge density of a point charge $\rho=q\delta^3(\mathbf x-\mathbf x_0)$ and of a *moving* charge $\rho=q\delta^3(\mathbf x-\mathbf r(t))$.

**Fourier transforms [Must]**

- Conventions (state yours): $\tilde f(k)=\int f(x)e^{-ikx}dx$, $f(x)=\int\frac{dk}{2\pi}\tilde f(k)e^{ikx}$; Gaussian $\to$ Gaussian; derivative $\to$ multiplication by $ik$; convolution theorem; the 3D transform of $\frac1r$ ($\frac{4\pi}{k^2}$) and of the Yukawa potential $\frac{e^{-\mu r}}r$ ($\frac{4\pi}{k^2+\mu^2}$); Fourier series on an interval (sine series).

**Index notation [Must]**

- Einstein summation, $\delta_{ij}$, $\epsilon_{ijk}$; $\epsilon_{ijk}\epsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}$; proofs of vector identities in one line.

**ODE kit [Should; revisited in Modules 06 to 08]**

- $y''+k^2y=0$ ($\sin,\cos$), $y''-k^2y=0$ ($\sinh,\cosh$ or $e^{\pm kx}$); the Euler equation $r^2R''+2rR'-\ell(\ell+1)R=0$ with solutions $r^\ell$ and $r^{-\ell-1}$; the Legendre and Bessel equations (names only); Sturm-Liouville eigenvalue problems and orthogonality (statement).

## Method cards

**Delta of a function:** (1) find the zeros $x_i$; (2) compute $|f'(x_i)|$; (3) $\sum\delta(x-x_i)/|f'(x_i)|$.

## Reading plan (pinned to your editions)

A session is part A (read, derive) followed by part B (exercises), about two and a half hours in all. Page numbers are the printed ones.

| Session | A: read and derive | B: do | Done when |
| --- | --- | --- | --- |
| 1 | Task 0 (orientation, 10 minutes: open each book at the pinned page). Griffiths §1.5.1 to §1.5.3 (pp. 43 to 50). | Griffiths Problem 1.44 (delta-function integrals (sifting property)), Problem 1.45 (delta-function integrals with delta(3x) and compositions), Problem 1.46 (x d/dx delta(x) = -delta(x); the step function and delta), Problem 1.47 (charge densities with delta functions: point charge, dipole, spherical shell); module exercises 1 and 2. | Every delta integral in 1.44 and 1.45 evaluated without hesitation; 1.47(c) gives total charge Q. |
| 2 | Jackson §1.2 (p. 24). Griffiths Problem 1.48 (3D delta-function integrals) and Problem 1.64 (check that the Laplacian of 1/r is -4 pi delta, another way). | Module exercises 3 and 4. Jackson Problem 1.2 (delta function in general orthogonal coordinates (limit of a Gaussian)) and Problem 1.3 (charge distributions written with delta functions (shell, cylinder, disc)) (p. 51). | The flux argument for the Laplacian of 1/r written on one page; Jackson 1.3(a) agrees with your Griffiths 1.47(c). |
| 3 | Riley §13.1 (pp. 433 to 453); Riley §26.1, §26.3, §26.8 (pp. 928 to 944). | Module exercises 5, 9 and 10. Riley Exercises 13.1, 13.3, 13.5, 13.7 (pp. 460 to 462) and 26.1, 26.5, 26.9 (pp. 977 to 980). | Gaussian transform and Yukawa transform done; both index-notation identities proved with $\epsilon_{ijk}$. |
| 4 (spare) | ODE kit: Riley §15.1 (p. 492) and §17.4 (p. 564), read only; cheat sheet. | Redo the failed items of the skip-test. | Cheat sheet written; skip-test items 1 to 5 all pass. |

## Problem set (pinned)

**Pin status:** Pinned: Griffiths and Jackson sections and problems (verified), Riley sections (verified). Riley exercises are pinned below (odd-numbered ones have worked solutions in the Student Solution Manual).

Tiers: **Must** (do all), **Should** (do when time allows), **Could** (only if the module is going well). A dash in the exercise column means the problem supports the reading rather than a module exercise. Purcell and Morin: stars give difficulty; problems are solved in Chapter 12 (the exercises are not).

| Book | Problem | What it asks | Module exercise | Tier |
| --- | --- | --- | --- | --- |
| Griffiths | 1.44 | delta-function integrals (sifting property) | 1 | Must |
| Griffiths | 1.45 | delta-function integrals with delta(3x) and compositions | 1 | Must |
| Griffiths | 1.47 | charge densities with delta functions: point charge, dipole, spherical shell | 4 | Must |
| Jackson | 1.3 | charge distributions written with delta functions (shell, cylinder, disc) | 2 | Must |
| Riley | 13.1 | Fourier transform of exp(-\vert t\vert ) | 5 | Must |
| Riley | 13.5 | transform the equation phi'' - K^2 phi = f(x): the screened-Poisson pattern | 9 | Must |
| Riley | 26.1 | Cartesian-tensor definition: basic properties | 10 | Must |
| Riley | 26.6 | vector identities by tensor methods (even number: no worked solution) | 10 | Must |
| Griffiths | 1.46 | x d/dx delta(x) = -delta(x); the step function and delta | 1 | Should |
| Griffiths | 1.48 | 3D delta-function integrals | 2 | Should |
| Griffiths | 1.64 | check that the Laplacian of 1/r is -4 pi delta, another way | 3 | Should |
| Riley | 13.3 | Fourier transform of H(x-a)exp(-bx) | 5 | Should |
| Riley | 13.7 | Fourier transform of the unit rectangular distribution | 5 | Should |
| Riley | 12.5 | Fourier series of f(x) = x | 5 | Should |
| Riley | 26.5 | the quotient law | 10 | Should |
| Griffiths | 1.49 | integral of e^{-r} times the divergence of r-hat/r^2, by two methods | 3 | Could |
| Jackson | 1.2 | delta function in general orthogonal coordinates (limit of a Gaussian) | 2 | Could |
| Purcell | 2.26 ** | the delta function (solved in chapter 12) | 1 | Could |
| Riley | 13.26 | f(x) as an integral over the delta function | 1 | Could |
| Riley | 12.1 | orthogonality relations of Fourier series | 5 | Could |
| Riley | 26.9 | determinant identity with epsilon_ijk | 10 | Could |

## Derive from scratch

1. $\delta(f(x))=\sum\delta(x-x_i)/|f'(x_i)|$.
2. $\nabla^2(1/r)=-4\pi\delta^3(\mathbf r)$.
3. The Fourier transform of the Yukawa potential.

## Bare-minimum exercises (with expected results)

The numbers 6 to 8 are kept on purpose, so that references to exercises 9 and 10 elsewhere in the guide stay valid.

1. **Delta of a function:** $\delta(x^2-a^2)=\frac{\delta(x-a)+\delta(x+a)}{2|a|}$; $\int_0^{2\pi}f(x)\delta(\cos x)dx=f(\tfrac\pi2)+f(\tfrac{3\pi}2)$.
2. **Spherical delta:** check $\int\delta^3(\mathbf x-\mathbf x')d^3x=1$ using $d^3x=r^2dr\,d\cos\theta\,d\phi$ and the spherical form above.
3. **$\nabla^2(1/r)$:** $\nabla\frac1r=-\frac{\hat{\mathbf r}}{r^2}$; the flux through a sphere is $-4\pi$ for any radius, so $\nabla^2\frac1r=-4\pi\delta^3(\mathbf r)$.
4. **Point and moving charges:** write $\rho$ and $\mathbf J$ for a charge $q$ on the trajectory $\mathbf r(t)$ ($\mathbf J=q\mathbf v\,\delta^3(\mathbf x-\mathbf r(t))$) and show $\partial_t\rho+\nabla\cdot\mathbf J=0$.
5. **Fourier transform of a Gaussian:** $\int e^{-ax^2}e^{-ikx}dx=\sqrt{\frac\pi a}e^{-k^2/4a}$.
6. to 8. **Moved to the complex analysis guide.** Old exercise 6 (the integral $\int\frac{e^{ikx}}{k^2+m^2}dk$) is CA08 exercise 2, which is the same integral with $\cos kx$. Old exercise 7 (the real-axis poles with $\pm i\epsilon$) is CA08 exercise 6. Old exercise 8 (Sokhotski) is CA09 exercise 6.
9. **Yukawa and Coulomb:** $\int d^3x\,e^{-i\mathbf k\cdot\mathbf x}\frac{e^{-\mu r}}{r}=\frac{4\pi}{k^2+\mu^2}$ (use $\int_0^\infty\sin kr\,e^{-\mu r}dr=\frac{k}{k^2+\mu^2}$); take $\mu\to0$ to get the Coulomb transform $\frac{4\pi}{k^2}$.
10. **Index notation:** prove $\nabla\cdot(\mathbf A\times\mathbf B)=\mathbf B\cdot(\nabla\times\mathbf A)-\mathbf A\cdot(\nabla\times\mathbf B)$ and $\nabla\times(\nabla\times\mathbf A)=\nabla(\nabla\cdot\mathbf A)-\nabla^2\mathbf A$ with $\epsilon_{ijk}$.

## Optional extension

Derive the Green function of $-\frac{d^2}{dx^2}+m^2$ on the line by Fourier transform, $G(x)=\frac{1}{2m}e^{-m|x|}$, and check it directly: $G$ is continuous, $-G''+m^2G=0$ away from the origin, and $G'$ jumps by $-1$ at $x=0$. (The contour evaluation of the inverse transform is CA08 exercise 2.)

## Pitfalls

- Mixing Fourier conventions (factors of $2\pi$) between texts.
- Treating $\delta(f(x))$ as $\delta(x)$ without the Jacobian $1/|f'|$.

## Gate questions

1. Why is $\nabla^2(1/r)$ a delta function and not zero?
2. What does the Jacobian factor in $\delta(f(x))$ come from?

## One-page cheat sheet contents

Delta identities; $\delta^3$ in curvilinear coordinates; Fourier pairs; $\epsilon\epsilon$ identity.
