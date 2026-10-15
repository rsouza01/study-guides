# Module 11: Relativistic quantum mechanics

**Zettili:** Chapter 12, *Relativistic Quantum Mechanics* (printed pp. 707–896; PDF pp. 727–916), new in the 3rd edition, with Appendices D and E (index notation and relativistic notation, pp. 951–978) as the notation primer.
**Time:** 3 weeks.

## Zettili pin (exact, from your 3rd edition)

PDF page = printed page + 20. This chapter is much larger than my original Module 11; it covers the Klein-Gordon and Dirac equations in detail, including Weyl fermions, chirality, discrete symmetries and the CPT theorem.

| Section | Printed page | Role |
| --- | --- | --- |
| Appendix D (index notation) and E (relativistic notation, four-vectors) | 951 to 978 | read first |
| 12.2 Four-vectors and the Minkowski metric | 709 to 714 | skim |
| 12.3.1 to 12.3.3 Klein-Gordon equation: genesis, free particle and covariance, nonrelativistic limit | 715 to 720 | core |
| 12.3.4 Conceptual problems of the Klein-Gordon equation | 721 | core |
| 12.3.5 Klein paradox for spin-0 particles | 725 | core |
| 12.3.6 to 12.3.7 KG in an electromagnetic field and its nonrelativistic limit | 731 to 733 | skim |
| 12.4.1 to 12.4.5 Dirac equation for a free particle, matrices, properties, representations (Dirac, Weyl, Majorana), covariant form | 735 to 748 | core |
| 12.4.6 to 12.4.7 Lorentz covariance and the continuity equation | 749 to 755 | core |
| 12.4.8 to 12.4.9 Free-particle solutions at rest and in motion | 756 to 762 | core |
| 12.4.10 to 12.4.12 Negative energies: hole theory, Feynman-Stueckelberg, Klein paradox for spin-1/2 | 763 to 776 | core |
| 12.4.13 to 12.4.14 Spin-half solutions and helicity | 777 to 783 | core |
| 12.4.15 to 12.4.18 Massless particles: Weyl fermions, parity violation, neutrinos, chirality | 784 to 792 | core for QCD and the weak interaction |
| 12.4.19 to 12.4.20 Dirac equation in an EM field; nonrelativistic limit | 793 to 799 | core ($g=2$) |
| 12.4.21 to 12.4.24 Discrete symmetries: charge conjugation, parity, time reversal | 800 to 814 | core |
| 12.4.25 The CPT theorem | 815 | core |
| 12.5 to 12.6 Successes, limitations, beyond relativistic QM | 817 to 819 | read |
| 12.7 Solved Problems 12.1 to 12.37 | 819 to 888 | exercise pool |
| 12.8 Exercises 12.2 to 12.43 | 889 to 896 | extra pool |

**Solved problems to do:** 12.9 (free Klein-Gordon solutions), 12.10 and 12.11 (Dirac matrix algebra and traces), 12.12 (free Dirac eigenstates), 12.13 to 12.16 (slashed quantities, covariant and contravariant matrices), 12.17 and 12.18 (rotation and boost matrices $S$), 12.20 to 12.25 (spinors, helicity, conservation of $J$ but not $L$), 12.26 and 12.27 (parity and charge conjugation of spinors), 12.29 and 12.30 (step potentials: Klein paradox for spin-1/2 and spin-0), 12.31 and 12.32 (current under parity, chiral states under parity), 12.34 to 12.37 (helicity eigenstates).
**Unsolved exercises worth doing:** 12.20 to 12.28, 12.30, 12.33 to 12.43.
**Not in Zettili:** the exact Dirac solution for hydrogen (fine structure from the Dirac equation) and the Dirac equation in scalar plus vector potentials (the Walecka mean field). Use Sakurai's *Advanced Quantum Mechanics* or Bjorken and Drell, and Walecka. (The nonrelativistic limit and spin-orbit term are in 12.4.20; compare with Section 9.2.3.)

## Why this matters for QCD

- **The Dirac equation is the equation of motion of the quark field and of the nucleon field.** The structure $\gamma^\mu$, $\bar\psi=\psi^\dagger\gamma^0$, spinors $u$ and $v$, helicity and chirality is the working vocabulary of QCD and of the electroweak theory.
- **Antiparticles** appear as the resolution of the negative-energy problem: the first, still-quantum-mechanical encounter with the need for field theory.
- **Dirac particle in scalar and vector potentials** is exactly the mean-field nucleon in the Walecka (quantum hadrodynamics) model: $M^*=M-g_\sigma\sigma$, energy $E=\sqrt{p^2+M^{*2}}+g_\omega\omega_0$, and the origin of the strong spin-orbit force in nuclei.
- **Parity, charge conjugation and the structure of the Lorentz group** (rotations plus boosts, $SL(2,\mathbb C)$) prepare Klauber's treatment of fields.

