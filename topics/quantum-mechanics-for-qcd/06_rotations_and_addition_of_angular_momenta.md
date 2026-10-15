# Module 06: Rotations and addition of angular momenta

**Zettili:** Chapter 7, *Rotations and Addition of Angular Momenta* (printed pp. 433–502; PDF pp. 453–522), including Section 7.3.6 (isospin) and Section 7.4 (tensor operators, Wigner-Eckart).
**Time:** 2 weeks.

## Zettili pin (exact, from your 3rd edition)

PDF page = printed page + 20.

| Section | Printed page | Role |
| --- | --- | --- |
| 7.1 Rotations in classical physics (active, passive, properties) | 433 to 436 | skim |
| 7.2 Rotations in QM (7.2.1 to 7.2.6: infinitesimal, finite, Euler, representation, rotation matrices and $Y_{\ell m}$) | 437 to 447 | core |
| 7.3.1 to 7.3.2 Addition of two angular momenta, Clebsch-Gordan coefficients | 448 to 459 | core |
| 7.3.3 Coupling of orbital and spin angular momenta | 460 | core |
| 7.3.4 Addition of more than two angular momenta | 464 | core (baryon spin) |
| 7.3.5 Rotation matrices for coupling two angular momenta | 465 | skim |
| 7.3.6 Isospin | 468 to 470 | core |
| 7.4 Rotations of scalar, vector, tensor operators; 7.4.4 Wigner-Eckart theorem | 471 to 478 | core |
| 7.5 Solved Problems 7.1 to 7.11 | 479 to 495 | exercise pool |
| 7.6 Exercises 7.1 to 7.33 | 496 to 502 | extra pool |

**Solved problems to do:** 7.1 (transformation of $J_x,J_y$), 7.3 to 7.5 (three and four spin-1/2 particles, Clebsch-Gordan, total spin), **7.6 (pion-nucleon isospin)**, 7.7 and 7.8 (Wigner-Eckart, dipole matrix elements), 7.9 ($d^{(1)}$), 7.10 (rotation matrices of coupled states), 7.11 (two particles of angular momentum 1).
**Unsolved exercises worth doing:** 7.8, 7.9, 7.17, 7.23, 7.25 to 7.33.
**Not in Zettili:** the connection of isospin to flavor SU(3) (Module 12); use Halzen and Martin.

## Why this matters for QCD

- **Isospin coupling** is *exactly* angular momentum addition: pion-nucleon scattering ($\tfrac12\otimes1=\tfrac32\oplus\tfrac12$), the $\Delta$ resonance ($I=3/2$), nucleon-nucleon states ($0\oplus1$), and relations between cross sections follow from Clebsch-Gordan coefficients.
- **Spin coupling** in hadrons: quark spins combine to baryon spin 1/2 or 3/2 and meson spin 0 or 1.
- **The Wigner-Eckart theorem** converts "which matrix elements vanish and what are their ratios" into pure group theory: selection rules and relations among decay rates and form factors.
- **Rotation matrices** define helicity states and partial-wave expansions in scattering and decay.

## Skip-test (40 minutes, no notes)

1. Write the rotation operator $U(\hat n,\theta)=e^{-i\theta\hat n\cdot\vec J/\hbar}$ and show that for spin-1/2 $U=\cos\frac\theta2-i\hat n\cdot\vec\sigma\sin\frac\theta2$.
2. Construct the four states of two spin-1/2 particles in the coupled basis: triplet $|1,1\rangle=|\uparrow\uparrow\rangle$, $|1,0\rangle=\frac{1}{\sqrt2}(|\uparrow\downarrow\rangle+|\downarrow\uparrow\rangle)$, $|1,-1\rangle$, singlet $|0,0\rangle=\frac{1}{\sqrt2}(|\uparrow\downarrow\rangle-|\downarrow\uparrow\rangle)$.
3. State the allowed $J$ in $j_1\otimes j_2$ and verify that the dimensions match: $(2j_1+1)(2j_2+1)=\sum_{J=|j_1-j_2|}^{j_1+j_2}(2J+1)$.
4. Obtain $|3/2,1/2\rangle=\sqrt{\tfrac13}\,|1,1\rangle|\!\downarrow\rangle+\sqrt{\tfrac23}\,|1,0\rangle|\!\uparrow\rangle$ for $1\otimes\tfrac12$.
5. State the Wigner-Eckart theorem and the selection rules for a vector operator.

## Prerequisites

Modules 04 and 05.

## Detailed topics (checklist)

