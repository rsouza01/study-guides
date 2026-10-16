# Module 14: Decay kinetics, alpha decay and fission (★, Week 13): Module D begins

**Books:** Krane chapter 6 sections 1 to 4 (decay law: fast); Krane chapter 8 (alpha decay); Krane chapter 13 sections 1 to 3 (fission); Wong's fission chapter for the deformation-energy treatment.
**Time:** 1 week. Module D (Modules 14 to 16) is the undergraduate canon: Krane is primary and at his best here. Every module has at least one hook (↪) back into the main line.

## Why this matters

**Decay kinetics** is cheap and necessary: decay law, chains, secular and transient equilibrium, branching. ↪ You need chain kinetics for an *accreting* crust, where composition is set by reaction networks, not equilibrium.

**Alpha decay.** Q-values from the mass formula explain why $\alpha$ and not $p$ or $d$. WKB penetration gives $\log t_{1/2}$ linear in $Q^{-1/2}$ (Geiger-Nuttall): a factor of two in $Q$ spans twenty orders of magnitude in lifetime. ↪ The same exponential sensitivity, at $T=0$ in a Coulomb lattice, is pycnonuclear fusion (Module 16).

**Fission: the largest payoff.** Expand the liquid-drop energy to second order in a quadrupole distortion:
$$\Delta E=\alpha_2^2\left[\tfrac25a_sA^{2/3}-\tfrac15a_c\frac{Z^2}{A^{1/3}}\right],$$
unstable when $\frac{Z^2}{A}>\frac{2a_s}{a_c}\approx50$. Define fissility $x=\frac{Z^2/A}{(Z^2/A)_{\rm crit}}$. ↪ **Thread A, the most important hook of Module D:** the same surface-versus-Coulomb competition governs the Wigner-Seitz cell of the inner crust (Module 19).

> **A correction to flag.** Your roadmap states "$x=1$ is the same as $E_{\rm surf}=2E_{\rm Coul}$". Working it out: the second-order expansion above vanishes when $\tfrac25E_S=\tfrac15E_C$, i.e. **$E_{\rm Coul}=2E_{\rm surf}$ for an isolated drop** at $x=1$. The relation $E_{\rm surf}=2E_{\rm Coul}$ is the *virial/equilibrium* condition for a nucleus in a Wigner-Seitz cell (Baym-Bethe-Pethick; Module 19). They are two faces of the same competition (surface versus Coulomb) and are related through an effective cell fissility, but they are not the same equation. Both are derived and compared in Modules 14 and 19: **check which one your Walecka and HPY readings use before copying a formula.**

## Skip-test (40 minutes, no notes)

1. Solve the decay chain $N_1\to N_2\to N_3$ and state secular and transient equilibrium.
2. Derive the deformation energy to second order in $\alpha_2$, obtain $(Z^2/A)_{\rm crit}$ and the fissility.
3. Compute the WKB Gamow factor for $\alpha$ tunnelling a Coulomb barrier and evaluate $t_{1/2}$ for $^{238}$U.
4. Recover the Geiger-Nuttall slope.
5. State the assault frequency and where preformation factors mark the model's limit.

## Prerequisites

Modules 03, 04, 08 (the Coulomb and surface terms; the Gamow idea).

## Detailed topics (checklist)

**Decay kinetics [Must]**
- $\frac{dN}{dt}=-\lambda N$, $t_{1/2}=\frac{\ln2}\lambda$, activity, mean life; chains: $N_2(t)=\frac{\lambda_1N_1(0)}{\lambda_2-\lambda_1}\left(e^{-\lambda_1t}-e^{-\lambda_2t}\right)$; **secular equilibrium** ($\lambda_1\ll\lambda_2$: $\lambda_1N_1=\lambda_2N_2$); **transient equilibrium** ($\lambda_1<\lambda_2$: $\frac{A_2}{A_1}=\frac{\lambda_2}{\lambda_2-\lambda_1}$); branching ratios and partial half-lives.

**Alpha decay [Must]**
- Why $\alpha$: $Q_\alpha=B(^4{\rm He})-\ldots>0$ for $A\gtrsim150$; barrier height $B_C=\frac{2Z_de^2}{R}\approx25$ to $28$ MeV against $Q\approx4$ to $9$ MeV; WKB transmission $e^{-2G}$ with $2G=\frac{4Z_\alpha Z_de^2}{\hbar v}\left[\arccos\sqrt x-\sqrt{x(1-x)}\right]$, $x=\frac{Q}{B_C}$; decay rate $\lambda=\nu e^{-2G}$ with assault frequency $\nu\approx\frac{v}{2R}\sim10^{21}$ s$^{-1}$; Geiger-Nuttall $\log t_{1/2}\propto\frac{Z}{\sqrt Q}$; preformation factors $P_\alpha\sim10^{-1}$ to $10^{-2}$.

**Fission [Must]**
- Liquid-drop energy for a distortion $R(\theta)=R_0\left[1+\alpha_2P_2(\cos\theta)\right]$ with volume conserved: $E_S\to E_S\left(1+\tfrac25\alpha_2^2\right)$ and $E_C\to E_C\left(1-\tfrac15\alpha_2^2\right)$; stability iff $\tfrac25E_S>\tfrac15E_C$; fissility; the fission barrier and spontaneous versus induced fission; shell corrections (Strutinsky), the double-humped barrier, asymmetric mass division.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Krane 6.1 to 6.4: decay kinetics; exercise 1 |
| Session 2 | Krane 8: alpha decay; exercises 2 to 4 |
| Session 3 | Krane 13.1 to 13.3: fission; exercises 5 and 6 |
| Session 4 | Wong's deformation-energy treatment; exercises 7 to 10 |

