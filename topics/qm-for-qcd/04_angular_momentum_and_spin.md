# Module 04: Angular momentum and spin

**Zettili:** Chapter 5, *Angular Momentum* (printed pp. 313–366; PDF pp. 333–386).
**Time:** 2 weeks.

## Zettili pin (exact, from your 3rd edition)

PDF page = printed page + 20.

| Section | Printed page | Role |
| --- | --- | --- |
| 5.2 Orbital angular momentum | 313 | core |
| 5.3 General formalism of angular momentum | 315 | core |
| 5.4 Matrix representation | 320 | core |
| 5.5 Geometrical representation | 323 | skim |
| 5.6.1 Experimental evidence of spin | 325 | skim |
| 5.6.2 General theory of spin | 329 | core |
| 5.6.3 Spin 1/2 and the Pauli matrices | 330 | core |
| 5.6.4 Schrodinger equation with spin: Pauli Hamiltonian | 333 | core |
| 5.7 Eigenfunctions of orbital angular momentum, spherical harmonics (5.7.1 to 5.7.3) | 335 to 343 | core |
| 5.8 Solved Problems 5.1 to 5.13 | 344 to 358 | exercise pool |
| 5.9 Exercises 5.1 to 5.38 | 359 to 366 | extra pool |
| Appendix B: angular momentum in spherical coordinates | 941 | read with 5.7 |

**Solved problems to do:** 5.1 ($\Delta J_x\Delta J_y$), 5.4 and 5.5 (spin along a direction), 5.6 (Hamiltonian $\epsilon\,\vec\sigma\cdot\hat n$), 5.7 and 5.8 ($j=1$ matrices and arbitrary direction), 5.9 (measurements on a superposition of $Y_{\ell m}$), 5.12 (action of $L^2,L_z$ on a function), 5.13 (spin 3/2 matrices).
**Unsolved exercises worth doing:** 5.13, 5.14, 5.21, 5.22, 5.26, 5.27, 5.29 to 5.35.
**Not in Zettili:** a treatment of magnetic resonance (a rotating transverse field); use Sakurai.

## Why this matters for QCD

- The **SU(2)** algebra $[J_i,J_j]=i\hbar\epsilon_{ijk}J_k$ is the algebra of spin, of **isospin** (the nucleon and pion multiplets) and of weak isospin. Learning it once serves all three.
- **Spin-1/2 and the Pauli matrices** are the foundation of the Dirac equation, helicity and chirality.
- **Spherical harmonics and partial waves** organize scattering (Module 10) and nuclear states.
- The fact that a $2\pi$ rotation of a spinor gives $-1$ is the first encounter with a **double cover** (SU(2) versus SO(3)), the same structure as the Lorentz group and SL(2,C).

## Skip-test (40 minutes, no notes)

1. From $[J_i,J_j]=i\hbar\epsilon_{ijk}J_k$ derive that $[J^2,J_i]=0$, define $J_\pm$ and show $J_\pm|j,m\rangle=\hbar\sqrt{j(j+1)-m(m\pm1)}|j,m\pm1\rangle$.
2. Show that the allowed $j$ are integer or half-integer and $m\in\{-j,\dots,j\}$.
3. Write the $3\times3$ spin-1 matrices $J_z,J_\pm,J_x,J_y$ in the $|1,m\rangle$ basis.
4. Show $(\vec\sigma\cdot\hat n)^2=1$ and find the eigenstates of $\vec\sigma\cdot\hat n$ in terms of the polar angles.
5. Evolve a spin-1/2 in a field $B\hat z$ and give the precession frequency.

## Prerequisites

Modules 01, 02. Spherical coordinates, partial differential equations of the Legendre type (awareness).

## Detailed topics (checklist)