## Skip-test (40 minutes, no notes)

1. Derive the Klein-Gordon equation from $E^2=p^2c^2+m^2c^4$ and explain the two problems with it as a single-particle equation (negative densities, negative energies).
2. Write the Dirac Hamiltonian $H=c\vec\alpha\cdot\vec p+\beta mc^2$ and derive the requirements $\{\alpha_i,\alpha_j\}=2\delta_{ij}$, $\{\alpha_i,\beta\}=0$, $\alpha_i^2=\beta^2=1$; give the Dirac representation.
3. Write the covariant form $(i\gamma^\mu\partial_\mu-m)\psi=0$ with $\gamma^0=\beta$, $\gamma^i=\beta\alpha_i$, $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$.
4. Give the positive-energy free solution $u(\vec p,s)=\sqrt{E+m}\begin{pmatrix}\chi_s\\\frac{\vec\sigma\cdot\vec p}{E+m}\chi_s\end{pmatrix}$ and the non-relativistic limit.
5. Show $J=L+S$ with $\vec S=\frac\hbar2\vec\Sigma$ commutes with $H_D$ while $\vec L$ alone does not.

## Prerequisites

Modules 04 (spin, Pauli matrices), 05 (hydrogen), 06 (angular momentum coupling), 08 (fine structure). Special relativity (four-vectors, Lorentz transformations).

## Detailed topics (checklist)

**Klein-Gordon equation**
- Derivation, plane-wave solutions with $E=\pm\sqrt{p^2c^2+m^2c^4}$, the conserved current $j^\mu=\frac{i\hbar}{2m}(\phi^*\partial^\mu\phi-\phi\partial^\mu\phi^*)$ with $\rho$ not positive-definite, the non-relativistic limit giving Schrodinger, coupling to an electromagnetic field ($\partial\to\partial+iqA$), the Klein-Gordon Coulomb problem (spin-0 "hydrogen"), the physical interpretation (a field equation for spin-0 particles, e.g., pions).

**Dirac equation**
- Linearization of $E^2=p^2+m^2$, the matrices $\alpha_i,\beta$ (at least $4\times4$), the Dirac and Weyl (chiral) representations, the covariant form with $\gamma^\mu$, the adjoint spinor $\bar\psi$, the conserved current $j^\mu=\bar\psi\gamma^\mu\psi$ with $j^0=\psi^\dagger\psi\ge0$.
- Free-particle solutions: positive-energy $u(\vec p,s)$ and negative-energy $v(\vec p,s)$ spinors, orthogonality and completeness relations (in the form $\sum_su\bar u=\gamma\cdot p+m$, $\sum_sv\bar v=\gamma\cdot p-m$), spin sums, helicity states.
- Spin: the spin operator $\vec\Sigma$, conservation of $\vec J$ and non-conservation of $\vec L$, helicity $\frac{\vec\Sigma\cdot\vec p}{|\vec p|}$ conserved for free particles, chirality $\gamma^5$ and the massless limit.

**Electromagnetic coupling and the Pauli limit**
- Minimal coupling $\vec p\to\vec p-q\vec A$, $E\to E-q\phi$; reduction to the Pauli equation, **$g=2$ for the electron**, the magnetic moment $\mu=\frac{q\hbar}{2m}$, the spin-orbit term and the Darwin term (Foldy-Wouthuysen expansion up to $1/m^2$): $H\approx mc^2+\frac{p^2}{2m}-\frac{p^4}{8m^3c^2}+q\phi-\frac{q\hbar}{2m}\vec\sigma\cdot\vec B+\frac{q\hbar^2}{8m^2c^2}\nabla^2\phi+\frac{q\hbar}{4m^2c^2}\vec\sigma\cdot(\nabla\phi\times\vec p)$ (verify signs in your book).

