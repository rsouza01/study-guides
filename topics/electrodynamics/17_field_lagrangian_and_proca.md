# Module 17: The field Lagrangian and the Proca field (★★★: the second of the two weeks that justify the guide)

**Books:** Jackson **12.7** (the Lagrangian for the electromagnetic field), **12.8** (the Proca Lagrangian and photon mass), 12.9 (effective photon mass in superconductivity, the London penetration depth: optional but strongly recommended: the Meissner effect is the Higgs mechanism in its natural habitat); Landau and Lifshitz *The Classical Theory of Fields* (from the start: builds electrodynamics from the action); your mechanics guide, Modules 17 to 19 (fields, stress-energy, Noether). **Gaussian units, signature $(+,-,-,-)$.**
**Time:** 3 weeks (six sessions). Give this a full week of attention: when you later open a QFT text at Klein-Gordon, you will already have derived most of the chapter.

## Why this matters

Section 12.7 is where classical electrodynamics *becomes* classical field theory: you stop treating $A_\mu$ as bookkeeping and start treating it as the dynamical variable of an action $$S=-\frac{1}{16\pi}\int F_{\mu\nu}F^{\mu\nu}\,d^4x-\frac1c\int J_\mu A^\mu\,d^4x$$ whose Euler-Lagrange equations *are* Maxwell's equations. Section 12.8 is your Klein-Gordon warm-up. Add $\frac{\mu^2}{8\pi}A_\mu A^\mu$ and verify each consequence yourself: (1) **gauge invariance dies**, which is *the* reason gauge bosons want to be massless and the reason the Higgs mechanism must exist; (2) the equation becomes $(\Box+\mu^2)A^\nu=\frac{4\pi}{c}J^\nu$: component by component, **the Klein-Gordon equation with a source**; (3) the static solution is the Yukawa potential $\frac{e^{-\mu r}}{r}$, which you met in Module 03; the circle closes; (4) the degrees of freedom go $2\to3$ (the longitudinal mode that gauge invariance had been removing).

## Skip-test (40 minutes, no notes)

1. Vary $S=-\frac{1}{16\pi}\int F_{\mu\nu}F^{\mu\nu}d^4x-\frac1c\int J_\mu A^\mu d^4x$ with respect to $A_\mu$ and obtain $\partial_\mu F^{\mu\nu}=\frac{4\pi}{c}J^\nu$; explain why the homogeneous equations need no variation (the Bianchi identity, automatic from $F=dA$).
2. Show $-\frac{1}{16\pi}F_{\mu\nu}F^{\mu\nu}=\frac{1}{8\pi}(E^2-B^2)$ and identify the canonical momentum densities ($\pi^0=0$, $\pi^i\propto E^i$).
3. Derive the Proca equation $\partial_\alpha F^{\alpha\beta}+\mu^2A^\beta=\frac{4\pi}{c}J^\beta$ from $\mathcal L=-\frac{1}{16\pi}F^2+\frac{\mu^2}{8\pi}A_\alpha A^\alpha-\frac1cJ_\alpha A^\alpha$.
4. Show the Lorenz condition $\partial_\alpha A^\alpha=0$ is now *forced* (by taking the divergence), not chosen, and that the equation reduces to $(\Box+\mu^2)A^\beta=\frac{4\pi}{c}J^\beta$.
5. Show the static point-charge solution is the Yukawa potential and count the physical degrees of freedom ($3$).

## Prerequisites

Modules 10, 11, 14, 15 and 16; mechanics guide Modules 17 to 19 (field Euler-Lagrange equations, Noether).

## Detailed topics (checklist)

**The EM field Lagrangian (12.7) [Must]**
- $\mathcal L=-\frac{1}{16\pi}F_{\mu\nu}F^{\mu\nu}-\frac1cJ_\mu A^\mu$; Lorentz invariant, gauge invariant if $\partial_\mu J^\mu=0$; the Euler-Lagrange equation for fields $\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu A_\nu)}-\frac{\partial\mathcal L}{\partial A_\nu}=0$ gives $\partial_\mu F^{\mu\nu}=\frac{4\pi}{c}J^\nu$; the homogeneous equations are the Bianchi identity.
- In terms of fields $\mathcal L=\frac{1}{8\pi}(E^2-B^2)-\rho\Phi+\frac1c\mathbf J\cdot\mathbf A$; canonical momenta $\pi^0=0$ (so $A_0$ is not dynamical) and $\pi^i\propto E^i$; the Hamiltonian density $\frac{1}{8\pi}(E^2+B^2)$.
- Particle plus field: $S=S_{\rm field}+S_{\rm int}+S_{\rm particle}$; the action reproduces both Maxwell's equations (vary $A$) and the Lorentz force (vary the worldline).

