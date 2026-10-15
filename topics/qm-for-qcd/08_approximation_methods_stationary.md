# Module 08: Approximation methods for stationary states

**Zettili:** Chapter 9, *Approximation Methods for Stationary States* (printed pp. 537–622; PDF pp. 557–642).
**Time:** 2 weeks.

## Zettili pin (exact, from your 3rd edition)

PDF page = printed page + 20.

| Section | Printed page | Role |
| --- | --- | --- |
| 9.2.1 Nondegenerate perturbation theory | 538 to 543 | core |
| 9.2.2 Degenerate perturbation theory | 544 to 547 | core |
| 9.2.3 Fine structure and the anomalous Zeeman effect (hyperfine structure is only mentioned, with the 21 cm line, near p. 553) | 548 to 557 | core |
| 9.3 The variational method | 558 to 565 | core |
| 9.4.1 WKB: general formalism | 566 | core |
| 9.4.3 Bound states, wells with one rigid wall | 575 | core |
| 9.4.4 Bound states, wells with two rigid walls | 577 | core |
| 9.4.5 Tunneling through a potential barrier | 579 | core |
| 9.6 Solved Problems 9.1 to 9.17 | 582 to 613 | exercise pool |
| 9.7 Exercises 9.1 to 9.45 | 614 to 622 | extra pool |

**Solved problems to do:** 9.1 and 9.2 (first-order and degenerate), 9.4 (hydrogen in electric and magnetic fields), 9.6 and 9.7 (variational: oscillator, box), 9.9 (bouncing ball, variational), 9.10 (hydrogen $2p$ in a field), 9.11 and 9.12 (Zeeman-type problems), **9.15 (proton incident on a nucleus: transmission through the Coulomb barrier)**, **9.17 (two-electron atom: first-order perturbation versus variational)**.
**Unsolved exercises worth doing:** 9.1 to 9.3, 9.6, 9.12, 9.19, 9.23, 9.29, 9.36, 9.39, 9.41, 9.43, 9.44.
**Not in Zettili:** a derivation of the hyperfine splitting (Fermi contact term); use Griffiths or Sakurai.

## Why this matters for QCD

- **Perturbation theory is the main computational tool of QFT.** Rayleigh-Schrodinger series, intermediate states, energy denominators and the pattern "order-by-order sum over virtual states" are the QM ancestors of Feynman diagrams.
- **Degenerate perturbation theory** is how you understand symmetry breaking and splittings inside multiplets: the isospin-breaking mass differences, the hyperfine (color-magnetic) splitting of hadron masses.
- **The variational method** underlies trial wave functions in nuclear physics and QCD (also lattice QCD ground-state extraction).
- **WKB and tunneling** give the Gamow factor of nuclear reactions and the semiclassical picture of instantons.

## Skip-test (40 minutes, no notes)

1. Derive the first- and second-order energy corrections $E_n^{(1)}=\langle n|V|n\rangle$, $E_n^{(2)}=\sum_{m\ne n}\frac{|V_{mn}|^2}{E_n-E_m}$ and the first-order state correction.
2. For $H=\frac{p^2}{2m}+\frac12m\omega^2x^2+\lambda x^4$ find $E_n^{(1)}=\lambda\left(\frac{\hbar}{2m\omega}\right)^2(6n^2+6n+3)$.
3. Prove that the variational energy $E[\psi]=\langle\psi|H|\psi\rangle/\langle\psi|\psi\rangle$ is an upper bound on the ground-state energy.
4. Use a trial wave function $e^{-Z_{\rm eff}r/a_0}$ for each electron in helium and show $Z_{\rm eff}=\frac{27}{16}$, $E=-77.5$ eV.
5. State the WKB quantization condition $\oint p\,dx=(n+\frac12)2\pi\hbar$ and the tunneling factor $e^{-\frac2\hbar\int\!|p|dx}$.

## Prerequisites

Modules 03, 05, 06, 07.

## Detailed topics (checklist)

**Non-degenerate perturbation theory**
- Rayleigh-Schrodinger expansion, first and second-order energy, first-order state, the normalization convention, the condition of validity ($|V_{mn}|\ll|E_n-E_m|$), the pattern of the series, level repulsion (the second-order shift pushes levels apart), applications: the anharmonic oscillator, the polarizability of the oscillator and hydrogen, the quadratic Stark effect.

