# Module 09 (Level 5): TOV and equations of state from scratch

**Resources:** `nicerkit/eos.py`, `nicerkit/tov.py`, `tests/test_core.py`; `examples/ex09_tov_eos.py`; Read et al. 2009 (piecewise polytropes); Hinderer 2008, Postnikov et al. 2010 (tidal deformability); Hartle 1967 (slow rotation). Your compact-objects guide, Modules 06 to 08, and your own `tov-solver.py` for cross-checks.
**Time:** 2 to 3 sessions. **Fully offline.**

## Why this matters

The EOS maps one-to-one onto a mass-radius curve, and the TOV equations are the bridge. If your solver fails exact tests, EOS inference on real data is meaningless, so this module is mostly **verification**: tests against exact and Newtonian results, then reference numbers you can quote.

## Diagnostic (15 minutes)

1. Write the TOV equations and say which variable you integrate in and why $P$ is a better variable than $\rho$.
2. What does thermodynamic consistency require of $\varepsilon(P)$ for a piecewise polytrope?
3. Why is the crust important for the radius but not for the maximum mass?

## Detailed topics (checklist)

- **TOV in geometric units:** $dP/dr=-(\varepsilon+P)(m+4\pi r^3P)/[r(r-2m)]$, $dm/dr=4\pi r^2\varepsilon$ ($G=c=1$; `solve_star` converts cgs). Integrate outward from a small $r_0$ with the series start, until $P$ drops to a floor ($10^{19}$ dyn/cm$^2$ here: the missing outer layers change $R$ by well under 10 m).
- **Piecewise polytropes (Read et al. 2009):** four fixed crust segments (SLy-like) and three core segments with free $(\log p_1,\Gamma_1,\Gamma_2,\Gamma_3)$ joined at $\rho_1=10^{14.7}$ and $\rho_2=10^{15.0}$ g/cm$^3$; $\varepsilon$ from the first law with offsets $a_i$ for continuity; $c_s^2=\Gamma P/(\varepsilon+P)$. The published $K_i$ are in units of $c^2$ (the test verifies continuity of $P$ across the crust boundaries to $<3\times10^{-4}$, validating the constants).
- **Slow-rotation moment of inertia** (Hartle): solve for the frame-dragging function; $I=J/\Omega$. **Tidal deformability** $\Lambda=\tfrac23k_2C^{-5}$ from the $y(r)$ equation with the Love-number formula (a Newtonian-limit branch avoids catastrophic cancellation).
- **Stable branch:** $dM/dP_c>0$; the curve is cut at the first maximum of $M$.

## Tasks

1. `python -m pytest -q tests/test_core.py` (7 tests, about 2 s). Read each test and say what exact result it checks.
2. `python ex09_tov_eos.py`: three EOS families, $M$-$R$ curves, density profiles, key numbers.
3. Cross-check against your own `tov-solver.py` for SLy-like parameters: agree to better than 0.5% in $R_{1.4}$?

## Exercises (with expected results)

1. **Exact interior solution (incompressible star):** $M=\tfrac{4\pi}3\varepsilon R^3$ to 0.2% and the central pressure matches $\varepsilon(1-x)/(3x-1)$ with $x=\sqrt{1-2M/R}$ to 0.5% (unit test).
2. **Newtonian $n=1$ polytrope:** $R=\sqrt{\pi K/2G}$ to 0.2%, $I/MR^2=0.261\pm0.004$, $k_2=0.2599\pm0.004$ (unit test; the textbook values are 0.261 and $(15-\pi^2)/2\pi^2=0.260$).
3. **SLy reference numbers (this solver):** $M_{\rm max}=2.05\,M_\odot$ (published 2.05), $R_{\rm at\,Mmax}=9.98$ km, $R_{1.4}=11.71$ km, $R_{2.0}=10.63$ km; at $1.4\,M_\odot$: $C=0.177$, $\Lambda=294$, $k_2=0.076$, $I=1.36\times10^{45}$ g cm$^2$, central density $3.4\,\rho_{\rm sat}$ ($\rho_{\rm sat}=2.66\times10^{14}$ g/cm$^3$), crust thickness $0.94$ km (to the crust-core junction at $P=6.0\times10^{32}$ dyn/cm$^2$).
4. **EOS families:** soft ($\log p_1=34.10,\Gamma=3,3,3$): $M_{\rm max}=1.75$ (the sequence is truncated where $c_s$ reaches $c$), $R_{1.4}=9.80$ km, $\Lambda_{1.4}=89$, $\rho_c=5.5\rho_{\rm sat}$; stiff ($34.70,3.0,2.8,2.8$): $M_{\rm max}=2.41$, $R_{1.4}=14.09$ km, $\Lambda_{1.4}=934$, $\rho_c=2.0\rho_{\rm sat}$. Observe: stiffer EOS, larger radius, larger $M_{\rm max}$, lower central density, much larger $\Lambda$ ($\propto R^5$).
5. **Speed:** the numba path integrates a 40-point $M$-$R$ curve in about 30 ms; the scipy path is about $10^3\times$ slower; the two agree to 0.2% in $M$ and 0.3% in $R$ (unit test).
6. **Surface boundary sensitivity:** `P_surf` $=10^{17},10^{19},10^{22}$ dyn/cm$^2$ gives $R_{1.4}=11.7058,11.7056,11.7038$ km: the surface cut matters at the 2 m level. Reproduce.
7. **Causality and the grid:** SLy's $c_s^2$ reaches 1 at $P=1.39\times10^{36}$ dyn/cm$^2$, essentially at $P_c(M_{\rm max})=1.4\times10^{36}$: the piecewise-polytrope SLy touches causality exactly at its maximum-mass star. **A grid ending at $10^{36}$ truncates $M_{\rm max}$ at 2.037**: this is a real trap (the default grid now extends to $10^{36.7}$ and the sequence is cut at $c_s=c$); reproduce it, and explain how it would bias an EOS inference.
8. **Your own EOS:** wrap a table from your nuclear-QHD guide in `TabulatedEOS` and compute its $M$-$R$ curve with `mr_curve` (slow path); compare with SLy at $1.4\,M_\odot$.

## Pitfalls

- Mixing $\rho$ (rest-mass) with $\varepsilon/c^2$ (total mass-energy density).
- Integrating past the maximum mass (unstable branch).
- Accepting an EOS that violates causality without noticing.

## Gate questions

1. Which two exact checks would you run on any new TOV code?
2. Why does $\Lambda$ scale as $C^{-5}$ and what does that mean for radius sensitivity?
3. What is the role of the crust in $R$ and $\Lambda$?

## One-page cheat sheet contents

TOV equations in geometric units; Read parametrisation; reference numbers (SLy, soft, stiff); the checks.
