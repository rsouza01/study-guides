# Module 02: Math patch: delta functions, Fourier transforms, index notation

**Books:** Boas *Mathematical Methods in the Physical Sciences* (or Arfken, or Riley, Hobson and Bence): the chapters on Fourier series and transforms, and ordinary differential equations (Sturm-Liouville preview); Stewart is not enough here; Jackson 1.2 and its delta-function treatment; Griffiths 1.5 (the Dirac delta function).
**Time:** 3 weeks (six sessions).
**Moved out:** contour integration (Cauchy's theorem, residues, Jordan's lemma, closing contours, the $\pm i\epsilon$ prescription, the principal value and the Sokhotski formula) is no longer part of this module. It is taught in the complex analysis guide (CA04 to CA09) and is first needed in Module 11.

## Why this matters

Stewart does not cover these, and you need all of them. **Delta-function calculus** gives $\nabla^2\frac1r=-4\pi\delta^3(\mathbf r)$ (Module 05) and the Lienard-Wiechert factor $(1-\boldsymbol\beta\cdot\hat{\mathbf n})^{-1}$ (Module 20). **Fourier transforms** turn differential equations into algebra. **Index notation** makes every vector identity a one-line proof. **ODE recipes** give the radial functions $r^\ell$, $r^{-\ell-1}$ and the Bessel and Legendre equations of Modules 06 to 08.

## Task 0: build your reading map (30 minutes)

In `notes/reading_map.md` make a table: *Module, Jackson sections, Griffiths chapter, Purcell chapter, Stewart sections, done? (Y/N)*. Use the overview's module list as a first guess; fix section numbers against your copies. This map is the reference for the whole guide.

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

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Task 0; Griffiths 1.5; delta calculus drills (exercises 1 to 4) |
| B1 | Exercises 3 and 4; Jackson 1.2 |
| A2 | Boas: Fourier transforms; the Gaussian and Yukawa transforms |
| B2 | Exercises 5 and 9; index notation |
| A3 | Exercise 10; ODE kit; cheat sheet |
| B3 | Spare session: redo the failed items of the skip-test |

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
