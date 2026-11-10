# Module 14: Spacetime structure and the Lorentz algebra (★)

**Books:** Jackson **11.6 Mathematical properties of the space-time of special relativity (pp. 536 to 543: the densest and most valuable section in the chapter)** and **11.7 Matrix representation of Lorentz transformations, infinitesimal generators (pp. 543 to 548)**; Griffiths §12.1.4 The Structure of Space-Time (pp. 530 to 538); Riley §26.15 The metric tensor (p. 957) and §26.16 General coordinate transformations (p. 960), optional. **Skip** Jackson 11.8 (Thomas precession) and 11.11 (BMT spin equation). Your mechanics guide, Module 12, is the prerequisite for the algebra.
**Time:** 2 weeks (four sessions).
**Pinned to:** Griffiths 5th ed. (2024), Jackson 3rd ed. (1999), Purcell and Morin 3rd ed. (2013, SI), Riley, Hobson and Bence 3rd ed. Page numbers are the printed book pages.

## Why this matters

Jackson writes the boost generators $\mathbf K$ and rotation generators $\mathbf S$ and shows the algebra closes. He stops there. You should form $\mathbf A_\pm=\frac12(\mathbf S\pm i\mathbf K)$ and verify the algebra splits into **two commuting $\mathfrak{su}(2)$'s.** That decomposition is why fields carry labels $(j_-,j_+)$, why $(\frac12,0)\oplus(0,\frac12)$ is the Dirac spinor, and why $(\frac12,\frac12)$ is $A_\mu$. Jackson gets you to the doorstep; you write the page that steps through it. **This is the highest-value hour of this thread.**

## Skip-test (40 minutes, no notes)

1. Write $\eta_{\mu\nu}$, raise and lower indices, and state the index-placement rule that follows from $\partial_\mu$ transforming covariantly while $x^\mu$ transforms contravariantly.
2. Show that a boost $\Lambda$ satisfies $\Lambda^T\eta\Lambda=\eta$ and write the $4\times4$ boost matrix along $x$ in terms of $\gamma,\beta$.
3. Write the generators $\mathbf S$ and $\mathbf K$ of rotations and boosts and verify $[S_i,S_j]=\epsilon_{ijk}S_k$, $[S_i,K_j]=\epsilon_{ijk}K_k$, $[K_i,K_j]=-\epsilon_{ijk}S_k$.
4. Form $\mathbf A_\pm=\frac12(\mathbf S\pm i\mathbf K)$ and show $[A^\pm_i,A^\pm_j]=\epsilon_{ijk}A^\pm_k$, $[A^+_i,A^-_j]=0$.
5. State which $(j_-,j_+)$ representation a scalar, a Weyl spinor, the four-vector $A_\mu$, and the field tensor $F_{\mu\nu}$ belong to.

## Prerequisites

Modules 13 and 02 (index notation); mechanics guide Module 12 (the rotation algebra, $SU(2)$).

## Detailed topics (checklist)

**The metric and tensors (11.6) [Must]**
- $\eta_{\mu\nu}=\mathrm{diag}(+,-,-,-)$; $x_\mu=\eta_{\mu\nu}x^\nu$; contravariant and covariant vectors; $a\cdot b=a^\mu b_\mu$ invariant; $\partial_\mu=\frac{\partial}{\partial x^\mu}$ transforms covariantly; $\Box=\partial_\mu\partial^\mu$ is invariant; general tensors $T^{\mu\nu}$, $F_{\mu\nu}$; contraction; the antisymmetric Levi-Civita tensor $\epsilon^{\mu\nu\alpha\beta}$ and the dual $\tilde F^{\mu\nu}=\frac12\epsilon^{\mu\nu\alpha\beta}F_{\alpha\beta}$.
- **Index-placement rule:** every index must be paired (one up, one down) in a Lorentz-invariant expression.

**The Lorentz group and its generators (11.7) [Must]**
- $\Lambda^T\eta\Lambda=\eta$; proper orthochronous subgroup; six parameters (three rotations, three boosts); finite transformations $\Lambda=e^{-\boldsymbol\omega\cdot\mathbf S-\boldsymbol\zeta\cdot\mathbf K}$ (sign conventions as in Jackson); the algebra $[S_i,S_j]=\epsilon_{ijk}S_k$, $[S_i,K_j]=\epsilon_{ijk}K_k$, $[K_i,K_j]=-\epsilon_{ijk}S_k$ (the minus sign is the whole difference between $SO(4)$ and $SO(3,1)$).
- **The extra step:** $\mathbf A_\pm=\frac12(\mathbf S\pm i\mathbf K)$ gives $[A^\pm_i,A^\pm_j]=\epsilon_{ijk}A^\pm_k$ and $[A^+_i,A^-_j]=0$: $\mathfrak{so}(1,3)\otimes\mathbb C\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$.
- **Classification of fields by $(j_-,j_+)$:** $(0,0)$ scalar; $(\frac12,0)$ and $(0,\frac12)$ left- and right-handed Weyl spinors (the Dirac spinor is $(\frac12,0)\oplus(0,\frac12)$); $(\frac12,\frac12)$ the four-vector; $(1,0)\oplus(0,1)$ the antisymmetric tensor $F^{\mu\nu}$ (six components $=\mathbf E\pm i\mathbf B$); $(1,1)$ the symmetric traceless tensor. *Connect to the Zettili guide (Chapter 12: Weyl fermions, chirality).*

