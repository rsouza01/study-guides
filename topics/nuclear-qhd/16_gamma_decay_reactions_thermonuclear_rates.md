# Module 16: Gamma decay, reactions, thermonuclear rates, and Consolidation 2 (Week 15)

**Books:** Krane chapter 10 sections 1 to 5 (gamma decay); Krane chapter 11 sections 1 to 6 selectively (reactions); Krane chapter 14 or **Iliadis, *Nuclear Physics of Stars*, chapter 3** (thermonuclear rates); Chamel and Haensel section 4.3 and the Haensel-Zdunik papers for the pycnonuclear end; **plus** any electrodynamics text's treatment of multipole radiation for the classical skeleton (your electrodynamics guide, Modules 20 and 21).
**Time:** 1 week, with **about 1.5 weeks of material**.

> **⚠ Budget note.** This module carries the classical multipole expansion, which an electrodynamics track would otherwise supply. Either take the overflow into Module 17's opening, or do the optional hour in Module 02 that pre-pays for it. Do not simply compress the $\gamma$ section: Weisskopf estimates are the transferable skill here.

## Why this matters

**Gamma decay.** Build the multipole expansion of the radiation field, then apply angular momentum and parity selection rules. Weisskopf single-particle estimates give transition rates from dimensional analysis plus a wavefunction overlap; the $\omega^{2L+1}$ scaling explains the whole lifetime hierarchy, why $E2$ competes with $M1$, and why isomers exist. ↪ **Return to your Module 12 collective results and express those $B(E2)$ values in Weisskopf units**: a factor $\sim100$ over a single-particle estimate is the quantitative definition of "collective".

**Reactions and thermonuclear rates.** Maxwell-Boltzmann tail $\times$ Gamow tunnelling $=$ the **Gamow peak**; the astrophysical $S$-factor; screening. ↪ The payoff: **X-ray bursts** (unstable H/He burning on the surface), **superbursts** (carbon ignition in the outer crust at $\sim10^9$ g/cm$^3$), **pycnonuclear reactions** (fusion at $T\to0$ driven by lattice zero-point motion: Module 14's tunnelling calculation transplanted into Module 05's crystal), and with the Module 15 electron-capture chains, **deep crustal heating** of $1$ to $2$ MeV per accreted nucleon: the thermal budget of an accreting neutron star's crust.

## Skip-test (40 minutes, no notes)

1. Compute the Weisskopf estimates for $E1$, $E2$, $E3$ and $M1$ at 1 MeV and tabulate.
2. For three transitions with known $J^\pi$ list the allowed multipolarities and the dominant one.
3. Derive the location and width of the Gamow peak.
4. Evaluate the Gamow peak for $^{12}$C$+^{12}$C at superburst conditions.
5. State what pycnonuclear means and why it needs no temperature.

## Prerequisites

Modules 12, 14 and 15; electrodynamics background (multipole radiation).

## Detailed topics (checklist)

**Gamma decay [Must]**
- Multipole fields: build $\mathbf A(\mathbf x)\propto\frac{e^{ikr}}{r}\int\mathbf J(\mathbf x')e^{-ik\hat{\mathbf n}\cdot\mathbf x'}d^3x'$ and expand in $kr'$; the leading term is the electric dipole; each higher order costs $(kR)^2$; the transition rate for $E1$: $\lambda=\frac{4\alpha\omega^3}{3c^2}|\langle f|\mathbf r|i\rangle|^2$.
- Selection rules: $|J_i-J_f|\le L\le J_i+J_f$ ($L\ne0$); $E L$ changes parity by $(-1)^L$, $M L$ by $(-1)^{L+1}$; Weisskopf rates ($E$ in MeV, $\lambda$ in s$^{-1}$): $\lambda(E1)=1.0\times10^{14}A^{2/3}E^3$, $\lambda(M1)=5.6\times10^{13}E^3$, $\lambda(E2)=7.3\times10^7A^{4/3}E^5$, $\lambda(M2)=3.5\times10^7A^{2/3}E^5$, $\lambda(E3)=34A^2E^7$; Weisskopf unit $B_W(E2)=0.0594A^{4/3}\ e^2{\rm fm}^4$; internal conversion as the competing channel; $E0$ and $0^+\to0^+$ transitions (no single photon).

