# Module 09: Quantum statistics and density of states

**Books:** Pathria (chapters 5 and 6: formulation of quantum statistics, ideal gases; chapter 8 opening), Schroeder (chapter 7), Mandl (quantum statistics), Blundell and Blundell (identical particles, Fermi and Bose gases), Swendsen (quantum ideal gases).
**Time:** 2 weeks.

## Why this matters for stars and EOS

Every gas in a star is a quantum gas; whether the classical Maxwell-Boltzmann description is adequate is decided by one number, the **degeneracy parameter** $n\lambda^3/g$. This module gives the general machinery: occupation numbers, the density of states for non-relativistic and relativistic particles, the integral forms of $N$, $P$ and $U$, and the first quantum corrections to the classical gas. Modules 10 and 11 apply it to fermions and bosons.

## Skip-test (40 minutes, no notes)

1. Write the Fermi-Dirac and Bose-Einstein occupation numbers $f(\epsilon)=\frac{1}{e^{(\epsilon-\mu)/kT}\pm1}$ and the classical limit.
2. Derive the density of states per unit energy for a non-relativistic particle in a 3D box, $g(\epsilon)=\frac{g_sV}{4\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\epsilon^{1/2}$, and for a massless particle $g(\epsilon)=\frac{g_sV\epsilon^2}{2\pi^2\hbar^3c^3}$.
3. Write $N=\int g(\epsilon)f(\epsilon)d\epsilon$ and $P=\frac13\int n(p)vp\,d^3p$; show $P=\frac23\frac UV$ (non-relativistic) and $P=\frac13\frac UV$ (ultra-relativistic).
4. Define the thermal wavelength and the degeneracy criterion $n\lambda^3/g\ll1$.
5. Give the first quantum correction to the ideal gas equation of state: $P=nkT\left[1\pm\frac{n\lambda^3}{2^{5/2}g}\right]$ (upper sign fermions).

## Prerequisites

Modules 06 to 08.

## Detailed topics (checklist)

**Indistinguishability and statistics**
- Symmetric and antisymmetric many-particle states; the occupation-number description; the grand partition function factorizes over single-particle orbitals; derivation of the FD and BE distributions (Module 08) and of the $\bar n$ formulas; the spin-statistics connection (stated).
- The classical limit: $\bar n\ll1$ everywhere, i.e. $z\ll1$; the Maxwell-Boltzmann distribution; counting with the corrected Boltzmann factor.

**Density of states**
- States in a box; the continuum limit $\sum_k\to\frac{V}{(2\pi)^3}\int d^3k$; spin degeneracy $g_s$ ($2$ for electrons, neutrons, protons; $2$ for photons; $1$ for each massless neutrino or antineutrino).
- Non-relativistic ($\epsilon=p^2/2m$): $g(\epsilon)\propto\epsilon^{1/2}$; ultra-relativistic ($\epsilon=pc$): $g(\epsilon)\propto\epsilon^2$; general relativistic $\epsilon=\sqrt{p^2c^2+m^2c^4}$ and the **relativity parameter** $x=p/mc$.
- General integrals: $N=\frac{g_sV}{h^3}\int_0^\infty4\pi p^2f\,dp$, $U=\frac{g_sV}{h^3}\int4\pi p^2\epsilon(p)f\,dp$, $P=\frac{g_s}{3h^3}\int4\pi p^2\,pv\,f\,dp$ with $v=pc^2/\epsilon$.

**Fermi-Dirac and Bose-Einstein integrals**
- Definitions $F_j(\eta)=\int_0^\infty\frac{x^j}{e^{x-\eta}+1}dx$, $G_j(\eta)=\int_0^\infty\frac{x^j}{e^{x-\eta}-1}dx$ with $\eta=\mu/kT$; limits $\eta\to-\infty$ (classical, $F_j\to\Gamma(j+1)e^\eta$) and $\eta\to+\infty$ (degenerate, $F_j\to\frac{\eta^{j+1}}{j+1}$); polylogarithm form $F_j(\eta)=-\Gamma(j+1){\rm Li}_{j+1}(-e^\eta)$.

**The classical limit and its first corrections**
- Degeneracy parameter $n\lambda^3/g_s$; the first quantum correction $\frac{P}{nkT}=1\pm\frac{n\lambda^3}{2^{5/2}g_s}$ ($+$ for fermions: Pauli repulsion; $-$ for bosons); exchange-effect interpretation.
- **Where stellar gases lie:** electrons at the solar centre have $n\lambda^3/g\approx0.2$ (mildly degenerate: percent-level correction); electrons in white dwarfs have $n\lambda^3\gg1$ (strongly degenerate); ions are always classical in stars; neutrons in neutron stars are degenerate.

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Pathria chapter 5: quantum statistics, occupation numbers |
| Lunch 2 | Schroeder chapter 7: identical particles, Fermi-Dirac and Bose-Einstein distributions |
| Lunch 3 | Mandl and Blundell and Blundell: density of states, the classical limit |
| Lunch 4 | Pathria chapter 8 opening: thermodynamic quantities of the ideal Fermi gas; Swendsen on quantum ideal gases |
| Week 2 lunches | Review; compute $n\lambda^3$ for stellar situations |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. The density of states in 1, 2, 3 dimensions for the non-relativistic and massless dispersion relations.
2. The FD and BE distributions and the classical limit.
3. $P=\frac23\frac UV$ and $P=\frac13\frac UV$ from the general integral for $P$.
4. The first quantum correction to the ideal gas: expand $N$ and $P$ to second order in $z$.
5. The degeneracy parameter and the temperature $T_F=E_F/k$ above which the Fermi gas is classical.

## Bare-minimum exercises (find matching problems with keywords: density of states, Fermi-Dirac distribution, quantum concentration, degeneracy)

1. **Density of states:** show that the number of states with momentum below $p$ is $\frac{g_sV}{6\pi^2\hbar^3}p^3$ and derive both $g(\epsilon)$ formulas.
2. **Thermal wavelength numbers:** for electrons at $T=10^7$ K, $\lambda=h/\sqrt{2\pi m_ekT}\approx2.4\times10^{-9}$ cm; for protons at the same $T$, $\lambda\approx5.5\times10^{-11}$ cm.
3. **Degeneracy at the solar centre:** with $n_e\approx6\times10^{25}$ cm$^{-3}$, $T=1.57\times10^7$ K get $n_e\lambda^3/2\approx0.2$; estimate the first quantum correction to the electron pressure ($\approx\frac{n\lambda^3}{2^{5/2}g}\approx0.04$, a few percent).
4. **Degeneracy in a white dwarf:** with $\rho=10^6$ g/cm$^3$, $\mu_e=2$ ($n_e=3\times10^{29}$ cm$^{-3}$), $T=10^7$ K find $n_e\lambda^3\approx4\times10^3\gg1$ so the electrons are strongly degenerate; the ions ($n_i\lambda_i^3$ tiny) are classical.
5. **Quantum correction sign:** derive that fermions have larger and bosons smaller pressure than classical ones at the same $n,T$, by the second-order expansion of $N$ and $P$ in the fugacity.
6. **Equation of state relation:** prove $PV=\frac23U$ for any non-relativistic ideal quantum gas and $PV=\frac13U$ for any ultra-relativistic one, with the general formula for arbitrary dispersion.
7. **Degeneracy temperature:** compute $T_F$ for electrons in a metal ($n=10^{23}$ cm$^{-3}$; $E_F\approx8$ eV, $T_F\approx9\times10^4$ K) and for the solar centre ($T_F\approx6\times10^6$ K, comparable to $T$).
8. **Photons are bosons with $\mu=0$:** from $g(\epsilon)\propto\epsilon^2$ and $f=1/(e^{\epsilon/kT}-1)$ obtain $U=aVT^4$ with $a=\pi^2k^4/15\hbar^3c^3$ (done fully in Module 11).
9. **Fermi-Dirac integral limits:** show the classical and degenerate limits of $F_{1/2}(\eta)$ and and compute $F_{1/2}(0)=(1-2^{-1/2})\Gamma(3/2)\zeta(3/2)=0.678$.
10. **Occupation fluctuations:** from $\langle\Delta n^2\rangle=\bar n(1\mp\bar n)$ show that degenerate fermions have a frozen Fermi sea: states deep inside the Fermi sea have no fluctuations.

## Optional extension

Derive the exact expression for the density of states of a relativistic particle in terms of $x=p/mc$ and the integrals for $n,P,u$ as functions of $(\mu,T,x)$, and check the two limits $x\ll1$ and $x\gg1$ (needed in Module 10).

## Pitfalls

- Forgetting the spin degeneracy $g_s$ in $g(\epsilon)$ or $n\lambda^3$.
- Mixing up the chemical potential with and without the rest-mass energy.
- Applying the classical formula to electrons at white dwarf densities.
- Forgetting that $\lambda$ depends on the *particle* mass: ions are always classical, electrons often are not.

## Gate questions

1. Why is the classical limit equivalent to $z\ll1$?
2. Why do fermions exert an extra "exchange pressure" even without interactions?
3. Which of electrons, ions and neutrons is degenerate in the Sun, a white dwarf and a neutron star?

## One-page cheat sheet contents

FD and BE distributions; $g(\epsilon)$ formulas; $N,U,P$ integrals; thermal wavelength and degeneracy criterion; $PV=\frac23U$ and $\frac13U$; first quantum correction.
