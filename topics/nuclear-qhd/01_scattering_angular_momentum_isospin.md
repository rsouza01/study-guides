# Module 01: Prerequisites I: scattering, angular momentum and isospin (Week S0.1)

**Books:** Griffiths *Quantum Mechanics*, the scattering chapter (partial waves, phase shifts, Born approximation) and section 4.4 (addition of angular momenta); Sakurai chapter 3 (Clebsch-Gordan, Wigner-Eckart); Bertulani (isospin) or Greiner *Quantum Mechanics: Symmetries* chapter 5; your Zettili guide, Modules 06 and 10, if you have them.
**Time:** 1 week (8 to 10 hours).

## Task 0: build your reading map (30 minutes)

In `notes/reading_map.md` make a table with columns *Module, Walecka (1st ed.), Krane, Bertulani, HPY / Chamel-Haensel, done?*, using the module list of the overview as a first guess. Walecka numbering differs between editions; this map is your reference for the whole guide.

## Why this matters

Closes the first of three gaps between "first half of Griffiths" and "opening Walecka Chapter 1". The entire experimental content of the nucleon-nucleon interaction is a table of **phase shifts**: Month 2 is the inverse problem. The shell model is **angular momentum coupling and nothing else**; the isospin algebra ties $T$ to $S$ and $L$ and is the language of the symmetry energy and the $\rho$ meson.

## Skip-test (40 minutes, no notes)

1. Derive $\sigma\to4\pi a^2$ at low energy from the partial-wave expansion and show $a=-\lim_{k\to0}\delta_0/k$.
2. For a square well of depth $V_0$ and radius $R$, find the condition for a bound state and show the scattering length diverges at threshold.
3. For two nucleons in relative $\ell=0$ use antisymmetry to show $S=1\Rightarrow T=0$ and $S=0\Rightarrow T=1$.
4. Evaluate $\boldsymbol\tau_1\cdot\boldsymbol\tau_2=2T(T+1)-3$ and $\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2=2S(S+1)-3$ in the four $(S,T)$ channels.
5. Couple $j_1=1$ and $j_2=\tfrac12$ and write the $|\tfrac32,\tfrac12\rangle$ state in the product basis.

## Prerequisites

Quantum mechanics at the level of Griffiths; a first look at angular momentum.

## Detailed topics (checklist)

**Scattering [Must]**
- Partial-wave expansion $f(\theta)=\frac1k\sum_\ell(2\ell+1)e^{i\delta_\ell}\sin\delta_\ell P_\ell(\cos\theta)$, $\sigma=\frac{4\pi}{k^2}\sum(2\ell+1)\sin^2\delta_\ell$; phase shifts from matching at the boundary; the optical theorem; the Born approximation $f(\mathbf q)=-\frac{2\mu}{\hbar^2}\frac{1}{4\pi}\int V e^{-i\mathbf q\cdot\mathbf r}d^3r$ (with $f=-\frac{2\mu}{\hbar^2q}\int V\sin(qr)\,r\,dr$ for a central $V$).
- Low-energy limit, scattering length $a$ (sign convention: state it), bound-state threshold.

**Angular momentum [Must]**
- Addition, Clebsch-Gordan coefficients, the stretched states, Wigner-Eckart, the reduced matrix element; $\mathbf L\cdot\mathbf S=\tfrac12[J(J+1)-L(L+1)-S(S+1)]$.

**Isospin [Must]**
- $T=\tfrac12$ for the nucleon; conventions on $t_3$; two-nucleon isospin $T=0,1$; the generalized Pauli principle: for two nucleons $(-1)^{L+S+T}=-1$; $\boldsymbol\tau_1\cdot\boldsymbol\tau_2=2T(T+1)-3$.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Griffiths scattering chapter; exercises 1 and 2 |
| Session 2 | Griffiths 4.4 and Sakurai 3: Clebsch-Gordan and Wigner-Eckart; exercise 5 |
| Session 3 | Isospin in Bertulani or Greiner; exercises 3 and 4 |
| Session 4 | Constants card; remaining exercises |

## Derive from scratch

1. The partial-wave expansion of the scattering amplitude.
2. $a=-\lim\delta_0/k$.
3. The square-well bound-state condition and the divergence of $a$.
4. The antisymmetry argument for $(S,T)$.
5. $\boldsymbol\tau_1\cdot\boldsymbol\tau_2=2T(T+1)-3$.