**Degenerate perturbation theory**
- Diagonalizing $V$ inside the degenerate subspace; "good" states, how a symmetry chooses them; the linear Stark effect of hydrogen $n=2$ ($\Delta E=\pm3eEa_0$); the Zeeman effect (weak field with the Lande factor $\Delta E=g_J\mu_Bm_jB$, strong field Paschen-Back).

**Fine and hyperfine structure of hydrogen**
- Relativistic kinetic energy correction, spin-orbit coupling, the Darwin term, and their sum
$$E_{nj}^{(\rm FS)}=-\frac{13.6\ {\rm eV}}{n^2}\,\frac{\alpha^2}{n^2}\left(\frac{n}{j+\frac12}-\frac34\right),$$
the $2P_{3/2}-2P_{1/2}$ splitting ($4.5\times10^{-5}$ eV, $10.9$ GHz), degeneracy in $j$ (broken by the Lamb shift, a QED effect).
- Hyperfine splitting from the spin-spin (Fermi contact) interaction, $F=0,1$, the 21 cm line ($5.9\times10^{-6}$ eV, $1420$ MHz).

**Variational method**
- The Rayleigh-Ritz principle, trial functions with parameters, excited states by orthogonality to the lower states, the virial theorem as a consistency check, applications: the oscillator (a Gaussian trial gives the exact answer), hydrogen with a Gaussian trial ($-\frac{4}{3\pi}$ Hartree $=-11.5$ eV versus $-13.6$), helium (screening, $-77.5$ eV versus the experimental $-79.0$ eV).

**WKB approximation**
- The semiclassical wave function, validity ($|d\lambda/dx|\ll1$), turning points and the connection formulas, the Bohr-Sommerfeld quantization $\oint p\,dx=(n+\frac12)2\pi\hbar$, applications to the oscillator (exact), the linear potential, tunneling through a barrier and the Gamow factor for Coulomb barriers $e^{-2\pi\eta}$ with $\eta=\frac{Z_1Z_2e^2}{\hbar v}$.

## Reading plan (exact)

| Block | Reading |
| --- | --- |
| Lunch 1 | Section 9.2.1 (pp. 538 to 544) |
| Lunch 2 | Section 9.2.2 (pp. 544 to 548) |
| Lunch 3 | Section 9.2.3 (pp. 548 to 558) |
| Lunch 4 | Section 9.3 (pp. 558 to 566) |
| Week 2 lunches | Section 9.4 (pp. 566 to 582) |
| Evenings | Derivations; then Problems 9.1 to 9.17; exercises |

## Derive from scratch (derivation nights)

1. The first and second-order Rayleigh-Schrodinger formulas including the normalization of the state.
2. Degenerate perturbation theory for a two-fold degenerate level, and the Stark effect for the $n=2$ states.
3. The fine-structure sum for hydrogen (the three terms) and the combined formula.
4. The helium variational calculation with a Coulomb integral: $\langle\frac{e^2}{r_{12}}\rangle=\frac58Z_{\rm eff}\frac{e^2}{a_0}$.
5. The WKB connection at a linear turning point, giving the $(n+\frac12)$ phase.

## Bare-minimum exercises (solved-problem keywords: perturbation, anharmonic, Stark, Zeeman, fine structure, hyperfine, variational, WKB)

