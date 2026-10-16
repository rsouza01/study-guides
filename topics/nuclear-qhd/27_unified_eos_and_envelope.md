# Module 27: The unified EOS and the envelope (★, Week 26)

**Books:** **Douchin and Haensel (2001), A&A 380, 151**; HPY chapter 6. Envelope: **Gudmundsson, Pethick and Epstein (1983)**; Potekhin, Chabrier and Yakovlev on the $T_b$-$T_s$ relation.
**Time:** 1 week.

## Why this matters

**(a) Unification.** You have an outer crust (Module 05), an inner crust (Module 20) and a core (Module 24). Naive stitching produces spurious discontinuities and thermodynamic inconsistency. The right approach is a *single* functional throughout. Read Douchin and Haensel as a template; understand the seams (drip, instability) and the continuity conditions ($\mu_B$ and $P$ continuous, composition free to jump).

**(b) The envelope and atmosphere.** The envelope ($\rho\lesssim10^{10}$ g/cm$^3$) is a thin insulating blanket decoupling $T_s$ from $T_b$, with $T_s\propto T_b^{0.5\text{ to }0.6}$ depending on composition. Electron conduction dominates; a light-element envelope conducts far better than iron and can shift the inferred $T_s$ by a factor of two. **Every cooling curve ever compared with data passes through this relation.** ↪ The heat it carries is partly the Module 16 deep crustal heating. The atmosphere on top ($\sim$cm) shapes the emergent spectrum: what NICER's radius measurements actually fit.

## Skip-test (40 minutes, no notes)

1. State the continuity conditions at the crust-core interface and show continuous $P$ and $\mu_B$ is equivalent to a Maxwell-type construction.
2. Explain when a genuine first-order transition is present instead.
3. Estimate $\Delta R$ analytically at $1.4M_\odot$ with a thin-layer argument.
4. Derive the radiative-zero envelope structure for a Kramers opacity.
5. State the $T_b$-$T_s$ scaling and what composition changes.

## Prerequisites

Modules 05, 20, 24, 25; thermodynamics guide Module 14 (radiative diffusion).

## Detailed topics (checklist)

**Unification [Must]**
- One functional (Skyrme or RMF) for crust and core; at a seam the baryon chemical potential $\mu_B$ and the pressure $P$ are continuous (equal at coexistence); the energy density may jump only at a true first-order transition; with two conserved charges (baryon and charge) the Gibbs construction rather than the Maxwell one applies (thermodynamics guide Module 13); beware transition densities where thermodynamic quantities are discontinuous in the derivative only (drip, crust-core).

**The envelope [Must]**
- Heat blanketing: energy transport by radiative diffusion in the non-degenerate outer layers and electron conduction at $\rho\gtrsim10^{9}$ to $10^{10}$ g/cm$^3$; the sensitivity strip at $\rho_s\sim10^{10}$; fits $T_s\approx3\times10^6$ to $6\times10^6$ K for $T_b=10^8$ K depending on composition; **light elements (accreted H/He) conduct better than iron** by raising $T_s$ by a factor of $\sim2$ at fixed $T_b$ (and luminosity $L\propto T_s^4$ by $\sim10$).

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Douchin-Haensel; exercises 1 and 2 |
| Session 2 | HPY 6; thin-crust estimate; exercise 3 |
| Session 3 | Gudmundsson-Pethick-Epstein; exercises 4 to 6 |
| Session 4 | Exercises 7 to 10 |

## Derive from scratch

1. The continuity conditions and the Maxwell construction.
2. The thin-crust thickness estimate.
3. The radiative-zero solution $P\propto T^{4.25}$.
4. The conduction-radiative transition.
5. The $T_b$-$T_s$ power law.

## Bare-minimum exercises (with expected results)

1. **Seams:** for a transition between two phases at fixed $T=0$ in a one-component system, equilibrium requires $P_1=P_2$ and $\mu_{B,1}=\mu_{B,2}$ (Maxwell construction on $P(\mu_B)$: the stable phase has the larger $P$); if the energy density is continuous and its derivatives are continuous there is no coexistence region.
2. **Two conserved charges:** with baryon number and electric charge the Gibbs construction gives a mixed phase with *rising* pressure; whether the crust-core boundary is a first-order transition is tested by checking whether $P(n_B)$ is monotonic and smooth across the instability density.
3. **Thin-crust thickness:** with $P_t\approx0.5$ MeV/fm$^3$, mean density $5\times10^{13}$ g/cm$^3$ and $g=2\times10^{14}$ cm/s$^2$: $\Delta R\approx\frac{P_t}{\bar\rho g}\approx0.8$ km; compare with the Module 20 numerical value from your TOV code at $1.4M_\odot$.
4. **Radiative-zero envelope:** with $F=\frac{4acT^3}{3\kappa\rho}\frac{dT}{dz}$, $dP=\rho g\,dz$, ideal gas $\rho\propto P/T$ and $\kappa=\kappa_0\rho T^{-3.5}$: $\frac{dT}{dP}\propto\frac{\kappa}{T^3}\propto PT^{-7.5}$, so $T^{8.5}\propto P^2$, i.e. $P\propto T^{4.25}$ (an $n=3.25$ polytrope).
5. **$T_b$-$T_s$ relation:** match radiative diffusion in the outer layers to conduction in the degenerate layers at $\rho_s\sim10^{10}$ g/cm$^3$: the flux $F\propto T_b^{2.2}$ gives $T_s\propto F^{1/4}\propto T_b^{0.55}$; at $T_b=10^8$ K, $T_s\approx3\times10^6$ K (iron) versus $\approx5\times10^6$ K (light-element envelope).
6. **Sensitivity of luminosity:** since $L=4\pi R^2\sigma T_s^4$ the factor $\sim1.7$ in $T_s$ between iron and H/He is a factor $\sim8$ in luminosity at fixed $T_b$: composition uncertainty is a cooling-curve uncertainty.
7. **Heat sources:** the deep crustal heating of Module 16 ($1$ to $2$ MeV per accreted nucleon) sets $T_b$ in accreting stars; steady state $L_\infty\approx\frac{\dot M}{m_u}\times1.5$ MeV.
8. **Atmosphere:** the outer $\sim$cm (hydrogen or heavier, magnetised or not) shapes the emergent spectrum, so inferred radii from NICER depend on atmosphere models.
9. **Unified EOS test:** state three tests of a unified EOS (thermodynamic consistency across seams, continuity of $\mu_B$ and $P$, reproduction of published $\Delta R$, $\Delta M$, $\Delta I/I$).
10. **Which module feeds which:** map Modules 05, 20, 24 to the three regions of the unified EOS and name the seam at each junction.

## Optional extension

Integrate the radiative-zero equations numerically from the photosphere inward until the onset of degeneracy and compute the radiative-conductive transition density for iron and hydrogen.

## Pitfalls

- Stitching EOS pieces with a discontinuous $P$ or $\mu_B$.
- Assuming $T_s\simeq T_b$.
- Using the same opacity for iron and light-element envelopes.

## Gate questions

1. Why must $P$ and $\mu_B$ be continuous at a seam?
2. Why does $T_s\ne T_b$?
3. Why does composition change the cooling curve?

## One-page cheat sheet contents

Continuity conditions; thin-crust estimate; $P\propto T^{4.25}$; $T_s\propto T_b^{0.55}$ and the composition factor.
