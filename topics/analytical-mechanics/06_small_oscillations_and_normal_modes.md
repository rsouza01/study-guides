# Module 06: Small oscillations and normal modes

**Books:** Goldstein 6.1 to 6.4 (6.5 forced and damped oscillations and 6.6 only as a skim); Landau and Lifshitz *Mechanics* sections 21 to 23 (optional); Hand and Finch for worked examples.
**Time:** 2 weeks (four sessions).

## Why this matters for the bridge

Once a system of coupled oscillators is written in **normal coordinates**, it is a set of completely independent one-dimensional oscillators. Take a chain of $N$ masses and let $N\to\infty$ and you have Goldstein 13.1: a field is a continuum of decoupled oscillators, and field quantization is the quantization of each normal mode (creation and annihilation operators are the ladder operators of the modes). If field quantization has ever felt arbitrary, it is usually because this chain of reasoning was never laid out explicitly. Also: simultaneous diagonalization of $T$ and $V$ is the same move as diagonalizing a Hamiltonian in quantum mechanics.

## Skip-test (40 minutes, no notes)

1. Expand $T$ and $V$ about a stable equilibrium to quadratic order, $T=\frac12\dot\eta^TM\dot\eta$, $V=\frac12\eta^TK\eta$, and derive the eigenproblem $(K-\omega^2M)\mathbf a=0$.
2. Show that eigenvectors of distinct frequencies satisfy $\mathbf a^TM\mathbf a'=0$ (orthogonality with respect to the mass matrix, not the identity).
3. Define normal coordinates $\zeta=A^{-1}\eta$ and show $L=\frac12\sum(\dot\zeta_n^2-\omega_n^2\zeta_n^2)$.
4. Solve the linear triatomic molecule (masses $m,M,m$ with springs $k$): frequencies $0$, $\sqrt{k/m}$ and $\sqrt{\frac km\left(1+\frac{2m}{M}\right)}$.
5. For $N$ equal masses on a string with fixed ends obtain $\omega_n=2\sqrt{k/m}\sin\frac{n\pi}{2(N+1)}$.

## Prerequisites

Modules 01, 02.

## Detailed topics (checklist)

**Formulation (6.1) [Must]**
- Equilibrium, expansion of $V$ to second order, positive definiteness of $K$ for stability, kinetic energy $T=\frac12T_{ij}\dot\eta_i\dot\eta_j$ evaluated at equilibrium (so $T_{ij}$ is constant).

**The eigenvalue problem (6.2 to 6.3) [Must]**
- Characteristic equation $\det(K-\omega^2M)=0$; real positive $\omega^2$; orthogonality and normalization $\mathbf a_n^TM\mathbf a_m=\delta_{nm}$; the modal matrix $A$ and normal coordinates; **the problem reduces to $n$ independent oscillators**; the general solution as a superposition of modes with amplitudes and phases.
- **Degeneracy and symmetry:** degenerate frequencies come from symmetries; any combination of degenerate modes is a mode (the classical analogue of degenerate eigenspaces).
- **Zero modes:** $\omega=0$ corresponds to a symmetry direction (e.g. translation of a free molecule); they give linear-in-time motion rather than oscillation.

**Examples (6.4) [Must]**
- Coupled pendulums; the linear triatomic molecule (symmetric and antisymmetric stretching modes, plus the translation zero mode); the loaded string.

**The loaded string and the continuum limit [Must]**
- $N$ masses $m$ coupled by springs $k$ with fixed ends: $\omega_n=2\sqrt{k/m}\sin\frac{n\pi}{2(N+1)}$, mode shapes $a_j^{(n)}\propto\sin\frac{nj\pi}{N+1}$. As the lattice spacing $a\to0$ with $m/a=\mu$ and $ka=Y$ fixed: $\omega=ck$ with $c=\sqrt{Y/\mu}$. *Keep these results; Module 17 takes the full continuum limit.*

**Forced and damped oscillations (6.5) [Could]**
- Resonance, the response function, Q factor, normal-mode decomposition of a driving force.

**Quantum remark**
- Each normal mode is a quantum oscillator: $H=\sum_n\hbar\omega_n(a_n^\dagger a_n+\frac12)$; phonons are its quanta. (This is the content of the Debye model of the thermodynamics guide.)

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Goldstein 6.1 to 6.2; derive the eigenproblem and orthogonality |
| B1 | Exercises 1 to 4 |
| A2 | Goldstein 6.3 to 6.4; derive the normal-coordinate Lagrangian |
| B2 | Exercises 5 to 10; cheat sheet |

