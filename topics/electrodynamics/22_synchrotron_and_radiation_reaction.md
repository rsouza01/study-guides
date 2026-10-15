# Module 22: Synchrotron radiation and radiation reaction

**Books:** Jackson **14.5** (frequency and angular distribution of the energy radiated by an accelerated charge), **14.6** (synchrotron radiation: this is the pulsar and magnetar emission mechanism, and the reason this module exists in your version of the plan and not in the first one), 16.1 to 16.3 (the Abraham-Lorentz force, the self-energy of a point charge, runaway solutions: *read, do not grind*). Afterwards: Rybicki and Lightman, *Radiative Processes in Astrophysics*, chapters 3 to 6 (picks up exactly where Jackson 14.6 stops). **Gaussian units.**
**Time:** 3 weeks (six sessions).

## Why this matters

Synchrotron radiation is the radiation of relativistic electrons gyrating in a magnetic field: pulsar wind nebulae, supernova remnants, magnetospheres of neutron stars. Section 16.2's **self-energy divergence** ($\propto1/a$ as the radius $a\to0$) is the original divergence, the one that motivated renormalization: meeting it in classical form makes the quantum version far less mysterious.

## Skip-test (40 minutes, no notes)

1. State the synchrotron critical frequency $\omega_c=\frac32\gamma^3\frac c\rho=\frac32\gamma^2\frac{eB}{mc}$ ($\nu_c\approx4.2\times10^6\gamma^2B_{\rm G}$ Hz) and the beaming cone half-angle $\sim\frac1\gamma$.
2. Derive the total power $P=\frac{2e^4B^2\gamma^2\beta^2}{3m^2c^3}=\frac43\sigma_Tc\gamma^2\beta^2U_B$ with $U_B=\frac{B^2}{8\pi}$, and the cooling time $t_{\rm cool}=\frac{\gamma mc^2}{P}\approx\frac{7.7\times10^8\,{\rm s}}{\gamma B_{\rm G}^2}$.
3. Sketch the single-particle spectrum: $\propto\omega^{1/3}$ for $\omega\ll\omega_c$, peak near $\omega_c$, $\propto\omega^{1/2}e^{-\omega/\omega_c}$ above; and for a power-law electron distribution $N(\gamma)\propto\gamma^{-p}$ the spectrum $P_\nu\propto\nu^{-(p-1)/2}$.
4. State the Abraham-Lorentz force $\mathbf F_{\rm rad}=\frac{2e^2}{3c^3}\dddot{\mathbf x}$, the characteristic time $\tau=\frac{2e^2}{3mc^3}\approx6.3\times10^{-24}$ s and the problems (runaway solutions, pre-acceleration).
5. Show the electrostatic self-energy of a charged shell $\frac{e^2}{2a}$ diverges as $a\to0$ and find the classical electron radius $r_e=\frac{e^2}{mc^2}=2.82\times10^{-13}$ cm by equating the energy to $mc^2$.

## Prerequisites

Modules 20 and 21 (LW fields, Larmor, beaming).

## Detailed topics (checklist)

**Frequency and angular distribution (14.5) [Must]**
- The radiated energy per unit solid angle per unit frequency, $\frac{d^2I}{d\omega\,d\Omega}=\frac{\omega^2}{4\pi^2c^3}\left|\int\hat{\mathbf n}\times(\hat{\mathbf n}\times\boldsymbol\beta)\,e^{i\omega(t'-\hat{\mathbf n}\cdot\mathbf r(t')/c)}dt'\right|^2\cdot q^2$ (Gaussian: $e^2$ replaces $q^2$); the idea: the observer sees a short pulse of duration $\Delta t\sim\frac{\rho}{c\gamma^3}$, so the spectrum extends to $\omega\sim\frac{1}{\Delta t}\sim\frac{\gamma^3c}{\rho}$.

