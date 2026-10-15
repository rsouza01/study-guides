# Module 18: The stress-energy tensor and relativistic fields (★)

**Books:** Goldstein 13.3 (the stress-energy tensor and conservation theorems), 13.5 (relativistic field theory), 13.6 (examples of relativistic field theories; read the Klein-Gordon example carefully); Jackson $\S$12.10 (the same tensor for the electromagnetic field, with the canonical-versus-symmetric problem and the Belinfante improvement; read the two accounts side by side); Landau and Lifshitz *Classical Theory of Fields* (optional).
**Time:** 2 weeks (four sessions). Units: $\hbar=c=1$ and signature $(+,-,-,-)$ unless stated.

## Why this matters for the bridge

The canonical stress-energy tensor $T^{\mu\nu}=\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\partial^\nu\phi-\eta^{\mu\nu}\mathcal L$ is the conserved current of spacetime translations (Noether, Module 19): $T^{00}$ is the energy density, $T^{0i}$ the momentum density, and $P^\mu=\int T^{0\mu}d^3x$ is the conserved four-momentum. It is the same object as Jackson's Maxwell stress tensor, and the same problems arise there (the canonical tensor is neither symmetric nor gauge-invariant; the Belinfante procedure repairs it). The Hamiltonian formulation of Module 17 gives the field Poisson bracket; here you see that $P^\mu$ *generates translations* of the field through that bracket, the field-theory version of Module 10's "momentum generates translations." Relativistic scalar and complex scalar fields are the arena in which this guide ends and quantum field theory begins.

## Skip-test (40 minutes, no notes)

1. Define $T^{\mu\nu}_{\rm can}=\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\partial^\nu\phi-\eta^{\mu\nu}\mathcal L$ and show $\partial_\mu T^{\mu\nu}=0$ on solutions of the field equations.
2. For the real scalar field $\mathcal L=\frac12(\partial_\mu\phi\partial^\mu\phi-m^2\phi^2)$ compute $T^{00}=\frac12(\dot\phi^2+(\nabla\phi)^2+m^2\phi^2)$ and $T^{0i}=-\dot\phi\,\partial_i\phi$.
3. State why $P^\mu=\int T^{0\mu}d^3x$ is conserved (and what boundary condition is needed).
4. Write the electromagnetic Lagrangian $\mathcal L=-\frac14F_{\mu\nu}F^{\mu\nu}$ and its symmetric stress tensor $\Theta^{\mu\nu}=F^{\mu\lambda}F_\lambda{}^\nu+\frac14\eta^{\mu\nu}F_{\lambda\sigma}F^{\lambda\sigma}$ with $\Theta^{00}=\frac12(E^2+B^2)$.
5. Show that $P^i=-\int\pi\,\partial_i\phi\,d^3x$ generates translations of the field through $\{\phi(x),P^i\}=-\partial_i\phi(x)$.

## Prerequisites

Modules 13, 17 (or at least the covariant notation), 10.

## Detailed topics (checklist)

**The stress-energy tensor (13.3) [Must]**
- Definition from a translation-invariant $\mathcal L$; $\partial_\mu T^{\mu\nu}=0$; the four conserved charges $P^\nu=\int T^{0\nu}d^3x$ (energy and momentum) provided the fields vanish fast enough at spatial infinity; $T^{00}=\mathcal H$.
- Examples: real scalar field, complex scalar field $\mathcal L=\partial_\mu\phi^*\partial^\mu\phi-m^2|\phi|^2$ with $T^{\mu\nu}=\partial^\mu\phi^*\partial^\nu\phi+\partial^\nu\phi^*\partial^\mu\phi-\eta^{\mu\nu}\mathcal L$; the self-interacting field $\mathcal L=\frac12(\partial\phi)^2-\frac12m^2\phi^2-\frac\lambda{4!}\phi^4$.
- **Canonical versus symmetric:** $T^{\mu\nu}_{\rm can}$ is not in general symmetric; one can add a total divergence $\partial_\lambda B^{\lambda\mu\nu}$ with $B$ antisymmetric in its first two indices without changing the charges $P^\mu$ (Belinfante); the symmetric tensor is the source of gravity in general relativity and agrees with the Maxwell stress tensor for the EM field.

**Hamiltonian formulation and brackets (13.4) [Must]**
- $\mathcal H=\pi\dot\phi-\mathcal L$; $H=\int\mathcal H\,d^3x$; $\dot\phi=\{\phi,H\}=\pi$, $\dot\pi=\{\pi,H\}=\nabla^2\phi-m^2\phi$ (free scalar); $P^i=-\int\pi\partial_i\phi\,d^3x$ generates translations: $\delta\phi=\epsilon\{\phi,P^i\}=-\epsilon\partial_i\phi$.

**Relativistic field theory (13.5 to 13.6) [Must]**
- Lorentz invariance of $\mathcal L$ (a scalar density); the Klein-Gordon field and its solutions $\omega_k^2=k^2+m^2$; fields as representations of the Lorentz group (scalar, vector $A^\mu$; the spinor is in the EM guide and QM guides); the electromagnetic field $\mathcal L=-\frac14F_{\mu\nu}F^{\mu\nu}-J^\mu A_\mu$ and its Euler-Lagrange equations $\partial_\mu F^{\mu\nu}=J^\nu$.
- The Proca field $\mathcal L=-\frac14F^2+\frac12\mu^2A_\mu A^\mu$: the mass term breaks gauge invariance (Jackson $\S$12.8).

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Goldstein 13.3; derive $\partial_\mu T^{\mu\nu}=0$ closed-book |
| B1 | Exercises 1 to 4 |
| A2 | Goldstein 13.5 to 13.6; the Klein-Gordon example |
| B2 | Exercises 5 to 7 |
| A3 | Jackson $\S$12.10 (if the EM guide has reached it) or Landau and Lifshitz on $T^{\mu\nu}$; compare with Goldstein |
| B3 | Exercises 8 to 10; cheat sheet |

