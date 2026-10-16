# Module 18: Part Three b, counterterms, vacuum polarization and the running coupling (Weeks 27 and 28; Protocol B)

**Books:** Klauber Part Three (counterterm and vacuum-polarization chapters); Schwartz renormalization chapters; Tong's renormalization lectures.
**Time:** 2 weeks.

## Why this matters

Week 27: counterterms and the bare versus physical parameters. Week 28: vacuum polarization and the running coupling. **The conceptual heart of Part Three: the coupling depends on the scale you probe. Screening, not bookkeeping.**

## Diagnostic (40 minutes, no notes)

1. State the bare/physical distinction and the counterterms $\delta_m$, $\delta_2$, $\delta_3$.
2. State the Ward identity relation between the vertex and electron wave-function renormalizations.
3. Write the renormalized vacuum polarization and its large-$Q^2$ behaviour.
4. Compute the effective $\alpha(Q^2)$ at $Q=M_Z$ from the electron loop alone and compare with the measured value.
5. State the $\beta$ function of QED and the Landau pole.

## Prerequisites

Module 17.

## Detailed topics (checklist)

**Week 27: counterterms, bare versus physical parameters [Must]**
- The Lagrangian written with bare parameters $m_0$, $e_0$ and fields $\psi_0=\sqrt{Z_2}\psi$, $A_0=\sqrt{Z_3}A$; counterterms $\delta_2=Z_2-1$, $\delta_m$, $\delta_3=Z_3-1$ absorb divergences; renormalization conditions (on-shell scheme: the pole of the propagator at $m$ with residue $i$; photon pole at $q^2=0$ with unit residue; $e$ defined at $q^2=0$); Ward identity $Z_1=Z_2$.
- The electron self-energy: mass shift $\delta m=\frac{3\alpha}{4\pi}m\ln\frac{\Lambda^2}{m^2}$ (cutoff version): a *logarithmic* sensitivity.
- *Counterfactuals:* is the bare mass physical? Are counterterms added or discovered?

**Week 28: vacuum polarization and the running coupling [Must]**
- $\Pi(q^2)=-\frac{2\alpha}{\pi}\int_0^1dx\,x(1-x)\left[\frac2\varepsilon-\gamma+\ln4\pi-\ln\frac{m^2-x(1-x)q^2}{\mu^2}\right]$; after the on-shell subtraction $\hat\Pi(q^2)=-\frac{2\alpha}\pi\int_0^1dx\,x(1-x)\ln\frac{m^2}{m^2-x(1-x)q^2}$; for $Q^2=-q^2\gg m^2$: $\hat\Pi\to\frac{\alpha}{3\pi}\left[\ln\frac{Q^2}{m^2}-\frac53\right]$ and $\alpha_{\rm eff}(Q^2)=\frac{\alpha}{1-\hat\Pi}$; $\beta(e)=\mu\frac{de}{d\mu}=\frac{e^3}{12\pi^2}$, i.e. $\mu\frac{d\alpha}{d\mu}=\frac{2\alpha^2}{3\pi}$; the Landau pole at $\mu\sim m\exp\left(\frac{3\pi}{2\alpha}\right)$ (far beyond any physical scale).

## Reading plan

| Week | Task |
| --- | --- |
| 27 | Prose pass; three questions; counterterms; exercises 1 to 3; the [C] on mass renormalization |
| 28 | Vacuum polarization; running; exercises 4 to 8; the [C] on screening |

## Derive from scratch (only if triggered)

1. The vacuum-polarization integral by Feynman parameters.
2. The on-shell subtraction and its large-$Q^2$ limit.
3. The one-loop $\beta$ function from $Z_3$.

## Exercises

