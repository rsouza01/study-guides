# Module 19: Bridge 3, Noether's theorem and gauge invariance (★★★)

**Books:** Goldstein 13.7 (Noether's theorem) and 13.8 (gauge invariance, if present in your printing); Jackson $\S$12.1 and 12.7 (EM Lagrangian and gauge invariance); Landau and Lifshitz *Classical Theory of Fields* (conservation laws from symmetries); Sakurai (momentum and angular momentum as generators), your Zettili guide (Section 3.7 on symmetries and conservation laws, Appendix F on canonical quantization).
**Time:** 3 weeks (six sessions). **A written deliverable.**

## Why this matters for the bridge

Noether's theorem is the *last section of the last chapter* of Goldstein, and everything from Module 04 onward has been a special case of it. Read it as the general statement that all those cases were instances of, not as new material. The symmetry $\to$ conserved quantity map is the same map as symmetry $\to$ generator (Module 10): the Noether charge $Q=\int j^0d^3x$ is the generator of the symmetry through the field Poisson bracket, and after quantization it is the operator that implements the symmetry. A case Chapter 2 could not reach is the **internal $U(1)$ phase symmetry of a complex scalar field**, which gives a conserved current: that is charge, and the fact that it comes from an *internal* rather than a spacetime symmetry is the door into gauge theory.

## Skip-test (40 minutes, no notes)

1. State Noether's theorem for fields: if $\mathcal L(\phi,\partial_\mu\phi)$ is invariant, up to a total divergence $\partial_\mu K^\mu$, under $\phi\to\phi+\epsilon\,\delta\phi$, then $j^\mu=\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\delta\phi-K^\mu$ satisfies $\partial_\mu j^\mu=0$ on shell, and $Q=\int j^0d^3x$ is conserved if the fields fall off at infinity.
2. Derive the conserved current of the $U(1)$ symmetry $\phi\to e^{i\alpha}\phi$ for $\mathcal L=\partial_\mu\phi^*\partial^\mu\phi-m^2\phi^*\phi$: $j^\mu=i(\phi\,\partial^\mu\phi^*-\phi^*\partial^\mu\phi)$.
3. For the Schrödinger field show the Noether current of $\psi\to e^{i\alpha}\psi$ is the probability current $(\rho,\mathbf J)=\left(|\psi|^2,\frac\hbar{2mi}(\psi^*\nabla\psi-\psi\nabla\psi^*)\right)$ up to an overall constant.
4. Derive $T^{\mu\nu}$ as the Noether current of spacetime translations $\delta\phi=-\epsilon_\nu\partial^\nu\phi$.
5. State what is lost when the surface term at infinity does not vanish.

## Prerequisites

Modules 04, 10, 17, 18.

## Detailed topics (checklist)

**Noether's theorem [Must]**
- Statement with the internal/spacetime distinction and with the surface term handled explicitly (this is where the Module 03 exercise about dropped boundary terms pays off): the variation of the action under a symmetry is a boundary term; the on-shell variation of the action equals $\int\partial_\mu(\dots)d^4x$, which gives $\partial_\mu j^\mu=0$.
- **Mechanics as a special case:** particle mechanics is a field theory in one dimension (time): the conserved quantity $Q=\sum p_j\delta q_j-F$ of Module 04, and the energy function $h$ from time translation.

**Spacetime symmetries [Must]**
- Translations $\to T^{\mu\nu}$ and $P^\mu$; rotations and boosts $\to$ the angular-momentum tensor $M^{\lambda\mu\nu}=x^\mu T^{\lambda\nu}-x^\nu T^{\lambda\mu}$ (plus a spin part for non-scalar fields); the Galilean-boost charge of Module 04 as a limit.

**Internal symmetries [Must]**
- $U(1)$: the complex scalar $\to$ charge current $j^\mu$ and $Q$; $O(N)$ for $N$ real scalars $\to$ currents $j^\mu_{ab}=\phi_a\partial^\mu\phi_b-\phi_b\partial^\mu\phi_a$; the Schrödinger field $\to$ probability conservation.
- **The Noether charge generates the symmetry:** $\{\phi,Q\}\propto\phi$ (up to sign conventions) so $Q$ implements $\phi\to e^{i\alpha}\phi$ through the field bracket; after quantization $e^{i\alpha\hat Q}$ is a unitary implementing the symmetry (Module 10).

**Gauge invariance (13.8) [Must]**
- Making the $U(1)$ symmetry *local*, $\alpha\to\alpha(x)$, forces a gauge field: with $D_\mu=\partial_\mu+iqA_\mu$, the Lagrangian $\mathcal L=(D_\mu\phi)^*(D^\mu\phi)-m^2|\phi|^2$ is invariant under $\phi\to e^{-iq\Lambda}\phi$, $A_\mu\to A_\mu+\partial_\mu\Lambda$; expanding gives $-A_\mu j^\mu+q^2A_\mu A^\mu|\phi|^2$ with $j^\mu=iq(\phi^*\partial^\mu\phi-\phi\partial^\mu\phi^*)$.
- Electromagnetism: $\mathcal L=-\frac14F_{\mu\nu}F^{\mu\nu}-J^\mu A_\mu$ is gauge invariant only if $\partial_\mu J^\mu=0$: gauge invariance *requires* charge conservation.
- Noether's second theorem (awareness): local symmetries yield identities among the field equations rather than new conserved charges (e.g., $\partial_\nu\partial_\mu F^{\mu\nu}=0$).

**Quantum descendants [Awareness]**
- The quantum version of Noether's theorem is a statement about correlation functions (**Ward identities**) rather than a conserved quantity, and it is where symmetries can fail quantum-mechanically (**anomalies**). The classical-to-quantum map for symmetries therefore also has an obstruction, as Bridge 1's Groenewold-van Hove result was an obstruction for observables: the right note to end on.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Goldstein 13.7; derive Noether's theorem for fields with the surface term explicit |
| B1 | Exercises 1 to 3 |
| A2 | Derive $T^{\mu\nu}$ from translations and the $U(1)$ current; link back to Module 04 |
| B2 | Exercises 4 to 6 |
| A3 | Goldstein 13.8 and Jackson 12.7; gauge invariance and minimal coupling |
| B3 | Exercises 7 to 10; **write the deliverable**; cheat sheet |

## Derive from scratch (A sessions, book closed)

1. Noether's theorem for fields with $\delta\mathcal L=\epsilon\,\partial_\mu K^\mu$.
2. $T^{\mu\nu}$ from translations; $P^\mu$ conservation.
3. The $U(1)$ current of the complex scalar and the Schrödinger field.
4. The covariant-derivative construction from local $U(1)$ invariance.
5. Gauge invariance of $\mathcal L_{\rm EM}$ requires $\partial_\mu J^\mu=0$.

## Bare-minimum exercises (with expected results)

1. **Translations:** with $\delta\phi=-\epsilon_\nu\partial^\nu\phi$ and $\delta\mathcal L=-\epsilon_\nu\partial^\nu\mathcal L$ (so $K^\mu=-\epsilon^\mu\mathcal L$) obtain $j^{\mu}{}_{(\nu)}=-T^\mu{}_\nu$-type currents; the conserved quantities are $P^\nu=\int T^{0\nu}d^3x$.
2. **$U(1)$ current:** for the complex scalar show $j^\mu=i(\phi\partial^\mu\phi^*-\phi^*\partial^\mu\phi)$ and verify $\partial_\mu j^\mu=\phi\,\Box\phi^*-\phi^*\Box\phi=0$ on shell (using $\Box\phi=-m^2\phi$). The charge density $j^0=i(\phi\dot\phi^*-\phi^*\dot\phi)$ is *not* positive definite: the origin of the Klein-Gordon interpretation problem.
3. **$O(N)$ symmetry:** for $N$ real scalars with $\mathcal L=\frac12\sum(\partial\phi_a)^2-\frac12m^2\sum\phi_a^2$ show the $N(N-1)/2$ currents $j^\mu_{ab}=\phi_a\partial^\mu\phi_b-\phi_b\partial^\mu\phi_a$ are conserved.
4. **Schrödinger field:** show the current of $\psi\to e^{i\alpha}\psi$ is proportional to $(|\psi|^2,\frac{\hbar}{2mi}(\psi^*\nabla\psi-\psi\nabla\psi^*))$ and that $\partial_t\rho+\nabla\cdot\mathbf J=0$ follows from the Schrödinger equation.
5. **Gauging:** show $D_\mu\phi\to e^{-iq\Lambda}D_\mu\phi$ under $\phi\to e^{-iq\Lambda}\phi$, $A_\mu\to A_\mu+\partial_\mu\Lambda$ for $D_\mu=\partial_\mu+iqA_\mu$, and expand $(D\phi)^*(D\phi)$ to identify the coupling $-A_\mu j^\mu+q^2A^2|\phi|^2$. (Sign conventions differ from $\mathbf p-q\mathbf A$ texts: $D_\mu=\partial_\mu+iqA_\mu$ corresponds to $\mathbf p-q\mathbf A$ with $\mathbf p=-i\nabla$ and signature $+---$.)
6. **Ambiguity:** adding $\partial_\nu B^{\mu\nu}$ with $B^{\mu\nu}$ antisymmetric to $j^\mu$ leaves $\partial_\mu j^\mu=0$ and $Q$ unchanged (for fields falling off at infinity); this is the freedom exploited by the Belinfante improvement.
7. **Mechanics as a special case:** for a particle with $L(q,\dot q)$ and time translation $\delta q=-\epsilon\dot q$ show the Noether charge is $-h=-(p\dot q-L)$; for $q\to q+\epsilon$ it is $p$.
8. **Surface terms:** give an example (a charge density with a flux that does not vanish at infinity, or a conducting boundary) where $\partial_\mu j^\mu=0$ holds locally but $Q$ is not conserved because $\oint\mathbf j\cdot d\mathbf a\neq0$.
9. **The charge generates the symmetry:** for the complex scalar the canonical momenta are $\pi=\partial\mathcal L/\partial\dot\phi=\dot\phi^*$ and $\pi^*=\dot\phi$, with $\{\phi(x),\pi(y)\}=\delta(x-y)$, $\{\phi^*(x),\pi^*(y)\}=\delta(x-y)$ and all other brackets zero. Show that the charge $Q=i\int(\phi^*\pi^*-\phi\pi)\,d^3x$ (the integral of $j^0$) satisfies $\{\phi(x),Q\}=-i\phi(x)$, so $\delta\phi=\epsilon\{\phi,Q\}=-i\epsilon\phi$ is an infinitesimal phase rotation (the sign is tied to the sign convention chosen for $j^\mu$).
10. **Gauge invariance implies current conservation:** under $A_\mu\to A_\mu+\partial_\mu\Lambda$ the interaction term changes by $-J^\mu\partial_\mu\Lambda=-\partial_\mu(J^\mu\Lambda)+\Lambda\,\partial_\mu J^\mu$; the action is invariant iff $\partial_\mu J^\mu=0$.

## The deliverable: `bridge3.md` (3 to 5 pages, your own words)

1. **State Noether's theorem properly**, with the internal/spacetime distinction and the surface term handled explicitly.
2. **Rederive your Module 04 results as corollaries.** Spacetime translation $\to T^{\mu\nu}$ and energy-momentum conservation; rotation $\to$ angular momentum; then the internal $U(1)$ symmetry of a complex scalar field $\to$ the conserved current $j^\mu$.
3. **Assemble the master table.** Combine everything from Bridge Modules 1 and 2:

| Classical mechanics | Field theory | Quantum |
| --- | --- | --- |
| $\{q_i,p_j\}=\delta_{ij}$ | $\{\eta(x),\pi(x')\}=\delta(x-x')$ | $[\hat\eta,\hat\pi]=i\hbar\delta$ |
| $G$ generates a canonical transformation | Noether charge $Q=\int j^0d^3x$ | $\hat U=e^{-i\epsilon\hat G/\hbar}$ |
| $\dot u=\{u,H\}$ | $\dot\eta=\{\eta,H\}$ | Heisenberg equation |
| Normal modes | Field modes | Creation and annihilation operators |
| $\oint p\,dq=nh$ | none | WKB, Bohr-Sommerfeld |
| $S$ (Hamilton's principal function) | $S[\phi]$ | Phase: $e^{iS/\hbar}$; path integral |
| Liouville | none | Unitarity |
| Noether | Noether currents | Ward identities |

4. **One paragraph on the last row.** You do not need to derive Ward identities now: note that the quantum version of Noether's theorem is a statement about correlation functions rather than a conserved quantity, and that this is where symmetry can fail quantum-mechanically (anomalies). Knowing that the classical-to-quantum map for symmetries also has an obstruction is the right note to end on.

**Rubric (2 points each):** statement with surface term; Module 04 results recovered; $U(1)$ current derived; master table complete and correct; the final paragraph.

## Pitfalls

- Forgetting the total-divergence term $K^\mu$ when the Lagrangian changes by a divergence.
- Treating the conserved charge as conserved when the surface term at infinity does not vanish.
- Mixing up sign conventions for $D_\mu$ and the gauge transformation.
- Believing that Noether's theorem gives a conserved charge for a local (gauge) symmetry (it gives identities instead).

## Gate questions

1. State Noether's theorem with the surface term; what is lost if the surface term does not vanish?
2. What is the difference between a spacetime and an internal symmetry in the theorem?
3. Why does gauge invariance of the electromagnetic Lagrangian require $\partial_\mu J^\mu=0$?

## One-page cheat sheet contents

Noether's theorem and $j^\mu$ formula; $T^{\mu\nu}$ from translations; $U(1)$ current; covariant derivative and gauge transformation; the master table.
