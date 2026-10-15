# Module 12: Conservation laws, discrete symmetries and plane waves

**Books:** Griffiths chapter 8 (conservation laws: Poynting, the Maxwell stress tensor, momentum, angular momentum) and chapter 9 (electromagnetic waves, 9.1 to 9.2); Purcell chapter 9; Jackson **6.7** (Poynting's theorem: conservation of energy and momentum, the Maxwell stress tensor), 6.9 (harmonic fields: light), **6.10** (transformations under rotations, spatial inversion and time reversal), 6.11 to 6.12 (magnetic monopoles, Dirac's quantization: optional, 90 minutes, and one of the most beautiful arguments in the book), 7.1 to 7.2 (plane waves, polarization, Stokes parameters: a coda, about four hours). **Skip** Jackson 6.8 (dissipative media) and 6.6 (macroscopic equations; skim).
**Time:** 3 weeks (six sessions).

## Why this matters

$T^{\mu\nu}$ arrives here as bookkeeping for momentum flux. In Module 18 it arrives again as the Noether current of spacetime translations. Seeing the same object from two directions is worth the trip (and your mechanics guide's Noether module is the other half). And 6.10 is your first encounter with **P and T as operators acting on fields**, the classical rehearsal for the discrete symmetries of QFT.

## Skip-test (40 minutes, no notes)

1. Derive Poynting's theorem $\partial_tu+\nabla\cdot\mathbf S=-\mathbf J\cdot\mathbf E$ with $u=\frac12\left(\epsilon_0E^2+\frac{B^2}{\mu_0}\right)$ and $\mathbf S=\frac{1}{\mu_0}\mathbf E\times\mathbf B$.
2. State momentum density $\mathbf g=\epsilon_0\mathbf E\times\mathbf B=\mathbf S/c^2$ and the Maxwell stress tensor $T_{ij}=\epsilon_0\left(E_iE_j-\frac12\delta_{ij}E^2\right)+\frac1{\mu_0}\left(B_iB_j-\frac12\delta_{ij}B^2\right)$; write the conservation law $\frac{d}{dt}(\mathbf P_{\rm mech}+\mathbf P_{\rm field})=\oint\mathbf T\cdot d\mathbf a$.
3. Find $\omega=ck$, $\mathbf B=\frac1c\hat{\mathbf k}\times\mathbf E$ for a plane wave and compute $\langle u\rangle$, $\langle\mathbf S\rangle$, and the radiation pressure on an absorber and a mirror.
4. Tabulate how $\mathbf E$, $\mathbf B$, $\rho$, $\mathbf J$ transform under P and T and show Maxwell's equations are invariant.
5. Describe linear, circular and elliptical polarization and the Stokes parameters.

## Prerequisites

Modules 03, 09, 10, 11 (at least the wave equation); mechanics guide Module 04 helps for the symmetry reading.

## Detailed topics (checklist)

**Energy and momentum conservation (6.7) [Must]**
- Work done on charges $\int\mathbf J\cdot\mathbf E\,d^3x$; Poynting's theorem; energy density $u$ and flux $\mathbf S$; electromagnetic momentum density $\mathbf g=\epsilon_0\mathbf E\times\mathbf B$; the **Maxwell stress tensor** $T_{ij}$ (momentum flux; force on charges in a volume $\mathbf F=\oint\mathbf T\cdot d\mathbf a-\frac{1}{c^2}\frac{d}{dt}\int\mathbf S\,d^3x$); angular momentum density $\mathbf x\times\mathbf g$; electrostatic pressure on a conductor $\frac{\epsilon_0E^2}{2}=\frac{\sigma^2}{2\epsilon_0}$.
- Examples: energy flow into a resistor and into a charging capacitor; the Poynting vector of a coaxial cable ($P=VI$).

**Plane waves (7.1 to 7.2, Griffiths 9) [Should]**
- $\mathbf E=\mathbf E_0e^{i(\mathbf k\cdot\mathbf x-\omega t)}$, $\omega=ck$, $\mathbf k\cdot\mathbf E_0=0$, $\mathbf B=\frac1c\hat{\mathbf k}\times\mathbf E$; polarization (linear, circular $\mathbf E_0=E_0(\hat{\mathbf x}\pm i\hat{\mathbf y})$, elliptical); Stokes parameters; intensity $I=\frac12c\epsilon_0E_0^2$; radiation pressure $\frac Ic$ (absorbed) or $\frac{2I}{c}$ (reflected).

**Discrete symmetries (6.10) [Must]**
- Under **parity**: $\mathbf E\to-\mathbf E$ (polar), $\mathbf B\to+\mathbf B$ (axial, a pseudovector), $\rho\to\rho$, $\mathbf J\to-\mathbf J$; under **time reversal**: $\mathbf E\to\mathbf E$, $\mathbf B\to-\mathbf B$, $\rho\to\rho$, $\mathbf J\to-\mathbf J$; Maxwell's equations are invariant under both; rotations as the continuous symmetry (a vector rotates as a vector).

**Monopoles and Dirac quantization (6.11 to 6.12) [Could]**
- Maxwell's equations with magnetic charge; duality; the Dirac condition $eg=\frac{n\hbar c}{2}$ (Gaussian) from the quantization of angular momentum in the field of a charge-monopole pair: charge quantization from a single monopole.

## Method cards

**Poynting flux problem:** (1) find $\mathbf E$ and $\mathbf B$ in the region; (2) compute $\mathbf S=\frac1{\mu_0}\mathbf E\times\mathbf B$ with its direction; (3) integrate over the surface; (4) compare with $\frac{dU}{dt}$ or the dissipated power; (5) check that it is conserved.
**Stress-tensor force:** (1) choose a closed surface surrounding the charges; (2) compute $T_{ij}n_j$ on it (diagonal components in the symmetric directions first); (3) integrate; (4) add the field-momentum term if the fields change in time; (5) check with the direct Coulomb/Lorentz force.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Griffiths 8.1 (Poynting); Jackson 6.7 first half |
| B1 | Exercises 1 to 3 |
| A2 | Griffiths 8.2 (momentum, stress tensor); Jackson 6.7 second half |
| B2 | Exercises 4 to 6 |
| A3 | Jackson 6.10 and Griffiths 9.1 to 9.2 |
| B3 | Exercises 7 and 8 |
| A4 | Jackson 7.1 to 7.2 (coda); 6.11 to 6.12 (optional) |
| B4 | Exercises 9 and 10; **Jackson targets** |
| A5/B5 | Spare sessions; the Month-3 gate |

## Derive from scratch

1. Poynting's theorem from Maxwell's equations and the Lorentz force.
2. The Maxwell stress tensor from the force on a charge distribution.
3. $\omega=ck$ and $\mathbf B=\frac1c\hat{\mathbf k}\times\mathbf E$ for a plane wave.
4. The P and T transformations of all fields.
5. The radiation pressure on an absorber.

## Bare-minimum exercises (with expected results)

1. **Resistive wire:** current $I$ in a wire of radius $a$ and length $\ell$ (resistance $R$) has $E=\frac{IR}{\ell}$ along the wire and $B=\frac{\mu_0I}{2\pi a}$ at the surface; $\mathbf S$ points *inward* with magnitude $\frac{EB}{\mu_0}$ and the total power through the surface is $I^2R$.
2. **Charging capacitor:** with plates of radius $R$ and gap $d$, show that the Poynting flux through the cylindrical side surface equals $\frac{d}{dt}\left(\frac12CV^2\right)$.
3. **Plane wave numbers:** for sunlight ($I=1361$ W/m$^2$) the amplitude is $E_0=\sqrt{\frac{2I}{c\epsilon_0}}\approx1.0\times10^3$ V/m and $B_0=\frac{E_0}{c}\approx3.4\ \mu$T; the radiation pressure is $\frac Ic\approx4.5\ \mu$Pa (absorbing) or $9.1\ \mu$Pa (reflecting).
4. **Coaxial cable:** for a coaxial cable (radii $a<b$) with potential difference $V$ and current $I$ the fields between the conductors are $E=\frac{V}{\rho\ln(b/a)}$ and $B=\frac{\mu_0I}{2\pi\rho}$; the Poynting flux integrated over the annulus $a<\rho<b$ is $VI$.
5. **Electrostatic pressure:** from $T_{ij}$ show that the force per unit area on a conductor with surface charge $\sigma$ is $\frac{\sigma^2}{2\epsilon_0}$ outward (use the field $\frac\sigma{\epsilon_0}$ outside and $0$ inside).
6. **Stress-tensor force:** two equal charges $q$ at separation $2d$: integrate $T_{zz}$ over the mid-plane to get the force $\frac{q^2}{4\pi\epsilon_0(2d)^2}$ (a classic check; the force on one charge equals the flux of momentum through the plane that separates them).
7. **Maxwell's equations under P and T:** verify each of the four equations is invariant given the transformation table; explain why $\mathbf B$ is a pseudovector.
8. **Polarization:** $\mathbf E_0=E_0(\hat{\mathbf x}+i\hat{\mathbf y})$ gives a field rotating counterclockwise (seen head-on, positive helicity); write $\mathrm{Re}\,\mathbf E$ and show the Stokes parameter $V=\pm I$.
9. **Dirac quantization (optional):** in Gaussian units a charge $e$ and a monopole $g$ have angular momentum $\frac{eg}{c}$ in their fields; requiring it to be $\frac{n\hbar}2$ gives $eg=\frac{n\hbar c}{2}$ and a minimum $g=\frac{\hbar c}{2e}=\frac{e}{2\alpha}\approx68.5\,e$.
10. **Jackson targets (about 6.2 and one stress-tensor force problem):** (a) derive the continuity equation from Maxwell's equations and the conservation of $\int(\mathbf x\times\mathbf g)\,d^3x$ in a simple geometry; (b) a stress-tensor force problem such as the force between two hemispheres of a uniformly charged sphere or the force on a half-space charge via $\oint T_{ij}n_jda$ (do exercise 6 first).

## Optional extension

Show that the angular momentum carried by a circularly polarized plane wave per unit energy is $\frac{1}{\omega}$ (photon spin $\hbar$ per photon of energy $\hbar\omega$), the classical shadow of photon helicity.

## Pitfalls

- Treating $\mathbf S$ as "where the energy is" (it is the flux; there is also the question of the contributions that cancel).
- Forgetting the field-momentum term when the fields change in time.
- Sign of $T_{ij}$ (momentum flux versus stress).
- Confusing a polar vector ($\mathbf E$) with an axial vector ($\mathbf B$) under parity.

## Gate questions

1. What does $\mathbf S$ represent and how does it enter Poynting's theorem?
2. Why is $\mathbf B$ a pseudovector and what does that imply for P and T?
3. What does the Maxwell stress tensor encode and why does it re-appear as the Noether current in Module 18?

## One-page cheat sheet contents

Poynting's theorem; $\mathbf g$ and $T_{ij}$; plane-wave relations and numbers; P and T table; Dirac condition.