## Derive from scratch

1. The chain solutions and the two equilibrium cases.
2. The distortion expansion of $E_S$ and $E_C$.
3. The WKB Gamow factor for a Coulomb barrier.
4. The Geiger-Nuttall relation.
5. $(Z^2/A)_{\rm crit}=2a_S/a_C$.

## Bare-minimum exercises (with expected results)

1. **Chains:** for a parent of half-life $10$ d and a daughter of half-life $1$ d the activity ratio tends to $\frac{A_2}{A_1}=\frac{\lambda_2}{\lambda_2-\lambda_1}=\frac{T_1}{T_1-T_2}=1.11$ (transient equilibrium); for a daughter much shorter-lived it tends to $1$ (secular equilibrium).
2. **Deformation energy:** with $E_S\to E_S(1+\tfrac25\alpha_2^2)$, $E_C\to E_C(1-\tfrac15\alpha_2^2)$ get $\Delta E=\alpha_2^2\left[\tfrac25E_S-\tfrac15E_C\right]$; with $E_S=a_SA^{2/3}$, $E_C=a_C\frac{Z^2}{A^{1/3}}$ obtain $\left(\frac{Z^2}{A}\right)_{\rm crit}=\frac{2a_S}{a_C}\approx51$ for $a_S=18.3$, $a_C=0.714$ MeV.
3. **Fissility and the relation to $E_{\rm surf}$, $E_{\rm Coul}$:** $x=\frac{E_C}{2E_S}$, so $x=1\Leftrightarrow E_{\rm Coul}=2E_{\rm surf}$ for the isolated drop; for $^{238}$U, $\frac{Z^2}{A}=35.6$ and $x\approx0.70$; for $^{256}$Fm, $x\approx0.76$. **Box this and the correction above:** Module 19's cell relation is the opposite ratio.
4. **Gamow factor:** for $^{238}$U$\to{}^{234}$Th$+\alpha$ ($Q=4.27$ MeV, $R=1.2(234^{1/3}+4^{1/3})=9.3$ fm, $B_C=27.9$ MeV, $x=0.153$) get $2G\approx88$ and, with $\nu\approx7.8\times10^{20}$ s$^{-1}$, $t_{1/2}\approx1.4\times10^{17}$ s (observed $1.4\times10^{17}$ s). Repeat for $^{212}$Po ($Q=8.95$ MeV): $2G\approx32$ and $t_{1/2}\approx6\times10^{-8}$ s (observed $3\times10^{-7}$ s).
5. **Geiger-Nuttall:** between $Q=4.27$ MeV and $8.95$ MeV (a factor 2.1) the lifetime changes by $\approx24$ orders of magnitude; plot $\log_{10}t_{1/2}$ versus $Q^{-1/2}$ for four even-even emitters and recover the slope; state where preformation or hindrance factors mark the model's honesty limit (e.g. $^{210}$Po comes out a factor $\sim40$ too fast).
6. **Alpha versus other clusters:** $Q_\alpha>0$ but $Q_p<0$ and $Q_d<0$ for heavy nuclei; the $\alpha$ is unusually bound ($B=28.3$ MeV), so it is the lightest cluster emitted.
7. **Barrier numbers:** $B_C\approx26$ MeV versus $Q\approx5$ MeV: the barrier is a factor $5$ above the energy; the classical turning point is $\frac{2Z_de^2}{Q}\approx60$ fm.
8. **Fission barrier from the drop model:** the barrier height falls to zero at $x=1$ and rises as $\sim(1-x)^3$ for $x\to1$; state why shell corrections (double-humped barrier) matter for actinides.
9. **Thread-A hook:** a nucleus in the inner crust is a charged drop in a neutralising background; sketch how the cell Coulomb energy is reduced and why this stabilises large drops against fission (Module 19).
10. **Accreting-crust hook:** write the equations for a three-step chain with $T_{1/2}=1$ s, $10$ s, stable and sketch the abundance curves: composition in an accreted crust is set by kinetics, not equilibrium.

## Optional extension

Compute the $\alpha_4$ and mass-asymmetry dependence of the liquid-drop deformation energy and sketch the saddle-point shape for $x\to1$.

## Pitfalls

- Reversing the fission relation (see the correction above).
- Using the Gamow factor without the assault frequency, or with the wrong $Z_1Z_2$ (use daughter times $\alpha$: $2Z_d$).
- Forgetting that spontaneous-fission half-lives depend on shell corrections.

## Gate questions

1. Why does $\log t_{1/2}$ vary linearly with $Q^{-1/2}$?
2. What does $x=1$ mean physically for the drop?
3. Why is the inner-crust cell relation the inverse of the fissility condition?

## One-page cheat sheet contents

Chain solutions; $2G$ and $t_{1/2}$ recipe; Geiger-Nuttall; deformation energy and $(Z^2/A)_{\rm crit}$; the two relations and which is which.
