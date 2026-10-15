# Module 02: Math patch: delta functions, contour integrals, Fourier transforms, index notation

**Books:** Boas *Mathematical Methods in the Physical Sciences* (or Arfken): the chapters on complex variables and residues, Fourier series and transforms, and ordinary differential equations (Sturm-Liouville preview); Stewart is not enough here; Jackson 1.2 and its delta-function treatment; Griffiths 1.5 (the Dirac delta function).
**Time:** 2 weeks (four sessions).

## Why this matters

Stewart does not cover these, and you need all of them. **Delta-function calculus** gives $\nabla^2\frac1r=-4\pi\delta^3(\mathbf r)$ (Module 05) and the Lienard-Wiechert factor $(1-\boldsymbol\beta\cdot\hat{\mathbf n})^{-1}$ (Module 20). **Contour integration is the single highest-leverage item in the prelude:** the retarded, advanced and Feynman propagators are *nothing but* which way you go around a pole, and Modules 11 and 19 collapse without it. **Fourier transforms** turn differential equations into algebra. **Index notation** makes every vector identity a one-line proof. **ODE recipes** give the radial functions $r^\ell$, $r^{-\ell-1}$ and the Bessel and Legendre equations of Modules 06 to 08.

## Task 0: build your reading map (30 minutes)

In `notes/reading_map.md` make a table: *Module, Jackson sections, Griffiths chapter, Purcell chapter, Stewart sections, done? (Y/N)*. Use the overview's module list as a first guess; fix section numbers against your copies. This map is the reference for the whole guide.

## Skip-test (40 minutes, no notes)

