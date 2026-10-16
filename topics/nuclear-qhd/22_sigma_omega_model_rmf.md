# Module 22: The $\sigma$-$\omega$ model and relativistic mean-field theory (★★★, Week 21)

**Books:** Walecka's RMFT chapter; Serot and Walecka sections 2 to 3 in parallel.
**Time:** 1 week. **The second of the two modules that justify the guide.**

## Why this matters

$$\mathcal L=\bar\psi\left[\gamma^\mu(i\partial_\mu-g_vV_\mu)-(M-g_s\phi)\right]\psi+\tfrac12\left(\partial_\mu\phi\partial^\mu\phi-m_s^2\phi^2\right)-\tfrac14F_{\mu\nu}F^{\mu\nu}+\tfrac12m_v^2V_\mu V^\mu.$$
A Dirac field, a scalar Yukawa coupling (the Module 08 attraction), and a massive vector field of Proca form (the Module 08 repulsion). **You derived both static limits yourself in Module 08**: get that page out before starting.

Mean field: replace $\phi\to\phi_0$, $V_\mu\to\delta_{\mu0}V_0$. The nucleon equation becomes a **Dirac equation with $M^*=M-g_s\phi_0$**; the meson equations become
$$m_v^2V_0=g_vn_B,\qquad m_s^2\phi_0=g_sn_s,\qquad n_s=\frac{\gamma}{(2\pi)^3}\int^{k_F}\frac{M^*}{\sqrt{k^2+M^{*2}}}d^3k.$$

**Derive the saturation mechanism and be able to explain it in sixty seconds.** Vector repulsion goes like $n_B$, linearly, forever. Scalar attraction goes like $n_s$, which *saturates*, because growing $\phi_0$ shrinks $M^*$, suppressing $M^*/E^*$ in the integrand and feeding back to limit $\phi_0$. Attraction saturates, repulsion does not, so there is a minimum. **Saturation from relativity plus self-consistency, with no three-body force.** The most beautiful result in the book. Note the structure: the Module 13 Hartree-Fock loop again, with relativistic fields.

## Skip-test (40 minutes, no notes)

1. Derive the field equations via Euler-Lagrange; apply mean-field theory; obtain the three coupled equations.
2. Solve the self-consistency equation numerically at several densities and plot $M^*/M$ versus $n_B$.
3. Show the scalar source $n_s$ saturates as $M^*\to0$ and explain the mechanism to a colleague who does GR but no nuclear physics.
4. State why the two fields give a "difference of large numbers".
5. Write the nucleon dispersion relation in the medium.

## Prerequisites

Modules 08, 13, 17 and 21; Dirac equation and field Euler-Lagrange equations (mechanics guide Modules 17 to 18, Zettili guide Module 11).

## Detailed topics (checklist)

**The model and mean field [Must]**
- Euler-Lagrange: $(\Box+m_s^2)\phi=g_s\bar\psi\psi$, $\partial_\mu F^{\mu\nu}+m_v^2V^\nu=g_v\bar\psi\gamma^\nu\psi$, $\left[\gamma^\mu(i\partial_\mu-g_vV_\mu)-(M-g_s\phi)\right]\psi=0$; in mean field $\bar\psi\psi\to n_s$, $\psi^\dagger\psi\to n_B$; the Dirac equation with $E=g_vV_0+\sqrt{k^2+M^{*2}}$; $M^*=M-g_s\phi_0=M-\frac{g_s^2}{m_s^2}n_s(M^*)$ (the self-consistency); the nucleon spectrum $E(k)=V_0+\sqrt{k^2+M^{*2}}$.

**Saturation [Must]**
- $n_s<n_B$ and decreases relative to $n_B$ as $M^*$ falls; scalar attraction $\sim\frac{(M-M^*)^2}{2}$ saturates while vector repulsion $\frac{g_v^2}{2m_v^2}n_B^2$ grows quadratically in energy density: a minimum of $\frac{\varepsilon}{n_B}$ appears (Module 23).

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Walecka RMFT chapter: the Lagrangian and the field equations; exercises 1 and 2 |
| Session 2 | Serot-Walecka 2 to 3; the self-consistency; exercises 3 to 5 |
| Session 3 | The saturation mechanism; exercises 6 to 8 |
| Session 4 | Exercises 9 and 10; the sixty-second explanation |

