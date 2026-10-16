# Module 15: Part Two c, cross sections and decay rates (Week 23; Protocol B)

**Books:** Klauber Part Two (cross-section chapter); second sources: Schwartz chapter 5, Tong's QED lecture, Lancaster and Blundell.
**Time:** 1 week.

## Why this matters

**One complete calculation end to end to a number**: Compton or $e^+e^-\to\mu^+\mu^-$, every trace. The only genuine link between formalism and experiment before Phase 2.

## Diagnostic (40 minutes, no notes)

1. Write the cross-section formula in terms of $|\mathcal M|^2$, the flux factor and two-body phase space.
2. Compute the spin-summed, spin-averaged $|\mathcal M|^2$ for $e^+e^-\to\mu^+\mu^-$ in the massless limit.
3. Obtain $\frac{d\sigma}{d\Omega}$ and $\sigma_{\rm tot}$ and evaluate at $\sqrt s=10$ GeV.
4. State the two-body decay-rate formula and apply it to a scalar decaying to a fermion pair.
5. State what makes a quantity observable in QFT.

## Prerequisites

Module 14.

## Detailed topics (checklist)

- Cross-section: $d\sigma=\frac{1}{4\sqrt{(p_1\cdot p_2)^2-m_1^2m_2^2}}|\mathcal M|^2d\Phi_n$; two-body phase space $\int d\Phi_2=\frac{|\mathbf p|}{4\pi\sqrt s}$ (angular integral), $d\Phi_2=\frac{|\mathbf p|}{16\pi^2\sqrt s}d\Omega$; in the CM frame $\frac{d\sigma}{d\Omega}=\frac{|\mathcal M|^2}{64\pi^2s}\frac{|\mathbf p_f|}{|\mathbf p_i|}$; decay rate $\Gamma=\frac{1}{2M}\int|\mathcal M|^2d\Phi_n$, two-body: $\Gamma=\frac{|\mathbf p|}{8\pi M^2}|\mathcal M|^2$ for a distinguishable final state.
- Spin sums and traces: $\sum|\mathcal M|^2$ via $\sum u\bar u=p\!\!\!/+m$ and trace identities; for $e^+e^-\to\mu^+\mu^-$ (massless): $\frac14\sum|\mathcal M|^2=2e^4\frac{t^2+u^2}{s^2}=e^4(1+\cos^2\theta)$.
- Observability: only amplitudes squared, summed over unobserved and averaged over unmeasured quantum numbers, are observables; the S-matrix element is the bridge.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Prose pass; the three questions; the cross-section and flux |
| A2 | The $e^+e^-\to\mu^+\mu^-$ amplitude and traces; exercises 1 to 4 |
| A3 | Decay rates; the R ratio; exercises 5 to 8; the [C] items |

## Derive from scratch (this module's calculation is required)

The complete $e^+e^-\to\mu^+\mu^-$ calculation: amplitude, spin sums, traces, angular distribution, total cross-section and the number.

## Exercises

1. **[T] The amplitude:** $i\mathcal M=\frac{ie^2}{s}\left[\bar v(p_2)\gamma^\mu u(p_1)\right]\left[\bar u(p_3)\gamma_\mu v(p_4)\right]$ (up to the overall sign convention); only the $s$-channel exists at tree level.
2. **[T] Traces:** $\sum_{\rm spins}|\mathcal M|^2=\frac{e^4}{s^2}L^{\mu\nu}M_{\mu\nu}$ with $L^{\mu\nu}=4\left[p_1^\mu p_2^\nu+p_1^\nu p_2^\mu-g^{\mu\nu}p_1\cdot p_2\right]$ and $M_{\mu\nu}=4\left[p_{3\mu}p_{4\nu}+p_{3\nu}p_{4\mu}-g_{\mu\nu}p_3\cdot p_4\right]$ (massless): $L^{\mu\nu}M_{\mu\nu}=32\left[(p_1\cdot p_3)(p_2\cdot p_4)+(p_1\cdot p_4)(p_2\cdot p_3)\right]$; with $p_1\cdot p_3=-\frac t2$, $p_1\cdot p_4=-\frac u2$: $\frac14\sum|\mathcal M|^2=\frac{e^4}{4s^2}\cdot8(t^2+u^2)=2e^4\frac{t^2+u^2}{s^2}$.
3. **[T] Angular distribution:** $t=-\frac s2(1-\cos\theta)$, $u=-\frac s2(1+\cos\theta)$ give $\frac14\sum|\mathcal M|^2=e^4(1+\cos^2\theta)$ and $\frac{d\sigma}{d\Omega}=\frac{\alpha^2}{4s}(1+\cos^2\theta)$.
4. **[T] The number:** $\sigma=\int\frac{d\sigma}{d\Omega}d\Omega=\frac{4\pi\alpha^2}{3s}=\frac{86.9\ {\rm nb}}{s/{\rm GeV}^2}$, i.e. $0.87$ nb at $\sqrt s=10$ GeV (using $1\ {\rm GeV}^{-2}=0.3894$ mb $=3.894\times10^5$ nb and $\alpha=\frac1{137.036}$).
5. **[T] Compton limit:** the low-energy ($\omega\ll m$) limit of the Compton cross-section is the Thomson value $\sigma_T=\frac{8\pi\alpha^2}{3m^2}=0.665$ barn for the electron.
6. **[T] Decay rate:** a scalar $\phi$ of mass $M$ with Yukawa coupling $g\phi\bar\psi\psi$: $\sum|\mathcal M|^2=2g^2M^2\beta^2$, $\Gamma=\frac{g^2M}{8\pi}\beta^3$, $\beta=\sqrt{1-\frac{4m^2}{M^2}}$ (the threshold factor $\beta^3$ is the $p$-wave behaviour of a scalar decaying to a fermion pair).
7. **[T] The R ratio:** $R=\frac{\sigma(e^+e^-\to{\rm hadrons})}{\sigma(e^+e^-\to\mu^+\mu^-)}=N_c\sum_fQ_f^2=2$ ($u,d,s$), $\frac{10}3$ (plus $c$), $\frac{11}3$ (plus $b$): the colour factor 3 is measured.
8. **[T] Helicity structure:** for massless fermions only opposite-helicity $e^-e^+$ annihilate; the $(1+\cos^2\theta)$ comes from the spin-1 virtual photon with $J_z=\pm1$ along the beam.
9. **[C] Observable:** what makes a quantity observable in QFT (gauge invariance, summing over unobserved states, IR safety)?
10. **[C] Explain-it:** from the amplitude to the number, in a paragraph with no equations: what physical question does $\sigma=\frac{4\pi\alpha^2}{3s}$ answer?

## Optional extension

Add the muon mass: $\sigma=\frac{4\pi\alpha^2}{3s}\beta\left(1+\frac{2m^2}{s}\right)$ with $\beta=\sqrt{1-4m^2/s}$ and show the threshold behaviour.

## Pitfalls

- Missing the $\frac14$ spin average (and the factor of $-1$ in a closed fermion trace).
- Wrong flux factor for massive initial states.
- Forgetting the $\frac12$ for identical final-state particles.

## Gate questions

1. Why is the cross-section $\propto\frac{1}{s}$?
2. Where does $(1+\cos^2\theta)$ come from?
3. What does the R ratio measure?

## One-page cheat sheet contents

Cross-section and decay formulas; the $e^+e^-\to\mu^+\mu^-$ result; the $R$ ratio; Thomson limit.
