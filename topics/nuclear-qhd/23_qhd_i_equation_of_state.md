# Module 23: The QHD-I equation of state (★, Week 22)

**Books:** Walecka's QHD-I chapter and the applications chapter; Serot and Walecka section 3.
**Time:** 1 week.

## Why this matters

$$\varepsilon=\frac{g_v^2}{2m_v^2}n_B^2+\frac{m_s^2}{2g_s^2}(M-M^*)^2+\frac{\gamma}{(2\pi)^3}\int^{k_F}\sqrt{k^2+M^{*2}}\,d^3k,$$
$$P=\frac{g_v^2}{2m_v^2}n_B^2-\frac{m_s^2}{2g_s^2}(M-M^*)^2+\frac13\frac{\gamma}{(2\pi)^3}\int^{k_F}\frac{k^2}{\sqrt{k^2+M^{*2}}}d^3k.$$
Only two combinations survive: $C_s^2=\frac{g_s^2M^2}{m_s^2}\simeq267.1$ and $C_v^2=\frac{g_v^2M^2}{m_v^2}\simeq195.9$, fitted to $n_0$ and $B_0$. Everything else is a **prediction**.

**Be honest about the predictions.** $K\approx545$ MeV, more than double the empirical value; $M^*/M\approx0.56$, too small. **A model that derives saturation from first principles and then overshoots $K$ by a factor of two is a far more interesting object than one that fits everything**: Module 24 is about what fixing it costs. Meanwhile $\varepsilon\to P$ as $n_B\to\infty$: causal by construction.

## Skip-test (40 minutes, no notes)

1. Derive $\varepsilon$ and $P$ from the energy-momentum tensor of the mean-field Lagrangian: build $T^{\mu\nu}$ from the Lagrangian directly.
2. Verify $P=n_B^2\frac{d}{dn_B}\left(\frac\varepsilon{n_B}\right)$ analytically using the self-consistency condition; note exactly where self-consistency enters.
3. Compute $K$ and $M^*$ at saturation and compare with experiment; diagnose the failure.
4. Compute $v_s^2=\frac{dP}{d\varepsilon}$ and show $v_s<c$ everywhere and $\to c$ asymptotically.
5. State which two parameters fix the model.

## Prerequisites

Module 22; the stress-energy tensor (mechanics guide Module 18).

## Detailed topics (checklist)

