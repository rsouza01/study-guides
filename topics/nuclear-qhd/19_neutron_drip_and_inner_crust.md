# Module 19: Neutron drip and the inner crust (★, Week 18)

**Books:** **Chamel and Haensel sections 3.2 to 3.3 and 4**; **HPY chapter 3 from section 3.4 onward**. Primary papers: **Baym, Bethe and Pethick (1971)**; **Negele and Vautherin (1973)**; Pethick and Ravenhall, *Ann. Rev. Nucl. Part. Sci.* **45** (1995) 429.
**Time:** 1 week.

## Why this matters

Past $\rho_{\rm drip}\approx4\times10^{11}$ g/cm$^3$ neutrons spill out of nuclei. Three components per cell:
$$E_{\rm cell}=E_{\rm bulk}(n_i,\delta_i)+E_{\rm surf}+E_{\rm Coul}+E_{\rm gas}+E_e,$$
minimised over cell radius, nucleus size and compositions, subject to baryon number and charge neutrality. (i) **Surface-Coulomb balance** gives $E_{\rm surf}=2E_{\rm Coul}$: the same competition as in your Module 14 fission derivation, but with the opposite ratio (see below). (ii) The **in-medium surface tension** falls as the neutron gas thickens, so nuclei *grow* and cells shrink with depth: what destroys spherical geometry in Module 20.

Orientation level: **$^1S_0$ superfluidity of dripped neutrons** (gap $\sim1$ MeV near $k_F\sim0.8$ fm$^{-1}$: ↪ connected both to the Module 07 virtual state and to the Module 12 moment-of-inertia deficit, the same phenomenon in a nucleus), and **entrainment**.

## Skip-test (40 minutes, no notes)

1. Write the drip condition as $\mu_n=m_nc^2$ and explain why drip occurs at $\sim10^{-3}n_0$.
2. Derive $E_{\rm surf}=2E_{\rm Coul}$ by minimising at fixed volume and obtain the equilibrium radius.
3. Compare line by line with your Module 14 fission derivation: what is the same and what differs?
4. Given a Skyrme $E/A(n,\delta)$ and $\sigma(\delta)$, set up the full CLDM minimisation at one pressure.
5. State the $^1S_0$ gap magnitude and where it peaks.

## Prerequisites

Modules 05, 14 and 17.

## Detailed topics (checklist)

**Neutron drip [Must]**
- Drip occurs when the neutron chemical potential of the cell reaches the vacuum value $\mu_n=m_nc^2$; at $\rho_{\rm drip}\approx4.3\times10^{11}$ g/cm$^3$ ($n_B\approx2.6\times10^{-4}$ fm$^{-3}\sim10^{-3}n_0$, $P\approx5\times10^{29}$ dyn/cm$^2$); beyond it a neutron gas coexists with neutron-rich nuclei.

**The compressible liquid-drop model (CLDM) [Must]**
- Cell: a spherical nucleus of radius $R_N$ in a Wigner-Seitz cell of radius $R_c$, $u=\left(\frac{R_N}{R_c}\right)^3$; $E_C=\frac35\frac{Z^2e^2}{R_N}\left(1-\tfrac32u^{1/3}+\tfrac12u\right)$, $E_S=4\pi R_N^2\sigma(\delta,n_{\rm gas})$; bulk and gas energies from a Skyrme functional; minimise $g=\frac{\varepsilon+P}{n_B}$ over $(A,Z,n_{\rm gas},R_c)$ at fixed $P$ subject to baryon-number conservation, charge neutrality, and equality of $\mu_n$ and $P$ between nucleus and gas.
- **Virial relation:** minimising $(E_S+E_C)/V_{\rm cell}$ over $R_N$ at fixed $u$ and densities, $E_S/V\propto\frac1{R_N}$ and $E_C/V\propto R_N^2$ give $E_{\rm surf}=2E_{\rm Coul}$ in all geometries (spheres, rods, slabs).

**Pairing and entrainment [Should, orientation]**
- $^1S_0$ neutron superfluidity: BCS gap $\sim1$ MeV at $k_{Fn}\approx0.8$ fm$^{-1}$ ($n_n\approx0.017$ fm$^{-3}$), $T_c=0.57\Delta\sim7\times10^9$ K, vanishing at $k_F\gtrsim1.3$ fm$^{-1}$; **entrainment** (Bragg scattering of superfluid neutrons by the lattice) reduces the superfluid fraction; glitch reservoir.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Chamel-Haensel 3.2: drip; BBP (1971); exercise 1 |
| Session 2 | The cell energy and the virial relation; exercises 2 and 7 |
| Session 3 | Negele-Vautherin; Pethick-Ravenhall; exercises 3 to 6 |
| Session 4 | Superfluidity orientation; exercises 8 to 10 |

## Derive from scratch

1. The drip condition.
2. $E_S=2E_C$ by the scaling argument and the equilibrium radius.
3. The cell energy and the full set of constraints.
4. The comparison with the fission derivation.
5. The effect of in-medium $\sigma$ on cell size.

