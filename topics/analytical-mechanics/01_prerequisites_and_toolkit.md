# Module 01: Prerequisites and toolkit

**Books:** Goldstein (the table of contents and Chapter 1 opening), Taylor *Classical Mechanics* (optional refresher), any multivariable calculus and linear algebra text.
**Time:** 1 week (two sessions).

## Task 0: build your reading map (30 minutes, do it first)

Open your Goldstein (3rd edition) at the table of contents. In `notes/goldstein_map.md` make a table with columns *Module, Goldstein sections, page range, has worked examples? has problems? (Y/N)*, using the overview's module table as a first guess. Mark any section numbers that differ from the overview (Cayley-Klein parameters and the Hamilton-Jacobi/wave-mechanics section are the likeliest to be off by one). This map is the reference for the whole guide. (If you upload the table of contents and problem lists, I will fill it in for you.)

## Why this matters for the bridge

The material is mostly review, but three skills decide whether later modules feel smooth: manipulating partial derivatives with a clear head about *which variables are held fixed* (the Legendre transformation and canonical transformations are all about this), diagonalizing symmetric matrices (normal modes, and later Hamiltonians), and running a small numerical integrator to check a result. A one-week calibration saves more than it costs.

## Skip-test (40 minutes, no notes)

1. Diagonalize $\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$; give eigenvalues, orthonormal eigenvectors, and show that the eigenvectors of a real symmetric matrix with distinct eigenvalues are orthogonal.
2. Solve $\ddot x+\omega^2x=0$ and $\ddot x+2\gamma\dot x+\omega^2x=0$ (underdamped case) with initial conditions $x(0)=x_0$, $\dot x(0)=0$.
3. Prove $\epsilon_{ijk}\epsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}$ and use it to derive $\mathbf a\times(\mathbf b\times\mathbf c)=\mathbf b(\mathbf a\cdot\mathbf c)-\mathbf c(\mathbf a\cdot\mathbf b)$.
4. Use a Lagrange multiplier to find the point on $x^2+y^2=1$ closest to $(2,1)$.
5. Expand a one-dimensional potential $V(x)$ about a minimum $x_0$ to quadratic order and identify the small-oscillation frequency $\omega^2=V''(x_0)/m$.

## Prerequisites

Single and multivariable calculus, basic linear algebra, basic Python. Nothing else.

## Detailed topics (checklist)

**Calculus (Must)**
- Partial derivatives and the chain rule; total versus partial time derivative $\frac{d}{dt}f(q,\dot q,t)=\frac{\partial f}{\partial t}+\dot q\frac{\partial f}{\partial q}+\ddot q\frac{\partial f}{\partial\dot q}$; implicit differentiation and Jacobians; Taylor series in several variables; exact differentials.
- Lagrange multipliers for constrained extrema (the finite-dimensional ancestor of constraint forces).
- Gaussian integrals and the delta function as a limit (used in later modules).

**Differential equations (Must)**
- Linear second-order equations with constant coefficients; the harmonic oscillator, damped and driven; complex exponentials $e^{i\omega t}$; resonance and Q factor.
- Phase portraits: reading $(x,\dot x)$ plots for the oscillator and the pendulum.

**Linear algebra (Must)**
- Real symmetric matrices and the spectral theorem; simultaneous diagonalization of a quadratic form pair (the small-oscillation eigenproblem); orthogonal matrices and rotations; matrix exponential $e^{A}$ and $e^{\epsilon A}\approx1+\epsilon A$; commutators $[A,B]=AB-BA$.
- Index notation: Einstein summation, $\delta_{ij}$, $\epsilon_{ijk}$.

**Newtonian refresher (Should)**
- Momentum, angular momentum and energy theorems for a system of particles (Goldstein 1.1 and 1.2): $\dot{\mathbf P}=\mathbf F^{(e)}$, $\dot{\mathbf L}=\mathbf N^{(e)}$, centre-of-mass decomposition, work-energy theorem, conservative forces.

**Numerics (Must)**
- Writing an ODE integrator: Euler, RK4 and **velocity Verlet (leapfrog)**; energy drift versus bounded energy error; time-step convergence tests. (Leapfrog is symplectic, which is why it matters from Module 09 on.)

## Reading plan