## Derive from scratch (A sessions, book closed)

1. The eigenproblem $(K-\omega^2M)\mathbf a=0$ from the Lagrangian.
2. Orthogonality with respect to $M$ for distinct frequencies, and why $\omega^2$ is real.
3. $L$ in normal coordinates.
4. The loaded-string dispersion relation $\omega_n=2\sqrt{k/m}\sin\frac{n\pi}{2(N+1)}$.
5. The continuum limit of the dispersion relation, $\omega=ck$.

## Bare-minimum exercises (with expected results)

1. **Two coupled pendulums** (equal lengths $\ell$, masses $m$, coupling spring $k$): $\omega_1^2=\frac g\ell$ (in phase), $\omega_2^2=\frac g\ell+\frac{2k}{m}$ (out of phase).
2. **Double pendulum** (from Module 02): $\omega^2=(2\pm\sqrt2)\frac g\ell$; the eigenvectors are $(1,\pm\sqrt2)$-type with respect to the mass matrix; check orthogonality with respect to $M$, *not* the identity.
3. **Linear triatomic molecule:** frequencies $0,\sqrt{k/m},\sqrt{\frac km(1+2m/M)}$; draw the modes; the zero mode is the centre-of-mass translation, a symmetry direction.
4. **Orthogonality check:** for exercise 3 verify $\mathbf a_i^TM\mathbf a_j=0$ numerically.
5. **Loaded string, $N=3$:** $\omega_n=2\sqrt{k/m}\sin\frac{n\pi}{8}$ gives $0.765,\ 1.414,\ 1.848$ in units of $\sqrt{k/m}$; mode shapes $(1,\sqrt2,1)$, $(1,0,-1)$, $(1,-\sqrt2,1)$ up to normalization.
6. **Continuum limit:** with lattice spacing $a$ show $\omega=2\sqrt{k/m}\left|\sin\frac{qa}{2}\right|\to\sqrt{\frac{ka^2}{m}}\,|q|$ for $qa\ll1$, so $c=a\sqrt{k/m}$; check the dispersion curve bends over at the zone edge $q=\pi/a$ (maximum frequency $2\sqrt{k/m}$).
7. **Normal-coordinate Hamiltonian:** for the two-pendulum problem show $H=\sum_n\frac12(P_n^2+\omega_n^2Q_n^2)$ and that $P_n,Q_n$ are canonical conjugates ($\{Q_n,P_m\}=\delta_{nm}$).
8. **Degeneracy from symmetry:** two identical uncoupled pendulums have a degenerate frequency $\omega=\sqrt{g/\ell}$ and any linear combination of the two modes is again a mode; relate to the $SO(2)$ rotation of the $(x_1,x_2)$ plane.
9. **Forced oscillation:** drive the loaded string at one end with frequency $\Omega$; show the response has resonant peaks at each $\omega_n$; sketch for $N=3$.
10. **Zero-point energy of the chain:** with the quantum remark, the ground-state energy of the $N$-chain is $\frac\hbar2\sum_n\omega_n$; evaluate it numerically for $N=3,10,100$ and note that it diverges as $N\to\infty$ (the continuum limit needs a cutoff; this is the first appearance of an ultraviolet divergence).

## Optional extension

Compute the normal modes of a periodic ring of $N$ masses (periodic boundary conditions) and show the modes are plane waves $e^{iqj}$ with $q=2\pi n/N$; the translation symmetry of the ring is why plane waves diagonalize the problem (Bloch's theorem).

## Pitfalls

- Using the identity matrix instead of the mass matrix in orthogonality.
- Dropping zero modes or treating them as oscillations.
- Expanding the kinetic energy to higher order (only the equilibrium value of $T_{ij}$ is needed at quadratic order).
- Assuming that a stable equilibrium needs $V''>0$ for every direction only along the coordinate axes (it needs $K$ positive definite).

## Gate questions

1. Why does the problem decouple into independent oscillators?
2. Why is a zero mode a statement about symmetry?
3. How does the loaded string become a field, and what replaces the discrete index?

## One-page cheat sheet contents

Eigenproblem and orthogonality; normal coordinates; triatomic frequencies; loaded-string dispersion and continuum limit; the quantum remark.
