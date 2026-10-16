# Module 02: Prerequisites II: second quantization and degenerate matter (Week S0.2)

**Books:** Fetter and Walecka, *Quantum Theory of Many-Particle Systems*, Chapter 1 (sections 1 to 4: the single highest-value reading in Session 0); Shapiro and Teukolsky chapter 2 for degenerate gases; your thermodynamics guide, Modules 09 and 10 (quantum statistics, degenerate Fermi gases).
**Time:** 1 week.

## Why this matters

Closes the second and third gaps before Walecka Chapter 1: **second quantization at working fluency** (the Hartree-Fock energy of a Slater determinant, direct and exchange terms) and **the thermodynamics of cold catalysed matter**. Three facts from the second block are used in every later module: thermodynamic consistency $P=n_B^2\frac{d}{dn_B}\left(\frac{\varepsilon}{n_B}\right)$, $\mu_B=\frac{\varepsilon+P}{n_B}$ at $T=0$, and that composition at fixed *pressure* minimises the **Gibbs energy per baryon**, not the energy density.

## Skip-test (40 minutes, no notes)

1. Write the one-body operator $\hat T=\sum\langle\alpha|t|\beta\rangle a^\dagger_\alpha a_\beta$ and the two-body operator $\hat V=\tfrac12\sum\langle\alpha\beta|v|\gamma\delta\rangle a^\dagger_\alpha a^\dagger_\beta a_\delta a_\gamma$.
2. Derive the Hartree-Fock energy of a Slater determinant, identifying direct and exchange terms.
3. Write $n$, $\varepsilon$ and $P$ for a relativistic ideal Fermi gas at $T=0$ and take both limits ($\Gamma=\frac53$ and $\frac43$).
4. Verify $P=n^2\frac{d(\varepsilon/n)}{dn}$ analytically for the ideal Fermi gas.
5. State why composition at fixed pressure minimises the Gibbs energy per baryon $g=\frac{\varepsilon+P}{n_B}$.

## Prerequisites

Module 01; thermodynamics guide Modules 09 and 10 (optional refresh).

## Detailed topics (checklist)

**Second quantization [Must]**
- Creation and annihilation operators, field operators $\psi(\mathbf x)=\sum\phi_\alpha(\mathbf x)a_\alpha$, anticommutators for fermions; occupation-number states; one- and two-body operators; the Slater determinant as $a^\dagger_1\dots a^\dagger_N|0\rangle$.
- **Hartree-Fock:** $E_{\rm HF}=\sum_i\langle i|t|i\rangle+\tfrac12\sum_{ij}\left[\langle ij|v|ij\rangle-\langle ij|v|ji\rangle\right]$ (direct minus exchange); the variational principle giving the HF equations (Module 13 builds the full derivation).

**Degenerate Fermi gases [Must]**
- $n=\frac{\gamma k_F^3}{6\pi^2}$ ($\gamma=2$ for neutrons or electrons, $4$ for symmetric nuclear matter); $\varepsilon=\frac{\gamma}{2\pi^2}\int_0^{k_F}\sqrt{k^2+M^2}\,k^2dk$, $P=\frac{\gamma}{6\pi^2}\int_0^{k_F}\frac{k^4}{\sqrt{k^2+M^2}}dk$, with closed forms $\varepsilon=\frac{\gamma}{16\pi^2}\left[k_FE_F(2k_F^2+M^2)-M^4\ln\frac{k_F+E_F}{M}\right]$ and $P=\frac{\gamma}{48\pi^2}\left[k_FE_F(2k_F^2-3M^2)+3M^4\ln\frac{k_F+E_F}{M}\right]$, $E_F=\sqrt{k_F^2+M^2}$; limits $P\propto n^{5/3}$ ($\Gamma=\frac53$) and $P=\frac\varepsilon3\propto n^{4/3}$ ($\Gamma=\frac43$).

**Thermodynamics of cold catalysed matter [Must]**
- $P=n_B^2\frac{d}{dn_B}\left(\frac\varepsilon{n_B}\right)$ (violate it and a TOV integration is silently wrong); $\mu_B=\frac{d\varepsilon}{dn_B}=\frac{\varepsilon+P}{n_B}$ at $T=0$; Gibbs-Duhem $dP=n_Bd\mu_B$ so at fixed $P$ the stable state has the lowest $\mu_B=g$; "catalysed" means complete $\beta$ equilibrium.

