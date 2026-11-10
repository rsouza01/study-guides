# Module 04: Laplace's equation, uniqueness and the method of images

**Books:** Griffiths §3.1 Laplace's Equation (pp. 113 to 124: 3.1.2 to 3.1.4 the mean-value property, 3.1.5 boundary conditions and uniqueness theorems p. 118, 3.1.6 conductors and the second uniqueness theorem p. 121) and §3.2 The Method of Images (pp. 124 to 129); Purcell and Morin 3rd ed. §2.11 to §2.12 (pp. 85 to 88), §3.3 uniqueness theorem (pp. 132 to 136), §3.4 image charges (pp. 136 to 141) and §3.8 (p. 151); Jackson 1.9 (pp. 37 to 38) and 2.1 to 2.5 (pp. 57 to 64; read for technique and do not linger). Jackson 1.8 and 1.10 belong to Module 05.
**Time:** 2 weeks (four sessions). **Tier note:** if diagnostic problem 5 is right, pass the skip-test and do the Jackson targets only.
**Pinned to:** Griffiths 5th ed. (2024), Jackson 3rd ed. (1999), Purcell and Morin 3rd ed. (2013, SI), Riley, Hobson and Bence 3rd ed. Page numbers are the printed book pages.

## Why this matters

Images are a trick, not a theory, but they give you the first non-trivial boundary-value solutions, and the **uniqueness theorem** is the logical reason the trick is legitimate: if a function satisfies the equation and the boundary conditions, it is *the* solution. This is the same logical move as "boundary conditions in time select the retarded Green function" (Module 11). The mean-value property of Laplace's equation (no local extrema) is Earnshaw's theorem and the first instance of "boundary values determine the interior."

## Skip-test (40 minutes, no notes)

1. State the mean-value theorem for solutions of Laplace's equation and deduce that $\Phi$ has no local maxima or minima in a charge-free region.
2. Prove the Dirichlet uniqueness theorem for Poisson's equation using Green's first identity.
3. A charge $q$ sits at height $d$ above a grounded conducting plane. Find the image, the force, the induced surface charge density and the total induced charge.
4. A charge $q$ sits at distance $y>a$ from the centre of a grounded conducting sphere of radius $a$. Find the image charge and its position.
5. State what changes if the sphere is isolated and neutral, or held at potential $V$.

## Prerequisites

Modules 01 to 03.

## Detailed topics (checklist)

**Laplace and Poisson [Must]**
- Laplace's equation in a charge-free region; harmonic functions; the mean-value theorem; no extrema (Earnshaw); the difference of two solutions satisfies Laplace's equation with zero boundary data.
- **Uniqueness:** Dirichlet (given $\Phi$ on $S$) and Neumann (given $\partial_n\Phi$ on $S$, unique up to a constant); mixed conditions; why one may not specify both $\Phi$ and $\partial_n\Phi$ on the same boundary.

**Method of images [Must]**
- Replace the boundary by fictitious charges *outside* the region of interest so that the boundary condition is satisfied; uniqueness guarantees the result.
- Grounded plane: $-q$ at the mirror point. Grounded sphere: $q'=-\frac{qa}{y}$ at $\frac{a^2}{y}$. Isolated neutral sphere: add $+\frac{qa}{y}$ at the centre. Sphere at potential $V$: add $4\pi\epsilon_0aV$ at the centre. Two planes at $90^\circ$: three images. Line charge parallel to a plane or cylinder.
- Induced surface charge $\sigma=-\epsilon_0\partial_n\Phi$; force on $q$ from the image; **energy is half** of the naive image-pair energy (the field exists only on one side).

**Conductor boundary-value problems [Should]**
- Capacitance as a ratio of charge to potential (concept only; do not linger); the capacitance of a wire above a plane.

## Method card

**Images:** (1) state the region where the potential is wanted and the boundary condition (e.g. $\Phi=0$ on $S$); (2) guess image charges *outside* that region using the symmetry of the boundary (reflection for planes, inversion for spheres); (3) verify the boundary condition at a few points and in general; (4) write $\Phi$ in the region as the sum over real and image charges; (5) compute $\sigma=-\epsilon_0\partial_n\Phi$, the force and the work, keeping track of the factor $\frac12$ in the energy.

## Reading plan (pinned to your editions)

A session is part A (read, derive) followed by part B (exercises), about two and a half hours in all. Page numbers are the printed ones.

