# Module 10: Scattering theory

**Zettili:** Chapter 11, *Scattering Theory* (printed pp. 671–706; PDF pp. 691–726).
**Time:** 3 weeks. This is the most important module for hadron physics and QFT, so it gets the extra week.

## Zettili pin (exact, from your 3rd edition)

PDF page = printed page + 20.

| Section | Printed page | Role |
| --- | --- | --- |
| 11.1 Scattering and cross section (11.1.1 and 11.1.2: lab and CM frames) | 671 to 674 | core |
| 11.2 Scattering amplitude of spinless particles (including the integral equation with Green's function) | 675 to 681 | core |
| 11.3 The Born approximation (11.3.1 first Born; 11.3.2 validity; the Born series) | 682 to 684 | core |
| 11.4.1 Partial-wave analysis for elastic scattering (including Rutherford and the optical theorem) | 685 | core |
| 11.4.2 Partial-wave analysis for inelastic scattering (optical theorem for inelastic scattering) | 689 | core |
| 11.5 Scattering of identical particles | 691 | core |
| 11.6 Solved Problems 11.1 to 11.8 | 693 to 703 | exercise pool |
| 11.7 Exercises 11.1 to 11.14 | 704 to 706 | extra pool |

**Solved problems to do:** **11.1 (Yukawa potential in the Born approximation)**, 11.2 (slow particles on a delta shell), 11.3 (hard sphere), 11.4 (low-energy scattering from a square well), 11.5 (Born approximation for another potential), **11.6 (phase shifts of 50 MeV neutrons: total cross section and nuclear radius)**, 11.7 (electron-hydrogen scattering), **11.8 (absorbing nucleus: elastic and inelastic cross sections, optical theorem check)**.
**Unsolved exercises worth doing:** 11.3, 11.5 to 11.9, 11.11 to 11.14 (11.12 is neutron-neutron $S$-wave scattering with a spin-dependent interaction).
**Not in Zettili:** the operator Lippmann-Schwinger/T-matrix formalism, the scattering length and effective range, resonances and the Breit-Wigner formula, S-matrix poles. Use Sakurai (scattering chapters), Griffiths (scattering chapter), and Halzen and Martin for the particle-physics language.

## Why this matters for QCD

- **Everything we know about hadrons comes from scattering.** Cross sections, phase shifts, scattering lengths and resonance parameters are the observables; QCD calculations (including lattice QCD) are compared with them.
- **The S-matrix and unitarity** are the organizing concepts of QFT. Partial-wave unitarity, the optical theorem and analyticity are first learned here.
- **Resonances** (the $\Delta(1232)$, $\rho$, $\psi$ states) are *particles* in the sense of poles of the S-matrix; the Breit-Wigner form is the scattering version of the decay width of Module 09.
- **Yukawa scattering and the Born approximation** are the QM version of tree-level meson exchange; the Born series is a sum of ladder diagrams.
- **Low-energy parameters** (scattering lengths, effective ranges) are the inputs of nuclear effective field theory and lattice QCD benchmarks.

## Skip-test (40 minutes, no notes)

1. Define the differential cross section $\frac{d\sigma}{d\Omega}=|f(\theta,\phi)|^2$ and the asymptotic form $\psi\to e^{ikz}+f(\theta)\frac{e^{ikr}}{r}$.
2. State the first Born approximation $f(\theta)=-\frac{m}{2\pi\hbar^2}\int e^{-i\vec q\cdot\vec r}V(\vec r)\,d^3r$ with $\vec q=\vec k'-\vec k$, $q=2k\sin\frac\theta2$.
3. Write the partial-wave expansion $f(\theta)=\frac1k\sum_\ell(2\ell+1)e^{i\delta_\ell}\sin\delta_\ell P_\ell(\cos\theta)$ and $\sigma=\frac{4\pi}{k^2}\sum(2\ell+1)\sin^2\delta_\ell$.
4. State the optical theorem $\sigma_{\rm tot}=\frac{4\pi}{k}\,\mathrm{Im}f(0)$.
5. Give the Breit-Wigner form of $\sigma_\ell$ near a resonance and its maximum $\frac{4\pi(2\ell+1)}{k^2}$.

## Prerequisites

Modules 05 (radial equation, spherical Bessel functions), 08, 09 (golden rule). For the pole analysis: basic complex analysis (your complex analysis track).

## Detailed topics (checklist)

**Kinematics and cross sections**
- Flux, cross section, differential cross section; laboratory versus centre-of-mass frames; the scattering amplitude $f(\theta,\phi)$; asymptotic boundary conditions, the scattering state $\psi_{\vec k}^{(+)}$.

**Integral formulation**
- The Lippmann-Schwinger equation $|\psi^{(+)}\rangle=|\phi\rangle+\frac{1}{E-H_0+i\epsilon}V|\psi^{(+)}\rangle$, the free Green's function $G_0^{(+)}(\vec r,\vec r')=-\frac{m}{2\pi\hbar^2}\frac{e^{ik|\vec r-\vec r'|}}{|\vec r-\vec r'|}$, the T-matrix, $f=-\frac{m}{2\pi\hbar^2}\langle\vec k'|T|\vec k\rangle(2\pi)^3$, the **Born series** $T=V+VG_0V+VG_0VG_0V+\dots$ (the ladder diagrams); validity of the Born approximation (high energy or weak potential); the Born amplitude for the Yukawa potential and its Coulomb limit giving Rutherford scattering.

**Partial waves**
- Expansion of a plane wave, radial solutions outside the range of the potential $R_\ell\propto\cos\delta_\ell\,j_\ell(kr)-\sin\delta_\ell\,n_\ell(kr)$, definition of the phase shift via the log derivative at the boundary, the S-matrix elements $S_\ell=e^{2i\delta_\ell}$, unitarity ($|S_\ell|=1$ for elastic scattering) and the bound $\sigma_\ell\le\frac{4\pi(2\ell+1)}{k^2}$, the partial-wave amplitude $f_\ell=\frac{e^{2i\delta_\ell}-1}{2ik}$.
- Hard sphere scattering and the low-energy limit $\sigma\to4\pi a^2$; the square well and its resonances; the relation between the sign of $\delta_\ell$ and attraction/repulsion; Levinson's theorem (awareness).

**Low-energy scattering**
- Scattering length $a$ defined by $k\cot\delta_0\to-\frac1a$; effective-range expansion $k\cot\delta_0=-\frac1a+\frac12r_0k^2+\dots$; the relation of a large positive scattering length to a shallow bound state with $E_B=\frac{\hbar^2}{2\mu a^2}$ (zero-range limit); the sign convention of $a$ (attractive and no bound state: negative; bound state: positive).
- Nucleon-nucleon: $a_t=5.4$ fm (triplet, deuteron), $a_s=-23.7$ fm (singlet, virtual state), $r_t\approx1.75$ fm, $r_s\approx2.7$ fm (verify).

**Resonances**
- The Breit-Wigner formula $\delta_\ell$ passing through $\pi/2$ with $\sigma_\ell=\frac{4\pi(2\ell+1)}{k^2}\frac{(\Gamma/2)^2}{(E-E_R)^2+(\Gamma/2)^2}$; the S-matrix pole at $E=E_R-i\Gamma/2$; time delay and the lifetime $\tau=\hbar/\Gamma$; bound states as poles on the positive imaginary $k$ axis, resonances on the lower half of the complex energy plane.

**Other topics**
- Identical particles in scattering (Mott formula, symmetrization of $f(\theta)$), spin-dependent scattering (singlet and triplet channels), Coulomb scattering and the Rutherford formula with the screened-potential limit, scattering from a delta shell or a delta-function potential (exactly solvable), the eikonal approximation (awareness).

## Reading plan (exact)

| Block | Reading |
| --- | --- |
| Lunch 1 | Section 11.1 (pp. 671 to 675) |
| Lunch 2 | Section 11.2 (pp. 675 to 682) |
| Lunch 3 | Section 11.3 Born approximation (pp. 682 to 685) |
| Lunch 4 | Section 11.4.1 partial waves (pp. 685 to 689) |
| Week 2 lunches | Sections 11.4.2 and 11.5 (pp. 689 to 693) |
| Week 3 lunches | Sakurai or Griffiths: resonances, Breit-Wigner, scattering length (not in Zettili) |
| Evenings | Derivations; then Problems 11.1 to 11.8; exercises |

## Derive from scratch (derivation nights)

1. The scattering cross section from the asymptotic wave function and the probability current.
2. The Born amplitude for a Yukawa potential $V=g\frac{e^{-\mu r}}{r}$: $f_B=-\frac{2mg}{\hbar^2}\frac{1}{q^2+\mu^2}$, and its Coulomb limit giving Rutherford $\frac{d\sigma}{d\Omega}=\left(\frac{g\,m}{2\hbar^2k^2\sin^2(\theta/2)}\right)^2$.
3. The partial-wave expansion and $\sigma=\frac{4\pi}{k^2}\sum_\ell(2\ell+1)\sin^2\delta_\ell$.
4. The optical theorem from the partial-wave form and unitarity.
5. Low-energy hard-sphere scattering: $\delta_0=-ka$, $\sigma=4\pi a^2$; the square-well scattering length $a=R\left[1-\frac{\tan(KR)}{KR}\right]$.

## Bare-minimum exercises (solved-problem keywords: Born approximation, partial waves, phase shift, scattering length, resonance, optical theorem, Rutherford)

1. **Born approximation for a Gaussian and a Yukawa potential:** compute $f(\theta)$ and the total cross section for the Yukawa; show that $\mu\to0$ gives the Rutherford form and check the divergence of the total cross section. *Zettili:* **Problem 11.1**, Problem 11.5; Exercises 11.3, 11.5, 11.7 to 11.9.
2. **Hard-sphere:** find $\delta_\ell=-\arctan\frac{j_\ell(ka)}{n_\ell(ka)}$; show $\delta_0=-ka$ and $\sigma_{\rm low\text{-}E}=4\pi a^2$ (four times the geometric cross section $\pi a^2$); at high energy $\sigma\to2\pi a^2$. *Zettili:* Problem 11.3.
3. **Square well, $\ell=0$:** derive $k\cot(ka+\delta_0)=K\cot Ka$ and the scattering length; show that a zero-energy resonance occurs when $KR=\frac\pi2$ (the first bound state appears) and the cross section $\sigma\to\infty$ as $a\to\infty$. *Zettili:* Problem 11.4; Exercise 11.11.
4. **Delta-shell potential:** for $V=\lambda\delta(r-R)$ match the $\ell=0$ radial solutions across the shell (the derivative jumps by $\frac{2m\lambda}{\hbar^2}u(R)$), obtain $\tan\delta_0$ as a function of $k$, $R$ and $\lambda$, and the condition for a bound state ($\lambda<0$ and sufficiently strong). *Zettili:* Problem 11.2; Exercises 11.4 and 11.6.
5. **Optical theorem check:** for a purely elastic $s$-wave amplitude $f=\frac{e^{2i\delta}-1}{2ik}$ verify $\sigma=\frac{4\pi}{k}\mathrm{Im}f(0)=\frac{4\pi}{k^2}\sin^2\delta$. *Zettili:* Section 11.4.2; Problem 11.8(b).
6. **Breit-Wigner fit:** model $\delta_1(E)$ for the $\Delta(1232)$ with $E_R=1232$ MeV and $\Gamma=117$ MeV (verify) and sketch $\sigma$ including the factor $\frac{4\pi(2\ell+1)}{k^2}$; compute the unitarity limit for a $p$-wave at $k\approx227$ MeV/c. *Zettili:* not covered; use Problem 11.6 for the partial-wave bookkeeping, resonances from Sakurai or Griffiths.
7. **Effective range and the deuteron:** with $a_t=5.4$ fm and $r_t=1.75$ fm, the bound-state pole $k=i\kappa$ satisfies $-\frac1a+\frac12r_0(i\kappa)^2=i(i\kappa)\Rightarrow\kappa\approx0.2316$ fm$^{-1}$ ($E_B\approx2.22$ MeV; verify). Check that the zero-range relation $\kappa=1/a$ gives $0.185$ fm$^{-1}$ and $1.4$ MeV, and that the effective-range correction brings it close to the true value. *Zettili:* not covered (the low-energy limits appear in Problems 11.2 and 11.4); use Sakurai.
8. **Identical particles:** compute the differential cross section for two identical spin-0 bosons ($f(\theta)+f(\pi-\theta)$) and for unpolarized spin-1/2 fermions ($\frac14$ weight for symmetric and $\frac34$ for antisymmetric spin states in the Mott formula). *Zettili:* Section 11.5; Exercise 11.13.
9. **Born validity:** for a square well of depth $V_0$ and range $R$, derive the condition $\frac{mV_0R^2}{\hbar^2}\ll1$ (low energy) and $\frac{V_0}{E}\ll1$ (high energy) for the first Born approximation. *Zettili:* Section 11.3.2; Exercise 11.6(b).
10. **Yukawa as meson exchange:** with $\mu=m_\pi c/\hbar$, compute the range $1/\mu\approx1.4$ fm and interpret $\frac{1}{q^2+\mu^2}$ as the propagator of a massive exchange particle (tree-level diagram). *Zettili:* Problem 11.1 for the calculation; the exchange interpretation is in Halzen and Martin.

## Optional extension

Numerically compute phase shifts for a square-well or Yukawa potential by integrating the radial equation out to a large radius and matching to spherical Bessel functions (a 40-line script), plot $\delta_\ell(E)$ and the cross section, and locate a resonance for $\ell=1$ with a centrifugal barrier plus well. Then extract the pole position from the energy dependence of the S-matrix.

## Pitfalls

- Sign convention of the scattering length: $a>0$ with a bound state in the convention $k\cot\delta=-1/a$ (some books use the opposite).
- Forgetting that $f(\theta)$ is not the same as the wave function; $\frac{d\sigma}{d\Omega}$ is a ratio of fluxes.
- Using the Born approximation at low energy for a strongly binding potential.
- Dropping the $e^{i\delta_\ell}$ phase in the amplitude so the optical theorem fails.
- Confusing the centre-of-mass and laboratory differential cross section.

## Gate questions

1. Why does unitarity bound the partial-wave cross section even for arbitrarily strong interactions?
2. What does a pole of the S-matrix at complex energy mean physically, and how does its imaginary part relate to a lifetime?
3. Why is the Born series the QM analogue of a perturbation series in Feynman diagrams?

## One-page cheat sheet contents

Cross-section definitions, Born formula, partial-wave formulas, optical theorem, scattering length and effective range, Breit-Wigner, unitarity limit, Rutherford.
