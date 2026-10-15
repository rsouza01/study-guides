# Module 13: Phase transitions and critical phenomena

**Books:** Callen (first-order phase transitions and critical phenomena in Part I), Schroeder (chapter 5 on phase transformations and chapter 8 on the Ising model and mean-field theory), Pathria (chapter 12: phase transitions, criticality, universality, scaling), Swendsen (Ising model, mean-field theory, phase transitions), Mandl, Blundell and Blundell.
**Time:** 2 weeks.

## Why this matters for stars and EOS

- **Liquid-solid** (crystallization of the white dwarf core, with latent heat and phase separation of mixtures), **nuclear liquid-gas** and **hadron-quark** transitions are first-order transitions whose treatment (Maxwell versus Gibbs construction) changes the EOS and the structure of the star.
- **Landau theory** is the simplest tool for order parameters, symmetry breaking and the thermodynamics near a transition; it is used for superfluids/superconductors (pairing gaps), chiral transitions and nuclear matter.
- The logic of **mean-field theory** (Weiss/Hartree) reappears in self-consistent models of dense matter.

## Skip-test (40 minutes, no notes)

1. For the mean-field Ising model derive $m=\tanh\left(\beta(Jzm+h)\right)$, $T_c=\frac{zJ}{k}$ and the spontaneous magnetization near $T_c$: $m\approx\sqrt{3(1-T/T_c)}$.
2. Write the Landau free energy $F=F_0+a(T-T_c)m^2+bm^4$ and derive $m^2=\frac{a(T_c-T)}{2b}$ and the specific-heat jump $\Delta C=\frac{a^2T_c}{2b}$.
3. State the mean-field critical exponents ($\alpha=0$, $\beta=\frac12$, $\gamma=1$, $\delta=3$).
4. For the van der Waals fluid obtain the critical point and the Maxwell equal-area construction.
5. State the Gibbs conditions for phase coexistence when two quantities are conserved (e.g., baryon number and charge) and contrast them with the Maxwell construction (one conserved quantity).

## Prerequisites

Modules 03, 05, 08.

## Detailed topics (checklist)

**First-order transitions**
- Coexistence curve, latent heat, Clausius-Clapeyron (Module 05); metastability, supercooling, spinodal, nucleation (qualitative: free-energy barrier $\Delta F=\frac{16\pi\sigma^3}{3(\Delta\mu\,n)^2}$ with surface tension $\sigma$).
- Van der Waals as a model with a first-order transition and critical point; law of corresponding states.
- **The Maxwell construction** (equal areas; $\mu$ and $P$ equal in the two phases; a flat $P$ plateau as a function of volume).
- **Gibbs construction with two conserved charges:** two chemical potentials (for example baryon and electric charge) and equality of $P$, $\mu_1$, $\mu_2$ across the phases with only *global* neutrality; the pressure then varies along the mixed phase (it is not constant), a finite-size correction (surface and Coulomb energies) pushes the result toward the Maxwell case.

**Second-order and critical phenomena**
- Order parameters and broken symmetry; the Ising model (exact in 1D, no transition; 2D Onsager, awareness); mean-field (Weiss/Bragg-Williams) solution: self-consistency, $T_c=zJ/k$, susceptibility $\chi\propto|T-T_c|^{-1}$, specific-heat jump.
- **Landau theory:** expansion of the free energy in the order parameter, symmetric ($m^2,m^4$) and with a cubic term (first-order transition); the role of an external field; critical exponents in mean field; the Ginzburg criterion (awareness: mean field fails near $T_c$ in low dimensions).
- Fluctuations and correlation length (awareness): universality and scaling exist; renormalization group beyond scope.

**Condensation and superfluid-type transitions (awareness)**
- Bose-Einstein condensation (Module 11) as a transition; the BCS gap equation as a self-consistent mean-field order parameter with $\Delta_0=1.764\,kT_c$ (derived elsewhere).

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Callen: first-order phase transitions; Schroeder chapter 5 phase transformations |
| Lunch 2 | Schroeder chapter 8: the Ising model and mean-field theory |
| Lunch 3 | Callen: critical phenomena; Landau theory |
| Lunch 4 | Pathria chapter 12 (the basic ideas); Swendsen on the Ising model |
| Week 2 lunches | Maxwell versus Gibbs construction (Callen and a nuclear/compact-star reference if available); review |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. The mean-field Ising self-consistency, $T_c$, and the critical exponents $\beta,\gamma$.
2. The Landau theory results: $m(T)$, $\Delta C$, susceptibility.
3. The Maxwell equal-area construction from $\mu_1=\mu_2$.
4. The Landau theory with a cubic term: a first-order transition and the discontinuity of $m$.
5. The two-charge Gibbs construction: conditions on $(\mu_1,\mu_2,P)$.

