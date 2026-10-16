# Module 11: Many particles, residual interactions and pairing (★, Week 10)

**Books:** Krane chapter 5 section 4 onward; Walecka's many-particle shell-model treatment; Suhonen if you want more scaffolding.
**Time:** 1 week.

## Why this matters

The most important piece of the residual interaction, for you, is **pairing**. The $\delta$-force in $j^2$ binds $J=0$ anomalously; hence all even-even ground states are $0^+$; hence $\Delta\approx\frac{12}{\sqrt A}$ MeV in the mass formula; hence **the crust is made of even-$Z$, even-$N$ nuclei.** You put that term in by hand in Module 04; this week derives it.

## Skip-test (40 minutes, no notes)

1. For two identical nucleons in a $j$-shell with a $\delta$-interaction, show the $J=0$ state is anomalously bound compared with $J\ge2$.
2. Extract the pairing gap from odd-even mass differences using three consecutive isotopes.
3. Show a $j^n$ configuration with $n$ even has a $0^+$ ground state under a pairing force.
4. State the crust consequence of the pairing term.
5. Define seniority and state its relation to the pairing gap in the spectrum.

## Prerequisites

Modules 04 and 10.

## Detailed topics (checklist)

**Residual interaction [Must]**
- The shell model $H=\sum\epsilon_ia^\dagger_ia_i+\tfrac12\sum V_{ijkl}a^\dagger_ia^\dagger_ja_la_k$; the residual interaction as the part of the NN force not absorbed in the mean field; configuration mixing; two-particle matrix elements $\langle j^2J|V|j^2J\rangle$.
- $\delta$-force $V=-V_0\delta(\mathbf r_1-\mathbf r_2)$ in a $j^2$ shell with $T=1$: $E_J\propto-V_0F_R(2j+1)^2\begin{pmatrix}j&j&J\\\tfrac12&-\tfrac12&0\end{pmatrix}^2$ for even $J$ (zero for odd $J$); the $J=0$ state is lowered by an amount proportional to $(2j+1)$, while $J\ge2$ shifts are $O(1)$.

**Pairing [Must]**
- Pair-creation operator $P^\dagger=\sum_{m>0}(-1)^{j-m}a^\dagger_{jm}a^\dagger_{j,-m}$; the pairing Hamiltonian $H=-GP^\dagger P$; $j^n$ ground state with seniority $v=0$ and $E_0(n)=-\frac G4n(2\Omega-n+2)$, $\Omega=\frac{2j+1}2$; the gap between the $0^+$ ground state and the first state with a broken pair ($v=2$) is the pairing gap.
- **Odd-even staggering:** $\Delta^{(3)}(N)=\frac{(-1)^N}{2}\left[B(N+1)-2B(N)+B(N-1)\right]\approx\frac{12}{\sqrt A}$ MeV; this is the SEMF pairing term.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Krane 5.4: configuration mixing; the $\delta$-force |
| Session 2 | The pairing Hamiltonian and seniority; exercises 1 and 3 |
| Session 3 | Odd-even mass differences from AME2020; exercises 2 and 5 |
| Session 4 | The crust consequence; exercises 4 and 6 to 10 |

## Derive from scratch

1. $E_J$ for two nucleons with a $\delta$-force (using the 3j symbols).
2. $E_0(n)$ for the pairing Hamiltonian in one $j$-shell.
3. The three-point odd-even formula.
4. The link between $\Delta$ and the SEMF term.
5. The seniority-zero ground state.

## Bare-minimum exercises (with expected results)

1. **$\delta$-force in $j^2$:** compute $E(J)$ for $(1f_{7/2})^2$ with a $\delta$-interaction; $J=0$ is lowered far below $J=2,4,6$; **show the ratio** and explain how this generates $\Delta$.
2. **Gap from masses:** use the three-point formula on tin ($A\approx118$) and lead ($A\approx208$) isotopes from AME2020: expect $\Delta\approx1.1$ to $1.4$ MeV for tin and $\approx0.8$ to $1.0$ MeV for lead, compared with $\frac{12}{\sqrt A}=1.10$ and $0.83$ MeV.
3. **Seniority zero:** show that for $n$ even the lowest state is $v=0$ and $0^+$ with $E_0=-\frac G4n(2\Omega-n+2)$; for $n=2$ it reduces to $-G\Omega$; check against the two-particle $\delta$-force result.
4. **Crust consequence:** the even-even term adds $\delta=+\frac{12}{\sqrt A}$ ($\approx1.6$ MeV at $A=56$, $1.1$ MeV at $A=118$) to $B$; odd-odd nuclei are never in the lowest $g$ of cold catalysed matter and odd-$A$ appear only as transients.
5. **Odd-even staggering and drip:** $S_n$ is larger for even $N$ by about $2\Delta$, producing the sawtooth in $S_n(N)$; drip occurs first at an even-$N$ nucleus *boundary* (the last bound even-$N$ nucleus).
6. **Excitation gap:** the first excited state of an even-even nucleus away from collective regions sits at about $2\Delta\approx2$ to $3$ MeV (breaking a pair); contrast with the low collective $2^+$ (Module 12).
7. **Why $0^+$:** explain in words why a short-range attractive force prefers $J=0$ pairs (maximum spatial overlap of $m,-m$ orbits).
8. **Counting states:** the number of $J=0$ pairs in $j=\tfrac{7}{2}$ is $\Omega=4$; the maximum pair number and the pairing energy scaling $-G\Omega$ per pair.
9. **Pairing in the SEMF:** write $\delta=\frac{a_P}{\sqrt A}$ with $a_P\approx12$ MeV and compute the even-even, odd-$A$, odd-odd values at $A=56$ ($+1.6,0,-1.6$).
10. **Month-3 gate prep:** write the $\delta$-force argument and the crust consequence in five lines.

## Optional extension

Solve the BCS gap equation $\Delta=\frac G2\sum_k\frac{\Delta}{\sqrt{(\epsilon_k-\lambda)^2+\Delta^2}}$ for a single level of degeneracy $\Omega$ and compare with the exact $-G\Omega$ result for small $\Omega$ (where BCS fails).

## Pitfalls

- Applying the pairing-force result to nucleons of different species (isospin $T=1$ requires identical-like pairing; $np$ pairing is a separate subject).
- Using $\Delta=12/\sqrt A$ for deformed nuclei with collective effects.
- Confusing the pairing gap with the first excitation energy.

## Gate questions

1. Why does a short-range force bind $J=0$ pairs so strongly?
2. Why is the crust even-$Z$, even-$N$?
3. How does odd-even staggering measure $\Delta$?

## One-page cheat sheet contents

$\delta$-force $E_J$ structure; seniority-zero energy; three-point formula; SEMF pairing term; crust consequence.
