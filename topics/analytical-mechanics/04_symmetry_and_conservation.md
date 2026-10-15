# Module 04: Symmetry and conservation laws

**Books:** Goldstein 2.6 to 2.7; Landau and Lifshitz *Mechanics* sections 1 to 10 (about 30 pages, **essential**); Hand and Finch for extra examples.
**Time:** 2 weeks (four sessions). The most important module of Phase I.

## Why this matters for the bridge

Goldstein presents cyclic coordinates and conserved momenta as a computational convenience. They are not. They are **Noether's theorem in its simplest guise**: a symmetry of $L$ implies a conserved quantity. Modules 10 and 19 return to this with the full machinery (generators and Noether currents). Landau and Lifshitz build the entire Lagrangian *from* the symmetries of spacetime (homogeneity of space and time, isotropy of space, Galilean relativity); reading those thirty pages reframes everything downstream.

## Skip-test (40 minutes, no notes)

1. State the three correspondences: homogeneity of space $\to$ momentum, isotropy $\to$ angular momentum, homogeneity of time $\to$ energy.
2. Show that if $L$ is invariant under $q\to q+\epsilon\,\delta q$ then $\sum_jp_j\,\delta q_j$ is conserved.
3. Define the energy function $h=\sum\dot q_j\frac{\partial L}{\partial\dot q_j}-L$, prove $\frac{dh}{dt}=-\frac{\partial L}{\partial t}$, and state three conditions under which $h=E=T+V$.
4. Give an example in which $h$ is conserved but $h\ne E$.
5. Derive the conserved quantity associated with a Galilean boost for a free particle system.

## Prerequisites

Modules 02, 03.

## Detailed topics (checklist)

**Cyclic coordinates and generalized momenta (2.6) [Must]**
- $p_j=\partial L/\partial\dot q_j$; a cyclic coordinate gives $p_j=$ const; examples: translations (linear momentum), rotations (angular momentum).
- **Symmetry as invariance of $L$:** under an infinitesimal transformation $q_j\to q_j+\epsilon\,\delta q_j$, if $\delta L=\epsilon\frac{dF}{dt}$ then $Q=\sum p_j\delta q_j-F$ is conserved (the mechanical Noether theorem). Contrast with "looking for the cyclic coordinate": the symmetry argument works without choosing coordinates in advance.
- Conservation of the centre-of-mass motion; Galilean boost symmetry and its conserved quantity $\mathbf K=M\mathbf R-\mathbf Pt$.

**The energy function (2.7) [Must]**
- $h=\sum\dot q\partial L/\partial\dot q-L$; $\frac{dh}{dt}=-\partial L/\partial t$.
- $h=E$ requires (1) the transformation $\mathbf r_i(q)$ to be time-independent, (2) $V$ velocity-independent; $h$ is conserved when $L$ has no explicit time dependence. The two statements are independent and fail in interesting cases (rotating frames, time-dependent constraints).

**Landau and Lifshitz sections 1 to 10 [Must]**
- Why the free-particle Lagrangian is $\frac12mv^2$ (Galilean relativity), Lagrangian of a system of particles, conservation laws from the homogeneity and isotropy, mechanical similarity (scaling) and the virial theorem.

**Scaling symmetries and the virial theorem [Should]**
- For $V\propto r^n$ the scaling $\mathbf r\to\lambda\mathbf r$, $t\to\lambda^{1-n/2}t$ leaves the equations invariant (mechanical similarity); virial theorem $2\langle T\rangle=n\langle V\rangle$.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Landau and Lifshitz sections 1 to 4 (free-particle Lagrangian from Galilean relativity); derive $h$ and $dh/dt$ |
| B1 | Exercises 1 to 4 |
| A2 | Goldstein 2.6 to 2.7; Landau and Lifshitz sections 5 to 10 (conservation laws, similarity) |
| B2 | Exercises 5 to 10; cheat sheet |

## Derive from scratch (A sessions, book closed)