| Session | A: read and derive | B: do | Done when |
| --- | --- | --- | --- |
| 1 | Griffiths §3.1.1 to §3.1.6 (pp. 113 to 124). Jackson 1.9 (pp. 37 to 38). Purcell §2.11, §2.12 and §3.3. | Module exercises 5 and 6. Griffiths Problem 3.1 (average potential over a sphere due to an interior charge), Problem 3.2 (Earnshaw's theorem in one sentence), Problem 3.5 (first uniqueness theorem), Problem 3.6 (second uniqueness theorem via Green's identity). | Uniqueness proof reproduced from a blank page in under ten minutes. |
| 2 | Griffiths §3.2 (pp. 124 to 129). The images method card. Purcell §3.4 (pp. 136 to 141) and §3.8 (p. 151). | Module exercises 1 to 4. Griffiths Problem 3.7 (force on +q in the plane-image problem of Fig. 3.14), Problem 3.9 (force between a charge and a grounded sphere), Problem 3.10 (grounded sphere with an added charge: second image), Problem 3.11 (force between a charge and a sphere carrying total charge Q), Problem 3.12 (line charge above a grounded plane). | Force, induced density and energy of the plane problem agree with Jackson's answers. |
| 3 | Jackson 2.1 to 2.5 (pp. 57 to 64), read for technique. | Module exercises 7 to 9. Griffiths Problem 3.13 (charge between two semi-infinite grounded planes at right angles), Problem 3.40 (alternative derivation of the induced charge density), Problem 3.41 (two parallel grounded planes with a charge between); optional (computational): Problem 3.42 (two charged conducting spheres, iterated images). | Image sets for the right-angle wedge written down correctly. |
| 4 | **Jackson targets:** Problem 2.1 (charge near a grounded plane: sigma, force, work, energy) and Problem 2.2 (point charge inside a grounded hollow sphere (images)). | Spare: redo failed steps. Optional: Problem 2.4 (point charge near an equally charged isolated sphere), Problem 2.5 (work to remove a charge from a grounded sphere), Problem 2.3 (line charge near two intersecting grounded planes), Problem 2.11 (line charge parallel to a conducting cylinder at fixed voltage). | 2.1(a) to (e) all done. |

## Problem set (pinned)

**Pin status:** Pinned: Griffiths and Jackson sections and problems (verified), Purcell sections and problems (verified; solutions in Chapter 12).

Tiers: **Must** (do all), **Should** (do when time allows), **Could** (only if the module is going well). A dash in the exercise column means the problem supports the reading rather than a module exercise. Purcell and Morin: stars give difficulty; problems are solved in Chapter 12 (the exercises are not).

| Book | Problem | What it asks | Module exercise | Tier |
| --- | --- | --- | --- | --- |
| Griffiths | 3.1 | average potential over a sphere due to an interior charge | 6 | Must |
| Griffiths | 3.5 | first uniqueness theorem | 5 | Must |
| Griffiths | 3.7 | force on +q in the plane-image problem of Fig. 3.14 | 1 | Must |
| Griffiths | 3.9 | force between a charge and a grounded sphere | 3 | Must |
| Griffiths | 3.10 | grounded sphere with an added charge: second image | 4 | Must |
| Griffiths | 3.12 | line charge above a grounded plane | 9 | Must |
| Griffiths | 3.13 | charge between two semi-infinite grounded planes at right angles | 7 | Must |
| Jackson | 2.1 | charge near a grounded plane: sigma, force, work, energy | 10 | Must |
| Jackson | 2.2 | point charge inside a grounded hollow sphere (images) | 10 | Must |
| Purcell | 3.13 *** | image charge for a grounded spherical shell | 3 | Must |
| Griffiths | 3.2 | Earnshaw's theorem in one sentence | 6 | Should |
| Griffiths | 3.6 | second uniqueness theorem via Green's identity | 5 | Should |
| Griffiths | 3.11 | force between a charge and a sphere carrying total charge Q | 4 | Should |
| Griffiths | 3.41 | two parallel grounded planes with a charge between | 7 | Should |
| Jackson | 2.4 | point charge near an equally charged isolated sphere | 3 | Should |
| Jackson | 2.5 | work to remove a charge from a grounded sphere | 2 | Should |
| Purcell | 3.12 ** | image charges for two planes | 7 | Should |
| Purcell | 3.14 | force from a conducting shell | 3 | Should |
| Purcell | 3.15 *** | dipole from a shell in a uniform field | 8 | Should |
| Griffiths | 3.40 | alternative derivation of the induced charge density | 1 | Could |
| Purcell | 3.16 ** | image charge for a non-grounded sphere | 4 | Could |
| Purcell | 3.37 ** | a charge between two plates (exercise) | 7 | Could |
| Purcell | 3.43 ** | images from three planes (exercise) | 7 | Could |
| Purcell | 3.51 *** | conducting sphere in a uniform field (exercise) | 8 | Could |