**Rotations**
- Active and passive rotations, the rotation group $SO(3)$ and its generators, finite rotations by exponentiation; composition of rotations and the non-commutativity of finite rotations.
- Euler angles $(\alpha,\beta,\gamma)$, $D^j_{m'm}(\alpha,\beta,\gamma)=e^{-im'\alpha}d^j_{m'm}(\beta)e^{-im\gamma}$, the small $d$-matrix for $j=\frac12,1$ ($d^{1/2}_{++}=\cos\frac\beta2$, $d^{1/2}_{-+}=\sin\frac\beta2$, $d^1_{00}=\cos\beta$), the relation of $D^\ell_{m0}$ to spherical harmonics.
- Rotation of spin-1/2 states and the double-valued representation; the rotation of a vector operator: $U^\dagger V_iU=R_{ij}V_j$ and the defining commutator $[J_i,V_j]=i\hbar\epsilon_{ijk}V_k$.

**Addition of angular momenta**
- Uncoupled and coupled bases $|j_1m_1;j_2m_2\rangle$ and $|j_1j_2;JM\rangle$; the allowed $J$ and the counting argument; the triangle rule.
- Clebsch-Gordan coefficients: definition, orthogonality, reality conventions (Condon-Shortley), symmetry properties, construction by $J_-$ and by orthogonality, standard tables ($\frac12\otimes\frac12$, $1\otimes\frac12$, $1\otimes1$).
- Coupling of spin and orbital angular momentum: $|\ell,\tfrac12;j,m\rangle$ and spin-orbit eigenvalues (Module 05 item 9); the Landé factor for $J=L+S$ (projection theorem).
- Wigner 3$j$ and 6$j$ symbols (awareness: what they are for, not how to compute them by hand).

**Tensor operators and Wigner-Eckart (Zettili Section 7.4, pp. 471 to 478; Sakurai for a second view)**
- Spherical components of vectors, irreducible tensor operators $T^{(k)}_q$ with $[J_z,T^k_q]=\hbar qT^k_q$.
- The Wigner-Eckart theorem: $\langle j'm'|T^k_q|jm\rangle=\langle jm;kq|j'm'\rangle\frac{\langle j'||T^k||j\rangle}{\sqrt{2j'+1}}$; selection rules ($m'=m+q$, triangle for $(j,k,j')$); ratios of matrix elements independent of the reduced matrix element.
- The projection theorem and the Landé $g$-factor.

## Reading plan (exact)

| Block | Reading |
| --- | --- |
| Lunch 1 | Sections 7.2.1 to 7.2.4 (pp. 437 to 443) |
| Lunch 2 | Sections 7.2.5 to 7.2.6 (pp. 443 to 448) |
| Lunch 3 | Sections 7.3.1 to 7.3.2 (pp. 448 to 460) |
| Lunch 4 | Sections 7.3.3 to 7.3.4 (pp. 460 to 465) |
| Week 2 lunches | Section 7.3.6 isospin (pp. 468 to 471) and Section 7.4 (pp. 471 to 479) |
| Evenings | Derivations; then Problems 7.1 to 7.11; exercises |

## Derive from scratch (derivation nights)

1. Construction of the $1\otimes\frac12$ Clebsch-Gordan coefficients using $J_-$ on the highest state and orthogonality.
2. The $\frac12\otimes\frac12$ triplet-singlet decomposition and the exchange symmetry (triplet symmetric, singlet antisymmetric).
3. The matrix $d^{1/2}(\beta)$ and the property $D^j(R_1R_2)=D^j(R_1)D^j(R_2)$.
4. The Wigner-Eckart theorem's ingredients: the commutator action of $J_\pm$ on $T^k_q$ and the recursion for matrix elements (Sakurai).
5. The Landé $g$-factor from the projection theorem.

## Bare-minimum exercises (solved-problem keywords: addition of angular momenta, Clebsch-Gordan, spin-orbit, rotation matrix, Wigner-Eckart)

