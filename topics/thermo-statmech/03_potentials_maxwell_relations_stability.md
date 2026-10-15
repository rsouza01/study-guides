# Module 03: Thermodynamic potentials, Maxwell relations and stability

**Books:** Callen (Legendre transformations, extremum principles in transformed representations, Maxwell relations, stability; Part I, roughly chapters 5 to 8), Schroeder (chapter 5), Blundell and Blundell (thermodynamic potentials).
**Time:** 2 weeks.

## Why this matters for stars and EOS

- An EOS used in a stellar code is usually built from a **Helmholtz free energy** $F(\rho,T,{\rm composition})$; every other quantity follows by differentiation, and consistency is automatic only if you do it this way.
- The quantities $\chi_\rho=(\partial\ln P/\partial\ln\rho)_T$, $\chi_T=(\partial\ln P/\partial\ln T)_\rho$, $c_V$, $c_P$, $\delta=-(\partial\ln\rho/\partial\ln T)_P$ are **response functions**, tied by **Maxwell relations**. Knowing the relations lets you check an EOS and derive the missing one.
- **Stability conditions** explain why a convective core, a degenerate gas or a nuclear-burning shell behaves as it does, and why gravitating systems can have negative specific heat without violating thermodynamics.

## Skip-test (40 minutes, no notes)

1. Define $F=U-TS$, $H=U+PV$, $G=U-TS+PV$, $\Omega=U-TS-\mu N$ and write their differentials.
2. Derive the four Maxwell relations from the mixed second derivatives of $U,F,H,G$.
3. Show $C_P-C_V=TV\alpha^2/\kappa_T$ and $\gamma=C_P/C_V=\kappa_T/\kappa_S$.
4. Show $\left(\frac{\partial U}{\partial V}\right)_T=T\left(\frac{\partial P}{\partial T}\right)_V-P$ and evaluate it for the ideal gas (0) and for blackbody radiation ($u=aT^4$).
5. State the stability conditions $C_V>0$, $\kappa_T>0$ and derive one from the convexity of $U(S,V)$ or the concavity of $S(U,V)$.

## Prerequisites

Modules 01 and 02.

## Detailed topics (checklist)

**Legendre transforms and potentials**
- Legendre transform of a convex function, the geometric meaning, change of natural variables: $U(S,V,N)\to F(T,V,N)\to G(T,P,N)$, $H(S,P,N)$, grand potential $\Omega(T,V,\mu)$.
- Differentials: $dF=-SdT-PdV+\mu dN$, $dH=TdS+VdP+\mu dN$, $dG=-SdT+VdP+\mu dN$, $d\Omega=-SdT-PdV-Nd\mu$; $\Omega=-PV$ for a homogeneous system.
- Extremum principles: at fixed $(T,V,N)$ equilibrium minimizes $F$; at fixed $(T,P,N)$ it minimizes $G$.
- **Which potential to use:** $F(\rho,T)$ is the natural choice for stellar EOS tables; $\Omega(T,V,\mu)$ is the natural output of the grand canonical ensemble (Module 08).

**Maxwell relations and response functions**
- The four Maxwell relations: $\left(\frac{\partial T}{\partial V}\right)_S=-\left(\frac{\partial P}{\partial S}\right)_V$; $\left(\frac{\partial S}{\partial V}\right)_T=\left(\frac{\partial P}{\partial T}\right)_V$; $\left(\frac{\partial T}{\partial P}\right)_S=\left(\frac{\partial V}{\partial S}\right)_P$; $\left(\frac{\partial S}{\partial P}\right)_T=-\left(\frac{\partial V}{\partial T}\right)_P$.
- Response functions: $\alpha=\frac1V\left(\frac{\partial V}{\partial T}\right)_P$, $\kappa_T=-\frac1V\left(\frac{\partial V}{\partial P}\right)_T$, $\kappa_S$, $C_V$, $C_P$; the identities $C_P-C_V=TV\alpha^2/\kappa_T$, $\kappa_T-\kappa_S=TV\alpha^2/C_P$, $\gamma=C_P/C_V=\kappa_T/\kappa_S$.
- **Stellar notation** (be able to translate): $\chi_\rho=1/(P\kappa_T)$ for fixed composition, $\delta=\alpha T=-(\partial\ln\rho/\partial\ln T)_P$, $\chi_T=\delta\chi_\rho$, $c_P-c_V=\frac{P}{\rho T}\frac{\chi_T^2}{\chi_\rho}$ (per unit mass).
- The Jacobian method: express any derivative of the form $(\partial X/\partial Y)_Z$ through $C_V,\alpha,\kappa_T$ and the EOS.
- Energy equation of state: $\left(\frac{\partial U}{\partial V}\right)_T=T\left(\frac{\partial P}{\partial T}\right)_V-P$, $\left(\frac{\partial H}{\partial P}\right)_T=V-T\left(\frac{\partial V}{\partial T}\right)_P$; the Joule expansion and Joule-Thomson coefficient (brief).

