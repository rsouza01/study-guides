# Module 01: Stewart calculus refresher (in progress)

**Books:** Stewart *Calculus*, 8th edition (7.1, 7.8, 11.9 to 11.10, 13.1 to 13.2, 14.5 to 14.6, 15.7 to 15.8, 16.1 to 16.9).
**Time:** three prelude weeks (P1 to P3). **Your status:** P1 and P2 done; P3 nearly done. **Remaining: about one week**, covering Stewart 16.8 (Stokes' theorem) and 16.9 (the divergence theorem), the "extra exercises" below, and the exit gate.
**This module stays in the document as the calculus reference for the whole guide.**

## Why this matters

Maxwell's equations, potentials and Green's identities are all vector calculus. Green's second identity is integration by parts in three dimensions, and the boundary terms are the surface integrals that carry every boundary condition. Convergence of improper integrals at $r\to0$ and $r\to\infty$ is where the physics lives. The multipole and Legendre expansions come from the series $(1+x)^{-1/2}$. The chain rule is why $\partial_\mu$ transforms with the inverse matrix. This module is the toolkit; Module 02 adds the two things Stewart does not cover.

## Skip-test (exit gate, 40 minutes, no notes)

1. Derive Green's second identity $\int_V(\phi\nabla^2\psi-\psi\nabla^2\phi)\,d^3x=\oint_S(\phi\,\partial_n\psi-\psi\,\partial_n\phi)\,da$ from the divergence theorem. **Target: under five minutes.**
2. Expand $\frac{1}{|\mathbf x-\mathbf x'|}=(r^2-2rr'\cos\gamma+r'^2)^{-1/2}$ in powers of $r'/r$ to third order.
3. State Stokes' theorem and the divergence theorem with the orientation conventions, and use them to turn $\oint\mathbf E\cdot d\boldsymbol\ell=-\frac{d}{dt}\int\mathbf B\cdot d\mathbf a$ and $\oint\mathbf E\cdot d\mathbf a=Q/\epsilon_0$ into differential form.
4. Prove $\nabla\times(\nabla f)=0$ and $\nabla\cdot(\nabla\times\mathbf F)=0$, and state which physical statements they underwrite ($\mathbf E=-\nabla\Phi$, $\mathbf B=\nabla\times\mathbf A$).
5. Convert $dV$ to spherical and cylindrical coordinates and write $\delta^3(\mathbf x)$ in each.

## Week P1: integration and series *(done)*

**Reading:**
- **Stewart 7.1, integration by parts.** *Why:* Green's second identity is integration by parts in three dimensions. Focus on the boundary terms.
- **7.8, improper integrals.** *Why:* potentials are integrals over infinite space; convergence at $r\to\infty$ and $r\to0$ is where the physics lives.
- **11.9 to 11.10, power, Taylor and Maclaurin series.** Key: the expansion of $(1+x)^{-1/2}$; it generates the multipole series and the Legendre generating function.

**Exercises:** 7.1 #29; 7.8 #31, #32; 11.10 #5, #12.
**Extra (30 min):** expand $\frac{1}{|\mathbf x-\mathbf x'|}$ by hand to third order. You have derived the first Legendre polynomials without knowing it. Keep the page.

## Week P2: multivariable machinery *(done)*

**Reading:** 13.1 to 13.2 (vector functions, space curves: parameterization for relativistic kinematics and the retarded position); 14.5 (the multivariable chain rule: it is why $\partial_\mu$ transforms with the *inverse* matrix); 14.6 (directional derivatives and the gradient: $\mathbf E=-\nabla\Phi$); 15.7 to 15.8 (cylindrical and spherical coordinates: the Jacobian $dV=r^2\sin\theta\,dr\,d\theta\,d\phi$ and the form of $\delta^3$).
**Exercises:** 14.5 #35 (implicit differentiation); 15.8 #21, #25 (spherical volumes).

## Week P3: vector calculus *(nearly done; remaining 16.8 and 16.9)*

**Reading (Stewart):**
- **16.1 to 16.3:** vector fields, line integrals, the fundamental theorem for line integrals. Focus: conservative fields, path independence, the test $P_y=Q_x$ (this is $\mathbf E=-\nabla V$ in embryo); note where "simply connected" first becomes necessary (the wire field).
- **16.4, Green's theorem (2D),** including the extended version for regions with holes: contour deformation, the real-variable ancestor of the residue theorem.
- **16.5, curl and divergence.** $\nabla$ as an operator. Land $\nabla\times(\nabla f)=\mathbf 0$ and $\nabla\cdot(\nabla\times\mathbf F)=0$: they are why $\mathbf E=-\nabla V$ and $\mathbf B=\nabla\times\mathbf A$ are legal.
- **16.6, parametric surfaces and areas** (fast): $|\mathbf r_u\times\mathbf r_v|\,du\,dv$.
- **16.7, surface integrals.** Oriented surfaces and flux: the language of Gauss's law.
- **16.8, Stokes' theorem** $\leftarrow$ **remaining.**
- **16.9, the divergence theorem** $\leftarrow$ **remaining.**

**Extra exercises (numbering from your roadmap; verify against your copy):**

| Section | Problems | Why |
| --- | --- | --- |
| 16.3 conservative fields | **3, 5, 7** (conservative? find $f$), **13** ($f$ then $\int_C\mathbf F\cdot d\mathbf r$), **16** (3D), **31 to 34** (open, connected, simply connected), **35 ★** | **35 is the wire field** $\mathbf F=\frac{-y\mathbf i+x\mathbf j}{x^2+y^2}$: $P_y=Q_x$ everywhere yet $\oint\neq0$. It is the same field as Green's Example 5, Ampere's law and $1/z$. **Do this one.** |
| 16.4 Green's theorem | **1** (verify both ways), **7, 9, 11**, **27 ★** (extended Green: contour deformation around a hole) | the real-variable ancestor of the residue theorem |
| 16.5 curl and divergence | **1, 3** (mechanical), **15**, **25, 27** (product rules for $\nabla\cdot$), **29 ★** ($\nabla\times\nabla\times\mathbf F=\nabla(\nabla\cdot\mathbf F)-\nabla^2\mathbf F$), **33, 34 ★★★** (Green's first and second identities), **38** (Maxwell's equations) | **29 is the identity that turns Maxwell's equations into wave equations.** **34 is the gate for Jackson Section 1.8: do it first.** |
| 16.6 parametric surfaces | **20, 23, 24** (plane, sphere, cylinder), **35**, **41**, **51 ★** ($dS=\sqrt{1+f_x^2+f_y^2}\,dA$) | the three geometries Jackson lives on |
| 16.7 surface integrals | **21, 22**, two more from 23 to 32 (a cylinder and a closed surface), **45 or 46 ★** (Gauss's law), **47** (heat conduction, $\mathbf F=-K\nabla u$) | be deliberate about orientation |
| 16.8 Stokes | one "verify Stokes" problem | **remaining** |
| 16.9 divergence theorem | one "verify the divergence theorem" problem | **remaining** |

**If you only do eight:** 16.3 #35, 16.4 #27, 16.5 #29, #33, #34, 16.6 #51, 16.7 #22, #45.
**The one to do first:** 16.5 #34 (Green's second identity).

## Method cards

**Verify Stokes' theorem:** (1) choose the surface $S$ and orient it, giving the boundary orientation by the right-hand rule; (2) compute $\oint_C\mathbf F\cdot d\mathbf r$ with a parameterization; (3) compute $\nabla\times\mathbf F$ and $\int_S(\nabla\times\mathbf F)\cdot d\mathbf S$; (4) compare. *Check:* $\mathbf F=(-y,x,0)$ around the unit circle: line integral $=2\pi$; $\nabla\times\mathbf F=(0,0,2)$; flux through the disc $=2\cdot\pi=2\pi$.
**Verify the divergence theorem:** (1) closed surface with outward normal; (2) compute the flux through each piece; (3) compute $\nabla\cdot\mathbf F$ and integrate over the volume; (4) compare. *Check:* $\mathbf F=(x,y,z)$ on a sphere of radius $R$: flux $=R\cdot4\pi R^2=4\pi R^3$; $\nabla\cdot\mathbf F=3$; volume integral $=3\cdot\frac43\pi R^3=4\pi R^3$.
**Green's second identity (derive):** apply the divergence theorem to $\mathbf F=\phi\nabla\psi-\psi\nabla\phi$; $\nabla\cdot\mathbf F=\phi\nabla^2\psi-\psi\nabla^2\phi$.

## Detailed topics (checklist)

- **[Must]** parts with boundary terms; improper integrals; the binomial series for $(1+x)^{-1/2}$.
- **[Must]** chain rule, implicit differentiation, gradient, spherical and cylindrical Jacobians.
- **[Must]** line and surface integrals; conservative fields; the five theorems (fundamental theorem of line integrals, Green, Stokes, divergence, and Green's identities); orientation conventions.
- **[Must]** $\nabla\times\nabla f=0$, $\nabla\cdot\nabla\times\mathbf F=0$, the product rules, $\nabla\times\nabla\times=\nabla\nabla\cdot-\nabla^2$.
- **[Should]** simply connected regions and the wire field; the extended Green's theorem.

## Reading plan (remaining week)

| Session | Task |
| --- | --- |
| A1 | Stewart 16.8 and 16.9; the verify-Stokes and verify-divergence exercises |
| B1 | Extra exercises 16.5 #34, #29, #33 and 16.3 #35; the exit gate (skip-test items 1 to 5) |

## Derive from scratch

1. Green's second identity from the divergence theorem.
2. $\nabla\times\nabla f=0$ and $\nabla\cdot\nabla\times\mathbf F=0$ with $\epsilon_{ijk}$.
3. The $r'/r$ expansion of $|\mathbf x-\mathbf x'|^{-1}$ to third order.
4. Stokes' theorem $\to\nabla\times\mathbf E=-\partial_t\mathbf B$ and the divergence theorem $\to\nabla\cdot\mathbf E=\rho/\epsilon_0$.
5. The wire-field counterexample ($P_y=Q_x$ but $\oint\ne0$).

## Pitfalls

- Choosing the surface normal inconsistently with the boundary orientation.
- Dropping boundary terms in integration by parts without checking they vanish.
- Applying "$\nabla\times\mathbf F=0\Rightarrow$ conservative" on a region that is not simply connected.

## Gate questions

1. Why is Green's second identity the gate for Jackson's formal solution of boundary-value problems?
2. Why do $\nabla\times\nabla f=0$ and $\nabla\cdot\nabla\times\mathbf F=0$ make $\mathbf E=-\nabla\Phi$ and $\mathbf B=\nabla\times\mathbf A$ legitimate?
3. What does the wire field show about simple connectivity?

## One-page cheat sheet contents

The five theorems with orientation rules; Green's identities; curl/div identities; spherical and cylindrical $dV$; the binomial series.
