# Appendix: constants, notation, calendar, tracking and glossary

> All values and book descriptions are from memory. Verify them against your copies.

## 1. Pinning the guide to your six books

I have not seen your tables of contents. To pin each module to exact chapters, sections and problem numbers, either:

- do **Task 0 of Module 01** (`notes/reading_map.md`), or
- upload the tables of contents (and the problem lists, if you like) and I will rewrite each module's reading plan and exercise list with exact references, as was done for the quantum-mechanics guide.

How to choose exercises from your books (by keyword; the keywords are listed in each module):

1. Search the end-of-chapter problems for the keywords; pick one problem per exercise (two for the exercises marked as core in your book).
2. Attempt it blind for 20 minutes, then compare with a solution or your consistency checks.
3. If you are stuck for more than 20 minutes, mark it and redo it two days later.
4. Use other problems only to repair weaknesses found by a gate question.

## 2. Constants and conversions (cgs, with SI where useful)

| Quantity | Value |
| --- | --- |
| $k_B$ | $1.381\times10^{-16}$ erg/K; $8.617\times10^{-5}$ eV/K |
| $h$, $\hbar$ | $6.626\times10^{-27}$, $1.055\times10^{-27}$ erg s |
| $c$ | $2.998\times10^{10}$ cm/s |
| $G$ | $6.674\times10^{-8}$ cgs |
| $m_u$, $m_e$, $m_p$, $m_n$ | $1.661\times10^{-24}$, $9.109\times10^{-28}$, $1.673\times10^{-24}$, $1.675\times10^{-24}$ g |
| $a=\pi^2k^4/15\hbar^3c^3$ | $7.566\times10^{-15}$ erg cm$^{-3}$ K$^{-4}$ |
| $\sigma_{\rm SB}=ac/4$ | $5.670\times10^{-5}$ cgs |
| $e^2$ | $2.307\times10^{-19}$ erg cm |
| $m_ec^2$ | $0.511$ MeV $\leftrightarrow5.93\times10^9$ K |
| $\alpha=e^2/\hbar c$ | $1/137.04$ |
| 1 eV | $1.602\times10^{-12}$ erg $\leftrightarrow11604$ K |
| Electron density from density | $n_e=\rho/(\mu_em_u)$ |
| Relativity parameter | $x=p_F/m_ec=(\rho/\mu_eB)^{1/3}$, $B=9.74\times10^5$ g/cm$^3$ |
| Non-relativistic degenerate $P$ | $1.0036\times10^{13}(\rho/\mu_e)^{5/3}$ |
| Ultra-relativistic degenerate $P$ | $1.2435\times10^{15}(\rho/\mu_e)^{4/3}$ |
| Degeneracy temperature | $T_F\approx3\times10^5(\rho/\mu_e)^{2/3}$ K (non-relativistic) |
| Photon number density | $n_\gamma\approx20.3\,T^3$ cm$^{-3}$ |
| $\left(\frac{2\pi m_ekT}{h^2}\right)^{3/2}$ | $2.415\times10^{15}T^{3/2}$ cm$^{-3}$ |

Stellar reference points (approximate): solar centre $T=1.57\times10^7$ K, $\rho=150$ g/cm$^3$, $P=2.3\times10^{17}$ dyn/cm$^2$, $\mu_{\rm mol}\approx0.85$; solar photosphere $T=5772$ K; white dwarf core $\rho\sim10^6$ to $10^8$ g/cm$^3$.

## 3. Notation used in the guide

| Symbol | Meaning |
| --- | --- |
| $U$, $u$ | internal energy, energy density (or per unit mass; the module says which) |
| $S$, $s$ | entropy, entropy per particle or per baryon |
| $F,H,G,\Omega$ | Helmholtz, enthalpy, Gibbs, grand potential |
| $\mu$ (chemical potential), $\mu_{\rm mol}$ (mean molecular weight), $\mu_e$ (per electron) | careful: three different "mu"s |
| $X,Y,Z$ | hydrogen, helium, metal mass fractions |
| $\chi_\rho,\chi_T$ | $\partial\ln P/\partial\ln\rho$, $\partial\ln P/\partial\ln T$ |
| $\delta=-(\partial\ln\rho/\partial\ln T)_P$ | thermal expansion in stellar notation |
| $\Gamma_1,\Gamma_2,\Gamma_3$ | adiabatic exponents; $\nabla_{\rm ad}$ adiabatic gradient |
| $\beta=P_{\rm gas}/P$ | gas pressure fraction |
| $\lambda=h/\sqrt{2\pi mkT}$ | thermal de Broglie wavelength |
| $z=e^{\mu/kT}$ | fugacity |
| $\Gamma$ (plasma) | coupling parameter $Z^2e^2/a_ikT$ (not an adiabatic exponent) |
| $g_s$ | spin degeneracy |
| $x$, $\theta$ | relativity parameters $p/mc$ and $kT/mc^2$ |
| $\eta$ | degeneracy parameter $\mu/kT$ |