## Derive from scratch

1. The mean-value theorem for harmonic functions (spherical average).
2. The Dirichlet uniqueness proof via Green's first identity.
3. The image charge and position for a grounded sphere (show the potential vanishes on the sphere).
4. The induced charge density on the plane and its total.
5. The energy of the image system and the factor $\frac12$.

## Bare-minimum exercises (with expected results)

1. **Charge above a plane:** $F=\frac{q^2}{16\pi\epsilon_0d^2}$ (attractive); $\sigma(\rho)=-\frac{qd}{2\pi(\rho^2+d^2)^{3/2}}$; total induced charge $-q$ (integrate over the plane).
2. **Work to bring the charge in:** $W=\frac{q^2}{16\pi\epsilon_0d}$ (integrate the force from infinity), which is *half* of $\frac{q^2}{4\pi\epsilon_0(2d)}$.
3. **Charge near a grounded sphere:** $q'=-\frac{qa}{y}$ at $\frac{a^2}y$; the force on $q$ is attractive with magnitude $F=\frac{q^2}{4\pi\epsilon_0}\frac{ay}{(y^2-a^2)^2}$; for $y\to a$ it diverges, for $y\gg a$ it falls as $y^{-3}$.
4. **Isolated neutral sphere:** add $+\frac{qa}{y}$ at the centre; the sphere's potential is then $\frac{q}{4\pi\epsilon_0y}$; the net attractive force on $q$ is $\frac{q^2a}{4\pi\epsilon_0}\left[\frac{y}{(y^2-a^2)^2}-\frac{1}{y^3}\right]$ (the grounded-sphere attraction minus the repulsion from the centre charge).
5. **Uniqueness:** if $\Phi_1,\Phi_2$ solve Poisson's equation with the same $\Phi$ on $S$, then $\int_V|\nabla(\Phi_1-\Phi_2)|^2d^3x=\oint(\Phi_1-\Phi_2)\partial_n(\Phi_1-\Phi_2)da=0$, so $\Phi_1=\Phi_2$.
6. **Mean-value property:** the average of $\Phi$ over a sphere in a charge-free region equals the value at the centre; deduce that a test charge cannot be in stable equilibrium in an electrostatic field (Earnshaw).
7. **Two planes at $90^\circ$:** for a charge $q$ at $(x_0,y_0)$ the images are $-q$ at $(-x_0,y_0)$, $-q$ at $(x_0,-y_0)$ and $+q$ at $(-x_0,-y_0)$; check $\Phi=0$ on both planes and compute the net force on $q$.
8. **Sphere in a uniform field:** for a grounded conducting sphere of radius $a$ in $\mathbf E=E_0\hat{\mathbf z}$ the solution is $\Phi=-E_0\left(r-\frac{a^3}{r^2}\right)\cos\theta$ with induced $\sigma=3\epsilon_0E_0\cos\theta$ (obtain it as the limit of two far-away image-paired charges, or check it satisfies Laplace's equation and the boundary conditions).
9. **Wire above a plane:** for a line charge $\lambda$ a distance $d$ above a grounded plane, the image is $-\lambda$ at $-d$; for a wire of radius $a$ the capacitance per length is $\frac{2\pi\epsilon_0}{\cosh^{-1}(d/a)}\approx\frac{2\pi\epsilon_0}{\ln(2d/a)}$.
10. **Jackson targets (about 2.1 and 2.2):** (a) the charge above a plane: image, induced density, force, work (exercises 1 and 2); (b) a charge near a grounded sphere: the image, the force and the induced charge $-q\,\frac{a}{y}$; sanity check that the induced charge is $q'$ and that the surface density integrates to it.

## Optional extension

Solve the charge-above-plane problem numerically by relaxation (Gauss-Seidel) on a 2D grid and compare with the image solution; the point is to feel the boundary conditions doing the work.

## Pitfalls

- Putting an image charge *inside* the region of interest.
- Forgetting the factor $\frac12$ in the energy of an image system.
- Assuming the image method works for any boundary (it needs a geometry with a reflection/inversion symmetry).
- Specifying both Dirichlet and Neumann data on the same boundary.

## Gate questions

1. Why does the uniqueness theorem make the images method legitimate?
2. What do the mean-value theorem and Earnshaw's theorem say about stable equilibria?
3. Why is the energy of a charge near a conducting plane half of the naive image-pair energy?

## One-page cheat sheet contents

Mean-value theorem; uniqueness proof; image charges for plane and sphere; induced charge formulas; energy factor.