1. **$\frac12\otimes\frac12$:** write all four coupled states; verify they are orthonormal and eigenstates of $S^2$ with $2\hbar^2$ and $0$. *Zettili:* Section 7.3.2; Exercises 7.29 and 7.30.
2. **$1\otimes\frac12$:** build $|\tfrac32,\pm\tfrac32\rangle$, $|\tfrac32,\pm\tfrac12\rangle$, $|\tfrac12,\pm\tfrac12\rangle$, with $|\tfrac12,\tfrac12\rangle=\sqrt{\tfrac23}|1,1\rangle|\!\downarrow\rangle-\sqrt{\tfrac13}|1,0\rangle|\!\uparrow\rangle$ (sign convention-dependent). *Zettili:* Exercises 7.23 and 7.28; Problem 7.10.
3. **$1\otimes1$:** build $|2,m\rangle$, $|1,m\rangle$, $|0,0\rangle=\frac{1}{\sqrt3}(|1,-1\rangle-|0,0\rangle+|-1,1\rangle)$, and verify the symmetry under exchange. *Zettili:* Problem 7.11; Exercise 7.31.
4. **Spin-orbit levels:** for $\ell=1,s=\frac12$ give the energies of $j=\frac32,\frac12$ levels with $H_{SO}=\xi\,\vec L\cdot\vec S$ and the splitting $\frac32\xi\hbar^2$. *Zettili:* Section 7.3.3; Exercises 7.8 and 7.27.
5. **Pion-nucleon isospin:** $|\pi^+p\rangle=|\tfrac32,\tfrac32\rangle$, and $|\pi^-p\rangle$ has overlap $\tfrac13$ with $|\tfrac32,-\tfrac12\rangle$ in the sense $|\tfrac32,-\tfrac12\rangle=\sqrt{\tfrac13}|\pi^-p\rangle+\sqrt{\tfrac23}|\pi^0n\rangle$ (up to phase conventions). At the $\Delta(1232)$ peak, where only $I=\tfrac32$ contributes, show that the cross sections are in the ratio elastic $\pi^+p$ : elastic $\pi^-p$ : charge exchange $\pi^-p\to\pi^0n$ $=1:\tfrac19:\tfrac29$, so the *total* $\pi^-p$ cross section is $\tfrac13$ of $\pi^+p$ (the famous $3:1$ ratio). *Zettili:* **Problem 7.6** and Section 7.3.6.
6. **Rotation matrices:** rotate $|1,0\rangle$ about $y$ by $\beta$ with $d^1(\beta)$ and show the result is $\cos\beta\,|1,0\rangle-\frac{\sin\beta}{\sqrt2}\left(|1,1\rangle-|1,-1\rangle\right)$ (sign conventions vary); check that it is normalized and that for $\beta=\pi/2$ it is the eigenstate of $J_x$ with eigenvalue $0$. *Zettili:* Problems 7.9 and 7.10; Exercise 7.24.
7. **Two nucleons:** list the isospin $I=0,1$ states, and the exchange symmetry in isospin; combine with spin and orbital symmetry to show the deuteron ($I=0$, $S=1$, $L=0$) is consistent with the generalized Pauli principle. *Zettili:* Section 7.3.6; the generalized Pauli principle is in Section 8.3 (Module 07).
8. **Selection rule via Wigner-Eckart:** for an electric dipole operator $\vec r$ between $|\ell m\rangle$ states show $\Delta\ell=\pm1$ and $\Delta m=0,\pm1$; state the allowed transitions among $np,\ n'd$ levels. *Zettili:* Problems 7.7 and 7.8; Exercises 7.17, 7.25, 7.26.
9. **Landé factor:** compute $g_J$ for a state with $L,S,J$ via the projection theorem, and test for $^2P_{3/2}$ ($g=\frac43$) and $^2P_{1/2}$ ($g=\frac23$). *Zettili:* Section 9.2.3 (anomalous Zeeman effect) in Module 08.
10. **Baryon spin states:** combine three spin-1/2 quarks into $S=\frac32$ and two $S=\frac12$ multiplets (dimension count $2\times2\times2=4+2+2$), write $|\tfrac32,\tfrac32\rangle=\uparrow\uparrow\uparrow$ and the mixed-symmetry states (for later SU(6) arguments). *Zettili:* Problem 7.4 (three spin-1/2), Problems 7.3 and 7.5 (four spins); Exercises 7.32 and 7.33.

## Optional extension

Compute the Clebsch-Gordan coefficients of $\frac12\otimes\frac12\otimes\frac12$ via sequential coupling and relate the two mixed-symmetry doublets to the proton's spin-flavor wave function in the quark model.

## Pitfalls

- Condon-Shortley phase conventions: different books differ by signs. Choose one and state it.
- Confusing rotation matrices for states ($D$) with those for components of operators.
- Forgetting that $M=m_1+m_2$ is conserved.
- Treating isospin $I_3$ and charge $Q$ as identical: $Q=I_3+\frac B2+\frac S2$ or similar relations depending on the hadron.

## Gate questions

1. Why are the triplet states symmetric and the singlet antisymmetric under exchange of two spin-1/2 particles?
2. How does the Wigner-Eckart theorem reduce a table of matrix elements to a few reduced elements?
3. Why does the $\Delta(1232)$ appear strongly in $\pi^+p$ and with relative weight $1/3$ in $\pi^-p$?

## One-page cheat sheet contents

Triangle rule, CG tables for $\frac12\otimes\frac12$, $1\otimes\frac12$, $1\otimes1$, spin-orbit eigenvalues, $d^{1/2}$ and $d^1$ matrices, Wigner-Eckart statement.
