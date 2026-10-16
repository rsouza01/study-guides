# Module 17: Nuclear matter, saturation and the symmetry energy (★★★, Week 16): Month 4 begins

**Books:** **Walecka's Nuclear Matter chapter**: the whole thing, slowly; HPY sections 5.1 to 5.5.
**Time:** 1 week. **The first of the two modules that justify the guide.**

## Why this matters

$$\frac EA(n,\delta)\simeq\frac EA(n,0)+S(n)\delta^2,\qquad\delta\equiv\frac{n_n-n_p}{n},$$
$$\frac EA(n,0)=-B_0+\frac{K}{18}\left(\frac{n-n_0}{n_0}\right)^2+\cdots,\qquad S(n)=J+\frac L3\frac{n-n_0}{n_0}+\cdots$$
$$n_0\simeq0.16\ {\rm fm^{-3}},\ B_0\simeq16\ {\rm MeV},\ K\simeq230\pm30\ {\rm MeV},\ J\simeq31\text{ to }33\ {\rm MeV},\ L\simeq40\text{ to }80\ {\rm MeV}.$$

**Learn these five numbers the way you know $\hbar c$.** Then internalise the thesis of the second half:

> $K$ sets EOS stiffness and therefore maximum mass. $J$ sets proton fraction and therefore whether direct Urca turns on. **$L$ sets the crust-core transition density, the crust thickness, the moment of inertia stored in the crust, and $R_{1.4}$.** Almost every outer-layer observable is a function of $L$.

Note the live tension: PREX-II's $^{208}$Pb skin prefers large $L$ ($\sim106\pm37$ MeV); the Module 12 dipole polarizability plus astrophysical and ab initio constraints prefer 40 to 70.

## Skip-test (40 minutes, no notes)

1. Compute $E/A$ versus $n$ for a non-interacting Fermi gas and show it does not saturate; state what the interaction must supply.
2. From your Module 13 Skyrme result derive analytic expressions for $n_0$, $B_0$, $K$, $J$, $L$ and evaluate for SLy4.
3. Show the pressure of pure neutron matter at $n_0$ is $\frac{L n_0}{3}$ to leading order.
4. Derive the neutron skin thickness as a function of $L$ in a droplet model and state the logic from a $^{208}$Pb measurement to a neutron-star radius.
5. State the five numbers and what each controls in a star.

## Prerequisites

Modules 02, 03 and 13.

## Detailed topics (checklist)

**Saturation [Must]**
- Definition: $\frac{d}{dn}\left(\frac EA\right)=0$ (zero pressure) at $n_0$ with $E/A=-B_0$ (in symmetric matter without Coulomb); the free Fermi gas has $\frac EA=M+\tfrac35E_F\propto n^{2/3}$ rising monotonically: the interaction must supply attraction at long range and repulsion at short range and density dependence.
- Incompressibility $K=9n^2\frac{d^2(E/A)}{dn^2}\big|_{n_0}$ (equivalently $K=9\frac{dP}{dn}$); the numbers above.

**Asymmetric matter and the symmetry energy [Must]**
- $\delta=\frac{n_n-n_p}{n}=1-2x$ with $x=\frac{n_p}{n}$; quadratic expansion; $J=S(n_0)$, $L=3n_0\frac{dS}{dn}\big|_{n_0}$; for pure neutron matter $\frac EN\approx\frac EA(n,0)+S(n)$ and $P_{\rm PNM}(n_0)\approx\frac{Ln_0}{3}$.
- For Skyrme: $S(n)=\frac{\hbar^2k_F^2}{6m}-\frac{t_0}{8}(2x_0+1)n-\frac{t_3}{48}(2x_3+1)n^{\alpha+1}-\frac{k_F^2n}{24}\left[3t_1x_1-t_2(4+5x_2)\right]$ (verified for SLy4: $S(n_0)=32.0$, $L=46.0$ MeV).
- Constraints: nuclear masses (fix $J$), neutron skins, the dipole polarizability $\alpha_D$ of $^{208}$Pb, giant resonances, heavy-ion flows, neutron-star radii, chiral EFT for neutron matter.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Walecka's Nuclear Matter chapter: the Fermi gas and saturation; exercises 1 and 2 |
| Session 2 | HPY 5.1 to 5.3: the symmetry energy; exercises 3, 4, 9 |
| Session 3 | HPY 5.4 to 5.5: constraints on $J$ and $L$; exercises 5 to 8 |
| Session 4 | The astrophysical thesis; exercise 10 |

## Derive from scratch

