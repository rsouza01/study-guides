# Module 05: Chemical equilibrium and phase equilibrium

**Books:** Schroeder (chapter 5: chemical thermodynamics, phase transformations), Callen (first-order phase transitions; chemical equilibrium), Pathria (chemical equilibrium in the theory of simple gases), Blundell and Blundell (chemical potential, phase transitions).
**Time:** 2 weeks.

## Why this matters for stars and EOS

- **Ionization and dissociation** (hydrogen, helium, metals, H$_2$) are chemical equilibria; the **Saha equation** is the law of mass action for ionization. It controls the opacity, the convective envelope, and $\Gamma_1,\nabla_{\rm ad}$ in stellar envelopes and atmospheres.
- **Pair equilibrium** ($e^-+e^+\leftrightarrow\gamma\gamma$), **nuclear statistical equilibrium** and **beta equilibrium** ($n\leftrightarrow p+e$) are the same logic with different species and conservation laws.
- **Phase coexistence** (liquid-solid in white dwarfs, nuclear liquid-gas, hadron-quark) is governed by the equality of chemical potentials and pressures.

## Skip-test (40 minutes, no notes)

1. Show that a chemical reaction $\sum_i\nu_iA_i=0$ at fixed $T,P$ is in equilibrium when $\sum_i\nu_i\mu_i=0$.
2. Write the chemical potential of an ideal gas species $\mu=kT\ln\left(\frac{n\lambda^3}{g}\right)$ with $\lambda=\frac{h}{\sqrt{2\pi mkT}}$ (and with internal energy levels $\mu=kT\ln\frac{n\lambda^3}{Z_{\rm int}}$).
3. Derive the law of mass action $\prod_in_i^{\nu_i}=K(T)$ and the Saha equation $\frac{n_en_{i+1}}{n_i}=\frac{2g_{i+1}}{g_i}\left(\frac{2\pi m_ekT}{h^2}\right)^{3/2}e^{-\chi/kT}$.
4. Derive the Clausius-Clapeyron equation $\frac{dP}{dT}=\frac{L}{T\Delta v}$ from $\mu_1=\mu_2$.
5. State the Gibbs phase rule $f=C-p+2$ and apply it to a triple point.

## Prerequisites

Modules 02, 03. (The partition-function derivation of Saha is in Module 08.)

## Detailed topics (checklist)

**Chemical potential and reactions**
- Chemical potential as $\mu=\partial G/\partial N$; equality of $\mu$ at phase coexistence; $\mu$ for classical ideal gases including internal degrees of freedom; reaction equilibrium $\sum\nu_i\mu_i=0$; equilibrium constants; Le Chatelier.
- Conservation laws with several reactions: baryon number, charge, lepton number and the corresponding Lagrange multipliers (the "chemical potential of a conserved charge") with $\mu_i=A_i\mu_B+Q_i\mu_Q+L_i\mu_L$.

**Applications you must master**
- **Saha equation**, including the statistical weights; hydrogen ionization fraction $x$ from $\frac{x^2}{1-x}=\frac{1}{n}\frac{2g_p}{g_H}\left(\frac{2\pi m_ekT}{h^2}\right)^{3/2}e^{-\chi/kT}$ (the prefactor $\left(\frac{2\pi m_ekT}{h^2}\right)^{3/2}=2.415\times10^{15}T^{3/2}$ cm$^{-3}$); the sharpness of the transition with temperature; multi-stage ionization.
- **Dissociation** of H$_2$ (dissociation energy $4.48$ eV) and its effect on heat capacity.
- **Pair equilibrium:** $\mu_{e^-}+\mu_{e^+}=0$, $n_-n_+=4\left(\frac{2\pi m_ekT}{h^2}\right)^3e^{-2m_ec^2/kT}$ (non-degenerate, non-relativistic).
- **Beta equilibrium** $\mu_n=\mu_p+\mu_e+\mu_\nu$ (with $\mu_\nu=0$ for escaping neutrinos) and the idea of nuclear statistical equilibrium (Module 15).

