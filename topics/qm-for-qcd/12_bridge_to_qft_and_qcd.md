# Module 12: Bridge to QFT and QCD (beyond Zettili)

**Zettili:** Chapter 13, *Beyond Relativistic Quantum Mechanics* (printed pp. 897–936; PDF pp. 917–956), Appendix F (Lagrangian and Hamiltonian mechanics, canonical quantization, pp. 979–992) and Sections 3.7 to 3.8 (symmetries, Poisson brackets). For the path integral, second quantization and SU(3), the reading comes from the supplementary books.
**Time:** 3 weeks.

## Zettili pin (exact, from your 3rd edition)

PDF page = printed page + 20. The 3rd edition now gives you part of this module's content: classical field theory with Lagrangians, the Lagrangian derivations of the Klein-Gordon and Dirac equations, and a short introduction to QFT and the QED Lagrangian. The path integral, second quantization and group theory are still not in the book.

| Section | Printed page | Role |
| --- | --- | --- |
| Appendix F.1 Lagrangian formulation of classical mechanics | 979 | read first |
| Appendix F.2 Hamiltonian formulation | 984 | read first |
| Appendix F.3 Canonical quantization: from classical to quantum mechanics | 989 | core |
| Sections 3.7 and 3.8 (symmetries and conservation laws; Poisson brackets) | 207 to 215 | revisit |
| 13.2 Advantages of Lagrangians in field theories | 898 | core |
| 13.3 Lagrangians in classical field theory | 899 | core |
| 13.4 Lagrangian derivation of the Maxwell equations | 903 to 910 | skim |
| 13.5 Lagrangian derivation of the Klein-Gordon equation | 911 | core |
| 13.6 Lagrangian derivation of the Dirac equation | 915 | core |
| 13.7 Beyond classical field theory: quantum field theory | 919 | core |
| 13.8 The Lagrangian of quantum electrodynamics | 920 | core |
| 13.9 Concluding thoughts | 922 | read |
| 13.10 Solved Problems 13.1 to 13.7 | 923 to 933 | exercise pool |
| 13.11 Exercises 13.1 to 13.8 | 934 to 936 | extra pool |

**Solved problems to do:** 13.1 (Hamiltonian formulation of classical fields), 13.5 (massive vector field Lagrangian), 13.6 (Dirac equation from a Lagrangian), 13.7 (electron coupled to the electromagnetic field).
**Unsolved exercises worth doing:** 13.6 to 13.8.
**Not in Zettili:** second quantization and the Fock space (Fetter and Walecka ch. 1, or Klauber), the path integral (Shankar, or Feynman and Hibbs), intrinsic C and P of hadrons, and SU(2)/SU(3) group theory for isospin, flavor and color (Halzen and Martin, Georgi, Cahn). Keep those parts of the module as written.

## Why this matters for QCD

This is the "missing QM" module: the three pieces that Zettili and Griffiths do not give you but that Klauber, Walecka and every QCD text assume.

1. **Second quantization**: the Fock space and the creation and annihilation operators for many-body systems and for fields.
2. **The path integral**: the other formulation of QM, and the one from which gauge theories are quantized and lattice QCD is defined.
3. **Symmetries and groups**: Noether's theorem, discrete symmetries (P, C, T), and the groups SU(2) (isospin) and SU(3) (flavor and color) that define QCD.

## Skip-test (40 minutes, no notes)

1. Write the single-mode boson and fermion algebras and show $[N,a^\dagger]=a^\dagger$.
2. Write the path-integral expression for $\langle x_b|e^{-iHt/\hbar}|x_a\rangle$ and the free-particle propagator $K=\sqrt{\frac{m}{2\pi i\hbar t}}\exp\left[\frac{im(x_b-x_a)^2}{2\hbar t}\right]$.
3. State Noether's theorem for a continuous symmetry and give the conserved quantities for translation, rotation and phase invariance.
4. State the C, P eigenvalues of the $\pi^0$ and explain why $\pi^0\to\gamma\gamma$ is allowed but $\pi^0\to\gamma\gamma\gamma$ is forbidden.
5. Decompose $3\otimes\bar3$ and $3\otimes3\otimes3$ of SU(3).

