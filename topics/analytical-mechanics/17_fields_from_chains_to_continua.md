# Module 17: Fields, from chains to continua (★★)

**Books:** Goldstein 13.1 (the transition from a discrete to a continuous system), 13.2 (the Lagrangian formulation for continuous systems and fields), 13.4 (the Hamiltonian formulation: canonical momenta and the field Hamiltonian); Landau and Lifshitz *Classical Theory of Fields* (the field-theory chapters, optional); your thermodynamics and QM guides for the quantum side.
**Time:** 2 weeks (four sessions).

## Why this matters for the bridge

Take the loaded string of Module 06, let $N\to\infty$ and the lattice spacing $a\to0$ with the density fixed. The discrete index $i$ becomes a continuous label $x$; $q_i(t)$ becomes a field $\eta(x,t)$; the sum becomes an integral; $L$ becomes $\int\mathcal L\,dx$ with $\mathcal L$ a *density* depending on $\eta,\dot\eta,\partial_x\eta$; and the Euler-Lagrange equations become a PDE. Since each normal mode is an independent oscillator, **a field is an infinite set of decoupled oscillators**. This is not a slogan but a theorem, and it is the entire conceptual content of field quantization: the creation and annihilation operators are the normal-mode ladder operators. This module also gives the **field Poisson bracket** $\{\eta(x),\pi(x')\}=\delta(x-x')$, the classical statement that becomes the equal-time commutator in canonical field quantization. Note the delta function where Module 09 had a Kronecker delta: that replacement *is* the discrete-to-continuum step.

## Skip-test (40 minutes, no notes)

1. Write the Lagrangian of a chain of masses $m$ with springs $k$ and take the limit $a\to0$ with $\mu=m/a$ and $Y=ka$ fixed to get $\mathcal L=\frac12\mu\dot\eta^2-\frac12Y\eta'^2$.
2. Derive the field Euler-Lagrange equation $\frac{\partial}{\partial t}\frac{\partial\mathcal L}{\partial\dot\eta}+\frac{\partial}{\partial x}\frac{\partial\mathcal L}{\partial\eta'}-\frac{\partial\mathcal L}{\partial\eta}=0$ and obtain the wave equation with $c^2=Y/\mu$.
3. Define $\pi=\partial\mathcal L/\partial\dot\eta$ and $\mathcal H=\pi\dot\eta-\mathcal L$; write $H=\int\mathcal H\,dx$.
4. Write the field Poisson bracket $\{\eta(x),\pi(x')\}=\delta(x-x')$ and show it implies $\dot\eta=\{\eta,H\}=\pi/\mu$.
5. Show that for a string of length $L$ with fixed ends $\eta=\sum_nq_n(t)\sqrt{2/L}\sin\frac{n\pi x}{L}$ gives $L=\sum_n\frac\mu2(\dot q_n^2-\omega_n^2q_n^2)$ with $\omega_n=n\pi c/L$.

## Prerequisites

Modules 03, 06, 07, 09.

## Detailed topics (checklist)

**From discrete to continuous (13.1) [Must]**
- The loaded string: $L=\sum_i\left[\frac12m\dot\eta_i^2-\frac12k(\eta_{i+1}-\eta_i)^2\right]$; $a\to0$: $\eta_i(t)\to\eta(x,t)$, $\sum_ia\to\int dx$, $\frac{\eta_{i+1}-\eta_i}{a}\to\eta'$; $\mu=m/a$, $Y=ka$; the discrete dispersion $\omega=2\sqrt{k/m}\left|\sin\frac{qa}{2}\right|\to c|q|$ (Module 06).

**Lagrangian formulation for fields (13.2) [Must]**
- Action $S=\int\mathcal L(\eta,\partial_\mu\eta,x,t)\,dx\,dt$; Hamilton's principle with fields fixed on the boundary; **Euler-Lagrange equations for fields** $\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\eta)}-\frac{\partial\mathcal L}{\partial\eta}=0$; several fields; the Lagrangian density in 3D.
- Standard Lagrangian densities: the wave equation, the Klein-Gordon field $\mathcal L=\frac12\left[(\partial_t\phi)^2-c^2(\nabla\phi)^2-m^2c^4\phi^2/\hbar^2\right]$ (units $\hbar=c=1$: $\frac12(\partial_\mu\phi\partial^\mu\phi-m^2\phi^2)$), the **Schrödinger field** $\mathcal L=i\hbar\psi^*\dot\psi-\frac{\hbar^2}{2m}\nabla\psi^*\cdot\nabla\psi-V\psi^*\psi$ (varying $\psi$ and $\psi^*$ independently gives the Schrödinger equation: the wavefunction as a classical field).

**Hamiltonian formulation (13.4) [Must]**
- Canonical momentum density $\pi=\partial\mathcal L/\partial\dot\eta$; Hamiltonian density $\mathcal H=\pi\dot\eta-\mathcal L$; **functional derivatives**: $\dot\eta=\frac{\delta H}{\delta\pi}$, $\dot\pi=-\frac{\delta H}{\delta\eta}$; the field Poisson bracket $\{F,G\}=\int dx\left(\frac{\delta F}{\delta\eta}\frac{\delta G}{\delta\pi}-\frac{\delta F}{\delta\pi}\frac{\delta G}{\delta\eta}\right)$; $\{\eta(x),\pi(x')\}=\delta(x-x')$.
- **Normal modes of a field:** Fourier expansion; $H=\sum_n\frac12(P_n^2+\omega_n^2Q_n^2)$ (per unit mass normalization): an infinite set of decoupled oscillators.

**The quantum remark [Must, awareness]**
- Replace $\{,\}\to\frac1{i\hbar}[,]$: $[\hat\eta(x),\hat\pi(x')]=i\hbar\delta(x-x')$; expand in modes and use ladder operators $\hat a_n,\hat a_n^\dagger$; $H=\sum\hbar\omega_n(\hat a_n^\dagger\hat a_n+\frac12)$; the zero-point energy $\frac\hbar2\sum\omega_n$ diverges (ultraviolet divergence; the origin of normal ordering and renormalization).
- The Schrödinger field: $\pi=i\hbar\psi^*$, so $\{\psi(x),\psi^*(x')\}=-\frac i\hbar\delta(x-x')$ and after quantization $[\hat\psi(x),\hat\psi^\dagger(x')]=\delta(x-x')$: second quantization.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Goldstein 13.1; redo the continuum limit of your Module 06 chain |
| B1 | Exercises 1 to 4 |
| A2 | Goldstein 13.2; derive the field Euler-Lagrange equation |
| B2 | Exercises 5 to 7 |
| A3 | Goldstein 13.4; derive the field Poisson bracket and $\dot\eta=\{\eta,H\}$ |
| B3 | Exercises 8 to 10; cheat sheet |

## Derive from scratch (A sessions, book closed)

1. The continuum limit of the loaded-string Lagrangian.
2. The field Euler-Lagrange equation from $\delta S=0$ (with the boundary term identified).
3. $\mathcal H$, and the field Hamilton equations.
4. The mode decomposition of the string and $H=\sum\frac12(P_n^2+\omega_n^2Q_n^2)$.
5. The Schrödinger equation from the field Lagrangian $i\hbar\psi^*\dot\psi-\frac{\hbar^2}{2m}|\nabla\psi|^2-V|\psi|^2$.

## Bare-minimum exercises (with expected results)

1. **Continuum limit:** from the chain Lagrangian show $\mathcal L=\frac12\mu\dot\eta^2-\frac12Y\eta'^2$ with $\mu=m/a$, $Y=ka$; the Euler-Lagrange equation $\mu\ddot\eta=Y\eta''$ is the wave equation with $c^2=Y/\mu=ka^2/m$ (matches Module 06).
2. **Dispersion:** show that the discrete dispersion $\omega=2\sqrt{k/m}|\sin\frac{qa}{2}|$ reduces to $\omega=cq$ for $qa\ll1$ and that deviations begin at $O(q^3a^3)$.
3. **Hamiltonian density:** for the string $\pi=\mu\dot\eta$, $\mathcal H=\frac{\pi^2}{2\mu}+\frac12Y\eta'^2$; $E=\int\mathcal H\,dx$; check that a travelling wave $\eta=f(x-ct)$ has equal kinetic and potential energy densities.
4. **Mode expansion:** with fixed ends $\eta(0)=\eta(L)=0$ show $\omega_n=\frac{n\pi c}{L}$ and compare with the $N\to\infty$ limit of $\omega_n=2\sqrt{k/m}\sin\frac{n\pi}{2(N+1)}$ from Module 06.
5. **Klein-Gordon:** with $\mathcal L=\frac12(\partial_\mu\phi\partial^\mu\phi-m^2\phi^2)$ ($\hbar=c=1$, signature $+---$) derive $(\Box+m^2)\phi=0$ and the dispersion relation $\omega^2=k^2+m^2$.
6. **Schrödinger field:** treat $\psi$ and $\psi^*$ as independent in $\mathcal L=i\hbar\psi^*\dot\psi-\frac{\hbar^2}{2m}|\nabla\psi|^2-V|\psi|^2$; the variation with respect to $\psi^*$ gives $i\hbar\dot\psi=-\frac{\hbar^2}{2m}\nabla^2\psi+V\psi$.
7. **Functional derivatives:** for $F[\phi]=\int\frac12(\nabla\phi)^2d^3x$ show $\frac{\delta F}{\delta\phi}=-\nabla^2\phi$; for $F[\phi]=\int V(\phi)\,d^3x$ show $\frac{\delta F}{\delta\phi}=V'(\phi)$.
8. **Field brackets and dynamics:** with $H=\int\mathcal H\,dx$ and $\{\eta(x),\pi(x')\}=\delta(x-x')$ verify $\dot\eta=\{\eta,H\}=\pi/\mu$ and $\dot\pi=\{\pi,H\}=Y\eta''$.
9. **Second-quantization bracket:** for the Schrödinger field, $\pi=\partial\mathcal L/\partial\dot\psi=i\hbar\psi^*$; show $\{\psi(x),\psi^*(x')\}=-\frac i\hbar\delta(x-x')$ and that $\frac{1}{i\hbar}[\,,]$-style quantization gives $[\hat\psi,\hat\psi^\dagger]=\delta$.
10. **Zero-point energy:** the ground-state energy of the string is $\frac\hbar2\sum_n\omega_n=\frac{\pi\hbar c}{2L}\sum_nn$; this diverges. (Regularizing by analytic continuation $\sum n=-\frac1{12}$ gives $-\frac{\pi\hbar c}{24L}$, the 1D Casimir energy. Note that the *dependence on $L$* is physical even though the total is infinite.)

## Optional extension

Quantize a free scalar field in a box: write $\hat\phi=\sum_k\frac{1}{\sqrt{2\omega_kV}}(\hat a_ke^{ikx}+\hat a_k^\dagger e^{-ikx})$ and verify the equal-time commutator $[\hat\phi(x),\hat\pi(x')]=i\delta(x-x')$ from $[\hat a_k,\hat a_{k'}^\dagger]=\delta_{kk'}$.

## Pitfalls

- Confusing the field index $x$ with a dynamical variable (it is a label, like $i$).
- Treating $\psi$ and $\psi^*$ as dependent in the Schrödinger Lagrangian.
- Forgetting the boundary term at the spatial boundary in the field Euler-Lagrange derivation.
- Believing that a continuum field has finitely many degrees of freedom per point of space (it has infinitely many in total, and UV divergences follow).

## Gate questions

1. Why is "a field is an infinite set of decoupled oscillators" a theorem and not a slogan?
2. What replaces the Kronecker delta in the Poisson bracket when going to the continuum?
3. Why does the zero-point energy diverge, and what remains physical?

## One-page cheat sheet contents

Chain-to-string limit; field Euler-Lagrange equation; $\mathcal H$ and the field brackets; mode decomposition; Klein-Gordon and Schrödinger Lagrangians.
