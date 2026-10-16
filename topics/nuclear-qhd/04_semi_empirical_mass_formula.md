# Module 04: The semi-empirical mass formula (★, Week 2)

**Books:** Krane chapter 3 (the semi-empirical mass formula); Bertulani's liquid-drop and $\beta$-stability sections. Q-values and mass parabolas only: $\beta$-decay *theory* is Module 15.
**Time:** 1 week.

## Why this matters: the week the crust is decided

Outer-crust composition is determined by nuclear masses and nothing else. The **pairing term** is why the crust holds even-$Z$ nuclei; the **symmetry term** is why it goes neutron-rich under compression; the **Coulomb term** is what electron capture fights. Derive, do not memorise: the symmetry term from Fermi-gas level filling and the Coulomb term from the uniform sphere.

## Skip-test (40 minutes, no notes)

1. Write $B(A,Z)=a_VA-a_SA^{2/3}-a_C\frac{Z^2}{A^{1/3}}-a_A\frac{(A-2Z)^2}{A}+\delta$ and state the physical origin of each term.
2. Derive the symmetry term from the degenerate Fermi gas and compare with the empirical $\approx23$ MeV.
3. Derive $Z_{\rm min}(A)$ by minimising the mass at fixed $A$.
4. Define $S_n$ and $S_p$ and state what $S_n\to0$ means.
5. State the condition for stability against electron capture in a degenerate electron gas.

## Prerequisites

Modules 02 and 03.

## Detailed topics (checklist)

**The formula [Must]**
- Typical coefficients: $a_V\approx15.8$, $a_S\approx18.3$, $a_C\approx0.714$, $a_A\approx23.2$ MeV and $\delta=\pm\frac{12}{\sqrt A}$ MeV (even-even $+$, odd-odd $-$, odd-$A$ zero) (verify against your Krane edition: tables differ by a few percent).
- Origins: volume (saturation), surface (fewer neighbours), Coulomb (uniform sphere $\tfrac35\frac{e^2Z^2}{R}$), symmetry (Pauli: filling neutron and proton levels evenly), pairing (Module 11).

**Symmetry term from the Fermi gas [Must]**
- For $N$ neutrons and $Z$ protons in a common volume the kinetic energy per nucleon is $\tfrac35E_F^0\cdot\tfrac12\left[(1+\delta)^{5/3}+(1-\delta)^{5/3}\right]$ with $\delta=\frac{N-Z}{A}$, expanding to $\tfrac35E_F^0+\tfrac13E_F^0\delta^2$: kinetic symmetry coefficient $a_A^{\rm kin}=\tfrac13E_F^0=12.3$ MeV for $E_F^0=36.8$ MeV. The empirical $\approx23$ MeV needs another $\sim11$ MeV from the *interaction*: it returns as $J$ in Module 17 and as the $\rho$ coupling in Module 24.

**Stability and Q-values [Must]**
- $Z_{\rm min}(A)=\frac A2\frac{1+(m_n-m_H)c^2/(4a_A)}{1+a_CA^{2/3}/(4a_A)}$; mass parabolas at fixed $A$ (one for odd $A$, two for even $A$); one- and two-nucleon separation energies $S_n(Z,N)=B(Z,N)-B(Z,N-1)$, $S_p$ likewise; **neutron drip at $S_n=0$**.
- Electron capture in a degenerate gas: $e^-+(A,Z)\to(A,Z-1)+\nu$ occurs when $\mu_e$ (including rest mass) exceeds $M_{\rm nuc}(A,Z-1)c^2-M_{\rm nuc}(A,Z)c^2$, and the product's own $\beta^-$ decay is Pauli-blocked.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Krane 3: the formula and its terms; exercise 1 |
| Session 2 | Mass parabolas, $Z_{\min}$, Q-values; exercises 2 to 4 |
| Session 3 | Separation energies and drip; electron capture; exercises 5 to 8 |
| Session 4 | Exercises 9 and 10 |

## Derive from scratch

1. The symmetry term from the Fermi gas.
2. The Coulomb term from the uniform sphere.
3. $Z_{\rm min}(A)$ from $\partial M/\partial Z=0$.
4. The $\beta$-stability and electron-capture conditions.
5. $S_n$ and $S_p$ from the formula (leading terms).

## Bare-minimum exercises (with expected results)

1. **Symmetry coefficient:** $a_A^{\rm kin}=\tfrac13E_F^0\approx12.3$ MeV against the empirical $\approx23$ MeV; the gap (about half) is the interaction contribution (the isospin dependence of the potential energy).
2. **Beta stability:** $Z_{\rm min}(56)\approx25.4$ and $Z_{\rm min}(118)\approx50.2$ (for $a_A=23.2$, $a_C=0.714$); compare with the stable $^{56}$Fe ($Z=26$) and $^{118}$Sn ($Z=50$); $^{118}$Kr ($Z=36$) lies far on the neutron-rich side of stability.
3. **Binding energy of $^{56}$Fe:** the formula gives $B\approx485.7$ MeV ($\approx8.67$ MeV per nucleon; measured $8.79$) with the pieces $884.8-267.9-126.2-6.6+1.6$.
4. **Separation energies:** for $^{56}$Fe $S_n=11.2$ MeV and $S_p=10.2$ MeV; for the neutron-rich $^{118}$Kr ($N=82$) the extrapolated $S_n$ is only a few MeV. Ask what it would take for $S_n$ to reach zero: that is **neutron drip**.
5. **Pairing:** with $\delta=12/\sqrt A$, $\delta(^{56}{\rm Fe})=1.6$ MeV; show an even-even nucleus is more bound than its odd neighbours by about $2\delta$ between even-$A$ isobars.
6. **Mass parabola:** for fixed even $A$ the two parabolas (even-even and odd-odd) are separated by $2\delta$; explain double $\beta$-decay isobars.
7. **Electron-capture threshold:** $^{56}$Fe$\to{}^{56}$Mn needs $\mu_e>M_{\rm nuc}(^{56}{\rm Mn})-M_{\rm nuc}(^{56}{\rm Fe})=3.695+0.511=4.21$ MeV (atomic mass difference plus $m_e$); this is evaluated as a density in Module 05.
8. **Why neutron-rich under compression:** as $\mu_e$ rises, electron capture lowers $Z/A$ and the nuclei move to larger $N/Z$ (the symmetry term makes it cost less than the lattice energy gained, Module 05).
9. **Surface and Coulomb at fission:** the surface coefficient $a_S$ and $a_C$ give $(Z^2/A)_{\rm crit}=2a_S/a_C\approx51$ (used in Module 14).
10. **Five origins:** write one sentence for each term's physical origin and which of Modules 11, 17 and 24 returns to it.

## Optional extension

Fit $a_V,a_S,a_C,a_A$ to ten tabulated even-even binding energies by least squares and check the residuals: they show the shell structure the formula lacks.

## Pitfalls

- Using $Z(Z-1)$ versus $Z^2$ in the Coulomb term inconsistently.
- Taking the pairing term sign backwards (even-even are *more* bound).
- Forgetting the rest mass in the electron-capture threshold.

## Gate questions

1. Why does the pairing term make the crust even-$Z$?
2. Why does the symmetry term push nuclei neutron-rich under compression?
3. What does $S_n=0$ define?

## One-page cheat sheet contents

The formula with coefficients; symmetry and Coulomb derivations; $Z_{\min}(A)$; separation energies; electron-capture condition.