## Bare-minimum exercises (with expected results)

1. **Drip:** $\mu_n=m_nc^2$ is reached when the neutron-gas chemical potential becomes positive; at $\rho\approx4.3\times10^{11}$ g/cm$^3$, $n_B=2.6\times10^{-4}$ fm$^{-3}$; explain in three sentences why drip occurs there and not at $n_0$ (nuclei have $S_n\sim$ few MeV and the lattice and electron terms lower the cost of neutron-rich nuclei, so $S_n\to0$ is reached at a low density).
2. **Virial relation (derivation):** with $E_C=\frac{16\pi^2}{15}e^2n_p^2R_N^5c(u)$ (using $Z=\frac{4\pi}{3}R_N^3n_p$ and $c(u)=1-\tfrac32u^{1/3}+\tfrac12u$) and $E_S=4\pi\sigma R_N^2$, minimise $f=\frac{E_S+E_C}{V_{\rm cell}}$, $V_{\rm cell}=\frac{4\pi}{3}\frac{R_N^3}{u}$, to get $R_N=\left[\frac{15\sigma}{8\pi e^2n_p^2c(u)}\right]^{1/3}$ and $E_S=2E_C$; the same scaling $E_S/V\propto R^{-1}$, $E_C/V\propto R^2$ gives $E_S=2E_C$ for rods and slabs.
3. **Illustrative size:** for $\sigma=1$ MeV fm$^{-2}$, $n_p=0.03$ fm$^{-3}$ and $u\approx0.01$ ($c=0.68$) the formula gives $R_N\approx9$ fm (a nucleus of $A\sim10^2$ to $10^3$); redo it at two depths with $\sigma$ falling and $u$ rising to see how the competition between the falling surface tension and the rising screening factor decides whether the nucleus grows.
4. **Compare with fission (line by line):** the isolated drop deformation energy is $\Delta E=\alpha_2^2\left[\frac25E_S-\frac15E_C\right]$ and is stable iff $E_C<2E_S$ ($x<1$); the cell optimum is $E_S=2E_C$ (i.e. $E_C=\frac12E_S$, $x_{\rm eff}=\frac{E_C}{2E_S}=\frac14$). *Same ingredients* ($E_S\propto R^2$, $E_C\propto Z^2/R$), *different question* (stability against deformation versus equilibrium size). The pasta instability (Module 20) occurs when the screened Coulomb energy and the volume fraction make the effective fissility reach 1 for the next geometry.
5. **CLDM minimisation (set-up):** list the unknowns $(A,Z,R_c,n_{\rm gas})$ and the conditions: $\mu_n^{\rm nucleus}=\mu_n^{\rm gas}$, $P^{\rm nucleus}=P^{\rm gas}+\ldots$ (including surface pressure), neutrality $Zn_N=n_e$, total $n_B$, and the cell-size optimisation.
6. **In-medium tension:** $\sigma(\delta)$ decreases with the neutron excess and with surrounding gas density (to zero as the nucleus dissolves); show that smaller $\sigma$ lowers $R_N\propto\sigma^{1/3}$ but the cell volume also shrinks: which dominates sets whether nuclei grow with depth.
7. **Geometry independence:** repeat the scaling argument for slabs ($E_C/V\propto R^2$) and rods to confirm $E_S=2E_C$ in each.
8. **Superfluid gap:** with $\Delta=1$ MeV and $T_c=0.567\Delta$ get $T_c=0.57$ MeV $=6.6\times10^9$ K; compare with crust temperatures $10^8$ to $10^9$ K: the dripped neutrons are superfluid throughout the star's life.
9. **Why near-unitarity:** at $k_F\approx0.8$ fm$^{-1}$ with $|a_s|=18.9$ fm, $k_F|a|\approx15\gg1$: the neutron gas is close to the unitary limit, which is why the gap is large (Module 07 exercise 9).
10. **Crust numbers:** the inner crust spans $4\times10^{11}$ to $\sim1.4\times10^{14}$ g/cm$^3$ ($n_B\sim2.6\times10^{-4}$ to $0.08$ fm$^{-3}$); the crust-core transition ($n\approx0.08$ fm$^{-3}$) is Module 20.

## Optional extension

Implement the CLDM at one density with SLy4 bulk energies and a simple $\sigma(\delta)$ ($\sigma_0=1.1$ MeV fm$^{-2}$) and scan $R_N$ to verify the minimum is at $E_S=2E_C$.

## Pitfalls

- Confusing the fissility relation ($E_C=2E_S$) with the cell optimum ($E_S=2E_C$).
- Forgetting surface contributions to the pressure balance.
- Using the isolated-nucleus Coulomb energy instead of the screened Wigner-Seitz expression.

## Gate questions

1. Why does drip occur at $\sim10^{-3}n_0$?
2. Why does the cell optimum have $E_S=2E_C$ in every geometry?
3. Why do nuclei grow with depth in the inner crust?

## One-page cheat sheet contents

Drip condition and numbers; cell energy terms; virial relation and the equilibrium radius; the fission comparison; superfluid gap and $T_c$.
