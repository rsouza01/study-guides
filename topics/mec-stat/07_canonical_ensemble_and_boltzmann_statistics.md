# Module 07: The canonical ensemble and Boltzmann statistics

**Books:** Schroeder (chapter 6), Pathria (chapters 3 and 6: canonical ensemble; simple gases including internal degrees of freedom), Mandl (the Boltzmann distribution, ideal gas, internal motion), Blundell and Blundell (Boltzmann factor, partition function), Swendsen (canonical ensemble).
**Time:** 2 weeks.

## Why this matters for stars and EOS

- Level populations of atoms and ions follow the Boltzmann factor: line strengths in spectra, the excitation correction to the EOS, and the form of the **atomic partition function** (including its famous divergence for hydrogen).
- The **Maxwell-Boltzmann distribution** is the starting point of kinetic theory and, combined with quantum tunneling, of the **Gamow peak** that sets thermonuclear reaction rates.
- Internal degrees of freedom (rotation, vibration, dissociation) give the heat capacity of molecular hydrogen in cool envelopes and in protostellar collapse.
- Equipartition, energy fluctuations and the relation $C_V=\frac{\langle\Delta E^2\rangle}{kT^2}$ are used throughout.

## Skip-test (40 minutes, no notes)

1. Derive the canonical probability $p_i=e^{-\beta E_i}/Z$ from the microcanonical ensemble of system plus reservoir, and show $F=-kT\ln Z$, $U=-\partial\ln Z/\partial\beta$, $S=-\partial F/\partial T$.
2. Show $\langle\Delta E^2\rangle=kT^2C_V$.
3. For $N$ identical non-interacting particles $Z=Z_1^N/N!$; compute $Z_1=V/\lambda^3$ for a monatomic gas and recover $PV=NkT$, $U=\frac32NkT$, and the Sackur-Tetrode entropy.
4. Derive the Maxwell speed distribution and give $v_{\rm mp}=\sqrt{2kT/m}$, $\bar v=\sqrt{8kT/\pi m}$, $v_{\rm rms}=\sqrt{3kT/m}$.
5. For a two-level system with splitting $\epsilon$ find $C_V(T)$ and the position of its maximum.

## Prerequisites

Modules 01 to 03 and 06.

## Detailed topics (checklist)

**The ensemble**
- The canonical (Gibbs/Boltzmann) distribution for a system in contact with a heat bath; the partition function $Z=\sum e^{-\beta E_i}$; the connection $F=-kT\ln Z$; energy, entropy, heat capacity from $Z$; energy fluctuations and the sharpness of $E$ for large $N$.
- Factorization of $Z$ for independent subsystems; the correct treatment of identical particles at low density $Z=Z_1^N/N!$.
- Equipartition theorem and its limits (quantum freeze-out).

**Ideal gases**
- Single-particle partition function $Z_1=\frac{V}{\lambda^3}Z_{\rm int}$ with the thermal wavelength $\lambda=h/\sqrt{2\pi mkT}$; Sackur-Tetrode entropy and $\mu=kT\ln\frac{n\lambda^3}{Z_{\rm int}}$.
- The Maxwell-Boltzmann velocity and speed distributions; effusion; the tail of the distribution.

**Internal degrees of freedom**
- Two-level and Schottky heat capacity ($C_{\max}\approx0.44k$ near $kT\approx0.42\epsilon$).
- Harmonic oscillator: $Z=\frac{1}{2\sinh(\beta\hbar\omega/2)}$, mean energy $\hbar\omega\left(\frac12+\frac{1}{e^{\beta\hbar\omega}-1}\right)$; $C=k\frac{(\beta\hbar\omega/2)^2}{\sinh^2(\beta\hbar\omega/2)}$.
- Rotors: rotational temperature $\Theta_{\rm rot}$, high-temperature limit $C=k$; **ortho/para** hydrogen and the effect of nuclear-spin statistics at low $T$.
- Diatomic gas heat capacity: $\frac32k$ (translation) plus $k$ (rotation, $T\gg\Theta_{\rm rot}\approx85$ K for H$_2$) plus $k$ (vibration, $T\gtrsim\Theta_{\rm vib}\approx6000$ K).

**Atoms and ions**
- Boltzmann level populations $\frac{n_j}{n_i}=\frac{g_j}{g_i}e^{-(E_j-E_i)/kT}$; the atomic partition function $Z_{\rm int}=\sum_ig_ie^{-E_i/kT}$.
- The hydrogen partition function diverges because the levels $E_n$ converge to the ionization limit while $g_n=2n^2$; the sum must be truncated (by the finite size of the atom, plasma microfields, pressure ionization); the physical consequence is that the *occupation probability* of high levels is small.

