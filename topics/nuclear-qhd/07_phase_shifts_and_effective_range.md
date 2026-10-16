# Module 07: Phase shifts, scattering length and effective range (★, Week 6)

**Books:** Krane chapter 4 sections 4 to 6; **Walecka chapter 1** continued; Griffiths and your Module 01 page on the square well.
**Time:** 1 week.

## Why this matters

Memorise four numbers:
$$a_t=+5.42\ {\rm fm},\ r_t=1.75\ {\rm fm}\ (^3S_1);\qquad a_s=-23.7\ {\rm fm},\ r_s=2.7\ {\rm fm}\ (^1S_0).$$
The large negative $a_s$ means a **virtual state**: almost bound. That near-threshold accident controls low-energy neutron cross sections and, later, $^1S_0$ neutron superfluidity in the inner crust. The effective-range expansion $k\cot\delta_0=-\frac1a+\tfrac12r_0k^2+\cdots$ is the deep result: **low-energy scattering depends on two parameters regardless of the potential's shape**. Your first encounter with EFT logic, and the honest justification for using a model as simple as QHD.

## Skip-test (40 minutes, no notes)

1. Derive the effective-range expansion for a square well.
2. Relate $a_t$, $r_t$ to $B_d$ via $\gamma=\sqrt{MB}/\hbar c$.
3. Show that $a<0$ with $|a|$ large means a virtual state and locate its energy.
4. Compute the zero-energy $np$ cross-section from $a_t$ and $a_s$.
5. State the unitarity bound on a partial-wave cross-section.

## Prerequisites

Modules 01 and 06.

## Detailed topics (checklist)

**Effective-range theory [Must]**
- $k\cot\delta_0=-\frac1a+\tfrac12r_0k^2+O(k^4)$; for a square well $a=R\left(1-\frac{\tan k_0R}{k_0R}\right)$ and $r_0=R-\frac{R^3}{3a^2}-\frac{1}{k_0^2a}$; shape independence; the bound-state pole at $k=i\gamma$: $-\frac1a-\frac12r_0\gamma^2+\gamma=0$, so $\frac1a=\gamma-\tfrac12r_0\gamma^2+\dots$.
- **Virtual state:** a pole of the S-matrix at $k=-i\beta$ ($\beta>0$) on the negative imaginary axis, producing a large negative $a$ and an enhanced low-energy cross-section without a bound state.

**Experimental content [Must]**
- Singlet and triplet scattering lengths and ranges (above); the zero-energy $np$ cross-section $\sigma=\tfrac34\cdot4\pi a_t^2+\tfrac14\cdot4\pi a_s^2\approx20.4$ b (measured value $20.4$ b); phase shifts versus energy: $^1S_0$ rises to $\approx60^\circ$ near 25 MeV lab and changes sign near 250 MeV (the repulsive core); $^3S_1$ decreases through zero at a similar energy.
- Partial-wave unitarity $\sigma_\ell\le\frac{4\pi(2\ell+1)}{k^2}$ and the resonance picture.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Krane 4.4 to 4.6: scattering and the np data; exercise 1 |
| Session 2 | Effective range for the square well; exercises 2 and 3 |
| Session 3 | Walecka chapter 1 continued; exercises 4 to 6 |
| Session 4 | Exercises 7 to 10 |

## Derive from scratch

1. The square-well $s$-wave phase shift.
2. The effective-range expansion and the formulas for $a$ and $r_0$.
3. The bound-state relation $\frac1a=\gamma-\tfrac12r_0\gamma^2$.
4. The virtual-state pole.
5. The shape-independence argument (Bethe).

## Bare-minimum exercises (with expected results)

1. **Effective range for a square well:** derive $k\cot\delta_0$ and show $a=R\left(1-\frac{\tan k_0R}{k_0R}\right)$; verify shape independence by tuning a second shape (exponential or Gaussian well) to the same $a$ and comparing $r_0$.
2. **Deuteron from $a_t$, $r_t$:** $\frac1a=\gamma-\tfrac12r_t\gamma^2$ with $\gamma=0.2316$ fm$^{-1}$, $r_t=1.75$ fm gives $a=5.41$ fm, matching $5.42$ fm; check numerically.
3. **Virtual state:** for $a_s=-23.7$ fm, $r_s=2.7$ fm solve $\tfrac12r\beta^2+\beta+\frac1a=0$: $\beta\approx0.040$ fm$^{-1}$, energy $-\frac{\hbar^2\beta^2}{M}\approx-66$ keV.
4. **Zero-energy cross-sections:** $\sigma_t=4\pi a_t^2=3.69$ b, $\sigma_s=4\pi a_s^2=70.6$ b; the spin-averaged $\sigma=\tfrac34\sigma_t+\tfrac14\sigma_s\approx20.4$ b: the large $a_s$ dominates by a factor of five.
5. **Publishable paragraph:** explain why $a_s<0$ with $|a_s|$ large means "almost bound" rather than "repulsive".
6. **Scattering length sign conventions:** list the sign convention in Krane, Walecka and Griffiths; for $\delta_0=-ka$, $a>0$ repulsive core or bound state.
7. **Unitarity:** $\sigma_{\ell=0}^{\max}=\frac{4\pi}{k^2}$; for $E_{\rm lab}=1$ MeV ($k=0.22$ fm$^{-1}$) this exceeds the observed cross-section, as it must.
8. **Phase-shift sketch:** sketch $\delta(^1S_0)$ versus $E_{\rm lab}$ (attractive at low energy, sign change near 250 MeV) and say what each feature says about the force (attraction plus a hard or repulsive core).
9. **Neutron matter hook:** a large $|a_s|$ at the neutron Fermi momenta of the inner crust ($k_F\sim0.8$ fm$^{-1}$, $k_F|a|\gg1$) gives a strongly interacting, nearly unitary gas: the origin of a $\sim1$ MeV $^1S_0$ pairing gap (Module 19).
10. **EFT logic:** write two sentences on why low-energy observables need only $a$ and $r_0$ and how that justifies a simple Lagrangian (Module 21).

## Optional extension

Compute $^1S_0$ and $^3S_1$ phase shifts up to 200 MeV for a two-parameter Reid-like potential and compare with the Nijmegen partial-wave analysis; observe how the repulsive core fixes the sign change.

## Pitfalls

- Mixing the scattering-length sign convention.
- Expanding $k\cot\delta$ beyond its radius of convergence (set by the range or the pion mass).
- Reading $a_s<0$ as "repulsive".

## Gate questions

1. Why does low-energy scattering depend on only two parameters?
2. What does a virtual state look like in the S-matrix?
3. Why is $a_s$ so large and negative?

## One-page cheat sheet contents

ERE formula; square-well $a$ and $r_0$; four numbers; bound and virtual pole conditions; zero-energy cross-sections.