1. The Fermi-gas energy per particle and why it does not saturate.
2. $n_0$, $B_0$, $K$ from the Skyrme $E/A$.
3. $S(n)$, $J$, $L$ from the Skyrme asymmetric-matter expressions.
4. $P_{\rm PNM}=\frac{Ln_0}{3}$.
5. The droplet-model relation between neutron skin and $L$.

## Bare-minimum exercises (with expected results)

1. **Fermi gas:** $\frac EA=M+\frac35E_F=M+22.1$ MeV at $n_0$ ($E_F=36.8$ MeV) and increases as $n^{2/3}$: no minimum; the interaction must contribute $-38$ MeV at $n_0$ (so $E/A=-16$ MeV).
2. **Skyrme numbers (SLy4):** $n_0=0.1595$ fm$^{-3}$, $B_0=15.97$ MeV, $K=229.9$ MeV, $J=S(n_0)=32.0$ MeV, $L=3n_0\frac{dS}{dn}=46.0$ MeV; **keep the analytic expressions** (from Module 13 exercise 2 and the $S(n)$ above).
3. **Pressure of neutron matter at $n_0$:** $P=n^2\frac{d(E/N)}{dn}$ with $E/N=\frac EA(n,0)+S(n)$ and $\frac{d(E/A)}{dn}\big|_{n_0}=0$ gives $P(n_0)=n_0^2\frac{dS}{dn}=\frac{Ln_0}{3}=2.4$ MeV/fm$^3$ ($\approx3.9\times10^{33}$ dyn/cm$^2$) for $L=46$ MeV: **$L$ is the pressure of neutron matter at saturation**, which is why it controls radii.
4. **Neutron skin and $L$:** in a droplet model $\Delta r_{np}$ grows with $L$ (a stiffer symmetry energy pushes neutrons outward): $\Delta r_{np}(^{208}{\rm Pb})\approx0.10+0.0015\,L$ fm ($L$ in MeV; approximate), so $L=46$ MeV gives $0.17$ fm and PREX-II's $0.283\pm0.071$ fm points to larger $L$ ($\sim100$ MeV). Contrast with the polarizability route, which weights $J$ and the shape of $S(n)$ near $\tfrac23n_0$.
5. **The five numbers and what each controls:** $n_0$ (central density of nuclei), $B_0$ (volume term), $K$ (EOS stiffness near $n_0$ and maximum mass), $J$ (proton fraction, drip, direct Urca), $L$ (crust-core transition, crust thickness, $\Delta I/I$, $R_{1.4}$); write one sentence each.
6. **Quartic corrections:** for SLy4 the full difference $E_{\rm PNM}-E_{\rm SNM}$ at $n_0$ is $32.7$ MeV versus $J=32.0$ MeV: the $\delta^4$ term is $\approx0.7$ MeV, small but not zero.
7. **Density dependence:** SLy4 gives $S(0.08)=22.2$, $S(0.16)=32.0$, $S(0.32)=42.9$, $S(0.48)=49.5$ MeV: $S$ rises sub-linearly; discuss which density region (below $n_0$: crust; above: core) the slope $L$ controls.
8. **The tension:** list the quoted ranges: PREX-II $L=106\pm37$ MeV, dipole polarizability plus ab initio $L\approx40$ to $70$ MeV, neutron-star radii $L\approx40$ to $60$ MeV; explain why a single experiment does not fix $L$.
9. **Why saturation matters for stars:** $n_0=2.7\times10^{14}$ g/cm$^3$ and $P(n_0)=0$ in symmetric matter but $P(n_0)=\frac{Ln_0}{3}>0$ in neutron matter: the star lives in asymmetric matter.
10. **Month-4 thesis:** write the one-paragraph version of the thesis above in your own words.

## Optional extension

Fit a two-parameter $S(n)=J\left(\frac n{n_0}\right)^\gamma$ to $S(n_0)=32$, $L=46$ and compare with the Skyrme $S(n)$ at $0.08$ and $0.32$ fm$^{-3}$.

## Pitfalls

- Confusing $E/A$ in symmetric matter with $E/N$ in neutron matter.
- Treating $L$ as a slope of $E/A$ rather than of $S(n)$.
- Quoting $K$ for the wrong quantity (finite-nucleus $K_A$ versus infinite-matter $K$).

## Gate questions

1. Why does the free Fermi gas not saturate?
2. Why is $P_{\rm PNM}(n_0)=\frac{Ln_0}{3}$?
3. Which star observables depend on each of $K$, $J$, $L$?

## One-page cheat sheet contents

The five numbers; $E/A(n,\delta)$ expansion; Skyrme $S(n)$; $P_{\rm PNM}(n_0)$; the astrophysical thesis; the PREX-II tension.