| Session | Task |
| --- | --- |
| A1 (2 to 3 h) | Task 0; the skip-test; review any failed item from a calculus/linear algebra text; Goldstein 1.1 to 1.2 (read quickly) |
| B1 (2 to 3 h) | Exercises 1 to 6 below |
| A2 (2 to 3 h) | Exercises 7 to 10; the numerical check; write your one-page cheat sheet |

## Derive from scratch (A sessions, book closed)

1. The total time derivative of $f(q,\dot q,t)$ and why $\frac{\partial\dot q}{\partial q}=0$ in the partial-derivative sense.
2. The spectral theorem for a real symmetric $2\times2$ matrix (eigenvalues real, eigenvectors orthogonal).
3. $\mathbf L=\mathbf R\times M\mathbf V+\sum_i\mathbf r_i'\times m\mathbf v_i'$ (the centre-of-mass split of angular momentum).
4. The solution of the damped oscillator by the ansatz $e^{\lambda t}$.
5. The Lagrange-multiplier condition $\nabla f=\lambda\nabla g$ as a statement about tangent spaces.

## Bare-minimum exercises (with expected results)

1. **Partial derivatives:** for $f(q,\dot q,t)=\frac12m\dot q^2-\frac12kq^2+\alpha t\,q$ compute $\frac{df}{dt}$ along $q=A\cos\omega t$ both by chain rule and directly; they agree.
2. **Symmetric matrix:** $\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$ has eigenvalues $1$ and $3$ with eigenvectors $\frac1{\sqrt2}(1,1)$ and $\frac1{\sqrt2}(1,-1)$.
3. **Quadratic-form pair:** diagonalize the pair $T=\frac12(\dot x_1^2+\dot x_2^2)$, $V=\frac12(2x_1^2-2x_1x_2+2x_2^2)$; frequencies $\omega^2=1,3$.
4. **Index notation:** prove $\nabla\times(\nabla\times\mathbf F)=\nabla(\nabla\cdot\mathbf F)-\nabla^2\mathbf F$ with $\epsilon_{ijk}$.
5. **Lagrange multiplier:** the point of $x^2+y^2=1$ nearest to $(2,1)$ is $(2,1)/\sqrt5$, distance $\sqrt5-1$.
6. **Oscillator:** for $\gamma=0.1\omega$ find the decay time $1/\gamma$ and the damped frequency $\omega\sqrt{1-(\gamma/\omega)^2}$.
7. **Matrix exponential:** compute $e^{\epsilon A}$ for $A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ and show it is the rotation by angle $\epsilon$ ($\cos\epsilon,\sin\epsilon$ entries).
8. **Euler versus leapfrog:** integrate the harmonic oscillator ($\omega=1$, $x_0=1$) for 100 periods with $\Delta t=0.05$; forward Euler's energy grows without bound (by a factor $1+\Delta t^2$ per step), leapfrog's energy oscillates within $O(\Delta t^2)$ of the initial value and does not drift.
9. **Convergence:** halve $\Delta t$ and verify RK4's global error falls by $2^4$ and leapfrog's by $2^2$.
10. **Pendulum phase portrait:** plot $(\theta,\dot\theta)$ curves for several energies; identify the separatrix at $E=2mg\ell$ (relative to the bottom) and the librating and rotating regions.

## Optional extension

Derive velocity Verlet as the composition of a half-kick, a drift and a half-kick, and show it has second-order accuracy. Module 09 returns to why this composition preserves phase-space area.

## Pitfalls

- Confusing $\partial L/\partial\dot q$ evaluated "at fixed $q$" with a derivative along a trajectory.
- Believing that a higher-order integrator (RK4) is always better than a low-order symplectic one for long-time orbital integration (it is not: energy drifts).
- Treating $\delta_{ij}$ and $\epsilon_{ijk}$ identities as memorized rather than derived.

## Gate questions

1. What is held fixed in $\partial L/\partial\dot q$, and what is held fixed in $d/dt$?
2. Why does the simultaneous diagonalization of $T$ and $V$ need $T$ positive definite?
3. Why does leapfrog stay near the true energy while forward Euler does not?

## One-page cheat sheet contents

Total/partial derivative formula; spectral theorem; $\epsilon\epsilon$ identity; oscillator solutions; leapfrog algorithm; Lagrange multiplier condition.
