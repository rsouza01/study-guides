# Module 12: Chapter 6, Symmetry, invariance and conservation (Weeks 17 and 18), and the Part One gate

**Books:** Klauber Ch. 6; second sources: Tong's symmetries lecture, Schwartz chapter 8, Lancaster and Blundell; your mechanics guide Modules 04 and 19 (Noether) if you have them.
**Time:** 2 weeks, uncompressed. Everything structural in Volume 2 descends from here.

## Why this matters

Noether's theorem for fields, the energy-momentum tensor, charge operators for complex scalar and Dirac fields, the passage from global to local symmetry (the doorway to gauge theory). Two weeks, uncompressed.

## Diagnostic (40 minutes, no notes)

1. State Noether's theorem for a continuous symmetry of the action and derive the conserved current.
2. Construct $T^{\mu\nu}$ for the free scalar field and verify $T^{00}=\mathcal H$.
3. Find the conserved current and charge of the complex scalar field and the Dirac field.
4. Write the charge operator in terms of the ladder operators.
5. State what changes when the symmetry is local rather than global.

## Prerequisites

Modules 06 to 11.

## Detailed topics (checklist)

- Noether: for $\phi\to\phi+\epsilon\,\delta\phi$ with $\delta\mathcal L=\partial_\mu K^\mu$, the current $j^\mu=\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\delta\phi-K^\mu$ satisfies $\partial_\mu j^\mu=0$ on shell and the charge $Q=\int d^3x\,j^0$ is conserved.
- **Spacetime symmetries:** translations give $T^{\mu\nu}=\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\partial^\nu\phi-g^{\mu\nu}\mathcal L$ and $P^\nu=\int d^3x\,T^{0\nu}$; for the free scalar $T^{\mu\nu}=\partial^\mu\phi\partial^\nu\phi-g^{\mu\nu}\mathcal L$, $T^{00}=\tfrac12(\dot\phi^2+(\nabla\phi)^2+m^2\phi^2)$; Lorentz invariance gives angular momentum and boosts.
- **Internal symmetries:** U(1) phase symmetry of the complex scalar $\phi\to e^{i\alpha}\phi$: $j^\mu=i(\phi^*\partial^\mu\phi-\phi\partial^\mu\phi^*)\cdot(\pm1)$ and $Q=\int d^3k\,(a^\dagger a-b^\dagger b)$; Dirac: $j^\mu=\bar\psi\gamma^\mu\psi$, $Q=\int(b^\dagger b-d^\dagger d)$.
- *Counterfactuals:* does Noether require a symmetry of the action, the Lagrangian, or the equations of motion, and does the distinction matter? What is conserved for a local rather than global symmetry?
- **Local symmetry:** requiring $\phi\to e^{i\alpha(x)}\phi$ forces a gauge field and covariant derivative $D_\mu=\partial_\mu+ieA_\mu$ (preview of Part Two).

## Reading plan

| Week | Task |
| --- | --- |
| 17 | Noether and $T^{\mu\nu}$; exercises 1 to 4 |
| 18 | Internal symmetries and charges; exercises 5 to 10; the Part One gate |

## Derive from scratch

1. Noether's theorem for fields.
2. $T^{\mu\nu}$ for the scalar field and $P^\mu$.
3. The U(1) current and charge for the complex scalar.
4. The Dirac current and charge.
5. The covariant derivative from local phase invariance.

## Exercises

1. **[T] Noether, U(1):** complex scalar $\mathcal L=\partial_\mu\phi^*\partial^\mu\phi-m^2\phi^*\phi$ with $\delta\phi=i\alpha\phi$: $j^\mu=i(\phi^*\partial^\mu\phi-\partial^\mu\phi^*\phi)$ up to an overall sign convention; $\partial_\mu j^\mu=0$ on shell.
2. **[T] $T^{\mu\nu}$:** $T^{\mu\nu}=\partial^\mu\phi\partial^\nu\phi-g^{\mu\nu}\mathcal L$, $T^{00}=\mathcal H$, $T^{0i}=\dot\phi\partial^i\phi$; check $\partial_\mu T^{\mu\nu}=0$ on shell.
3. **[T] Momentum:** $\mathbf P=-\int d^3x\,\pi\nabla\phi=\int d^3k\,\mathbf k\,a^\dagger a$ (after normal ordering).
4. **[T] Charge operator:** substitute the expansion: $Q=\int d^3k\,(a^\dagger a-b^\dagger b)$: particles carry $+1$, antiparticles $-1$.
5. **[T] Dirac charge:** $Q=\int d^3x\,\psi^\dagger\psi=\int\frac{d^3p}{(2\pi)^3}\sum_s(b^\dagger b-d^\dagger d)$ (with the anticommutation relations and normal ordering).
6. **[T] Energy-momentum for a field with a $\phi^4$ term:** $T^{\mu\nu}$ keeps its form with $\mathcal L$ including $-\frac\lambda{4!}\phi^4$; $T^{00}$ adds $+\frac\lambda{4!}\phi^4$.
7. **[T] Local gauging:** $\mathcal L=D_\mu\phi^*D^\mu\phi-m^2\phi^*\phi$ with $D_\mu=\partial_\mu+ieA_\mu$ is invariant under $\phi\to e^{i\alpha(x)}\phi$, $A_\mu\to A_\mu-\frac1e\partial_\mu\alpha$; expand to find the interaction $-eA_\mu j^\mu+e^2A^2\phi^*\phi$.
8. **[T] Lorentz current:** state the six conserved currents $M^{\mu\nu\lambda}$ for rotations and boosts and the associated charges $\mathbf J$, $\mathbf K$.
9. **[C] Noether without equations:** explain Noether's theorem, without equations, to someone who knows classical mechanics.
10. **[C] A conservation law you use:** name a conservation law you use constantly and identify the symmetry behind it.

## ▣ Part One gate (end of Week 18, about 2 hours)

Second source first (Lancaster and Blundell or Tong on free-field quantisation). Then:
1. What is a quantum field, and why does the theory need one?
2. Build a free field theory from a Lagrangian for spin 0, 1/2 and 1: the same steps, three times, in parallel columns.
3. All three propagators; which contour gives which; what each means physically.
4. Why fermions anticommute.
5. Gauge freedom, and why it is not a defect.
6. Noether and one worked consequence.
7. **Compression: free field theory on one page**, as an argument, not a formula sheet.

## Optional extension

Derive the Belinfante symmetric stress tensor for the Dirac field and show it differs from the canonical one by a total divergence.

## Pitfalls

- Assuming $T^{\mu\nu}$ from Noether is automatically symmetric.
- Mixing up signs of the U(1) current across conventions.
- Treating local invariance as just a bigger symmetry (it implies a new field).

## Gate questions

1. Why is $Q=a^\dagger a-b^\dagger b$ and not $a^\dagger a+b^\dagger b$?
2. What does a local symmetry add to a global one?
3. How is $T^{00}$ related to $\mathcal H$?

## One-page cheat sheet contents

Noether's current; $T^{\mu\nu}$; charges in terms of ladder operators; the covariant derivative.