## Derive from scratch (A sessions, book closed)

1. $\partial_\mu T^{\mu\nu}_{\rm can}=0$ on shell.
2. $T^{00}$ and $T^{0i}$ for the real scalar field.
3. $P^\mu=\int T^{0\mu}d^3x$ and its conservation.
4. $\{\phi(x),P^i\}=-\partial_i\phi(x)$ from the field brackets.
5. The Belinfante improvement for the electromagnetic field.

## Bare-minimum exercises (with expected results)

1. **Scalar $T^{\mu\nu}$:** for $\mathcal L=\frac12(\partial\phi)^2-\frac12m^2\phi^2$ show $T^{\mu\nu}=\partial^\mu\phi\,\partial^\nu\phi-\eta^{\mu\nu}\mathcal L$, symmetric already, with $T^{00}=\frac12(\dot\phi^2+(\nabla\phi)^2+m^2\phi^2)\ge0$.
2. **Conservation:** verify $\partial_\mu T^{\mu\nu}=0$ using $(\Box+m^2)\phi=0$.
3. **Plane wave:** for $\phi=a\cos(\omega t-kx)$ with $\omega^2=k^2+m^2$ show the period averages are $\langle T^{00}\rangle=\frac12a^2\omega^2$ and $\langle T^{0x}\rangle=\frac12a^2\omega k$, so the energy flows with velocity $\langle T^{0x}\rangle/\langle T^{00}\rangle=k/\omega$, the group velocity.
4. **Complex scalar:** show $T^{\mu\nu}=\partial^\mu\phi^*\partial^\nu\phi+\partial^\nu\phi^*\partial^\mu\phi-\eta^{\mu\nu}\mathcal L$ is conserved and symmetric.
5. **$\phi^4$ theory:** for $\mathcal L=\frac12(\partial\phi)^2-\frac\lambda{4!}\phi^4$ find $T^{00}$ and show the energy is bounded below for $\lambda>0$.
6. **Brackets and translations:** with $P^i=-\int\pi\partial_i\phi\,d^3x$ show $\{\phi(x),P^i\}=-\partial_i\phi(x)$ and interpret: the field is translated by $+\epsilon$ (so $\phi'(x)=\phi(x-\epsilon)$).
7. **Energy generates time evolution:** show $\{\phi,H\}=\pi=\dot\phi$ and $\{\pi,H\}=\nabla^2\phi-m^2\phi=\ddot\phi$ for the free scalar field: the Klein-Gordon equation from Hamilton's equations.
8. **EM stress tensor:** show $\Theta^{00}=\frac12(E^2+B^2)$ (Heaviside-Lorentz units) from $F^{0i}=-E^i$, $F^{ij}=-\epsilon^{ijk}B^k$ and $\Theta^{0i}=(\mathbf E\times\mathbf B)^i$; compare with Jackson's Poynting vector.
9. **Canonical versus symmetric:** compute $T^{\mu\nu}_{\rm can}=-F^{\mu\lambda}\partial^\nu A_\lambda+\frac14\eta^{\mu\nu}F^2$ and show $T^{\mu\nu}_{\rm can}-\Theta^{\mu\nu}=-\partial_\lambda(F^{\mu\lambda}A^\nu)$ on shell ($\partial_\lambda F^{\mu\lambda}=0$): a total divergence antisymmetric in $(\mu,\lambda)$, so it changes neither $\partial_\mu T^{\mu\nu}=0$ nor the charges $P^\nu$.
10. **Lorentz transformation:** show $T^{\mu\nu}$ transforms as a tensor, so the total four-momentum $P^\mu=\int T^{0\mu}d^3x$ of a localized, conserved wave packet transforms as a four-vector (this uses $\partial_\mu T^{\mu\nu}=0$); compute the invariant mass $\sqrt{P^\mu P_\mu}$ of a packet at rest and of the same packet boosted.

## Optional extension

Compute the angular momentum density of the scalar field $M^{\lambda\mu\nu}=x^\mu T^{\lambda\nu}-x^\nu T^{\lambda\mu}$, show it is conserved when $T^{\mu\nu}$ is symmetric, and note that for the canonical (non-symmetric) tensor an additional *spin* term is required.

## Pitfalls

- Believing the canonical tensor is always symmetric.
- Dropping the boundary term at infinity when claiming $P^\mu$ is conserved.
- Sign errors from $\partial^i=-\partial_i$ in $T^{0i}$.
- Confusing $\mathcal H$ (a density) with $H$ (the integral).

## Gate questions

1. What is $T^{00}$, and what does $\int T^{0i}d^3x$ represent?
2. Why can one add a total divergence to the canonical tensor, and what does it leave unchanged?
3. Why does $P^i$ generate translations of the field through the bracket, and how does this parallel Module 10?

## One-page cheat sheet contents

Definition of $T^{\mu\nu}$ and conservation; scalar-field $T^{\mu\nu}$; EM symmetric tensor; Belinfante; $P^\mu$ as generators.