**Reactions [Should]**
- Q-values and kinematics; cross section $\sigma$, $n\sigma v$; the compound nucleus and Breit-Wigner $\sigma=\pi\bar\lambda^2\frac{2J+1}{(2s_1+1)(2s_2+1)}\frac{\Gamma_a\Gamma_b}{(E-E_R)^2+\Gamma^2/4}$; level densities; a glance at direct reactions. Working level only; reaction *theory* is the appendix.

**Thermonuclear rates [Must]**
- $\langle\sigma v\rangle=\sqrt{\frac{8}{\pi\mu}}\frac{1}{(kT)^{3/2}}\int\sigma(E)Ee^{-E/kT}dE$; $\sigma(E)=\frac{S(E)}{E}e^{-2\pi\eta}$ with $2\pi\eta=\frac{b}{\sqrt E}$, $b=31.29Z_1Z_2\sqrt\mu$ keV$^{1/2}$ ($\mu$ in amu); Gamow peak $E_0=\left(\frac{bkT}2\right)^{2/3}$, width $\Delta=\frac{4}{\sqrt3}\sqrt{E_0kT}$; electron screening.
- **Pycnonuclear reactions** at $T\to0$: tunnelling driven by the zero-point motion of ions in the Coulomb lattice, with a rate that rises steeply with density and is independent of $T$.
- **Deep crustal heating:** the net energy released by electron captures, neutron emission and pycnonuclear fusions as accreted matter sinks through the crust totals $\sim1$ to $2$ MeV per accreted nucleon, to be compared with $\sim5$ to $7$ MeV per nucleon from surface H/He burning and $\sim200$ MeV per nucleon of gravitational energy.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Krane 10.1 to 10.3: multipoles and selection rules; exercises 1 to 3 |
| Session 2 | Krane 10.4 to 10.5: Weisskopf; internal conversion; exercises 2 and 9 |
| Session 3 | Krane 11: reactions; Breit-Wigner; exercise 6 |
| Session 4 | Iliadis 3: the Gamow peak; exercises 4, 5, 7, 8; the Consolidation 2 gate |

## Derive from scratch

1. The multipole expansion of the radiation field and the $\omega^{2L+1}$ scaling.
2. The Weisskopf estimate by dimensional analysis.
3. The Gamow peak position and width.
4. The Breit-Wigner peak cross-section.
5. The energy budget of the schematic deep-heating chain.

## Bare-minimum exercises (with expected results)

