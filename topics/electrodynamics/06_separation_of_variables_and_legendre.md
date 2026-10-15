# Module 06: Separation of variables, orthogonal functions and Legendre polynomials

**Books:** Griffiths 3.3 (separation of variables: Cartesian and spherical; the engine) and 3.1 to 3.2 for background; Jackson 2.8 (orthogonal functions and expansions: *sets up the whole of Months 2 to 3*), 2.9 to 2.10 (separation in rectangular coordinates; a two-dimensional problem), 3.1 to 3.3 (Laplace's equation in spherical coordinates, Legendre polynomials, azimuthal symmetry). (Your roadmap listed a "hemispheres" section at 2.7; in the 3rd edition the hemisphere problem is Problem 3.1: verify against your copy.) Skip Jackson 2.11, 2.12 and 3.4.
**Time:** 3 weeks (six sessions). **Tier note:** if diagnostic problem 6 is right, still do the Jackson targets.

## Why this matters

Separation of variables turns a PDE into ODEs whose solutions are **orthogonal function sets**; expanding the boundary data in that set solves the problem. The **regularity argument** that quantizes $\ell$ (the Legendre equation has a solution regular at $\theta=0,\pi$ only for integer $\ell$) is the same argument that quantizes angular momentum in quantum mechanics: watch for it. The completeness of orthogonal sets is the idea behind every Green function expansion in the next modules.

## Skip-test (40 minutes, no notes)

1. Solve $\nabla^2\Phi=0$ in the rectangle $0<x<a$, $0<y<b$ with $\Phi=V_0$ on $y=b$ and $0$ on the other three sides.
2. Expand $f(x)=1$ on $(0,a)$ in a sine series.
3. Separate Laplace's equation in spherical coordinates with azimuthal symmetry; write the radial solutions $r^\ell$, $r^{-(\ell+1)}$ and state the Legendre equation.
4. State the orthogonality relation of $P_\ell(x)$ and the generating function $\frac{1}{\sqrt{1-2xt+t^2}}=\sum t^\ell P_\ell(x)$; write $P_0,\dots,P_3$.
5. State the regularity argument that forces $\ell$ to be an integer.

## Prerequisites

Modules 02 (ODE kit), 04, 05.

## Detailed topics (checklist)

**Orthogonal functions (2.8) [Must]**
- Orthogonality and completeness of $\{\sin\frac{n\pi x}a\}$ and $\{e^{ikx}\}$; Fourier series; expansion of a given function; Parseval (statement); the Gibbs phenomenon (awareness).

**Rectangular coordinates (2.9 to 2.10) [Must]**
- $\Phi=X(x)Y(y)Z(z)$; separation constants $\alpha^2+\beta^2=\gamma^2$; choosing $\sin/\cos$ versus $\sinh/\cosh$ from the boundary conditions; homogeneous conditions give the eigenvalues; the inhomogeneous condition is expanded in the orthogonal set; summation of the series (2.10, awareness).

**Spherical coordinates and Legendre polynomials (3.1 to 3.3) [Must]**
- $\Phi=\frac{U(r)}rP(\theta)Q(\phi)$; Legendre's equation $\frac{d}{dx}\left[(1-x^2)\frac{dP}{dx}\right]+\ell(\ell+1)P=0$; polynomial solutions $P_\ell$ (Rodrigues' formula $P_\ell=\frac{1}{2^\ell\ell!}\frac{d^\ell}{dx^\ell}(x^2-1)^\ell$); orthogonality $\int_{-1}^1P_\ell P_{\ell'}dx=\frac{2}{2\ell+1}\delta_{\ell\ell'}$; the generating function.
- Azimuthal symmetry: $\Phi=\sum_\ell\left(A_\ell r^\ell+B_\ell r^{-(\ell+1)}\right)P_\ell(\cos\theta)$; matching a boundary value $\Phi(a,\theta)=\sum\ldots$; the **axis-matching trick**: if $\Phi(0,0,z)$ is known, the full potential is obtained by replacing $z^{-\ell-1}\to r^{-\ell-1}P_\ell(\cos\theta)$ term by term.
- **The regularity argument:** the series solution of the Legendre equation diverges at $x=\pm1$ unless it terminates, i.e. unless $\ell$ is a non-negative integer. Quantization comes from *regularity*, not from an extra postulate.

## Method cards

**Separation of variables:** (1) pick coordinates matching the boundaries; (2) write $\Phi=X(x)Y(y)Z(z)$ and divide through; (3) assign separation constants with signs chosen so that the directions with homogeneous conditions oscillate ($\sin$, $\cos$) and the other grows ($\sinh$, $e^{\pm}$); (4) impose the homogeneous boundary conditions to quantize the constants; (5) superpose, impose the remaining condition and project with orthogonality; (6) check symmetry, limits and special points.
**Axis matching:** (1) compute $\Phi$ on the symmetry axis by direct integration; (2) expand in powers of $1/z$ (outside) or $z$ (inside); (3) multiply each power by $P_\ell(\cos\theta)$ and replace $z\to r$.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Jackson 2.8; Fourier sine series (exercise 1) |
| B1 | Exercises 1 and 2 |
| A2 | Griffiths 3.3.1 and Jackson 2.9 to 2.10 (rectangular separation) |
| B2 | Exercise 3 and **Jackson target (a)** (hollow cube) |
| A3 | Griffiths 3.3.2; Jackson 3.1 to 3.2 (Legendre) |
| B3 | Exercises 4 and 5 |
| A4 | Jackson 3.3 (azimuthal symmetry); axis matching |
| B4 | Exercises 6 to 8 |
| A5 | **Jackson target (b)**; the regularity argument |
| B5 | Exercises 9 and 10; spare |

