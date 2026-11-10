# Module 05: Green functions for the Poisson equation (★, thread A begins)

**Books:** Jackson 1.8 Green's Theorem (pp. 35 to 37: **slow down, read three times**), 1.10 Formal Solution of the Electrostatic Boundary-Value Problem with Green Function (pp. 38 to 40: *the reason for this module*), 2.6 Green Function for the Sphere (pp. 64 to 65); Griffiths §3.1.5 to §3.1.6 (pp. 118 to 124) for the physical reading; Riley §17.5 (pp. 569 to 572) and §21.5 (pp. 751 to 767) for the Green function as the inverse of a differential operator; Zangwill (optional).
**Time:** 2 weeks (four sessions). **Never skip** this module: Jackson 1.8 to 1.10 and 2.6 are non-negotiable.
**Pinned to:** Griffiths 5th ed. (2024), Jackson 3rd ed. (1999), Purcell and Morin 3rd ed. (2013, SI), Riley, Hobson and Bence 3rd ed. Page numbers are the printed book pages.

## Why this matters

$G(\mathbf x,\mathbf x')$ with $\nabla^2G=-4\pi\delta^3(\mathbf x-\mathbf x')$ is *the inverse of the Laplacian*. Everything you will later do with propagators is this idea plus a time dimension, a mass term and a choice of contour. Note in the margin that **boundary conditions selecting a unique $G$ is the same logical move as boundary conditions in time (retarded versus advanced) selecting a unique propagator.**

## Skip-test (40 minutes, no notes)

1. Derive Green's second identity from the divergence theorem (this is the Stewart exit gate; it should take under five minutes).
2. Show that $G=\frac1{|\mathbf x-\mathbf x'|}+F(\mathbf x,\mathbf x')$ with $\nabla^2F=0$ inside $V$ is a Green function, and derive the formal solution $$\Phi(\mathbf x)=\frac{1}{4\pi\epsilon_0}\int_V\rho(\mathbf x')G_D\,d^3x'-\frac{1}{4\pi}\oint_S\Phi(\mathbf x')\frac{\partial G_D}{\partial n'}da'$$ for $G_D=0$ on $S$.
3. Explain precisely why a Neumann Green function *cannot* have $\partial G_N/\partial n'=0$ on $S$ (hint: integrate $\nabla'^2G$).
4. Show $G_D(\mathbf x,\mathbf x')=G_D(\mathbf x',\mathbf x)$ and say where the boundary condition entered.
5. Write the Dirichlet Green function for the half-space $z>0$ and the sphere of radius $a$.

## Prerequisites

Modules 01 to 04 (Green's identities, delta functions, images).

## Detailed topics (checklist)

**Green's theorem (1.8) [Must]**
- Green's first and second identities; the free-space Green function $\frac{1}{|\mathbf x-\mathbf x'|}$; the general solution $G=\frac1R+F$ with $F$ a harmonic function chosen to meet a boundary condition.

