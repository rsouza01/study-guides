# Module 07: Spherical harmonics and Green function expansions (★★: the technique of the whole guide)

**Books:** Jackson 3.5 (associated Legendre functions and $Y_{\ell m}$), 3.6 (the addition theorem: **memorise the statement**), **3.9 (expansion of Green functions in spherical coordinates)**, **3.10 (solving potential problems with it)**; Griffiths 3.4 (multipole expansion, for the physical reading); Boas or Arfken for $Y_{\ell m}$ background.
**Time:** 3 weeks (six sessions). **If you master one technique in this whole guide, make it the radial Green function construction.**

## Why this matters

Completeness of $\{Y_{\ell m}\}$ resolves the identity on the sphere. That single fact *is* the partial-wave decomposition of a scattering amplitude and *is* the decomposition of a field into irreducible representations of $SO(3)$. Jackson reduces $\nabla^2G=-4\pi\delta^3$ to a set of 1D ODEs for $g_\ell(r,r')$; solves each by taking the homogeneous solution regular at the inner end and the one regular at the outer end; and fixes the normalization by **integrating the ODE across $r=r'$ to get a jump condition on the derivative**, expressed through the Wronskian. That procedure, *homogeneous solutions on either side glued by a discontinuity whose size the delta function sets*, is exactly how the radial Klein-Gordon and Dirac Green functions are built, how partial-wave amplitudes are constructed, and it is structurally identical to the time-ordered propagator with $t\lessgtr t'$ replacing $r\lessgtr r'$.

## Skip-test (40 minutes, no notes)

1. Write $Y_{00}$, $Y_{10}$, $Y_{11}$, and state orthonormality and completeness of $Y_{\ell m}$.
2. State the addition theorem $P_\ell(\cos\gamma)=\frac{4\pi}{2\ell+1}\sum_mY^*_{\ell m}(\theta',\phi')Y_{\ell m}(\theta,\phi)$ and use it to derive $\frac{1}{|\mathbf x-\mathbf x'|}=4\pi\sum_{\ell m}\frac{1}{2\ell+1}\frac{r_<^\ell}{r_>^{\ell+1}}Y^*_{\ell m}(\theta',\phi')Y_{\ell m}(\theta,\phi)$.
3. Construct $g_\ell(r,r')$ for free space *from scratch*: radial ODE, homogeneous solutions $r^\ell$ and $r^{-(\ell+1)}$, regularity at $0$ and $\infty$, integrate across $r=r'$, fix the coefficient. Then repeat between two concentric spheres.
4. Define the multipole moments $q_{\ell m}=\int Y^*_{\ell m}r'^\ell\rho\,d^3x'$ and show that $\ell=0,1$ give the total charge and the dipole.
5. State how $\sum_m|Y_{\ell m}|^2=\frac{2\ell+1}{4\pi}$ follows from the addition theorem.

## Prerequisites

Modules 05 and 06 (Green functions, Legendre polynomials).

## Detailed topics (checklist)

**Associated Legendre functions and $Y_{\ell m}$ (3.5) [Must]**
- $Y_{\ell m}(\theta,\phi)=\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-m)!}{(\ell+m)!}}P_\ell^m(\cos\theta)e^{im\phi}$; $Y_{\ell,-m}=(-1)^mY^*_{\ell m}$; examples $Y_{00}=\frac1{\sqrt{4\pi}}$, $Y_{10}=\sqrt{\frac3{4\pi}}\cos\theta$, $Y_{1\pm1}=\mp\sqrt{\frac3{8\pi}}\sin\theta e^{\pm i\phi}$; orthonormality $\int Y^*_{\ell m}Y_{\ell'm'}d\Omega=\delta_{\ell\ell'}\delta_{mm'}$; completeness $\sum_{\ell m}Y^*_{\ell m}(\Omega')Y_{\ell m}(\Omega)=\delta(\phi-\phi')\delta(\cos\theta-\cos\theta')$; general solution of Laplace's equation $\Phi=\sum_{\ell m}\left(A_{\ell m}r^\ell+B_{\ell m}r^{-(\ell+1)}\right)Y_{\ell m}$.

**The addition theorem (3.6) [Must]**
- $P_\ell(\cos\gamma)=\frac{4\pi}{2\ell+1}\sum_{m=-\ell}^\ell Y^*_{\ell m}(\theta',\phi')Y_{\ell m}(\theta,\phi)$ with $\cos\gamma=\cos\theta\cos\theta'+\sin\theta\sin\theta'\cos(\phi-\phi')$; the expansion of $\frac{1}{|\mathbf x-\mathbf x'|}$.

**Green function expansions (3.9 to 3.10) [Must]**
- $G(\mathbf x,\mathbf x')=\sum_{\ell m}g_\ell(r,r')Y^*_{\ell m}(\Omega')Y_{\ell m}(\Omega)$ with $\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{dg_\ell}{dr}\right)-\frac{\ell(\ell+1)}{r^2}g_\ell=-\frac{4\pi}{r^2}\delta(r-r')$.
- **The construction:** $g_\ell=C\,u_1(r_<)u_2(r_>)$ with $u_1=r^\ell$ (regular at $0$) and $u_2=r^{-(\ell+1)}$ (regular at $\infty$); continuity at $r=r'$; the **jump condition** $\left.\frac{dg}{dr}\right|_{r'^+}-\left.\frac{dg}{dr}\right|_{r'^-}=-\frac{4\pi}{r'^2}$ gives $C=-\frac{4\pi}{r'^2W}$ with the Wronskian $W=u_1u_2'-u_1'u_2=-\frac{2\ell+1}{r^2}$, so $g_\ell=\frac{4\pi}{2\ell+1}\frac{r_<^\ell}{r_>^{\ell+1}}$.
- **Between concentric spheres** $a<r<b$ (Dirichlet): $g_\ell=\frac{4\pi}{(2\ell+1)\left[1-(a/b)^{2\ell+1}\right]}\left(r_<^\ell-\frac{a^{2\ell+1}}{r_<^{\ell+1}}\right)\left(\frac{1}{r_>^{\ell+1}}-\frac{r_>^\ell}{b^{2\ell+1}}\right)$; the sphere with a point charge inside recovers the image result.
- **Multipoles (preview of 4.1):** reading the expansion backwards, outside the charges $\Phi=\frac1{\epsilon_0}\sum_{\ell m}\frac{1}{2\ell+1}\frac{q_{\ell m}}{r^{\ell+1}}Y_{\ell m}$ with $q_{\ell m}=\int Y^*_{\ell m}r'^\ell\rho\,d^3x'$.

## Method card

**Radial Green function:** (1) expand the delta function and $G$ in $Y_{\ell m}$; (2) write the radial ODE with $-\frac{4\pi}{r^2}\delta(r-r')$; (3) pick the two homogeneous solutions satisfying the boundary condition at each end (regular at $0$ or vanishing at $a$; regular at $\infty$ or vanishing at $b$); (4) glue them, $g=Cu_1(r_<)u_2(r_>)$, so the solution is continuous automatically; (5) integrate the ODE across $r'$ to fix $C$ through the Wronskian; (6) check the free-space limit $\frac{4\pi}{2\ell+1}\frac{r_<^\ell}{r_>^{\ell+1}}$ and the symmetry in $r\leftrightarrow r'$.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Jackson 3.5; explicit $Y_{\ell m}$ (exercises 1 and 2) |
| B1 | Exercises 1 to 3 |
| A2 | Jackson 3.6; the addition theorem and the $1/|\mathbf x-\mathbf x'|$ expansion |
| B2 | Exercises 3 and 4 |
| A3 | Jackson 3.9; **read the "Why" paragraph above before starting**; construct $g_\ell$ |
| B3 | Exercises 5 and 6 |
| A4 | Jackson 3.10; the concentric-sphere case |
| B4 | Exercises 7 to 9 |
| A5 | **Jackson target** (exercise 10); redo the free-space construction from a blank page |
| B5 | Spare session |

## Derive from scratch

1. The addition-theorem consequence $\sum_m|Y_{\ell m}|^2=\frac{2\ell+1}{4\pi}$.
2. The free-space $g_\ell$ with the jump condition and the Wronskian.
3. $g_\ell$ between two concentric spheres.
4. The multipole moments $q_{\ell m}$ and the identification of $\ell=0,1$.
5. The expansion $\frac{1}{|\mathbf x-\mathbf x'|}=4\pi\sum\frac{1}{2\ell+1}\frac{r_<^\ell}{r_>^{\ell+1}}Y^*Y$.

## Bare-minimum exercises (with expected results)

1. **Explicit harmonics:** verify $\int|Y_{10}|^2d\Omega=1$ with $Y_{10}=\sqrt{\frac{3}{4\pi}}\cos\theta$ and that $Y_{1,-1}=-Y_{11}^*$; write $Y_{20}=\sqrt{\frac5{16\pi}}(3\cos^2\theta-1)$.
2. **Orthogonality:** check $\int Y^*_{11}Y_{10}d\Omega=0$ and $\int Y_{00}^*Y_{10}d\Omega=0$.
3. **Addition theorem at $\ell=1$:** $\cos\gamma=\frac{4\pi}{3}\sum_{m}Y^*_{1m}(\Omega')Y_{1m}(\Omega)$ reproduces $\cos\theta\cos\theta'+\sin\theta\sin\theta'\cos(\phi-\phi')$.
4. **Sum rule:** setting $\gamma=0$ in the addition theorem gives $\sum_m|Y_{\ell m}|^2=\frac{2\ell+1}{4\pi}$; check $\ell=1$.
5. **Free-space radial Green function:** carry out the construction with the jump condition and show $g_\ell=\frac{4\pi}{2\ell+1}\frac{r_<^\ell}{r_>^{\ell+1}}$; verify it reproduces $\frac{1}{|\mathbf x-\mathbf x'|}$ for $\mathbf x\parallel\mathbf x'$ ($\gamma=0$) by summing the geometric series $\sum(r_</r_>)^\ell\frac{1}{r_>}$.
6. **Concentric spheres:** show that the Green function with $G=0$ at $r=a$ and $r=b$ has the $g_\ell$ above, and that $b\to\infty$ gives $\frac{4\pi}{2\ell+1}\left[\frac{r_<^\ell}{r_>^{\ell+1}}-\frac{a^{2\ell+1}}{(rr')^{\ell+1}}\right]$, i.e. the exterior-sphere image result.
7. **Point charge in a grounded sphere:** on the axis ($\mathbf x'=z_0\hat{\mathbf z}$) the potential is $\Phi=\frac{q}{4\pi\epsilon_0}\left[\frac1{|\mathbf x-\mathbf x'|}-\frac{a}{z_0|\mathbf x-\frac{a^2}{z_0^2}\mathbf x'|}\right]$; from $g_\ell$ show the induced charge is $-q$ for $z_0<a$ and compare with the image charge.
8. **Multipole moments:** $q_{00}=\frac{Q}{\sqrt{4\pi}}$; for a point charge $q$ on the $z$ axis at $z_0$, $q_{\ell0}=q\sqrt{\frac{2\ell+1}{4\pi}}z_0^\ell$ and $q_{\ell m}=0$ for $m\neq0$; reconstruct the far potential $\Phi=\frac{q}{4\pi\epsilon_0}\sum\frac{z_0^\ell}{r^{\ell+1}}P_\ell(\cos\theta)$ ($r>z_0$).
9. **Dipole from $q_{1m}$:** two charges $\pm q$ at $z=\pm\frac d2$ give $q_{10}=\sqrt{\frac3{4\pi}}qd$ and a potential $\frac{qd\cos\theta}{4\pi\epsilon_0r^2}$: Module 03's dipole.
10. **Jackson target (about 3.6 and the radial Green function):** (a) construct $g_\ell(r,r')$ for free space and between concentric spheres from scratch (the **blank-page gate**); (b) a charge distribution on a sphere's inside or outside with a grounded sphere present (Jackson about 3.6): use the sphere Green function and compute the potential and the charge induced on the sphere.

## Optional extension

Use the expansion to compute the electrostatic energy of interaction of two charge distributions in terms of their multipole moments, $U\sim\frac{q_{\ell m}Q^*_{\ell m}}{R^{\ell+\ell'+1}}$-type terms (Jackson 4.2 preview), and recover the dipole-dipole formula.

## Pitfalls

- Using the interior series ($r^\ell$) outside the region it is regular in.
- Forgetting the $\frac{4\pi}{2\ell+1}$ factor or putting $4\pi$ in the wrong place (QFT texts carry no $4\pi$: note the offset once).
- Applying the jump condition with the wrong sign (the derivative decreases across $r'$).
- Using the Wronskian at a point other than $r'$ (it is $r$-dependent).

## Gate questions

1. Why does the jump condition appear, and what sets its size?
2. Why are the two homogeneous solutions chosen as they are at each end?
3. How is this construction structurally the same as $t\lessgtr t'$ in the time-ordered propagator?

## One-page cheat sheet contents

$Y_{\ell m}$ list; orthonormality and completeness; addition theorem; the radial Green function recipe with the Wronskian; the concentric-sphere $g_\ell$; multipole moments.