## Bare-minimum exercises (find matching problems with keywords: Ising model, mean-field, Landau theory, van der Waals, first-order transition, critical exponent)

1. **Mean-field Ising:** solve $m=\tanh(m\,T_c/T)$ graphically and numerically for $T/T_c=0.5,0.9,0.99$ and compare $m$ with $\sqrt{3(1-T/T_c)}$ near $T_c$.
2. **Susceptibility:** show $\chi=\frac{\partial m}{\partial h}\propto\frac1{T-T_c}$ above $T_c$ (Curie-Weiss law).
3. **Landau theory:** with $F=a(T-T_c)m^2+bm^4-hm$ show $m\propto(T_c-T)^{1/2}$, the field response $m\propto h^{1/3}$ at $T_c$, and the specific-heat discontinuity $\Delta C=\frac{a^2T_c}{2b}$.
4. **Landau first-order:** add a cubic term $-cm^3$ and show that the free energy then has two degenerate minima (a first-order transition) at a temperature $T_1$ slightly above the temperature where the quadratic coefficient vanishes; and show that with $F=a(T-T_c)m^2-cm^3+bm^4$ the transition occurs at $a(T_1-T_c)=\frac{c^2}{4b}$ with a jump $m^*=\frac{c}{2b}$ (from the condition that $a(T-T_c)-cm+bm^2$ has a double root).
5. **Van der Waals critical constants:** $kT_c=\frac{8a}{27b}$, $v_c=3b$, $P_c=\frac{a}{27b^2}$, $\frac{P_cv_c}{kT_c}=\frac38$; and the law of corresponding states.
6. **Equal-area construction:** at $T=0.9T_c$ solve the Maxwell construction numerically for the reduced van der Waals EOS $\tilde P=\frac{8\tilde T}{3\tilde v-1}-\frac3{\tilde v^2}$: coexistence pressure $\tilde P\approx0.647$ and volumes $\tilde v\approx0.603$ and $1.6$ (verify numerically).
7. **Spinodal and stability:** locate the spinodal curve $\partial P/\partial v=0$ for the same EOS and show the region $\kappa_T<0$ is unstable.
8. **Surface tension and nucleation:** for a droplet of radius $r$ with surface tension $\sigma$ and bulk free-energy gain per volume $\Delta f$ obtain the critical radius $r_c=2\sigma/\Delta f$ and barrier $\Delta F=\frac{16\pi\sigma^3}{3\Delta f^2}$.
9. **Two-charge Gibbs construction:** for a toy transition between a phase 1 with energy density $\epsilon_1(n_1,q_1)$ and a phase 2 with $\epsilon_2(n_2,q_2)$ with total baryon density $n$ and total charge zero, write the Gibbs conditions and explain why the mixed-phase pressure rises with density (unlike a Maxwell plateau).
10. **Crystallization of a plasma:** with the OCP coupling parameter (Module 12) identify the liquid-solid transition at $\Gamma_m\approx175$; show that the latent heat per ion is a small fraction of $kT$ ($\approx0.77kT$; verify in your reference).

## Optional extension

Derive the Gibbs-Bogoliubov or the Ginzburg-Landau argument for the failure of mean-field theory near $T_c$ in $d<4$ and explain why mean-field is accurate for long-range interactions (the Coulomb crystal, nuclear mean fields).

## Pitfalls

- Using the Maxwell construction when two conserved charges require a Gibbs construction.
- Confusing the order parameter with the field conjugate to it.
- Using the Landau expansion far from $T_c$.
- Believing mean-field exponents hold near critical points in 3D (they do not).

## Gate questions

1. Why does the existence of a van der Waals loop signal a first-order transition?
2. Why does a first-order transition between phases with two conserved charges not have a constant pressure in the mixed phase?
3. What do $\alpha,\beta,\gamma,\delta$ describe, and why are they universal?

## One-page cheat sheet contents

Mean-field Ising; Landau expansion results; vdW critical constants; Maxwell and Gibbs conditions; nucleation formulas.
