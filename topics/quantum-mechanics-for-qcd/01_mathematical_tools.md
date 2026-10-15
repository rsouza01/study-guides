# Module 01: Mathematical tools

**Zettili:** Chapter 2, *Mathematical Tools of Quantum Mechanics* (printed pp. 91–186; PDF pp. 111–206). Skim Section 2.4.8 (antilinear and antiunitary operators, Wigner theorem) now; you will need it for time reversal in Module 11.
**Time:** 2 weeks (about 8 h/week: 4 lunch blocks, 3 quiet evenings).

## Task 0 (already done for you)

The chapter, section and problem map below was built from your 3rd edition (all page numbers are printed pages; PDF page = printed + 20). Copy the module table of the overview into `notes/zettili_map.md` and keep it as your reference. Your edition has 13 chapters; Chapters 12 and 13 and Appendices D to F are new in the 3rd edition and are used in Modules 11 and 12.

## Zettili pin (exact, from your 3rd edition)

PDF page = printed page + 20.

| Section | Printed page | Role |
| --- | --- | --- |
| 2.2 Hilbert space and wave functions (2.2.1 to 2.2.4) | 91 | core |
| 2.3 Dirac notation | 97 | core |
| 2.4.1 to 2.4.7 operators, adjoint, projectors, commutator algebra, uncertainty, functions of operators, inverse and unitary operators | 104 to 113 | core |
| 2.4.8 Antilinear and antiunitary operators, Wigner theorem | 114 | skim (needed in Module 11) |
| 2.4.9 Eigenvalues and eigenvectors | 118 | core |
| 2.4.10 Infinitesimal and finite unitary transformations | 120 | core (generators) |
| 2.5 Representation in discrete bases (2.5.1 to 2.5.3) | 123 | core |
| 2.6 Representation in continuous bases (2.6.1 to 2.6.4) | 141 | core |
| 2.6.5 Parity operator | 148 | core |
| 2.7 Matrix and wave mechanics | 150 | skim |
| 2.9 Solved Problems 2.1 to 2.20 | 153 to 175 | exercise pool |
| 2.10 Exercises 2.1 to 2.55 | 176 to 186 | extra pool |
| Appendix A: the delta function | 937 | read with 2.6 |

**Solved problems to do:** 2.2 (projectors), 2.4 (sums and products of projectors), 2.6 and 2.7 (hermiticity of $X$, $d/dx$, $L$), 2.8 (unitarity conditions), 2.9 (commutators of powers), 2.11 to 2.14 (matrix eigenproblems), 2.15 (antiunitary times unitary), 2.16 (delta function), 2.19 and 2.20 (eigenfunctions and boundary conditions).
**Unsolved exercises worth doing:** 2.11, 2.12, 2.15, 2.16, 2.19, 2.20, 2.21, 2.27, 2.30 to 2.34, 2.36, 2.38, 2.44 to 2.47.
**Not in Zettili:** nothing essential; this chapter is complete for the module.

## Why this matters for QCD

Every QFT statement is about states and operators on a Hilbert space, so the formalism is the language, not a prerequisite you can skip. In particular:
- *Fock space* is built from the operator algebra you practice here.
- *Commuting observables* and simultaneous eigenbases underlie quantum numbers (spin, isospin, color charges).
- *Generators of transformations* (translations by momentum, rotations by angular momentum) are the template for Noether charges.
- *Delta functions and Fourier transforms* appear in every propagator.

## Skip-test (40 minutes, no notes)

1. Prove that a Hermitian operator has real eigenvalues and orthogonal eigenvectors for distinct eigenvalues.
2. Show that $e^{i\theta\,\hat n\cdot\vec\sigma}=\cos\theta+i\,\hat n\cdot\vec\sigma\,\sin\theta$.
3. Show that if $[A,B]=0$ and $A$ has a nondegenerate spectrum, every eigenvector of $A$ is an eigenvector of $B$.
4. Derive $e^{A}Be^{-A}=B+[A,B]+\tfrac1{2!}[A,[A,B]]+\dots$.
5. From $[x,p]=i\hbar$ show that in the position representation $p=-i\hbar\,d/dx$, and that $e^{-ipa/\hbar}$ translates a wave function by $a$.

