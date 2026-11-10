# Module 03: Electrostatics I: fields, potentials and energy

**Books:** Griffiths chapter 2 (the engine): §2.1 The Electric Field (pp. 57 to 63), §2.2 Divergence and Curl of Electrostatic Fields (pp. 64 to 76), §2.3 Electric Potential (pp. 76 to 88), §2.4 Work and Energy in Electrostatics (pp. 88 to 95), §2.5 Conductors (pp. 95 to 104); Purcell and Morin 3rd ed. §1.5 (p. 11), §1.7 to §1.13 (pp. 16 to 29), §1.14 to §1.15 (pp. 30 to 35), §2.1 to §2.7 (pp. 59 to 78), §3.1 to §3.2 and §3.7 (pp. 125 to 132, 149 to 151); Jackson 1.1 to 1.7 (pp. 24 to 35) and 1.11 (pp. 40 to 43; skip the capacitance subsection), read after Griffiths.
**Time:** 3 weeks (six sessions). **Tier note:** if the diagnostic problems 1 to 4 are all right, pass the skip-test and do only the Jackson target (exercise 10).
**Pinned to:** Griffiths 5th ed. (2024), Jackson 3rd ed. (1999), Purcell and Morin 3rd ed. (2013, SI), Riley, Hobson and Bence 3rd ed. Page numbers are the printed book pages.

## Why this matters

This is the module where "I understand the concept" turns into "I can compute the field." The techniques are Gauss's law with symmetry, direct integration, the potential, and the energy, and they are the same ones the rest of the guide builds on. The Jackson target (the screened potential of exercise 10) is the *static Klein-Gordon kernel in disguise* and you will meet it again in Module 17.

## Skip-test (40 minutes, no notes)

1. Find the field of an infinite uniformly charged cylinder inside and outside by Gauss's law.
2. Find the on-axis field of a uniformly charged ring and of a disc.
3. Find the potential inside and outside a uniformly charged sphere by integrating $\mathbf E$.
4. Compute the energy of a uniformly charged sphere and of a thin shell.
5. State the boundary conditions on $\mathbf E$ and $\Phi$ at a surface charge.

## Prerequisites

Modules 01, 02 (at least the delta function and the divergence theorem).

## Detailed topics (checklist)

