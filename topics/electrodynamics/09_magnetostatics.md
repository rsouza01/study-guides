# Module 09: Magnetostatics (trimmed to the field content)

**Books:** Griffiths chapter 5 (the engine): §5.1 The Lorentz Force Law (pp. 209 to 221), §5.2 The Biot-Savart Law (pp. 221 to 226), §5.3 The Divergence and Curl of B (pp. 227 to 242), §5.4 Magnetic Vector Potential (pp. 243 to 254); Purcell and Morin 3rd ed. chapter 5 §5.2 to §5.9 (pp. 237 to 267: why magnetism is relativistic) and chapter 6 §6.1 to §6.5 (pp. 278 to 303), §6.3 vector potential (pp. 293 to 296); Jackson 5.1 to 5.6 (pp. 174 to 188), 5.15 Faraday's Law (pp. 208 to 212: preview for Module 10), 5.16 Energy in the Magnetic Field (pp. 212 to 215). **Skip** Jackson 5.7 to 5.14 (magnetic media, ferromagnetism), 5.17 and 5.18.
**Time:** 3 weeks (six sessions). **Tier note:** if diagnostic problem 7 is right, pass the skip-test but still do exercises 2 and 6 and the Jackson target.
**Pinned to:** Griffiths 5th ed. (2024), Jackson 3rd ed. (1999), Purcell and Morin 3rd ed. (2013, SI), Riley, Hobson and Bence 3rd ed. Page numbers are the printed book pages.

## Why this matters

You want $\mathbf A$ promoted from a computational convenience to a fundamental variable. That promotion completes in Module 17. Magnetostatics is also where *Ampere's law plus symmetry* and *Biot-Savart integration* become fluent skills, the magnetic counterparts of Gauss's law and Coulomb integration.

## Skip-test (40 minutes, no notes)

