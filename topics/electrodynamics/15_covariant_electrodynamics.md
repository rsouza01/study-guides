# Module 15: Covariant electrodynamics (★)

**Books:** Jackson **11.9** (invariance of charge; covariance of electrodynamics), **11.10** (transformation of the electromagnetic fields), 11.12 (notation note); Griffiths 12.3 (relativistic electrodynamics: how magnetism is a relativistic effect; the field tensor); Purcell chapter 5 (the fields of moving charges, the cleanest account of why magnetism is relativistic). **Units: Gaussian** from here (Jackson Chapter 11 onward); the SI dictionary is in the appendix.
**Time:** 2 weeks (four sessions).

## Why this matters

Chapters 1 to 7 are a covariant theory in a non-covariant costume. $F^{\mu\nu}$ collapses four vector equations into two tensor equations, and the field transformation law says the split into "electric" and "magnetic" is **frame-dependent**: there is one field, not two. Collect the invariants: $F_{\mu\nu}F^{\mu\nu}\propto B^2-E^2$ and $\epsilon^{\mu\nu\alpha\beta}F_{\mu\nu}F_{\alpha\beta}\propto\mathbf E\cdot\mathbf B$. The first is the Lagrangian density (Module 17). The second is the topological term whose coefficient is the QCD $\theta$-parameter: you are looking at the strong CP problem in a 1962 textbook.

## Skip-test (40 minutes, no notes)

1. Write the four-current $J^\mu=(c\rho,\mathbf J)$ and the continuity equation $\partial_\mu J^\mu=0$; state the invariance of charge.
2. Write $F^{\mu\nu}$ as a $4\times4$ matrix in terms of $\mathbf E,\mathbf B$ (Gaussian), the dual $\tilde F^{\mu\nu}$, and show $\partial_\alpha F^{\alpha\beta}=\frac{4\pi}{c}J^\beta$, $\partial_\alpha\tilde F^{\alpha\beta}=0$ reproduce all four Maxwell equations.
3. Derive the field transformation laws from $F'^{\mu\nu}=\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta F^{\alpha\beta}$: $\mathbf E'_\parallel=\mathbf E_\parallel$, $\mathbf E'_\perp=\gamma(\mathbf E_\perp+\boldsymbol\beta\times\mathbf B)$, $\mathbf B'_\parallel=\mathbf B_\parallel$, $\mathbf B'_\perp=\gamma(\mathbf B_\perp-\boldsymbol\beta\times\mathbf E)$.
4. Compute the two invariants and say when a frame exists with $\mathbf E=0$ or $\mathbf B=0$.
5. Write the covariant Lorentz force $\frac{dp^\mu}{d\tau}=\frac qcF^{\mu\nu}u_\nu$.

## Prerequisites

Modules 10, 13 and 14 (four-vectors and index placement).

## Detailed topics (checklist)

**Four-current and the field tensor (11.9) [Must]**
- $J^\mu=(c\rho,\mathbf J)$; charge is invariant (the total charge in a volume is a Lorentz scalar); the four-potential $A^\mu=(\Phi,\mathbf A)$; $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$ with (Gaussian) $F^{0i}=-E^i$, $F^{ij}=-\epsilon_{ijk}B^k$; Maxwell's equations $\partial_\alpha F^{\alpha\beta}=\frac{4\pi}{c}J^\beta$ and $\partial_\alpha\tilde F^{\alpha\beta}=0$ with $\tilde F^{\alpha\beta}=\frac12\epsilon^{\alpha\beta\gamma\delta}F_{\gamma\delta}$; the homogeneous equations are the Bianchi identity $\partial_{[\alpha}F_{\beta\gamma]}=0$ and hold automatically for $F=dA$.
- **Lorenz gauge** $\partial_\mu A^\mu=0$ and the wave equation $\Box A^\mu=\frac{4\pi}{c}J^\mu$ (Module 10 in covariant form); gauge freedom $A_\mu\to A_\mu+\partial_\mu\Lambda$.
- **Covariant Lorentz force:** $\frac{dp^\mu}{d\tau}=\frac qcF^{\mu\nu}u_\nu$.