If you can do all five, skip to Module 02.

## Prerequisites

Linear algebra (vector spaces, inner products, eigenvalues, diagonalization), calculus, complex numbers, Fourier series. Complex analysis is *not* required yet.

## Detailed topics (checklist)

**Hilbert space and Dirac notation**
- Complex vector spaces, inner products, norm, Cauchy-Schwarz inequality, orthonormal bases, completeness relation $\sum_n|n\rangle\langle n|=1$.
- Kets, bras, dual space, outer products, projection operators ($P^2=P=P^\dagger$).
- Finite versus infinite dimension, the space $L^2$ of square-integrable functions, continuous bases $|x\rangle$ and $|p\rangle$, non-normalizable states, delta-function normalization.

**Operators**
- Linear operators, matrix representations, adjoint, Hermitian, unitary, normal, projection operators, trace and its cyclic property, determinant.
- Eigenvalue problems, degeneracy, the spectral theorem (every Hermitian operator is diagonalizable in an orthonormal basis), diagonalizing a matrix.
- Functions of operators: power series, $e^{A}$, $f(A)$ through the spectral decomposition.
- Commutators and anticommutators, identities ($[AB,C]=A[B,C]+[A,C]B$), Jacobi identity, Hadamard lemma, Baker-Campbell-Hausdorff for operators whose commutator is a c-number: $e^{A+B}=e^Ae^Be^{-[A,B]/2}$.
- Commuting operators, complete sets of commuting observables (CSCO), simultaneous eigenbases.
- Unitary transformations, change of basis, generators of continuous unitary groups ($U=e^{-i\epsilon G}$).

**Representations**
- Position and momentum representations, $\langle x|p\rangle=\frac{1}{\sqrt{2\pi\hbar}}e^{ipx/\hbar}$, Fourier transform pairs, Parseval.
- The operators $x$ and $p$ in each representation, $p=-i\hbar\,\partial_x$, the commutator $[x,p]=i\hbar$, domain issues (a brief awareness, not a course in functional analysis).
- Dirac delta function: definition by integration, identities ($\delta(ax)$, $\delta(f(x))$, derivative), Fourier representation, Gaussian integrals.

## Reading plan (exact)

| Block | Reading |
| --- | --- |
| Lunch 1 | Sections 2.2 to 2.3 (pp. 91 to 104), then the worked examples with the answers covered |
| Lunch 2 | Sections 2.4.1 to 2.4.5 (pp. 104 to 112) |
| Lunch 3 | Sections 2.4.6 to 2.4.10 (pp. 112 to 123); skim 2.4.8 |
| Lunch 4 | Sections 2.5 (pp. 123 to 141) |
| Week 2 lunches | Sections 2.6 and 2.7 (pp. 141 to 152) and Appendix A (p. 937) |
| Evenings | Derivations from the list; then exercises (pool above) |

## Derive from scratch (derivation nights)

1. Cauchy-Schwarz inequality from positivity of the norm.
2. The spectral theorem for a $2\times2$ Hermitian matrix by explicit diagonalization (then state the general case).
3. The Hadamard lemma $e^{A}Be^{-A}=\sum_n\frac1{n!}[A,B]_n$ and the BCH formula for $[A,B]=c\,\mathbb 1$.
4. Position and momentum representations from $[x,p]=i\hbar$, and the momentum-space wave function of a Gaussian.
5. The identity $\delta(f(x))=\sum_i\delta(x-x_i)/|f'(x_i)|$.

## Bare-minimum exercises (find matching solved problems in the chapter; keywords in parentheses)

