# Module 09: Isospin, charge independence, the modern picture, and the Month-2 gate (Week 8)

**Books:** Walecka chapter 1 remainder; Bertulani on charge independence and charge-symmetry breaking (CSB); then **90 minutes of orientation only** on chiral EFT (N$^3$LO potentials, power counting, three-nucleon forces): learning what the current answer looks like, not learning chiral EFT.
**Time:** 1 week.

## Why this matters

(i) **Isospin in the many-body setting**: the $\rho$ meson couples to the isovector current and the symmetry energy is an isospin statement. (ii) **Three-nucleon forces**, because pure neutron matter is materially affected by them, and any honest account of the crust-core transition must say so. This module is also the last of the dense Month 2 and ends with its gate and the **Week 8 checkpoint**.

## Skip-test (40 minutes, no notes)

1. Write the general NN potential allowed by translation, rotation, parity, time-reversal and isospin invariance; enumerate the operators.
2. List the allowed $(L,S,J,T)$ channels up to $J=2$ using $(-1)^{L+S+T}=-1$.
3. State what $a_{pp}$, $a_{nn}$ and $a_{np}$ (singlet) show about charge independence and charge-symmetry breaking.
4. Show the symmetry term $\propto\frac{(N-Z)^2}{A}$ is a $T^2$ statement.
5. Describe what a three-nucleon force does and why it matters for neutron matter.

## Prerequisites

Modules 01, 06, 07, 08.

## Detailed topics (checklist)

**The general NN interaction [Must]**
- Operator basis: central $1$, spin-spin $\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2$, tensor $S_{12}$, spin-orbit $\mathbf L\cdot\mathbf S$, quadratic spin-orbit $L^2$, $L^2\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2$, $(\mathbf L\cdot\mathbf S)^2$, each multiplied by $1$ or $\boldsymbol\tau_1\cdot\boldsymbol\tau_2$ (Argonne $v_{18}$ structure); which observable constrains which: deuteron $B$ (central, spin-spin), $Q$ and $P_D$ (tensor), $^3P_J$ splittings (spin-orbit), higher partial waves ($L^2$ terms).

**Charge independence [Must]**
- Isospin as an approximate symmetry; $m_{\pi^\pm}-m_{\pi^0}=4.6$ MeV and the neutron-proton mass difference break it; after removing Coulomb effects $a_{pp}\approx-17.3$ fm, $a_{nn}\approx-18.9$ fm, $a_{np}^{(^1S_0)}=-23.7$ fm: charge-symmetry breaking $a_{pp}\neq a_{nn}$ is a fraction of a fm, charge-independence breaking $\frac{a_{pp}+a_{nn}}{2}\neq a_{np}$ is larger ($\approx5.6$ fm) because it reflects the pion mass splitting in a nearly bound channel.

**Orientation: the modern picture [Should]**
- Chiral EFT: nucleons and pions as degrees of freedom, a power counting in $Q/\Lambda_\chi$, two-nucleon potentials at N$^3$LO that fit scattering data to $\chi^2/{\rm datum}\approx1$, **three-nucleon forces** at N$^2$LO (the Fujita-Miyazawa $\Delta$-excitation mechanism); effect: pure neutron matter and the saturation point are materially changed by the three-body force.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Walecka chapter 1 remainder: isospin and the general potential |
| Session 2 | Bertulani: charge independence and CSB; exercises 1 to 5 |
| Session 3 | Chiral EFT orientation (90 minutes); exercises 6 and 7 |
| Session 4 | Exercises 8 to 10; the Month-2 gate |

## Derive from scratch

1. The operator basis from symmetry alone.
2. The generalized Pauli principle for two nucleons including isospin.
3. $\frac{(N-Z)^2}{A}=\frac{4T_z^2}{A}$ and its connection to $T(T+1)$.
4. The estimate of CSB from the scattering lengths.
5. The role of a three-nucleon force in the Coester-line argument (preview).

## Bare-minimum exercises (with expected results)