## Derive from scratch

1. The Euler-Lagrange equations for $\psi$, $\phi$, $V_\mu$.
2. The mean-field reduction and the three equations.
3. The self-consistency equation for $M^*$.
4. The saturation of $n_s$.
5. The nucleon dispersion relation.

## Bare-minimum exercises (with expected results)

1. **Field equations:** derive the three Euler-Lagrange equations above and the mean-field versions $V_0=\frac{g_v}{m_v^2}n_B$, $\phi_0=\frac{g_s}{m_s^2}n_s$.
2. **Self-consistent $M^*$ (numerical):** with $C_s^2=\frac{g_s^2M^2}{m_s^2}=267.1$, $C_v^2=\frac{g_v^2M^2}{m_v^2}=195.9$ ($M=939$ MeV, symmetric matter $\gamma=4$) solve $M^*=M-\frac{C_s^2}{M^2}n_s(M^*)$: $\frac{M^*}{M}=0.88,0.76,0.56,0.29,0.16,0.10,0.06$ at $n_B=0.05,0.1,0.193,0.4,0.8,1.6,3.2$ fm$^{-3}$ (the saturation density of the standard fit, $k_F=1.42$ fm$^{-1}$, is $0.193$; roadmap values of $0.54$ come from slightly different inputs: state yours).
3. **Saturation of the scalar source:** $\frac{n_s}{n_B}=0.99,0.97,0.93,0.72,0.42,0.23,0.12$ at the same densities; the scalar potential $S=M^*-M=-115,-226,-416,-667,-790,-848,-882$ MeV tends to $-M$ while the vector potential $V_0=\frac{C_v^2}{M^2}n_B\hbar c=85,171,330,683,1366,2731,5463$ MeV grows linearly: this *is* the saturation mechanism (and why a causal EOS follows).
4. **Sixty-second explanation (write it):** the scalar field screens its own source because it makes the nucleon lighter and thus lowers $\bar\psi\psi$; the vector field has no such feedback because $\psi^\dagger\psi=n_B$ is conserved.
5. **Difference of large numbers:** at $n_B=0.193$ fm$^{-3}$, $V_0\approx330$ and $S\approx-416$ MeV, so $V_0+S\approx-86$ MeV (the central potential, before kinetic energy) while the net binding is $-16$ MeV.
6. **Dispersion relation:** $E(k)=V_0+\sqrt{k^2+M^{*2}}$; at the Fermi surface $E_F=V_0+\sqrt{k_F^2+M^{*2}}=\mu_B$; check that $\mu_B=\frac{\varepsilon+P}{n_B}$ at saturation ($=M-B_0=923$ MeV).
7. **Why only two combinations:** $g_s^2/m_s^2$ and $g_v^2/m_v^2$ appear in the equations for the *uniform* system; the meson masses separately matter only for finite nuclei (range).
8. **Compare with Module 13:** list the parallels between this self-consistency loop and the Skyrme HF loop (guess $\to$ build field $\to$ solve $\to$ rebuild $\to$ iterate).
9. **Weak coupling check:** at low density $M^*\to M$ and $V_0\to0$; recover the free Fermi gas.
10. **Large-$n_B$ limit:** $M^*\to0$, $n_s\to0$, $S\to-M$ while $V_0\to\infty$: preview of the causal EOS $P\to\varepsilon$ (Module 23).

## Optional extension

Solve for $M^*$ using Newton's method with the derivative $\frac{dn_s}{dM^*}$ computed analytically and show quadratic convergence; plot the effective potential as a function of $\phi_0$ at several $n_B$ to see the minimum move.

## Pitfalls

- Confusing $n_s$ ($\bar\psi\psi$) with $n_B$ ($\psi^\dagger\psi$).
- Dropping the self-consistency by using $M^*=M$ in the scalar density.
- Using the wrong sign for the vector potential in the dispersion relation.

## Gate questions

1. Why does $n_s$ saturate while $n_B$ does not?
2. Why does saturation need no three-body force?
3. Why do only two coupling combinations appear?

## One-page cheat sheet contents

The Lagrangian; mean-field equations; self-consistency; the density table of $M^*$, $S$, $V_0$; the sixty-second explanation.
