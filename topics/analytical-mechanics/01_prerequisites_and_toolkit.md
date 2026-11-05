# Module 01: Prerequisites and toolkit

**Books:** Stewart *Calculus*, 8th edition (sections 9.2, 14.3, 14.5, 14.8, 15.3, 15.9, 17.1, 17.3); Boas *Mathematical Methods in the Physical Sciences*, chapters 3 and 4; Goldstein 1.1 to 1.2 (pp. 1 to 11).
**Time:** 8 sessions if nothing is rusty, up to 12 if the skip-test exposes gaps. The schedule is a queue: a long Module 01 costs nothing.
**Verification status:** Stewart and Goldstein section numbers are checked against the tables of contents. Boas section numbers are from the 3rd edition as recalled: confirm them against your copy and correct this file if they differ. Book problem numbers are not pinned yet (see the end of the sniper map).

## Task 0: reading map (done)

`notes/goldstein_map.md` already holds the Goldstein reading map for the whole guide. Copy it into your `notes/` folder and fill in its "Worked examples?" column as you open each section.

## Why this matters for the bridge

The material is mostly review, but three skills decide whether later modules feel smooth.

1. **Partial derivatives with a clear head about which variables are held fixed.** The Legendre transformation (Module 07) and canonical transformations (Module 08) are all about this.
2. **Diagonalizing symmetric matrices.** Normal modes (Module 06) and, later, Hamiltonians.
3. **A small numerical integrator.** It lets you check a result and see why symplectic integrators matter (Modules 07 to 09).

## Skip-test (40 minutes, no notes)

Run this first. Log every item you miss: those items, and only those, set how much time the rest of the module needs.

1. Diagonalize $`\begin{pmatrix}2&-1\\-1&2\end{pmatrix}`$; give eigenvalues, orthonormal eigenvectors, and show that the eigenvectors of a real symmetric matrix with distinct eigenvalues are orthogonal.
2. Solve $\ddot x+\omega^2x=0$ and $\ddot x+2\gamma\dot x+\omega^2x=0$ (underdamped case) with initial conditions $x(0)=x_0$, $\dot x(0)=0$.
3. Prove $\epsilon_{ijk}\epsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}$ and use it to derive $\mathbf a\times(\mathbf b\times\mathbf c)=\mathbf b(\mathbf a\cdot\mathbf c)-\mathbf c(\mathbf a\cdot\mathbf b)$.
4. Use a Lagrange multiplier to find the point on $x^2+y^2=1$ closest to $(2,1)$.
5. Expand a one-dimensional potential $V(x)$ about a minimum $x_0$ to quadratic order and identify the small-oscillation frequency $\omega^2=V''(x_0)/m$.

| Item you missed | Go to |
| --- | --- |
| 1 | Block E (spectral theorem) |
| 2 | Block D (oscillator) |
| 3 | Block F (index notation) |
| 4 | Block C (Lagrange multipliers) |
| 5 | Block B (Taylor in several variables) |

## Prerequisites

Single and multivariable calculus, basic linear algebra, basic Python. Nothing else.

## Sniper map: what to read, what to do

For every topic: the exact reading, the exercises from this file to do, and the group of book problems to pair with them.

Legend. **Do** refers to this file's *Derive from scratch* (D1 to D5) and *Bare-minimum exercises* (E1 to E10), both below. **Book problems** names the group of problems to pair with them; exact numbers are pending your exercise pages.

### Block A: partial derivatives and the chain rule (what is held fixed)

