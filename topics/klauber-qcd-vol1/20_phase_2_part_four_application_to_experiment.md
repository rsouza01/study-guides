# Module 20: Phase 2, Part Four, application to experiment (about 6 weeks from Week 30; new material)

**Books:** Klauber Part Four; second sources: Schwartz (the anomalous magnetic moment and Lamb-shift chapters), Peskin and Schroeder chapter 6 for the vertex correction, Tong's QED lecture.
**Time:** about 6 weeks at full hours (after your primary track), with undivided attention. New material: derive freely, that is what derivations are for. **Protocol A** again, since this is first-pass territory.

## Why this matters

The anomalous magnetic moment (the vertex correction, Schwinger's $\frac{\alpha}{2\pi}$, comparison with measurement). The Lamb shift (which effects contribute, at what order, how they assemble). Then a full session on **what agreement to ten significant figures actually establishes**, about QED and about QFT as a framework.

## Diagnostic (40 minutes, no notes)

1. State the Dirac value of $g$ and the definition of $a=\frac{g-2}2$.
2. State Schwinger's result and evaluate it numerically.
3. Estimate the order of magnitude of the Lamb shift from $\alpha^5m$.
4. List the contributions to the hydrogen $2S_{1/2}$-$2P_{1/2}$ splitting.
5. State the experimental and theoretical status of $a_e$.

## Prerequisites

Phase 1 (Modules 01 to 19), especially Module 18 (vacuum polarization).

## Detailed topics (checklist)

**The anomalous magnetic moment [Must]**
- Vertex $\Gamma^\mu(p',p)=\gamma^\mu F_1(q^2)+\frac{i\sigma^{\mu\nu}q_\nu}{2m}F_2(q^2)$; Dirac $F_2=0$, $g=2$; one-loop vertex correction gives $F_2(0)=\frac{\alpha}{2\pi}$ (Schwinger, 1948), so $a_e=\frac{\alpha}{2\pi}+C_2\left(\frac\alpha\pi\right)^2+\cdots$ with $C_2=-0.328\,479$; the Feynman-parameter integral and the Ward identity ($F_1(0)=1$).

**The Lamb shift [Must]**
- The $2S_{1/2}$-$2P_{1/2}$ degeneracy of the Dirac equation is lifted by radiative effects: electron self-energy (the dominant effect, $\approx1017$ MHz including the Bethe logarithm), vacuum polarization (Uehling; $\approx-27$ MHz), the anomalous magnetic moment (contributes $\approx+68$ MHz); total $\approx1057.8$ MHz. Bethe's non-relativistic estimate: $\Delta E\approx\frac{4\alpha^5m}{3\pi n^3}\left[\ln\frac1{\alpha^2}-\ln k_0+\ldots\right]$ with $\ln k_0\approx2.8$ for $2S$.
- Orders: $\alpha^5m$ (leading), $\alpha^6m$ (two-loop and recoil), etc.

**What ten digits establish [Should]**
- QED as an effective theory is tested at $10^{-10}$ in $a_e$ (and the comparison provides the best determination of $\alpha$); it does *not* test physics above the TeV scale or the foundations of renormalization; the status of the muon $a_\mu$ (hadronic vacuum polarization; check the current literature, as the data-driven and lattice values have been in flux).

## Reading plan

| Week | Task |
| --- | --- |
| 30 | The vertex function; the Schwinger integral; exercises 1 to 3 |
| 31 | Gordon identity; form factors; exercise 4 |
| 32 to 33 | The Lamb shift: orders and contributions; exercises 5 to 7 |
| 34 | Higher orders and measurements; exercise 8 |
| 35 | The conceptual session; exercises 9 and 10 |

## Derive from scratch

1. The one-loop vertex correction and $F_2(0)=\frac\alpha{2\pi}$.
2. The Gordon identity decomposition.
3. Bethe's estimate of the Lamb shift.

## Exercises

1. **[T] Dirac value:** $\boldsymbol\mu=g\frac{e}{2m}\mathbf S$ with $g=2$ from the Dirac equation (the $\sigma^{\mu\nu}$ term with coefficient 1 in $\bar u\gamma^\mu u=\bar u\left[\frac{(p+p')^\mu}{2m}+\frac{i\sigma^{\mu\nu}q_\nu}{2m}\right]u$ by the Gordon identity).
2. **[T] Schwinger:** $a=\frac\alpha{2\pi}=\frac{7.2974\times10^{-3}}{6.2832}=1.1614\times10^{-3}$, $g=2.002323$.
3. **[T] Higher orders:** $a_e=\frac\alpha{2\pi}-0.3285\left(\frac\alpha\pi\right)^2+1.18\left(\frac\alpha\pi\right)^3+\ldots=1.1614\times10^{-3}-1.77\times10^{-6}+1.5\times10^{-8}\approx1.15965\times10^{-3}$, agreeing with the measured $1.15965218\times10^{-3}$ to the digits shown (with the full 4th and 5th order terms and small hadronic and electroweak pieces the agreement is at the $10^{-10}$ level).
4. **[T] Form factors:** $F_1(0)=1$ is charge conservation (Ward identity); $F_2(0)=a$; the vertex divergence cancels against $Z_1=Z_2$.
5. **[T] Order of the Lamb shift:** $\alpha^5m_ec^2=1.06\times10^{-5}$ eV $=2.6$ GHz; the Bethe formula with $\frac{4}{3\pi n^3}=0.053$ and the logarithm $\sim7.7$ gives $\approx1.0$ GHz, matching $\approx1057.8$ MHz.
6. **[T] Contributions (orders of magnitude):** self-energy $+1017$ MHz, vacuum polarization $-27$ MHz, anomalous moment (included in the self-energy structure) $\sim+68$ MHz, total $\approx1058$ MHz; state which is $O(\alpha^5m)$ and which is suppressed by $\alpha$ relative to the leading self-energy logarithm.
7. **[T] Bethe's picture:** the shift as the difference between the free-electron and bound-electron self-energy, $\Delta E\propto\ln\frac{m}{\langle E-E_n\rangle}$ (bounded below the electron mass by renormalization): why only the difference matters.
8. **[T] Determination of $\alpha$:** from $a_e^{\rm exp}$ and the QED series one infers $\alpha^{-1}=137.035\,999\ldots$ (compare with atom-recoil values: check the current numbers).
9. **[C] What does ten-digit agreement establish about QED?** A full session: what is tested (perturbative QED at $\sim4$ to $5$ loops), what is not (physics at energies far above $m_e$), and what it says about renormalization as a method.
10. **[C] And about QFT as a framework?** Which assumptions of the whole of Volume 1 are tested by $a_e$, and which are untouched?

## Optional extension

Compute the one-loop vertex correction $F_2(0)=\frac\alpha{2\pi}$ from the Feynman-parameter integral $\frac{\alpha}{2\pi}\int_0^1dx\,dy\,dz\,\delta(x+y+z-1)\frac{2m^2z(1-z)}{m^2(1-z)^2}$ and check you get $\frac{\alpha}{2\pi}$ exactly.

## Pitfalls

- Treating the Lamb shift as a single effect rather than several comparable contributions.
- Quoting experimental numbers without checking the latest values.
- Confusing agreement at $10^{-10}$ with a proof of the foundations of QFT.

## Gate questions

1. Why is $F_1(0)=1$ but $F_2(0)\ne0$?
2. Why is the Lamb shift of order $\alpha^5m$?
3. What does ten-digit agreement not test?

## One-page cheat sheet contents

Form factors and Schwinger's result; the series for $a_e$; Lamb-shift contributions and orders; what $g-2$ tests.