**Synchrotron radiation (14.6) [Must]**
- Circular motion in a uniform magnetic field: $\rho=\frac{\gamma mc^2\beta}{eB}$; radiation confined to a cone of half-angle $\sim\frac1\gamma$ around the instantaneous velocity; polarization mostly in the orbital plane; critical frequency $\omega_c=\frac32\gamma^3\frac c\rho$; spectrum $\frac{dI}{d\omega}\propto F(\omega/\omega_c)$ with $F\sim\omega^{1/3}$ below and $\omega^{1/2}e^{-\omega/\omega_c}$ above (modified Bessel functions $K_{2/3},K_{1/3}$); the universal function $F(x)=x\int_x^\infty K_{5/3}(\xi)d\xi$ (Rybicki and Lightman).
- Power: $P=\frac{2e^2c}{3\rho^2}\beta^4\gamma^4$ (that is, $\frac{2e^2}{3c^3}\gamma^4a^2$ with $a=\frac{v^2}{\rho}$), i.e. $P=\frac{2e^4B^2\gamma^2\beta^2}{3m^2c^3}$; ratio to inverse-Compton scattering $\frac{P_{\rm sync}}{P_{\rm IC}}=\frac{U_B}{U_{\rm rad}}$.
- **Astrophysical mapping:** pulsar wind nebulae and supernova remnants: electrons with $N(\gamma)\propto\gamma^{-p}$ in $B\sim10^{-4}$ to $10^{-3}$ G give a power-law spectrum with index $\frac{p-1}{2}$; the **cooling break** where $t_{\rm cool}$ equals the age; in a neutron-star magnetosphere ($B\sim10^{12}$ G) particles lose perpendicular energy almost instantly to cyclotron/synchrotron emission; for magnetars ($B\sim10^{14}$ to $10^{15}$ G) the cyclotron energy $\hbar\omega_c=11.6\,{\rm keV}\,\frac{B}{10^{12}{\rm G}}$ approaches $mc^2$ at $B_Q=4.4\times10^{13}$ G, where the classical treatment fails.

**Radiation reaction (16.1 to 16.3) [Should]**
- Energy balance gives the Abraham-Lorentz force $\mathbf F_{\rm rad}=\frac{2e^2}{3c^3}\dddot{\mathbf x}$ and the equation $m(\ddot{\mathbf x}-\tau\dddot{\mathbf x})=\mathbf F_{\rm ext}$, $\tau=\frac{2e^2}{3mc^3}$; **runaway solutions** $a\propto e^{t/\tau}$ and, when excluded by the boundary condition at $t\to\infty$, **pre-acceleration** over a time $\tau$ (acausal); the relativistic generalization (Abraham-Lorentz-Dirac) and the Landau-Lifshitz reduction (awareness).
- **Self-energy (16.2):** the energy of a uniformly charged shell of radius $a$ is $\frac{e^2}{2a}$ (diverging as $a\to0$); the classical electron radius $r_e=\frac{e^2}{mc^2}$; the structure of a point charge as a problem of classical theory, solved only by renormalization in QED.

## Method card

**Synchrotron source estimate:** (1) from $\gamma$ and $B$ get $\rho=\frac{\gamma mc^2}{eB}$ and $\omega_c$; (2) power $P=\frac43\sigma_Tc\gamma^2U_B$; (3) cooling time $\frac{\gamma mc^2}{P}$ and compare with the source age; (4) for a power-law population, spectral index $\frac{p-1}{2}$ (and $\frac p2$ above the cooling break); (5) check against observed frequencies ($\nu_c=4.2\times10^6\gamma^2B_{\rm G}$ Hz).

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Jackson 14.5; the pulse-duration argument for $\omega_c$ |
| B1 | Exercises 1 to 3 |
| A2 | Jackson 14.6; spectrum shape and polarization |
| B2 | Exercises 4 and 5 |
| A3 | Astrophysical mapping; Rybicki and Lightman chapter 6 (optional) |
| B3 | Exercises 6 and 9 |
| A4 | Jackson 16.1 to 16.3 |
| B4 | Exercises 7 and 8 |
| A5 | **Jackson targets** (exercise 10); the computational task |
| B5 | The final blank-page gate |
| A6/B6 | Spare sessions |

## Derive from scratch

1. The critical frequency from the pulse duration $\Delta t\sim\frac{\rho}{c\gamma^3}$.
2. The total power $P=\frac43\sigma_Tc\gamma^2\beta^2U_B$.
3. The spectral index $\frac{p-1}{2}$ for a power-law electron distribution.
4. The Abraham-Lorentz force from energy balance.
5. The self-energy of a charged shell and $r_e$.

## Bare-minimum exercises (with expected results)

