# Module 02: Math patch: delta functions, Fourier transforms, index notation

This file says **what to study and where**. The exercises live in separate files, one per session:

- `exercises/02_session_1_delta_basics_exercises.md`
- `exercises/02_session_2_three_dimensions_exercises.md`
- `exercises/02_session_3_fourier_and_index_notation_exercises.md`

## At a glance

- **Time:** 2 weeks, four sessions (three of work and one spare).
- **Session structure:** part A (read), then part B (exercises, in the exercise file of that session). About two and a half hours in all.
- **Pinned to:** Griffiths 5th ed. (2024), Jackson 3rd ed. (1999), Purcell and Morin 3rd ed. (2013, SI), Riley, Hobson and Bence 3rd ed. Page numbers are the printed book pages.
- **Moved out:** contour integration (Cauchy's theorem, residues, Jordan's lemma, closing contours, the $`\pm i\epsilon`$ prescription, the principal value and the Sokhotski formula). It is taught in the complex analysis guide (CA04 to CA09) and is first needed in Module 11.

## Books and sections (where to read)

**Griffiths (5th ed.), §1.5 The Dirac Delta Function, pp. 43 to 50**

- §1.5.1 the divergence of $`\hat r/r^2`$
- §1.5.2 the one-dimensional delta
- §1.5.3 the three-dimensional delta

**Jackson (3rd ed.), §1.2 Electric Field, p. 24**

- the delta-function treatment of point charges

**Riley, Hobson and Bence (3rd ed.)**

- §13.1 Fourier transforms, pp. 433 to 453: the Dirac $`\delta`$-function, its relation to Fourier transforms, convolution, Parseval, Fourier transforms in higher dimensions
- Chapter 12 Fourier series, pp. 415 to 426: §12.1 to §12.3 and §12.7
- Chapter 26 Tensors (index notation), pp. 928 to 944: §26.1 notation, §26.3 Cartesian tensors, §26.8 the tensors $`\delta_{ij}`$ and $`\epsilon_{ijk}`$
- ODE kit: §15.1 (p. 492) and §17.4 Sturm-Liouville (p. 564)

**Stewart is not enough here.**

## Why this matters

- **Delta-function calculus** gives $`\nabla^2\frac1r=-4\pi\delta^3(\mathbf r)`$ (Module 05) and the Lienard-Wiechert factor $`(1-\boldsymbol\beta\cdot\hat{\mathbf n})^{-1}`$ (Module 20).
- **Fourier transforms** turn differential equations into algebra.
- **Index notation** makes every vector identity a one-line proof.
- **ODE recipes** give the radial functions $`r^\ell`$, $`r^{-\ell-1}`$ and the Bessel and Legendre equations of Modules 06 to 08.

## Task 0: orientation (10 minutes)

Before Session 1, open Griffiths at p. 43, Jackson at p. 24 and Riley at p. 433 and check that the pages match what is pinned here. Note any mismatch in `notes/error_log.md`.

## Skip-test (closed book, your cheat sheet allowed, no clock)

Run this first. Log every item you miss: those items set how much time the module needs.

1. Show $`\delta(f(x))=\sum_i\frac{\delta(x-x_i)}{\lvert f'(x_i)\rvert}`$ and evaluate $`\delta(x^2-a^2)`$.
2. Write $`\delta^3(\mathbf x-\mathbf x')`$ in spherical coordinates and show that $`\int\delta^3\,d^3x=1`$.
3. Show $`\nabla^2\frac1r=-4\pi\delta^3(\mathbf r)`$ using the divergence theorem on a small sphere.
4. Compute the Fourier transform of $`e^{-ax^2}`$ and state the convolution theorem.
5. Prove $`\nabla\times(\nabla\times\mathbf A)=\nabla(\nabla\cdot\mathbf A)-\nabla^2\mathbf A`$ with $`\epsilon_{ijk}`$.

| Item you missed | Go to |
| --- | --- |
| 1 | Session 1 |
| 2 | Session 1 (exercise 2) |
| 3 | Session 2 (exercise 3) |
| 4 | Session 3 (exercise 5) |
| 5 | Session 3 (exercise 10) |

## Prerequisites

Module 01.

## Detailed topics (checklist)

**Delta-function calculus (Must)**

