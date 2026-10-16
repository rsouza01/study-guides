# Module 13: Hartree-Fock, Skyrme and energy density functionals (★, Week 12) and the Month-3 gate

**Books:** Wong's Hartree-Fock sections; Ring and Schuck chapter 5 as reference; Fetter and Walecka chapter 1 (the variational derivation you met in Module 02).
**Time:** 1 week (the gate sits at the end of this week; Module 16's consolidation doubles as recovery).

## Why this matters: the conceptual keystone of the first half

The shell-model potential becomes *self-consistent*. Then the practical resolution of the hard-core problem: an **effective** interaction. The Skyrme force
$$v_{12}=t_0(1+x_0P_\sigma)\delta(\mathbf r)+\tfrac12t_1(\ldots)+t_2(\ldots)+\tfrac16t_3(1+x_3P_\sigma)n^\alpha\delta(\mathbf r)+iW_0(\ldots)$$
is zero-range, momentum-dependent, density-dependent and fitted, reducing the many-body problem to an energy density functional. **Every modern unified neutron-star EOS (SLy4, BSk) is a Skyrme functional.**

## Skip-test (40 minutes, no notes)

1. Derive the HF equations by varying $\langle\Phi|H|\Phi\rangle$ with orthonormality constraints; identify the exchange term and explain why it has no classical analogue.
2. For the Skyrme force, derive $E/A$ for infinite symmetric nuclear matter in terms of $t_0$, $t_3$, $\alpha$ and the momentum-dependent terms.
3. Explain why a $\delta$-function effective interaction succeeds where the bare force makes HF diverge.
4. Compute the Skyrme effective mass $m^*/m$ for SLy4.
5. Describe the self-consistency loop of an HF code.

## Prerequisites

Modules 02, 10 and 11.

## Detailed topics (checklist)

**Hartree-Fock theory [Must]**
- $E_{\rm HF}[\{\phi_i\}]=\sum_i\langle i|t|i\rangle+\tfrac12\sum_{ij}\left[\langle ij|v|ij\rangle-\langle ij|v|ji\rangle\right]$; variation gives $\left[-\frac{\hbar^2}{2m}\nabla^2+U_H(\mathbf r)\right]\phi_i-\int U_x(\mathbf r,\mathbf r')\phi_i(\mathbf r')d^3r'=\epsilon_i\phi_i$ with a local direct (Hartree) field and a nonlocal exchange field; self-consistency; Koopmans' theorem; the single-particle energies as separation energies (approximately).
- **The hard-core problem:** a bare $v$ with a repulsive core has $\langle v\rangle=\infty$; Brueckner resummation (Module 18) or an effective force avoids it.

**Skyrme functional [Must]**
- Parameters $t_0,t_1,t_2,t_3,x_0,\dots,x_3,\alpha,W_0$; the energy per particle of symmetric matter
$$\frac EA(n)=\frac35\frac{\hbar^2k_F^2}{2m}+\frac38t_0n+\frac1{16}t_3n^{\alpha+1}+\frac{3}{80}\left[3t_1+(5+4x_2)t_2\right]nk_F^2,\quad k_F=\left(\tfrac{3\pi^2n}{2}\right)^{1/3}$$
(verify against Chabanat et al. for your parameter set); effective mass $\frac{m^*}{m}=\left[1+\frac{m}{8\hbar^2}\left(3t_1+(5+4x_2)t_2\right)n\right]^{-1}$; the spin-orbit term $\propto W_0$ (**fitted, not derived**: Module 21 explains it).
- SLy4 (published): $t_0=-2488.91$, $t_1=486.82$, $t_2=-546.39$, $t_3=13777.0$, $x_0=0.834$, $x_1=-0.344$, $x_2=-1.0$, $x_3=1.354$, $W_0=123$, $\alpha=\tfrac16$ (energies in MeV and fm); it gives $n_0\approx0.160$ fm$^{-3}$, $E/A\approx-15.97$ MeV, $K\approx230$ MeV, $J=32.0$ MeV, $L=45.9$ MeV.

**Energy density functionals [Should]**
- The Hohenberg-Kohn-style statement that the ground-state energy is a functional of the densities; Skyrme, Gogny and RMF functionals as phenomenological members; fits to masses and radii.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Wong: Hartree-Fock; the variational derivation; exercise 1 |
| Session 2 | The Skyrme force and the matter energy; exercises 2 and 8 |
| Session 3 | Why $\delta$-forces work; exercises 3 to 5 |
| Session 4 | Exercises 6 to 10; the Month-3 gate |

## Derive from scratch

1. The HF equations from the variational principle.
2. The Skyrme symmetric-matter energy per particle.
3. $m^*/m$ for a Skyrme force.
4. The exchange term for a $\delta$-force.
5. The self-consistency iteration.

## Bare-minimum exercises (with expected results)

1. **HF derivation:** vary $E_{\rm HF}$ under $\langle\phi_i|\phi_j\rangle=\delta_{ij}$ (Lagrange multipliers $\epsilon_i$); identify the direct and exchange terms and explain why exchange has no classical analogue (it is an antisymmetrisation effect: no counterpart for distinguishable particles).
2. **Skyrme symmetric matter (keep this: Module 17 needs it):** evaluate the energy per particle above for SLy4: minimum at $n_0=0.1595$ fm$^{-3}$ with $E/A=-15.97$ MeV and $K=9n_0^2\frac{d^2(E/A)}{dn^2}=229.9$ MeV; check the three kinds of terms (kinetic, $t_0$ attraction, $t_3$ density-dependent repulsion at large $n$, momentum-dependent).
3. **Why a $\delta$ force works:** a zero-range density-dependent force has finite matrix elements; the density-dependent term mimics the in-medium reduction of the bare interaction by Pauli blocking (the $G$-matrix, Module 18).
4. **Exchange for a $\delta$ force:** for the $t_0(1+x_0P_\sigma)\delta$ term, like-particle pairs interact only in the spin-singlet channel, so pure neutron matter has $\frac EN\ni\frac14t_0(1-x_0)n$ while symmetric matter has $\frac EA\ni\frac38t_0n$ (independent of $x_0$); derive both from the direct and exchange terms and note the spin-isospin averaging.
5. **Self-consistency loop:** guess $\rho$; construct $U(\mathbf r)$; solve for the $\phi_i$; rebuild $\rho$; iterate with damping until $\Delta E<10^{-6}$; the same loop returns for the $\sigma$ field in Module 22.
6. **Effective mass of SLy4:** $\Theta_s=3t_1+(5+4x_2)t_2=914$ MeV fm$^5$ and $\frac{m}{8\hbar^2}=0.0030$ fm$^{-2}$ MeV$^{-1}$ give $\frac{m^*}{m}=\frac{1}{1+0.0030\times914\times0.1595}=0.69$.
7. **Sign of $t_3$:** show a *positive* $t_3$ term (repulsive, $n^{\alpha+1}$) provides saturation: attraction from $t_0<0$ scaling as $n$ is overcome at high density by $n^{\alpha+1}$ (and the kinetic term $n^{2/3}$).
8. **Neutron matter and the symmetry energy:** with $\frac EN\Big|_{\rm PNM}=\frac35\frac{\hbar^2k_n^2}{2m}+\frac14t_0(1-x_0)n+\frac1{24}t_3(1-x_3)n^{\alpha+1}+\frac{3}{40}k_n^2n\left[t_1(1-x_1)+3t_2(1+x_2)\right]$, $k_n=(3\pi^2n)^{1/3}$, SLy4 gives $16.7$ MeV at $n=0.1595$ fm$^{-3}$, so the difference from symmetric matter is $\approx32.7$ MeV ($J=32.0$ and $L\approx46$ MeV from the quadratic expansion in $\delta$): Module 17 starts from this.
9. **EDF viewpoint:** write the total energy as $\int\varepsilon[n_n,n_p,\tau,\mathbf J]d^3r$ and say which variables the Skyrme functional uses (densities $n_q$, kinetic densities $\tau_q$, spin-orbit densities $\mathbf J_q$).
10. **Month-3 gate prep:** attempt the five items below.

## Blank-page gate: Month 3

1. Magic numbers and three independent lines of evidence.
2. Derive the level ordering from oscillator plus $\mathbf l\cdot\mathbf s$; predict $J^\pi$ for four odd-$A$ nuclei; state the anomalous spin-orbit magnitude. **Write "explained in Module 21" beside it.**
3. Pairing from the $\delta$-force; the SEMF pairing term; the crust consequence.
4. Vibrator versus rotor signatures; the moment-of-inertia deficit and its explanation.
5. Derive the HF equations; write the Skyrme functional; derive $E/A$ for symmetric matter.

### Computational task (optional)

A spherical HF solver for $^{16}$O or $^{40}$Ca with a simplified Skyrme force. About 300 lines. The value is *feeling* self-consistency converge: the same loop you re-run in Module 22 for the $\sigma$ field.

## Pitfalls

- Treating $t_3$ as a three-body force without the two-body $\delta$ interpretation ($\alpha$ non-integer is a density dependence).
- Using Skyrme parameter sets with different conventions for $x_i$ and $W_0$.
- Expecting HF eigenvalues to be exact separation energies.

## Gate questions

1. Why does a $\delta$-function interaction avoid the hard-core divergence?
2. Which Skyrme terms provide saturation?
3. Why is the Skyrme $W_0$ a fit parameter, and where will it be explained?

## One-page cheat sheet contents

HF equations; Skyrme force and the symmetric-matter $E/A$; $m^*/m$; SLy4 values; the self-consistency loop.
