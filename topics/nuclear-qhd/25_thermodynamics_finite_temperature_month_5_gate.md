# Module 25: Thermodynamics, finite temperature and the relativistic crust (Week 24), with the Month-5 gate

**Books:** Walecka's "Some Thermodynamics" chapter; Glendenning, *Compact Stars*, chapters 4 to 5; your thermodynamics guide (Modules 03, 10, 15) for the formalism.
**Time:** 1 week. If proto-neutron stars are out of scope, the finite-$T$ part lightens; the rearrangement term and the consistency lesson do not.

## Why this matters

(i) **The partition function at $T\neq0$**: needed for the envelope (Module 27) and the natural bridge to Kapusta and Gale. (ii) **Thermodynamic consistency with density-dependent couplings**: the rearrangement term; omit it and your pressure is wrong and your TOV solution silently wrong with it. (iii) **RMF for inhomogeneous matter**: relativistic Thomas-Fermi and pasta, so you have seen a unified relativistic treatment spanning crust and core.

## Skip-test (40 minutes, no notes)

1. Construct the grand partition function of QHD-I in mean-field theory; derive $\varepsilon$, $P$, $s$ at finite $T$; verify the $T\to0$ limit reproduces Module 23.
2. For density-dependent $g_s(n_B)$ derive the rearrangement term and show what breaks if it is dropped.
3. State the Thomas-Fermi approximation for inhomogeneous matter.
4. Compute the thermal energy and entropy per baryon of a degenerate nucleon gas at $kT=10$ MeV.
5. Give the Gibbs-Duhem check that detects a missing rearrangement term.

## Prerequisites

Modules 22 to 24; thermodynamics guide Module 03.

## Detailed topics (checklist)

**Finite-$T$ mean field [Must]**
- $\Omega/V=-P=-\frac{\gamma}{(2\pi)^3}kT\int d^3k\left[\ln(1+e^{-(E^*-\nu)/kT})+\ln(1+e^{-(E^*+\nu)/kT})\right]-\frac{g_v^2}{2m_v^2}n_B^2\ldots+\tfrac12m_s^2\phi_0^2$ (particles and antiparticles, $E^*=\sqrt{k^2+M^{*2}}$, $\nu=\mu-g_vV_0$); $M^*$ from $\frac{\partial\Omega}{\partial M^*}=0$ at fixed $T,\mu$; $s=-\frac{\partial\Omega}{\partial T}$, $\varepsilon=Ts-P+\mu n_B$; the $T\to0$ limit gives Module 23. Thermal corrections to a degenerate gas: $\varepsilon_{\rm th}\approx\frac{\pi^2}{4}\frac{n(kT)^2}{E_F}$ per baryon, $s\approx\frac{\pi^2}{2}\frac{kT}{E_F}$.

**Rearrangement term [Must]**
- For couplings $g_i(n_B)$: the chemical potential acquires $\Sigma^r=\frac{\partial g_v}{\partial n_B}V_0n_B-\frac{\partial g_s}{\partial n_B}\phi_0n_s$ (sign conventions per your source), and $P=P_{\rm naive}+n_B\Sigma^r$; without it $P\ne n_B^2\frac{d(\varepsilon/n_B)}{dn_B}$.

**Inhomogeneous matter [Should]**
- Relativistic Thomas-Fermi: replace the density by the local Fermi-gas value and solve the meson equations with sources; spherical cells and pasta; a unified relativistic crust-core treatment.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Walecka thermodynamics chapter; exercises 1 and 4 |
| Session 2 | Rearrangement terms; exercises 2 and 3 |
| Session 3 | Thomas-Fermi for crust matter; exercises 5 and 6 |
| Session 4 | Exercises 7 to 10; the Month-5 gate |

## Derive from scratch

1. The finite-$T$ grand potential and $s$.
2. The $T\to0$ limit.
3. The rearrangement term from $\frac{\partial\Omega}{\partial n_B}$ with $g(n_B)$.
4. The thermal energy and entropy of a degenerate gas.
5. The consistency check via Gibbs-Duhem.

