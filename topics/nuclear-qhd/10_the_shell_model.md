# Module 10: The shell model (★, Week 9)

**Books:** Krane chapter 5 sections 1 to 3; Wong's shell-model chapter; **Walecka's shell-model chapter**, sections 1 to 2.
**Time:** 1 week. Month 3 asks: **given a strong, short-ranged, hard-core interaction, why does an independent-particle model work at all?**

## Why this matters

Evidence first: magic numbers $2,8,20,28,50,82,126$ in separation energies, stable-isotope abundances, quadrupole moments and capture cross-sections. Then mechanism: a harmonic oscillator or Woods-Saxon potential gives $2,8,20$ and fails; **adding $-\zeta(r)\,\mathbf l\cdot\mathbf s$ with a large negative coefficient** produces the rest. Two margin notes. The required spin-orbit strength far exceeds the atomic (Thomas) value: unexplained in 1949, *derived* in Module 21 from the relativistic mean field. And $N=50$ and $N=82$ are exactly the plateaus in your Module 05 output: the crust has shell structure because the mass table does.

## Skip-test (40 minutes, no notes)

1. Fill the 3D harmonic-oscillator levels and get $2,8,20,40,70$; add $\mathbf l\cdot\mathbf s$ and show the intruder orbitals produce $28,50,82,126$.
2. Predict $J^\pi$ for $^{15}$O, $^{17}$O, $^{41}$Ca, $^{207}$Pb.
3. Compute Schmidt magnetic moments for those states and compare with measurement.
4. List three independent lines of experimental evidence for magic numbers.
5. State the Woods-Saxon-plus-spin-orbit level order up to 126.

## Prerequisites

Modules 01 and 03.

## Detailed topics (checklist)

**Evidence for shells [Must]**
- Two-neutron separation energies drop after a magic number; unusually many stable isotopes and isotones; small neutron-capture cross-sections; first $2^+$ energies large and $B(E2)$ small at closed shells; magic numbers $2,8,20,28,50,82,126$.

**The mean field [Must]**
- Harmonic oscillator $E_N=(N+\tfrac32)\hbar\omega$, $\hbar\omega\approx41A^{-1/3}$ MeV, with degeneracies $(N+1)(N+2)$ and cumulative $2,8,20,40,70,112$; Woods-Saxon $V(r)=-\frac{V_0}{1+e^{(r-R)/a}}$ with $V_0\approx50$ MeV; the spin-orbit term $V_{ls}(r)\,\mathbf l\cdot\mathbf s$ with $\langle\mathbf l\cdot\mathbf s\rangle=\tfrac12\ell$ for $j=\ell+\tfrac12$ and $-\tfrac12(\ell+1)$ for $j=\ell-\tfrac12$ and the sign such that $j=\ell+\tfrac12$ is *lower*; level order $1s_{1/2}\,|\,1p_{3/2}1p_{1/2}\,|\,1d_{5/2}2s_{1/2}1d_{3/2}\,|\,1f_{7/2}\,|\,2p_{3/2}1f_{5/2}2p_{1/2}1g_{9/2}\,|\,1g_{7/2}2d_{5/2}2d_{3/2}3s_{1/2}1h_{11/2}\,|\,\ldots1i_{13/2}$.
- Ground-state $J^\pi$ of odd-$A$ nuclei from the last unpaired nucleon (or hole); Schmidt magnetic moments $\mu=g_\ell(j-\tfrac12)+\tfrac12g_s$ for $j=\ell+\tfrac12$ and $\mu=\frac{j}{j+1}\left[(j+\tfrac32)g_\ell-\tfrac12g_s\right]$ for $j=\ell-\tfrac12$, with $g_\ell=1,0$ and $g_s=5.586,-3.826$ for proton, neutron.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Krane 5.1 to 5.2: evidence and the oscillator; exercises 1 and 4 |
| Session 2 | Spin-orbit and the level scheme; exercise 1 |
| Session 3 | $J^\pi$ predictions and Schmidt moments; exercises 2 and 3 |
| Session 4 | Walecka shell-model chapter 1 to 2; exercises 5 to 10 |