**Stellar reaction rates (first look)**
- The Maxwell-Boltzmann factor $e^{-E/kT}$ times the Coulomb-barrier tunneling factor $e^{-b/\sqrt E}$ produces a narrow **Gamow peak** at $E_0=(bkT/2)^{2/3}$; for $p+p$ at $1.5\times10^7$ K, $E_0\approx5.9$ keV $\gg kT\approx1.3$ keV.

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Schroeder chapter 6: Boltzmann factor, partition function |
| Lunch 2 | Schroeder chapter 6: ideal gas, Maxwell distribution, equipartition |
| Lunch 3 | Pathria chapter 3 (canonical ensemble); Mandl on the Boltzmann distribution |
| Lunch 4 | Pathria chapter 6 and Mandl: ideal gases with internal motion, diatomic gases, ortho/para hydrogen |
| Week 2 lunches | Blundell and Blundell on the partition function and applications; review |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. The Boltzmann distribution via the system plus reservoir argument.
2. $F=-kT\ln Z$, $U$, $S$, $C_V$ from $Z$, and $\langle\Delta E^2\rangle=kT^2C_V$.
3. The ideal-gas partition function including $1/N!$ and the Sackur-Tetrode entropy.
4. The Maxwell speed distribution and its moments.
5. The harmonic oscillator and two-level heat capacities.

## Bare-minimum exercises (find matching problems with keywords: partition function, Maxwell distribution, equipartition, rotational and vibrational heat capacity, Boltzmann factor)

1. **Excited-state fraction in hydrogen:** the fraction of H atoms in $n=2$ relative to $n=1$ at $T=10^4$ K is $\frac{g_2}{g_1}e^{-10.2\,{\rm eV}/kT}=4\times e^{-11.84}\approx2.9\times10^{-5}$; repeat at $T=6000$ K and $15000$ K.
2. **Divergence of $Z_H$:** show $\sum_n2n^2e^{-\chi(1-1/n^2)/kT}$ diverges and estimate the effect of truncating at $n_{\max}=100$ versus $n_{\max}=30$ at $T=10^4$ K.
3. **Maxwell-Boltzmann numbers:** for protons at the solar centre ($1.57\times10^7$ K) compute $v_{\rm rms}=\sqrt{3kT/m}\approx620$ km/s, and the fraction of protons with kinetic energy above $10\,kT$, using the energy distribution $f(x)=\frac{2}{\sqrt\pi}\sqrt x\,e^{-x}$ ($x=E/kT$): $\mathrm{erfc}(\sqrt{10})+\frac{2}{\sqrt\pi}\sqrt{10}\,e^{-10}\approx1.7\times10^{-4}$.
4. **Gamow peak:** maximize $e^{-E/kT-b/\sqrt E}$ and show $E_0=(bkT/2)^{2/3}$; expanding the exponent about $E_0$ to second order gives a Gaussian of full $1/e$ width $\Delta=\frac{4}{\sqrt3}\sqrt{E_0kT}$. Evaluate for $p+p$ at $1.5\times10^7$ K with $b=\pi\alpha Z_1Z_2\sqrt{2m_rc^2}$: $E_0\approx5.9$ keV and $\Delta\approx6.4$ keV, with $kT\approx1.3$ keV.
5. **Two-level system:** $C_V(T)$ and the Schottky peak: verify $C_{\max}=0.44k$ at $kT\approx0.42\epsilon$; sketch.
6. **Oscillator:** verify $C\to k$ for $kT\gg\hbar\omega$ and the exponential freezing for $kT\ll\hbar\omega$; apply to the vibrational mode of H$_2$.
7. **Diatomic heat capacity:** for H$_2$ sketch $C_V/Nk$ from $T=10$ K to $10^4$ K: $3/2$, then $5/2$ after rotation turns on near $\Theta_{\rm rot}=85$ K, then $7/2$ above $\Theta_{\rm vib}\approx6000$ K (before dissociation).
8. **Fluctuations:** for an ideal monatomic gas show $\frac{\Delta E}{E}=\sqrt{2/3N}$.
9. **Equipartition with a quadratic term:** derive $\langle E\rangle=\frac12kT$ per quadratic degree of freedom; check it for the oscillator and for the relativistic particle $E=pc$ (it gives $kT$ per degree of freedom, not $\frac12kT$).
10. **Ortho/para:** with nuclear-spin statistics the ortho states have odd $J$ and weight 3, para even $J$ with weight 1: show the equilibrium ortho/para ratio tends to 3:1 at high $T$ and 0 at $T\to0$.

## Optional extension

Compute the equilibrium heat capacity of hydrogen gas across the molecular dissociation transition at fixed pressure using the Saha-type law of mass action (Module 05) plus the diatomic partition function; show that $C_P$ has a large peak near the dissociation temperature.

## Pitfalls

- Treating the Maxwell distribution as valid for degenerate gases (Module 10).
- Applying classical equipartition at low temperature without checking quantum freeze-out.
- Forgetting the $1/N!$ in $Z$ for identical gas molecules.
- Ignoring that the hydrogen partition function needs a physical cutoff.

## Gate questions

1. Why does the canonical energy distribution become sharply peaked for large $N$?
2. Why do rotational and vibrational modes not contribute to $C_V$ at low $T$?
3. Why does the Gamow peak lie far above $kT$?

## One-page cheat sheet contents

$Z$ and its derivatives; ideal-gas $Z_1$ and $\lambda$; Maxwell distribution moments; two-level and oscillator heat capacities; diatomic temperatures; Boltzmann population ratio; Gamow-peak formula.