1. Show $\delta(f(x))=\sum_i\frac{\delta(x-x_i)}{|f'(x_i)|}$ and evaluate $\delta(x^2-a^2)$.
2. Write $\delta^3(\mathbf x-\mathbf x')$ in spherical coordinates and show that $\int\delta^3d^3x=1$.
3. Show $\nabla^2\frac1r=-4\pi\delta^3(\mathbf r)$ using the divergence theorem on a small sphere.
4. Evaluate $\int_{-\infty}^\infty\frac{e^{ikx}}{k^2+m^2}dk$ and $\int_{-\infty}^\infty\frac{e^{ikx}}{k^2-m^2\pm i\epsilon}dk$ by closing the contour.
5. Write $\frac1{x\pm i\epsilon}$ in terms of the principal value and a delta function.

## Prerequisites

Module 01.

## Detailed topics (checklist)

**Delta-function calculus [Must]**
- Definition by $\int f\delta=f(0)$; $\delta(ax)=\delta(x)/|a|$; $\delta(f(x))=\sum_i\delta(x-x_i)/|f'(x_i)|$; derivative of the delta function; the step function $\theta(x)$ and $\theta'=\delta$.
- Three dimensions: $\delta^3(\mathbf x-\mathbf x')=\frac{\delta(r-r')\delta(\theta-\theta')\delta(\phi-\phi')}{r^2\sin\theta}=\frac{\delta(r-r')\delta(\cos\theta-\cos\theta')\delta(\phi-\phi')}{r^2}$ (and the cylindrical analogue with $\rho$); $\nabla^2\frac1r=-4\pi\delta^3$; the charge density of a point charge $\rho=q\delta^3(\mathbf x-\mathbf x_0)$ and of a *moving* charge $\rho=q\delta^3(\mathbf x-\mathbf r(t))$.

**Complex analysis [Must]**
- Cauchy's theorem, residues, Jordan's lemma, closing contours; **poles on the real axis** and the $\pm i\epsilon$ prescription; the principal value; the Sokhotski formula $\frac1{x\pm i\epsilon}=\mathrm P\frac1x\mp i\pi\delta(x)$.
- Standard results: $\int_{-\infty}^\infty\frac{e^{ikx}}{k^2+m^2}dk=\frac{\pi}{m}e^{-m|x|}$; for the real-axis poles, $\int\frac{e^{ikx}}{k^2-m^2+i\epsilon}dk=-\frac{i\pi}{m}e^{-im|x|}$ and with $-i\epsilon$ it is $+\frac{i\pi}{m}e^{+im|x|}$.

**Fourier transforms [Must]**
- Conventions (state yours): $\tilde f(k)=\int f(x)e^{-ikx}dx$, $f(x)=\int\frac{dk}{2\pi}\tilde f(k)e^{ikx}$; Gaussian $\to$ Gaussian; derivative $\to$ multiplication by $ik$; convolution theorem; the 3D transform of $\frac1r$ ($\frac{4\pi}{k^2}$) and of the Yukawa potential $\frac{e^{-\mu r}}r$ ($\frac{4\pi}{k^2+\mu^2}$); Fourier series on an interval (sine series).

**Index notation [Must]**
- Einstein summation, $\delta_{ij}$, $\epsilon_{ijk}$; $\epsilon_{ijk}\epsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}$; proofs of vector identities in one line.

**ODE kit [Should; revisited in Modules 06 to 08]**
- $y''+k^2y=0$ ($\sin,\cos$), $y''-k^2y=0$ ($\sinh,\cosh$ or $e^{\pm kx}$); the Euler equation $r^2R''+2rR'-\ell(\ell+1)R=0$ with solutions $r^\ell$ and $r^{-\ell-1}$; the Legendre and Bessel equations (names only); Sturm-Liouville eigenvalue problems and orthogonality (statement).

## Method cards

**Closing a contour:** (1) write the integrand $e^{ikx}g(k)$; (2) for $x>0$ close in the upper half plane (where $e^{ikx}$ decays), for $x<0$ in the lower; (3) find the poles inside, with $\pm i\epsilon$ telling you which side of the axis each lies on; (4) sum $2\pi i\times$ residues (counterclockwise) or $-2\pi i\times$ (clockwise, lower half plane); (5) check $x\to0$ and the symmetric case.
**Delta of a function:** (1) find the zeros $x_i$; (2) compute $|f'(x_i)|$; (3) $\sum\delta(x-x_i)/|f'(x_i)|$.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Task 0; Griffiths 1.5; delta calculus drills (exercises 1 to 4) |
| B1 | Exercises 3 and 4; Jackson 1.2 |
| A2 | Boas: complex integration and residues; the method card |
| B2 | Exercises 6 to 7 |
| A3 | Boas: Fourier transforms; the Gaussian and Yukawa transforms |
| B3 | Exercises 5, 8, 9; index notation |
| A4 | Exercise 10; ODE kit; cheat sheet |
| B4 | Spare session: redo the failed items of the skip-test |

## Derive from scratch

1. $\delta(f(x))=\sum\delta(x-x_i)/|f'(x_i)|$.
2. $\nabla^2(1/r)=-4\pi\delta^3(\mathbf r)$.
3. The two contour integrals above, including which poles are enclosed.
4. $\frac{1}{x\pm i\epsilon}=\mathrm P\frac1x\mp i\pi\delta(x)$.
5. The Fourier transform of the Yukawa potential.

## Bare-minimum exercises (with expected results)

1. **Delta of a function:** $\delta(x^2-a^2)=\frac{\delta(x-a)+\delta(x+a)}{2|a|}$; $\int_0^{2\pi}f(x)\delta(\cos x)dx=f(\tfrac\pi2)+f(\tfrac{3\pi}2)$.
2. **Spherical delta:** check $\int\delta^3(\mathbf x-\mathbf x')d^3x=1$ using $d^3x=r^2dr\,d\cos\theta\,d\phi$ and the spherical form above.
3. **$\nabla^2(1/r)$:** $\nabla\frac1r=-\frac{\hat{\mathbf r}}{r^2}$; the flux through a sphere is $-4\pi$ for any radius, so $\nabla^2\frac1r=-4\pi\delta^3(\mathbf r)$.
4. **Point and moving charges:** write $\rho$ and $\mathbf J$ for a charge $q$ on the trajectory $\mathbf r(t)$ ($\mathbf J=q\mathbf v\,\delta^3(\mathbf x-\mathbf r(t))$) and show $\partial_t\rho+\nabla\cdot\mathbf J=0$.
5. **Fourier transform of a Gaussian:** $\int e^{-ax^2}e^{-ikx}dx=\sqrt{\frac\pi a}e^{-k^2/4a}$.
6. **Contour:** $\int_{-\infty}^\infty\frac{e^{ikx}}{k^2+m^2}dk=\frac\pi me^{-m|x|}$ (poles at $\pm im$).
7. **Real-axis poles:** with $+i\epsilon$ the poles sit at $\pm(m-i\epsilon')$; closing up for $x>0$ encloses $k=-m+i\epsilon'$ and gives $-\frac{i\pi}{m}e^{-imx}$; for $x<0$ close down and find $-\frac{i\pi}{m}e^{+imx}$, i.e. $-\frac{i\pi}me^{-im|x|}$ for both. With $-i\epsilon$ the result is $+\frac{i\pi}me^{+im|x|}$. *Keep this page.*
8. **Sokhotski:** verify $\int\frac{f(x)}{x\pm i\epsilon}dx\to\mathrm P\!\!\int\frac{f}{x}\mp i\pi f(0)$ with $f=e^{-x^2}$.
9. **Yukawa and Coulomb:** $\int d^3x\,e^{-i\mathbf k\cdot\mathbf x}\frac{e^{-\mu r}}{r}=\frac{4\pi}{k^2+\mu^2}$ (use $\int_0^\infty\sin kr\,e^{-\mu r}dr=\frac{k}{k^2+\mu^2}$); take $\mu\to0$ to get the Coulomb transform $\frac{4\pi}{k^2}$.
10. **Index notation:** prove $\nabla\cdot(\mathbf A\times\mathbf B)=\mathbf B\cdot(\nabla\times\mathbf A)-\mathbf A\cdot(\nabla\times\mathbf B)$ and $\nabla\times(\nabla\times\mathbf A)=\nabla(\nabla\cdot\mathbf A)-\nabla^2\mathbf A$ with $\epsilon_{ijk}$.

## Optional extension

Derive the Green function of $-\frac{d^2}{dx^2}+m^2$ on the line by Fourier transform, $G(x)=\frac{1}{2m}e^{-m|x|}$, and compare with the contour result of exercise 6: the same object, two derivations.

## Pitfalls

- Closing the contour on the wrong side (check where $e^{ikx}$ decays).
- Forgetting that real-axis poles make the integral undefined until you choose $\pm i\epsilon$.
- Mixing Fourier conventions (factors of $2\pi$) between texts.
- Treating $\delta(f(x))$ as $\delta(x)$ without the Jacobian $1/|f'|$.

## Gate questions

1. Why does the choice of contour correspond to a physical boundary condition?
2. Why is $\nabla^2(1/r)$ a delta function and not zero?
3. What does the Jacobian factor in $\delta(f(x))$ come from?

## One-page cheat sheet contents

Delta identities; $\delta^3$ in curvilinear coordinates; residue recipe and the three standard contour integrals; Sokhotski; Fourier pairs; $\epsilon\epsilon$ identity.
