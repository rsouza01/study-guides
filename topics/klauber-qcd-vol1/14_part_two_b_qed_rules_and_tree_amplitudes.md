# Module 14: Part Two b, the QED interaction, the Feynman rules and tree amplitudes (Weeks 21 and 22; Protocol B)

**Books:** Klauber Part Two (QED interaction and tree-level chapters); second sources: Lancaster and Blundell, Tong (QED lectures), Schwartz chapters 4 to 5.
**Time:** 2 weeks.

## Why this matters

**Derive the rules from the S-matrix expansion, in full**: rules quoted rather than derived is the classic hollow spot. Then use them: tree-level amplitudes from scratch, and the conceptual question of what an internal (off-shell) line is.

## Diagnostic (40 minutes, no notes)

1. Derive the QED vertex $-ie\gamma^\mu$ and the three propagators from the second-order S-matrix term.
2. Write the Feynman rules in momentum space (external lines, vertex, propagators, loops).
3. Write the amplitude for $e^-\mu^-\to e^-\mu^-$ at tree level.
4. Write the two tree-level Compton diagrams.
5. Evaluate the Mandelstam sum rule for equal-mass $2\to2$ scattering.

## Prerequisites

Modules 10, 11 and 13.

## Detailed topics (checklist)

**Week 21: QED and the Feynman rules [Must]**
- $\mathcal L_{\rm QED}=\bar\psi(i\partial\!\!\!/-m)\psi-\tfrac14F^2-e\bar\psi\gamma^\mu\psi A_\mu$; the interaction is **minimal coupling** (Module 12: forced by local U(1)). *Counterfactual:* is minimal coupling derived, guessed, or forced?
- From $S^{(n)}$ with Wick's theorem to the rules (momentum space): vertex $-ie\gamma^\mu$; fermion propagator $\frac{i(p\!\!\!/+m)}{p^2-m^2+i\epsilon}$; photon propagator $\frac{-ig_{\mu\nu}}{k^2+i\epsilon}$; external lines $u(p,s)$, $\bar u(p',s')$, $v$, $\bar v$, $\epsilon_\mu(k,\lambda)$, $\epsilon^*_\mu$; momentum conservation at each vertex; $\int\frac{d^4k}{(2\pi)^4}$ for each loop; a factor $(-1)$ for each closed fermion loop and for relative fermion permutations.

**Week 22: tree-level amplitudes [Must]**
- Mandelstam variables $s=(p_1+p_2)^2$, $t=(p_1-p_3)^2$, $u=(p_1-p_4)^2$ with $s+t+u=\sum m_i^2$; amplitudes $i\mathcal M$.
- *Counterfactual:* internal lines are off-shell: what is off-shell-ness physically?

## Reading plan

| Week | Task |
| --- | --- |
| 21 | Prose pass; the three questions; derive the rules; exercises 1 to 3 |
| 22 | Tree-level amplitudes; counterfactual; exercises 4 to 8; the [C] items |

## Derive from scratch (this module's derivation is required, not triggered)

1. The Feynman rules from the S-matrix expansion.
2. The $e^-\mu^-\to e^-\mu^-$ tree amplitude.
3. The Compton amplitude with both diagrams.

## Exercises

1. **[T] Rules from the S-matrix:** the first-order term $-ie\int d^4x\,:\bar\psi\gamma^\mu\psi A_\mu:$ between plane-wave states gives $-ie\,\bar u(p')\gamma^\mu u(p)\,\epsilon_\mu\,(2\pi)^4\delta^4(p'-p-k)$: vertex $-ie\gamma^\mu$ and an overall momentum-conserving delta.
2. **[T] $e^-\mu^-\to e^-\mu^-$:** $i\mathcal M=(-ie)^2\left[\bar u(p_1')\gamma^\mu u(p_1)\right]\frac{-ig_{\mu\nu}}{q^2}\left[\bar u(p_2')\gamma^\nu u(p_2)\right]$, $q=p_1-p_1'$; i.e. $\mathcal M=\frac{e^2}{q^2}\left[\bar u\gamma^\mu u\right]\left[\bar u\gamma_\mu u\right]$.
3. **[T] Non-relativistic limit:** $\bar u(p')\gamma^0u(p)\to2m$ and the spatial components are suppressed, so with $q^2=-|\mathbf q|^2$: $\mathcal M\to\frac{e^2}{q^2}(2m_1)(2m_2)=-4m_1m_2\frac{e^2}{|\mathbf q|^2}$; comparing with the Born amplitude $\mathcal M=-4m_1m_2\tilde V(\mathbf q)$ gives $\tilde V(\mathbf q)=\frac{e^2}{|\mathbf q|^2}$, i.e. $V(r)=\frac{\alpha}{r}$ (repulsive for like charges).
4. **[T] Compton scattering:** $i\mathcal M=-ie^2\epsilon^*_\nu(k')\epsilon_\mu(k)\,\bar u(p')\left[\frac{\gamma^\nu(p\!\!\!/+k\!\!\!/+m)\gamma^\mu}{(p+k)^2-m^2}+\frac{\gamma^\mu(p\!\!\!/-k\!\!\!/'+m)\gamma^\nu}{(p-k')^2-m^2}\right]u(p)$ (two diagrams, $s$-channel and $u$-channel); Ward identity: replacing $\epsilon\to k$ gives zero.
5. **[T] Mandelstam sum:** for equal masses $s+t+u=4m^2$; in the CM frame $t=-2p^2(1-\cos\theta)$ and $u=-2p^2(1+\cos\theta)$ for elastic scattering with $|\mathbf p|$ the CM momentum.
6. **[T] Propagator denominators:** in the $s$-channel Compton diagram $(p+k)^2-m^2=2p\cdot k=s-m^2$ ($k^2=0$) and in the $u$-channel $(p-k')^2-m^2=-2p\cdot k'=u-m^2$: finite away from threshold.
7. **[T] Pair annihilation $e^+e^-\to\gamma\gamma$:** crossing of Compton: same amplitude with $p\to-p$ for the positron; write the two diagrams.
8. **[T] Counting couplings:** a tree-level $2\to2$ QED amplitude is $O(e^2)$; $2\to n$ is $O(e^n)$; a loop adds $e^2$.
9. **[C] Minimal coupling:** is minimal coupling derived, guessed, or forced? What additional choices could be added (Pauli term) and why are they excluded here?
10. **[C] Two charges repel:** explain to a classical physicist why two charges repel, in QFT terms, **without letting "they exchange a photon" do the work**.

## Optional extension

Compute $\mathrm{tr}$ over spins of $|\mathcal M|^2$ for $e^-\mu^-\to e^-\mu^-$ in the massless limit and obtain $\frac{1}{4}\sum|\mathcal M|^2=2e^4\frac{s^2+u^2}{t^2}$ (the standard result; Module 15 does one such calculation to a number).

## Pitfalls

- Quoting the rules without deriving the vertex factor and propagator numerators.
- Dropping the fermion-ordering sign.
- Treating internal lines as on-shell.

## Gate questions

1. Why does $-ie\gamma^\mu$ appear at the vertex?
2. What makes a line off-shell, physically?
3. Why do the two Compton diagrams need to be added?

## One-page cheat sheet contents

The Feynman rules; the two tree amplitudes; Mandelstam variables; the Ward identity.