**Hydrogen in the Dirac theory (not in Zettili's Chapter 12; use Sakurai's *Advanced Quantum Mechanics* or Bjorken and Drell)**
- Separation into radial and angular (spin-angle) functions, the quantum number $\kappa=\mp(j+\frac12)$, the exact spectrum $E_{nj}=mc^2\left[1+\frac{(Z\alpha)^2}{(n-\delta_j)^2}\right]^{-1/2}$ with $\delta_j=j+\tfrac12-\sqrt{(j+\tfrac12)^2-(Z\alpha)^2}$, the expansion reproducing the fine structure of Module 08, the degeneracy of $2S_{1/2}$ and $2P_{1/2}$ (lifted by the Lamb shift, a QED effect), the breakdown at $Z\alpha>1$.

**Negative-energy states and antiparticles**
- The Dirac sea (hole theory), the interpretation of holes as positrons, Klein paradox (reflection coefficient exceeds 1 for a strong step), Zitterbewegung (interference of positive and negative energy components), charge conjugation $\psi^c=C\bar\psi^T$, parity $\psi\to\gamma^0\psi(-\vec x)$, time reversal (awareness). The need for a many-particle (field) theory.

**Lorentz covariance**
- Transformation of the spinor $\psi'(x')=S(\Lambda)\psi(x)$ with $S=\exp\left(-\frac i4\omega_{\mu\nu}\sigma^{\mu\nu}\right)$, $\sigma^{\mu\nu}=\frac i2[\gamma^\mu,\gamma^\nu]$; $\bar\psi\psi$ scalar, $\bar\psi\gamma^\mu\psi$ vector, $\bar\psi\gamma^5\psi$ pseudoscalar, $\bar\psi\gamma^\mu\gamma^5\psi$ axial vector (the bilinear classification).

**Dirac equation in scalar and vector potentials (the nuclear application)**
- With a scalar potential $S$ and a vector potential $V$: $[\vec\alpha\cdot\vec p+\beta(M-S)+V]\psi=E\psi$. For uniform fields the spectrum is $E=V\pm\sqrt{p^2+(M-S)^2}$; the effective mass $M^*=M-S$; in nuclei $S\approx-350$ MeV and $V\approx+300$ MeV (large and nearly opposite), which add in the spin-orbit potential. This is the content of the relativistic mean-field model.

## Reading plan (exact)

| Block | Reading |
| --- | --- |
| Lunch 1 | Appendix D (pp. 951 to 960) and E (pp. 961 to 978), skim Section 12.2 |
| Lunch 2 | Section 12.3 (pp. 715 to 734) |
| Lunch 3 | Sections 12.4.1 to 12.4.5 (pp. 735 to 749) |
| Lunch 4 | Sections 12.4.6 to 12.4.9 (pp. 749 to 763) |
| Week 2 lunches | Sections 12.4.10 to 12.4.14 (pp. 763 to 784) |
| Week 3 lunches | Sections 12.4.15 to 12.4.25 (pp. 784 to 817) |
| Evenings | Derivations; then Problems 12.9 to 12.37; exercises; Walecka or Bjorken-Drell for what Zettili lacks |

## Derive from scratch (derivation nights)

1. The Dirac matrices from the requirement $E^2=p^2+m^2$; verify the Dirac representation satisfies the algebra.
2. The free solutions $u,v$, normalization $\bar uu=2m$ or $u^\dagger u=2E$, and the spin sums.
3. The conservation of $\vec J$ and non-conservation of $\vec L$ via $[H,\vec L]=-ic\hbar\vec\alpha\times\vec p$.
4. The Pauli limit: eliminate the small components, show $g=2$ and the spin-orbit term.
5. The Dirac hydrogen spectrum via the squared Dirac equation or the radial method, and the expansion to order $\alpha^4$.
6. The uniform scalar plus vector potential spectrum $E=V+\sqrt{p^2+(M-S)^2}$.

## Bare-minimum exercises (solved-problem keywords: Klein-Gordon, Dirac matrices, free particle spinor, magnetic moment, Dirac hydrogen, negative energy, Klein paradox)