## Derive from scratch

1. The 3D oscillator level counting.
2. The $\mathbf l\cdot\mathbf s$ splitting and which orbitals are pushed down.
3. The shell-closure counting to 126.
4. The Schmidt formulas.
5. Why a $\delta$-function mean field misses the shell structure (preview of Module 13).

## Bare-minimum exercises (with expected results)

1. **Oscillator and spin-orbit:** the oscillator gives $2,8,20,40,70,112$; the $\mathbf l\cdot\mathbf s$ splitting lowers $1f_{7/2}$ from $N=3$ (so $28$ becomes a gap), $1g_{9/2}$ from $N=4$ ($50$), $1h_{11/2}$ from $N=5$ ($82$), $1i_{13/2}$ from $N=6$ ($126$); show the cumulative count to $126$.
2. **Ground-state spins:** $^{15}$O (neutron hole in $1p_{1/2}$): $\tfrac12^-$; $^{17}$O (neutron in $1d_{5/2}$): $\tfrac52^+$; $^{41}$Ca (neutron in $1f_{7/2}$): $\tfrac72^-$; $^{207}$Pb (neutron hole in $3p_{1/2}$): $\tfrac12^-$; all agree with data.
3. **Schmidt moments ($\mu_N$):** $^{17}$O $-1.913$ (measured $-1.894$); $^{17}$F $+4.793$ ($+4.722$); $^{15}$N $-0.264$ ($-0.283$); $^{15}$O $+0.638$ ($+0.719$); $^{41}$Ca $-1.913$ ($-1.595$); $^{207}$Pb $+0.638$ ($+0.592$). The measured values lie between the two Schmidt lines and are systematically *smaller in magnitude* for $g_s$: explain with core polarization, meson-exchange currents and the effective $g_s\approx0.7g_s^{\rm free}$.
4. **Evidence for shells:** list three independent observables (separation energies, abundances, $E(2^+)$ and $B(E2)$) and sketch each versus $N$ across $N=28,50,82$.
5. **Spin-orbit magnitude:** the nuclear spin-orbit splitting of $1p_{3/2}$-$1p_{1/2}$ in $^{15}$N/$^{15}$O is $\approx6$ MeV, far larger than the atomic Thomas value would give; write "explained in Module 21" beside it.
6. **Why $\mathbf l\cdot\mathbf s$ must be negative:** if $j=\ell-\tfrac12$ were lower the magic numbers would not appear; check with $N=28$.
7. **Counting check:** the number of states in $1f_{7/2}$ is $2j+1=8$: $20+8=28$.
8. **Oscillator constants:** $\hbar\omega=41A^{-1/3}$ MeV gives $\approx7.2$ MeV for $^{208}$Pb and $\approx16$ MeV for $^{16}$O; compare with the spacing between major shells.
9. **Independent-particle puzzle:** state the mean free path of a nucleon in nuclear matter versus nuclear size and why independent-particle motion is a surprise given the hard core (Pauli blocking, Module 18).
10. **Month-3 gate prep:** write the level scheme from memory and predict $J^\pi$ for four odd-$A$ nuclei.

## Optional extension

Solve the radial Schrödinger equation numerically in a Woods-Saxon plus spin-orbit potential for $A=40$ and $A=208$ and plot the level scheme against the empirical one.

## Pitfalls

- Getting the sign of the spin-orbit splitting backwards.
- Using the Schmidt line for configurations with mixed seniority.
- Forgetting holes: $J^\pi$ of a one-hole state equals that of the hole orbital.

## Gate questions

1. Why does an independent-particle model work despite a hard-core interaction?
2. Which three observables show the magic numbers?
3. Why does the empirical spin-orbit strength seem anomalous?

## One-page cheat sheet contents

Level scheme with cumulative numbers; spin-orbit sign; Schmidt formulas and values; evidence for shells.