| Topic | Read | Do | Book problems |
| --- | --- | --- | --- |
| Partial derivatives, higher derivatives | Stewart 14.3 | | 14.3: a few mixed-partial problems (confirm Clairaut's theorem) |
| Chain rule with a final variable $t$ | Stewart 14.5 | D1, E1 | 14.5: chain-rule problems where all variables depend on $t$. This is exactly $\frac{d}{dt}f(q,\dot q,t)$ |
| "Which variable is held fixed" | Boas 4.1 (notation), 4.6 (implicit differentiation), 4.7 (more chain rule) | Gate question 1 | Boas 4.6: problems written with $`\left(\frac{\partial u}{\partial x}\right)_y`$ notation |
| Jacobians | Stewart 15.9 | none now; Modules 08 to 10 use it | 15.9: the first few "find the Jacobian" problems |

**Payoff, to be done in Module 02 and noted here:** Goldstein 1.4 uses $\partial\dot r_i/\partial\dot q_j=\partial r_i/\partial q_j$ and $\frac{d}{dt}\frac{\partial r_i}{\partial q_j}=\frac{\partial\dot r_i}{\partial q_j}$. If D1 is clear, both lemmas are two lines.

### Block B: Taylor series and exact differentials

| Topic | Read | Do | Book problems |
| --- | --- | --- | --- |
| Taylor series in several variables | Boas 4.2 (power series in two variables) | skip-test item 5 | Boas 4.2: expand a function of two variables to second order |
| Exact differentials | Boas 4.3 (total differentials). You already did Stewart 16.3 in the EM prelude: the test is $P_y=Q_x$ | none | none |

### Block C: Lagrange multipliers

| Topic | Read | Do | Book problems |
| --- | --- | --- | --- |
| Constrained extrema | Stewart 14.8 (read the tangent-gradient argument) | skip-test item 4, E5, D5 | 14.8: two-variable problems with one constraint |
| Gaussian integral | Stewart 15.3 (the $\sqrt\pi$ example in polar coordinates) | none | none |
| Delta function as a limit | Griffiths 1.5. EM Module 02 covers it: do it there, not twice | none | |

### Block D: the oscillator

| Topic | Read | Do | Book problems |
| --- | --- | --- | --- |
| Second-order linear equations with constant coefficients | Stewart 17.1 (the auxiliary equation and its three cases) | skip-test item 2, D4, E6 | 17.1: homogeneous problems with initial conditions |
| Damped and driven vibrations | Stewart 17.3 (springs: simple, damped, forced) | E6 | 17.3: damped-spring problems |
| Q factor and resonance, in full | Goldstein 6.5 (p. 258), in Module 06 | none now | none |
| Phase portraits | Goldstein 3.3 (p. 76) for the effective-potential picture | E10 | none |

### Block E: linear algebra

| Topic | Read | Do | Book problems |
| --- | --- | --- | --- |
| Special matrices (orthogonal, Hermitian) | Boas 3.9 | | Boas 3.9: a few "is it orthogonal or unitary?" problems |
| Eigenvalues and eigenvectors; symmetric matrices | Boas 3.11 | skip-test item 1, E2, D2 | Boas 3.11: $2\times2$ and $3\times3$ symmetric matrices |
| Diagonalization and quadratic forms | Boas 3.12 | E3 | Boas 3.12: diagonalizing a quadratic form |
| Matrix exponential | no text needed; Goldstein 4.8 returns to it in Module 12 | E7 | none |
| Commutators $[A,B]=AB-BA$ | nothing to read | | none |

### Block F: index notation

| Topic | Read | Do | Book problems |
| --- | --- | --- | --- |
| Einstein summation, $\delta_{ij}$, $\epsilon_{ijk}$ | EM Module 02 (same material). Do it once, in whichever guide comes first | skip-test item 3, E4 | the identities in the exercises below |

### Block G: the Newtonian refresher and numerics

| Topic | Read | Do | Book problems |
| --- | --- | --- | --- |
| Momentum, angular momentum and energy theorems | Goldstein 1.1 to 1.2 (pp. 1 to 11) | D3 | none |
| Euler's method | Stewart 9.2 | E8 (first half) | none |
| Velocity Verlet (leapfrog) | no text; use the algorithm in the Optional extension | E8, E9 | none |

**Filling in the book problems.** Send the exercise pages for Stewart 14.3, 14.5, 14.8, 15.9, 17.1 and 17.3 and for Boas 3.9, 3.11, 3.12 and 4.1 to 4.7. Each "Book problems" cell then becomes six to eight problems with a reason for each.

## Reading plan (8 core sessions, 4 spare)

Each session is about 2 hours. After every session, tick the boxes below.

| Session | Task |
| --- | --- |
| 1 | Copy `goldstein_map.md` into `notes/`; the skip-test; log what you missed; Goldstein 1.1 to 1.2 |
| 2 | Block A: Stewart 14.3, 14.5, Boas 4.1, 4.6, 4.7; D1; E1 |
| 3 | Blocks B and C: Boas 4.2, 4.3, Stewart 14.8, 15.3; D5; E5 |
| 4 | Block D: Stewart 17.1, 17.3; D4; E6 |
| 5 | Block E: Boas 3.9, 3.11, 3.12; D2; E2, E3 |
| 6 | Block F and the rest of E: D3; E4, E7 |
| 7 | Block G: Stewart 9.2; E8, E9 |
| 8 | E10; the optional extension; the cheat sheet; the gate questions |
| 9 to 12 | Spare: redo whatever the skip-test or the exercises exposed |

## Progress

- [ ] Session 1: skip-test done, misses logged
- [ ] Session 2: Block A
- [ ] Session 3: Blocks B and C
- [ ] Session 4: Block D
- [ ] Session 5: Block E
- [ ] Session 6: Blocks F and E (rest)
- [ ] Session 7: Block G
- [ ] Session 8: pendulum, cheat sheet, gate questions

## Detailed topics (checklist)

**Calculus (Must)**
- Partial derivatives and the chain rule; total versus partial time derivative $\frac{d}{dt}f(q,\dot q,t)=\frac{\partial f}{\partial t}+\dot q\frac{\partial f}{\partial q}+\ddot q\frac{\partial f}{\partial\dot q}$; implicit differentiation and Jacobians; Taylor series in several variables; exact differentials. *(Blocks A and B)*
- Lagrange multipliers for constrained extrema (the finite-dimensional ancestor of constraint forces). *(Block C)*
- Gaussian integrals and the delta function as a limit (used in later modules). *(Block C)*

**Differential equations (Must)**
- Linear second-order equations with constant coefficients; the harmonic oscillator, damped and driven; complex exponentials $e^{i\omega t}$; resonance and Q factor. *(Block D)*
- Phase portraits: reading $(x,\dot x)$ plots for the oscillator and the pendulum. *(Block D)*

**Linear algebra (Must)**
- Real symmetric matrices and the spectral theorem; simultaneous diagonalization of a quadratic form pair (the small-oscillation eigenproblem); orthogonal matrices and rotations; matrix exponential $e^{A}$ and $e^{\epsilon A}\approx1+\epsilon A$; commutators $[A,B]=AB-BA$. *(Block E)*
- Index notation: Einstein summation, $\delta_{ij}$, $\epsilon_{ijk}$. *(Block F)*

**Newtonian refresher (Should)**
- Momentum, angular momentum and energy theorems for a system of particles (Goldstein 1.1 and 1.2): $\dot{\mathbf P}=\mathbf F^{(e)}$, $\dot{\mathbf L}=\mathbf N^{(e)}$, centre-of-mass decomposition, work-energy theorem, conservative forces. *(Block G)*

**Numerics (Must)**
- Writing an ODE integrator: Euler, RK4 and **velocity Verlet (leapfrog)**; energy drift versus bounded energy error; time-step convergence tests. Leapfrog is symplectic, which is why it matters from Module 09 on. *(Block G)*

## Derive from scratch (book closed)

- **D1.** The total time derivative of $f(q,\dot q,t)$ and why $\frac{\partial\dot q}{\partial q}=0$ in the partial-derivative sense.
- **D2.** The spectral theorem for a real symmetric $2\times2$ matrix (eigenvalues real, eigenvectors orthogonal).
- **D3.** $\mathbf L=\mathbf R\times M\mathbf V+\sum_i\mathbf r_i'\times m\mathbf v_i'$ (the centre-of-mass split of angular momentum).
- **D4.** The solution of the damped oscillator by the ansatz $e^{\lambda t}$.
- **D5.** The Lagrange-multiplier condition $\nabla f=\lambda\nabla g$ as a statement about tangent spaces.

## Bare-minimum exercises (with expected results)

- **E1. Partial derivatives.** For $f(q,\dot q,t)=\frac12m\dot q^2-\frac12kq^2+\alpha t\,q$ compute $\frac{df}{dt}$ along $q=A\cos\omega t$ both by chain rule and directly; they agree.
- **E2. Symmetric matrix.** $`\begin{pmatrix}2&-1\\-1&2\end{pmatrix}`$ has eigenvalues $1$ and $3$ with eigenvectors $\frac1{\sqrt2}(1,1)$ and $\frac1{\sqrt2}(1,-1)$.
- **E3. Quadratic-form pair.** Diagonalize the pair $T=\frac12(\dot x_1^2+\dot x_2^2)$, $V=\frac12(2x_1^2-2x_1x_2+2x_2^2)$; frequencies $\omega^2=1,3$.
- **E4. Index notation.** Prove $\nabla\times(\nabla\times\mathbf F)=\nabla(\nabla\cdot\mathbf F)-\nabla^2\mathbf F$ with $\epsilon_{ijk}$.
- **E5. Lagrange multiplier.** The point of $x^2+y^2=1$ nearest to $(2,1)$ is $(2,1)/\sqrt5$, distance $\sqrt5-1$.
- **E6. Oscillator.** For $\gamma=0.1\omega$ find the decay time $1/\gamma$ and the damped frequency $\omega\sqrt{1-(\gamma/\omega)^2}$.
- **E7. Matrix exponential.** Compute $e^{\epsilon A}$ for $`A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}`$ and show it is the rotation by angle $\epsilon$ ($\cos\epsilon$, $\sin\epsilon$ entries).
- **E8. Euler versus leapfrog.** Integrate the harmonic oscillator ($\omega=1$, $x_0=1$) for 100 periods with $\Delta t=0.05$. Forward Euler's energy grows without bound (by a factor $1+\Delta t^2$ per step); leapfrog's energy oscillates within $O(\Delta t^2)$ of the initial value and does not drift.
- **E9. Convergence.** Halve $\Delta t$ and verify RK4's global error falls by $2^4$ and leapfrog's by $2^2$.
- **E10. Pendulum phase portrait.** Plot $(\theta,\dot\theta)$ curves for several energies; identify the separatrix at $E=2mg\ell$ (relative to the bottom) and the librating and rotating regions.

## Optional extension

Derive velocity Verlet as the composition of a half-kick, a drift and a half-kick, and show it has second-order accuracy. The algorithm, for $\ddot x=a(x)$:

1. $v\leftarrow v+\frac{\Delta t}{2}\,a(x)$
2. $x\leftarrow x+\Delta t\,v$
3. $v\leftarrow v+\frac{\Delta t}{2}\,a(x)$

Module 09 returns to why this composition preserves phase-space area.

## Pitfalls

- Confusing $\partial L/\partial\dot q$ evaluated "at fixed $q$" with a derivative along a trajectory.
- Believing that a higher-order integrator (RK4) is always better than a low-order symplectic one for long-time orbital integration (it is not: energy drifts).
- Treating $\delta_{ij}$ and $\epsilon_{ijk}$ identities as memorized rather than derived.
- Trusting a section number from this file without checking it against your own copy of Boas.

## Gate questions

1. What is held fixed in $\partial L/\partial\dot q$, and what is held fixed in $d/dt$?
2. Why does the simultaneous diagonalization of $T$ and $V$ need $T$ positive definite?
3. Why does leapfrog stay near the true energy while forward Euler does not?

## One-page cheat sheet contents

Total/partial derivative formula; spectral theorem; $\epsilon\epsilon$ identity; oscillator solutions; leapfrog algorithm; Lagrange multiplier condition.
