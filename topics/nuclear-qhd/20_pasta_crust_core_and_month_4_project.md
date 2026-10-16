# Module 20: Pasta, the crust-core boundary, and the Month-4 project (Week 19)

**Books (light reading, about 3 hours):** Chamel and Haensel section 3.3 on pasta; Ravenhall, Pethick and Wilson (1983) and Hashimoto et al. (1984); the thermodynamic instability condition for uniform $npe$ matter (Pethick-Ravenhall 1995; HPY chapter 6).
**Time:** 1 week (consolidation).

## Why this matters

↪ The instability criterion is a fissility condition applied to a cell: as the nuclear volume fraction $u$ grows the screened Coulomb energy and the surface energy make a deformation of the cell (spheres $\to$ rods $\to$ slabs, then the inverse phases) favourable. The transition density near $n\approx0.08$ fm$^{-3}$ is a strong function of $L$: **stiffer symmetry energy $\Rightarrow$ lower transition density $\Rightarrow$ thinner crust.** (Check the ratio convention: Module 19's correction applies.) This module closes Month 4 with a gate and **the second payoff**.

## Skip-test (40 minutes, no notes)

1. Name the pasta phases in order of increasing nuclear volume fraction.
2. State the thermodynamic instability criterion of uniform $npe$ matter and where it puts the crust-core transition.
3. State how the transition density depends on $L$ and why.
4. Estimate $\Delta R$ of the crust at $1.4M_\odot$ with a thin-layer argument.
5. Explain why the pasta energy differences are small.

## Prerequisites

Modules 17, 19.

## Detailed topics (checklist)

**Pasta [Must]**
- As the density increases the cell shape passes through spheres ("gnocchi"), rods ("spaghetti"), slabs ("lasagna"), then the inverse phases (tubes, bubbles) before uniform matter; the Coulomb functions $\Phi_d(u)$ for dimensionality $d=3,2,1$: $\Phi_3=\tfrac15(2-3u^{1/3}+u)$, $\Phi_2=\tfrac14(u-1-\ln u)$, $\Phi_1=\frac{(1-u)^2}{3u}$; at the optimal size the energy density scales as $u\,(d\sigma)^{2/3}\Phi_d^{1/3}$, so the preferred geometry minimises $d^2\Phi_d(u)$ (equal at the transitions); the energy differences between phases are very small (keV per nucleon), so the effect on the EOS is below 1 percent but matters for transport.

**The crust-core boundary [Must]**
- Uniform $npe$ matter in $\beta$ equilibrium is stable against long-wavelength density fluctuations if the thermodynamic stability condition holds (positive curvature of the energy with respect to $n_B$ at fixed neutrality and chemical equilibrium); it fails at $n\approx0.08$ fm$^{-3}$ for typical Skyrme sets, signalling the onset of clustering; with the Coulomb interaction the dynamical (finite-wavelength) criterion is satisfied later than the thermodynamic one and the transition is slightly lower in density.
- **Dependence on $L$:** the transition density decreases as $L$ increases (roughly from $\sim0.09$ fm$^{-3}$ at $L\approx30$ MeV to $\sim0.065$ fm$^{-3}$ at $L\approx100$ MeV; approximate): a stiff symmetry energy keeps the proton fraction low and clustering sets in earlier, giving a **thinner crust**.

**Crust observables [Should]**
- Crust thickness $\Delta R\sim1$ km, $\Delta M\sim0.01$ to $0.05\ M_\odot$, $\frac{\Delta I}{I}\sim$ a few percent (a fraction of which participates in glitches), all increasing as $L$ decreases.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Chamel-Haensel 3.3; the pasta sequence; exercises 1 and 2 |
| Session 2 | The instability criterion; $L$ dependence; exercises 3 and 4 |
| Session 3 | Crust observables; exercises 5 to 8 |
| Session 4 | The Month-4 gate and the computational task |

## Derive from scratch

1. The Coulomb functions $\Phi_d(u)$ (or at least $\Phi_3$) from the Wigner-Seitz cell.
2. The optimal energy density $\propto u(d\sigma)^{2/3}\Phi_d^{1/3}$.
3. The stability condition for uniform $npe$ matter.
4. The thin-layer estimate of $\Delta R$.
5. The $L$ dependence of the transition density.

## Bare-minimum exercises (with expected results)

1. **Pasta order:** spheres (gnocchi) $\to$ rods (spaghetti) $\to$ slabs (lasagna) $\to$ tubes (anti-spaghetti) $\to$ bubbles (anti-gnocchi) $\to$ uniform; the inverse phases follow from $u\to1-u$.
2. **Geometry competition:** minimising $d^2\Phi_d(u)$ among $d=3,2,1$ gives sphere-to-rod at $u\approx0.2$ and rod-to-slab at $u\approx0.35$ in this simple model (real calculations shift these by small amounts); verify numerically.
3. **Transition density and $L$:** for SLy4 ($L=46$ MeV) the thermodynamic transition is near $n\approx0.08$ fm$^{-3}$; for a stiffer set ($L\approx100$ MeV) near $0.065$ fm$^{-3}$ (approximate): state the sign of $\frac{dn_t}{dL}$ and why a larger $L$ means a lower $n_t$.
4. **Thin-layer crust thickness:** with $P_t\approx0.5$ MeV/fm$^3$ ($8\times10^{32}$ dyn/cm$^2$) at the crust-core boundary, mean crust density $\sim5\times10^{13}$ g/cm$^3$ and $g\approx2\times10^{14}$ cm/s$^2$ (GR-corrected for $1.4M_\odot$, $R=12$ km): $\Delta R\approx\frac{P_t}{\bar\rho g}\approx0.8$ km.
5. **Crust mass:** $\Delta M\approx4\pi R^2\Delta R\,\bar\rho\approx4\pi(1.2\times10^6)^2\times8\times10^4\times5\times10^{13}\approx7\times10^{31}$ g $\approx0.035M_\odot$; $\frac{\Delta I}{I}$ is a few percent; state the dependence on $L$ (smaller $L\Rightarrow$ thicker crust).
6. **Small energy differences:** show the difference between the optimal pasta energy and the sphere-only energy is $\ll1$ percent of the cell energy; so the EOS is insensitive but the shear modulus and transport are not.
7. **Instability criterion:** write the condition on $\frac{\partial P}{\partial n_B}$ for $npe$ matter with $x_p(n_B)$ from $\beta$ equilibrium and explain qualitatively how its value depends on the derivative of $S(n)$ (i.e. on $L$) through the proton fraction.
8. **Fissility analogy:** apply the Module 14 logic: the sphere becomes unstable to deformation to rods when the effective fissility of the cell (with screened Coulomb energy) reaches 1; state what changes relative to the isolated nucleus.
9. **Observational link:** list three observations sensitive to the crust thickness: glitch activity (moment of inertia), the cooling of quiescent transients, and magnetar QPO frequencies.
10. **Month-4 gate prep:** attempt the six items below.

## Blank-page gate: Month 4

1. $E/A(n,\delta)$ and its expansion; the five numbers; **what each controls in a star.**
2. The free Fermi gas does not saturate; the two escapes.
3. $G$-matrix, Coester line, why QHD exists.
4. The drip condition; the density; the physics.
5. The inner-crust cell functional; the virial relation; why nuclei grow with depth.
6. The crust-core criterion and its $L$ dependence.

## Computational task: **the second payoff**

Extend Module 05's code inward with a Skyrme functional (SLy4 parameters are published and short): implement the CLDM inner crust minimising over $(A,Z,n_{\rm gas},R_{\rm cell})$ at fixed $P$; locate drip from your outer-crust endpoint; locate the crust-core transition by thermodynamic instability; output a continuous, **thermodynamically consistent** $P(\rho)$ from $10^6$ to $\sim10^{14}$ g/cm$^3$, verifying $P=n^2\frac{d(\varepsilon/n)}{dn}$ numerically everywhere.

Then feed it to `tov-solver.py` with a fixed core EOS and compute **$\Delta R$, $\Delta M$, $\Delta I/I$** at $1.4M_\odot$. Repeat with a different-$L$ Skyrme set and watch all three move.

**Cut if behind:** drop the superfluidity/entrainment orientation and the pasta reading. **Never** drop Module 17 or the computational task.

## Optional extension

Include the pasta phases by adding the geometry-dependent Coulomb functions to the CLDM cell energy and show the EOS changes by well under 1 percent while the transition density is unchanged.

## Pitfalls

- Equating the thermodynamic instability density with the dynamical one.
- Forgetting that crust thickness depends on both $L$ and the core EOS.
- Using different Skyrme parameter sets in the crust and core (thermodynamic inconsistency).

## Gate questions

1. Why does a larger $L$ give a thinner crust?
2. Why do pasta phases barely change the EOS?
3. What does thermodynamic consistency require at the seams?

## One-page cheat sheet contents

Pasta sequence and $\Phi_d$; instability criterion and $L$ dependence; thin-layer estimates; the computational recipe.