## Bare-minimum exercises (with expected results)

1. **Degenerate-gas thermal numbers:** for nucleons with $E_F=37$ MeV at $kT=10$ MeV: $\varepsilon_{\rm th}/N\approx\frac{\pi^2}{4}\frac{(kT)^2}{E_F}=6.7$ MeV and $s\approx\frac{\pi^2}{2}\frac{kT}{E_F}=1.33\,k_B$ per baryon (the Sommerfeld expansion is marginal at $kT/E_F=0.27$).
2. **Rearrangement term:** write $\mathcal L$ with $g_s(n_B)$; derive $P$ from $-\Omega/V$ and from $n_B^2\frac{d(\varepsilon/n_B)}{dn_B}$; the difference is $n_B\Sigma^r$; show the identity holds only with it.
3. **What breaks:** a pressure computed without $\Sigma^r$ violates $dP=n_Bd\mu_B$ (Gibbs-Duhem); the error grows with $\frac{\partial g}{\partial n_B}$ and is silently carried into the TOV equation.
4. **$T\to0$ limit:** show $-\frac{\Omega}{V}\to P$ of Module 23 as $T\to0$ (the logarithms become step-function integrals); antiparticles drop out.
5. **Antiparticles:** at $kT=10$ MeV the antinucleon population is negligible ($e^{-M^*/kT}\sim e^{-50}$); at $kT\sim100$ MeV it matters (heavy-ion regime).
6. **Thomas-Fermi at a cell:** a cell with a nucleus of central density $n_{\rm in}$ and gas density $n_g$: the local $M^*(r)$ and $V_0(r)$ follow from the uniform-matter relations at the local density (gradient terms neglected); list the corrections.
7. **Gibbs-Duhem check (numerical test):** compute $P$ and $\mu_B$ on a density grid for a density-dependent-coupling EOS with and without $\Sigma^r$ and monitor $\frac{dP}{dn_B}-n_B\frac{d\mu_B}{dn_B}$: zero only with the term.
8. **Entropy per baryon in a proto-neutron star:** $s/k\approx1$ to $2$ at birth; state how it changes the proton fraction and the EOS softness qualitatively.
9. **Where finite $T$ enters this guide:** the envelope (Module 27) uses $T$ in the crust but not in the nuclear EOS; the core EOS is cold ($kT\ll E_F$).
10. **Gate prep:** attempt the seven items below.

## Blank-page gate: Month 5 (the hardest gate in the plan)

1. The QHD-I Lagrangian from memory; the field equations.
2. The mean-field reduction; the three coupled equations; **the saturation mechanism in plain language.**
3. $\varepsilon$ and $P$; only $C_s^2$, $C_v^2$ appear; thermodynamic consistency and where self-consistency was used.
4. QHD-I's predictions for $K$ and $M^*$; their failure; the repair.
5. The $\rho$; $S(n)$; $J$ and $L$ in terms of couplings.
6. Non-relativistic reduction with large $S$ and $V$; the spin-orbit term; the shell model's anomalous coefficient.
7. $v_s\to c$ from below as $n_B\to\infty$.

## Optional extension

Compute $s(n_B,T)$ and $P(n_B,T)$ for QHD-I numerically at $kT=10$ and $30$ MeV and compare with the degenerate-gas expansions.

## Pitfalls

- Using $\mu$ without subtracting the vector potential in the Fermi-Dirac functions.
- Omitting the rearrangement term in density-dependent models.
- Applying Thomas-Fermi where gradient corrections are large (nuclear surfaces).

## Gate questions

1. Why does a density-dependent coupling need a rearrangement term?
2. How does the $T\to0$ limit reproduce Module 23?
3. What does Thomas-Fermi neglect?

## One-page cheat sheet contents

Finite-$T$ formulas; Sommerfeld thermal numbers; rearrangement term and the Gibbs-Duhem test; Thomas-Fermi.
