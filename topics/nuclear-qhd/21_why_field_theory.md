# Module 21: Why field theory (Week 20): Month 5 begins, Walecka Part 2

**Books:** Walecka's "Why Field Theory" chapter. **Companion reading all month:** **Serot and Walecka, *Adv. Nucl. Phys.* 16 (1986) 1** (canonical QHD pedagogy, clearer than the book in places) and **Serot and Walecka, *Int. J. Mod. Phys.* E6 (1997) 515** (nucl-th/9701058, free).
**Time:** 1 week.

## Why this matters

Three arguments you should be able to make unprompted. (i) **Causality**: non-relativistic potential models develop $v_s>c$; a covariant field theory cannot. Structural, not aesthetic, for a maximum-mass calculation. (ii) **The large fields**: Dirac phenomenology demands scalar and vector potentials of several hundred MeV each, nearly cancelling; the small binding is a *difference of large numbers*. (iii) **Extrapolation** to 5 to 10 $n_0$.

## Skip-test (40 minutes, no notes)

1. Show a non-relativistic $P\propto n^\Gamma$ with $\Gamma>2$ violates causality above some density and find it for a typical Skyrme force.
2. Write the Dirac equation with scalar $S$ and vector $V$ potentials and take the non-relativistic reduction.
3. Show the spin-orbit term $\propto\frac1r\frac{d}{dr}(V-S)$ is the *sum* of large potentials in magnitude while central binding is the *difference* $V+S$.
4. State why this resolves the anomalous spin-orbit strength of Module 10.
5. Explain why a covariant theory is causal by construction.

## Prerequisites

Modules 02, 08, 10 and 17; the Dirac equation (Zettili guide Module 11, if you have it).

## Detailed topics (checklist)

**Causality [Must]**
- Sound speed $v_s^2=\frac{dP}{d\varepsilon}\le c^2$; for non-relativistic matter $\varepsilon\simeq Mn$, so $v_s^2/c^2\approx\frac{1}{M}\frac{dP}{dn}$; a potential model with a stiff repulsive core can give $\frac{dP}{dn}>M$ above some density. Check with Skyrme: SLy4 pure neutron matter becomes acausal at $n\approx1.2$ fm$^{-3}$ ($\approx7n_0$, $\rho\approx2\times10^{15}$ g/cm$^3$), symmetric matter at $\approx1.3$ fm$^{-3}$: just inside the central densities of massive neutron stars.

**The Dirac equation with scalar and vector potentials [Must]**
- $\left[\boldsymbol\alpha\cdot\mathbf p+\beta(M+S)+V\right]\psi=E\psi$; Dirac effective mass $M^*=M+S$; the upper-component reduction: $\left[\frac{p^2}{2M}+(V+S)+\frac{1}{2M^2}\frac1r\frac{d(V-S)}{dr}\mathbf L\cdot\mathbf S+\dots\right]\phi=(E-M)\phi$ (for $S$ and $V$ small compared with $2M$; keep the $V-S$ structure); so central binding $\propto V+S$ (small, $\sim-50$ to $-100$ MeV) while spin-orbit $\propto V-S$ (large, $\sim700$ MeV).

**Extrapolation [Should]**
- At $5$ to $10n_0$ nucleon velocities are $\sim0.4c$ to $0.6c$, hadronic fields are large and relativistic effects (the $M^*$ dependence of the scalar density) are first-order.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Walecka "Why Field Theory": the three arguments; exercises 1 and 2 |
| Session 2 | Serot-Walecka (1986) introduction; exercises 3 to 5 |
| Session 3 | The Dirac reduction; exercises 6 and 7 |
| Session 4 | Exercises 8 to 10 |

## Derive from scratch

1. The non-relativistic reduction of the Dirac equation with $S$ and $V$.
2. The spin-orbit coefficient and its scaling with $V-S$.
3. The causality condition $v_s\le c$ for a given EOS.
4. The magnitude of $V$ and $S$ from QHD-I (preview).
5. The "difference of large numbers" argument.