- Definition by $`\int f\delta=f(0)`$.
- Scaling: $`\delta(ax)=\delta(x)/\lvert a\rvert`$.
- Composition: $`\delta(f(x))=\sum_i\delta(x-x_i)/\lvert f'(x_i)\rvert`$.
- The derivative of the delta function; the step function $`\theta(x)`$ and $`\theta'=\delta`$.
- Three dimensions, spherical: $`\delta^3(\mathbf x-\mathbf x')=\frac{\delta(r-r')\,\delta(\theta-\theta')\,\delta(\phi-\phi')}{r^2\sin\theta}=\frac{\delta(r-r')\,\delta(\cos\theta-\cos\theta')\,\delta(\phi-\phi')}{r^2}`$.
- Three dimensions, cylindrical: the same with $`\rho`$ in place of $`r^2`$ in the denominator.
- $`\nabla^2\frac1r=-4\pi\delta^3`$.
- Point charge: $`\rho=q\,\delta^3(\mathbf x-\mathbf x_0)`$. Moving charge: $`\rho=q\,\delta^3(\mathbf x-\mathbf r(t))`$.

**Fourier transforms (Must)**

- Conventions (state yours): $`\tilde f(k)=\int f(x)e^{-ikx}\,dx`$ and $`f(x)=\int\frac{dk}{2\pi}\tilde f(k)e^{ikx}`$.
- Gaussian goes to Gaussian; derivative goes to multiplication by $`ik`$; the convolution theorem.
- The 3D transform of $`\frac1r`$ is $`\frac{4\pi}{k^2}`$; of the Yukawa potential $`\frac{e^{-\mu r}}r`$ it is $`\frac{4\pi}{k^2+\mu^2}`$.
- Fourier series on an interval (sine series).

**Index notation (Must)**

- Einstein summation, $`\delta_{ij}`$, $`\epsilon_{ijk}`$.
- $`\epsilon_{ijk}\epsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}`$.
- Vector identities proved in one line.

**ODE kit (Should; revisited in Modules 06 to 08)**

- $`y''+k^2y=0`$ ($`\sin,\cos`$) and $`y''-k^2y=0`$ ($`\sinh,\cosh`$ or $`e^{\pm kx}`$).
- The Euler equation $`r^2R''+2rR'-\ell(\ell+1)R=0`$ with solutions $`r^\ell`$ and $`r^{-\ell-1}`$.
- The Legendre and Bessel equations (names only).
- Sturm-Liouville eigenvalue problems and orthogonality (statement).

## Method card

**Delta of a function**

1. Find the zeros $`x_i`$.
2. Compute $`\lvert f'(x_i)\rvert`$ at each.
3. Write $`\sum_i\delta(x-x_i)/\lvert f'(x_i)\rvert`$.

## Reading plan (pinned to your editions)

### Session 1: delta function basics

**A: read**

- Task 0 (orientation).
- Griffiths §1.5.1 to §1.5.3 (pp. 43 to 50).

**B: do** → `exercises/02_session_1_delta_basics_exercises.md`

**Done when**

- you have read §1.5.1 to §1.5.3 and can say why $`\nabla\cdot(\hat r/r^2)`$ is $`4\pi\delta^3`$ and not zero
- the exercises of Session 1 are ticked off in their file

### Session 2: three dimensions and point charges

**A: read**

- Jackson §1.2 (p. 24).
- Griffiths §1.5.1 and §1.5.3 again, now with the 3D delta in mind.

**B: do** → `exercises/02_session_2_three_dimensions_exercises.md`

**Done when**

- the flux argument for $`\nabla^2\frac1r`$ is written on one page
- Jackson 1.3(a) agrees with your Griffiths 1.47(c)

### Session 3: Fourier transforms and index notation

**A: read**

- Riley §13.1 (pp. 433 to 453).
- Riley §26.1, §26.3, §26.8 (pp. 928 to 944).

**B: do** → `exercises/02_session_3_fourier_and_index_notation_exercises.md`

**Done when**

- the Gaussian transform and the Yukawa transform are done
- both index-notation identities are proved with $`\epsilon_{ijk}`$

### Session 4 (spare): ODE kit and consolidation

**A: read**

- ODE kit: Riley §15.1 (p. 492) and §17.4 (p. 564), read only.

**B: do**

- Redo the skip-test items you missed.
- Write the cheat sheet (contents below).

**Done when**

- the cheat sheet is written
- skip-test items 1 to 5 all pass

