# Module 14: Kinetic theory, local thermodynamic equilibrium and transport

**Books:** Mandl (kinetic theory, transport phenomena, the Boltzmann equation), Pathria (chapter 15: fluctuations and nonequilibrium statistical mechanics), Blundell and Blundell (kinetic theory, transport, mean free path), Schroeder (chapter 1 and the transport sections), Swendsen (kinetic basics).
**Time:** 2 weeks.

## Why this matters for stars and EOS

- Every EOS in a stellar model assumes **local thermodynamic equilibrium** (LTE): matter and radiation have a local temperature. This module explains *when* that holds (stellar interiors: extremely well) and when it fails (atmospheres, winds, low-density plasmas).
- **Radiative diffusion** (the dominant energy transport in most of a star) is a kinetic-theory result: a photon gas with a short mean free path behaves like a conducting fluid.
- **Electron conduction** in degenerate matter (white dwarfs, neutron-star crusts) uses the Wiedemann-Franz law.
- Transport coefficients and relaxation times control the **timescales** (thermal, diffusive, equilibration) that organize stellar evolution.

## Skip-test (40 minutes, no notes)

1. Estimate the mean free path $\ell=\frac{1}{n\sigma}$, and from kinetic theory the diffusion coefficient $D=\frac13\bar v\ell$, the viscosity $\eta=\frac13\rho\bar v\ell$ and the thermal conductivity $K=\frac13c_V^{(\rm vol)}\bar v\ell$.
2. Derive the radiative conductivity of a photon gas: $K_{\rm rad}=\frac13(4aT^3)c\,\ell=\frac{4acT^3}{3\kappa\rho}$ with $\ell=\frac{1}{\kappa\rho}$, hence the radiative flux $F=-\frac{4acT^3}{3\kappa\rho}\frac{dT}{dr}$.
3. State the Wiedemann-Franz law $\frac{K}{\sigma_eT}=\frac{\pi^2}{3}\frac{k^2}{e^2}$ and the conditions for it.
4. State what is meant by local thermodynamic equilibrium and give the condition in terms of timescales.
5. Write the Boltzmann equation $\frac{\partial f}{\partial t}+\vec v\cdot\nabla f+\vec F\cdot\frac{\partial f}{\partial\vec p}=\left(\frac{\partial f}{\partial t}\right)_{\rm coll}$ and its relaxation-time approximation $-\frac{f-f_0}{\tau}$.

## Prerequisites

Modules 07, 09, 11.

## Detailed topics (checklist)

**Kinetic theory**
- Free path, collision cross section, collision frequency; the Maxwell-Boltzmann averages $\bar v$, $v_{\rm rms}$; effusion; pressure from momentum transfer.
- Transport coefficients from simple kinetic arguments: diffusion, viscosity, thermal conductivity; their temperature and density dependence ($K,\eta\propto T^{1/2}$ and independent of density for a classical gas); the Knudsen number and the hydrodynamic limit.
- The Boltzmann equation, the collision integral, the H-theorem (statement), the relaxation-time approximation and how it yields conductivities; the Chapman-Enskog method (awareness).

**Radiation transport**
- Photon mean free path $\ell=\frac{1}{\kappa\rho}$ with the Rosseland mean opacity $\kappa$; the **diffusion approximation** for optical depth $\tau\gg1$: radiative conductivity, flux, energy density gradient; the radiative diffusion time $t\sim\frac{3\kappa\rho R^2}{\pi^2c}$ (order $R^2/\ell c$); the validity of the diffusion approximation and the breakdown near the surface (optically thin) where a transfer equation is needed.
- Radiative equilibrium; Kirchhoff's law $j_\nu=\kappa_\nu B_\nu$ in LTE.

**Conduction by degenerate electrons**
- Electrical and thermal conductivity of a degenerate electron gas in the relaxation-time approximation, $\sigma_e=\frac{ne^2\tau}{m^*}$, $K=\frac{\pi^2}{3}\frac{k^2T}{e^2}\sigma_e$ (Wiedemann-Franz, valid for elastic scattering); Matthiessen's rule $\tau^{-1}=\sum\tau_i^{-1}$; scattering by ions and by electrons; why conduction is efficient in degenerate cores but negligible in the ideal-gas interior of the Sun.