**Optional (about 1 hour):** review the classical multipole expansion of a radiating source (Jackson 9.1 to 9.3 or Griffiths' radiation chapter). Module 16 builds it from scratch, but an hour here saves two there.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Fetter-Walecka 1.1 to 1.2: creation operators, field operators |
| Session 2 | Fetter-Walecka 1.3 to 1.4: one- and two-body operators; Hartree-Fock |
| Session 3 | Degenerate gases (fast review); the three thermodynamic facts |
| Session 4 | Exercises; the exit gate |

## Derive from scratch

1. $\hat V$ in second-quantized form from the first-quantized $\frac12\sum v(\mathbf x_i,\mathbf x_j)$.
2. The HF energy: direct and exchange.
3. $\varepsilon$ and $P$ for the relativistic gas and the two limits.
4. $P=n^2d(\varepsilon/n)/dn$ for the Fermi gas.
5. $\mu_B=(\varepsilon+P)/n_B$.

## Bare-minimum exercises (with expected results)

1. **Number operator and one-body operators:** $\hat N=\sum a^\dagger_\alpha a_\alpha$; for a one-body $t$ diagonal in the basis, $\hat T=\sum t_\alpha a^\dagger_\alpha a_\alpha$ and $\langle\Phi|\hat T|\Phi\rangle=\sum_{i\in{\rm occ}}t_i$.
2. **Direct and exchange:** for a contact interaction $v=v_0\delta^3(\mathbf r_1-\mathbf r_2)$ between spin-$\tfrac12$ fermions, the exchange term cancels the direct term for same-spin pairs, so only opposite-spin pairs interact: $E_{\rm int}=v_0\frac{N_\uparrow N_\downarrow}{V}$.
3. **Fermi gas numbers:** $E/N=\tfrac35E_F$ and $P=\tfrac25nE_F$ (non-relativistic); $\Gamma=\frac{d\ln P}{d\ln n}=\frac53$.
4. **Relativistic limits:** for $M\to0$, $\varepsilon=\frac{\gamma k_F^4}{8\pi^2}$ and $P=\frac{\gamma k_F^4}{24\pi^2}=\frac\varepsilon3$, $\Gamma=\frac43$; check the closed forms reduce to these.
5. **Consistency:** with $\varepsilon\propto n^{4/3}$, $n^2\frac{d(\varepsilon/n)}{dn}=n^2\cdot\frac13\frac{\varepsilon}{n^2}=\frac\varepsilon3=P$.
6. **Chemical potential:** $\mu_B=\frac{d\varepsilon}{dn_B}=\frac43\frac{\varepsilon}{n_B}$ for the ultra-relativistic gas equals $\frac{\varepsilon+P}{n_B}$.
7. **Gibbs minimisation:** use $dP=n_Bd\mu_B$ to show that among candidate configurations at the same $P$ the one with the smallest $g=\mu_B$ is stable (the same argument as the lowest-$\mu$ phase wins in phase coexistence).
8. **Cold catalysed numbers:** for electrons at $\rho=10^7$ g/cm$^3$ with $Y_e=26/56$: $n_e=\frac{\rho Y_e}{m_u}=2.8\times10^{30}$ cm$^{-3}$, $x=\frac{p_F}{m_ec}\approx1.7$, $\mu_e\approx1.0$ MeV (including rest mass).
9. **Conversions:** $P=1$ MeV/fm$^3\leftrightarrow1.602\times10^{33}$ dyn/cm$^2$; the neutron-star crust spans $P\sim10^{22}$ to $10^{33}$ dyn/cm$^2$, i.e. $10^{-11}$ to $\sim1$ MeV/fm$^3$.
10. **Exit gate (blank page, under 15 minutes):** (a) write $\hat V$ in second-quantized form and derive the HF energy, identifying direct and exchange terms; (b) write $\varepsilon$ and $P$ for a relativistic ideal Fermi gas at $T=0$ and verify $P=n^2d(\varepsilon/n)/dn$ analytically.

## Optional extension

Show that the HF exchange term for a spin-saturated gas with a Coulomb interaction gives $\varepsilon_x=-\frac34\left(\frac3\pi\right)^{1/3}e^2n^{4/3}$ (the exchange energy of the electron gas), and compare with the lattice term of Module 05.

## Pitfalls

- Missing the factor $\tfrac12$ in $\hat V$ or the ordering $a_\delta a_\gamma$.
- Using the Fermi-gas formulas with the wrong degeneracy $\gamma$.
- Violating $P=n^2d(\varepsilon/n)/dn$ by adding contributions to $P$ and $\varepsilon$ separately.
- Minimising the energy density at fixed density when the problem is at fixed pressure.

## Gate questions

1. Why does the exchange term have no classical analogue?
2. Why is the lowest $\mu_B$ at fixed $P$ the stable composition?
3. What goes silently wrong in a TOV integration if $P$ and $\varepsilon$ are inconsistent?

## One-page cheat sheet contents

Second-quantized operators; HF energy; relativistic Fermi-gas closed forms and limits; the three thermodynamic identities; conversion factors.
