# Module 07: Identical particles

**Zettili:** Chapter 8, *Identical Particles* (printed pp. 503–536; PDF pp. 523–556). This is the shortest chapter: only five solved problems.
**Time:** 2 weeks.

## Zettili pin (exact, from your 3rd edition)

PDF page = printed page + 20.

| Section | Printed page | Role |
| --- | --- | --- |
| 8.1 Many-particle systems (Schrodinger equation, interchange symmetry, distinguishable noninteracting particles) | 503 to 507 | core |
| 8.2 Systems of identical particles (8.2.1 to 8.2.5: exchange degeneracy, symmetrization postulate, constructing symmetric and antisymmetric functions, noninteracting identical particles) | 508 to 515 | core |
| 8.3 The Pauli exclusion principle | 516 | core |
| 8.4 The exclusion principle and the periodic table | 517 to 523 | skim |
| 8.5 Solved Problems 8.1 to 8.5 | 524 to 532 | exercise pool |
| 8.6 Exercises 8.1 to 8.19 | 533 to 536 | extra pool |

**Solved problems to do:** 8.1 (three noninteracting particles in a box), 8.2 (three identical spin-1/2 particles), 8.3 ($N$ identical particles in a box), 8.4 and 8.5 (two noninteracting particles: states and energies). Add Problem 9.16 (two identical spin-1/2 particles in a box) and Problem 9.17 (two-electron atom) from Chapter 9.
**Unsolved exercises worth doing:** 8.1, 8.4 to 8.11, 8.12, 8.14 to 8.16.
**Not in Zettili:** the free Fermi gas as such (use the box problems and Griffiths or Fetter-Walecka), second quantization and occupation numbers (Module 12), and the $\Delta^{++}$/color argument (Halzen and Martin, chapter on the quark model).

## Why this matters for QCD

- **Quark statistics and color.** The $\Delta^{++}$ ($uuu$, spin $\tfrac32$, symmetric in space, spin and flavor) would violate the Pauli principle unless quarks carry another, antisymmetric degree of freedom: **color**. This is the cleanest argument you will see for why QCD has three colors.
- **Free Fermi gases** (nucleons, electrons, quarks) are the starting point of nuclear matter, neutron stars and the Walecka model.
- **Exchange symmetry** is the QM seed of the spin-statistics connection and of the (anti)commutation relations of QFT fields.
- **The occupation-number language** is second quantization in embryo (Module 12).

## Skip-test (40 minutes, no notes)

1. Define the exchange operator $P_{12}$; show $P_{12}^2=1$ and that for identical particles $[P_{12},H]=0$.
2. Construct the properly symmetrized (bosons) and antisymmetrized (fermions) two-particle states for single-particle states $\phi_a,\phi_b$.
3. Write the Slater determinant for three fermions in three orbitals and show it vanishes if two orbitals coincide.
4. Compute the Fermi energy of a free neutron gas of density $n=0.16$ fm$^{-3}$ (answer $\approx37$ MeV for spin-1/2).
5. Explain the symmetry of the two-electron ground state of helium: symmetric spatial part, antisymmetric spin singlet.

## Prerequisites

Modules 04 and 06 (spin states and coupling), and 05 (hydrogen-like orbitals).

## Detailed topics (checklist)

**Indistinguishability and symmetrization**
- Identical particles and the failure of classical labeling; the exchange operator; symmetric and antisymmetric states; the **symmetrization postulate** (bosons symmetric, fermions antisymmetric), the spin-statistics connection (stated as a theorem, proven in QFT: integer spin bosons, half-integer spin fermions).
- Constructing the symmetric and antisymmetric combinations from products; the exchange degeneracy and its removal.
- Many-particle states: $N$ fermions in a Slater determinant, $N$ bosons in a permanent, normalization factors $\frac{1}{\sqrt{N!}}$ and $\sqrt{\frac{N!}{\prod n_i!}}$.
- Counting states: two particles in a three-level system, distinguishable ($9$), bosons ($6$), fermions ($3$).

