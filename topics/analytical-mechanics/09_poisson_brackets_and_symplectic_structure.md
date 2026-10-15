# Module 09: Poisson brackets and the symplectic structure (★★)

**Books:** Goldstein 9.3 to 9.4; José and Saletan chapters 5 and 6 (symplectic geometry, strongly recommended here); Landau and Lifshitz *Mechanics* section 42 (Poisson brackets).
**Time:** 2 weeks (four sessions).

## Why this matters for the bridge

This is the heart of the classical-quantum bridge. Two definitions of "canonical" are shown equivalent: preserving the form of Hamilton's equations, and preserving the **symplectic form** ($M^TJM=J$). Then the **Poisson brackets** appear as the canonical invariants, and the fundamental brackets $\{q_i,p_j\}=\delta_{ij}$, $\{q_i,q_j\}=\{p_i,p_j\}=0$ *characterize* canonical transformations completely. Write those three relations on a card: in Module 11 you will write $[\hat q_i,\hat p_j]=i\hbar\delta_{ij}$ underneath them. Also: the **Jacobi identity** is the property that makes the bracket a Lie algebra, and it is the property that survives quantization.

## Skip-test (40 minutes, no notes)

1. Write Hamilton's equations as $\dot{\boldsymbol\eta}=J\,\partial H/\partial\boldsymbol\eta$ with $\boldsymbol\eta=(q,p)^T$ and $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$; state the symplectic condition $MJM^T=J$ for the Jacobian $M=\partial\boldsymbol\zeta/\partial\boldsymbol\eta$ of a canonical transformation.
2. Define $\{u,v\}=\sum_i\left(\frac{\partial u}{\partial q_i}\frac{\partial v}{\partial p_i}-\frac{\partial u}{\partial p_i}\frac{\partial v}{\partial q_i}\right)$ and state antisymmetry, linearity, the Leibniz rule and the Jacobi identity.
3. Show that the fundamental brackets are invariant under canonical transformations.
4. Show $\frac{du}{dt}=\{u,H\}+\frac{\partial u}{\partial t}$.
5. State Poisson's theorem: the bracket of two integrals of motion is an integral of motion.

## Prerequisites

Modules 07, 08.

## Detailed topics (checklist)

**Symplectic formulation (9.3) [Must]**
- $\boldsymbol\eta=(q_1,\dots,q_n,p_1,\dots,p_n)$; $\dot{\boldsymbol\eta}=J\frac{\partial H}{\partial\boldsymbol\eta}$; the Jacobian $M$ of a transformation; **canonical iff $MJM^T=J$**; symplectic matrices $M^TJM=J$ form a group ($Sp(2n)$) closed under transposition and inversion; $\det M=1$ (phase-space volume preservation; Liouville in Module 10).
- Sign convention warning: Goldstein's $J$ and bracket sign conventions; keep $\{q,p\}=+1$ throughout.
- The symplectic form $\omega=\sum dq_i\wedge dp_i$ (José and Saletan): canonical transformations are the maps that preserve it.

**Poisson brackets (9.4) [Must]**
- Definition and **properties:** antisymmetry, bilinearity, Leibniz $\{uv,w\}=u\{v,w\}+\{u,w\}v$, **Jacobi identity** $\{u,\{v,w\}\}+\{v,\{w,u\}\}+\{w,\{u,v\}\}=0$.
- Fundamental brackets; invariance of $\{u,v\}$ under canonical transformations (so the brackets can be computed in any canonical variables); a transformation is canonical iff it preserves the fundamental brackets.
- Equation of motion in bracket form $\dot u=\{u,H\}+\partial_tu$; conserved quantities as brackets with $H$; **Poisson's theorem**.
- Lagrange brackets (awareness): the inverse structure.

**Useful bracket identities [Must]**
- $\{q_i,F(q,p)\}=\frac{\partial F}{\partial p_i}$, $\{p_i,F\}=-\frac{\partial F}{\partial q_i}$.
- $\{L_i,L_j\}=\epsilon_{ijk}L_k$; for any vector $\mathbf V(\mathbf r,\mathbf p)$: $\{L_i,V_j\}=\epsilon_{ijk}V_k$; for a scalar $S$: $\{L_i,S\}=0$.

