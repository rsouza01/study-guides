# Module 24: Extensions: nonlinear terms, the $\rho$ meson, QHD-II (★, Week 23)

**Books:** Walecka's "Extensions of RMFT" chapter, and **the QHD-II chapter: present in your 1st edition, absent from the 2nd.**
**Time:** 1 week.

## Why this matters

**(i) Nonlinear scalar self-interactions.** Add $-\frac13bM(g_s\phi)^3-\frac14c(g_s\phi)^4$ (Boguta-Bodmer): two parameters fitted to $K$ and finite-nucleus properties. This is what makes QHD usable: NL3, TM1, FSUGold and the modern RMF family. Note the epistemic trade: a parameter-free prediction for a fit. That trade is what "effective field theory" means in practice.

**(ii) The $\rho$ meson.** Add $-\tfrac12g_\rho\bar\psi\gamma^\mu\boldsymbol\tau\psi\cdot\mathbf b_\mu$; in mean field only $b_0^{(3)}$ survives, sourced by $n_p-n_n$, contributing $\propto\delta^2$. **The $\rho$ coupling *is* the symmetry energy.** $J$ and $L$ become computable, and the $\omega$-$\rho$ cross-coupling is how modern parametrisations tune $L$ independently of $J$: i.e. how they tune crust thickness.

Also: **relativistic Hartree for finite nuclei.** The spin-orbit splitting comes out right *with no free parameter*, for the reason you derived in Module 21. Given how much of Month 3 went into putting $\mathbf l\cdot\mathbf s$ in by hand, savour it.

## Skip-test (40 minutes, no notes)

1. Add the nonlinear $\sigma$ terms; re-derive the field equations and the EOS; show how $b$ and $c$ fit $K$ and $M^*$ independently.
2. Add the $\rho$; derive $S(n)$ analytically in mean field; separate kinetic and potential contributions.
3. Evaluate $J$ and $L$ for a published parameter set and compare with Module 17 and the Module 12 dipole-polarizability constraint.
4. Write the general asymmetric-matter mean-field equations for arbitrary $x=n_p/n_B$.
5. State the role of the $\omega$-$\rho$ coupling.

## Prerequisites

Modules 17, 22 and 23.

## Detailed topics (checklist)

**Nonlinear terms [Must]**
- $U(\phi)=\frac13bM(g_s\phi)^3+\frac14c(g_s\phi)^4$ modifies the scalar equation to $m_s^2\phi_0+\frac{dU}{d\phi}=g_sn_s$; with $b,c$ fitted, $K$ drops from $546$ to $\sim250$ to $270$ MeV and $M^*/M$ rises to $\sim0.6$. Published sets: **NL3** ($n_0=0.148$ fm$^{-3}$, $E/A=-16.3$ MeV, $K=272$, $J=37.4$, $L=118$ MeV, $M^*/M=0.60$); **FSUGold** ($K\approx230$, $J\approx32.6$, $L\approx60$ MeV, with an $\omega$-$\rho$ coupling $\Lambda_v=0.03$).

**The $\rho$ meson [Must]**
- Mean-field equations (proton $t_3=+\tfrac12$ convention): $m_\rho^2b_0=\tfrac12g_\rho(n_p-n_n)$; $\mu_n=\sqrt{k_n^2+M^{*2}}+g_vV_0-\tfrac12g_\rho b_0$, $\mu_p=\sqrt{k_p^2+M^{*2}}+g_vV_0+\tfrac12g_\rho b_0$; $M^*=M-\frac{g_s^2}{m_s^2}(n_s^p+n_s^n)+\ldots$; the symmetry energy $S(n)=\frac{k_F^2}{6E_F^*}+\frac{g_\rho^2}{8m_\rho^2}n_B$ (kinetic plus $\rho$-potential), $k_F=(3\pi^2n_B/2)^{1/3}$.
- $L=3n_B\frac{dS}{dn_B}$; the $\omega$-$\rho$ cross-coupling $2\Lambda_vg_v^2g_\rho^2V_\mu V^\mu\mathbf b_\nu\cdot\mathbf b^\nu$ reduces $L$ at fixed $J$.

**Finite nuclei and QHD-II [Should]**
- Relativistic Hartree for finite nuclei (the same loop as Module 13 with the meson fields as sources of the Dirac equation): spin-orbit splittings come out right without a free parameter ($1p_{1/2}$-$1p_{3/2}$ in $^{16}$O $\approx6$ MeV, empirical $6.3$).
- QHD-II (1st edition): adds the isovector $\rho$ and the pion in a gauge-invariant (SU(2)$_I$) way and the photon; orientation only.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Walecka "Extensions of RMFT": the nonlinear terms; exercises 1 to 3 |
| Session 2 | The $\rho$ meson and $S(n)$; exercises 4 and 5 |
| Session 3 | Asymmetric-matter equations; exercise 6 |
| Session 4 | Finite nuclei and QHD-II; exercises 7 to 10 |