1. **General potential:** enumerate $V=\sum_iV_i(r)O_i$ with $O_i\in\{1,\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2,S_{12},\mathbf L\cdot\mathbf S,L^2,\dots\}\times\{1,\boldsymbol\tau_1\cdot\boldsymbol\tau_2\}$; state which deuteron or phase-shift observable fixes each family.
2. **Allowed channels:** the rule $(-1)^{L+S+T}=-1$ gives, up to $J=2$: $^1S_0(T=1)$, $^3S_1$-$^3D_1(T=0)$, $^1P_1(T=0)$, $^3P_0$, $^3P_1$, $^3P_2$-$^3F_2$ $(T=1)$, $^1D_2(T=1)$, $^3D_2(T=0)$.
3. **CSB estimate:** with $a_{pp}=-17.3$ fm and $a_{nn}=-18.9$ fm the charge-symmetry breaking is $\Delta a=1.6$ fm, a few parts in $10^{2}$ of the strength of the $^1S_0$ interaction because $a$ is a sensitive function of the near-threshold strength.
4. **CIB estimate:** $\frac{a_{pp}+a_{nn}}{2}=-18.1$ fm versus $a_{np}=-23.7$ fm: the $T=1$ amplitudes differ by $5.6$ fm; show the origin in the $\pi^\pm$ versus $\pi^0$ mass difference via the shift of the Yukawa range.
5. **Isospin and the symmetry energy:** with $T=\frac{|N-Z|}{2}$, $\frac{(N-Z)^2}{A}=\frac{4T^2}{A}$; the term $a_A\frac{(N-Z)^2}{A}$ is an isospin-dependent energy, with $T(T+1)$ the exact quantum form for an $SU(2)_T$-symmetric Hamiltonian.
6. **Three-nucleon force:** a $\Delta$ excited in intermediate states by one nucleon while exchanging pions with two others gives a repulsive three-body force at $n_0$; state its effect on the saturation point and on pure neutron matter (Module 18).
7. **Chiral EFT power counting:** write which orders contain one-pion exchange, two-pion exchange and contact terms; explain why three-nucleon forces first appear at N$^2$LO.
8. **Parity and Pauli:** list the allowed $(S,T)$ for $L=1$ ($S=1,T=1$ or $S=0,T=0$) and explain why two neutrons ($T=1$) can be in $^1S_0$ or $^3P_J$ but never in $^3S_1$ (that needs $T=0$).
9. **The $nn$ system:** no bound state, $a_{nn}=-18.9$ fm: neutron matter at low density is the near-unitary Fermi gas of Module 19.
10. **Month-2 gate prep:** attempt the five items below.

## Blank-page gate: Month 2

1. List the deuteron observables; derive from each what it forces; end at "the tensor force must exist."
2. Derive the $s$-wave phase shift for a square well; derive the effective-range expansion; state shape independence.
3. **Derive the Yukawa potential from the static KG equation, contour and all**, and the OPEP spin-isospin structure. Get the tensor operator to emerge.
4. State and derive the sign rule: scalar attracts, vector repels.
5. Write the general NN interaction operator basis from symmetry alone.

### ⚑ Week 8 checkpoint: the two-track decision point

Look at your log. If this track has come in under 6 hours in two of the last eight weeks, **pause your secondary track now** and run single-track until the log recovers. Do not thin both.

**Cut if behind:** drop the chiral EFT orientation and the CSB exercise. **Never** drop Module 08.

## Optional extension

Compute the pion-mass-splitting contribution to $a_{np}-\frac{a_{pp}+a_{nn}}{2}$ with the Born approximation for the Yukawa potential of the two masses and compare with the exercise 4 numbers.

## Pitfalls

- Treating isospin as exact (the $\pi^\pm$-$\pi^0$ and $n$-$p$ mass differences break it).
- Forgetting the generalized Pauli principle when listing channels.
- Conflating CSB ($pp$ versus $nn$) with CIB ($np$ versus the average).

## Gate questions

1. Which deuteron observable constrains the tensor force and which the central force?
2. Why is charge-independence breaking larger than charge-symmetry breaking in $a$?
3. Why do three-nucleon forces matter for neutron matter?

## One-page cheat sheet contents

The operator basis; allowed channels; the four scattering lengths; Argonne-type structure; three-nucleon-force orientation.
