# Module 11 (Level 7): the interior of the star from the EOS posterior

**Resources:** `nicerkit/tov.py::solve_star`; `examples/ex12_structure.py`; Lattimer & Prakash reviews; your nuclear-QHD guide, Modules 19, 20 and 27 (inner crust, pasta, unified EOS), and compact-objects guide Modules 07, 10, 12.
**Time:** 2 sessions.

## Why this matters

NICER constrains radii at a few masses; the EOS posterior turns that into *internal* quantities that no instrument measures: where the density sits, how thick the crust is, how much angular momentum the crust can hold, how deformable the star is. The skill is knowing which of these numbers the data constrain and which are inherited from the parametrisation.

## Diagnostic (15 minutes)

1. Which structure outputs depend mostly on the core EOS and which on the crust?
2. Why is $\Lambda$ so sensitive to radius?
3. What does a posterior band on $\rho(r)$ mean when every curve comes from a different EOS?

## Detailed topics (checklist)

- **Per-sample structure:** for each EOS draw and each target mass, `solve_star(eos, P_c)` gives $\rho(r)$, $P(r)$, $m(r)$, $R$, $\rho_c$, $I$, $k_2$, $\Lambda$; the crust thickness is $R-r(\rho_0)$ at the crust-core junction pressure `eos.P_of_rho(eos.rho0)`.
- **Bands:** overlay a few hundred curves with transparency, or compute percentiles on a common $r/R$ grid; keep the posterior over $R$ separate from the shape.
- **Interpretation levels:** (i) *directly constrained by NICER + the model*: $R_{1.4}$, the radius–mass slope; (ii) *inherited from the EOS family*: central density, crust thickness (the crust is fixed to SLy-like in this parametrisation, so its thickness has essentially no independent information); (iii) *needs extra data*: $\Lambda$ (GW170817), $I$ (not yet measured; the double pulsar may), cooling.
- **Swap in your own crust:** build a `TabulatedEOS` from a unified table (nuclear-QHD capstone) and compare crust thickness, $\Delta I/I$, and $R$ with the parametrised result.

## Tasks

1. `python ex12_structure.py injection_chain.npy` (or your real chain): prints medians and 68% intervals for $1.4$ and $2.0\,M_\odot$ stars; saves density and mass profiles.
2. Plot $\rho(r)/\rho_{\rm sat}$ for the posterior draws and for SLy; mark the crust-core junction.
3. Tabulate $R$, $\rho_c/\rho_{\rm sat}$, crust thickness, $I$, $\Lambda$ with uncertainties.

## Exercises (with expected results)

1. **Reference structure (SLy, exact):** $1.4\,M_\odot$: $R=11.71$ km, $\rho_c=3.4\rho_{\rm sat}$, crust $0.94$ km, $I=1.36\times10^{45}$ g cm$^2$, $\Lambda=294$.
2. **Reference posterior (the unconverged injection run, normalised mass prior):** $1.4\,M_\odot$: $R=11.14^{+0.64}_{-0.35}$ km, $\rho_c=3.19^{+0.25}_{-0.27}\rho_{\rm sat}$, crust $0.92^{+0.08}_{-0.15}$ km, $I=1.31^{+0.08}_{-0.05}\times10^{45}$ g cm$^2$, $\Lambda=250^{+71}_{-36}$; $2.0\,M_\odot$: $R=11.26^{+0.42}_{-0.42}$ km, $\rho_c=4.0^{+1.0}_{-0.5}\rho_{\rm sat}$, crust $0.49^{+0.06}_{-0.10}$ km, $I=2.32^{+0.22}_{-0.17}\times10^{45}$ g cm$^2$, $\Lambda=21.8^{+4.5}_{-6.3}$. Notice: the relative uncertainty is smallest for $I$ (about 6%) and largest for $\Lambda$ (about 30%, $\propto R^5$).
3. **Which numbers does the data constrain?** compare the width of each quantity with its width under the *prior* (run `ex12_structure` on a chain sampled with no sources, e.g. `infer.run_emcee([], ...)`): the ratio posterior/prior width tells you how much NICER taught you. The crust thickness barely changes: explain.
4. **$I$-$C$ or $I$-$\Lambda$ relation:** plot $I$ against compactness and $\Lambda$ against $R$ for your draws: tight, almost EOS-independent relations ("universal relations") explain why $I$ is better constrained than the radius suggests.
5. **Central density of the heaviest star:** $\rho_c(M_{\max})$ and $c_s^2$ there from `infer.derived`; discuss what this says about where the EOS is probed and why NICER cannot constrain densities above $\rho_c(2.1\,M_\odot)$.
6. **Crust fraction of $I$ (stretch):** compute $\Delta I/I$ from the profile (integrate $I$ over the crust layer) and compare with the thin-crust estimate $\Delta I/I\approx$ few % (nuclear-QHD Module 20).
7. **Replace the crust:** with your unified EOS table wrapped in `TabulatedEOS`, recompute crust thickness for the same core; how different is it?

## Pitfalls

- Reading a thin $\rho_c$ band as a precise measurement: it is conditional on the EOS family.
- Comparing structure quantities from different parametrisations without stating the crust.
- Quoting $\Lambda$ at the wrong mass.

## Gate questions

1. Which three structure quantities does NICER $(M,R)$ data constrain best, and why?
2. Why is the crust thickness here essentially an input, not an output?
3. What additional measurement would constrain $I$ or $\Lambda$ directly?

## One-page cheat sheet contents

Structure outputs and how to compute them; reference numbers (SLy and the injection posterior); a ranked list of what is data-driven versus parametrisation-driven.