1. **Klein-Gordon density:** show $\rho$ can be negative for a superposition of positive and negative energy waves. *Zettili:* Section 12.3.4; Problem 12.9.
2. **Dirac algebra:** verify $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$ in the Dirac representation, $(\gamma^0)^2=1$, $(\gamma^i)^2=-1$, $\gamma^5=i\gamma^0\gamma^1\gamma^2\gamma^3$, $\{\gamma^5,\gamma^\mu\}=0$. *Zettili:* Problems 12.10, 12.11, 12.13 to 12.15; Exercises 12.20 to 12.28.
3. **Free spinor:** for $\vec p=p\hat z$ write $u(\vec p,\uparrow)$ and $u(\vec p,\downarrow)$; verify that they satisfy the Dirac equation and that helicity is conserved. *Zettili:* Problem 12.12; Section 12.4.9; Exercises 12.33 to 12.35.
4. **Dirac implies Klein-Gordon:** apply $(i\gamma\cdot\partial+m)$ to the Dirac equation and obtain $(\Box+m^2)\psi=0$. *Zettili:* Sections 12.4.1 to 12.4.5; Exercise 12.30.
5. **Spin non-conservation:** show $[H_D,\vec L]\ne0$ and $[H_D,\vec J]=0$. *Zettili:* Problems 12.21 to 12.24 (helicity commutes with $H$, $L$ does not).
6. **Magnetic moment:** reduce the Dirac equation with minimal coupling to the Pauli equation and read off $g=2$. *Zettili:* Sections 12.4.19 and 12.4.20 ($g=2$ from the nonrelativistic limit).
7. **Dirac hydrogen $n=2$:** compute $E_{2,1/2}$ and $E_{2,3/2}$ using the exact formula with $Z=1$ and verify the splitting $4.5\times10^{-5}$ eV and that the $2S_{1/2}$ and $2P_{1/2}$ levels coincide. *Zettili:* not in Chapter 12 (no Dirac-hydrogen section); use Sakurai's *Advanced Quantum Mechanics* or Bjorken and Drell; compare with Section 9.2.3.
8. **Klein paradox:** for a Dirac particle on a potential step with $V_0>E+mc^2$ (the Klein regime) show that $R=\left(\frac{1-\kappa}{1+\kappa}\right)^2$ with $\kappa=\frac{p_2(E+mc^2)}{p_1(E-V_0+mc^2)}<0$, so that $R>1$ and $T=1-R<0$; interpret the result through pair creation at the step, and explain why this signals the breakdown of the single-particle interpretation (verify the expressions in your book). *Zettili:* Sections 12.3.5 and 12.4.12; Problems 12.29 and 12.30; Exercises 12.42 and 12.43.
9. **Nucleon in a mean field:** for uniform nuclear matter with a scalar potential of magnitude $S$ (attractive) and a vector potential $V$ (repulsive), give $E(p)=V+\sqrt{p^2+(M-S)^2}$. With $M=939$ MeV and $S=375$ MeV show $M^*/M=0.60$; with $V=300$ MeV the central (Schrodinger-equivalent) potential $\approx V-S\approx-75$ MeV is a small difference of large numbers, while the spin-orbit potential is proportional to $V+S\approx675$ MeV and is large (verify the sign structure in Walecka). *Zettili:* not covered; Walecka (use Section 12.4.9 for the free solution).
10. **Bilinears:** list how $\bar\psi\psi,\bar\psi\gamma^5\psi,\bar\psi\gamma^\mu\psi,\bar\psi\gamma^\mu\gamma^5\psi,\bar\psi\sigma^{\mu\nu}\psi$ transform under Lorentz transformations and parity, and name them (scalar, pseudoscalar, vector, axial vector, tensor). *Zettili:* Problem 12.31 (current under parity), Problem 12.32 (chirality under parity), Section 12.4.18; discrete symmetries also Problems 12.26 and 12.27, Exercises 12.36 to 12.41.

## Optional extension

Using the chiral representation, split $\psi=(\psi_L,\psi_R)$ and show that for $m=0$ the Dirac equation decouples into two Weyl equations; discuss why the weak interaction couples to $\psi_L$ only and why QCD preserves chirality in the massless-quark limit (chiral symmetry). It is the doorway to the pion as a pseudo-Goldstone boson.

## Pitfalls

- Using different metric signatures or $\gamma$-matrix conventions between books. Fix one (Bjorken-Drell) and convert.
- Believing that $\vec S=\frac\hbar2\vec\sigma$ and $\vec L$ are separately conserved for the Dirac particle.
- Interpreting the Dirac wave function as a single-particle amplitude beyond the weak-field limit (Zitterbewegung, Klein paradox are signs of the breakdown).
- Forgetting that the bilinear $u^\dagger u$ differs from $\bar uu$.

## Gate questions

1. Why does the Dirac equation predict $g=2$ and spin-1/2 without assuming them?
2. Why must a relativistic quantum theory become a field theory with antiparticles?
3. Why do large scalar and vector potentials of opposite sign nearly cancel in the nucleon energy but add in the spin-orbit force?

## One-page cheat sheet contents

$\gamma$ matrix algebra, Dirac representation, free spinors and spin sums, bilinear classification, Dirac hydrogen formula, scalar-plus-vector potential formula.