**Spin and spatial symmetry**
- Two spin-1/2 particles: triplet (symmetric) and singlet (antisymmetric) spin states; the total wave function $\Psi=\psi(\vec r_1,\vec r_2)\chi(s_1,s_2)$ antisymmetric; singlet requires symmetric space, triplet requires antisymmetric space.
- The exchange energy: the Coulomb (direct) and exchange integrals in helium excited states; why triplet states are lower in energy (Hund's rule origin).
- Helium: ground state, the variational estimate (Module 08), excited singlet (para) and triplet (ortho) states.

**Free Fermi gas**
- Particles in a box, density of states, the Fermi momentum $k_F=(6\pi^2n/g)^{1/3}$ with degeneracy $g$, the Fermi energy $\frac{\hbar^2k_F^2}{2m}$, the total energy $\frac35NE_F$, the pressure, the compressibility (degeneracy pressure); the extension to relativistic fermions (Module 11); the two-species gas (neutrons plus protons) and its isospin structure.

**Occupation-number representation (first look)**
- The state as a list of occupations $|n_1,n_2,\ldots\rangle$, creation and annihilation operators for bosons ($[a_i,a_j^\dagger]=\delta_{ij}$) and fermions ($\{a_i,a_j^\dagger\}=\delta_{ij}$), number operator $N=\sum a_i^\dagger a_i$, and how antisymmetry is encoded in the anticommutators. Used again in Module 12.

**Color and quarks (application)**
- Quark wave function: space $\otimes$ spin $\otimes$ flavor $\otimes$ color. For baryons in the ground state the space part is symmetric, the color singlet is antisymmetric, so the spin-flavor part must be symmetric: the SU(6) wave functions for the proton and the $\Delta$.

## Reading plan (exact)

| Block | Reading |
| --- | --- |
| Lunch 1 | Sections 8.1 (pp. 503 to 508) |
| Lunch 2 | Sections 8.2.1 to 8.2.3 (pp. 508 to 512) |
| Lunch 3 | Sections 8.2.4 to 8.2.5 and 8.3 (pp. 512 to 517) |
| Lunch 4 | Section 8.4 skim (pp. 517 to 523); Halzen and Martin on the $\Delta^{++}$ |
| Week 2 lunches | Review; Fetter and Walecka chapter 1 (occupation numbers) |
| Evenings | Derivations; then Problems 8.1 to 8.5, 9.16, 9.17; exercises |

## Derive from scratch (derivation nights)

1. The Slater determinant and its normalization, and the Pauli principle from it.
2. The spin singlet and triplet exchange symmetries, and the link to the space symmetry for electrons.
3. Fermi momentum, Fermi energy and total energy of a free Fermi gas in a box: $n=\frac{g}{6\pi^2}k_F^3$, $E/N=\frac35E_F$.
4. The direct and exchange integrals for two electrons in orbitals $\phi_a,\phi_b$: $E=E_a+E_b+J\pm K$.
5. The $\Delta^{++}$ argument: write the wave function of $\Delta^{++}$ with $S_z=\frac32$ and show it is symmetric under quark exchange without color.

## Bare-minimum exercises (solved-problem keywords: identical particles, symmetrization, Slater determinant, helium, exchange, Pauli)

1. **Two-particle states:** for two fermions in states $|a\rangle,|b\rangle$ construct $|\Psi\rangle=\frac{1}{\sqrt2}(|ab\rangle-|ba\rangle)$ and show $|\Psi\rangle=0$ for $a=b$. *Zettili:* Problem 8.5; Exercises 8.4 and 8.5.
2. **Counting:** two identical bosons or fermions distributed over a 3-level system: count states and compare with distinguishable particles ($6$, $3$, $9$). *Zettili:* Problem 8.1; Exercise 8.1.
3. **Spin-statistics symmetric:** two spin-1/2 particles in the $|\uparrow\uparrow\rangle$ state: determine the allowed spatial symmetry (antisymmetric); for the singlet (symmetric). *Zettili:* Problem 8.2; Exercises 8.14 and 8.15; Problem 9.16.
4. **Three fermions:** write the Slater determinant for three spin-1/2 electrons in the 1s orbital with both spins and a 2s orbital with one spin. *Zettili:* Problem 8.2; Exercises 8.9 to 8.11 and 8.16.
5. **Fermi energy of nucleons:** with $n_0=0.16$ fm$^{-3}$ and degeneracy 4 (symmetric nuclear matter), $k_F=1.33$ fm$^{-1}$ and $E_F\approx37$ MeV (verify); with degeneracy 2 for pure neutron matter, $k_F=(3\pi^2n)^{1/3}=1.68$ fm$^{-1}$ and $E_F\approx58$ MeV (verify). *Zettili:* Problem 8.3; Exercises 8.7 and 8.8.
6. **Degeneracy pressure:** derive $P=\frac25nE_F$ for a nonrelativistic Fermi gas and evaluate it at $n_0=0.16$ fm$^{-3}$ ($\approx2.4$ MeV/fm$^3$ for symmetric matter and $\approx3.7$ MeV/fm$^3$ for pure neutron matter; verify). *Zettili:* extension of Problem 8.3; no dedicated problem.
7. **Exchange energy sign:** for the helium $1s2s$ configuration show that the triplet lies below the singlet by $2K$ with $K>0$. *Zettili:* Problem 9.17; Exercise 8.12 (spinless-boson helium, as a contrast).
8. **Bosonic enhancement:** the probability for two non-interacting identical bosons to be found at the same position is twice that for distinguishable particles; contrast with the fermion zero. *Zettili:* Exercise 8.1.
9. **$\Delta^{++}$ and color:** write the spin-flavor wave function for $\Delta^{++}$ ($u\uparrow u\uparrow u\uparrow$), show it is symmetric, and conclude that an antisymmetric color singlet $\epsilon_{abc}/\sqrt6$ makes the total antisymmetric. *Zettili:* not covered; Halzen and Martin. Section 8.3 states the Pauli principle.
10. **Occupation numbers:** for fermionic modes $a_1,a_2$ with $\{a_i,a_j^\dagger\}=\delta_{ij}$ write all four states $|n_1n_2\rangle$ and the action of $a_1^\dagger a_2$ including the sign from anticommutation. *Zettili:* not covered; Fetter and Walecka chapter 1 (Module 12).

## Optional extension

Construct the SU(6) proton wave function (flavor-spin symmetric combination of mixed-symmetry flavor and spin states) and compute the proton magnetic moment ratio $\mu_n/\mu_p=-\tfrac23$ in the quark model (observed $-0.685$).

## Pitfalls

- Applying the symmetrization postulate to the spatial part only, forgetting spin.
- Treating the Pauli principle as a force rather than a symmetry constraint.
- Dropping the normalization factors in Slater determinants.
- Confusing the degeneracy factor $g$ (spin and isospin states) in the Fermi momentum formula.

## Gate questions

1. Why does exchange symmetry lead to a quantum "force" even without interaction?
2. Why did the $\Delta^{++}$ require a new quantum number?
3. How do the anticommutation relations of fermion operators encode the antisymmetry of many-fermion states?

## One-page cheat sheet contents

Symmetrization rules, Slater determinant, spin singlet/triplet symmetry, Fermi gas formulas ($k_F$, $E_F$, $P$), occupation-number commutators, color-antisymmetry argument.
