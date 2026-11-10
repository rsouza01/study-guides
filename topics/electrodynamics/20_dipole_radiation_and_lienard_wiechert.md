# Module 20: Dipole radiation and the Lienard-Wiechert potentials (★)

**Books:** Griffiths §11.1 Dipole radiation (pp. 472 to 487) and §10.3 Point charges: the Liénard-Wiechert potentials and fields (pp. 456 to 468); Jackson 9.1 (pp. 407 to 410), 9.2 (pp. 410 to 413), 9.3 (pp. 413 to 416), **14.1 Liénard-Wiechert potentials and fields (pp. 661 to 665)**; Purcell and Morin 3rd ed. §5.7 (pp. 251 to 255) and Appendix H, radiation by an accelerated charge (p. 812). **Skip** Jackson 9.6 to 9.8. Jackson Chapter 9 is **SI**; Chapter 14 is **Gaussian**. This corrects an earlier pointer: the Liénard-Wiechert potentials are in Griffiths 10.3, not chapter 11.
**Time:** 3 weeks (six sessions).
**Pinned to:** Griffiths 5th ed. (2024), Jackson 3rd ed. (1999), Purcell and Morin 3rd ed. (2013, SI), Riley, Hobson and Bence 3rd ed. Page numbers are the printed book pages.

## Why this matters

Section 14.1 is the payoff of Module 11. The retarded Green function applied to a delta-function source moving on a worldline gives the Lienard-Wiechert (LW) potentials. Be explicit about where the $(1-\boldsymbol\beta\cdot\hat{\mathbf n})^{-1}$ factor comes from: it is the $\delta(f(x))$ Jacobian rule from Module 02. **It is not a length contraction**, despite what half the internet says. Dipole radiation is the simplest radiating system and the entry to Chapter 14.

## Skip-test (40 minutes, no notes)

1. State the radiation-zone expansion of the retarded vector potential for a localized oscillating source: $\mathbf A\approx\frac{\mu_0}{4\pi}\frac{e^{ikr}}{r}\int\mathbf J(\mathbf x')e^{-ik\hat{\mathbf n}\cdot\mathbf x'}d^3x'$, valid for $r\gg d$ and $r\gg kd^2$.
2. For an oscillating electric dipole $\mathbf p\,e^{-i\omega t}$ give $\mathbf H=\frac{ck^2}{4\pi}(\hat{\mathbf n}\times\mathbf p)\frac{e^{ikr}}{r}$, $\mathbf E=Z_0\mathbf H\times\hat{\mathbf n}$, the angular distribution $\frac{dP}{d\Omega}\propto\sin^2\theta$ and the total power $P=\frac{c^2Z_0k^4|\mathbf p|^2}{12\pi}$ (SI; Gaussian $P=\frac{ck^4|\mathbf p|^2}{3}$).
3. Write the LW potentials $\Phi=\frac{q}{(1-\hat{\mathbf n}\cdot\boldsymbol\beta)R}\Big|_{\rm ret}$, $\mathbf A=\frac{q\boldsymbol\beta}{(1-\hat{\mathbf n}\cdot\boldsymbol\beta)R}\Big|_{\rm ret}$ (Gaussian) and derive the factor $(1-\hat{\mathbf n}\cdot\boldsymbol\beta)^{-1}$ from the retarded delta function.
4. State the LW fields: $\mathbf E=q\left[\frac{\hat{\mathbf n}-\boldsymbol\beta}{\gamma^2(1-\hat{\mathbf n}\cdot\boldsymbol\beta)^3R^2}\right]_{\rm ret}+\frac qc\left[\frac{\hat{\mathbf n}\times\left((\hat{\mathbf n}-\boldsymbol\beta)\times\dot{\boldsymbol\beta}\right)}{(1-\hat{\mathbf n}\cdot\boldsymbol\beta)^3R}\right]_{\rm ret}$, $\mathbf B=\hat{\mathbf n}\times\mathbf E$; identify the velocity field ($1/R^2$) and acceleration field ($1/R$).
5. Explain why only the acceleration field carries energy to infinity.

## Prerequisites

Modules 11 (retarded Green function), 15 (field of a moving charge), 18 (covariant Green function); Module 02 ($\delta(f(x))$).

## Detailed topics (checklist)

