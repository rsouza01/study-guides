# Module 17: Part Three a, where divergences come from, and regularization (Weeks 25 and 26; Protocol B)

**Books:** Klauber Part Three (divergence and regularization chapters); **read Schwartz's renormalization chapters alongside, not after**; second sources: Tong's renormalization lectures, Lancaster and Blundell.
**Time:** 2 weeks. Part Three in total is five weeks (Modules 17 to 19). Given that you derived this and it still did not land, the hollowness is probably worst here: loop-integral algebra is absorbing enough to hide the concept entirely underneath it.

## Diagnostic (40 minutes, no notes)

1. Compute the superficial degree of divergence of a QED diagram with $E_\gamma$ external photons and $E_f$ external fermions.
2. Set up the one-loop correction to $2\to2$ in $\phi^4$ and classify its divergence.
3. Evaluate the Euclidean integral $\int\frac{d^4\ell_E}{(2\pi)^4}\frac{1}{(\ell_E^2+\Delta)^2}$ with a cutoff and in dimensional regularization.
4. Combine denominators with a Feynman parameter.
5. State whether the regulator is physical.

## Prerequisites

Modules 13 to 16.

## Detailed topics (checklist)

**Week 25: where divergences come from [Must]**
- A loop integral integrates over *all* loop momenta; **superficial degree of divergence** $D$: for $\phi^4$ in four dimensions $D=4-E$ (where $E$ is the number of external legs), so only the $E=2$ ($D=2$) and $E=4$ ($D=0$) amplitudes diverge; for QED $D=4-\tfrac32E_f-E_\gamma$: electron self-energy ($D=1$, reduced to logarithmic by symmetry), vacuum polarization ($D=2$, reduced to logarithmic by gauge invariance), vertex ($D=0$), light-by-light ($D=0$, finite by gauge invariance), three-photon amplitude vanishes (Furry); renormalizability = finitely many divergent amplitude types.
- *Counterfactual:* are divergences a failure of the theory, of perturbation theory, or a signal about short-distance physics?

**Week 26: regularization [Must]**
- Methods: momentum cutoff; Pauli-Villars (heavy regulator fields); **dimensional regularization**: $d=4-\varepsilon$, $\int\frac{d^d\ell}{(2\pi)^d}\frac{1}{(\ell^2-\Delta)^2}=\frac{i}{(4\pi)^{d/2}}\Gamma\left(2-\tfrac d2\right)\Delta^{d/2-2}\to\frac{i}{16\pi^2}\left(\frac2\varepsilon-\gamma+\ln4\pi-\ln\Delta\right)$; Feynman parameters $\frac1{AB}=\int_0^1\frac{dx}{[xA+(1-x)B]^2}$; Wick rotation $\ell^0=i\ell_E^0$.
- *Counterfactual:* is the regulator physical? Different regulators agree: why should that be true?

## Reading plan

| Week | Task |
| --- | --- |
| 25 | Prose pass; three questions; power counting; exercises 1 to 3; the [C] |
| 26 | Regularization; counterfactuals; exercises 4 to 7; the sceptic explanation |

## Derive from scratch (only if triggered)

1. The superficial degree of divergence formula.
2. The dimensional-regularization master formula.
3. The Feynman-parameter combination.

## Exercises

1. **[T] Power counting:** each loop adds $d^4\ell$ (4), each fermion propagator $\sim\frac1\ell$ ($-1$), each boson propagator $\sim\frac1{\ell^2}$ ($-2$): $\phi^4$ one loop with $E=4$ has two propagators: $D=4-4=0$ (log); QED vacuum polarization: $4-2\times1=2$.
2. **[T] $\phi^4$ one-loop bubble:** $\int\frac{d^4\ell_E}{(2\pi)^4}\frac{1}{(\ell_E^2+\Delta)^2}=\frac{1}{16\pi^2}\left[\ln\frac{\Lambda^2}{\Delta}-1\right]+O(\Delta/\Lambda^2)$ with a cutoff $\Lambda$ on $|\ell_E|$.
3. **[T] Wick rotation:** $\int d^4\ell\frac{1}{(\ell^2-\Delta+i\epsilon)^2}=i\int d^4\ell_E\frac{1}{(\ell_E^2+\Delta)^2}$ (rotating the contour counter-clockwise avoids the poles at $\ell^0=\pm\sqrt{\ell^2+\Delta-i\epsilon}$).
4. **[T] Dimensional regularization:** $\frac{i}{16\pi^2}\Gamma(\frac\varepsilon2)\left(\frac{4\pi}{\Delta}\right)^{\varepsilon/2}=\frac{i}{16\pi^2}\left[\frac2\varepsilon-\gamma+\ln4\pi-\ln\Delta+O(\varepsilon)\right]$; the pole $\frac2\varepsilon$ replaces $\ln\Lambda^2$.
5. **[T] Feynman parameters:** $\frac{1}{(\ell^2-m^2)((\ell+p)^2-m^2)}=\int_0^1\frac{dx}{\left[(\ell+xp)^2-m^2+x(1-x)p^2\right]^2}$; the shift $\ell\to\ell-xp$ gives $\Delta=m^2-x(1-x)p^2$.
6. **[T] Same divergence, three regulators:** the coefficient of the logarithmic divergence ($\frac{1}{16\pi^2}$) is the same in cutoff, Pauli-Villars and dimensional regularization; only the finite constants differ (scheme dependence).
7. **[T] A convergent contrast:** $\int\frac{d^4\ell_E}{(2\pi)^4}\frac{1}{(\ell_E^2+\Delta)^3}=\frac{1}{32\pi^2\Delta}$: finite, $D=-2$.
8. **[T] Setup of a real diagram:** write the electron self-energy $-i\Sigma(p)=(-ie)^2\int\frac{d^4k}{(2\pi)^4}\gamma^\mu\frac{i(p\!\!\!/-k\!\!\!/+m)}{(p-k)^2-m^2}\gamma_\mu\frac{-i}{k^2}$ and classify its divergence ($D=1$, log after symmetric integration).
9. **[C] Why all scales?** Why does integrating over all loop momenta amount to a claim about physics at all energy scales, and why is that claim obviously unjustified?
10. **[C] The sceptic:** explain to a sceptic why "subtracting infinity" is not what is happening. **If you cannot do this convincingly, that is the first pass's failure, located.**

## Optional extension

Show that quadratic divergences in the scalar mass correction are absent in dimensional regularization and discuss what that does and does not imply about the hierarchy problem.

## Pitfalls

- Treating the cutoff as physical or as harmless.
- Forgetting the Wick-rotation factor $i$.
- Mistaking scheme-dependent finite parts for predictions.

## Gate questions

1. Which diagrams diverge in $\phi^4$ and in QED?
2. Why do different regulators agree on the logarithm?
3. What is the regulator for?

## One-page cheat sheet contents

Power counting; the dimensional-regularization master formula; Wick rotation; Feynman parameters.
