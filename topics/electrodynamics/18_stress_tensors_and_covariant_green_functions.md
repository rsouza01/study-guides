# Module 18: Stress tensors and covariant Green functions (★)

**Books:** Jackson **12.10** (canonical and symmetric stress tensors; conservation laws) and **12.11** (solution of the wave equation in covariant form: invariant Green functions); your mechanics guide, Modules 18 and 19 (the stress-energy tensor and Noether's theorem: read them side by side with this module). Gaussian units; **note the sign convention for $\Box$ changes**: Jackson's chapter 6 uses $\Box=\nabla^2-\frac{1}{c^2}\partial_t^2$, while chapter 12 uses $\Box=\partial_\mu\partial^\mu=\frac{1}{c^2}\partial_t^2-\nabla^2$.
**Time:** 2 weeks (four sessions).

## Why this matters

Jackson builds the canonical stress tensor from the Lagrangian, finds it neither symmetric nor gauge-invariant, and repairs it by adding a total divergence (the **Belinfante procedure**). This exact issue recurs verbatim in QFT and in general relativity. Meeting it here, where every step can be checked against known answers, is a real advantage. Section 12.11 is Module 11 redone covariantly: $D_r(x-x')$ as an honest Lorentz-invariant distribution.

## Skip-test (40 minutes, no notes)

1. Compute the canonical stress tensor $T^{\mu\nu}_{\rm can}=\frac{\partial\mathcal L}{\partial(\partial_\mu A_\lambda)}\partial^\nu A_\lambda-g^{\mu\nu}\mathcal L=-\frac{1}{4\pi}F^{\mu\lambda}\partial^\nu A_\lambda+\frac{1}{16\pi}g^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}$ and show it is neither symmetric nor gauge invariant.
2. Show the symmetric tensor $\Theta^{\mu\nu}=\frac1{4\pi}\left[g^{\mu\alpha}F_{\alpha\beta}F^{\beta\nu}+\frac14g^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right]$ differs from $T^{\mu\nu}_{\rm can}$ by a total divergence, and give its components $\Theta^{00}$, $\Theta^{0i}$, $\Theta^{ij}$.
3. Derive $\partial_\mu\Theta^{\mu\nu}=-\frac1cF^{\nu\lambda}J_\lambda$ (the force density).
4. Show $\Theta^\mu{}_\mu=0$.
5. State the covariant Green function $D_r(x-x')=\frac{1}{2\pi}\theta(x^0-x'^0)\delta\left[(x-x')^2\right]$ and solve $\Box A^\alpha=\frac{4\pi}{c}J^\alpha$ with it.

## Prerequisites

Modules 11, 15, 17; mechanics guide Modules 18 and 19.

## Detailed topics (checklist)

**Canonical and symmetric stress tensors (12.10) [Must]**
- Noether's theorem for translations: $T^{\mu\nu}_{\rm can}=\frac{\partial\mathcal L}{\partial(\partial_\mu A_\lambda)}\partial^\nu A_\lambda-g^{\mu\nu}\mathcal L$, conserved ($\partial_\mu T^{\mu\nu}=0$ for free fields).
- **Problems with it:** not symmetric (so angular momentum $M^{\lambda\mu\nu}=x^\mu T^{\lambda\nu}-x^\nu T^{\lambda\mu}$ is not conserved without a spin term) and not gauge invariant (contains $A_\lambda$ explicitly).
- **The Belinfante repair:** add $\partial_\lambda B^{\lambda\mu\nu}$ with $B^{\lambda\mu\nu}=-B^{\mu\lambda\nu}$; for EM, $\Theta^{\mu\nu}=T^{\mu\nu}_{\rm can}+\frac{1}{4\pi}\partial_\lambda(F^{\mu\lambda}A^\nu)$ (on shell for free fields); the total four-momentum $P^\nu=\int\Theta^{0\nu}d^3x$ is unchanged because the added term is a total divergence with antisymmetry in $(\lambda,\mu)$.
- Components (Gaussian): $\Theta^{00}=\frac{E^2+B^2}{8\pi}$, $\Theta^{0i}=\frac{(\mathbf E\times\mathbf B)_i}{4\pi}=\frac{S_i}{c}$, $\Theta^{ij}=-T_{ij}$ with $T_{ij}=\frac{1}{4\pi}\left[E_iE_j+B_iB_j-\frac12\delta_{ij}(E^2+B^2)\right]$: the Maxwell stress tensor of Module 12.
- Conservation with sources: $\partial_\mu\Theta^{\mu\nu}=-\frac1cF^{\nu\lambda}J_\lambda$ (the Lorentz-force density $f^\nu$); tracelessness $\Theta^\mu{}_\mu=0$ (conformal invariance of 4D electrodynamics, photons are massless).

**Covariant Green functions (12.11) [Must]**
- $\Box D(x-x')=\delta^{(4)}(x-x')$ with Jackson's $\Box=\partial_\mu\partial^\mu$; $D_r(z)=\frac{1}{2\pi}\theta(z^0)\delta(z^2)$, $D_a(z)=\frac{1}{2\pi}\theta(-z^0)\delta(z^2)$; solution $A^\alpha(x)=\frac{4\pi}{c}\int D_r(x-x')J^\alpha(x')d^4x'$ (plus a homogeneous solution); manifest Lorentz invariance of $\theta(z^0)\delta(z^2)$ (on the light cone the sign of $z^0$ is invariant).
- Relation to Module 11: $D_r=\frac{1}{4\pi}G_{\rm ret}$ (the $4\pi$ offset).
- **Preview of Module 20:** for a point charge $J^\alpha=qc\int d\tau\,u^\alpha\delta^{(4)}(x-z(\tau))$ the integral over $\tau$ with $\delta[(x-z)^2]$ gives the Lienard-Wiechert potential $A^\alpha=\frac{qu^\alpha}{u\cdot(x-z)}\Big|_{\rm ret}$ (the $\delta(f(\tau))$ Jacobian from Module 02).

## Method card

**Constructing $T^{\mu\nu}$ from $\mathcal L$:** (1) compute $\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}$ for each field component; (2) $T^{\mu\nu}=\sum_a\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_a)}\partial^\nu\phi_a-g^{\mu\nu}\mathcal L$; (3) check conservation on the field equations; (4) test symmetry and gauge invariance; (5) improve with a total divergence if needed and verify the charges are unchanged.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Jackson 12.10; derive $T^{\mu\nu}_{\rm can}$ for EM |
| B1 | Exercises 1 to 3 |
| A2 | The Belinfante term; mechanics Module 19 side by side |
| B2 | Exercises 4 to 6 and 9 |
| A3 | Jackson 12.11; the invariant Green function |
| B3 | Exercises 7 and 8 |
| A4 | **Jackson targets** (exercise 10) |
| B4 | Spare session |