## Progress

- [ ] Task 0: pages checked
- [ ] Skip-test done, misses logged
- [ ] Session 1: read and exercises done
- [ ] Session 2: read and exercises done
- [ ] Session 3: read and exercises done
- [ ] Session 4: cheat sheet written, skip-test redone

## Problem set (pinned)

Master index of every book problem tied to this module. The session files tell you when to do each one.

- **Pin status:** Griffiths and Jackson sections and problems verified; Riley sections and exercises verified. Odd-numbered Riley exercises have worked solutions in the Student Solution Manual.
- **Tiers:**
  - **Must:** do all
  - **Should:** do when time allows
  - **Could:** only if the module is going well
- **Module exercise column:** the numbered exercise (in the session files) that the problem belongs to or supports.
- **Purcell and Morin:** stars give difficulty; problems are solved in its Chapter 12.

| Book | Problem | What it asks | Module exercise | Tier |
| --- | --- | --- | --- | --- |
| Griffiths | 1.44 | delta-function integrals (sifting property) | 1 | Must |
| Griffiths | 1.45 | delta-function integrals with $`\delta(3x)`$ and compositions | 1 | Must |
| Griffiths | 1.47 | charge densities with delta functions: point charge, dipole, spherical shell | 4 | Must |
| Jackson | 1.3 | charge distributions written with delta functions (shell, cylinder, disc) | 2 | Must |
| Riley | 13.1 | Fourier transform of $`e^{-\lvert t\rvert}`$ | 5 | Must |
| Riley | 13.5 | transform the equation $`\phi''-K^2\phi=f(x)`$: the screened-Poisson pattern | 9 | Must |
| Riley | 26.1 | Cartesian-tensor definition: basic properties | 10 | Must |
| Riley | 26.6 | vector identities by tensor methods (even number: no worked solution) | 10 | Must |
| Griffiths | 1.46 | $`x\,\frac{d}{dx}\delta(x)=-\delta(x)`$; the step function and the delta | 1 | Should |
| Griffiths | 1.48 | 3D delta-function integrals | 2 | Should |
| Griffiths | 1.64 | check that the Laplacian of $`1/r`$ is $`-4\pi\delta`$, another way | 3 | Should |
| Riley | 13.3 | Fourier transform of $`H(x-a)e^{-bx}`$ | 5 | Should |
| Riley | 13.7 | Fourier transform of the unit rectangular distribution | 5 | Should |
| Riley | 12.5 | Fourier series of $`f(x)=x`$ | 5 | Should |
| Riley | 26.5 | the quotient law | 10 | Should |
| Griffiths | 1.49 | integral of $`e^{-r}`$ times the divergence of $`\hat r/r^2`$, by two methods | 3 | Could |
| Jackson | 1.2 | delta function in general orthogonal coordinates (limit of a Gaussian) | 2 | Could |
| Purcell | 2.26 ** | the delta function (solved in chapter 12) | 1 | Could |
| Riley | 13.26 | $`f(x)`$ as an integral over the delta function | 1 | Could |
| Riley | 12.1 | orthogonality relations of Fourier series | 5 | Could |
| Riley | 26.9 | determinant identity with $`\epsilon_{ijk}`$ | 10 | Could |

## Pitfalls

- Mixing Fourier conventions (factors of $`2\pi`$) between texts.
- Treating $`\delta(f(x))`$ as $`\delta(x)`$ without the Jacobian $`1/\lvert f'\rvert`$.
- Writing "$`\int_V\nabla\cdot\mathbf F\,dV=-4\pi\delta`$": the delta is a statement about integrands, so it only appears *after* you have shown the integrals agree for every volume.
- Treating $`\theta`$ and $`\cos\theta`$ as the same variable in $`\delta(\theta-\theta')`$: they differ by a factor $`\sin\theta'`$.

## Gate questions

Answer in your own words, cheat sheet at hand.

1. Why is $`\nabla^2(1/r)`$ a delta function and not zero?
2. Where does the Jacobian factor in $`\delta(f(x))`$ come from?
3. Why does the flux of $`\hat r/r^2`$ not depend on the radius of the sphere?

## One-page cheat sheet contents

Delta identities; $`\delta^3`$ in curvilinear coordinates; Fourier pairs (Gaussian, Yukawa, Coulomb); the $`\epsilon\epsilon`$ identity.