## Derive from scratch

1. The scalar field equation with the nonlinear terms.
2. $S(n)$ with the $\rho$ meson.
3. The asymmetric-matter equations for $x\ne\tfrac12$.
4. $L$ in terms of the couplings.
5. The effect of the $\omega$-$\rho$ coupling.

## Bare-minimum exercises (with expected results)

1. **Nonlinear $\sigma$:** the energy density gains $+U(\phi_0)$ and the scalar equation becomes $m_s^2\phi_0+U'(\phi_0)=g_sn_s$, i.e. $M^*=M-\frac{g_s^2}{m_s^2}\left[n_s-bM(g_s\phi_0)^2-c\,(g_s\phi_0)^3\right]$ with $U(\phi)=\frac13bM(g_s\phi)^3+\frac14c(g_s\phi)^4$; re-derive $\varepsilon$ and $P$ and verify $P=n_B^2\frac{d(\varepsilon/n_B)}{dn_B}$ still follows from $\frac{\partial\varepsilon}{\partial M^*}=0$; for the fitted signs of $b$ and $c$ the scalar attraction is weakened at large $\phi_0$, lowering $K$.
2. **Fitting $b$, $c$:** two parameters can be fitted independently to $K$ and $M^*$ at $n_0$ (state why: $U'$ and $U''$ enter the two conditions $P=0$ and $K$).
3. **Published sets:** NL3: $K=272$, $J=37.4$, $L=118$ MeV, $M^*/M=0.60$ (too stiff $L$; large neutron skin); FSUGold: $K=230$, $J=32.6$, $L=60$ MeV: comment on how the $\omega$-$\rho$ term moves $L$ at fixed $J$.
4. **$S(n)$ with the $\rho$:** $S=\frac{k_F^2}{6E_F^*}+\frac{g_\rho^2}{8m_\rho^2}n_B$; with QHD-I values at $k_F=1.42$ fm$^{-1}$, $E_F^*=592$ MeV and the kinetic part is $22.1$ MeV; **fitting the $\rho$ to $J=32$ MeV gives $C_\rho^2=\frac{g_\rho^2M^2}{m_\rho^2}\approx47$ and $L\approx104$ MeV**: a linear $\rho$ coupling alone gives a large $L$; this is why the nonlinear $\omega$-$\rho$ term is added.
5. **$\omega$-$\rho$ coupling:** the term modifies $\frac{g_\rho^2}{8m_\rho^2}n_B\to\frac{g_\rho^2n_B/8}{m_\rho^2+2\Lambda_vg_v^2g_\rho^2V_0^2}$: it suppresses the $\rho$ contribution at high density, lowering $L$ without changing $J$ if the $\rho$ coupling is refitted.
6. **General asymmetric-matter equations (Module 26 needs these):** write $k_{n,p}=(3\pi^2n_{n,p})^{1/3}$, the self-consistency $M^*=M-\frac{g_s^2}{m_s^2}(n_s^n+n_s^p)$, the vector and isovector potentials, and the chemical potentials $\mu_{n,p}$ above; verify they reduce to Module 22 at $x=\tfrac12$.
7. **Spin-orbit splitting:** the RMF mean field in $^{16}$O gives a $1p$ splitting of $\sim6$ MeV from $V-S$; state why this agrees with the 6.3 MeV observation without a spin-orbit fit parameter.
8. **Parameter counting:** Walecka's QHD-I has 2 parameters; NL3 has 7 (4 couplings, 2 nonlinear, plus the $\rho$); count the observables they are fitted to and state what remains predictive (neutron skins, $K$, EOS above $2n_0$).
9. **The epistemic trade (write a paragraph):** why a model with a few well-motivated terms fitted to data and then used to extrapolate is "an effective field theory" and what that implies for the reliability of its predictions at $5n_0$.
10. **Constraint check:** list which of NL3 and FSUGold satisfies each of: $K=230\pm30$, $J=31$ to $33$, $L=40$ to $80$ MeV, and the $2M_\odot$ maximum mass.

## Optional extension

Solve the relativistic Hartree equations for $^{16}$O (or $^{40}$Ca) with NL3 numerically (spherical, Dirac radial equations in the meson fields) and compare the single-particle spectrum with Module 13's Skyrme HF.

## Pitfalls

- Assigning the wrong sign convention to $t_3$ when writing $\mu_n$, $\mu_p$.
- Fixing $L$ without checking $J$ (the two are correlated).
- Treating published sets as predictions rather than fits.

## Gate questions

1. Why does the $\rho$ meson produce the symmetry energy?
2. What does the $\omega$-$\rho$ coupling do to $L$?
3. Why is the spin-orbit splitting a prediction in RMF but a fit in the shell model?

## One-page cheat sheet contents

Nonlinear terms and their effect; $\rho$ equations and $S(n)$; $L$ formula; NL3 and FSUGold numbers; the asymmetric-matter equations.
