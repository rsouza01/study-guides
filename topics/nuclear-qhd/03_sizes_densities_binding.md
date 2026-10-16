# Module 03: Sizes, densities and binding (Week 1)

**Books:** Krane chapter 3 in full (fast: the empirical bedrock); Bertulani chapter 1 in parallel; skim Walecka chapter 1 section 1 to learn what his compression rate feels like.
**Time:** 1 week.

## Why this matters

$R\simeq1.2A^{1/3}$ fm means **the central density is independent of $A$**: nuclear matter saturates. The charge form factor $F(q)=\int\rho_{\rm ch}e^{i\mathbf q\cdot\mathbf r}d^3r$ is a Fourier transform, so electron scattering measures $\rho_{\rm ch}$ directly: Walecka's own research programme, and why he can assert saturation rather than assume it.

## Skip-test (40 minutes, no notes)

1. From $R=r_0A^{1/3}$ compute the central number density and convert to g/cm$^3$.
2. Compute the form factor of a uniform sphere and locate its first diffraction minimum.
3. Show that the Coulomb energy difference between mirror nuclei gives $r_0$.
4. State the two-parameter Fermi (Woods-Saxon) density and the 10-90 percent surface thickness.
5. State the empirical binding energy per nucleon curve: rises to a maximum near $A=56$ to $62$ ($\approx8.8$ MeV), roughly constant at $\approx8$ MeV above $A\sim12$.

## Prerequisites

Modules 01 and 02.

## Detailed topics (checklist)

**Sizes and densities [Must]**
- $R=r_0A^{1/3}$ with $r_0\approx1.1$ to $1.2$ fm; central density $n=\frac{3}{4\pi r_0^3}\approx0.14$ to $0.16$ fm$^{-3}$ independent of $A$; root-mean-square radius $\langle r^2\rangle^{1/2}=\sqrt{\tfrac35}R$ for a uniform sphere; the Woods-Saxon profile $\rho(r)=\frac{\rho_0}{1+e^{(r-R)/a}}$ with $a\approx0.55$ fm.

**Form factors [Must]**
- Born approximation for electrons: $\frac{d\sigma}{d\Omega}=\left(\frac{d\sigma}{d\Omega}\right)_{\rm Mott}|F(q)|^2$; uniform sphere $F(q)=\frac{3(\sin x-x\cos x)}{x^3}$, $x=qR$, first zero at $x=4.493$; surface diffuseness fills in the minima; the inversion problem.

**Binding [Must]**
- $B(A,Z)$ and the binding energy per nucleon; saturation of the strong force (the volume term dominates); nuclear matter as the $A\to\infty$ limit with no Coulomb force (Module 17).
- Coulomb energies and mirror nuclei: $E_C=\tfrac35\frac{e^2Z(Z-1)}{R}$ for a uniform sphere.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Krane 3.1 to 3.3 (sizes, densities, form factors) |
| Session 2 | Krane 3.4 to 3.6 (binding, mass measurement, abundances); Bertulani chapter 1 |
| Session 3 | Walecka chapter 1, section 1 (skim); exercises 1 to 5 |
| Session 4 | Exercises 6 to 10 |

## Derive from scratch

1. The central density from $r_0$ and its independence of $A$.
2. The uniform-sphere form factor.
3. The Coulomb energy of a uniform sphere.
4. The mirror-nuclei estimate of $r_0$.
5. The rms radius of a uniform sphere.

## Bare-minimum exercises (with expected results)

1. **Central density:** $n=\frac{3}{4\pi r_0^3}$ gives $0.138$ fm$^{-3}$ for $r_0=1.2$ fm and $0.161$ fm$^{-3}$ for $r_0=1.14$ fm; in mass density $2.7\times10^{14}$ g/cm$^3$ (using $1\ {\rm fm^{-3}}\leftrightarrow1.66\times10^{15}$ g/cm$^3$).
2. **Form factor:** $F(q)=\frac{3(\sin x-x\cos x)}{x^3}$ with first zero at $x=4.493$; for $^{208}$Pb ($R=7.1$ fm) the minimum is at $q\approx0.63$ fm$^{-1}$ ($\approx125$ MeV/$c$).
3. **Surface diffuseness:** the 10-90 percent thickness of a Woods-Saxon profile is $t=4a\ln3=4.39a\approx2.4$ fm for $a=0.55$ fm; comment on what this does to the diffraction minima (they become shallow, not zeros).
4. **Mirror nuclei:** $^{15}$O and $^{15}$N: the mass difference $2.754$ MeV plus the neutron-hydrogen mass difference $0.782$ MeV gives $\Delta E_C=3.54$ MeV; with $\Delta E_C=\tfrac35\frac{e^2}{R}\left[Z(Z-1)\right]$ difference $=\tfrac35\frac{e^2}{R}\times14$ one gets $R=3.42$ fm and $r_0=1.39$ fm (larger than the charge-density value because of Coulomb exchange and other corrections; comment).
5. **rms radius:** $\langle r^2\rangle^{1/2}=\sqrt{\tfrac35}R=0.775R$; for $A=16$, $R=1.2A^{1/3}=3.0$ fm gives $\langle r^2\rangle^{1/2}\approx2.3$ fm.
6. **Saturation:** the binding energy per nucleon is roughly constant ($\approx8$ MeV) for $A>12$; explain from the volume-proportional energy and short range of the force (each nucleon interacts only with its neighbours). Contrast with Coulomb ($B/A\propto A^{2/3}$ growth).
7. **Matter density from $n_0$:** $r_0=\left(\frac{3}{4\pi n_0}\right)^{1/3}=1.14$ fm for $n_0=0.16$ fm$^{-3}$; the spacing between nucleons is $\sim1.8$ fm.
8. **Potential depth estimate:** $E_F(n_0)=36.8$ MeV plus binding $B=16$ MeV gives a mean-field depth $V_0\approx52$ MeV (to be compared with the Woods-Saxon fits of Module 10).
9. **Neutron star scales:** $n_0=2.7\times10^{14}$ g/cm$^3$ is the density at the centre of a heavy nucleus *and* roughly the neutron-star core density at the crust-core boundary scale; state why this coincidence matters for the guide.
10. **Neutron skin (data):** the skin thickness $\Delta r_{np}=\langle r_n^2\rangle^{1/2}-\langle r_p^2\rangle^{1/2}$ of $^{208}$Pb is $\approx0.15$ to $0.3$ fm; PREX-II reports $0.283\pm0.071$ fm; keep this for Module 17.

## Optional extension

Compute the form factor of a Woods-Saxon density numerically for $A=208$, $a=0.55$ fm and compare with the uniform-sphere minimum position and the shape of the second maximum.

## Pitfalls

- Using $r_0$ from the charge radius where the matter radius is needed (a few percent difference).
- Forgetting that $\rho$ in nuclear physics is a number density.
- Treating the form-factor minimum as an exact zero for real nuclei.

## Gate questions

1. Why does a nearly constant central density imply saturation?
2. Why is the form factor a Fourier transform of the *charge* density?
3. What does $B/A\approx8$ MeV say about the range of the force?

## One-page cheat sheet contents

$R=r_0A^{1/3}$ and densities; uniform-sphere form factor and first zero; Woods-Saxon thickness; Coulomb energy; binding curve.
