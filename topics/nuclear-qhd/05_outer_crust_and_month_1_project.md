# Module 05: The outer crust (★) and the Month-1 project (Weeks 3 and 4)

**Books:** Shapiro and Teukolsky chapter 2 and sections 3.1 to 3.5; HPY chapter 2 and sections 3.1 to 3.3; Chamel and Haensel sections 2 and 3. **Primary paper: Baym, Pethick and Sutherland (1971), ApJ 170, 299**: ten pages, completely readable.
**Time:** 2 weeks (Week 3 content, Week 4 consolidation and the computational task).

## Why this matters

You assemble the outer crust from three ingredients you already have: nuclei on a bcc lattice in a relativistic degenerate electron gas, with lattice energy per cell $E_L=-0.895929\frac{Z^2e^2}{a}$, $a=\left(\frac{3}{4\pi n_N}\right)^{1/3}$. That Madelung constant does real work: a $\sim5$ percent energy correction that shifts the drip density and the composition sequence. Collect also $\Gamma=\frac{Z^2e^2}{ak_BT}$ and melting at $\Gamma_m\approx175$: the crust's phase diagram, and the boundary between the **ocean** and the solid crust. **The astrophysical payoff arrives before the hard theory, so the theory has somewhere to land.**

## Skip-test (40 minutes, no notes)

1. Derive the Wigner-Seitz Coulomb energy $-\tfrac9{10}\frac{Z^2e^2}{a}$ and state why the bcc coefficient $0.8959$ differs.
2. Write $\varepsilon_{\rm tot}/n_B=$ nuclear rest mass $+$ electron kinetic $+$ lattice; form $g=\frac{\varepsilon+P}{n_B}$ and state the variational problem.
3. Show the $P\to0$ minimum is $^{56}$Fe and explain why rising pressure drives the sequence to larger $N/Z$ rather than larger $A$.
4. Estimate the density at which $\mu_e$ exceeds the $^{56}$Fe$\to{}^{56}$Mn capture threshold.
5. Define neutron drip and state the density ($\approx4\times10^{11}$ g/cm$^3$).

## Prerequisites

Modules 02 and 04.

## Detailed topics (checklist)

**Ingredients [Must]**
- Relativistic degenerate electrons (Module 02); nuclei with number density $n_N=\frac{n_e}{Z}$ and baryon density $n_B=An_N$; lattice energy density $\varepsilon_L=E_Ln_N$ and pressure $P_L=\tfrac13E_Ln_N$ (negative: a negative pressure favouring large $Z$, since $E_L\propto n_N^{1/3}$); the coupling parameter $\Gamma=\frac{Z^2e^2}{ak_BT}$ and melting at $\Gamma_m\approx175$.

**The variational problem [Must]**
- At fixed pressure minimise $g(A,Z;P)=\frac{\varepsilon+P}{n_B}$ over the mass table; at $P\to0$ the minimum is $^{56}$Fe (the lowest atomic mass per nucleon, not the most bound per nucleon: that is $^{62}$Ni); compression adds electron Fermi energy that is reduced by capture, producing the sequence $^{56}$Fe, $^{62}$Ni, then the $N=50$ chain, then the $N=82$ chain near drip.
- **Why Gibbs and not energy:** the stable state at fixed pressure has the smallest $\mu_B$ (Module 02). Minimising the energy density at fixed density is a different constraint and gives the wrong composition.

**Drip [Must]**
- Neutron drip where $\mu_n=m_nc^2$ (equivalently the neutron separation energy of the optimal nuclide, shifted by the lattice and electron terms, vanishes): $\rho_{\rm drip}\approx4\times10^{11}$ g/cm$^3$, $n_B\approx2.6\times10^{-4}$ fm$^{-3}\sim10^{-3}n_0$.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Shapiro-Teukolsky 2 and 3.1 to 3.5; the lattice energy |
| Session 2 | BPS (1971): read the whole paper |
| Session 3 | Chamel-Haensel 2 to 3; exercises 1 to 6 |
| Session 4 | Exercises 7 to 10; the Month-1 gate |
| Sessions 5 to 8 | The computational task |

## Derive from scratch

1. The Wigner-Seitz Coulomb energy.
2. The lattice pressure $P_L=\tfrac13E_Ln_N$.
3. $g=\frac{\varepsilon+P}{n_B}$ and why it is minimised.
4. Why compression drives the composition neutron-rich.
5. The drip condition.

## Bare-minimum exercises (with expected results)