**Orbital angular momentum**
- $\vec L=\vec r\times\vec p$, the commutators $[L_i,L_j]=i\hbar\epsilon_{ijk}L_k$, $[L^2,L_i]=0$, $[L_i,x_j]=i\hbar\epsilon_{ijk}x_k$ (same for $p$): $\vec r$ and $\vec p$ are vector operators.
- $L_z=-i\hbar\partial_\phi$ and $L^2$ in spherical coordinates, eigenfunctions $Y_\ell^m(\theta,\phi)$, orthonormality, parity $(-1)^\ell$, the first few explicit ($Y_0^0$, $Y_1^m$, $Y_2^m$), the addition theorem and Legendre polynomials ($P_\ell(\cos\gamma)=\frac{4\pi}{2\ell+1}\sum_mY_\ell^{m*}Y_\ell^m$), only integer $\ell$ for orbital motion.

**General angular momentum algebra**
- Ladder operators, spectra of $J^2$ and $J_z$, matrix elements, construction of representations of dimension $2j+1$.
- Spin-1/2: Pauli matrices, spinors, $\vec S=\frac\hbar2\vec\sigma$, $\sigma_i\sigma_j=\delta_{ij}+i\epsilon_{ijk}\sigma_k$, spin-up/down along an arbitrary axis.
- Spin-1: the $3\times3$ matrices; the Cartesian representation (vector).
- Rotation of a spin-1/2 by an angle $\theta$ about $\hat n$: $U=e^{-i\theta\hat n\cdot\vec\sigma/2}$; the $2\pi$ rotation gives $-1$ and the $4\pi$ rotation gives $+1$.

**Spin in a magnetic field**
- The magnetic moment $\vec\mu=\gamma\vec S$ with $\gamma=gq/2m$ ($g=2$ for the electron at leading order); Stern-Gerlach; Larmor precession at $\omega=\gamma B$; magnetic resonance (a rotating transverse field) as a Rabi problem.

**Orbital plus spin**
- The total $\vec J=\vec L+\vec S$ (a preview of Module 06), the Pauli equation, and the fact that spin is intrinsic and has no classical coordinate representation.

## Reading plan (exact)

| Block | Reading |
| --- | --- |
| Lunch 1 | Sections 5.2 to 5.3 (pp. 313 to 320) |
| Lunch 2 | Sections 5.4 to 5.5 (pp. 320 to 325) |
| Lunch 3 | Sections 5.6.2 to 5.6.4 (pp. 329 to 335) |
| Lunch 4 | Section 5.7 (pp. 335 to 344) and Appendix B (p. 941) |
| Week 2 lunches | Review; Section 5.6.1 skim; read the worked examples with answers covered |
| Evenings | Derivations; then Problems 5.1 to 5.13; exercises |

## Derive from scratch (derivation nights)

1. The entire ladder-operator derivation of the angular momentum spectrum (this is the key derivation of the module).
2. $L_z$, $L_\pm$ and $L^2$ in spherical coordinates; the spherical harmonics $Y_\ell^\ell$ from $L_+Y_\ell^\ell=0$ and $Y_\ell^{\ell-1}$ from $L_-$.
3. $\sigma_i\sigma_j=\delta_{ij}+i\epsilon_{ijk}\sigma_k$ and $(\vec\sigma\cdot\vec a)(\vec\sigma\cdot\vec b)$.
4. $e^{-i\theta\hat n\cdot\vec\sigma/2}=\cos\frac\theta2-i\,\hat n\cdot\vec\sigma\sin\frac\theta2$ and the $2\pi$ result.
5. Larmor precession from $H=-\gamma\vec B\cdot\vec S$ in the Heisenberg picture: $\dot{\vec S}=\gamma\vec S\times\vec B$.

## Bare-minimum exercises (solved-problem keywords: ladder operators, spin-1/2 matrices, spin-1, spherical harmonics, Stern-Gerlach)