**The formal solution (1.10) [Must]**
- Apply Green's second identity with $\psi=G$ and $\phi=\Phi$: $$\Phi(\mathbf x)=\frac1{4\pi\epsilon_0}\int_V\rho G\,d^3x'+\frac{1}{4\pi}\oint_S\left[G\frac{\partial\Phi}{\partial n'}-\Phi\frac{\partial G}{\partial n'}\right]da'.$$
- **Dirichlet:** $G_D=0$ for $\mathbf x'\in S$: kills the $\partial_n\Phi$ term (which you do not know). **Neumann:** $\partial_{n'}G_N$ cannot vanish (since $\oint\partial_{n'}G\,da'=-4\pi$), so $\partial_{n'}G_N=-\frac{4\pi}{S}$; the potential is then defined up to a constant. Why you cannot specify both on the same boundary.
- Symmetry $G_D(\mathbf x,\mathbf x')=G_D(\mathbf x',\mathbf x)$ (reciprocity).

**Examples [Must]**
- Half-space $z>0$: $G_D=\frac1{|\mathbf x-\mathbf x'|}-\frac1{|\mathbf x-\mathbf x'_{\rm image}|}$ and the resulting Poisson kernel $\Phi(\mathbf x)=\frac{z}{2\pi}\int\frac{\Phi(x',y',0)}{[(x-x')^2+(y-y')^2+z^2]^{3/2}}dx'dy'$.
- Sphere of radius $a$ (2.6): $G_D=\frac{1}{|\mathbf x-\mathbf x'|}-\frac{a}{x'\left|\mathbf x-\frac{a^2}{x'^2}\mathbf x'\right|}$; the interior Poisson kernel $\Phi(\mathbf x)=\frac{a(a^2-x^2)}{4\pi}\oint\frac{\Phi(a,\Omega')}{(x^2+a^2-2ax\cos\gamma)^{3/2}}d\Omega'$.
- The Green function *is* the image solution: the "image charges" are the harmonic part $F$.

**The logic of the construction [Must]**
- A Green function is a solution for a unit point source; once you have it, *any* source and boundary data are handled by integration; the same idea with a time dimension gives the retarded Green function (Module 11) and the propagator of QFT.

## Method card

**Constructing $G_D$:** (1) write $G=\frac1R+F$; (2) find $F$ (harmonic inside $V$, i.e. with sources outside $V$) such that $G=0$ for $\mathbf x$ on $S$; in simple geometries $F$ is the image potential; (3) verify the boundary condition and symmetry; (4) compute $\partial G/\partial n'$ on $S$; (5) insert in the formal solution and check a known case (constant boundary data).

## Reading plan (pinned to your editions)

A session is part A (read, derive) followed by part B (exercises), about two and a half hours in all. Page numbers are the printed ones.

| Session | A: read and derive | B: do | Done when |
| --- | --- | --- | --- |
| 1 | Jackson 1.8 (pp. 35 to 37), three readings. Derive the formal solution (derivations 1 and 2). | Module exercises 1 to 4. Jackson Problem 1.12 (Green's reciprocation theorem); Griffiths Problem 3.54 (Green's reciprocity theorem). | Green's second identity and the formal solution written from a blank page. |
| 2 | Jackson 1.10 (pp. 38 to 40): Dirichlet and Neumann; the Neumann subtlety; the half-space example. | Module exercises 5 and 6. Jackson Problem 1.14 (symmetry of the Dirichlet Green function; Neumann case) (symmetry of $G_D$; $G_N$ not symmetric) and Problem 1.13 (charge induced between two grounded planes, by reciprocation). | You can say exactly where the boundary condition enters the symmetry proof. |
| 3 | Jackson 2.6 (pp. 64 to 65): construct $G_D$ for the sphere. | Module exercises 7 to 9. Jackson Problem 2.2 (point charge inside a grounded hollow sphere (images)) (the same image charge, from the other side). | $G_D$ vanishes on the sphere; the Poisson kernel check passes. |
| 4 | **Jackson target:** Problem 2.7 (half-space Green function; disc at potential V; on-axis result). Redo derivations 1 and 2 from a blank page. | Spare. Optional with the complex analysis guide: Problem 2.21 (Cauchy's theorem gives the Poisson integral). | On-axis $V(1-z/\sqrt{a^2+z^2})$ obtained and the far-field expansion consistent with it. |

## Problem set (pinned)

**Pin status:** Pinned: Jackson sections and problems (verified), Griffiths problems (verified), Riley sections (verified).

Tiers: **Must** (do all), **Should** (do when time allows), **Could** (only if the module is going well). A dash in the exercise column means the problem supports the reading rather than a module exercise. Purcell and Morin: stars give difficulty; problems are solved in Chapter 12 (the exercises are not).

| Book | Problem | What it asks | Module exercise | Tier |
| --- | --- | --- | --- | --- |
| Jackson | 1.12 | Green's reciprocation theorem | 1 | Must |
| Jackson | 1.14 | symmetry of the Dirichlet Green function; Neumann case | 3 | Must |
| Jackson | 2.7 | half-space Green function; disc at potential V; on-axis result | 10 | Must |
| Jackson | 1.13 | charge induced between two grounded planes, by reciprocation | 2 | Should |
| Jackson | 2.2 | point charge inside a grounded hollow sphere (images) | 7 | Should |
| Griffiths | 3.54 | Green's reciprocity theorem | 1 | Should |
| Riley | 21.23 | Green function in the half-space z > 0 | 5 | Should |
| Jackson | 2.21 | Cauchy's theorem gives the Poisson integral | 10 | Could |
| Griffiths | 3.55 | problems solved with reciprocity | 1 | Could |
| Riley | 17.14 | Poisson's equation solved with a Green function | 1 | Could |

## Derive from scratch

1. Green's second identity.
2. The formal solution with $G_D$, term by term (which terms vanish and why).
3. The Neumann condition $\partial_{n'}G_N=-4\pi/S$.
4. $G_D$ symmetric: apply Green's second identity to $G(\cdot,\mathbf x)$ and $G(\cdot,\mathbf y)$.
5. $G_D$ for the sphere, and the Poisson kernel.

## Bare-minimum exercises (with expected results)

1. **Formal solution:** write it out and identify the three contributions (volume charge, boundary potential, boundary normal derivative) and which survive for $G_D$.
2. **Free space:** with $S\to\infty$ and $\Phi,\partial_n\Phi$ falling off, the formal solution reduces to $\Phi=\frac1{4\pi\epsilon_0}\int\frac{\rho}{|\mathbf x-\mathbf x'|}d^3x'$ (surface terms vanish at infinity).
3. **Dirichlet symmetry:** apply Green's second identity to $G(\mathbf z,\mathbf x)$ and $G(\mathbf z,\mathbf y)$ (as functions of $\mathbf z$); the boundary terms vanish because $G_D=0$ on $S$; conclude $G_D(\mathbf x,\mathbf y)=G_D(\mathbf y,\mathbf x)$.
4. **Neumann:** integrate $\nabla'^2G_N=-4\pi\delta$ over $V$ to get $\oint\partial_{n'}G_N\,da'=-4\pi$, so $\partial_{n'}G_N=0$ is impossible.
5. **Half-space:** $G_D=\frac{1}{|\mathbf x-\mathbf x'|}-\frac{1}{|\mathbf x-\bar{\mathbf x}'|}$ with $\bar{\mathbf x}'=(x',y',-z')$; show $\partial G_D/\partial n'|_{z'=0}$ (outward normal $-\hat{\mathbf z}$) gives $-\frac{2z}{R^3}$ and the Poisson kernel above.
6. **Disc target:** for a disc of radius $a$ at potential $V$ in the plane $z=0$ (grounded outside the disc) the potential on the axis is $\Phi(0,0,z)=V\left(1-\frac{z}{\sqrt{z^2+a^2}}\right)$ (integrate the Poisson kernel); check $z\to0$ and $z\gg a$ ($\Phi\to\frac{Va^2}{2z^2}$).
7. **Sphere:** show $G_D=\frac1{|\mathbf x-\mathbf x'|}-\frac{a}{x'|\mathbf x-a^2\mathbf x'/x'^2|}$ vanishes for $|\mathbf x|=a$ and is symmetric in $\mathbf x\leftrightarrow\mathbf x'$.
8. **Poisson kernel check:** for constant $\Phi(a,\Omega')=V$ the interior formula must give $\Phi(\mathbf x)=V$; this requires $\oint\frac{d\Omega'}{(x^2+a^2-2ax\cos\gamma)^{3/2}}=\frac{4\pi}{a(a^2-x^2)}$ (verify by direct integration over $\cos\gamma$).
9. **Mean value:** at the centre ($x=0$) the interior formula gives $\Phi(0)=\frac1{4\pi}\oint\Phi(a,\Omega')d\Omega'$ (the mean-value theorem again).
10. **Jackson targets (about 2.7 and the Green-identity problems):** (a) the Dirichlet Green function of the half-space, then the potential of a disc at fixed potential (exercise 6); (b) a point charge inside a grounded sphere, via $G_D$, with the induced charge on the sphere $-q$.

## Optional extension

Solve the two-dimensional analogue: the Green function of the Laplacian in the plane is $-\ln|\mathbf x-\mathbf x'|$ (up to constants and the factor $2\pi$); find $G_D$ for a circle by the image method and the 2D Poisson kernel.

## Pitfalls

- Specifying both Dirichlet and Neumann data on the same boundary.
- Forgetting that the normal derivative $\partial_{n'}$ acts on the *source* variable $\mathbf x'$.
- Taking the outward normal from the wrong region (exterior versus interior problems flip the sign).
- Treating $F$ as a charge inside $V$ (it comes from sources outside).

## Gate questions

1. Why is the Green function "the inverse of the Laplacian" and what picks the unique one?
2. Why can the Neumann Green function not have zero normal derivative?
3. How is "boundary conditions select the Green function" the same idea as "retarded versus advanced"?

## One-page cheat sheet contents

Green's identities; the general $G=1/R+F$; the formal solution (Dirichlet and Neumann); half-space and sphere Green functions and kernels.