**Wigner rotation [Should]**
- Two non-collinear boosts compose into a boost times a rotation; this is the origin of Thomas precession (the rotation angle for small velocities is $\approx\frac{1}{2c^2}|\mathbf v_1\times\mathbf v_2|$).

## Method card

**Index gymnastics:** (1) write every tensor with its index positions; (2) every repeated index must be one up, one down; (3) raise or lower with $\eta$; (4) to check invariance, count free indices on each side (they must match in position); (5) test with a boost matrix on a simple case.

## Reading plan (pinned to your editions)

A session is part A (read, derive) followed by part B (exercises), about two and a half hours in all. Page numbers are the printed ones.

| Session | A: read and derive | B: do | Done when |
| --- | --- | --- | --- |
| 1 | Jackson 11.6 (pp. 536 to 543). Index drills. | Module exercises 1 to 3. Griffiths Problems 12.53, 12.54. Riley Exercise 26.12. | Raising and lowering done without sign errors. |
| 2 | Jackson 11.7 (pp. 543 to 548). Verify the generator commutators. | Module exercises 3 to 5. Jackson Problems 11.9 and 11.10. | $[K_i,K_j]=-i\epsilon_{ijk}J_k$ verified. |
| 3 | The $\mathbf A_\pm=\frac12(\mathbf J\pm i\mathbf K)$ decomposition. Griffiths §12.1.4. | Module exercises 6 to 8; write the deliverable page. Griffiths Problem 12.19. | Two commuting $SU(2)$ algebras identified. |
| 4 | **Jackson targets**; the computational task. | Jackson Problems 11.11 and 11.12. Spare. | Infinitesimal-transformation algebra complete. |

## Problem set (pinned)

**Pin status:** Pinned: sections and problems in Griffiths, Jackson and Riley (verified).

Tiers: **Must** (do all), **Should** (do when time allows), **Could** (only if the module is going well). A dash in the exercise column means the problem supports the reading rather than a module exercise. Purcell and Morin: stars give difficulty; problems are solved in Chapter 12 (the exercises are not).

| Book | Problem | What it asks | Module exercise | Tier |
| --- | --- | --- | --- | --- |
| Jackson | 11.9 | infinitesimal Lorentz transformation and its inverse | 10 | Must |
| Jackson | 11.10 | boost and rotation matrices: relations | 10 | Must |
| Griffiths | 12.19 | parallel between rotations and Lorentz transformations | 6 | Should |
| Griffiths | 12.53 | symmetry of a tensor is frame independent | 1 | Should |
| Griffiths | 12.54 | covariant from contravariant 4-vector | 1 | Should |
| Jackson | 11.11 | two transformations differing by an infinitesimal amount | 10 | Should |
| Riley | 26.12 | antisymmetric tensors in four dimensions | 1 | Could |
| Jackson | 11.12 | application of 11.11 | 10 | Could |

## Derive from scratch

1. $\Lambda^T\eta\Lambda=\eta$ for an $x$-boost.
2. The commutators $[S_i,K_j]$ and $[K_i,K_j]$ from the $4\times4$ matrices.
3. The $\mathbf A_\pm$ decomposition.
4. The six components of $F^{\mu\nu}$ as $\mathbf E\pm i\mathbf B$ and their $(1,0)\oplus(0,1)$ nature.
5. The index-placement rule from the chain rule (Stewart 14.5).

## Bare-minimum exercises (with expected results)