1. The free-particle Lagrangian from homogeneity, isotropy and Galilean relativity (Landau's argument).
2. The conserved quantity $\sum p_j\delta q_j-F$ for an invariant (up to a total derivative) $L$.
3. $\frac{dh}{dt}=-\frac{\partial L}{\partial t}$ and the conditions for $h=E$.
4. Angular momentum conservation for an isotropic potential, constructed from the invariance of $L$ under rotations.
5. The Galilean-boost conserved quantity and its interpretation (centre of mass).

## Bare-minimum exercises (with expected results)

1. **Cyclic coordinate:** for a particle in a central potential in polar coordinates, $\phi$ is cyclic and $p_\phi=mr^2\dot\phi=L_z$.
2. **Rotation symmetry directly:** apply $\delta x=-\epsilon y$, $\delta y=\epsilon x$ to $L=\frac12m(\dot x^2+\dot y^2)-V(x^2+y^2)$; $\delta L=0$ and the conserved quantity is $p_x\delta x/\epsilon+p_y\delta y/\epsilon=xp_y-yp_x$.
3. **Galilean boost:** for a free particle $L=\frac12m\dot x^2$ under $\delta x=\epsilon t$ one finds $\delta L=\epsilon\frac{d}{dt}(mx)$; the conserved quantity is $m\dot xt-mx=$ const, i.e. $x(t)-vt=$ const. For $N$ particles it is $M\mathbf R-\mathbf Pt$.
4. **Energy function not equal to the energy:** for the bead on the rotating hoop of Module 02, $h=\frac12mR^2\dot\theta^2-\frac12mR^2\Omega^2\sin^2\theta-mgR\cos\theta$ is conserved but $E=T+V=\frac12mR^2(\dot\theta^2+\Omega^2\sin^2\theta)-mgR\cos\theta\ne h$ (and $E$ is not conserved).
5. **Explicit time dependence:** for $L=\frac12m\dot x^2-\frac12kx^2\,e^{-\alpha t}$ show $dh/dt=-\partial L/\partial t\ne0$.
6. **Partial symmetry:** for $L=\frac12m\dot{\mathbf r}^2-mgz$ identify the conserved $p_x,p_y$ and show $p_z$ is not conserved; recover the energy $h=E$.
7. **Helical symmetry:** for a potential depending on $z$ and $\phi$ only through $\phi-kz$, the transformation $\delta\phi=\epsilon$, $\delta z=\epsilon/k$ leaves $\phi-kz$ unchanged, so $p_\phi+p_z/k$ is conserved (while $p_\phi$ and $p_z$ separately are not).
8. **Virial theorem:** for a bounded orbit in $V=-k/r$ show $\langle T\rangle=-\frac12\langle V\rangle$ by averaging $\frac{d}{dt}(\mathbf r\cdot\mathbf p)$.
9. **Magnetic field, symmetric gauge:** for a charged particle in $\mathbf B=B\hat z$ with $\mathbf A=\frac B2(-y,x,0)$ the Lagrangian is rotation invariant; the conserved canonical angular momentum is $p_\phi=m\rho^2\dot\phi+\frac{qB}{2}\rho^2$. Compare with the mechanical angular momentum $m\rho^2\dot\phi$, which is not conserved.
10. **Ambiguity of the charge:** adding $\frac{dF}{dt}$ to $L$ changes the Noether charge by a function of $q,t$ only (it does not change which quantity is conserved up to such shifts); verify for $L\to L+\frac d{dt}(\alpha x)$ with $x$ translation symmetry.

## Optional extension

Show that for $V\propto r^{-2}$ the quantity $D=\mathbf r\cdot\mathbf p-2Ht$ is conserved (a dilation symmetry); this is the classical shadow of the conformal symmetry of the inverse-square potential.

## Pitfalls

- Equating $h$ with $E$ without checking the two conditions.
- Concluding that a quantity is conserved because it looks like a momentum (check the symmetry).
- Forgetting the total-derivative term $F$ in the conserved quantity.
- Mixing up kinetic and canonical angular momentum in a magnetic field.

## Gate questions

1. Which symmetry gives energy conservation, and which condition makes $h=E$?
2. Why does Galilean boost invariance give a conserved quantity even though $L$ is only quasi-invariant?
3. Why is "find a cyclic coordinate" weaker than "find a symmetry"?

## One-page cheat sheet contents

Symmetry $\to$ conserved quantity formula; $h$ and $dh/dt$; the three $h=E$ conditions; Galilean boost charge; scaling and virial theorem.