1. Find the field of an infinite straight wire (inside and outside, uniform current density) with Ampere's law.
2. Find the on-axis field of a circular loop with Biot-Savart.
3. Find the field of a long solenoid and of a toroid with Ampere's law.
4. State $\nabla\cdot\mathbf B=0$, $\nabla\times\mathbf B=\mu_0\mathbf J$, define $\mathbf A$ and write $\nabla^2\mathbf A=-\mu_0\mathbf J$ (Coulomb gauge) and $\mathbf A=\frac{\mu_0}{4\pi}\int\frac{\mathbf J}{|\mathbf x-\mathbf x'|}d^3x'$.
5. Define the magnetic dipole moment $\mathbf m=\frac12\int\mathbf x\times\mathbf J\,d^3x$ and give the dipole vector potential, the force and torque on a dipole in an external field.

## Prerequisites

Modules 01 to 03 (vector calculus, Gauss-type recipes); Module 02 (index notation helps with 5.5).

## Detailed topics (checklist)

**Fields from currents [Must]**
- Current density $\mathbf J$, continuity $\nabla\cdot\mathbf J+\partial_t\rho=0$, steady currents $\nabla\cdot\mathbf J=0$; the Lorentz force $\mathbf F=q\mathbf v\times\mathbf B$; Biot-Savart $\mathbf B=\frac{\mu_0}{4\pi}\int\frac{\mathbf J\times(\mathbf x-\mathbf x')}{|\mathbf x-\mathbf x'|^3}d^3x'$.
- Differential and integral equations: $\nabla\cdot\mathbf B=0$, $\nabla\times\mathbf B=\mu_0\mathbf J$, $\oint\mathbf B\cdot d\boldsymbol\ell=\mu_0I_{\rm enc}$; when Ampere's law determines the field (infinite wire, sheet, solenoid, toroid).

**The vector potential [Must]**
- $\mathbf B=\nabla\times\mathbf A$ (legal because $\nabla\cdot\mathbf B=0$); gauge freedom $\mathbf A\to\mathbf A+\nabla\Lambda$; Coulomb gauge $\nabla\cdot\mathbf A=0$ gives $\nabla^2\mathbf A=-\mu_0\mathbf J$ (Poisson's equation, three copies of Module 05); $\mathbf A=\frac{\mu_0}{4\pi}\int\frac{\mathbf J(\mathbf x')}{|\mathbf x-\mathbf x'|}d^3x'$.
- **Magnetic dipole (5.5 to 5.6):** expand $\frac{1}{|\mathbf x-\mathbf x'|}$ for a localized current: no monopole, $\mathbf A=\frac{\mu_0}{4\pi}\frac{\mathbf m\times\mathbf x}{r^3}$ with $\mathbf m=\frac12\int\mathbf x'\times\mathbf J\,d^3x'$; $\mathbf B=\frac{\mu_0}{4\pi}\frac{3\hat{\mathbf n}(\mathbf m\cdot\hat{\mathbf n})-\mathbf m}{r^3}$ (plus a delta function at the origin); force $\mathbf F=\nabla(\mathbf m\cdot\mathbf B)$, torque $\boldsymbol\tau=\mathbf m\times\mathbf B$, energy $U=-\mathbf m\cdot\mathbf B$.

**Energy (5.16) and preview of induction (5.15) [Must]**
- Field energy $W=\frac{1}{2\mu_0}\int B^2d^3x=\frac12\int\mathbf J\cdot\mathbf A\,d^3x$; Faraday's law $\oint\mathbf E\cdot d\boldsymbol\ell=-\frac{d\Phi_B}{dt}$ (finished in Module 10).

## Method cards

**Ampere's law:** (1) name the symmetry and what $\mathbf B$ depends on and its direction (use the right-hand rule); (2) draw the Amperian loop on which $\mathbf B$ is constant and tangent (or perpendicular to the loop segments elsewhere); (3) compute $\oint\mathbf B\cdot d\boldsymbol\ell$; (4) find $I_{\rm enc}$ for each region; (5) check continuity and limits.
**Biot-Savart integration:** (1) draw $\mathbf x$, $\mathbf x'$, $\mathbf R$; (2) $d\mathbf B\propto\frac{I\,d\boldsymbol\ell'\times\mathbf R}{R^3}$; (3) kill components by symmetry; (4) express $R$ and the surviving component with one angle or one coordinate; (5) integrate and check far field ($\to$ dipole) and near field.
**Vector potential:** (1) choose the integral $\mathbf A=\frac{\mu_0}{4\pi}\int\frac{\mathbf J}{R}$ or solve $\nabla^2\mathbf A=-\mu_0\mathbf J$ by symmetry; (2) take the curl; (3) check $\nabla\cdot\mathbf A=0$ and the direction of $\mathbf A$ (parallel to $\mathbf J$).

## Reading plan (pinned to your editions)

A session is part A (read, derive) followed by part B (exercises), about two and a half hours in all. Page numbers are the printed ones.

| Session | A: read and derive | B: do | Done when |
| --- | --- | --- | --- |
| 1 | Griffiths §5.1 to §5.2 (pp. 209 to 226). Purcell §6.1, §6.2, §6.4, §6.5 (pp. 278 to 292, 296 to 303). | Module exercises 1 and 2. Griffiths Problems 5.8, 5.9, 5.11. Purcell Problem 6.12. | Axis field of a loop and the field at the centre of a square loop reproduced. |
| 2 | Griffiths §5.3 (pp. 227 to 242). The Ampère method card. | Module exercises 3 to 5. Griffiths Problems 5.14, 5.15, 5.17, 5.19. Purcell Problem 6.19 and Exercise 6.55 (Helmholtz coils). | Each Ampère problem begins with the symmetry argument and the loop drawn. |
| 3 | Griffiths §5.4 (pp. 243 to 254). Purcell ch. 5 §5.2 to §5.9 (pp. 237 to 267) and §6.3 (pp. 293 to 296). | Module exercise 6. Griffiths Problems 5.25, 5.26, 5.27, 5.29. Purcell Problems 6.4, 6.5, 6.6. | $\mathbf A=\frac12\mathbf B\times\mathbf r$ checked for divergence and curl. |
| 4 | Jackson 5.1 to 5.4 (pp. 174 to 181): compare with Griffiths. The magnetic dipole. | Module exercises 7 and 8. Griffiths Problems 5.36, 5.60. Purcell Problem 6.14. Jackson Problem 5.2. | Dipole potential and torque derived without notes. |
| 5 | Jackson 5.5 to 5.6 (pp. 181 to 188), 5.15 (pp. 208 to 212), 5.16 (pp. 212 to 215). | Module exercise 9 and the **Jackson target** (exercise 10): Jackson Problems 5.3 and 5.13. Griffiths Problem 7.29 for the solenoid energy. | Energy per length of the solenoid equals $\frac12LI^2$ per length. |
| 6 (spare) | Redo failed steps from `error_log.md`. | Optional: Jackson Problems 5.7, 5.9 (coil pair); Purcell Problem 6.22. | No repeated stuck step. |

## Problem set (pinned)

**Pin status:** Pinned: all sections (verified) and problems in all three books (verified). Purcell problems have full solutions in Chapter 12 (ch. 6: pp. 684 to 706).

Tiers: **Must** (do all), **Should** (do when time allows), **Could** (only if the module is going well). A dash in the exercise column means the problem supports the reading rather than a module exercise. Purcell and Morin: stars give difficulty; problems are solved in Chapter 12 (the exercises are not).

| Book | Problem | What it asks | Module exercise | Tier |
| --- | --- | --- | --- | --- |
| Griffiths | 5.8 | field at the centre of a square loop | 2 | Must |
| Griffiths | 5.9 | field at P for the current configurations of the figure | 2 | Must |
| Griffiths | 5.14 | field of a long cylindrical wire, two current distributions | 1 | Must |
| Griffiths | 5.15 | thick slab carrying current | 5 | Must |
| Griffiths | 5.25 | vector potential of a finite straight segment | 6 | Must |
| Griffiths | 5.27 | A = -(1/2) r x B works for uniform B | 6 | Must |
| Griffiths | 5.36 | dipole field in coordinate-free form | 7 | Must |
| Jackson | 5.3 | finite solenoid, the target | 10 | Must |
| Griffiths | 5.11 | field on the axis of a tightly wound solenoid | 2 | Should |
| Griffiths | 5.17 | two coaxial solenoids with opposite currents | 4 | Should |
| Griffiths | 5.19 | field of an infinite solenoid runs parallel to the axis | 4 | Should |
| Griffiths | 5.26 | current density that produces a given A | 6 | Should |
| Griffiths | 5.29 | vector potential above and below a surface current | 6 | Should |
| Griffiths | 5.60 | dipole in a uniform field | 8 | Should |
| Griffiths | 7.29 | energy stored in a section of a long solenoid | 9 | Should |
| Purcell | 6.12 ** | field in the plane of a ring | 2 | Should |
| Purcell | 6.19 *** | solenoid field inside and outside | 4 | Should |
| Purcell | 6.55 ** | Helmholtz coils (exercise) | 3 | Should |
| Purcell | 6.4 * | vector potential for a wire | 6 | Should |
| Jackson | 5.13 | rotating uniformly charged sphere | 10 | Should |
| Purcell | 6.5 ** | vector potential for a finite wire | 6 | Could |
| Purcell | 6.6 *** | zero divergence of A | 6 | Could |
| Purcell | 6.14 *** | far field from a square loop | 7 | Could |
| Jackson | 5.2 | long solenoid of arbitrary cross section | 4 | Could |
| Jackson | 5.7 | compact circular coil | 10 | Could |

## Derive from scratch

1. $\mathbf B=\frac{\mu_0I}{2\pi s}$ for the infinite wire, by Biot-Savart and by Ampere.
2. The on-axis loop field.
3. $\nabla\cdot\mathbf B=0$ and $\nabla\times\mathbf B=\mu_0\mathbf J$ from Biot-Savart (Jackson 5.2).
4. The dipole vector potential from the expansion of $|\mathbf x-\mathbf x'|^{-1}$.
5. $\mathbf A=\frac12\mathbf B\times\mathbf r$ for a uniform field.

## Bare-minimum exercises (with expected results)

1. **Straight wire:** $B=\frac{\mu_0I}{2\pi s}$ outside; for a wire of radius $R$ with uniform $J$, $B=\frac{\mu_0Is}{2\pi R^2}$ inside.
2. **Loop on the axis:** $B_z=\frac{\mu_0Ia^2}{2(a^2+z^2)^{3/2}}$; at the centre $\frac{\mu_0I}{2a}$; for $z\gg a$ it matches the dipole field with $m=I\pi a^2$.
3. **Helmholtz pair:** two coaxial loops separated by their radius $a$ have a nearly uniform field at the midpoint, $B=\left(\frac45\right)^{3/2}\frac{\mu_0I}{a}\approx0.716\frac{\mu_0I}{a}$ per turn (the second derivative of $B_z$ vanishes there).
4. **Solenoid and toroid:** $B=\mu_0nI$ inside a long solenoid and $0$ outside; a toroid of $N$ turns has $B=\frac{\mu_0NI}{2\pi s}$ inside the winding.
5. **Surface current:** a sheet with surface current $K$ gives $B=\frac{\mu_0K}{2}$ on each side (opposite directions); the discontinuity across the sheet is $\mu_0K$.
6. **Vector potential:** a uniform field $B\hat{\mathbf z}$ has $\mathbf A=\frac B2(-y,x,0)$ ($\nabla\cdot\mathbf A=0$); an infinite solenoid of radius $R$ has $A_\phi=\frac{Br}2$ ($r<R$) and $\frac{BR^2}{2r}$ ($r>R$): *nonzero* outside where $\mathbf B=0$ (the Aharonov-Bohm set-up; flux $\Phi=\pi R^2B=\oint\mathbf A\cdot d\boldsymbol\ell$).
7. **Dipole:** for a loop $\mathbf m=I\mathbf a$; $\mathbf A=\frac{\mu_0}{4\pi}\frac{\mathbf m\times\mathbf r}{r^3}$ and $\mathbf B=\frac{\mu_0}{4\pi r^3}\left[3(\mathbf m\cdot\hat{\mathbf r})\hat{\mathbf r}-\mathbf m\right]$; compare with the electric dipole field of Module 03.
8. **Force and torque:** $\boldsymbol\tau=\mathbf m\times\mathbf B$, $U=-\mathbf m\cdot\mathbf B$, $\mathbf F=\nabla(\mathbf m\cdot\mathbf B)$; show that a dipole in a field of a long straight wire at distance $s$ with $\mathbf m$ parallel to $\mathbf B$ feels a force toward the wire.
9. **Energy:** the energy per unit length of a long solenoid is $\frac{B^2}{2\mu_0}\pi R^2=\frac12LI^2$ with $L=\mu_0n^2\pi R^2$ per unit length (as a check of $W=\frac1{2\mu_0}\int B^2$; do not dwell on inductance).
10. **Jackson target (about 5.3 and one magnetic-moment problem):** the vector potential of a circular current loop (radius $a$, current $I$) in the far field: $A_\phi=\frac{\mu_0Ia^2\sin\theta}{4r^2}$ ($=\frac{\mu_0m\sin\theta}{4\pi r^2}$ with $m=I\pi a^2$), and a moment problem: the torque and force on a small loop in a given field.

## Optional extension

Derive the exact vector potential of a circular loop in terms of elliptic integrals (Jackson 5.5, awareness) and check that the dipole formula is its far-field limit.

## Pitfalls

- Using Ampere's law when the symmetry is not there.
- Mixing up $\mathbf B$ and $\mathbf H$ (we stay with $\mathbf B$ and $\mu_0$).
- Forgetting that $\mathbf A$ is parallel to $\mathbf J$ and gauge-dependent.
- Taking the dipole field $\propto m/r^3$ at the origin literally (it needs the delta-function term).

## Gate questions

1. Why does $\nabla\cdot\mathbf B=0$ allow a vector potential and what freedom does it leave?
2. Why is $\mathbf A$ nonzero outside an ideal solenoid?
3. Why is there no magnetic monopole term in the multipole expansion?

## One-page cheat sheet contents

Ampere and Biot-Savart cards; wire, loop, solenoid, toroid results; vector potential equations; dipole formulas; field energy.