1. **Boost matrix:** $\Lambda=\begin{pmatrix}\gamma&-\gamma\beta\\-\gamma\beta&\gamma\end{pmatrix}$ (in the $(ct,x)$ block); verify $\Lambda^T\eta\Lambda=\eta$ and $\det\Lambda=1$; composition of two boosts has rapidity $\eta_1+\eta_2$.
2. **Index placement:** show $\partial_\mu x^\mu=4$ (a scalar), that $\partial_\mu$ transforms with $(\Lambda^{-1})^\nu{}_\mu$ and $x^\mu$ with $\Lambda^\mu{}_\nu$, and that $\Box=\partial_\mu\partial^\mu$ is invariant.
3. **Generators as matrices:** construct the six $4\times4$ matrices ($S_i$ rotates the spatial components; $K_i$ mixes $t$ with $x_i$) and verify $[S_i,S_j]=\epsilon_{ijk}S_k$, $[S_i,K_j]=\epsilon_{ijk}K_k$, $[K_i,K_j]=-\epsilon_{ijk}S_k$ numerically; compare with the rotation algebra of mechanics Module 12.
4. **The decomposition:** verify $[A^+_i,A^+_j]=\epsilon_{ijk}A^+_k$, $[A^-_i,A^-_j]=\epsilon_{ijk}A^-_k$ and $[A^+_i,A^-_j]=0$ for $\mathbf A_\pm=\frac12(\mathbf S\pm i\mathbf K)$, using the three commutators of exercise 3. *This is the page you write.*
5. **Counting:** the Lorentz group has $6$ generators and the Poincare group $10$ (adding four translations); explain why $\mathfrak{so}(3)$ has three (the rotation algebra of Module 12).
6. **Wigner rotation:** compose a boost along $x$ with $\beta_1=0.5$ and a boost along $y$ with $\beta_2=0.5$ as $4\times4$ matrices and show the product equals a pure boost times a rotation about $z$; for small $\beta$ the angle is $\approx\frac12\beta_1\beta_2$ (that would be $0.125$ rad here); for perpendicular boosts the exact angle satisfies $\cos\theta=\frac{\gamma_1+\gamma_2}{1+\gamma_1\gamma_2}$, giving $\theta\approx0.143$ rad for $\beta_1=\beta_2=0.5$ (verify numerically).
7. **$F^{\mu\nu}$ as a representation:** $F^{\mu\nu}$ has six independent components; the complex vector $\mathbf F=\mathbf E+i c\mathbf B$ (Riemann-Silberstein) transforms under rotations as an ordinary vector and under a boost as a rotation by an *imaginary* angle; this is the $(1,0)\oplus(0,1)$ statement.
8. **Invariants preview:** with $\mathbf F=\mathbf E+ic\mathbf B$ the scalar $\mathbf F\cdot\mathbf F=E^2-c^2B^2+2ic\,\mathbf E\cdot\mathbf B$ is invariant, so $E^2-c^2B^2$ and $\mathbf E\cdot\mathbf B$ are the two invariants ($\propto F_{\mu\nu}F^{\mu\nu}$ and $\epsilon^{\mu\nu\alpha\beta}F_{\mu\nu}F_{\alpha\beta}$).
9. **Dimension of representations:** the $(j_-,j_+)$ representation has dimension $(2j_-+1)(2j_++1)$; check $(\frac12,\frac12)$ has dimension 4 (the four-vector), $(1,0)\oplus(0,1)$ has dimension 6 ($F^{\mu\nu}$), and $(\frac12,0)\oplus(0,\frac12)$ has dimension 4 (Dirac).
10. **Jackson targets:** (a) a tensor-transformation drill (transform $F^{\mu\nu}$ under a boost and extract $\mathbf E',\mathbf B'$: Module 15); (b) a generator-commutator computation (exercise 3); (c) **the deliverable page** `m14-lorentz-algebra.md`: the $\mathbf A_\pm$ decomposition and the field classification, in your own words.

## Computational task (project, optional)

A small four-vector library (Minkowski product, boosts, composition, invariant mass) used to reproduce a threshold-energy calculation *and* a **Wigner rotation** from two non-collinear boosts. The Wigner rotation surprises everyone the first time; seeing it fall out of matrix multiplication makes Thomas precession free.

## Pitfalls

- Treating $\mathfrak{so}(1,3)$ as $\mathfrak{so}(4)$ (the minus sign in $[K_i,K_j]$ is the difference).
- Forgetting that the complexification is needed for the $\mathbf A_\pm$ split.
- Index placement errors: always check up/down pairing.
- Mixing generator sign conventions between Jackson and other texts.

## Gate questions

1. Why does the Lorentz algebra split into two commuting $\mathfrak{su}(2)$'s?
2. Which $(j_-,j_+)$ is a Dirac spinor, a vector, an antisymmetric tensor?
3. Why do two non-collinear boosts produce a rotation?

## One-page cheat sheet contents

Metric and index rules; the three commutators; $\mathbf A_\pm$; table of $(j_-,j_+)$ representations; Wigner rotation.