1. **Weisskopf table ($A=100$, $E=1$ MeV):** $\lambda(E1)=2.2\times10^{15}$, $\lambda(M1)=5.6\times10^{13}$, $\lambda(E2)=3.4\times10^{10}$, $\lambda(E3)=3.4\times10^5$ s$^{-1}$: each step in $L$ costs $10^{-4}$ to $10^{-5}$ (the $(kR)^{2}$ suppression $\sim(ER/\hbar c)^2\approx6\times10^{-4}$ times numerical factors); $M1$ competes with $E2$ and is $\sim20$ times slower than $E1$.
2. **Collectivity in Weisskopf units:** for $^{168}$Er $B(E2;2^+\to0^+)=\frac{B(E2\uparrow)}{5}=1.16\ e^2{\rm b}^2=11\,600\ e^2{\rm fm}^4$ and $B_W=0.0594A^{4/3}=55\ e^2{\rm fm}^4$: $\approx210$ W.u.; a factor $\sim100$ to $200$ over a single particle is what "collective" means.
3. **Selection rules:** $2^+\to0^+$: $L=2$, $E2$; $1^-\to0^+$: $L=1$, $E1$; $\tfrac32^+\to\tfrac12^+$: $L=1,2$ and no parity change, so $M1$ and $E2$ (mixed; $M1$ dominates unless hindered); $0^+\to0^+$: no single-photon transition (internal conversion or pair emission), the case where the obvious answer is wrong.
4. **Gamow peak for $^{12}$C$+{}^{12}$C at superburst conditions** ($T=5\times10^8$ K, $kT=43$ keV): $b=31.29\times36\times\sqrt6=2760$ keV$^{1/2}$, $E_0=\left(\frac{bkT}{2}\right)^{2/3}\approx1.5$ MeV, $\Delta=\frac{4}{\sqrt3}\sqrt{E_0kT}\approx0.6$ MeV; for $p+p$ at $kT=1.3$ keV, $E_0=5.9$ keV (compare Thermodynamics guide Module 07).
5. **Why the peak is far above $kT$:** $\frac{E_0}{kT}=\left(\frac{b}{2\sqrt{kT}}\right)^{2/3}\approx35$ for the carbon case: the Maxwell-Boltzmann tail and the tunnelling factor balance far in the tail.
6. **Breit-Wigner:** at the peak $\sigma=4\pi\bar\lambda^2\frac{2J+1}{(2s_1+1)(2s_2+1)}\frac{\Gamma_a\Gamma_b}{\Gamma^2}$; for a neutron resonance with $\Gamma_n\approx\Gamma$ the cross-section is $\approx4\pi\bar\lambda^2\cdot\frac{2J+1}{2}$, enormous at low energy because $\bar\lambda\propto E^{-1/2}$.
7. **Pycnonuclear fusion:** explain in words why the rate depends on density but not temperature (the lattice zero-point energy $\hbar\omega_p$ supplies the "kinetic energy" and tunnelling through the Coulomb barrier between neighbouring ions does the rest); cf. Module 14 exercise 4 with the barrier replaced by the inter-ion barrier.
8. **Deep-heating chain (schematic):** the net energy per accreted nucleon is $\sim1$ to $2$ MeV; list the three kinds of reaction (electron capture lowering $Z$, neutron emission at drip, pycnonuclear fusion), say which releases heat deposited in the crust versus carried away by neutrinos, and compare with the $\sim200$ MeV per nucleon of accretion luminosity.
9. **Internal conversion:** the conversion coefficient $\alpha_{\rm IC}$ grows with $Z$ and with decreasing $E$ and increasing multipolarity; for $E0$ and $0^+\to0^+$ it is the only decay mode.
10. **Consolidation 2 gate prep:** attempt the ten items below.

## Blank-page gate: Consolidation 2 (Month 3 and Module D)

1. The shell-model level scheme; $J^\pi$ for four nuclei.
2. Pairing from the $\delta$ force; the SEMF term; the crust consequence.
3. Vibrator versus rotor; the moment-of-inertia deficit and its explanation.
4. HF from the variational principle; the Skyrme functional; $E/A$ for symmetric matter.
5. Decay law, chains, secular equilibrium.
6. **Fission deformation energy, fissility, and the two relations ($E_{\rm Coul}=2E_{\rm surf}$ at $x=1$; $E_{\rm surf}=2E_{\rm Coul}$ for the cell).**
7. The Gamow factor and Geiger-Nuttall.
8. Allowed $\beta$ spectrum from phase space; Kurie plot; Fermi versus Gamow-Teller selection rules; $ft$.
9. Weisskopf estimates and $\gamma$ selection rules; the $\omega^{2L+1}$ hierarchy.
10. The Gamow peak; what pycnonuclear means and why it needs no temperature.

**Cut if behind:** compressible order within Module D: reaction theory in this module (compound nucleus and Breit-Wigner to orientation level), then decay kinetics in Module 14, then Kurie/neutrino-mass in Module 15. **Never** drop the fission deformation energy, the $\beta$-decay rate structure, or the Gamow peak.

## Optional extension

Compute the thermonuclear rate $\langle\sigma v\rangle$ for $^{12}$C$+^{12}$C numerically from a simple $S$-factor and verify the Gamow-peak position and width by integrating the product of the Maxwell-Boltzmann tail and the tunnelling factor.

## Pitfalls

- Forgetting the $\theta$-function conditions in the rate integral ($\sigma(E)$ at the Gamow peak, not at $kT$).
- Using Weisskopf rates for collective transitions without the enhancement factor.
- Applying selection rules without checking parity.

## Gate questions

1. Why does the $\gamma$-ray rate scale as $\omega^{2L+1}$?
2. Why is the Gamow peak at $E_0\gg kT$?
3. What makes pycnonuclear fusion temperature independent?

## One-page cheat sheet contents

Weisskopf rates and $B_W$; selection rules; Gamow peak formulas; Breit-Wigner; deep-heating energy bookkeeping.