## Derive from scratch

1. The separation of Laplace's equation in Cartesian coordinates and the choice of $\sin/\sinh$.
2. The Legendre equation by separation in spherical coordinates, with the regularity argument.
3. $\int_{-1}^1P_\ell P_{\ell'}dx=\frac{2}{2\ell+1}\delta_{\ell\ell'}$ (from the self-adjoint form of the equation).
4. The generating function and $\frac1{|\mathbf x-\mathbf x'|}=\sum_\ell\frac{r_<^\ell}{r_>^{\ell+1}}P_\ell(\cos\gamma)$.
5. The sphere with hemispheres at $\pm V$: the first two nonzero coefficients.

## Bare-minimum exercises (with expected results)

1. **Fourier sine series:** $1=\frac4\pi\sum_{n\,{\rm odd}}\frac1n\sin\frac{n\pi x}{a}$ on $(0,a)$; sketch partial sums and the overshoot.
2. **The box:** $\Phi=\frac{4V_0}{\pi}\sum_{n\,{\rm odd}}\frac1n\sin\frac{n\pi x}{a}\frac{\sinh(n\pi y/a)}{\sinh(n\pi b/a)}$; check the three grounded sides and the limit $y\to b$.
3. **Hollow-cube check:** five faces grounded and the top at $V$: by superposition of six such problems, the potential at the centre is $\frac{V}{6}$ (each face contributes equally to the centre when the total is $V$ for all six at $V$). The series is $\Phi=\frac{16V}{\pi^2}\sum_{n,m\,{\rm odd}}\frac{1}{nm}\sin\frac{n\pi x}a\sin\frac{m\pi y}a\frac{\sinh(\gamma_{nm}z)}{\sinh(\gamma_{nm}a)}$ with $\gamma_{nm}=\frac{\pi}{a}\sqrt{n^2+m^2}$; verify the leading term at the centre is consistent with $\frac V6$ (the first few terms give about $0.1666V$).
4. **Legendre polynomials:** $P_0=1$, $P_1=x$, $P_2=\frac12(3x^2-1)$, $P_3=\frac12(5x^3-3x)$ from Rodrigues; check $\int_{-1}^1P_1P_2=0$ and $\int_{-1}^1P_2^2=\frac25$.
5. **Generating function:** expand $\frac1{\sqrt{1-2xt+t^2}}$ to $t^3$ and read off $P_0$ to $P_3$; deduce $\frac{1}{|\mathbf x-\mathbf x'|}=\sum_\ell\frac{r'^\ell}{r^{\ell+1}}P_\ell(\cos\gamma)$ for $r>r'$ (your Module 01 extra, now complete).
6. **Hemispheres (Jackson 3.1):** for a sphere with the upper hemisphere at $+V$ and the lower at $-V$, the interior potential is $\Phi=V\left[\frac32\frac ra P_1-\frac78\left(\frac ra\right)^3P_3+\frac{11}{16}\left(\frac ra\right)^5P_5-\dots\right]$ (compute $A_1,A_3$ from $\int_0^1P_\ell(x)dx$).
7. **Sphere with $\Phi(a,\theta)=V_0\cos\theta$:** inside $\Phi=V_0\frac ra\cos\theta$ (uniform field), outside $\Phi=V_0\frac{a^2}{r^2}\cos\theta$ (a dipole); the surface charge is $\sigma=\frac{3\epsilon_0V_0}a\cos\theta$.
8. **Axis matching:** a ring of charge $Q$, radius $a$: on the axis $\Phi=\frac{Q}{4\pi\epsilon_0\sqrt{z^2+a^2}}$; expanding gives $\Phi(r,\theta)=\frac{Q}{4\pi\epsilon_0}\sum_{\ell\,{\rm even}}\frac{a^\ell}{r^{\ell+1}}P_\ell(0)P_\ell(\cos\theta)$ (since $P_\ell(0)=0$ for odd $\ell$ and $P_2(0)=-\frac12$).
9. **Conducting sphere in a uniform field:** show by separation that $\Phi=-E_0\left(r-\frac{a^3}{r^2}\right)\cos\theta$ for $r>a$, with induced $\sigma=3\epsilon_0E_0\cos\theta$ (compare with Module 04 exercise 8: same answer, different route).
10. **Regularity and quantization:** show that a power-series solution of Legendre's equation has the recursion $a_{k+2}=\frac{k(k+1)-\ell(\ell+1)}{(k+1)(k+2)}a_k$ and that it terminates only for integer $\ell$; otherwise it behaves like $\ln(1-x)$ at $x=1$.

## Optional extension

Solve the same box problem by relaxation (Gauss-Seidel) on a grid and compare with the series; study the Gibbs overshoot near the corners.

## Pitfalls

- Picking $\sin$ versus $\sinh$ without looking at which boundaries are homogeneous.
- Forgetting the normalization $\frac{2}{2\ell+1}$ when extracting coefficients.
- Using interior series for an exterior problem (the $B_\ell$ terms must vanish inside and the $A_\ell$ terms outside).
- Treating the $\ell$-quantization as an assumption (it is regularity).

## Gate questions

1. Why does regularity at $\theta=0,\pi$ force $\ell\in\mathbb N$?
2. Why must you use the *homogeneous* boundary conditions first?
3. What does completeness of $\{P_\ell\}$ let you do with an arbitrary boundary value?

## One-page cheat sheet contents

Separation recipe; Legendre polynomials and orthogonality; generating function; the azimuthally symmetric general solution; axis matching; the box and hemispheres results.