**Energy-momentum tensor [Must]**
- **Self-contained step:** construct $T^{\mu\nu}=\sum_i\frac{\partial\mathcal L}{\partial(\partial_\mu\varphi_i)}\partial^\nu\varphi_i-\eta^{\mu\nu}\mathcal L$ from the Lagrangian directly, then read off $\varepsilon=\langle T^{00}\rangle$ and $P=\frac13\langle T^{ii}\rangle$ (budget an extra hour if Noether's theorem is cold).
- In mean field the meson kinetic terms vanish (uniform fields); $\varepsilon$ and $P$ as above; **thermodynamic consistency:** $P=n_B^2\frac{d(\varepsilon/n_B)}{dn_B}$ requires $\frac{\partial\varepsilon}{\partial M^*}=0$ at fixed $n_B$: *that is the self-consistency equation*.

**Predictions and failures [Must]**
- Saturation at $k_F=1.42$ fm$^{-1}$ ($n_0=0.193$ fm$^{-3}$) with $E/A=-15.75$ MeV by construction; predictions: $K=546$ MeV, $\frac{M^*}{M}=0.56$, symmetry energy too small and no isospin structure (Module 24).
- Causality: $v_s^2\to1$ from below as $n_B\to\infty$.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Walecka QHD-I chapter: $\varepsilon$ and $P$; exercise 1 |
| Session 2 | The $T^{\mu\nu}$ construction; consistency; exercises 2 and 3 |
| Session 3 | The predictions; exercises 4 to 6 |
| Session 4 | Causality; exercises 7 to 10 |

## Derive from scratch

1. $T^{\mu\nu}$ for the mean-field Lagrangian.
2. $\varepsilon$ and $P$.
3. $P=n^2d(\varepsilon/n)/dn$ with the self-consistency condition.
4. $K$ from the second derivative of $\varepsilon/n_B$.
5. The causal limit.

## Bare-minimum exercises (with expected results)

1. **$\varepsilon$ and $P$ from $T^{\mu\nu}$:** for uniform fields $\mathcal L=\bar\psi[\ldots]\psi-\tfrac12m_s^2\phi_0^2+\tfrac12m_v^2V_0^2$; $T^{00}=\varepsilon$, $T^{ii}/3=P$; reproduce the two formulas above (the nucleons contribute the Fermi-gas integrals with $M^*$; the fields contribute $\pm\frac{m_s^2\phi_0^2}{2}$ and $+\frac{m_v^2V_0^2}{2}$).
2. **Consistency:** show $\frac{\partial}{\partial M^*}\left[\frac{\varepsilon}{n_B}\right]=0$ reproduces $M^*=M-\frac{g_s^2}{m_s^2}n_s$ (this is where self-consistency enters), and then $n_B^2\frac{d(\varepsilon/n_B)}{dn_B}=P$.
3. **Saturation point and $K$:** minimising $\frac{\varepsilon}{n_B}$ gives $\frac\varepsilon{n_B}=923.5$ MeV at $n_B=0.193$ fm$^{-3}$ ($E/A=-15.75$ MeV, $P=0$); numerically $K=9n_0^2\frac{d^2(E/A)}{dn^2}=546$ MeV against the empirical $230\pm30$ MeV: a factor $\sim2.4$ too stiff; $M^*/M=0.56$ (empirical estimates $\sim0.6$ to $0.8$) too small.
4. **Table:** at $n_B=0.193,0.4,0.8,1.6,3.2$ fm$^{-3}$: $P=0,66,494,2252,9141$ MeV/fm$^3$ and $v_s^2=0.07,0.55,0.80,0.88,0.92$: always below $1$ and rising towards $1$.
5. **Causal limit:** as $M^*\to0$ the nucleons are ultra-relativistic and the vector field dominates: $\varepsilon\to\frac{C_v^2}{2M^2}n_B^2$, $P\to\varepsilon$ (a stiff fluid), $v_s\to1^-$; verify numerically that $\frac{dP}{d\varepsilon}$ stays below $1$ and approaches it (0.92 at $n_B=3.2$ fm$^{-3}$).
6. **Diagnosis in two paragraphs:** the incompressibility is large because the vector repulsion $\propto n_B^2$ is steep while the scalar attraction saturates; reducing $K$ requires softening the scalar sector at $n_0$ (nonlinear self-interactions, Module 24).
7. **Parameters:** $g_s^2/4\pi=7.29$, $g_v^2/4\pi=10.83$ for $m_s=550$, $m_v=783$ MeV reproduce $C_s^2$, $C_v^2$; vary $m_s$ and show $C_s^2$ and $C_v^2$ are unchanged.
8. **Neutron matter:** with the isoscalar-only model (no $\rho$) the EOS of pure neutron matter is symmetric matter with a changed $\gamma$ and extra Fermi energy: check the kinetic symmetry energy is $\frac{k_F^2}{6E_F^*}\approx22$ MeV at saturation (with $E_F^*=\sqrt{k_F^2+M^{*2}}$), too small against $J\approx32$ MeV (preview of Module 24).
9. **Relation to Skyrme:** list three qualitative contrasts with the Module 13 Skyrme functional (relativistic kinetic term, field-mediated forces, causal asymptotics).
10. **Gate prep:** state the five items of the Month-5 gate that this module covers (items 3 and 4).

## Optional extension

Compute the nuclear-matter EOS with $m_s=550$ and an independent fit to $k_F=1.30$ fm$^{-1}$ (the empirical density) and see how $K$ and $M^*$ change: the failures are robust.

## Pitfalls

- Forgetting the $\pm\frac{(M-M^*)^2}{\ldots}$ field terms in $P$ and $\varepsilon$ (their sign differs).
- Using the free Fermi-gas $P$ with $M$ instead of $M^*$.
- Quoting the nuclear-matter parameters without stating which of $n_0$ and $k_F$ was fitted.

## Gate questions

1. Where does self-consistency enter the thermodynamic identity?
2. Why is $K$ too large in QHD-I?
3. Why is the EOS causal by construction?

## One-page cheat sheet contents

$\varepsilon$, $P$ formulas; $C_s^2$, $C_v^2$; the predictions ($K$, $M^*/M$); the $T^{\mu\nu}$ construction; the table of $P$ and $v_s^2$.