**The Proca Lagrangian (12.8) [Must]**
- $\mathcal L_{\rm Proca}=-\frac{1}{16\pi}F_{\alpha\beta}F^{\alpha\beta}+\frac{\mu^2}{8\pi}A_\alpha A^\alpha-\frac1cJ_\alpha A^\alpha$; equation of motion $\partial_\alpha F^{\alpha\beta}+\mu^2A^\beta=\frac{4\pi}{c}J^\beta$; the divergence gives $\mu^2\partial_\beta A^\beta=\frac{4\pi}{c}\partial_\beta J^\beta=0$, so $\partial_\beta A^\beta=0$ is forced; then $(\Box+\mu^2)A^\beta=\frac{4\pi}{c}J^\beta$: **the Klein-Gordon equation with a source for each component**.
- **Consequences:** (1) the mass term $A_\alpha A^\alpha$ is *not* invariant under $A_\mu\to A_\mu+\partial_\mu\Lambda$; (2) static source: $(-\nabla^2+\mu^2)\Phi=4\pi\rho$, so $\Phi=q\frac{e^{-\mu r}}{r}$ (Yukawa); (3) degrees of freedom $4-1=3$: two transverse and one longitudinal polarization, the dispersion relation $\omega^2=c^2k^2+\mu^2c^2$; (4) the photon mass is bounded experimentally (static fields, Jupiter's field, etc.); the Compton wavelength $\lambda_C=\frac1\mu$.
- **London and the Meissner effect (12.9):** inside a superconductor $\nabla^2\mathbf B=\frac{\mathbf B}{\lambda_L^2}$, the photon acquires an effective mass $\mu=\frac1{\lambda_L}$; fields are screened over $\lambda_L$; the Higgs mechanism in its natural habitat.

## Method card

**Varying an action:** (1) write $\mathcal L$ in terms of the independent fields; (2) compute $\frac{\partial\mathcal L}{\partial(\partial_\mu A_\nu)}$ (careful with the antisymmetric $F_{\mu\nu}$: the derivative of $F_{\alpha\beta}F^{\alpha\beta}$ gives $4F^{\mu\nu}$) and $\frac{\partial\mathcal L}{\partial A_\nu}$; (3) assemble the Euler-Lagrange equation; (4) take the divergence to find constraints; (5) interpret (gauge invariance, conservation, degrees of freedom).

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Jackson 12.7; the variation of the action (derivation 1) |
| B1 | Exercises 1 and 2 |
| A2 | The canonical momenta; the Hamiltonian; Landau and Lifshitz on the action |
| B2 | Exercises 3 |
| A3 | Jackson 12.8; Proca (derivation 3 and 4) |
| B3 | Exercises 4 to 6 |
| A4 | The Yukawa solution; counting degrees of freedom |
| B4 | Exercises 7 to 9 |
| A5 | Jackson 12.9; the Meissner effect |
| B5 | **Jackson targets** (exercise 10); write the deliverable `m17-proca.md` |
| A6/B6 | Spare sessions; the month gate (items 7 and 8) |

## Derive from scratch

1. Maxwell's equations from the action.
2. $\mathcal L=\frac{1}{8\pi}(E^2-B^2)$ and the canonical momenta.
3. The Proca equation.
4. The forced Lorenz condition and the Klein-Gordon form.
5. The Yukawa solution and the counting of degrees of freedom.

## Bare-minimum exercises (with expected results)

1. **Maxwell from the action:** show $\frac{\partial\mathcal L}{\partial(\partial_\mu A_\nu)}=-\frac{1}{4\pi}F^{\mu\nu}$ and $\frac{\partial\mathcal L}{\partial A_\nu}=-\frac1cJ^\nu$, so $\partial_\mu F^{\mu\nu}=\frac{4\pi}{c}J^\nu$; explain why varying $F_{\mu\nu}F^{\mu\nu}$ gives a factor $4$ that cancels the $\frac{1}{16\pi}$ to $\frac{1}{4\pi}$.
2. **Fields form:** $F_{\mu\nu}F^{\mu\nu}=2(B^2-E^2)$ so $-\frac{1}{16\pi}F^2=\frac{1}{8\pi}(E^2-B^2)$.
3. **Canonical momenta:** with $\partial_0=\frac1c\partial_t$ and $F_{0i}=\partial_0A_i-\partial_iA_0$ show $\pi^i=\frac{\partial\mathcal L}{\partial(\partial_0A_i)}\propto E^i$ and $\pi^0=0$: the scalar potential is not a dynamical variable (a constraint; see Module 10's Coulomb gauge).
4. **Proca equation:** derive $\partial_\alpha F^{\alpha\beta}+\mu^2A^\beta=\frac{4\pi}{c}J^\beta$; take $\partial_\beta$ of both sides to get $\mu^2\partial_\beta A^\beta=0$, hence $\partial_\beta A^\beta=0$ is forced; then $\partial_\alpha F^{\alpha\beta}=\Box A^\beta-\partial^\beta(\partial\cdot A)=\Box A^\beta$ and $(\Box+\mu^2)A^\beta=\frac{4\pi}{c}J^\beta$.
5. **Yukawa:** for a static point charge $q$ at the origin, $(\nabla^2-\mu^2)\Phi=-4\pi q\delta^3(\mathbf x)$ is solved by $\Phi=q\frac{e^{-\mu r}}{r}$ (check by substitution with $\nabla^2\frac{e^{-\mu r}}{r}=\mu^2\frac{e^{-\mu r}}{r}-4\pi\delta^3$ and compare with Module 03 exercise 10 and Module 02 exercise 9).
6. **Gauge invariance dies:** under $A_\mu\to A_\mu+\partial_\mu\Lambda$ the mass term changes by $\frac{\mu^2}{8\pi}(2A^\mu\partial_\mu\Lambda+\partial_\mu\Lambda\partial^\mu\Lambda)\ne0$, whereas $F_{\mu\nu}$ is invariant.
7. **Counting polarizations:** plane waves $A^\mu=\epsilon^\mu e^{-ik\cdot x}$ in Proca have $k^2=\mu^2c^2$ and $k\cdot\epsilon=0$, giving $4-1=3$ independent polarizations (versus $2$ for the massless case: $k^2=0$, $k\cdot\epsilon=0$ with the residual gauge $\epsilon\to\epsilon+\alpha k$).
8. **Photon-mass scale:** if static fields are Coulombic out to $6400$ km (Earth scale), $\mu^{-1}\gtrsim6.4\times10^6$ m so $m_\gamma c^2=\hbar c\mu\lesssim\frac{1.97\times10^{-7}\,{\rm eV\,m}}{6.4\times10^6\,{\rm m}}\approx3\times10^{-14}$ eV (the tighter bounds from astrophysical fields are many orders of magnitude smaller).
9. **London depth:** for $n=10^{22}$ cm$^{-3}$ electrons, $\lambda_L=\sqrt{\frac{mc^2}{4\pi ne^2}}\approx5\times10^{-6}$ cm (about 50 nm); the static equation $\nabla^2\mathbf B=\mathbf B/\lambda_L^2$ gives exponential screening.
10. **Jackson targets (about 12.15 or 12.16, at least one mandatory):** the Proca equations for a static localized source, the Yukawa solution and the experimental bounds on the photon mass; then the month-4 gate items 7 and 8 (below) as a written deliverable `m17-proca.md`.

## Blank-page gate (Month 4, items 7 and 8)

7. Vary the action with respect to $A_\mu$ and obtain $\partial_\mu F^{\mu\nu}=\frac{4\pi}{c}J^\nu$; explain why the homogeneous equations need no variation.
8. Derive the Proca equation; show gauge invariance fails; show $\partial_\mu A^\mu=0$ is now *forced* rather than chosen; get the Yukawa solution; count the degrees of freedom.

## Optional extension

Quantize the massive field mode by mode (each Fourier mode is an oscillator with frequency $\omega_k=c\sqrt{k^2+\mu^2/\hbar^2}$): the particle spectrum is the Proca particle of mass $\hbar\mu/c$ and spin 1; compare with the massless photon and its two helicities.

## Pitfalls

- Forgetting the factor $4$ from varying the antisymmetric $F_{\mu\nu}$.
- Believing the Lorenz gauge is a choice for the Proca field (it is a consequence).
- Mixing the sign of the mass term in $\mathcal L$ (check that it gives $+\mu^2A^\beta$ in the equation).
- Treating the three Proca polarizations as all physical in the $\mu\to0$ limit (the longitudinal one decouples from conserved currents).

## Gate questions

1. Why do the homogeneous Maxwell equations need no variation?
2. Why does a mass term break gauge invariance and what does that suggest about the Higgs mechanism?
3. Why does the Proca field have three degrees of freedom while the photon has two?

## One-page cheat sheet contents

$\mathcal L_{\rm EM}$ and its equation; $\mathcal L_{\rm Proca}$ and its equation; forced Lorenz condition; Yukawa; counting; London depth.