## Derive from scratch

1. $T^{\mu\nu}_{\rm can}$ for the EM field.
2. $\Theta^{\mu\nu}-T^{\mu\nu}_{\rm can}$ as a total divergence.
3. $\Theta^{00}$, $\Theta^{0i}$, $\Theta^{ij}$ and $\Theta^\mu{}_\mu=0$.
4. $\partial_\mu\Theta^{\mu\nu}=-\frac1cF^{\nu\lambda}J_\lambda$.
5. $D_r=\frac1{2\pi}\theta(z^0)\delta(z^2)$ from Module 11.

## Bare-minimum exercises (with expected results)

1. **Canonical tensor:** $T^{\mu\nu}_{\rm can}=-\frac{1}{4\pi}F^{\mu\lambda}\partial^\nu A_\lambda+\frac{1}{16\pi}g^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}$; show $T^{\mu\nu}_{\rm can}\ne T^{\nu\mu}_{\rm can}$ in general and that it changes under $A\to A+\partial\Lambda$.
2. **The improvement:** $T^{\mu\nu}_{\rm can}-\Theta^{\mu\nu}=-\frac{1}{4\pi}\partial_\lambda(F^{\mu\lambda}A^\nu)$ for free fields (use $\partial_\lambda F^{\mu\lambda}=0$); the extra term is antisymmetric in $(\mu,\lambda)$.
3. **Components:** from $F^{0i}=-E^i$, $F^{ij}=-\epsilon_{ijk}B^k$ compute $\Theta^{00}=\frac{E^2+B^2}{8\pi}$ and $\Theta^{0i}=\frac{(\mathbf E\times\mathbf B)_i}{4\pi}$; identify $\Theta^{ij}=-T_{ij}$ (compare with Module 12's stress tensor).
4. **Trace:** $\Theta^\mu{}_\mu=\frac1{4\pi}\left[F_{\nu\beta}F^{\beta\nu}+F_{\alpha\beta}F^{\alpha\beta}\right]=0$.
5. **Conservation with sources:** compute $\partial_\mu\Theta^{\mu\nu}$ using Maxwell's equations; for $\nu=0$ show $\partial_t u+\nabla\cdot\mathbf S=-\mathbf J\cdot\mathbf E$ (Poynting's theorem) and for $\nu=i$ the momentum conservation law of Module 12.
6. **Invariance of the charges:** show $P^\nu=\int\Theta^{0\nu}d^3x$ and $P^\nu_{\rm can}=\int T^{0\nu}_{\rm can}d^3x$ agree: the difference is $\frac{1}{4\pi}\int\partial_i(F^{0i}A^\nu)d^3x=0$ (surface term; only the spatial divergence survives since the $\lambda=0$ term vanishes by antisymmetry).
7. **Invariant Green function:** use $\delta(x_0^2-R^2)=\frac{\delta(x_0-R)+\delta(x_0+R)}{2R}$ to show $\frac{1}{2\pi}\theta(x^0)\delta(x^2)=\frac{\delta(x^0-R)}{4\pi R}$, i.e. $D_r=\frac{G_{\rm ret}}{4\pi}$ (with $G_{\rm ret}$ of Module 11, in units $x^0=ct$).
8. **Preview of Lienard-Wiechert:** for a point charge $J^\alpha(x')=qc\int d\tau'\,u^\alpha(\tau')\delta^{(4)}(x'-z(\tau'))$. Insert it in $A^\alpha(x)=\frac{4\pi}{c}\int D_r(x-x')J^\alpha(x')d^4x'$ and do the $x'$ integral to get $A^\alpha(x)=2q\int d\tau'\,u^\alpha(\tau')\,\theta\left(x^0-z^0(\tau')\right)\delta\left[(x-z(\tau'))^2\right]$; evaluate the $\tau'$ integral with the Jacobian $\frac{d}{d\tau'}(x-z)^2=-2u\cdot(x-z)$ to get $A^\alpha=\frac{q\,u^\alpha}{u\cdot(x-z)}$ at the retarded proper time (the full derivation is Module 20).
9. **Belinfante for angular momentum:** show that with $T^{\mu\nu}_{\rm can}$ the orbital $M^{\lambda\mu\nu}=x^\mu T^{\lambda\nu}-x^\nu T^{\lambda\mu}$ is conserved only if $T^{\mu\nu}$ is symmetric (compute $\partial_\lambda M^{\lambda\mu\nu}=T^{\mu\nu}-T^{\nu\mu}$) and identify the missing *spin* part for the vector field.
10. **Jackson targets (about 12.11 and 12.12):** a stress tensor and conservation-law problem (exercises 3 to 5), and a covariant Green function problem (exercise 7). *If your mechanics guide is running, write the two-line dictionary between Goldstein 13.3 and this section.*

## Pitfalls

- Forgetting that Jackson's $\Box$ flips sign between chapters 6 and 12.
- Assuming the canonical tensor is physical (it is the gauge-invariant symmetric one that sources gravity).
- Dropping the antisymmetry condition on $B^{\lambda\mu\nu}$ (it is what keeps $P^\mu$ unchanged).
- Using $D_r$ without the $\theta(z^0)$.

## Gate questions

1. Why is the canonical stress tensor unsatisfactory and what does the Belinfante term fix?
2. Why does $\Theta^\mu{}_\mu=0$ and what does it mean physically?
3. How is $D_r$ the same object as Module 11's $G_{\rm ret}$?

## One-page cheat sheet contents

$T^{\mu\nu}_{\rm can}$ and $\Theta^{\mu\nu}$ with components; Belinfante term; trace; conservation with sources; $D_r$.
