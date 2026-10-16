# Module 13: Part Two a, the interaction picture, the Dyson series and Wick's theorem (Weeks 19 and 20; Protocol B)

**Books:** Klauber Part Two (interaction-picture, S-matrix and Wick chapters); second source: Lancaster and Blundell, Tong's perturbation-theory lecture, Schwartz chapters 4 and 7 (the "Part Two gate" second source). If you ran the Zettili guide, its Module 09 (time-dependent perturbation theory) is a rehearsal.
**Time:** 2 weeks. **Six weeks for Part Two in total** (Modules 13 to 16). The bet is that with the machinery owned these chapters cost less than they did the first time.

## Protocol B steps (per chapter)

(1) Prose-only pass (45 min); (2) the three questions, written, no equations (60 to 90 min); (3) counterfactual interrogation (30 min); (4) targeted derivation only if triggered; (5) explain-it (20 min); (6) problems: **[C] first, [T] second** (triage: in Protocol B weeks, if time runs short, drop the [T] and keep the [C]).

## Diagnostic (40 minutes, no notes)

1. Write the interaction picture and the Dyson series for the evolution operator $U(t,t_0)$ to second order.
2. State Wick's theorem for four scalar fields and name the contraction.
3. Count the contractions and find the symmetry factors of the first-order tadpole and the vacuum bubble in $\frac\lambda{4!}\phi^4$.
4. Write the tree-level $2\to2$ amplitude in $\phi^4$ and the cross-section.
5. State what the Dyson series is and is not (convergence).

## Prerequisites

Modules 03 to 12 (especially the Feynman propagator, Module 08).

## Detailed topics (checklist)

**Week 19: interaction picture, S-operator, Dyson expansion [Must]**
- $H=H_0+H_I$; the interaction picture $\phi_I(x)$ evolves with $H_0$ (it is the free field of Part One); $U_I(t,t_0)=T\exp\left[-i\int_{t_0}^td^4x\,\mathcal H_I\right]$; $S=U_I(\infty,-\infty)=T\exp\left[-i\int d^4x\,\mathcal H_I\right]=1+(-i)\int\mathcal H_I+\frac{(-i)^2}{2!}\int\int T\{\mathcal H_I\mathcal H_I\}+\cdots$; the S-matrix element $\langle f|S|i\rangle$ as the amplitude.
- *Counterfactuals:* why an interaction picture; is the Dyson series convergent, and if not why trust it?

**Week 20: Wick's theorem and contractions [Must]**
- $T\{\phi_1\phi_2\}=\,:\!\phi_1\phi_2\!:+\,\langle0|T\{\phi_1\phi_2\}|0\rangle$ with the contraction equal to the Feynman propagator $D_F(x_1-x_2)$; general theorem: $T\{\ldots\}=:\ldots:+\sum$ (all single, double, ... contractions); only fully contracted terms contribute to vacuum matrix elements.
- *Counterfactuals:* what does time-ordering mean physically, not formally?

## Reading plan

| Week | Task |
| --- | --- |
| 19 | Prose pass; three questions; the Dyson series; exercises 1, 2 and the [C] |
| 20 | Wick's theorem; counterfactuals; exercises 3 to 8; the explain-it |

## Derive from scratch (only if triggered)

1. The Dyson series from the interaction-picture evolution equation.
2. Wick's theorem for four fields by induction.
3. The symmetry factors of the tadpole and the vacuum bubble.

## Exercises

1. **[T] Second-order Dyson:** $S^{(2)}=\frac{(-i)^2}{2}\int d^4x\,d^4y\,T\{\mathcal H_I(x)\mathcal H_I(y)\}$; check unitarity at this order: $S^\dagger S=1$ implies $S^{(1)}+S^{(1)\dagger}=0$ and $S^{(2)}+S^{(2)\dagger}=-S^{(1)\dagger}S^{(1)}$ (the optical-theorem structure).
2. **[T] Wick for four fields:** $T\{\phi_1\phi_2\phi_3\phi_4\}=:\phi_1\phi_2\phi_3\phi_4:+$ (6 single contractions times two normal-ordered fields) $+$ (3 double contractions): $D_{12}D_{34}+D_{13}D_{24}+D_{14}D_{23}$.
3. **[T] First-order $2\to2$ in $\phi^4$:** $\langle0|T\{\phi(x_1)\phi(x_2)\phi(x_3)\phi(x_4)\cdot\frac{-i\lambda}{4!}\int d^4z\,\phi^4(z)\}|0\rangle$: $4!$ contractions cancel $\frac1{4!}$: amplitude $-i\lambda\int d^4z\prod_iD_F(x_i-z)$.
4. **[T] Tadpole counting:** for $\frac{-i\lambda}{4!}\int\phi^4$ with external $\phi(x)\phi(y)$: choose which $\phi(z)$ contracts with $\phi(x)$ (4), which with $\phi(y)$ (3), the remaining two contract together (1): $12\times\frac1{4!}=\frac12$ (symmetry factor $\frac12$).
5. **[T] Vacuum bubble:** $\langle0|\phi^4|0\rangle$ connected figure-eight: $3$ contractions $\times\frac1{4!}=\frac18$.
6. **[T] Tree-level cross-section:** $i\mathcal M=-i\lambda$, so $\mathcal M=-\lambda$; for identical particles in the CM frame $\frac{d\sigma}{d\Omega}=\frac{|\mathcal M|^2}{64\pi^2s}$ and $\sigma_{\rm tot}=\frac{\lambda^2}{32\pi s}$ (including $\frac12$ for identical final-state particles).
7. **[T] QED interaction:** $\mathcal H_I=e\bar\psi\gamma^\mu\psi A_\mu$ (sign convention-dependent); the first-order S-matrix term $-ie\int d^4x\,\bar\psi\gamma^\mu\psi A_\mu$; list the three fields to be contracted in a Compton-scattering second-order term.
8. **[T] Normal ordering:** $T\{\phi(x)\phi(y)\}$ versus $:\phi(x)\phi(y):$: their difference is $D_F(x-y)$ (a c-number).
9. **[C] Perturbation theory in a coupling that is not always small:** what does that cost, and where does it fail (non-perturbative effects, asymptotic series)?
10. **[C] What is a Feynman diagram?** A picture of a process, a mnemonic for a term, or something else? Defend your answer.

## Optional extension

Prove Wick's theorem for fermions with the extra signs from anticommutation and state how a closed fermion loop acquires $-1$.

## Pitfalls

- Treating the Dyson series as convergent.
- Mixing the interaction-picture field with the Heisenberg field.
- Mis-counting symmetry factors (derive from contractions, not from diagram symmetry rules alone).

## Gate questions

1. Why does the contraction equal the Feynman propagator?
2. Why does time-ordering appear in $S$?
3. What is the symmetry factor, counted from contractions?

## One-page cheat sheet contents

Dyson series; Wick's theorem; the counting examples ($\frac12$, $\frac18$); tree-level $\phi^4$ amplitude.