**The field [Must]**
- Coulomb's law, superposition, charge densities ($\rho,\sigma,\lambda$); the field of discrete and continuous distributions; Gauss's law $\nabla\cdot\mathbf E=\rho/\epsilon_0$ and its integral form; when Gauss's law *determines* the field (spherical, cylindrical, planar symmetry).
- $\nabla\times\mathbf E=0$; the potential $\Phi$, $\mathbf E=-\nabla\Phi$; Poisson's equation $\nabla^2\Phi=-\rho/\epsilon_0$; the potential of a distribution $\Phi=\frac{1}{4\pi\epsilon_0}\int\frac{\rho(\mathbf x')}{|\mathbf x-\mathbf x'|}d^3x'$.

**Boundary conditions and conductors [Must]**
- Surface charge: $E_\perp$ jumps by $\sigma/\epsilon_0$, $E_\parallel$ is continuous, $\Phi$ is continuous; in a conductor $\mathbf E=0$ inside, $\Phi=$ const, charge on the surface, $\mathbf E=\frac\sigma{\epsilon_0}\hat{\mathbf n}$ just outside; induced charge.

**Energy [Must]**
- $U=\frac12\int\rho\Phi\,d^3x=\frac{\epsilon_0}2\int E^2d^3x$; energy density $\frac{\epsilon_0}{2}E^2$; the energy of point charges and the self-energy divergence (preview of Module 22).

**Dipoles and first multipoles [Should]**
- The dipole potential $\Phi=\frac{\mathbf p\cdot\hat{\mathbf r}}{4\pi\epsilon_0r^2}$ and field; torque and energy in an external field.

## Method cards

**Gauss's law problem:** (1) name the symmetry (sphere, cylinder, plane) and say what $\mathbf E$ depends on and which way it points; (2) draw the Gaussian surface on which $\mathbf E$ is constant and normal; (3) compute $\oint\mathbf E\cdot d\mathbf a$; (4) find $Q_{\rm enc}$ for each region; (5) check continuity and the limits.
**Field by integration:** (1) draw $\mathbf x$, $\mathbf x'$ and $\mathbf R=\mathbf x-\mathbf x'$; (2) use symmetry to kill components; (3) write $dq$ in the right coordinates; (4) substitute $R^2$ and the surviving component; (5) integrate; check far-field $\to Q/(4\pi\epsilon_0r^2)$.
**Potential from the field:** $\Phi(\mathbf x)=-\int_{\mathcal O}^{\mathbf x}\mathbf E\cdot d\boldsymbol\ell$ from a reference point (infinity if the charge is localized); do each region from outside in and match at boundaries.

## Reading plan (pinned to your editions)

A session is part A (read, derive) followed by part B (exercises), about two and a half hours in all. Page numbers are the printed ones.

| Session | A: read and derive | B: do | Done when |
| --- | --- | --- | --- |
| 1 | Griffiths §2.1 (pp. 57 to 63) and §2.2.1 to §2.2.3 (pp. 64 to 74). Purcell §1.7 to §1.13 (pp. 16 to 29). The Gauss method card. | Module exercises 1 to 4. Griffiths Problem 2.2 (field above the midpoint of two charges), Problem 2.5 (field on the axis of a circular loop), Problem 2.6 (field on the axis of a disk), Problem 2.12 (shell: Gauss's law inside and outside), Problem 2.13 (solid sphere: Gauss's law inside), Problem 2.14 (infinite line charge: field), Problem 2.18 (infinite slab: field). | Results match the module's expected values; the symmetry and the Gaussian surface are written down before each Gauss problem. |
| 2 | Griffiths §2.2.4 (pp. 74 to 76) and §2.3.1 to §2.3.3 (pp. 76 to 82). Purcell §2.1 to §2.7 (pp. 59 to 78). | Module exercises 5 and 6. Griffiths Problem 2.22 (potential of a uniformly charged solid sphere), Problem 2.23 (potential of an infinite line charge), Problem 2.26 (potential on the axis of the distributions of Fig. 2.34), Problem 2.27 (potential at the apex of a charged cone (ice-cream cone)), Problem 2.28 (potential on the axis of a charged solid cylinder). | Potential of the shell and of the solid sphere reproduced from $\mathbf E$; dipole field from $-\nabla\Phi$. |
| 3 | Griffiths §2.3.4 to §2.3.5 (pp. 82 to 88) and §2.4 (pp. 88 to 95). Purcell §1.5 (p. 11), §1.14 to §1.15 (pp. 30 to 35). | Module exercises 7 and 8. Griffiths Problem 2.31 (check the boundary conditions against the earlier results), Problem 2.35 (energy of a uniformly charged sphere, three ways), Problem 2.36 (energy of the sphere, a fourth way), Problem 2.37 (energy of two concentric shells), Problem 2.38 (interaction energy of two point charges). | Boundary-condition jumps derived from a pillbox and a loop; the energy of the sphere obtained three ways with the same result. |
| 4 | Griffiths §2.5 (pp. 95 to 104). Purcell §3.1, §3.2, §3.7 (pp. 125 to 132, 149 to 151). | Module exercise 9. Griffiths Problem 2.39 (metal sphere inside a thick concentric metal shell), Problem 2.40 (two spherical cavities in a neutral conductor), Problem 2.42 (two large metal plates with charges), Problem 2.43 (force between the hemispheres of a charged metal sphere), Problem 2.44 (capacitance per length of coaxial tubes). | Induced charge and the force on a conductor computed without looking at the solution. |
| 5 | Jackson 1.1 to 1.7 (pp. 24 to 35) and 1.11 (pp. 40 to 43). Read; write down what is new compared with Griffiths. | **Jackson target:** Problem 1.5 (hydrogen-atom potential: find the charge distribution). Do this one first: it returns in Module 17. | Total charge zero; point charge plus the exponential cloud found. |
| 6 (spare) | Optional Jackson problems: Problem 1.4 (Gauss's theorem for three charged spheres (n = -2 and +2)), Problem 1.6 (capacitance by Gauss's law (plates, spheres, cylinders)), Problem 1.8 (energy and energy density of the capacitors of 1.6), Problem 1.11 (normal derivative of E at a curved conductor (radii of curvature)). | Redo failed steps from `error_log.md`. | Error log has no step that appears three times. |

## Problem set (pinned)

**Pin status:** Pinned: Griffiths sections and problems (verified), Jackson sections and problems (verified), Purcell sections and problems (verified; Purcell problems are solved in Chapter 12, pp. 611 to 659 for chapters 2 and 3).

Tiers: **Must** (do all), **Should** (do when time allows), **Could** (only if the module is going well). A dash in the exercise column means the problem supports the reading rather than a module exercise. Purcell and Morin: stars give difficulty; problems are solved in Chapter 12 (the exercises are not).

| Book | Problem | What it asks | Module exercise | Tier |
| --- | --- | --- | --- | --- |
| Griffiths | 2.2 | field above the midpoint of two charges | 1 | Must |
| Griffiths | 2.5 | field on the axis of a circular loop | 2 | Must |
| Griffiths | 2.6 | field on the axis of a disk | 2 | Must |
| Griffiths | 2.12 | shell: Gauss's law inside and outside | 3 | Must |
| Griffiths | 2.13 | solid sphere: Gauss's law inside | 3 | Must |
| Griffiths | 2.14 | infinite line charge: field | 1 | Must |
| Griffiths | 2.22 | potential of a uniformly charged solid sphere | 5 | Must |
| Griffiths | 2.35 | energy of a uniformly charged sphere, three ways | 8 | Must |
| Griffiths | 2.39 | metal sphere inside a thick concentric metal shell | 9 | Must |
| Jackson | 1.5 | hydrogen-atom potential: find the charge distribution | 10 | Must |
| Griffiths | 2.18 | infinite slab: field | 4 | Should |
| Griffiths | 2.23 | potential of an infinite line charge | 5 | Should |
| Griffiths | 2.26 | potential on the axis of the distributions of Fig. 2.34 | 5 | Should |
| Griffiths | 2.31 | check the boundary conditions against the earlier results | 7 | Should |
| Griffiths | 2.36 | energy of the sphere, a fourth way | 8 | Should |
| Griffiths | 2.37 | energy of two concentric shells | 8 | Should |
| Griffiths | 2.40 | two spherical cavities in a neutral conductor | 9 | Should |
| Griffiths | 2.42 | two large metal plates with charges | 9 | Should |
| Griffiths | 2.43 | force between the hemispheres of a charged metal sphere | 9 | Should |
| Purcell | 1.14 ** | hole in a plane | 1 | Should |
| Purcell | 1.17 ** | zero field inside a spherical shell | 3 | Should |
| Purcell | 1.32 ** | energy of a shell (exercise) | 8 | Should |
| Purcell | 2.12 ** | E and phi from a ring | 2 | Should |
| Purcell | 2.14 ** | energy of a sphere | 8 | Should |
| Purcell | 2.22 ** | discontinuous E and phi | 7 | Should |
| Purcell | 3.1 ** | inner-surface charge density | 7 | Should |
| Purcell | 3.6 * | a charge inside a shell | 9 | Should |
| Griffiths | 2.27 | potential at the apex of a charged cone (ice-cream cone) | 5 | Could |
| Griffiths | 2.28 | potential on the axis of a charged solid cylinder | 5 | Could |
| Griffiths | 2.38 | interaction energy of two point charges | 8 | Could |
| Griffiths | 2.44 | capacitance per length of coaxial tubes | 9 | Could |
| Jackson | 1.4 | Gauss's theorem for three charged spheres (n = -2 and +2) | 3 | Could |
| Jackson | 1.6 | capacitance by Gauss's law (plates, spheres, cylinders) | 9 | Could |
| Purcell | 1.30 ** | force on a patch of charge | 7 | Could |
| Purcell | 1.47 * | field from a semicircle (exercise) | 2 | Could |
| Purcell | 2.24 ** | two expressions for the energy | 8 | Could |
| Purcell | 2.43 ** | potential from a rod (exercise) | 5 | Could |
| Purcell | 3.3 ** | principal radii of curvature | 7 | Could |
| Purcell | 3.11 * | how much work? | 9 | Could |

## Derive from scratch

1. The field of an infinite line charge by integration and by Gauss's law (compare).
2. The on-axis field of a disc.
3. $\nabla\times\mathbf E=0$ for a point charge and the existence of $\Phi$.
4. The energy of a charge distribution: $U=\frac12\int\rho\Phi\to\frac{\epsilon_0}2\int E^2$ (integration by parts, boundary term).
5. The boundary conditions on $\mathbf E$ from the pillbox and the loop.

## Bare-minimum exercises (with expected results)

1. **Line charge:** $E=\frac{\lambda}{2\pi\epsilon_0s}$ (by integration over the line, or by Gauss); a uniformly charged cylinder of radius $R$ and density $\rho$ has $E=\frac{\rho s}{2\epsilon_0}$ inside and $\frac{\rho R^2}{2\epsilon_0s}$ outside.
2. **Disc on axis:** $E_z=\frac{\sigma}{2\epsilon_0}\left(1-\frac{z}{\sqrt{z^2+R^2}}\right)$; $\to\frac\sigma{2\epsilon_0}$ as $z\to0$ and $\to\frac{Q}{4\pi\epsilon_0z^2}$ for $z\gg R$.
3. **Sphere:** $E=\frac{\rho r}{3\epsilon_0}$ inside ($\frac{Qr}{4\pi\epsilon_0R^3}$) and $\frac{Q}{4\pi\epsilon_0r^2}$ outside.
4. **Planes:** an infinite sheet gives $\frac{\sigma}{2\epsilon_0}$ on each side; two opposite sheets give $\frac\sigma{\epsilon_0}$ between and $0$ outside.
5. **Potential of a shell:** $\Phi=\frac{Q}{4\pi\epsilon_0R}$ inside (constant), $\frac{Q}{4\pi\epsilon_0r}$ outside; for the solid sphere $\Phi_{\rm in}=\frac{Q(3R^2-r^2)}{8\pi\epsilon_0R^3}$.
6. **Dipole:** $\Phi=\frac{p\cos\theta}{4\pi\epsilon_0r^2}$, $E_r=\frac{2p\cos\theta}{4\pi\epsilon_0r^3}$, $E_\theta=\frac{p\sin\theta}{4\pi\epsilon_0r^3}$ (take $-\nabla\Phi$ in spherical coordinates).
7. **Boundary conditions:** from a pillbox show $\Delta E_\perp=\sigma/\epsilon_0$; from a loop show $\Delta E_\parallel=0$; apply to a charged shell (field jumps by $\sigma/\epsilon_0$ at $r=R$).
8. **Energy:** uniformly charged sphere $U=\frac{3}{5}\frac{Q^2}{4\pi\epsilon_0R}$; thin shell $U=\frac{Q^2}{8\pi\epsilon_0R}$; check with $U=\frac{\epsilon_0}2\int E^2d^3x$.
9. **Conductors:** two conducting spheres ($a_1,a_2$) joined by a wire have equal potential, so $\frac{Q_1}{a_1}=\frac{Q_2}{a_2}$ and the surface fields are in the ratio $\frac{E_1}{E_2}=\frac{a_2}{a_1}$ (the lightning-rod effect).
10. **Jackson target (about 1.5):** find the charge density that produces $\Phi=\frac{q}{4\pi\epsilon_0}\frac{e^{-\alpha r}}{r}\left(1+\frac{\alpha r}2\right)$. Answer: a point charge $q$ at the origin plus a cloud $\rho=-\frac{q\alpha^3}{8\pi}e^{-\alpha r}$ (use $\nabla^2\frac{e^{-\alpha r}}{r}=\alpha^2\frac{e^{-\alpha r}}r-4\pi\delta^3$); the total charge is zero (the hydrogen-atom potential). *Do this one first: it returns in Module 17.*

## Optional extension

Verify $U=\frac12\int\rho\Phi\,d^3x$ against $\frac{\epsilon_0}{2}\int E^2d^3x$ for two point charges and identify what changes (the self-energy terms) and what does not (the interaction energy).

## Pitfalls

- Using Gauss's law when the symmetry is not there.
- Forgetting the direction of $\hat{\mathbf n}$ in the boundary condition at a surface.
- Evaluating $\Phi$ at infinity for charge distributions that extend to infinity.
- Treating $\frac12\epsilon_0E^2$ as the interaction energy only (it includes self-energy).

## Gate questions

1. When does Gauss's law determine the field and when not?
2. Why is $\nabla\times\mathbf E=0$ equivalent to the existence of $\Phi$?
3. Why is the field at a conductor's surface $\sigma/\epsilon_0$, not $\sigma/2\epsilon_0$?

## One-page cheat sheet contents

Gauss method card; field-by-integration card; boundary conditions; energy formulas; the shell, sphere, disc, dipole results.
