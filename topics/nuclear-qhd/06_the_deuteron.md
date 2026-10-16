# Module 06: The deuteron (Week 5)

**Books:** Krane chapter 4 sections 1 to 3; Wong's deuteron sections; **Walecka chapter 1** (first serious pass).
**Time:** 1 week.

## Why this matters

The deuteron is the entire nucleon-nucleon interaction compressed into one bound state. Each observable forces a property of the force:

| Datum | What it forces |
| --- | --- |
| $B=2.2245$ MeV, barely bound | Strong but short-ranged; barely over the Module 01 threshold |
| $J^\pi=1^+$, $S=1$, $T=0$ | Spin dependence: stronger in the triplet channel |
| No excited state | No $^1S_0$ bound state (it is a virtual state, Module 07) |
| $Q=+0.286$ fm$^2\neq0$ | **$L$ is not a good quantum number** $\Rightarrow$ **tensor force** $\Rightarrow$ about 4 to 6 percent D-state |
| $\mu_d\neq\mu_p+\mu_n$ ($0.8574$ vs $0.8798\ \mu_N$) | The same conclusion, independently |

## Skip-test (40 minutes, no notes)

1. For a square well of radius $R=2.1$ fm find $V_0$ giving $B=2.22$ MeV and the probability of finding the nucleons outside the well.
2. Show $S_{12}=3(\boldsymbol\sigma_1\cdot\hat r)(\boldsymbol\sigma_2\cdot\hat r)-\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2$ commutes with $\mathbf J$ but not with $\mathbf L$, hence mixes $^3S_1$ and $^3D_1$.
3. Estimate the D-state probability from $\mu_d$ and from $Q$.
4. Explain why the deuteron has $T=0$ and no $^1S_0$ partner.
5. State the asymptotic form of the wavefunction $u(r)\to e^{-\gamma r}$ with $\gamma=\frac{\sqrt{MB}}{\hbar c}$ and compute $\gamma$.

## Prerequisites

Modules 01 and 02.

## Detailed topics (checklist)

**Facts and quantum numbers [Must]**
- $B=2.2245$ MeV, $\gamma=\frac{\sqrt{MB}}{\hbar c}=0.2316$ fm$^{-1}$ ($1/\gamma=4.32$ fm), $J^\pi=1^+$, $S=1$, $T=0$, even parity so $L=0,2$; magnetic moment $\mu_d=0.8574\ \mu_N$, quadrupole moment $Q=0.286$ fm$^2$; rms matter radius $\approx2.1$ fm; no excited bound state.

**The central-force model [Must]**
- Radial equation $u''+\frac{M}{\hbar^2}(E-V)u=0$ with $E=-B$; inside $u=\sin kr$, outside $u=Ce^{-\gamma r}$; matching: $k\cot kR=-\gamma$; the wavefunction extends mostly outside the well, so any potential fitted to $B$ alone is poorly constrained in shape.

**The tensor force [Must]**
- $S_{12}$ commutes with $\mathbf J$ and $S$ but not $\mathbf L$; $\langle{}^3S_1|S_{12}|{}^3S_1\rangle=0$ and $\langle{}^3D_1|S_{12}|{}^3S_1\rangle=\sqrt8$; the D-state admixture from $\mu_d=\mu_p+\mu_n-\tfrac32(\mu_p+\mu_n-\tfrac12)P_D$ and from $Q$.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Krane 4.1 to 4.3: the facts; exercises 1 and 5 |
| Session 2 | Wong: the deuteron; the tensor operator; exercise 2 |
| Session 3 | Walecka chapter 1, first pass; exercises 3 and 4 |
| Session 4 | Exercises 6 to 10 |

## Derive from scratch

1. The square-well matching condition and the bound-state spectrum.
2. $[S_{12},\mathbf J]=0$ and $[S_{12},\mathbf L]\neq0$.
3. The D-state probability from $\mu_d$.
4. The asymptotic form and $\gamma$.
5. The antisymmetry argument for $T=0$.

## Bare-minimum exercises (with expected results)

1. **Square-well deuteron:** with $R=2.1$ fm the matching $k\cot kR=-\gamma$ gives $kR=1.830$, $k=0.872$ fm$^{-1}$ and $V_0=\frac{\hbar^2k^2}{M}+B\approx33.7$ MeV; the probability of being outside the well is $\approx63$ percent, so the wavefunction is mostly outside.
2. **$S_{12}$:** show $[S_{12},J_i]=0$, $[S_{12},L_i]\neq0$ (use $S_{12}=2\left[3(\mathbf S\cdot\hat r)^2-\mathbf S^2\right]$ for $S=1$) and $S_{12}^2=6+2\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2-2S_{12}$.
3. **D-state from $\mu_d$:** $P_D=\frac{\mu_p+\mu_n-\mu_d}{\frac32(\mu_p+\mu_n-\frac12)}=\frac{0.8798-0.8574}{1.5\times0.3798}\approx3.9$ percent.
4. **D-state from $Q$:** the quadrupole moment is $Q\propto\frac{1}{\sqrt{50}}\int uw\,r^2dr-\frac1{20}\int w^2r^2dr$ (S-D interference minus D-D); with a deuteron D/S asymptotic ratio $\eta\approx0.0256$ it requires $P_D\approx4$ to $6$ percent (the two estimates agree within the model dependence).
5. **Asymptotics:** $\gamma=0.2316$ fm$^{-1}$; the zero-range estimate $B\approx\frac{\hbar^2}{Ma_t^2}\approx1.4$ MeV for $a_t=5.42$ fm differs from $2.22$ MeV because of the effective range (Module 07).
6. **No $^1S_0$ bound state:** the singlet channel is attractive but slightly too weak ($a_s=-23.7$ fm, a virtual state); the singlet-triplet difference is a spin-dependent force.
7. **Isospin:** $T=0$ follows from $S=1$, $L=0,2$ and antisymmetry; the "other" $S=1$, $T=1$ system ($nn$, $pp$ in $^3P_J$) is unbound.
8. **Size:** the rms radius $\approx2.1$ fm versus $1/\gamma=4.3$ fm: the deuteron is a loosely bound system whose wavefunction extends beyond the force range.
9. **Tensor force sign:** the pion-exchange tensor force (Module 08) makes the $S=1$, $T=0$, $J=1$ channel attractive when the spins are aligned along $\hat r$; state why this lowers the energy of the deuteron relative to a pure central force.
10. **Observables table:** write the table of observables above and, beside each, the property of $V_{NN}$ it forces; end at "a tensor force must exist."

## Optional extension

Solve the coupled $^3S_1$-$^3D_1$ equations numerically for a Yukawa-plus-tensor potential and fit $B$, $Q$ and $P_D$; observe how $Q$ constrains the tensor strength.

## Pitfalls

- Assuming the wavefunction is confined to the well.
- Estimating $P_D$ from $\mu_d$ and $Q$ and expecting exact agreement (the two use different operators).
- Forgetting that $^3S_1$ and $^3D_1$ share $J^\pi=1^+$.

## Gate questions

1. Why does $Q\ne0$ force a tensor force?
2. Why does $\mu_d\ne\mu_p+\mu_n$ say the same thing independently?
3. Why can the deuteron have no $^1S_0$ partner?

## One-page cheat sheet contents

Deuteron facts; $\gamma$; square-well matching and $V_0$; $S_{12}$ properties; D-state formulas.