1. **[T] Mass shift size:** $\frac{\delta m}{m}=\frac{3\alpha}{4\pi}\ln\frac{\Lambda^2}{m^2}$; with $\Lambda=M_P$ and $m=0.511$ MeV, $\ln\frac{\Lambda^2}{m^2}\approx103$, so $\frac{\delta m}{m}\approx0.18$: a mild, logarithmic, not catastrophic, sensitivity to the cutoff.
2. **[T] Ward identity:** $Z_1=Z_2$ follows from current conservation; consequence: the renormalized charge is determined by the photon self-energy alone: $e=\sqrt{Z_3}e_0$.
3. **[T] Counterterm Lagrangian:** $\mathcal L=\bar\psi(iZ_2\partial\!\!\!/-Z_2m_0)\psi-\tfrac14Z_3F^2-e_0Z_2\bar\psi\gamma^\mu\psi A_\mu$ (with $Z_1=Z_2$) rewritten as the renormalized Lagrangian plus counterterms $\delta_2$, $\delta_3$, $\delta_m$.
4. **[T] Vacuum polarization at large $Q^2$:** $\hat\Pi(-Q^2)\to\frac{\alpha}{3\pi}\left[\ln\frac{Q^2}{m^2}-\frac53\right]$ (the integral $\int_0^1dx\,x(1-x)\ln\frac{Q^2x(1-x)}{m^2}$ gives $\frac16\left(\ln\frac{Q^2}{m^2}-\frac53\right)$).
5. **[T] Running to $M_Z$ (electron loop only):** $\ln\frac{M_Z^2}{m_e^2}=24.2$, $\hat\Pi=\frac{7.297\times10^{-3}}{3\pi}(24.2-1.67)=0.0174$; $\alpha_{\rm eff}=\frac{\alpha}{1-0.0174}$, i.e. $1/\alpha_{\rm eff}=137.036\times(1-0.0174)=134.7$. Including all charged fermions the measured value is $1/\alpha(M_Z)\approx128$ to $129$: the running is *observed* (Bhabha scattering and the $R$ ratio).
6. **[T] $\beta$ function:** from $\alpha(Q^2)=\frac{\alpha}{1-\frac{\alpha}{3\pi}\ln(Q^2/m^2)}$: $\mu\frac{d\alpha}{d\mu}=\frac{2\alpha^2}{3\pi}$ (QED: coupling grows with energy).
7. **[T] Landau pole:** $1-\frac\alpha{3\pi}\ln\frac{Q^2}{m^2}=0$ at $Q=m\exp\left(\frac{3\pi}{2\alpha}\right)=m\,e^{646}\approx10^{280}m$: no physical significance in the Standard Model.
8. **[T] Self-energy setup in dimensional regularization:** $\Sigma(p\!\!\!/)=\frac{\alpha}{4\pi}\left(\frac2\varepsilon+\ldots\right)(-p\!\!\!/+4m)$ in Feynman gauge (state the structure $A(p^2)p\!\!\!/+B(p^2)m$ and which part gives $\delta m$ and which $\delta_2$).
9. **[C] Mass renormalization:** what does mass renormalization mean physically? Is the bare mass physical? Are counterterms added or discovered?
10. **[C] Running:** what is screened, by what, and how would you measure the running? Connect to a real experiment (e.g. Bhabha scattering at LEP, the hadronic $R$ ratio).

## Optional extension

Compute the one-loop $\beta$ function of $\phi^4$ theory, $\beta(\lambda)=\frac{3\lambda^2}{16\pi^2}$, and contrast the sign with QED's behaviour (both grow at high energy).

## Pitfalls

- Reading $\delta m$ as a physical shift of an unobservable quantity.
- Confusing scheme-dependent constants ($-\frac53$) with the physical running ($\ln$).
- Forgetting that the electron loop is only one of many fermion contributions at $M_Z$.

## Gate questions

1. Why is the running of $\alpha$ a *measured* effect?
2. Why does the photon propagator need a counterterm but the photon mass does not?
3. What distinguishes a counterterm from an arbitrary subtraction?

## One-page cheat sheet contents

Counterterms and renormalization conditions; $\hat\Pi(Q^2)$ at large $Q^2$; $\beta$ function; Landau pole.