1. **Pauli algebra** (spin-1/2 matrices): verify $\sigma_i\sigma_j=\delta_{ij}+i\epsilon_{ijk}\sigma_k$, $\mathrm{Tr}\,\sigma_i\sigma_j=2\delta_{ij}$, and $(\vec\sigma\cdot\vec a)(\vec\sigma\cdot\vec b)=\vec a\cdot\vec b+i\vec\sigma\cdot(\vec a\times\vec b)$. *Zettili:* no direct problem; do Exercise 5.30 (Pauli matrices) in Module 04.
2. **Diagonalization** (eigenvalues of $2\times2$ and $3\times3$ Hermitian matrices): diagonalize $H=\begin{pmatrix}a&b\\b^*&d\end{pmatrix}$, give the eigenvalues $\frac{a+d}2\pm\sqrt{(\frac{a-d}2)^2+|b|^2}$ and the unitary matrix that diagonalizes it. *Zettili:* Problems 2.11 and 2.12; Exercises 2.19 and 2.37.
3. **Commuting operators** (simultaneous eigenvectors, degeneracy): construct a $3\times3$ example where $A$ is degenerate and show that $B$ must be diagonalized inside the degenerate subspace. *Zettili:* Problems 2.12 and 2.14; Exercises 2.27 and 2.29.
4. **Operator functions** (exponential of a matrix): compute $e^{i\theta\sigma_z}$ and $e^{i\theta\hat n\cdot\vec\sigma}$. *Zettili:* Exercises 2.15, 2.16, 2.35.
5. **Projection operators**: show that $P_n=|n\rangle\langle n|$ satisfy $P_nP_m=\delta_{nm}P_n$ and $\sum P_n=1$; write $A=\sum a_nP_n$. *Zettili:* Problems 2.1, 2.2, 2.4; Exercises 2.11, 2.12.
6. **Commutator identities**: compute $[x^n,p]$, $[x,p^n]$, $[x,f(p)]=i\hbar f'(p)$. *Zettili:* Problem 2.9; Exercises 2.30 to 2.34.
7. **Delta function**: evaluate $\int\delta(x^2-a^2)g(x)dx$, and the Fourier transform of $e^{-ax^2}$. *Zettili:* Problem 2.16; Exercises 2.44 to 2.46 (use Appendix A).
8. **Momentum representation**: for $\psi(x)=Ne^{-x^2/2\sigma^2}$ find $\phi(p)$, normalize, and confirm $\Delta x\,\Delta p=\hbar/2$. *Zettili:* Section 2.6.4 (p. 144); no dedicated problem.
9. **Trace and cyclic property**: show $\mathrm{Tr}(ABC)=\mathrm{Tr}(CAB)$ and that $[A,B]$ has zero trace in finite dimension, hence no finite-dimensional representation of $[x,p]=i\hbar$. *Zettili:* Exercises 2.20 and 2.21.
10. **Unitary change of basis**: given two bases of a qubit, find the unitary that relates them and show that matrix elements and traces are invariant. *Zettili:* Problem 2.8; Exercises 2.16, 2.38, 2.40.

## Optional extension

Look up (do not master) the difference between Hermitian and self-adjoint for unbounded operators, and why $p$ on a half line has no self-adjoint extension. One page of notes.

## Pitfalls

- Treating $|x\rangle$ and $|p\rangle$ as ordinary normalizable vectors.
- Assuming $e^{A+B}=e^Ae^B$ without checking commutation.
- Forgetting the complex conjugate when taking a bra.
- Confusing Hermitian with symmetric, and unitary with orthogonal.

## Gate questions

1. Why must the observable operators in QM be Hermitian?
2. What makes $x$ and $p$ conjugate in the sense that they cannot be simultaneously diagonalized?
3. Why does the commutator $[x,p]=i\hbar$ rule out finite-dimensional representations?

## One-page cheat sheet contents

Dirac notation rules, completeness relations, operator types and their defining relations, Hadamard lemma and BCH, $x$ and $p$ representations, delta-function identities.
