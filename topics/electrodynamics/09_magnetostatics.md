# Module 09: Magnetostatics (trimmed to the field content)

**Books:** Griffiths chapter 5 (the engine); Purcell chapters 5 to 6 (the fields of moving charges and the magnetic field: the best account of why magnetism is relativistic; read for understanding); Jackson 5.1 to 5.6 (Biot-Savart, the differential equations of magnetostatics, the vector potential, the vector potential of a localized current, magnetic moment, force and torque), 5.15 (Faraday's law: preview for Module 10), 5.16 (magnetic field energy). **Skip** Jackson 5.7 to 5.14 (magnetic media, ferromagnetism, boundary-value problems with $\mu$), 5.17 (self and mutual inductance: circuits) and 5.18 (eddy currents, magnetic diffusion).
**Time:** 3 weeks (six sessions). **Tier note:** if diagnostic problem 7 is right, pass the skip-test but still do exercises 2 and 6 and the Jackson target.

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

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Griffiths 5.1 to 5.2 (Lorentz force, Biot-Savart); Purcell chapter 6 |
| B1 | Exercises 1 and 2 |
| A2 | Griffiths 5.3 (divergence and curl of $\mathbf B$, Ampere's law); Ampere card |
| B2 | Exercises 3 to 5 |
| A3 | Griffiths 5.4 (vector potential); Purcell chapter 5 (why magnetism is relativistic) |
| B3 | Exercise 6 |
| A4 | Jackson 5.1 to 5.4 (compare with Griffiths); the magnetic dipole |
| B4 | Exercises 7 and 8 |
| A5 | Jackson 5.5 to 5.6, 5.15 to 5.16 |
| B5 | Exercise 9 and **Jackson target** (exercise 10) |
| A6/B6 | Spare sessions |

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