1. **Wigner-Seitz energy:** the energy of a sphere of radius $a$ with uniform neutralising background is $-\tfrac9{10}\frac{Z^2e^2}{a}$; the bcc lattice sum $-0.895929\frac{Z^2e^2}{a}$ is $\approx0.5$ percent lower in magnitude (the spherical cell overestimates).
2. **Coupling and melting:** for $^{56}$Fe at $\rho=10^7$ g/cm$^3$, $a=1.3\times10^{-10}$ cm and $\Gamma=\frac{Z^2e^2}{ak_BT}\approx86\frac{10^8\,{\rm K}}{T}$; melting at $\Gamma_m=175$ gives $T_m\approx5\times10^7$ K.
3. **The variational problem:** with $\varepsilon=n_NM_{\rm nuc}c^2+\varepsilon_e+E_Ln_N$, $P=P_e+\frac13E_Ln_N$, $n_e=Zn_N$ and $\varepsilon_e+P_e=n_e\mu_e$ show $g(A,Z;P)=\frac{M_{\rm nuc}(A,Z)c^2+Z\mu_e+\frac43E_L}{A}$, where $\mu_e$ is fixed by $P=P_e(\mu_e)+P_L$; state the minimisation over $(A,Z)$ at each $P$.
4. **$^{56}$Fe versus $^{62}$Ni:** atomic mass per nucleon $0.998838$ u for $^{56}$Fe, $0.998844$ u for $^{62}$Ni and $0.998850$ u for $^{58}$Fe: $^{56}$Fe is lowest by only $\approx6$ keV per nucleon, while $^{62}$Ni has the highest binding energy per nucleon.
5. **The first transition:** the $^{56}$Fe$\to{}^{62}$Ni transition occurs at about $8\times10^6$ g/cm$^3$ (published value; reproduce it in the project): lattice and electron terms favour the more neutron-rich nuclide long before the capture threshold of exercise 6.
6. **Capture-threshold density:** $^{56}$Fe$\to{}^{56}$Mn needs $\mu_e>4.21$ MeV, i.e. $p_Fc=4.17$ MeV and $n_e=\frac{(p_F/\hbar)^3}{3\pi^2}=3.2\times10^{-7}$ fm$^{-3}$, $\rho=\frac{n_em_uA}{Z}\approx1.1\times10^9$ g/cm$^3$: the simple threshold is *not* where the composition changes, because the true sequence minimises $g$ including the lattice.
7. **Lattice pressure:** $P_L=\tfrac13E_Ln_N<0$; show it is a few percent of $P_e$ at $\rho=10^8$ g/cm$^3$ and grows relative to $P_e$ with $Z$.
8. **Drip:** at drip $n_B\approx2.6\times10^{-4}$ fm$^{-3}$ and $P\approx5\times10^{29}$ dyn/cm$^2$ (verify against BPS); explain in three sentences why drip occurs there and not at $n_0$.
9. **Sequence from shell closures:** the composition plateaus at $N=50$ ($^{86}$Kr, $^{84}$Se, $^{82}$Ge, $^{80}$Zn) and $N=82$ ($^{126}$Ru, $^{124}$Mo, $^{122}$Zr, $^{120}$Sr) are the closed-shell nuclei with exceptionally large separation energies; state why a closed neutron shell lowers $g$.
10. **Month-1 gate prep:** list the five blank-page items below and attempt each.

## Blank-page gate: Month 1

1. Write the semi-empirical formula; derive the symmetry and Coulomb terms; state the physical origin of the other three.
2. Define $S_n$, $S_p$, vacuum $\beta$-stability; modify the condition for matter with a degenerate electron gas.
3. Write $\varepsilon$ and $P$ for a relativistic degenerate electron gas; take both limits.
4. Write the outer-crust energy functional; state the minimisation principle **and why it is Gibbs energy at fixed pressure**; give the consequence of getting it wrong.
5. Define neutron drip; state the density ($\approx4\times10^{11}$ g/cm$^3$); explain in three sentences why there and not at $n_0$.

## Computational task: **the month's payoff**

Build the outer crust. Take **AME2020** (plus FRDM or HFB-24 for the neutron-rich extrapolation). For pressures $10^{22}$ to $10^{30}$ dyn/cm$^2$: compute $g(P;A,Z)$ = nuclear + electron + lattice, minimise over the table, output composition versus depth and $P(\rho)$.
- **Checks:** $^{56}$Fe at the surface, then $^{62}$Ni near $8\times10^6$ g/cm$^3$, the $N=50$ chain, then the $N=82$ region near drip. **The shell closures appear without you putting them in**: when $N=50$ and $N=82$ emerge as plateaus, you have watched nuclear structure write itself onto a neutron star.
- Then hand $P(\rho)$ to `tov-solver.py` as a low-density segment and check against a published BPS table. About 200 lines, reusable forever.

**Cut if behind:** drop the form-factor material of Module 03. **Never** drop the Gibbs formulation or the computational task.

## Pitfalls

- Minimising the energy density at fixed density instead of $g$ at fixed pressure.
- Forgetting the electron rest mass or the electron chemical potential in $g$.
- Using atomic masses where nuclear masses are needed (electron binding is small but the $Zm_e$ shift matters at the percent-of-$Q$ level).
- Treating the lattice term as a perturbation: it moves the composition sequence.

## Gate questions

1. Why is $^{56}$Fe the ground state of cold catalysed matter and not $^{62}$Ni?
2. Why does the lattice energy favour larger $Z$?
3. What sets the drip density?

## One-page cheat sheet contents

Lattice energy and pressure; $g=\frac{\varepsilon+P}{n_B}$; $\Gamma$ and $\Gamma_m$; the composition sequence; drip density.