1. **Matrix elements:** compute $\langle j,m\pm1|J_\pm|j,m\rangle$ for $j=1$ and build $J_x,J_y,J_z$; verify $J^2=2\hbar^2$ and $[J_x,J_y]=i\hbar J_z$. *Zettili:* Problems 5.7 and 5.8; Exercises 5.21 and 5.27.
2. **Spin along a direction:** find the eigenstates of $\vec\sigma\cdot\hat n$ with $\hat n=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)$. *Zettili:* Problems 5.4 and 5.5; Exercises 5.33 to 5.35.
3. **Sequential Stern-Gerlach:** a beam polarized along $+z$ passes a filter along $+x$ and then one along $+z$ again. Show that the surviving fraction is $\frac12$ after the $+x$ filter and $\frac14$ after the final $+z$ filter, and explain why removing the middle filter would give fraction $1$. *Zettili:* Section 5.6.1; Exercise 5.33.
4. **Spin-1 in a field:** diagonalize $H=\omega S_z+\beta S_x^2$ or $H=\omega J_z$ for $j=1$ and sketch the level scheme (the quadratic Zeeman effect). *Zettili:* Problem 5.13 (spin 3/2 matrices); Exercises 5.29, 5.31, 5.32.
5. **Orbital:** write $L_x$ and $L_y$ in terms of $L_\pm$; compute $\langle L_x^2\rangle$ in $|\ell,m\rangle$ ($=\hbar^2[\ell(\ell+1)-m^2]/2$). *Zettili:* Problems 5.1 and 5.9; Exercise 5.14.
6. **Spherical harmonics:** verify $Y_1^0=\sqrt{3/4\pi}\cos\theta$ is an eigenfunction of $L^2$ with $2\hbar^2$ and construct $Y_1^{\pm1}$ with $L_\pm$. *Zettili:* Problem 5.12; Exercises 5.13, 5.22, 5.26.
7. **Magnetic resonance:** for $H=-\gamma B_0S_z-\gamma B_1(S_x\cos\omega t+S_y\sin\omega t)$, move to the rotating frame and show the Rabi formula with the detuning $\Delta=\omega-\omega_0$. *Zettili:* Sections 5.6.4 and 6.4; the rotating-field (Rabi) problem is not in Zettili, use Sakurai.
8. **Rotation of a spinor:** apply a rotation by $\pi/2$ about $y$ to $|\uparrow\rangle$ and obtain $|{\to}\rangle$; show the $2\pi$ rotation gives $-|\uparrow\rangle$. *Zettili:* Section 7.2 (Module 06); Exercises 7.10 and 7.15.
9. **Spin-orbit preview:** for $\vec L\cdot\vec S=\frac12(J^2-L^2-S^2)$ compute the eigenvalues for $\ell=1$, $s=\frac12$ (i.e., $\frac{\hbar^2}2\ell$ for $j=\ell+\frac12$ and $-\frac{\hbar^2}2(\ell+1)$ for $j=\ell-\frac12$). *Zettili:* Problem 5.6; Section 7.3.3 (Module 06).
10. **Isospin analogy (2 lines):** state which of the above results apply verbatim to the nucleon doublet $(p,n)$ and the pion triplet $(\pi^+,\pi^0,\pi^-)$. *Zettili:* Section 7.3.6 (isospin).

## Optional extension

Show the explicit homomorphism $SU(2)\to SO(3)$ by $U\sigma_iU^\dagger=R_{ij}\sigma_j$ and compute the kernel $\{\pm1\}$.

## Pitfalls

- Using the wrong sign convention for the magnetic moment and precession direction. Fix a convention in your notes.
- Forgetting that $L_x$ and $L_y$ do not commute with each other, only with $L^2$.
- Assuming half-integer $\ell$ can occur for orbital angular momentum.
- Treating the spin operators as acting on position-space functions.

## Gate questions

1. Why do orbital angular momentum eigenvalues $\ell$ have to be integers while spin can be half-integer?
2. What is the physical meaning of the double cover $SU(2)\to SO(3)$?
3. Why do nucleons and pions fit into the same algebraic structure as spins?

## One-page cheat sheet contents

Angular momentum algebra, ladder formulas, Pauli identities, rotation operator, first spherical harmonics, spin in a field.