**Stability**
- Local stability from convexity of $U(S,V)$ (or concavity of $S$): $C_V>0$, $\kappa_T>0$ (hence $C_P>C_V>0$, $\kappa_S>0$); Le Chatelier's principle; what happens at a first-order transition (negative $\kappa_T$ regions are unstable; Maxwell construction in Module 13).
- Gravitating systems and systems with long-range forces are not covered by these conditions because additivity and the thermodynamic limit fail (Module 15).

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Callen: Legendre transformations and alternative representations (chapter 5) |
| Lunch 2 | Callen: extremum principles in the transformed representations (chapter 6); Schroeder chapter 5.1 to 5.2 (free energies) |
| Lunch 3 | Callen: Maxwell relations and applications (chapter 7) |
| Lunch 4 | Callen: stability (chapter 8); Blundell and Blundell on potentials |
| Week 2 lunches | Schroeder chapter 5 problems on thermodynamic identities; review |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. The four potentials and their differentials from successive Legendre transforms.
2. The four Maxwell relations.
3. $C_P-C_V=TV\alpha^2/\kappa_T$ via a Jacobian derivation.
4. $\left(\frac{\partial U}{\partial V}\right)_T=T\left(\frac{\partial P}{\partial T}\right)_V-P$.
5. The stability conditions $C_V>0$ and $\kappa_T>0$ from the minimization of $U$ at fixed $S,V$ (second-order conditions).

## Bare-minimum exercises (find matching problems in the books with these keywords)

1. **Potentials of the ideal gas** (Helmholtz, Gibbs free energy): derive $F=-NkT\left[\ln\frac{V}{N\lambda^3}+1\right]$ and $G=NkT\ln(P\lambda^3/kT)$; verify $P=-\partial F/\partial V=NkT/V$ and $G=\mu N$.
2. **Radiation potentials:** $F=-\frac13aVT^4$; derive $P,S,U$ from it and show $G=0$ (since $\mu=0$).
3. **Energy equation:** verify $(\partial U/\partial V)_T=0$ for an ideal gas and $aT^4$ for radiation using $T(\partial P/\partial T)_V-P$.
4. **$C_P-C_V$ for the ideal gas:** $Nk$; for radiation $C_V=4aVT^3$ and $C_P=\infty$ (constant $P$ means constant $T$); explain.
5. **Maxwell-relation derivation:** show $\left(\frac{\partial C_V}{\partial V}\right)_T=T\left(\frac{\partial^2P}{\partial T^2}\right)_V$ and use it to prove that $C_V$ of an ideal gas is independent of volume.
6. **Stellar translation:** from the EOS $P=\rho kT/\mu m_u+aT^4/3$ compute $\chi_\rho$, $\chi_T$, $\delta$ and $c_P-c_V$; check the limits $\beta\to1$ ($\chi_\rho=\chi_T=1$) and $\beta\to0$ ($\chi_\rho=0$, $\chi_T=4$).
7. **Consistency test:** given a proposed EOS $P(\rho,T)$ and $u(\rho,T)$ with $u=\frac{3}{2}\frac{\rho kT}{\mu m_u}+aT^4$, check the energy equation $\left(\frac{\partial u/\rho}{\partial\rho}\right)_T=\frac{1}{\rho^2}\left[P-T\left(\frac{\partial P}{\partial T}\right)_\rho\right]$ (which is the Maxwell relation in per-mass form); an inconsistent pair fails it.
8. **Gibbs free energy of a two-species mixture:** $G=\sum N_i\mu_i$; derive Gibbs-Duhem from it and use it to show $\sum n_id\mu_i=dP$ at constant $T$.
9. **Stability:** show that a van der Waals isotherm below $T_c$ has a region with $\kappa_T<0$ and mark it; explain why the real system phase-separates.
10. **Why gravity breaks the argument:** explain, using additivity, why a self-gravitating gas can have a negative heat capacity.

## Optional extension

Show that for a monatomic ideal gas mixed with radiation, $c_V$, $c_P$, and $\nabla_{\rm ad}=\frac{P\delta}{\rho Tc_P}$ can be written entirely in terms of $\beta$; this is done in Module 04.

## Pitfalls

- Using Maxwell relations without keeping $N$ (or composition) fixed where it matters.
- Confusing the isothermal ($\kappa_T$) and adiabatic ($\kappa_S$) compressibility; the sound speed uses $\kappa_S$.
- Forgetting that $\Omega=-PV$ only holds for homogeneous systems.
- Believing that thermodynamic stability conditions apply to a star as a whole.

## Gate questions

1. Why does a free-energy minimum at fixed $(T,V)$ correspond to equilibrium, and what is minimized at fixed $(T,P)$?
2. Why is it enough to know $F(T,V,N)$ to get the complete EOS?
3. Why must $C_P\ge C_V$?

## One-page cheat sheet contents

Potentials and differentials; Maxwell relations; response-function identities; stellar notation dictionary; stability conditions.