**Transformation of the fields (11.10) [Must]**
- The field-transformation laws above (for a boost with velocity $\boldsymbol\beta$ from $S$ to $S'$); the physical content: a pure $\mathbf E$ field in one frame has a $\mathbf B$ field in another, and there is one field, not two; **magnetism as a relativistic effect** (Purcell, Griffiths): a current-carrying neutral wire is charged in the rest frame of a moving test charge because of length contraction.
- **Invariants:** $F_{\mu\nu}F^{\mu\nu}=2(B^2-E^2)$ and $\epsilon^{\mu\nu\alpha\beta}F_{\mu\nu}F_{\alpha\beta}=-8\,\mathbf E\cdot\mathbf B$; a frame with $\mathbf E=0$ exists iff $\mathbf E\cdot\mathbf B=0$ and $B^2>E^2$; a frame with $\mathbf B=0$ exists iff $\mathbf E\cdot\mathbf B=0$ and $E^2>B^2$.
- **The field of a uniformly moving point charge** by boosting the rest-frame Coulomb field: $\mathbf E=\frac{q}{r^2}\frac{(1-\beta^2)}{(1-\beta^2\sin^2\psi)^{3/2}}\hat{\mathbf r}$ (with $\mathbf r$ from the present position, $\psi$ the angle between $\mathbf r$ and $\mathbf v$), $\mathbf B=\boldsymbol\beta\times\mathbf E$: the Lorentz-contracted "pancake".

## Method card

**Field transformation:** (1) decompose $\mathbf E$ and $\mathbf B$ into components parallel and perpendicular to $\boldsymbol\beta$; (2) apply the four laws; (3) check an invariant ($E^2-B^2$, $\mathbf E\cdot\mathbf B$) in both frames; (4) check the limit $\beta\to0$.
**Field of a moving charge:** (1) write the Coulomb field in the rest frame $S'$; (2) transform the coordinates of the field point to $S'$ using $x'=\gamma(x-vt)$; (3) transform $\mathbf E'$ back to $S$ (parallel unchanged, perpendicular $\gamma$-enhanced); (4) express in terms of the present position.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Jackson 11.9; Griffiths 12.3.1 to 12.3.2; the $F^{\mu\nu}$ matrix |
| B1 | Exercises 1 and 2 |
| A2 | Jackson 11.10; the field-transformation derivation |
| B2 | Exercises 3 and 4 |
| A3 | Purcell chapter 5; magnetism from relativity (exercise 7) |
| B3 | Exercises 5 to 8 |
| A4 | **Jackson targets** (exercise 10) |
| B4 | Spare session; the month gate |

## Derive from scratch

1. $F^{\mu\nu}$ as a matrix and Maxwell's equations from $\partial_\alpha F^{\alpha\beta}$ and $\partial_\alpha\tilde F^{\alpha\beta}$.
2. The field transformation laws for a boost.
3. The two invariants.
4. The field of a moving point charge by boosting.
5. Charge conservation $\partial_\mu J^\mu=0$ from $\partial_\mu\partial_\nu F^{\mu\nu}=0$.

## Bare-minimum exercises (with expected results)

1. **The matrix:** $F^{\mu\nu}=\begin{pmatrix}0&-E_x&-E_y&-E_z\\E_x&0&-B_z&B_y\\E_y&B_z&0&-B_x\\E_z&-B_y&B_x&0\end{pmatrix}$ (Gaussian, signature $+---$); check antisymmetry and that lowering both indices flips the sign of $\mathbf E$.
2. **Maxwell from $F$:** show $\beta=0$ of $\partial_\alpha F^{\alpha\beta}=\frac{4\pi}{c}J^\beta$ gives Gauss's law $\nabla\cdot\mathbf E=4\pi\rho$ and $\beta=i$ gives Ampere-Maxwell $\nabla\times\mathbf B-\frac1c\partial_t\mathbf E=\frac{4\pi}{c}\mathbf J$; $\partial_\alpha\tilde F^{\alpha\beta}=0$ gives $\nabla\cdot\mathbf B=0$ and Faraday's law.
3. **Boosting a pure electric field:** a field $\mathbf E=E_y\hat{\mathbf y}$ in $S$ has, for a boost along $x$ with $\beta$, $E'_y=\gamma E_y$ and $B'_z=-\gamma\beta E_y$; check that $E'^2-B'^2=E_y^2$ is unchanged.
4. **Invariants:** show $F_{\mu\nu}F^{\mu\nu}=2(B^2-E^2)$ and $\mathbf E\cdot\mathbf B$ invariant; a plane wave ($E=B$, $\mathbf E\perp\mathbf B$) has both invariants zero in every frame.
5. **The pancake:** transform the Coulomb field of a charge at rest in $S'$ to $S$ (moving at $\beta$); at the instant the charge passes the origin the field in the transverse direction is $\gamma q/r^2$ and along the direction of motion $q/(\gamma^2r^2)$.
6. **Four-current of a point charge:** $J^\mu(x)=qc\int d\tau\,u^\mu(\tau)\delta^{(4)}(x-z(\tau))=q(c,\mathbf v)\delta^3(\mathbf x-\mathbf z(t))$; verify it is a four-vector and $\partial_\mu J^\mu=0$ (this uses $\delta(f(\tau))$ from Module 02).
7. **Magnetism from relativity:** a neutral wire carrying current $I$ (positive charges at rest, negative charges moving with speed $u$, equal and opposite linear densities in the lab) produces at distance $s$ the field $B=\frac{2I}{cs}$ (Gaussian), so a charge $q$ moving parallel to the wire at speed $v$ feels $F=\frac{qvB}{c}=\frac{2qvI}{c^2s}$. In the charge's rest frame the two charge sheets are Lorentz-contracted by different amounts, so the wire carries a net charge density and the force is purely electric. Show to first order in $v^2/c^2$ that $F'=\gamma F\simeq F$ (transverse forces transform with a factor $\gamma$).
8. **Covariant force:** from $\frac{dp^\mu}{d\tau}=\frac qcF^{\mu\nu}u_\nu$ derive $\frac{d(\gamma m\mathbf v)}{dt}=q\left(\mathbf E+\frac{\mathbf v}{c}\times\mathbf B\right)$ and $\frac{dE}{dt}=q\mathbf E\cdot\mathbf v$.
9. **Charge conservation for free:** $\partial_\mu J^\mu=\frac{c}{4\pi}\partial_\mu\partial_\nu F^{\mu\nu}=0$ because $F$ is antisymmetric and partial derivatives commute.
10. **Jackson targets (about 11.15 and 11.18):** (a) the two invariants, and when a frame exists with $\mathbf E=0$ or $\mathbf B=0$ (**do this one**); (b) the field of a relativistically moving charge by boosting, the $\gamma$-compressed pancake; **compare with your Module 11 retarded-potential answer** (two routes, one result).

## Optional extension

Show that $\mathbf F=\mathbf E+i\mathbf B$ transforms under a boost as a vector rotated by an imaginary angle (the $(1,0)\oplus(0,1)$ statement of Module 14) and deduce the two invariants as the real and imaginary parts of $\mathbf F\cdot\mathbf F$.

## Pitfalls

- Sign errors in $F^{0i}=-E^i$ and in the lowering of indices.
- Applying the field transformations to the *coordinates* of the field point as well (they also transform).
- Using SI field laws in Jackson's Gaussian chapters ($\mathbf v\times\mathbf B$ carries $1/c$ in Gaussian units).
- Believing $\mathbf E$ and $\mathbf B$ are separate objects.

## Gate questions

1. Why is "one field, not two" a consequence of the transformation law?
2. How do the two Lorentz invariants of $F^{\mu\nu}$ constrain which frames exist?
3. Why do the homogeneous Maxwell equations hold automatically when $F=dA$?

## One-page cheat sheet contents

$F^{\mu\nu}$ matrix; covariant Maxwell equations; field transformation laws; invariants; four-current; covariant force.
