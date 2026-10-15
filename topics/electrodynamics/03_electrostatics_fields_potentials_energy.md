# Module 03: Electrostatics I: fields, potentials and energy

**Books:** Griffiths chapter 2 (the engine); Purcell chapters 1 to 3 (intuition); Jackson 1.1 to 1.7 and 1.11 (read after Griffiths; skip the capacitance subsection of 1.11).
**Time:** 3 weeks (six sessions). **Tier note:** if the diagnostic problems 1 to 4 are all right, pass the skip-test and do only the Jackson target (exercise 10).

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

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Griffiths 2.1 to 2.2 (field, divergence and curl); the Gauss method card; Purcell chapter 1 |
| B1 | Exercises 1 to 4 |
| A2 | Griffiths 2.3 (potential); Purcell chapter 2 |
| B2 | Exercises 5 and 6 |
| A3 | Griffiths 2.4 to 2.5 (work, energy, conductors); Purcell chapter 3 |
| B3 | Exercises 7 to 9 |
| A4 | Jackson 1.1 to 1.7, 1.11 (read; note what is new compared with Griffiths) |
| B4 | **Jackson target:** exercise 10 |

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
