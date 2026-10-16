# Module 12: Collective models (★, Week 11)

**Books:** Krane chapter 5 section 5 in full; Bertulani's collective chapter; **Greiner and Maruhn, *Nuclear Models*** for worked examples on vibrations and rotations; Ring and Schuck chapters 1 and 6 as reference.
**Time:** 1 week.

## Why this matters

**The spectroscopic fingerprints.** Parametrise the surface as $R(\theta,\phi)=R_0\left[1+\sum_{\lambda\mu}\alpha_{\lambda\mu}Y_{\lambda\mu}\right]$. Quadrupole vibrations give phonon spectra: one-phonon $2^+$, two-phonon $(0^+,2^+,4^+)$ triplet, $\frac{E(4^+)}{E(2^+)}=2.0$. Rigid axial rotation gives $E_J=\frac{\hbar^2}{2\mathcal I}J(J+1)$, so $\frac{E(4^+)}{E(2^+)}=\frac{10}3$. Real nuclei sit at one limit or the other with startling fidelity: that ratio classifies a nucleus from two numbers.

**The moment-of-inertia deficit: the reason this week exists.** The measured $\mathcal I$ is roughly **half the rigid-body value** but several times the irrotational-flow value. The resolution is **pairing**: paired nucleons form a superfluid that does not follow the rotation. This is the cleanest laboratory evidence for nuclear superfluidity, and it is the *same* superfluidity that in the inner crust stores angular momentum and releases it in pulsar glitches. Backbending is the finite-nucleus analogue of vortex unpinning.

## Skip-test (40 minutes, no notes)

1. Derive $\frac{E(4^+)}{E(2^+)}$ for the harmonic quadrupole vibrator and the rigid axial rotor.
2. Compute rigid-body and irrotational-flow moments of inertia at $\beta_2=0.3$ and compare with the value extracted from a measured rare-earth $2^+$ energy.
3. Explain qualitatively the Nilsson diagram: why a single-$j$ level splits into $j+\tfrac12$ doublets under deformation.
4. Derive the $A^{-1/3}$ scaling of the giant dipole resonance energy in a two-fluid model.
5. Relate $\beta_2$ to $B(E2\uparrow)$.

## Prerequisites

Modules 10 and 11.

## Detailed topics (checklist)

**Vibrations and rotations [Must]**
- Quadrupole vibrator $E_n=n\hbar\omega_2$, multiplets $0^+,2^+,4^+$ at $2\hbar\omega_2$; rigid axial rotor $E_J=\frac{\hbar^2}{2\mathcal I}J(J+1)$ with $J=0,2,4,\dots$ for even-even; ratios $2.0$ and $3.33$; transitional nuclei in between.
- Deformation: $\beta_2$ from $B(E2;0^+\to2^+)=\left(\frac{3}{4\pi}ZeR_0^2\right)^2\beta_2^2$ (about $50.6\ \beta_2^2\ e^2$b$^2$ for $A=168$).

**Moments of inertia [Must]**
- Rigid body $\mathcal I_{\rm rig}=\tfrac25AMR_0^2(1+0.31\beta_2)$; irrotational flow $\mathcal I_{\rm irr}=\frac{9}{8\pi}AMR_0^2\beta_2^2$; measured values lie between: the **superfluid** (paired) nucleons do not rotate rigidly; backbending as pairs break.

**Single-particle motion in a deformed field [Should]**
- The Nilsson model: $\Omega$ ($=K$) as the good quantum number; each spherical $j$ splits into $\frac{2j+1}{2}$ doublets $\pm\Omega$; level crossing and the lowering of the energy of a mid-shell nucleus by deformation (Jahn-Teller-like).

**Giant resonances [Should]**
- The giant dipole resonance as protons oscillating against neutrons with the symmetry energy as restoring force: $E_{\rm GDR}\approx78A^{-1/3}$ MeV; the electric dipole polarizability $\alpha_D$ of $^{208}$Pb as a laboratory constraint on $L$, in tension with PREX-II.

↪ **Thread A:** every mass model used for the crust (FRDM, HFB-2x) must get deformation energy right, because neutron-rich nuclei near drip are not spherical and their masses are not measured: your Module 05 composition curve past $N=82$ is only as good as that deformation physics.

*Note:* the Weisskopf yardstick that makes "enhanced $B(E2)$" quantitative arrives in Module 16. Take the factor $\sim100$ as data for now.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Krane 5.5: vibrations and rotations; exercises 1 and 5 |
| Session 2 | Moments of inertia; exercises 2 and 6 |
| Session 3 | Nilsson model and deformation; exercise 3 |
| Session 4 | Giant resonances; exercises 4, 7 to 10 |

## Derive from scratch