**Phase equilibrium**
- Coexistence conditions $T_1=T_2$, $P_1=P_2$, $\mu_1=\mu_2$; the Gibbs phase rule; Clausius-Clapeyron equation; latent heat and entropy of transformation; the triple and critical points; the Maxwell equal-area construction; metastable states and the spinodal.
- The van der Waals equation as a model: critical constants $kT_c=\frac{8a}{27b}$, $v_c=3b$, $P_c=\frac{a}{27b^2}$.

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Schroeder chapter 5: free energy, equilibrium of reactions |
| Lunch 2 | Blundell and Blundell on the chemical potential; Pathria on chemical equilibrium |
| Lunch 3 | Callen on first-order phase transitions (Clausius-Clapeyron, van der Waals, Maxwell construction) |
| Lunch 4 | Schroeder chapter 5: phase transformations of pure substances and mixtures |
| Week 2 lunches | Review; compute hydrogen and helium ionization by hand |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. The reaction equilibrium condition from minimizing $G$ at fixed $T,P$.
2. The chemical potential of a classical ideal gas from the Sackur-Tetrode entropy: $\mu=kT\ln(n\lambda^3/g)$.
3. The Saha equation from $\mu_e+\mu_{i+1}=\mu_i$ with the internal-energy shift $\chi$.
4. The Clausius-Clapeyron equation, and its integrated form for an ideal-gas vapor.
5. The van der Waals critical constants from $\partial P/\partial v=\partial^2P/\partial v^2=0$.

## Bare-minimum exercises (find matching problems with keywords: Saha, ionization, chemical equilibrium, Clausius-Clapeyron, van der Waals)

1. **Hydrogen ionization:** at $T=10^4$ K and a total hydrogen density $n=10^{15}$ cm$^{-3}$ solve the Saha equation. Expect $x\approx0.4$ ($n_en_p/n_H=3.4\times10^{14}$ cm$^{-3}$ from the right-hand side). Repeat at $T=8000$ and $12000$ K to see the sharp rise.
2. **Hydrogen ionization at stellar densities:** at $T=10^5$ K and $\rho=10^{-8}$ g/cm$^3$ show hydrogen is almost completely ionized; discuss why the Saha formula fails at much higher densities (pressure ionization).
3. **Two-stage helium:** write the two Saha equations for He$\to$He$^+\to$He$^{2+}$ (ionization energies $24.6$ and $54.4$ eV) and find at which temperatures at $n_e\sim10^{14}$ cm$^{-3}$ each stage is half ionized (about $1.5\times10^4$ K for the first stage and $3.3\times10^4$ K for the second; verify numerically).
4. **Molecular hydrogen:** with $\chi=4.48$ eV, estimate the dissociation temperature at $n=10^{16}$ cm$^{-3}$; discuss why the heat capacity rises during dissociation.
5. **Pair equilibrium:** evaluate $n_-=n_+$ at $T=10^{10}$ K (non-degenerate and relativistic limit needed) and at $T=3\times10^9$ K using $n_-n_+=4(2\pi m_ekT/h^2)^3e^{-2m_ec^2/kT}$; discuss its validity (it is non-relativistic; the order of magnitude suffices).
6. **Clausius-Clapeyron:** with $L$ per particle and an ideal-gas vapor, integrate to $P=P_0e^{-L/kT}$; evaluate the slope for water at 100 C (use data from the book) and compare with the observed $dP/dT$.
7. **van der Waals critical point:** derive $T_c,v_c,P_c$ and the law of corresponding states; compute $\frac{P_cv_c}{kT_c}=\frac38$.
8. **Maxwell construction:** for $P=\frac{kT}{v-b}-\frac{a}{v^2}$ at $T=0.9T_c$ find the coexistence pressure by the equal-area rule (numerically); find the two coexisting volumes.
9. **Gibbs phase rule:** for a hydrogen-helium plasma of fixed composition with ionization equilibria how many independent intensive variables ($f=C-p+2$ with chemical reactions removing components) describe the state? (Answer: 2 for $T,\rho$ plus composition, once the reactions are accounted for.)
10. **Conserved charges:** write the equilibrium conditions for $n\leftrightarrow p+e^-+\bar\nu_e$ with neutrinos escaping and with neutrinos trapped; identify the Lagrange multipliers (baryon, charge, lepton number).

## Optional extension

Solve the coupled Saha equations for a hydrogen-helium mixture ($X=0.74,Y=0.25$) over $T=10^3$ to $10^5$ K at fixed density (a 30-line script) and compute the mean molecular weight $\mu_{\rm mol}(T)$ across the ionization zones.

## Pitfalls

- Forgetting the statistical-weight factor $2g_{i+1}/g_i$ and the electron spin factor 2.
- Using the Saha equation outside its validity (high density: non-ideality and pressure ionization; low density: non-equilibrium).
- Mixing the equilibrium constant at fixed $P$ and fixed $V$.
- Treating a conserved charge as if it had an independent chemical potential in every reaction.

## Gate questions

1. Why does the Saha equation give such a sharp ionization transition for hydrogen?
2. What is the thermodynamic meaning of the chemical potential of a conserved charge?
3. Why is the chemical potential equal across a phase boundary but not the density?

## One-page cheat sheet contents

Reaction equilibrium condition; ideal-gas $\mu$; Saha equation with the numeric prefactor; pair equilibrium; Clausius-Clapeyron; van der Waals constants; Gibbs phase rule.