**Numerics (Should)**
- A symplectic integrator preserves the symplectic form exactly (to rounding): leapfrog's Jacobian satisfies $\det M=1$ and $MJM^T=J$ exactly; RK4's does not (and its energy drifts).

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Goldstein 9.3; derive the symplectic condition closed-book |
| B1 | Exercises 1 to 5 |
| A2 | Goldstein 9.4; **prove the Jacobi identity in full** (tedious; do it once) |
| B2 | Exercises 6 to 10; the numerical check of exercise 8; cheat sheet |

## Derive from scratch (A sessions, book closed)

1. The symplectic condition $MJM^T=J$ from the requirement that $\boldsymbol\zeta$ obeys Hamilton's equations.
2. The properties of the Poisson bracket, **including the full Jacobi identity**.
3. The invariance of $\{u,v\}$ under canonical transformations.
4. $\frac{du}{dt}=\{u,H\}+\partial u/\partial t$ and Poisson's theorem.
5. $\{L_i,L_j\}=\epsilon_{ijk}L_k$ from scratch.

## Bare-minimum exercises (with expected results)

1. **Jacobi:** prove the Jacobi identity for the Poisson bracket by direct expansion (or check it for $u,v,w$ being the three components of $\mathbf L$).
2. **Angular momentum algebra:** $\{L_i,L_j\}=\epsilon_{ijk}L_k$ and $\{L^2,L_i\}=0$.
3. **Basic identities:** $\{q_i,F(\mathbf p)\}=\partial F/\partial p_i$; $\{p_i,G(\mathbf q)\}=-\partial G/\partial q_i$; use them to compute $\{x,p_x^2\}=2p_x$ and $\{p_x,V(x)\}=-V'(x)$.
4. **Poisson's theorem:** show that if $L_x$ and $L_y$ are conserved then $L_z=\{L_x,L_y\}$ is conserved, even without knowing the Hamiltonian's form (given both are conserved).
5. **Area-preserving $2\times2$ maps:** a linear map $M=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ of $(q,p)$ is canonical iff $ad-bc=1$ (the symplectic condition for $n=1$ is just $\det M=1$).
6. **Oscillator transformation:** show the Jacobian of $(Q,P)\to(q,p)=\left(\sqrt{2P/m\omega}\sin Q,\sqrt{2m\omega P}\cos Q\right)$ has determinant $1$.
7. **Flow is symplectic:** for $H$ with Hessian $H''$ the infinitesimal flow map $M=1+\epsilon JH''$ satisfies $MJM^T=J+O(\epsilon^2)$.
8. **Numerical check:** for the pendulum compute the one-step Jacobian $M=\partial(q_{n+1},p_{n+1})/\partial(q_n,p_n)$ for leapfrog and for RK4 by finite differences. Expect $\det M_{\rm leapfrog}=1$ to rounding error and $\det M_{\rm RK4}=1+O(\Delta t^5)\ne1$; plot energy versus time to see bounded error (leapfrog) versus drift (RK4) on long runs.
9. **Vector brackets:** show $\{L_i,x_j\}=\epsilon_{ijk}x_k$ and $\{L_i,p_j\}=\epsilon_{ijk}p_k$, and deduce $\{L_i,\mathbf r\cdot\mathbf p\}=0$ and $\{L_i,r^2\}=0$. (These identities are the classical content of "vector operators" in Module 12.)
10. **Chain rule for brackets:** show $\{f(u),v\}=f'(u)\{u,v\}$ and compute $\{x,\cos(p_x)\}=-\sin(p_x)$.

## Optional extension

Compute the Lagrange brackets $[u,v]$ for a transformation and show they satisfy $\sum_k\{u_i,u_k\}[u_k,u_j]=-\delta_{ij}$ when $\{u_i,u_j\}$ and $[u_i,u_j]$ are inverse matrices up to sign.

## Pitfalls

- Sign conventions for $J$ and for the bracket (keep $\{q,p\}=+1$).
- Computing a bracket in non-canonical variables and treating the result as invariant.
- Believing that the bracket of two conserved quantities is always nonzero or always a new quantity (it can be zero or a combination of the old ones).
- Treating a numerical integrator's high order as a guarantee of symplecticity.

## Gate questions

1. Why is the Jacobi identity the property that makes the bracket a Lie algebra, and why does it matter for quantization?
2. State the two equivalent definitions of a canonical transformation (form-preserving and symplectic).
3. Why do the fundamental brackets completely characterize canonical transformations?

## One-page cheat sheet contents

Symplectic matrix and condition; definition and properties of the bracket (including Jacobi); fundamental brackets; $\dot u=\{u,H\}+\partial_tu$; Poisson's theorem; vector-operator brackets with $\mathbf L$.
