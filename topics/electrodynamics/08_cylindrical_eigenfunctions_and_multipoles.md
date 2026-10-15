# Module 08: Cylindrical coordinates, eigenfunction expansions and multipoles

**Books:** Jackson 3.7 to 3.8 (Bessel functions and cylindrical boundary-value problems: *read for the pattern, not the special-function detail*), 3.11 (cylindrical Green functions), **3.12 (eigenfunction expansions for Green functions)**, 4.1 (the multipole expansion: this is 3.10 read backwards), 4.2 (multipole interaction energy); Griffiths 3.4 (multipole expansion). **Skip** Jackson 3.13 and 4.3 to 4.7 (skim 4.3 only for the idea of macroscopic averaging, which returns in 6.6).
**Time:** 2 weeks (four sessions).

## Why this matters

The same Green function construction works in every separable geometry. The **eigenfunction expansion** $G=4\pi\sum_n\frac{\psi_n^*(\mathbf x')\psi_n(\mathbf x)}{\lambda_n}$ says the Green function is the inverse of the operator in its eigenbasis; what breaks when some $\lambda_n\to0$ (**zero modes**) returns in gauge fixing in QFT. The **multipole expansion** is the physics payoff: far from a source, the field is organized by $\ell$, each term falling off as $r^{-(\ell+1)}$.

## Skip-test (40 minutes, no notes)

1. Separate Laplace's equation in cylindrical coordinates; write the radial solution $J_m(k\rho)$ and the axial $\sinh(kz)$ or $e^{\pm kz}$, and state the orthogonality of Bessel functions on $(0,a)$.
2. Write $G=4\pi\sum_n\frac{\psi_n^*(\mathbf x')\psi_n(\mathbf x)}{\lambda_n}$ for $-\nabla^2\psi_n=\lambda_n\psi_n$ with Dirichlet conditions and say what breaks when some $\lambda_n\to0$.
3. Define the Cartesian multipole moments $Q$, $\mathbf p$, $Q_{ij}=\int(3x_ix_j-r^2\delta_{ij})\rho\,d^3x$ and write the multipole expansion of the potential through the quadrupole.
4. Give the energy of a dipole in an external field and the interaction energy of two dipoles.
5. Show that the monopole and dipole terms of the spherical expansion are the total charge and the dipole moment.

## Prerequisites

Modules 06 and 07.

## Detailed topics (checklist)

**Cylindrical coordinates and Bessel functions (3.7 to 3.8) [Should]**
- $\Phi=R(\rho)Q(\phi)Z(z)$; $Q=e^{im\phi}$ with integer $m$ (single-valuedness); radial equation $\rho^2R''+\rho R'+(k^2\rho^2-m^2)R=0$ with solutions $J_m(k\rho)$ (regular at $0$) and $N_m(k\rho)$; zeros $x_{mn}$ ($J_0$: $2.405$, $5.520$, $8.654$); orthogonality $\int_0^a\rho J_m(x_{mn}\rho/a)J_m(x_{mn'}\rho/a)d\rho=\frac{a^2}2J_{m+1}^2(x_{mn})\delta_{nn'}$; Fourier-Bessel series. *Keep only the pattern:* the same recipe (separate, impose homogeneous conditions, expand, project).
- The pattern for a finite cylinder with a given top: $\Phi=\sum_nA_nJ_0\left(\frac{x_{0n}\rho}{a}\right)\frac{\sinh(x_{0n}z/a)}{\sinh(x_{0n}L/a)}$.

**Green functions in cylindrical coordinates and eigenfunction expansions (3.11 to 3.12) [Must]**
- $G$ expanded in $e^{im(\phi-\phi')}$, a Fourier or Bessel transform in $z$ or $\rho$, and a one-dimensional jump condition in the remaining variable (the same recipe as Module 07).
- **Eigenfunction expansion (3.12):** $G(\mathbf x,\mathbf x')=4\pi\sum_n\frac{\psi_n^*(\mathbf x')\psi_n(\mathbf x)}{\lambda_n}$; completeness of the $\psi_n$; **zero modes**: if $\lambda_n=0$ the sum diverges, which signals that the operator is not invertible (a Neumann problem has a constant zero mode; a gauge field has pure-gauge zero modes). The cure: restrict to the orthogonal complement or fix the gauge.

**The multipole expansion (4.1 to 4.2) [Must]**
- $\Phi=\frac{1}{4\pi\epsilon_0}\left[\frac Qr+\frac{\mathbf p\cdot\mathbf x}{r^3}+\frac12\sum_{ij}Q_{ij}\frac{x_ix_j}{r^5}+\dots\right]$ with $Q_{ij}=\int(3x_ix_j-r^2\delta_{ij})\rho\,d^3x$ (traceless); relation to $q_{\ell m}$ (for example $q_{20}=\frac12\sqrt{\frac5{4\pi}}Q_{33}$).
- **Energy in an external field:** $W=Q\Phi(0)-\mathbf p\cdot\mathbf E(0)-\frac16\sum_{ij}Q_{ij}\partial_iE_j(0)+\dots$; torque $\mathbf p\times\mathbf E$; dipole-dipole energy $U=\frac{1}{4\pi\epsilon_0R^3}\left[\mathbf p_1\cdot\mathbf p_2-3(\mathbf p_1\cdot\hat{\mathbf n})(\mathbf p_2\cdot\hat{\mathbf n})\right]$.

## Method cards

**Fourier-Bessel problem:** (1) separate with $e^{im\phi}$; (2) impose the homogeneous radial condition at $\rho=a$ to get $k=x_{mn}/a$; (3) take $\sinh$ or $e^{\pm kz}$ in $z$ as the geometry requires; (4) expand the given boundary function in $J_m$; (5) $A_n=\frac{2}{a^2J_{m+1}^2(x_{mn})}\int_0^a\rho f(\rho)J_m(x_{mn}\rho/a)d\rho$.
**Multipole moments:** (1) pick the origin (it can be chosen to kill the dipole if $Q\ne0$); (2) compute $Q$, then $\mathbf p$, then $Q_{ij}$; (3) check tracelessness; (4) write the potential through the first non-vanishing order; (5) check the angular dependence against symmetry.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Jackson 3.7 to 3.8 (pattern); Bessel zeros and orthogonality |
| B1 | Exercises 2 and 3 |
| A2 | Jackson 3.11 to 3.12; eigenfunction expansion of a 1D Green function (exercise 4) |
| B2 | Exercises 4 and 5; **Jackson target (a)** |
| A3 | Jackson 4.1 to 4.2; Griffiths 3.4 |
| B3 | Exercises 1 and 6 to 8 |
| A4 | Exercises 9 and 10; **Jackson target (b)** |
| B4 | Spare session; Month-2 style gate (below) |

## Derive from scratch

1. The cylindrical separation and the requirement $m\in\mathbb Z$.
2. The eigenfunction expansion of the 1D Green function on $(0,L)$ and its closed form.
3. The Cartesian multipole expansion from the Taylor series of $\frac{1}{|\mathbf x-\mathbf x'|}$.
4. The energy of a dipole and of two dipoles.
5. The reason a Neumann eigenfunction expansion fails (zero mode).

## Bare-minimum exercises (with expected results)

1. **Multipole moments of a discrete configuration:** charges $+q$ at $z=\pm a$ and $-2q$ at the origin (a linear quadrupole): $Q=0$, $\mathbf p=0$, $Q_{zz}=4qa^2$, $Q_{xx}=Q_{yy}=-2qa^2$; the potential is $\Phi=\frac{1}{4\pi\epsilon_0}\frac{Q_{zz}}{4}\frac{3\cos^2\theta-1}{r^3}=\frac{qa^2(3\cos^2\theta-1)}{4\pi\epsilon_0r^3}$. Check $q_{20}=\frac12\sqrt{\frac5{4\pi}}Q_{zz}$ against the direct $\int Y^*_{20}r'^2\rho$.
2. **Bessel zeros:** $J_0$ vanishes at $2.405,5.520,8.654$; check the first zero numerically from the series $1-\frac{x^2}4+\frac{x^4}{64}-\dots$.
3. **Cylinder with a given top:** for a grounded cylinder of radius $a$ and length $L$ with $V$ on the top face, $A_n=\frac{2V}{x_{0n}J_1(x_{0n})}$; check that the series gives $V$ at $z=L$ near the axis.
4. **1D eigenfunction expansion:** for $-\frac{d^2G}{dx^2}=\delta(x-x')$ on $(0,L)$ with $G(0)=G(L)=0$: $G=\frac{2}{L}\sum_n\frac{\sin(n\pi x/L)\sin(n\pi x'/L)}{(n\pi/L)^2}=\frac{x_<(L-x_>)}{L}$; verify the jump $G'(x'^+)-G'(x'^-)=-1$.
5. **Zero modes:** for Neumann conditions on the same interval the constant is a zero mode with $\lambda_0=0$ and the formula breaks; show that $-G''=\delta$ with $G'(0)=G'(L)=0$ has no solution (integrate: $0=-1$) unless a compensating uniform source $\frac1L$ is added.
6. **Dipole:** from the Cartesian formula $\Phi=\frac{\mathbf p\cdot\mathbf x}{4\pi\epsilon_0r^3}$ recover Module 03's $E_r=\frac{2p\cos\theta}{4\pi\epsilon_0r^3}$, $E_\theta=\frac{p\sin\theta}{4\pi\epsilon_0r^3}$.
7. **Dipole-dipole energy:** two dipoles $\mathbf p_1,\mathbf p_2$ at separation $R\hat{\mathbf n}$: $U=\frac{1}{4\pi\epsilon_0R^3}\left[\mathbf p_1\cdot\mathbf p_2-3(\mathbf p_1\cdot\hat{\mathbf n})(\mathbf p_2\cdot\hat{\mathbf n})\right]$; head-to-tail along $\hat{\mathbf n}$ gives $-\frac{2p_1p_2}{4\pi\epsilon_0R^3}$, side by side and parallel gives $+\frac{p_1p_2}{4\pi\epsilon_0R^3}$.
8. **Torque:** a dipole $\mathbf p$ in a uniform field has $\tau=\mathbf p\times\mathbf E$ and $U=-\mathbf p\cdot\mathbf E$; small oscillations about the stable orientation have $\omega^2=pE/I$.
9. **Quadrupole in a field:** show $U=-\frac16\sum_{ij}Q_{ij}\partial_iE_j$ for a traceless quadrupole in a non-uniform field with $\nabla\cdot\mathbf E=0$ (and that the trace part would not contribute).
10. **Jackson targets:** (a) about 3.19, the Green function inside a cylinder; and about 3.17 (mandatory in your roadmap): a point charge between two grounded parallel planes via the Green function expansion (compare with the infinite image series: the force on a charge at the mid-plane vanishes by symmetry); (b) about 4.1, the multipole moments of a discrete configuration (exercise 1), including the first non-vanishing moment and the angular pattern.

## Month-2 style blank-page gate (after Module 08)

1. Derive Legendre's equation by separation and state the regularity argument quantizing $\ell$.
2. State the addition theorem and derive the $Y_{\ell m}$ expansion of $\frac{1}{|\mathbf x-\mathbf x'|}$.
3. **Construct $g_\ell(r,r')$ for free space from scratch**, then between concentric spheres.
4. Derive $q_{\ell m}$; show $\ell=0,1$ give the total charge and the dipole.
5. Write $G=4\pi\sum\frac{\psi^*\psi}{\lambda}$ and say what breaks when some $\lambda_n\to0$.

**Computational task (optional):** implement $g_\ell(r,r')$ for free space and for the two-sphere region numerically; sum the series and verify against $\frac{1}{|\mathbf x-\mathbf x'|}$; plot convergence versus $\ell_{\max}$ as $\mathbf x\to\mathbf x'$ and watch it fail. Understanding why it fails at coincident points is understanding why propagators are singular on the light cone.

## Pitfalls

- Allowing non-integer $m$ (single-valuedness of $\Phi$ forces integers).
- Forgetting that the quadrupole tensor is *traceless* by definition.
- Shifting the origin and forgetting that the dipole depends on the origin when $Q\ne0$.
- Ignoring the zero mode of a Neumann problem.

## Gate questions

1. What does a zero eigenvalue of the operator mean for the Green function?
2. Why does the multipole expansion converge outside the smallest sphere containing the charges?
3. Why is the energy of a dipole $-\mathbf p\cdot\mathbf E$ and not $-\frac12\mathbf p\cdot\mathbf E$?

## One-page cheat sheet contents

Cylindrical separation and Bessel facts; eigenfunction expansion; Cartesian multipoles; dipole and quadrupole energies.