1. **Anharmonic oscillator:** compute the first-order shift for $V'=\lambda x^4$ and the second-order shift for $V'=\lambda x^3$ ($E_n^{(2)}=-\frac{\lambda^2\hbar^2}{m^3\omega^4}\left(\frac{30n^2+30n+11}{8}\right)$; verify). *Zettili:* Problems 9.1 and 9.2; Exercises 9.1 to 9.3 and 9.8.
2. **Oscillator in a field:** $V'=-eEx$ gives exactly $E_n^{(2)}=-\frac{e^2E^2}{2m\omega^2}$, equal to the exact shift of the completed square (use as a check). *Zettili:* Exercises 9.30 to 9.32 (check the statements); Problem 4.17 for the exact answer.
3. **Linear Stark effect:** diagonalize $eE z$ in the $n=2$ hydrogen subspace (states $|200\rangle,|210\rangle$ mix, $|21\pm1\rangle$ unshifted) and get $\Delta E=\pm3eEa_0$. *Zettili:* Problems 9.4 and 9.10.
4. **Fine structure:** evaluate $E_{nj}^{\rm FS}$ for $n=2,j=\frac12,\frac32$ and verify the splitting $4.5\times10^{-5}$ eV. *Zettili:* Section 9.2.3; Exercises 9.39, 9.41, 9.44.
5. **Hyperfine 21 cm:** from the Fermi contact interaction obtain the ground-state splitting $\Delta E_{\rm hf}=\frac43g_p\frac{m_e}{m_p}\alpha^4m_ec^2$ and evaluate it ($g_p=5.586$): $5.9\times10^{-6}$ eV, i.e. $1420$ MHz and a wavelength of $21$ cm. Explain which factor makes it $\sim10^{3}$ times smaller than the fine structure. *Zettili:* only qualitative (p. 553); derive with Griffiths or Sakurai.
6. **Zeeman effect:** for the $2P_{3/2}$ level in a weak field list the $g_J=\frac43$ sublevels $m_j=\pm\frac32,\pm\frac12$ and their energies. *Zettili:* Section 9.2.3; Problems 9.11 and 9.12; Exercises 9.36 and 9.43 (positronium).
7. **Variational oscillator and hydrogen:** with a Gaussian trial $e^{-\beta x^2}$ minimize and recover $\frac12\hbar\omega$ exactly; with $e^{-\beta r^2}$ for hydrogen obtain $-\frac{4}{3\pi}$ Hartree ($-11.5$ eV). *Zettili:* Problems 9.6, 9.7, 9.9; Exercises 9.12 and 9.23.
8. **Helium:** compute the variational energy as a function of $Z_{\rm eff}$: $E=\left(Z_{\rm eff}^2-2ZZ_{\rm eff}+\frac58Z_{\rm eff}\right)\times27.2$ eV, minimize and obtain $Z_{\rm eff}=\frac{27}{16}$, $E=-77.5$ eV. *Zettili:* **Problem 9.17**; Exercises 9.18 and 9.19.
9. **WKB for a linear potential:** for $V=\sigma r$ ($\ell=0$, $u(0)=0$) obtain $E_n=\left[\frac{3\pi}{2}\left(n+\frac34\right)\right]^{2/3}\left(\frac{\hbar^2\sigma^2}{2m}\right)^{1/3}$ and check the lowest level: WKB gives $2.32$ versus the exact Airy-zero value $2.338$. *Zettili:* Section 9.4.3; Exercises 9.6 and 9.29; compare Problem 9.9 and Exercise 9.13.
10. **Gamow factor:** estimate the tunneling probability for $p+p$ at $E=1$ keV through the Coulomb barrier using $e^{-2\pi\eta}$ with $\eta=\frac{e^2}{\hbar v}=\alpha\frac{c}{v}$ and reduced mass $\mu=m_p/2$; compare with the thermal energy at the solar centre ($\sim1.3$ keV; see Volume 1, Module 07). *Zettili:* **Problem 9.15**; Exercises 9.26 and 9.28.

## Optional extension

Compute the second-order energy of the ground state of a two-level system (exact answer $\frac{E_1+E_2}{2}-\ldots$) and expand to confirm the perturbative series converges for $|V|<\frac{|E_1-E_2|}{2}$. Then discuss the *asymptotic* nature of the anharmonic oscillator series (the series in $\lambda$ has zero radius of convergence), an early encounter with the divergence of perturbation series in QFT.

## Pitfalls

- Using non-degenerate formulas in a degenerate space.
- Taking the first-order wave-function correction as a normalized state.
- Applying the variational method to excited states without orthogonality constraints.
- Using the WKB quantization with $n$ instead of $n+\frac12$ (and with $n+\frac34$ for a hard wall plus soft turning point).

## Gate questions

1. Why do perturbative corrections push neighbouring energy levels apart?
2. Why does degenerate perturbation theory need the "good" basis, and how does a symmetry choose it?
3. Why is the variational energy always an upper bound?

## One-page cheat sheet contents

RS formulas, degenerate procedure, fine-structure and hyperfine numbers, variational recipe, WKB conditions and the Gamow factor.