1. **Critical frequency:** for a 1 GeV electron ($\gamma\approx1957$) in $B=1$ T ($10^4$ G), $\nu_c=4.2\times10^6\gamma^2B_{\rm G}\approx1.6\times10^{17}$ Hz, i.e. $h\nu_c\approx0.66$ keV (soft X-rays); the orbit radius is $\rho\approx3.3$ m.
2. **Power:** for $\gamma=10^3$ and $B=1$ G, $U_B=\frac{B^2}{8\pi}=0.040$ erg/cm$^3$ and $P=\frac43\sigma_Tc\gamma^2U_B\approx1.1\times10^{-9}$ erg/s.
3. **Cooling time:** $t_{\rm cool}=\frac{3mc}{4\sigma_T\gamma U_B}\approx\frac{7.7\times10^8\,{\rm s}}{\gamma B_{\rm G}^2}$; for $\gamma=10^3$, $B=1$ G this is $7.7\times10^5$ s (about 9 days).
4. **Spectral index:** electrons with $N(\gamma)\propto\gamma^{-p}$ radiate $P_\nu\propto\nu^{-(p-1)/2}$ (use $\nu\propto\gamma^2$ and $P\propto\gamma^2$); $p=2.2$ gives $\alpha=0.6$ (typical of supernova remnants); above a cooling break the spectrum steepens by $\frac12$.
5. **Pulse duration:** the observer sees a pulse of duration $\Delta t\approx\frac{\rho}{2c\gamma^3}$ (the radiating arc $\rho/\gamma$ traversed at speed $c(1-\beta)$); hence $\omega_c\sim\frac{1}{\Delta t}\sim\frac{\gamma^3c}{\rho}$ (with the factor $\frac32$ from the exact calculation).
6. **Crab nebula:** with $B\approx3\times10^{-4}$ G, optical emission ($\nu=5\times10^{14}$ Hz) needs $\gamma\approx\sqrt{\frac{\nu}{4.2\times10^6B}}\approx6\times10^5$, with $t_{\rm cool}\approx\frac{7.7\times10^8}{\gamma B^2}\approx1.4\times10^{10}$ s ($\approx430$ yr), shorter than the age $\approx10^3$ yr: so electrons must be continuously re-accelerated.
7. **Abraham-Lorentz:** the equation $m\dot a=\frac{m}{\tau}\left(a-\frac{F}{m}\right)$ has the homogeneous solution $a\propto e^{t/\tau}$ (runaway); the physical solution $a(t)=\frac1\tau\int_t^\infty e^{(t-t')/\tau}\frac{F(t')}{m}dt'$ shows pre-acceleration over a time $\tau=6.3\times10^{-24}$ s (the time light takes to cross $\frac23r_e$).
8. **Self-energy and $r_e$:** a uniformly charged shell has $U=\frac{e^2}{2a}$ (sphere: $\frac{3e^2}{5a}$); setting $U=mc^2$ gives $a\sim r_e=\frac{e^2}{mc^2}=2.82\times10^{-13}$ cm $=\alpha\frac{\hbar}{mc}$: well inside the Compton wavelength, where classical electrodynamics ceases to apply.
9. **Magnetar scales:** the cyclotron energy $\hbar\omega_c=\frac{\hbar eB}{mc}=11.6$ keV$\times\frac{B}{10^{12}{\rm G}}$; at $B=10^{14}$ G it is $1.2$ MeV $\approx2mc^2$, in the regime where the classical formulas fail (the quantum critical field is $B_Q=\frac{m^2c^3}{e\hbar}=4.4\times10^{13}$ G).
10. **Jackson targets (about 14.12 and 16.1):** (a) the angular distribution of synchrotron radiation (exercises 1 and 5: beaming and polarization); (b) the radiation damping force (exercise 7).

## Blank-page gate: Month 5 (the final gate, items 3 to 7)

3. Derive the Larmor formula and its relativistic generalization.
4. Sketch the synchrotron spectrum: $\omega_c\sim\gamma^3c/\rho$, the $1/\gamma$ forward cone, and the power-law spectrum from a power-law electron distribution; state how this maps onto pulsar wind nebula emission.
5. Derive the Kramers-Kronig relations from causality plus contour integration.
6. Derive the Thomson cross-section.
7. Show the electrostatic self-energy of a uniformly charged sphere diverges as $a\to0$; obtain the classical electron radius by setting it equal to $mc^2$.

## Computational task (project): the Lienard-Wiechert synchrotron spectrum

Evaluate the LW fields numerically for a charge on a circular orbit at several $\gamma$; produce the angular power distribution; then FFT the field at a fixed observer to recover the synchrotron spectrum; verify the $\omega^{1/3}$ rise, the peak near $\omega_c$ and the exponential cutoff. Directly reusable for compact-object work.

## Pitfalls

- Using non-relativistic cyclotron frequency in the synchrotron formulas (the relevant frequency is $\gamma^3$-enhanced).
- Mixing the pitch angle: for pitch angle $\alpha$ replace $B\to B\sin\alpha$.
- Applying classical synchrotron theory when $\hbar\omega_c\gtrsim mc^2$ (magnetar fields).
- Treating the Abraham-Lorentz equation as a fundamental law (it has runaway solutions).

## Gate questions

1. Why does the characteristic frequency scale as $\gamma^3$ while the gyrofrequency scales as $1/\gamma$?
2. Why does a power-law electron distribution give a power-law spectrum, and what is the index?
3. Why does the self-energy divergence signal the breakdown of classical electrodynamics?

## One-page cheat sheet contents

$\omega_c$ and $\nu_c$ formula; power and cooling time; spectrum limits and spectral index; magnetar scales; Abraham-Lorentz force; $r_e$.