## 4. Suggested 35-week calendar (8 hours a week)

| Weeks | Module |
| --- | --- |
| 1 | 01 Prerequisites and tools |
| 2 to 3 | 02 Thermodynamic foundations |
| 4 to 5 | 03 Potentials, Maxwell relations, stability |
| 6 to 7 | 04 Adiabatic processes |
| 8 to 9 | 05 Chemical and phase equilibrium |
| 10 to 11 | 06 Microcanonical ensemble |
| 12 to 13 | 07 Canonical ensemble |
| 14 to 15 | 08 Grand canonical ensemble |
| 16 to 17 | 09 Quantum statistics |
| 18 to 20 | 10 Degenerate Fermi gases |
| 21 to 22 | 11 Photons, Bose gases, phonons |
| 23 to 25 | 12 Interacting systems and plasmas |
| 26 to 27 | 13 Phase transitions |
| 28 to 29 | 14 Kinetic theory, LTE, transport |
| 30 to 32 | 15 Stars and dense matter |
| 33 to 35 | 16 Readiness test and projects |

**Fast path (about 18 weeks):** pass the skip-tests of Modules 01 to 05 and 07 (record them as done), then do Modules 08 to 12, 14 and 15 in full, 13 in condensed form, and 16.

## 5. Tracking template

Keep `notes/progress.md`:

| Module | Skip-test passed? | Reading done | Derivations (of 5) | Exercises (of 10) | Gate questions | Cheat sheet | Date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | | | | | | | |
| 02 | | | | | | | |
| 03 | | | | | | | |
| 04 | | | | | | | |
| 05 | | | | | | | |
| 06 | | | | | | | |
| 07 | | | | | | | |
| 08 | | | | | | | |
| 09 | | | | | | | |
| 10 | | | | | | | |
| 11 | | | | | | | |
| 12 | | | | | | | |
| 13 | | | | | | | |
| 14 | | | | | | | |
| 15 | | | | | | | |
| 16 | | | | | | | |

## 6. Conventions to fix in your notes (and never change)

| Item | Recommended convention |
| --- | --- |
| Units | cgs for stellar numbers; say which for each calculation |
| Entropy and particle number | per particle $s/k$ or per baryon $s/k_B$; state which |
| Energy density versus per mass | write $u$ (per volume) and $u_m$ (per mass) |
| Chemical potential | include or exclude rest mass explicitly; for relativistic work include it |
| Degeneracy factor | $g_s=2$ for electrons, protons, neutrons; $g_s=1$ per neutrino helicity state |
| Mean molecular weights | state $\mu_{\rm mol},\mu_e,\mu_{\rm ion}$ separately |
| Partial derivatives | always write the variable held fixed |

## 7. Pitfalls that recur across the guide

1. Mixing the three chemical-potential-like quantities ($\mu$, $\mu_{\rm mol}$, $\mu_e$).
2. Assigning a chemical potential to a non-conserved quantity.
3. Forgetting $1/N!$, spin degeneracy $g_s$ or the factor 2 for photon polarization.
4. Using the Sommerfeld expansion or Debye-Hueckel outside their ranges.
5. Applying thermodynamic stability conditions to self-gravitating systems.
6. Building an EOS from independent fits to $P$ and $u$ (inconsistent) instead of from one potential.
7. Trusting remembered numbers: every check value should be verified against a primary source.

## 8. Glossary

- **BEC:** Bose-Einstein condensation. **FD, BE, MB:** Fermi-Dirac, Bose-Einstein, Maxwell-Boltzmann.
- **LTE, NLTE:** local and non-local thermodynamic equilibrium.
- **NSE:** nuclear statistical equilibrium.
- **OCP:** one-component plasma.
- **EOS:** equation of state.
- **KH:** Kelvin-Helmholtz (timescale).
- **vdW:** van der Waals.

## 9. What this guide deliberately leaves out

- Heat engines, refrigerators and thermodynamic cycles beyond the second-law logic.
- Magnetism and condensed-matter applications other than degenerate gases, plasmas and phonons.
- The renormalization group and exact solutions of the 2D Ising model.
- Linear-response theory, Green-Kubo formulas and the full machinery of non-equilibrium statistical mechanics.
- Quantum field theory at finite temperature and density (the natural next step for relativistic matter).
- Interacting Fermi systems beyond the Debye-Hueckel, ion-sphere and exchange corrections (nuclear many-body theory, Fermi liquids, superfluidity and BCS pairing).
