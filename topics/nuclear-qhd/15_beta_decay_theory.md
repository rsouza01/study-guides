# Module 15: Beta decay theory (★, Week 14)

**Books:** Krane chapter 9 in full (the chapter Module D exists for); Bertulani in parallel. **Skim** Walecka's semileptonic weak processes chapter for 45 minutes to see where the graduate version goes; do not attempt it.
**Time:** 1 week.

## Why this matters

Fermi's four-fermion theory, the golden rule and the phase-space factor. The **Kurie plot** and the neutrino-mass endpoint. The **Fermi function $F(Z,E)$**: not a detail, since crustal electron-capture rates depend on it and $Z$ is large in the crust. **$ft$ values**, superallowed $0^+\to0^+$ transitions, extraction of $G_FV_{ud}$. **Selection rules**: allowed Fermi ($\Delta J=0$, vector, $\tau$) versus Gamow-Teller ($\Delta J=0,\pm1$, axial, $\boldsymbol\sigma\boldsymbol\tau$); forbidden transitions. **Parity violation** and Wu. **Electron capture** and its Q-value relation.

↪ **Thread A, the main hook:** direct Urca, $n\to p+e^-+\bar\nu_e$, *is* $\beta$ decay in a medium where all three species are degenerate. Module 26 gives the threshold; this module gives the rate. The $T^6$ scaling of the direct Urca emissivity (versus $T^8$ for modified Urca) comes from counting how much of each Fermi surface participates: the difference between a star that cools fast and one that does not.

↪ **Thread C:** the Gamow-Teller operator $\boldsymbol\sigma\boldsymbol\tau$ is the spin-isospin structure of OPEP (Module 08), returning in the $\rho$ and $\pi$ sectors of QHD.

## Skip-test (40 minutes, no notes)

1. Derive the allowed $\beta$ spectrum from phase space and show the Kurie plot is linear.
2. State how a neutrino mass modifies the endpoint of the spectrum.
3. Compute $F(Z,E)\approx\frac{2\pi\eta}{1-e^{-2\pi\eta}}$ for an electron and a positron at $Z=26$.
4. State the allowed and forbidden selection rules and the typical $\log ft$ ranges.
5. Show the $T^6$ scaling of the direct Urca emissivity by counting thermally available phase space.

## Prerequisites

Modules 01 and 14.

## Detailed topics (checklist)

**Fermi theory [Must]**
- Golden rule $\lambda=\frac{2\pi}\hbar|M_{fi}|^2\rho_f$; the allowed spectrum $N(p)dp\propto F(Z,E)\,p\,E\,(E_0-E)^2dp$ for a massless neutrino; the Kurie function $K(E)=\sqrt{\frac{N(p)}{pEF(Z,E)}}\propto(E_0-E)$; neutrino mass: near the endpoint $N\propto(E_0-T)\sqrt{(E_0-T)^2-m_\nu^2c^4}$ (tritium, $Q=18.59$ keV; KATRIN bound $m_\nu<0.45$ eV).
- The Fermi function: $F(Z,E)\approx\frac{2\pi\eta}{1-e^{-2\pi\eta}}$ with $\eta=\pm\frac{Z\alpha E}{pc}$ ($+$ for $\beta^-$, $-$ for $\beta^+$).

