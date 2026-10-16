# Module 18: Why the many-body problem is hard, and the two escapes (Week 17)

**Books:** Walecka's nuclear-matter chapter, the Brueckner and independent-pair sections; Fetter and Walecka as backup.
**Time:** 1 week.

## Why this matters

The bare interaction has a hard core; $\langle V\rangle$ diverges in a Slater determinant; ordinary Hartree-Fock is undefined. Brueckner replaces $v$ with the **G-matrix**, summing ladders with Pauli blocking (Bethe-Goldstone). It works: almost.

The punchline: non-relativistic calculations with two-body forces alone land on the **Coester line**, missing the empirical saturation point. **Two escapes:** three-body forces, or relativity with $M\to M^*$. **Month 5 is the second.**

## Skip-test (40 minutes, no notes)

1. Sketch the Bethe-Goldstone equation and explain the Pauli operator $Q$.
2. Explain why $G$ is finite where $v$ is not.
3. Explain the Coester line in your own words: what varies along it, what fails, why a three-body force moves you off it.
4. Compute $k_F$, $E_F$, $v_F/c$ at $n_0$ and $5n_0$.
5. Comment on whether "relativistic" is justified by nucleon velocity.

## Prerequisites

Modules 13 and 17.

## Detailed topics (checklist)

**The hard-core problem and Brueckner theory [Must]**
- A repulsive core of radius $c\approx0.4$ fm makes $\langle v\rangle=\infty$ for any uncorrelated wavefunction; the physical wavefunction has a correlation hole (healing at $r\sim1$ fm). The reaction (G-)matrix: $G(\omega)=v+v\frac{Q}{\omega-H_0}G(\omega)$ with the Pauli operator $Q=\theta(|\mathbf k_1|-k_F)\theta(|\mathbf k_2|-k_F)$ forbidding scattering into occupied states; $G$ is finite because the ladder resummation tames the core; the self-consistent single-particle potential $U(k)=\sum_{k'<k_F}\langle kk'|G|kk'\rangle_A$.
- Hole-line expansion: the Bethe-Brueckner-Goldstone ordering; two-body correlations dominate, three-hole-line corrections are small.

**The Coester line and the two escapes [Must]**
- Different NN potentials (all fitted to NN scattering) give saturation points $(n_0,E/A)$ that fall along a band (the Coester line) with $E/A\approx-10$ to $-20$ MeV at too high a density ($k_F\approx1.4$ to $1.9$ fm$^{-1}$): none reaches the empirical $(0.16,-16)$.
- **Escape 1: three-body forces** (Fujita-Miyazawa $\Delta$ excitation, Module 09): density-dependent repulsion $\propto n^2$ that moves the saturation point to lower density. **Escape 2: relativity:** the Dirac-Brueckner-Hartree-Fock (DBHF) effective mass $M^*<M$ reduces the in-medium coupling, again a density-dependent repulsion; this is the route that QHD takes in mean-field form (Module 22).

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Walecka NM chapter: the Brueckner sections; exercises 1 to 3 |
| Session 2 | The Coester line; exercises 4 and 5 |
| Session 3 | Three-body forces and DBHF; exercises 6 to 9 |
| Session 4 | The conclusion; exercise 10 |

## Derive from scratch

1. Why $\langle v\rangle$ diverges for a hard core.
2. The Bethe-Goldstone equation as the ladder sum.
3. The role of $Q$ in the healing of the wavefunction.
4. The kinematic numbers $k_F$, $E_F$, $v_F/c$.
5. The three-body force as a density-dependent two-body force.

## Bare-minimum exercises (with expected results)

1. **Hard core:** for a core of radius $c=0.4$ fm, $\langle v\rangle=\infty$; the fraction of volume occupied by cores at $n_0$ is $\frac{4\pi}{3}c^3n_0=0.043$, so overlaps are rare but the divergence is absolute.
2. **Bethe-Goldstone:** write $G=v+vG_0Qv+\cdots$ and show that for $v\to\infty$ in $r<c$ the correlated wavefunction vanishes there and $G$ stays finite.
3. **Pauli operator:** explain why blocking intermediate states below $k_F$ makes $G$ density dependent and why this dependence is repulsive in the short-range part.
4. **Coester line:** sketch $E/A$ versus $k_F$ (or $n$) for four potentials with their saturation points on a line missing the empirical point $(k_F=1.33,E/A=-16)$; state what varies along the line (the strength of the tensor force through the D-state probability).
5. **Kinematic numbers:** at $n_0$ ($\gamma=4$): $k_F=1.333$ fm$^{-1}$, $E_F=36.8$ MeV, $v_F/c=\frac{k_F}{\sqrt{k_F^2+(M/\hbar c)^2}}=0.27$; at $5n_0$: $k_F=2.28$ fm$^{-1}$, $E_F^{\rm NR}=108$ MeV (relativistic kinetic energy $102$ MeV), $v_F/c=0.43$. **A velocity of $0.27c$ to $0.43c$ does not justify "relativistic"**: the relativity in QHD is not in the kinetic energy but in the large scalar and vector potentials (Module 21).
6. **Three-body force as density dependence:** averaging a three-body force over a third nucleon gives an effective two-body force $\propto n$; the energy per particle then gains a term $\propto n^2$, positive, pushing the minimum to lower density.
7. **Escape 2:** in DBHF the in-medium spinors have $M^*<M$ and suppress the attractive scalar coupling; show the density dependence qualitatively (it is repulsive, like the three-body force).
8. **Healing distance:** estimate $\xi\sim1/\sqrt{2M\epsilon}$ for a few-MeV excitation: $\approx1$ fm, comparable to the nucleon spacing $1.8$ fm; so correlations are local.
9. **Hole-line counting:** why the two-hole-line (Brueckner) term dominates; the expansion parameter is the "wound" integral $\kappa\approx0.1$ to $0.2$ at $n_0$.
10. **Conclusion:** write three sentences stating the problem (bare interactions miss saturation), the two escapes, and which one this guide pursues.

## Optional extension

Solve the Bethe-Goldstone equation for a hard core of radius $0.4$ fm plus an attractive tail in the $^1S_0$ channel in the pair-in-medium approximation (Pauli operator replaced by $\theta(k-k_F)$) and plot the healing of the wavefunction versus $k_F$.

## Pitfalls

- Treating $G$ as an effective interaction independent of density.
- Reading "relativistic" as "$v\sim c$".
- Assuming three-body forces and relativity are unrelated (DBHF mimics a three-body force).

## Gate questions

1. Why does $G$ stay finite for a hard core?
2. What is the Coester line, and why do all two-body potentials sit on it?
3. What are the two escapes?

## One-page cheat sheet contents

Bethe-Goldstone equation; Pauli operator; Coester line; three-body forces; DBHF; kinematic numbers.