## Bare-minimum exercises (with expected results)

1. **Low-energy cross-section:** $\delta_0\approx-ka$ gives $\sigma\to4\pi a^2$.
2. **Square well bound-state threshold:** with reduced mass $\mu=M/2$ the first bound state exists when $k_0R>\frac\pi2$, i.e. $V_0R^2>\frac{\pi^2\hbar^2}{4M}\approx102$ MeV fm$^2$ (for $R=2.1$ fm, $V_0>23$ MeV); the scattering length $a=R\left(1-\frac{\tan k_0R}{k_0R}\right)$ diverges as $k_0R\to\frac\pi2$ from below. **Keep this page**: Module 07 is this with real numbers.
3. **Antisymmetry:** for $\ell=0$ the spatial wavefunction is symmetric, so the spin-isospin part must be antisymmetric: $S=1\Rightarrow T=0$ (the deuteron), $S=0\Rightarrow T=1$.
4. **Operator values:** $\boldsymbol\tau_1\cdot\boldsymbol\tau_2=-3$ for $T=0$ and $+1$ for $T=1$; $\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2=-3$ for $S=0$ and $+1$ for $S=1$; the four-channel table of products $(\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2)(\boldsymbol\tau_1\cdot\boldsymbol\tau_2)$: $(S,T)=(1,0)\to-3$, $(0,1)\to-3$, $(1,1)\to+1$, $(0,0)\to+9$.
5. **Clebsch-Gordan:** $\left|\tfrac32,\tfrac12\right\rangle=\sqrt{\tfrac13}\,|1,1\rangle\left|\tfrac12,-\tfrac12\right\rangle+\sqrt{\tfrac23}\,|1,0\rangle\left|\tfrac12,\tfrac12\right\rangle$; check normalization and orthogonality to $\left|\tfrac12,\tfrac12\right\rangle$.
6. **Born approximation for a Yukawa potential:** for $V=V_0\frac{e^{-m r}}{mr}$, $f(q)=-\frac{2\mu V_0}{\hbar^2m}\frac{1}{q^2+m^2}$; interpret the pole at $q^2=-m^2$ as the exchanged mass.
7. **Fermi gas numbers:** for symmetric matter $n=\frac{\gamma k_F^3}{6\pi^2}$ with $\gamma=4$; at $n_0=0.16$ fm$^{-3}$, $k_F=1.333$ fm$^{-1}$, $E_F=\frac{\hbar^2k_F^2}{2M}=36.8$ MeV, $\frac{k_F}{M}=0.28$.
8. **Consistency check:** for a non-relativistic degenerate gas $\varepsilon=Mn+\frac35nE_F$; verify $P=n^2\frac{d(\varepsilon/n)}{dn}=\frac25nE_F$.
9. **Conversions:** $n_0=0.16$ fm$^{-3}\leftrightarrow2.66\times10^{14}$ g/cm$^3$ (with the atomic mass unit); 1 MeV/fm$^3\leftrightarrow1.602\times10^{33}$ dyn/cm$^2$.
10. **The constants card (deliverable, 30 minutes):** $\hbar c=197.327$ MeV fm, $e^2=1.4400$ MeV fm, $m_\pi=139.57$ MeV ($\hbar/m_\pi c=1.414$ fm), $M_N=938.92$ MeV, $n_0=0.16$ fm$^{-3}$, $k_F(n_0)=1.33$ fm$^{-1}$, and the two conversions above. Tape it inside the book cover.

## Optional extension

Compute the phase shift for the square well at low energy to first order in $k$ and verify $\delta_0=-ka$ with the $a$ of exercise 2; plot $\sigma(E)$ across the bound-state threshold.

## Pitfalls

- Mixing sign conventions for the scattering length ($k\cot\delta=-1/a$ versus $+1/a$).
- Forgetting the generalized Pauli principle includes isospin.
- Using the neutron or proton as $t_3=+\tfrac12$ inconsistently.

## Gate questions

1. Why does a positive scattering length with a bound state look the same as a repulsive core at low energy?
2. Why is $\ell=0$, $S=1$ forced into $T=0$?
3. What does the Born approximation assume about the potential?

## One-page cheat sheet contents

Partial-wave formulas; scattering length conventions; Clebsch-Gordan table for $1\otimes\frac12$ and $\frac12\otimes\frac12$; $\sigma\cdot\sigma$ and $\tau\cdot\tau$ values; Fermi-gas numbers.