**Radiation from a localized source (9.1) [Must]**
- Harmonic sources $\mathbf J(\mathbf x)e^{-i\omega t}$; the three zones (near $r\ll\lambda$, intermediate, radiation $r\gg\lambda$); far-field form $\mathbf A\to\frac{\mu_0}{4\pi}\frac{e^{ikr}}{r}\int\mathbf J e^{-ik\hat{\mathbf n}\cdot\mathbf x'}d^3x'$; $\mathbf B=ik\hat{\mathbf n}\times\mathbf A$, $\mathbf E=cB\times\hat{\mathbf n}$-type; the long-wavelength multipole expansion in powers of $kd$: electric dipole, then magnetic dipole and electric quadrupole.

**Electric dipole radiation (9.2) [Must]**
- $\mathbf p=\int\mathbf x'\rho\,d^3x'$ related to $\int\mathbf J=-i\omega\mathbf p$; the fields in all zones (near field Coulomb-like, radiation $\propto1/r$); angular pattern $\sin^2\theta$; total power $\propto\omega^4|\mathbf p|^2$; the centre-fed linear antenna: $\frac{dP}{d\Omega}=\frac{Z_0I_0^2}{8\pi^2}\frac{\left[\cos\left(\frac{kd}{2}\cos\theta\right)-\cos\frac{kd}{2}\right]^2}{\sin^2\theta}$, half-wave pattern $\frac{\cos^2(\frac\pi2\cos\theta)}{\sin^2\theta}$, radiation resistance $\approx73\ \Omega$.

**Magnetic dipole and electric quadrupole radiation (9.3) [Should]**
- Magnetic dipole: same pattern with $\mathbf p\to\mathbf m/c$; electric quadrupole: $\propto k^6$ (suppressed by $(kd)^2$ relative to the dipole); selection-rule preview for atomic transitions.

**Lienard-Wiechert (14.1) [Must]**
- Retarded potentials of a point charge on a worldline $\mathbf z(t)$: $\rho=q\delta^3(\mathbf x-\mathbf z(t))$; the delta function $\delta\left(t'-t+\frac{R(t')}{c}\right)$ has the Jacobian $\left|\frac{d}{dt'}\left(t'+\frac{R(t')}{c}\right)\right|=1-\hat{\mathbf n}\cdot\boldsymbol\beta$ (this is the $(1-\hat{\mathbf n}\cdot\boldsymbol\beta)^{-1}$ factor); $\Phi=\frac{q}{(1-\hat{\mathbf n}\cdot\boldsymbol\beta)R}\Big|_{\rm ret}$, $\mathbf A=\boldsymbol\beta\Phi$; the covariant form $A^\alpha=\frac{qu^\alpha}{u\cdot(x-z)}\Big|_{\rm ret}$ (Module 18).
- The fields: **velocity field** $\propto\frac{1}{R^2}$ (the boosted Coulomb field, reduces to Module 15's pancake for uniform motion) and **acceleration (radiation) field** $\propto\frac{1}{R}\dot{\boldsymbol\beta}$; the Poynting flux of the velocity field falls as $R^{-4}$ and does not reach infinity; the acceleration field's flux falls as $R^{-2}$ and carries energy away.

## Method cards

**Dipole radiation problem:** (1) find $\mathbf p$ (or $\mathbf J$) of the source; (2) write the far-field $\mathbf A$ or use the dipole formulas; (3) get $\mathbf B$, $\mathbf E$ in the radiation zone; (4) compute $\frac{dP}{d\Omega}=\frac{r^2}{2\mu_0}\mathrm{Re}(\mathbf E\times\mathbf B^*)\cdot\hat{\mathbf n}$; (5) integrate for the total power and check $\omega^4$ scaling.
**LW derivation:** (1) write the retarded integral with the point-charge source; (2) integrate over $\mathbf x'$ with $\delta^3$, leaving a one-dimensional delta function in $t'$; (3) apply $\delta(f(t'))=\frac{\delta(t'-t_{\rm ret})}{|f'(t_{\rm ret})|}$ with $f'=1-\hat{\mathbf n}\cdot\boldsymbol\beta$; (4) take $-\nabla\Phi-\frac1c\partial_t\mathbf A$ with care for the dependence of $t_{\rm ret}$ on $\mathbf x$ and $t$.

## Reading plan (pinned to your editions)

A session is part A (read, derive) followed by part B (exercises), about two and a half hours in all. Page numbers are the printed ones.

| Session | A: read and derive | B: do | Done when |
| --- | --- | --- | --- |
| 1 | Griffiths §11.1 (pp. 472 to 487). Jackson 9.1 (pp. 407 to 410). The radiation-zone expansion. | Module exercises 1 and 4. Griffiths Problems 11.1, 11.2. | Radiation-zone fields of an oscillating dipole obtained. |
| 2 | Jackson 9.2 (pp. 410 to 413). Dipole pattern and power. | Module exercises 2 and 3. Griffiths Problems 11.4, 11.5. | $P=\frac{\mu_0p_0^2\omega^4}{12\pi c}$ reproduced. |
| 3 | Jackson 9.3 (skim). Griffiths §10.3 (pp. 456 to 468). | Module exercises 5 and 6. Griffiths Problems 10.17, 10.22. | LW potentials of a uniformly moving charge. |
| 4 | Jackson 14.1 (pp. 661 to 665). LW fields. | Module exercises 7 to 9. Jackson Problem 14.1. Griffiths Problem 10.23. | Velocity and acceleration fields separated. |
| 5 | **Jackson targets**; the computational task. | Jackson Problems 14.3 and 9.2. Optional: Griffiths Problem 10.16; Jackson 9.1. | Three routes, one field of a uniformly moving charge. |
| 6 (spare) | Spare. | Optional: Jackson Problems 9.3, 9.15. | — |

## Problem set (pinned)

**Pin status:** Pinned: sections and problems in all three books (verified).

Tiers: **Must** (do all), **Should** (do when time allows), **Could** (only if the module is going well). A dash in the exercise column means the problem supports the reading rather than a module exercise. Purcell and Morin: stars give difficulty; problems are solved in Chapter 12 (the exercises are not).

| Book | Problem | What it asks | Module exercise | Tier |
| --- | --- | --- | --- | --- |
| Griffiths | 11.4 | rotating electric dipole as two oscillating dipoles | 2 | Must |
| Griffiths | 10.22 | flux of E for a uniformly moving charge, from the LW fields | 5 | Must |
| Jackson | 14.1 | verify the LW expressions for the fields | 7 | Must |
| Jackson | 14.3 | Heaviside-Feynman expression for the field | 10 | Must |
| Jackson | 9.2 | radiating quadrupole | 10 | Must |
| Griffiths | 11.1 | retarded potentials of an oscillating dipole | 1 | Should |
| Griffiths | 11.2 | coordinate-free dipole radiation fields | 1 | Should |
| Griffiths | 11.5 | fields of an oscillating magnetic dipole | 2 | Should |
| Griffiths | 10.17 | scalar potential of a charge in uniform motion | 5 | Should |
| Griffiths | 10.23 | field of a moving infinite line charge from the LW fields | 7 | Should |
| Griffiths | 10.16 | charge on a circle: fields | 10 | Could |
| Jackson | 9.1 | a standard radiating system | 10 | Could |
| Jackson | 9.3 | two halves of a metallic shell | 10 | Could |

## Derive from scratch

1. The far-field $\mathbf A$ and the dipole fields.
2. The dipole power $P=\frac{c^2Z_0k^4|\mathbf p|^2}{12\pi}$ (SI).
3. The LW potentials with the Jacobian $(1-\hat{\mathbf n}\cdot\boldsymbol\beta)$.
4. The covariant form $A^\alpha=\frac{qu^\alpha}{u\cdot(x-z)}$.
5. The velocity/acceleration decomposition of $\mathbf E$.

## Bare-minimum exercises (with expected results)

1. **Dipole power (Gaussian):** for $\mathbf p(t)=p_0\hat{\mathbf z}\cos\omega t$, the Larmor-type instantaneous power $\frac{2\ddot p^2}{3c^3}$ averages to $P=\frac{\omega^4p_0^2}{3c^3}=\frac{ck^4p_0^2}{3}$; the pattern is $\frac{dP}{d\Omega}=\frac{ck^4p_0^2}{8\pi}\sin^2\theta$.
2. **Short antenna:** a Hertzian dipole of length $d\ll\lambda$ with uniform current $I_0$ has $p_0=\frac{I_0d}{\omega}$ and $R_{\rm rad}=\frac{2P}{I_0^2}=80\pi^2\left(\frac d\lambda\right)^2\ \Omega\approx790\left(\frac d\lambda\right)^2\Omega$ (for a triangular current distribution the factor is $\approx197$).
3. **Half-wave antenna (Jackson about 9.2):** pattern $\frac{\cos^2(\frac\pi2\cos\theta)}{\sin^2\theta}$, total radiated power $P=\frac12I_0^2R_{\rm rad}$ with $R_{\rm rad}\approx73.1\ \Omega$ and directivity $\approx1.64$.
4. **Polarization and nulls:** the radiated $\mathbf E$ lies in the plane containing $\mathbf p$ and $\hat{\mathbf n}$, along $\hat{\boldsymbol\theta}$; there is no radiation along the dipole axis; the angular momentum carried away is zero for a linear dipole.
5. **Frequency scaling:** the dipole power $\propto\omega^4$ explains the blue sky (Rayleigh scattering: scattered power $\propto\lambda^{-4}$, ratio $(700/450)^4\approx5.9$ between red and blue).
6. **The Jacobian:** show $\frac{d}{dt'}\left[t'+\frac{|\mathbf x-\mathbf z(t')|}{c}\right]=1-\hat{\mathbf n}\cdot\boldsymbol\beta$ with $\hat{\mathbf n}=\frac{\mathbf x-\mathbf z}{|\mathbf x-\mathbf z|}$, and use $\delta(f)=\frac{\delta(t'-t_{\rm ret})}{|f'|}$ to obtain $\Phi=\frac{q}{(1-\hat{\mathbf n}\cdot\boldsymbol\beta)R}\Big|_{\rm ret}$. It is a Jacobian, not a contraction.
7. **Three routes to one answer:** the velocity-field part of $\mathbf E$ for $\dot{\boldsymbol\beta}=0$ reproduces your Module 11 (retarded potentials) and Module 15 (boost) results: $\mathbf E=\frac{q(1-\beta^2)\mathbf R_{\rm pres}}{R_{\rm pres}^3(1-\beta^2\sin^2\psi)^{3/2}}$ with $\mathbf R_{\rm pres}$ the vector from the present position; check at $\beta\to0$ and at $\psi=90^\circ$ ($\gamma q/r^2$).
8. **Energy escape:** the Poynting flux of the velocity field falls as $\frac1{R^4}$ and of the acceleration field as $\frac1{R^2}$; only the latter integrates to a finite power at infinity.
9. **Non-relativistic limit:** for $\beta\ll1$ the acceleration field is $\mathbf E_{\rm rad}=\frac{q}{c^2R}\hat{\mathbf n}\times(\hat{\mathbf n}\times\mathbf a)$ and $\frac{dP}{d\Omega}=\frac{q^2a^2\sin^2\Theta}{4\pi c^3}$ with $\Theta$ the angle between $\hat{\mathbf n}$ and $\mathbf a$: this is the Larmor result of Module 21.
10. **Jackson targets (about 14.3 and 9.2):** (a) the fields of a charge at constant velocity from the LW formula; **compare against Module 11 and Module 15** (three routes, one answer); (b) the centre-fed antenna (exercise 3).

## Blank-page gate (Month 5, items 1 and 2)

1. Derive the Lienard-Wiechert potentials from the retarded Green function, explicit about the Jacobian factor.
2. Separate the LW field into velocity ($1/R^2$) and acceleration ($1/R$) pieces; explain why only the latter carries energy to infinity.

## Computational task (project, optional)

Evaluate the LW fields numerically for a charge on a circular orbit at several $\gamma$ (solve $t_{\rm ret}$ for the observer position and time); produce the angular power distribution and watch the dipole pattern collapse into the forward $1/\gamma$ cone. Then FFT the field at a fixed observer to recover the synchrotron spectrum (Module 22). This one is directly reusable for compact-object work.

## Pitfalls

- Calling the $(1-\hat{\mathbf n}\cdot\boldsymbol\beta)^{-1}$ factor a length contraction.
- Evaluating the LW fields at the present rather than the retarded time.
- Mixing SI (Chapter 9) and Gaussian (Chapter 14) formulas in one calculation.
- Applying the dipole approximation when $kd\gtrsim1$.

## Gate questions

1. Where does $(1-\hat{\mathbf n}\cdot\boldsymbol\beta)^{-1}$ come from?
2. Why does the dipole power scale as $\omega^4$?
3. Why does only the acceleration field carry energy to infinity?

## One-page cheat sheet contents

Dipole fields, pattern and power; antenna results; LW potentials and fields; velocity versus acceleration field; the Jacobian derivation.