## Bare-minimum exercises (with expected results)

1. **Acausality of a potential model:** $v_s^2=\frac{dP}{d\varepsilon}$; with $P=n^2\frac{d(E/N)}{dn}$ and $\varepsilon=n(M+E/N)$ for SLy4 neutron matter: $v_s^2=0.045,0.15,0.35,0.68,0.86,1.01$ at $n=0.16,0.3,0.5,0.8,1.0,1.2$ fm$^{-3}$: acausal above $n\approx1.18$ fm$^{-3}$; for a power law $P\propto n^\Gamma$ causality fails when $\Gamma\frac Pn>M$.
2. **Dirac reduction:** derive the effective Schrödinger-like equation for the upper component with $M^*=M+S$ and identify the $\mathbf L\cdot\mathbf S$ term; show for $S=0$ (pure vector) and $V=0$ (pure scalar) the spin-orbit signs coincide: the two contribute with the *same* sign because of $V-S$ with $S<0$.
3. **Large fields:** in QHD-I at saturation $V\approx+330$ MeV and $S=M^*-M\approx-430$ MeV ($M^*/M=0.54$): the central potential $V+S\approx-100$ MeV (including the kinetic correction the nucleon is bound by $\sim16$ MeV) while $V-S\approx760$ MeV: **the spin-orbit potential is about 8 times larger than the central one**, explaining the large empirical spin-orbit force.
4. **The anomalous shell-model coefficient:** state that the Module 10 spin-orbit strength (about 20 times the Thomas value) is *derived* here (Module 24: relativistic Hartree for finite nuclei gives it with no free parameter).
5. **Why the sign rule matters:** from Module 08, scalar attracts and vector repels; the nearly cancelling large fields are the field-theoretic origin of the weak net binding.
6. **Extrapolation to the core:** at $n=5n_0$, $k_F=2.28$ fm$^{-1}$, $v_F/c=0.43$ and the field $V\propto n_B$ grows linearly while $M^*$ decreases: estimate $V$ at $5n_0$ from $V\propto n_B$ ($\approx1.6$ GeV in QHD-I): the Dirac effective mass cannot be ignored.
7. **Covariance and causality:** explain in three sentences why a Lorentz-covariant Lagrangian has $v_s\le c$ (the signal propagates through field equations of hyperbolic type).
8. **Check the reduction in a limit:** for $V=-S=U_0$ (spin-orbit maximal, central zero), show the upper-component equation has the same spin-orbit form and no central potential.
9. **Thomas value:** the atomic Thomas spin-orbit coefficient is $\frac{1}{4M^2}\frac1r\frac{dV}{dr}$; compare with $\frac{1}{2M^2}\frac1r\frac{d(V-S)}{dr}$ and estimate the enhancement for $V\approx-S$: $\approx2\times\frac{V-S}{V}\approx4$ times larger plus the factor from the potential shape.
10. **Summary:** write the three arguments for field theory in three sentences each.

## Optional extension

Solve the Dirac equation for a Woods-Saxon $S$ and $V$ with $S=-\kappa V$ numerically and plot the spin-orbit splitting of the $1p$ levels versus $\kappa$.

## Pitfalls

- Treating the nucleon as relativistic because $v_F/c\sim0.3$ (the relativity is in the potentials).
- Dropping the $V-S$ structure by assuming a single potential.
- Using the Thomas coefficient as if it applied to the strong interaction.

## Gate questions

1. Why is causality a *structural* argument for a maximum-mass calculation?
2. Why is the central potential $V+S$ small while the spin-orbit potential $V-S$ is large?
3. What does the Dirac effective mass do to the scalar attraction at high density?

## One-page cheat sheet contents

Causality criterion; Dirac equation with $S$, $V$; non-relativistic reduction and the $V\pm S$ combinations; the large-field numbers.
