# Module 26: $\beta$ equilibrium and the composition of dense matter (Week 25): Month 6 begins

**Books:** HPY sections 5.5 to 5.9; Glendenning chapter 4; Chamel and Haensel section 5.
**Time:** 1 week.

## Why this matters

$\mu_n=\mu_p+\mu_e$, with $n_p=n_e+n_\mu$ and muons appearing above $\mu_e>105.7$ MeV. Solved with the Module 24 mean-field equations this gives $x(n_B)$, controlled almost entirely by $S(n)$: to lowest order $x\simeq\frac{(4S/\hbar c)^3}{3\pi^2n_B}(1-2x)^3$.

**Direct Urca** requires $p_{Fn}<p_{Fp}+p_{Fe}$, hence threshold proton fractions of $\frac19$ ($npe$) or $\approx0.148$ ($npe\mu$). ↪ **Module 15 gave you the rate; this module gives the gate.** Whether a star can direct-Urca-cool is a question about $J$ and $L$: the same numbers that set crust thickness.

## Skip-test (40 minutes, no notes)

1. Derive $\beta$ equilibrium and charge neutrality; solve for $x(n_B)$ to lowest order.
2. Find the muon threshold density.
3. Derive the direct Urca threshold and get $\frac19$ for $npe$; redo including muons.
4. State what controls the proton fraction and the direct Urca onset.
5. Relate the Urca onset to a stellar mass via the TOV solution.

## Prerequisites

Modules 15, 17, 24.

## Detailed topics (checklist)

**Equilibrium [Must]**
- $\mu_n-\mu_p=\mu_e=\mu_\mu$ (neutrinos escape); charge neutrality $n_p=n_e+n_\mu$; baryon number $n_B=n_n+n_p$; leptons as free Fermi gases; $\mu_n-\mu_p=4S(n)(1-2x)$ in the quadratic approximation; ultra-relativistic electrons: $\mu_e\approx\hbar c(3\pi^2n_Bx)^{1/3}$.

**Direct Urca [Must]**
- Momentum triangle: $p_{Fn}\le p_{Fp}+p_{Fe}$; for $npe$ with $p_{Fp}=p_{Fe}$: $\frac{n_n}{n_p}\le8$, $x\ge\frac19=0.111$; with ultra-relativistic muons $a^3=p_e^3+p_\mu^3\to2p_e^3$ and $x_{\rm DU}=\frac{1}{1+(1+2^{-1/3})^3}=0.148$.
- Whether the threshold is reached in a star of given mass depends on $S(n)$ at $\sim3n_0$.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | HPY 5.5 to 5.7: equilibrium; exercises 1 to 3 |
| Session 2 | Muons; exercise 4 |
| Session 3 | Direct Urca; exercises 5 and 6 |
| Session 4 | Exercises 7 to 10 |

## Derive from scratch

1. The equilibrium equations.
2. $x(n_B)$ to lowest order.
3. The muon threshold.
4. The $\frac19$ and $0.148$ thresholds.
5. The required $S(n)$ for direct Urca.

## Bare-minimum exercises (with expected results)

1. **Equilibrium:** write $\mu_n=\mu_p+\mu_e$, $\mu_\mu=\mu_e$, $n_p=n_e+n_\mu$; show for ultra-relativistic electrons $4S(1-2x)=\hbar c(3\pi^2n_Bx)^{1/3}$.
2. **Proton fraction (SLy4 symmetry energy):** $x\simeq\frac{(4S/\hbar c)^3}{3\pi^2n_B}(1-2x)^3$ gives $x\approx0.044$ at $n_0$ ($S=32$ MeV) and $\approx0.050$ at $2n_0$ ($S=43$ MeV): small, typical of soft symmetry energies.
3. **Muon threshold:** $\mu_e=105.66$ MeV gives $n_e=\frac{(105.66/197.327)^3}{3\pi^2}=5.2\times10^{-3}$ fm$^{-3}$, i.e. $n_B\approx\frac{n_e}{x}\approx0.12$ fm$^{-3}$ ($\approx0.7n_0$).
4. **Effect of muons:** muons add a negative charge reservoir, lowering $\mu_e$ and slightly raising $x$ and softening the EOS.
5. **Direct Urca $npe$:** $p_{Fn}=2p_{Fp}$ at threshold gives $\frac{n_n}{n_p}=8$ and $x=\frac19$.
6. **With muons:** $p_{Fp}^3=p_{Fe}^3+p_{F\mu}^3\to2p_{Fe}^3$ in the ultra-relativistic limit, $p_{Fn}=p_{Fp}+p_{Fe}=(1+2^{-1/3})p_{Fp}$, so $x=\frac{1}{1+(1+2^{-1/3})^3}=0.148$.
7. **Required symmetry energy:** setting $x=\frac19$ in the lowest-order formula needs $(4S/\hbar c)^3=6.98n_B$, i.e. $S\approx75$ MeV at $n_B=0.5$ fm$^{-3}$; compare with $S(0.5)\approx50$ MeV for SLy4: direct Urca does not occur at that density in SLy4, but a set with large $L$ (e.g. NL3-like, $S$ rising steeply) can reach it at lower density.
8. **Two RMF sets of different $L$ (with your TOV solver):** find the density where $x=\frac19$ (or $0.148$), the stellar mass whose central density equals it, and combine with the Module 15 emissivities to estimate the luminosity contrast between a star above and below threshold ($\sim10^6$ at $T_9=1$).
9. **Observational hook:** young cooling neutron stars (e.g. those measured with X-rays) that are cold early imply enhanced cooling; a threshold mass above which enhanced cooling turns on is a constraint on $J$ and $L$.
10. **Link to the crust:** the same $L$ that lowers the DU threshold thins the crust (Module 20): a single parameter, two observables.

## Optional extension

Solve the full $npe\mu$ equilibrium numerically with the asymmetric-matter RMF equations of Module 24 for an NL3-like set and plot $x_p(n_B)$, $x_\mu(n_B)$ and the direct Urca threshold.

## Pitfalls

- Using $\mu_e=\mu_p$-type conditions with the wrong sign conventions for $b_0$.
- Forgetting that muons modify the DU threshold.
- Using the lowest-order $x$ formula far from $\delta\ll1$.

## Gate questions

1. Why is the proton fraction controlled by $S(n)$?
2. Why is the direct Urca threshold $\frac19$ and then $0.148$?
3. What do $J$ and $L$ decide for cooling?

## One-page cheat sheet contents

Equilibrium equations; lowest-order $x$; muon threshold; Urca thresholds; required $S(n)$.