## Prerequisites

Modules 03 (oscillator), 07 (identical particles, occupation numbers), 09 (interaction picture), 10 (Green's functions), 11 (Dirac equation). The $SU(2)$ material of Modules 04 and 06.

## Detailed topics (checklist)

### A. Second quantization

- Fock space for bosons and fermions, the occupation-number basis, the vacuum, creation and annihilation operators: $[a_i,a_j^\dagger]=\delta_{ij}$ (bosons), $\{a_i,a_j^\dagger\}=\delta_{ij}$ (fermions), number operator, the normalization of $(a^\dagger)^n|0\rangle$.
- One-body and two-body operators in second quantization: $T=\sum_{ij}\langle i|t|j\rangle a_i^\dagger a_j$, $V=\frac12\sum\langle ij|v|kl\rangle a_i^\dagger a_j^\dagger a_la_k$; the field operators $\psi(\vec x)=\sum_k\phi_k(\vec x)a_k$ with $[\psi(\vec x),\psi^\dagger(\vec y)]_\mp=\delta^3(\vec x-\vec y)$; Hamiltonian $H=\int\psi^\dagger\left(-\frac{\hbar^2\nabla^2}{2m}\right)\psi+\frac12\int\!\!\int\psi^\dagger\psi^\dagger V\psi\psi$.
- The free scalar field as a collection of oscillators: $\phi(\vec x)=\int\frac{d^3k}{(2\pi)^3}\frac{1}{\sqrt{2\omega_k}}\left(a_ke^{i\vec k\cdot\vec x}+a_k^\dagger e^{-i\vec k\cdot\vec x}\right)$, $H=\int\frac{d^3k}{(2\pi)^3}\omega_k\left(a^\dagger_ka_k+\frac12\right)$, normal ordering and the vacuum energy.
- Wick's theorem for the two-point function (awareness: the origin of Feynman propagators), the Fermi sea and particle-hole excitations (link to the Fermi gas of Module 07).

### B. The path integral

- Derivation of the propagator as a sum over paths: time-slicing, $K=\lim\int\prod dx_i\,e^{iS/\hbar}$, the classical action $S=\int L\,dt$, the stationary-phase (classical) limit.
- The free particle and the harmonic oscillator (Gaussian integrals), the relation of $K$ to the energy spectrum, the Green's function $G(E)=\frac{1}{E-H+i\epsilon}$ and the Fourier transform of $K$.
- **Euclidean (imaginary-time) path integral:** $t\to-i\tau$, $e^{-S_E/\hbar}$, the thermal partition function $Z=\mathrm{Tr}\,e^{-\beta H}=\int_{x(0)=x(\beta\hbar)}\mathcal Dx\,e^{-S_E/\hbar}$, the ground state as the large-time limit. This is the formulation used in lattice QCD.
- Perturbation theory from the path integral (generating functional, Gaussian integrals with sources) as a preview of Feynman diagrams.

### C. Symmetries, conservation laws and discrete symmetries

- Noether's theorem in Lagrangian mechanics and in field theory: translation $\to$ energy-momentum, rotation $\to$ angular momentum, global phase $\to$ charge/number conservation; the QM version via unitary operators (Module 02).
- Discrete symmetries: parity ($\psi\to\gamma^0\psi(-\vec x)$ for Dirac fields), charge conjugation, time reversal (antiunitary); intrinsic parities and C-parities of particles ($\pi$: $0^-$, $\pi^0$: $C=+1$; $\rho$: $1^{--}$; photon: $C=-1$), selection rules, **G-parity** (awareness); the CPT theorem (statement).
- Symmetry breaking (spontaneous versus explicit): examples (ferromagnet, the $\sigma$ model), Goldstone's theorem (statement), the role of the pion as an approximate Goldstone boson.

### D. Group theory for QCD: SU(2) to SU(3)

- Lie groups and Lie algebras: generators, structure constants, representations, Casimir operators; $SU(2)$ revisited (Modules 04 and 06): isospin $I=0,\frac12,1,\frac32$; the relation of $SU(2)$ and $SO(3)$.
- $SU(3)$: Gell-Mann matrices $\lambda_a$, generators $T^a=\lambda_a/2$, $[T^a,T^b]=if^{abc}T^c$ with $f^{123}=1$, $f^{147}=\frac12$, $f^{458}=\frac{\sqrt3}{2}$, $\mathrm{Tr}(T^aT^b)=\frac12\delta^{ab}$; fundamental $3$, antifundamental $\bar3$, adjoint $8$; the weight diagrams (isospin $I_3$ and hypercharge $Y$); Casimirs $C_F=\frac43$ and $C_A=3$.
- Tensor products: $3\otimes\bar3=1\oplus8$ (mesons), $3\otimes3=\bar3\oplus6$, $3\otimes3\otimes3=1\oplus8\oplus8\oplus10$ (baryons).
- **Flavor SU(3):** the octet and decuplet of baryons, the meson nonet, the Gell-Mann-Okubo mass formula (awareness). **Color SU(3):** the quark colors $3$, gluons in the $8$, color singlet hadrons, the color factors $C_F$ in the $q\bar q$ potential.
- Isospin and strangeness: $Q=I_3+\frac{Y}{2}$ with $Y=B+S$.

## Reading plan (exact)

| Week | Reading |
| --- | --- |
| Week 1 (second quantization) | Fetter and Walecka chapter 1; Klauber's first chapters; then Zettili Appendix F (pp. 979 to 992) |
| Week 2 (fields, path integral) | Zettili Sections 13.2 to 13.9 (pp. 898 to 923); Shankar or Feynman and Hibbs for the path integral |
| Week 3 (symmetries and groups) | Zettili Sections 3.7 to 3.8 and 12.4.21 to 12.4.25 for C, P, T; Halzen and Martin or Griffiths (particle physics) for SU(2) and SU(3); Cahn or Georgi for the algebra |
| Evenings | Derivations; then Problems 13.1 and 13.5 to 13.7; the exercises of this module |

## Derive from scratch (derivation nights)

1. The path-integral propagator from time slicing (insert completeness relations, Gaussian integrals), and the free-particle result.
2. The partition function of the oscillator from the energy spectrum and from the Euclidean path integral: $Z=\frac{1}{2\sinh(\beta\hbar\omega/2)}$.
3. The second-quantized form of a one-body operator and of the Hamiltonian of a Fermi gas with a contact interaction.
4. Noether's theorem for a global phase symmetry of $\mathcal L=\psi^*(i\partial_t+\frac{\nabla^2}{2m})\psi$: the conserved current and charge.
5. The commutation relations of the Gell-Mann matrices: $[\lambda_1,\lambda_2]=2i\lambda_3$, and $\sum_aT^aT^a=C_F\mathbb 1$ with $C_F=\frac43$.

## Bare-minimum exercises

1. **Free-particle propagator:** compute $K(x,t;x',0)$ by the Fourier integral $\int\frac{dp}{2\pi\hbar}e^{ip(x-x')/\hbar-ip^2t/2m\hbar}$ and confirm $K\to\delta(x-x')$ as $t\to0$. *Zettili:* not covered (path integral); Shankar or Feynman and Hibbs.
2. **Oscillator partition function:** show $\mathrm{Tr}\,e^{-\beta H}=\sum_ne^{-\beta\hbar\omega(n+\frac12)}=\frac1{2\sinh(\beta\hbar\omega/2)}$, and derive the mean energy $\langle E\rangle=\frac{\hbar\omega}{2}\coth\frac{\beta\hbar\omega}{2}$; take $\beta\to\infty$ to extract the ground-state energy (the lattice-QCD logic). *Zettili:* not covered; a statistical-mechanics text (compare the oscillator spectrum of Section 4.8).
3. **Fock space:** for two fermionic modes list the four states, compute $a_1^\dagger a_2|01\rangle$ and $H=\epsilon_1n_1+\epsilon_2n_2+Un_1n_2$ on each; for bosons compute $(a^\dagger)^3|0\rangle$ and its norm. *Zettili:* not covered; Fetter and Walecka chapter 1.
4. **Field commutators:** from $[a_k,a_{k'}^\dagger]=(2\pi)^3\delta^3(\vec k-\vec k')$ show $[\phi(\vec x),\pi(\vec y)]=i\delta^3(\vec x-\vec y)$ with $\pi=\dot\phi$. *Zettili:* Appendix F.3, Section 13.3; Exercise 13.8 (scalar field equations of motion).
5. **Noether charge:** show that the number operator $N=\int\psi^\dagger\psi$ commutes with $H$ for a number-conserving Hamiltonian. *Zettili:* Section 3.7.3; Section 13.3; Problem 13.1.
6. **C and P selection rules:** show that $C(\pi^0)=+1$ and $C(\gamma)=-1$ allow $\pi^0\to2\gamma$ and forbid $\pi^0\to3\gamma$; use P to forbid a $0^+\to0^-$ electric dipole transition. *Zettili:* Sections 12.4.21 to 12.4.23; Problems 12.26, 12.27, 12.31.
7. **SU(3) algebra:** verify $\mathrm{Tr}(\lambda_a\lambda_b)=2\delta_{ab}$, $[\lambda_1,\lambda_2]=2i\lambda_3$, the structure constants $f^{147}=\tfrac12$ and $f^{458}=\tfrac{\sqrt3}{2}$, and $T^aT^a=\frac43\cdot1$ on the fundamental. *Zettili:* not covered; Halzen and Martin, Georgi, or Cahn.
8. **Representation counting:** show that $3\times\bar3=9=1+8$ and $3\times3\times3=27=1+8+8+10$ by weights ($I_3,Y$); identify the baryon octet and decuplet. *Zettili:* not covered; same references.
9. **Color singlet baryon:** show $\epsilon_{abc}q^aq^bq^c$ is invariant under $SU(3)$ color (using $\det U=1$) and antisymmetric in color indices, and connect to the $\Delta^{++}$ problem of Module 07. *Zettili:* not covered.
10. **Color factors:** using $\vec T_1\cdot\vec T_2=\frac12(C_{\rm tot}-C_1-C_2)$ show the one-gluon-exchange potential between $q\bar q$ in a color singlet is $-\frac43\frac{\alpha_s}{r}$ (attractive, factor $-C_F$) and between $qq$ in the $\bar3$ is $-\frac23\frac{\alpha_s}{r}$. *Zettili:* not covered.

## Optional extension

Compute the Euclidean path-integral ground-state energy of the anharmonic oscillator numerically with a Metropolis Monte Carlo on a time lattice (about 60 lines of Python): discretize $\tau$, update paths, measure $\langle x^2\rangle$ and the energy via the virial theorem, and compare with the diagonalization result. This is a miniature lattice calculation.

## Pitfalls

- Mixing conventions for field normalization ($\frac{1}{\sqrt{2\omega}}$ versus $\frac{1}{\sqrt{2\omega(2\pi)^3}}$) and measure ($d^3k/(2\pi)^3$ versus $d^3k$) between QFT texts. Fix one convention (Klauber's) and stay with it.
- Treating the path integral as a rigorous mathematical object: it is a computational definition, rigorous only after discretization or Wick rotation.
- Forgetting that the structure constants and normalization of the generators ($\mathrm{Tr}\,T^aT^b=\frac12\delta^{ab}$) fix the value of $C_F$ and $C_A$.
- Confusing flavor SU(3) (an approximate global symmetry) with color SU(3) (an exact gauge symmetry).

## Gate questions

1. Why is every free quantum field a collection of harmonic oscillators?
2. What does it mean to say "the ground state dominates at large Euclidean time", and why is it useful for lattice QCD?
3. Why is the color SU(3) a gauge symmetry while the flavor SU(3) is only an approximate global symmetry?

## One-page cheat sheet contents

Fock space algebra, field expansion, path-integral propagator and oscillator partition function, Noether charges, C and P table for light hadrons, Gell-Mann matrices and structure constants, SU(3) tensor products, color factors.