**$ft$ values and selection rules [Must]**
- $f$ the phase-space integral, $t=t_{1/2}/{\rm BR}$; $\log ft\approx3$ for superallowed, $4$ to $7$ for allowed, $6$ to $9$ for first-forbidden. Allowed Fermi (vector current, $\Delta J=0$, no parity change, $\Delta T=0$) and Gamow-Teller ($\boldsymbol\sigma\boldsymbol\tau$, $\Delta J=0,\pm1$ not $0\to0$, no parity change); first-forbidden has parity change.
- Superallowed $0^+\to0^+$: $\mathcal Ft=ft(1+\delta_R')(1-\delta_C+\delta_{NS})\approx3072$ s and $|V_{ud}|^2=\frac{K}{2G_F^2\mathcal Ft(1+\Delta_R^V)}$ giving $|V_{ud}|\approx0.9737$ ($K/(\hbar c)^6=8120.28\times10^{-10}$ GeV$^{-4}$ s, $G_F=1.1664\times10^{-5}$ GeV$^{-2}$, $\Delta_R^V\approx2.45\%$).
- Parity violation (Wu, 1957): electrons from polarised $^{60}$Co emitted preferentially opposite to the spin. **Electron capture:** $Q_{\rm EC}=Q_{\beta^+}+2m_ec^2$ and competition with $\beta^+$.

**In-medium: Urca processes [Must]**
- Direct Urca $n\to p+e^-+\bar\nu_e$, $p+e^-\to n+\nu_e$ in degenerate $npe$ matter: the momentum-triangle condition $p_{Fn}<p_{Fp}+p_{Fe}$; emissivity $\propto T^6$ by counting: the three degenerate fermions each contribute a factor $T$ from their energy integral subject to one energy conservation delta ($T^2$ net), and the neutrino contributes $\int E_\nu^2dE_\nu\cdot E_\nu\propto T^4$; total $T^6$. Modified Urca (a spectator nucleon): two more degenerate fermions give an extra $T^2$: $T^8$.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Krane 9.1 to 9.3: the spectrum, Fermi function, Kurie plot; exercises 1 to 3 |
| Session 2 | Krane 9.4 to 9.6: $ft$ values and selection rules; exercises 4 to 6 |
| Session 3 | Parity violation; electron capture; exercises 7 and 8 |
| Session 4 | The Urca counting; exercises 9 and 10 |

## Derive from scratch

1. The allowed spectrum from phase space.
2. The Kurie linearisation.
3. The effect of $m_\nu$ on the endpoint.
4. The $T^6$ scaling of direct Urca.
5. $V_{ud}$ from $\mathcal Ft$.

## Bare-minimum exercises (with expected results)

1. **Spectrum and Kurie plot:** $N(T)\propto F(Z,T)\,pE(Q-T)^2$; $\sqrt{N/(pEF)}\propto(Q-T)$ is a straight line that hits zero at $T=Q$; sketch for tritium ($Q=18.59$ keV).
2. **Neutrino mass:** show that for $m_\nu\ne0$ the Kurie plot bends over within $\sim m_\nu c^2$ of the endpoint and ends at $Q-m_\nu c^2$; for KATRIN's bound $m_\nu<0.45$ eV this is the last $\sim$eV of an 18.6 keV spectrum.
3. **Fermi function:** for an electron of kinetic energy $1$ MeV in $^{56}$Fe-like $Z=26$: $E=1.511$ MeV, $pc=1.422$ MeV and $\eta=\frac{Z\alpha E}{pc}=0.20$, so $F_{\beta^-}\approx1.76$ and $F_{\beta^+}\approx0.50$ (the Coulomb field enhances electron and suppresses positron emission; important for crustal capture where $Z\sim30$ to $40$).
4. **$ft$ and $\mathcal Ft$:** for the superallowed decay of $^{14}$O ($t_{1/2}=70.6$ s, branching $\approx99.3\%$, $f\approx43$) get $ft\approx3.0\times10^3$ s; the corrected $\mathcal Ft\approx3072$ s is universal across superallowed transitions (conserved vector current).
5. **$V_{ud}$:** $|V_{ud}|^2=\frac{2984.6\ {\rm s}}{\mathcal Ft(1+\Delta_R^V)}=\frac{2984.6}{3072\times1.0245}$ gives $|V_{ud}|=0.9737$; compare with the muon-decay value of $G_F$.
6. **Classification from $J^\pi$:** $^{14}$O$\to{}^{14}$N$^*$ ($0^+\to0^+$): superallowed Fermi; $^6$He$\to{}^6$Li ($0^+\to1^+$): pure Gamow-Teller ($\log ft=2.9$); $^3$H$\to{}^3$He ($\tfrac12^+\to\tfrac12^+$): mixed Fermi and Gamow-Teller ($\log ft=3.05$); $^{207}$Tl$\to{}^{207}$Pb ($\tfrac12^+\to\tfrac12^-$): first-forbidden; use your Module 10 $J^\pi$ assignments.
7. **Parity violation:** state what an asymmetry $\propto\mathbf J\cdot\mathbf p_e$ means (a pseudoscalar correlation) and why it implies parity violation in the weak interaction.
8. **Electron capture:** $Q_{\rm EC}=Q_{\beta^+}+1.022$ MeV; list the nuclei for which only EC is possible ($Q_{\rm EC}<1.022$ MeV).
9. **Direct Urca scaling:** write the emissivity as (matrix element) $\times$ (phase space on the three Fermi surfaces and the neutrino) and count: $T^6$; for modified Urca $T^8$; at $T=10^9$ K the ratio $\epsilon_{\rm MU}/\epsilon_{\rm DU}\sim10^{-6}$ (verify with published coefficients: $\epsilon_{\rm DU}\approx4\times10^{27}\left(\frac{n_e}{n_0}\right)^{1/3}T_9^6$ erg cm$^{-3}$ s$^{-1}$).
10. **Momentum triangle:** show $p_{Fn}<p_{Fp}+p_{Fe}$ with $p_{Fe}=p_{Fp}$ (charge neutrality, $npe$) is $p_{Fn}<2p_{Fp}$, i.e. $\frac{n_n}{n_p}<8$, hence $x_p>\frac19$ (Module 26).

## Optional extension

Compute $f(Z,Q)$ numerically for a few allowed transitions with the exact Fermi function and compare with the Sargent $E_0^5/30$ approximation.

## Pitfalls

- Omitting the Fermi function for large $Z$ and $\beta^+$ decays.
- Using $t_{1/2}$ instead of the partial half-life $t_{1/2}/{\rm BR}$ in $ft$.
- Confusing Fermi and Gamow-Teller selection rules for $0^+\to0^+$ (only Fermi).

## Gate questions

1. Why is the Kurie plot linear and what does a neutrino mass do to it?
2. Why is the direct Urca emissivity $\propto T^6$ and modified Urca $\propto T^8$?
3. Which transitions give $V_{ud}$ and why?

## One-page cheat sheet contents

Allowed spectrum and Kurie; Fermi function; $\log ft$ ranges and selection rules; $\mathcal Ft$ and $V_{ud}$; Urca scalings and the momentum triangle.