1. $\frac{E(4^+)}{E(2^+)}$ for both limits.
2. The rigid and irrotational moments of inertia.
3. $B(E2)$ in terms of $\beta_2$.
4. The two-fluid GDR energy scaling.
5. The Nilsson splitting argument.

## Bare-minimum exercises (with expected results)

1. **Ratios:** vibrator $\frac{E_4}{E_2}=2.0$, rotor $\frac{J(J+1)|_{4}}{J(J+1)|_2}=\frac{20}{6}=3.33$. Classify from data: $^{110}$Cd has $R=2.34$ (vibrator), $^{168}$Er has $R=3.31$ (rotor), $^{152}$Sm has $R=3.01$ (transitional: a shape-phase-transition region where neither limit applies).
2. **Moment of inertia (keep this page):** for $^{168}$Er ($A=168$, $\beta_2\approx0.3$, $E(2^+)=79.8$ keV): $\mathcal I_{\rm meas}=\frac{3\hbar^2}{E(2^+)}=37.6\ \hbar^2$/MeV, $\mathcal I_{\rm rig}\approx77\ \hbar^2$/MeV and $\mathcal I_{\rm irr}\approx5.7\ \hbar^2$/MeV: the measured value is about **half the rigid value** and several times the irrotational value. Implication: only part of the nucleus (the unpaired or normal component) follows the rotation; the rest is superfluid.
3. **Nilsson diagram (qualitative):** under quadrupole deformation a spherical level $j$ splits into $\frac{2j+1}2$ doublets labelled by $\Omega=|m_j|$; low-$\Omega$ states are lowered for prolate shapes (the orbit lies in the symmetry plane, near the bulk); a mid-shell nucleus lowers its energy by deforming because occupied low-$\Omega$ levels gain.
4. **GDR:** $E_{\rm GDR}\approx78A^{-1/3}$ MeV gives $13.2$ MeV for $^{208}$Pb (observed $13.5$); in a two-fluid model the restoring force constant is set by the symmetry energy coefficient and the mass by $\frac{NZ}{A}M$, giving $E\propto\frac{1}{R}\propto A^{-1/3}$ with a coefficient of $70$ to $80$ MeV for Goldhaber-Teller or Steinwedel-Jensen flow.
5. **Deformation from $B(E2)$:** with $B(E2\uparrow)=5.8\ e^2{\rm b}^2$ for $^{168}$Er and $\left(\frac{3}{4\pi}ZeR_0^2\right)^2=50.6\ e^2{\rm b}^2$ ($Z=68$, $R_0=6.62$ fm) get $\beta_2=\sqrt{5.8/50.6}\approx0.34$.
6. **Superfluid fraction:** $\frac{\mathcal I_{\rm meas}}{\mathcal I_{\rm rig}}=\frac{37.6}{77}\approx0.49$; explain why the BCS moment of inertia (Inglis cranking with pairing) approaches the irrotational value as $\Delta\to\infty$ and the rigid value as $\Delta\to0$.
7. **Backbending:** sketch $\frac{2\mathcal I}{\hbar^2}$ versus $(\hbar\omega)^2$ showing the sudden jump when a pair of high-$j$ nucleons breaks (Coriolis anti-pairing) and relate to vortex unpinning.
8. **Surface parametrisation:** volume conservation fixes $\alpha_{00}=-\frac{1}{\sqrt{4\pi}}\sum|\alpha_{\lambda\mu}|^2$; show the quadrupole surface for $\alpha_{20}=\beta_2$ is prolate for $\beta_2>0$.
9. **Phonon triplet:** list the states of the two-phonon quadrupole multiplet ($0^+,2^+,4^+$) and state which are observed in $^{110}$Cd (all three, near $2E(2^+)$).
10. **Crust hook:** state in two sentences why a mass model that omits deformation overbinds the wrong nuclei near $N=82$ drip and so shifts the composition and the drip density.

## Optional extension

Compute the Nilsson levels for $\kappa=0.06$, $\mu=0.5$ numerically for the $N=4$ shell as a function of $\epsilon$ and locate the level crossings that underlie the sudden onset of deformation in the rare earths.

## Pitfalls

- Using the rigid moment of inertia without the superfluid correction.
- Confusing $\beta_2$ conventions (some texts include a factor of $\sqrt{4\pi/5}$).
- Reading $R=2$ as proof of a vibrator when anharmonicities exist.

## Gate questions

1. Why is $\mathcal I_{\rm meas}\approx\tfrac12\mathcal I_{\rm rig}$ evidence for pairing?
2. Why is the GDR energy $\propto A^{-1/3}$?
3. Why must a crust mass model include deformation?

## One-page cheat sheet contents

Vibrator and rotor ratios; moments of inertia and the deficit; $\beta_2$ from $B(E2)$; GDR scaling; Nilsson sketch.