**Local thermodynamic equilibrium**
- Equilibrium versus LTE: a local temperature for particles, for radiation (Planck function), for excitation and ionization (Boltzmann and Saha with the *same* $T$); the condition that collisional rates exceed radiative rates and that gradients are small over a mean free path; NLTE (awareness): scattering-dominated lines and low-density atmospheres.
- **Equilibration times:** electron-electron collision time $\tau_e\approx3.44\times10^5\frac{T_{\rm eV}^{3/2}}{n\ln\Lambda}$ s (Spitzer; verify), ion-electron energy exchange slower by $m_i/m_e$, thermal and radiative diffusion times; the ordering of timescales in a star: collision $\ll$ dynamical $\ll$ thermal $\ll$ nuclear.

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Blundell and Blundell: kinetic theory, mean free path, transport |
| Lunch 2 | Mandl: transport phenomena, Boltzmann equation |
| Lunch 3 | Pathria chapter 15 (selected): nonequilibrium basics |
| Lunch 4 | A radiative-diffusion derivation from kinetic theory (derive it yourself) |
| Week 2 lunches | Wiedemann-Franz law (a solid-state or statistical-mechanics reference) and LTE discussion |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. Mean free path, diffusion coefficient, viscosity and thermal conductivity from simple kinetic theory.
2. The radiative conductivity $K_{\rm rad}=\frac{4acT^3}{3\kappa\rho}$.
3. The relaxation-time approximation to the Boltzmann equation giving $\sigma_e$.
4. The Wiedemann-Franz law from the relaxation-time conductivities.
5. A timescale argument for LTE in terms of $\ell\,|\nabla T|/T$.

## Bare-minimum exercises (find matching problems with keywords: mean free path, thermal conductivity, diffusion, Wiedemann-Franz, kinetic theory)

1. **Gas kinetics numbers:** mean free path and collision time of nitrogen at 1 atm and 300 K ($\ell\approx7\times10^{-6}$ cm, $\tau\sim10^{-10}$ s).
2. **Thermal conductivity independence of density:** show $K\propto\bar v\ell\,c_V^{(\rm vol)}\propto n^0$ for a classical gas.
3. **Photon mean free path in the Sun:** with $\kappa\sim1$ cm$^2$/g and $\rho=150$ g/cm$^3$ at the centre $\ell\approx7\times10^{-3}$ cm, and at the mean density $\ell\approx0.7$ cm; the temperature difference across one mean free path at the centre is $\Delta T\approx\ell|dT/dr|\approx10^{-6}$ K (with $|dT/dr|\sim2\times10^{-4}$ K/cm), i.e. a fractional difference $\sim10^{-13}$, so LTE is excellent.
4. **Radiative diffusion time:** $t_{\rm diff}\sim R^2/(\ell c)$ for the Sun with $\ell=0.01$ cm: $\sim5\times10^5$ yr; compare with the free-flight time $R/c=2.3$ s.
5. **Radiative conductivity:** evaluate $K_{\rm rad}=\frac{4acT^3}{3\kappa\rho}$ at the solar centre ($\kappa=1$): $\approx8\times10^{15}$ erg cm$^{-1}$ s$^{-1}$ K$^{-1}$, and check that $L=4\pi r^2K|dT/dr|$ at $r=0.1R_\odot$ is of order $10^{33}$ erg/s for a gradient of order $10^{-3}$ K/cm.
6. **Collision times:** compute the electron-electron collision time $\tau_e$ at the solar centre ($T=1.35$ keV, $n=6\times10^{25}$ cm$^{-3}$, $\ln\Lambda\approx3$): $\sim10^{-16}$ s; compare with the dynamical time $\sim30$ min.
7. **Wiedemann-Franz constant:** compute $\frac{\pi^2k^2}{3e^2}=2.44\times10^{-8}$ W $\Omega$ K$^{-2}$ in SI.
8. **Degenerate versus radiative conduction:** write the ratio $K_{\rm cond}/K_{\rm rad}$ in terms of $\sigma_e$ and $\kappa\rho$; state which dominates in a white dwarf core (conduction) and in the Sun's core (radiation).
9. **Knudsen number:** at what density does the hydrodynamic description fail for a gas confined to a box of size $L$? Apply to a stellar atmosphere with $\ell\sim R_{\rm atm}$.
10. **Relaxation time approximation:** derive the electrical conductivity $\sigma=\frac{ne^2\tau}{m}$ (Drude) and show how a velocity-dependent $\tau$ changes the Wiedemann-Franz ratio.

## Optional extension

Derive the radiative diffusion equation from the moments of the radiative transfer equation (Eddington approximation) and show how it connects to the kinetic-theory derivation above, including the factor $\frac13$.

## Pitfalls

- Using the diffusion approximation where the optical depth is not large.
- Applying the Wiedemann-Franz law to inelastic scattering (where it fails).
- Treating LTE as a property of the whole star rather than a local condition.
- Confusing the photon mean free path with the diffusion length.

## Gate questions

1. Why is thermal conductivity of a classical gas independent of density?
2. Why do photons in the stellar interior behave diffusively?
3. Under what conditions would LTE fail in a stellar atmosphere?

## One-page cheat sheet contents

Kinetic transport coefficients; $K_{\rm rad}$; diffusion time; Wiedemann-Franz law; LTE conditions and timescale ordering; collision-time formula.
