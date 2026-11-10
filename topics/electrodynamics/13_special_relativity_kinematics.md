# Module 13: Special relativity: postulates, Lorentz transformations, kinematics

**Books:** Griffiths §12.1 (pp. 508 to 538) and §12.2 (pp. 538 to 553); Jackson 11.1 (p. 515), **11.2** (p. 518), **11.3** (p. 524), **11.4** (p. 530), **11.5** (p. 533); Purcell and Morin 3rd ed. §5.4 to §5.5 (pp. 241 to 247) and Appendix G, a short review of special relativity (p. 804). **Units switch to Gaussian from Jackson Chapter 11 onward** (kinematics is unit-free).
**Time:** 2 weeks (four sessions).
**Pinned to:** Griffiths 5th ed. (2024), Jackson 3rd ed. (1999), Purcell and Morin 3rd ed. (2013, SI), Riley, Hobson and Bence 3rd ed. Page numbers are the printed book pages.

## Why this matters

Chapters 1 to 7 are a covariant theory in a non-covariant costume. Special relativity is thread B: the Lorentz group, four-vectors, invariants, and (in Module 14) the algebra whose representations are the fields of the Standard Model. Kinematics problems are cheap and high-yield: invariant-mass arguments for thresholds, Doppler shifts and aberration from the four-vector $k^\mu$ come up again in radiation physics (Modules 20 to 22).

## Skip-test (40 minutes, no notes)

1. Derive the Lorentz transformation for a boost along $x$ from the two postulates alone: $x'=\gamma(x-\beta ct)$, $ct'=\gamma(ct-\beta x)$.
2. Derive time dilation, length contraction and velocity addition $u'=\frac{u-v}{1-uv/c^2}$.
3. Construct $u^\mu=\gamma(c,\mathbf v)$, $p^\mu=m u^\mu=(E/c,\mathbf p)$; show $p^\mu p_\mu=m^2c^2$ (so $E^2=p^2c^2+m^4c^4/c^2$ in standard form $E^2=p^2c^2+m^2c^4$).
4. Use the four-vector $k^\mu=(\omega/c,\mathbf k)$ to derive the Doppler formula $\omega'=\gamma\omega(1-\beta\cos\theta)$ and the aberration formula.
5. Find the threshold energy for $pp\to pp\,p\bar p$ on a fixed target using the invariant mass.

## Prerequisites

Module 01 (chain rule: why $\partial_\mu$ transforms with the inverse matrix); mechanics guide Module 13 (if you have it).

## Detailed topics (checklist)

**Postulates and Lorentz transformations (11.2 to 11.3) [Must]**
- The two postulates (the laws of physics are the same in all inertial frames; $c$ is the same); the invariant interval $s^2=c^2t^2-\mathbf x^2$; Lorentz transformation as the linear map preserving it; boost $\gamma=\frac{1}{\sqrt{1-\beta^2}}$; **rapidity** $\beta=\tanh\eta$ (boosts along one axis add rapidities); time dilation, length contraction, simultaneity (conceptual traps).
- Four-vectors: $x^\mu=(ct,\mathbf x)$, the transformation $x'^\mu=\Lambda^\mu{}_\nu x^\nu$, the invariant product $a\cdot b=a^0b^0-\mathbf a\cdot\mathbf b$ (signature $+---$).

**Velocity addition, four-velocity, momentum and energy (11.4 to 11.5) [Must]**
- $u'=\frac{u-v}{1-uv/c^2}$; $u^\mu=\gamma(c,\mathbf v)$, $u\cdot u=c^2$; $p^\mu=mu^\mu=(E/c,\mathbf p)$, $E=\gamma mc^2$, $\mathbf p=\gamma m\mathbf v$; the mass shell $p\cdot p=m^2c^2$.
- **Invariant mass and thresholds:** $s=(p_1+p_2)^2c^2$ is frame independent; threshold when all products are at rest in the CM frame.
- **Doppler and aberration:** photon four-vector $k^\mu$ ($k\cdot k=0$); $\omega'=\gamma(\omega-\beta ck_x)$, $\cos\theta'=\frac{\cos\theta-\beta}{1-\beta\cos\theta}$; relativistic beaming (the $1/\gamma$ cone appears in Module 22).

## Method card

**Relativity problem:** (1) define the frames and events; (2) write the four-vectors involved (position, momentum, wave vector); (3) use invariants and conservation of four-momentum *before* transforming anything; (4) transform only at the end, with one boost; (5) check the limits $\beta\to0$ (Newtonian) and $\beta\to1$.

## Reading plan (pinned to your editions)

A session is part A (read, derive) followed by part B (exercises), about two and a half hours in all. Page numbers are the printed ones.

| Session | A: read and derive | B: do | Done when |
| --- | --- | --- | --- |
| 1 | Griffiths §12.1 (pp. 508 to 538). Jackson 11.1 to 11.2 (pp. 515 to 524). Derive the Lorentz transformation. | Module exercises 1 to 4. Griffiths Problems 12.7, 12.8, 12.12, 12.14. | Lorentz transformation and velocity addition derived from the postulates. |
| 2 | Jackson 11.3 to 11.4 (pp. 524 to 533). Four-vectors and velocity addition. | Module exercises 5 and 6. Griffiths Problems 12.20, 12.21. Jackson Problem 11.3. | Interval invariance used without hesitation. |
| 3 | Griffiths §12.2 (pp. 538 to 553). Jackson 11.5 (pp. 533 to 536). | Module exercises 7 to 9. Griffiths Problems 12.26, 12.33, 12.34, 12.39. | $u\cdot u=c^2$ and $u\cdot a=0$ shown. |
| 4 | **Jackson targets.** | Jackson Problems 11.5 and 11.24 (threshold kinetic energy); Griffiths Problem 12.64. Spare; Purcell Appendix G. | Threshold energy found in the invariant-mass way. |

## Problem set (pinned)

**Pin status:** Pinned: sections and problems in Griffiths and Jackson (verified).

Tiers: **Must** (do all), **Should** (do when time allows), **Could** (only if the module is going well). A dash in the exercise column means the problem supports the reading rather than a module exercise. Purcell and Morin: stars give difficulty; problems are solved in Chapter 12 (the exercises are not).

| Book | Problem | What it asks | Module exercise | Tier |
| --- | --- | --- | --- | --- |
| Griffiths | 12.7 | muon lifetime in the laboratory | 1 | Must |
| Griffiths | 12.12 | solve the Lorentz transformation for x, y, z, t | 1 | Must |
| Griffiths | 12.20 | events A and B: invariant interval | 5 | Must |
| Griffiths | 12.26 | invariant product of the 4-velocity with itself | 9 | Must |
| Griffiths | 12.34 | pion decay | 7 | Must |
| Jackson | 11.5 | frame K' moving relative to K: transformation of a particle's motion | 10 | Must |
| Jackson | 11.24 | threshold kinetic energy of a reaction | 10 | Must |
| Griffiths | 12.8 | rocket ship | 1 | Should |
| Griffiths | 12.14 | velocity addition in the y direction | 6 | Should |
| Griffiths | 12.21 | coordinates of event A: spacelike or timelike | 5 | Should |
| Griffiths | 12.33 | collision of a particle of energy 2mc^2 with an identical particle at rest | 7 | Should |
| Griffiths | 12.39 | proper acceleration | 9 | Should |
| Griffiths | 12.64 | threshold momentum | 10 | Should |
| Jackson | 11.3 | successive Lorentz transformations in one direction | 5 | Should |

## Derive from scratch

1. The Lorentz transformation from the two postulates (the exit item of Month 4).
2. Velocity addition and the rapidity form.
3. $p\cdot p=m^2c^2$ and $E^2=p^2c^2+m^2c^4$.
4. The Doppler and aberration formulas from $k^\mu$.
5. The threshold for $pp\to pp\,p\bar p$.

## Bare-minimum exercises (with expected results)

1. **Muons:** a muon (rest lifetime $2.2\ \mu$s) at $v=0.99c$ has $\gamma=7.09$ and travels $\approx4.6$ km before decaying (versus $0.65$ km without dilation).
2. **Velocity addition:** $0.5c$ and $0.5c$ give $0.8c$; $0.99c$ and $0.99c$ give $0.99995c$; show the result can never exceed $c$ (use $\tanh(\eta_1+\eta_2)$).
3. **Doppler:** a source receding at $\beta$ along the line of sight has $\omega'=\omega\sqrt{\frac{1-\beta}{1+\beta}}$; the general result is $\omega'=\gamma\omega(1-\beta\cos\theta)$ with $\theta$ measured in the frame where the *source frequency* $\omega$ is defined; the transverse cases are $\omega_{\rm obs}=\gamma\omega_0$ for light emitted at $90^\circ$ in the source frame and $\omega_{\rm obs}=\omega_0/\gamma$ for light received at $90^\circ$ in the observer's frame.
4. **Aberration:** $\cos\theta'=\frac{\cos\theta-\beta}{1-\beta\cos\theta}$; at $\beta\to1$ almost all directions in the frame $S$ appear in a narrow forward cone in $S'$ of half-angle about $1/\gamma$ (you will use this in Module 22).
5. **Pion threshold:** $\gamma+p\to p+\pi^0$ on a stationary proton needs a photon energy $E_\gamma\ge m_\pi c^2\left(1+\frac{m_\pi}{2m_p}\right)\approx144.7$ MeV (with $m_\pi=134.98$ MeV, $m_p=938.27$ MeV).
6. **Proton-antiproton threshold:** $pp\to pp\,p\bar p$ on a fixed target has $T_{\rm th}=6m_pc^2\approx5.63$ GeV ($E_{\rm th}=7m_pc^2$); two equal head-on beams need only $\sqrt s=4m_pc^2$, i.e. $E=2m_pc^2$ per beam (kinetic energy $m_pc^2\approx0.94$ GeV each).
7. **Fixed-target equivalence:** a 13 TeV centre-of-mass energy $\sqrt s$ with a stationary target needs a beam energy $E=\frac{s}{2m_pc^2}\approx9\times10^7$ GeV.
8. **Two-body decay:** $\pi^+\to\mu^+\nu$ in the pion rest frame gives the muon $E_\mu=\frac{m_\pi^2+m_\mu^2}{2m_\pi}c^2\approx109.8$ MeV and $p_\mu c=\frac{m_\pi^2-m_\mu^2}{2m_\pi}c^2\approx29.8$ MeV (with $m_\pi=139.57$, $m_\mu=105.66$ MeV/$c^2$).
9. **Four-velocity:** $u\cdot u=c^2$ for any motion; the four-acceleration $a^\mu=\frac{du^\mu}{d\tau}$ satisfies $u\cdot a=0$; for $\mathbf v\parallel\mathbf a$ the proper acceleration is $\gamma^3a$.
10. **Jackson targets (about 11.3 and 11.5):** (a) Doppler and aberration derived from the transformation of the four-vector $k^\mu$ (exercises 3 and 4); (b) a threshold energy for particle production by the invariant-mass method (exercises 5 and 6). *Do two or three extra kinematics problems if you find them: they are cheap and high-yield.*

## Optional extension

Show that the longitudinal and transverse Doppler formulas agree with the general result and that for a receding source the observed frequency in the *observer's* frame at transverse emission angle (in that frame) is not the same as the source-frame $90^\circ$ result: this is a classic source of sign errors.

## Pitfalls

- Using the transformation matrix when an invariant would do.
- Treating "length contraction" and "time dilation" without specifying which frame measures which events.
- Mixing signatures $(+---)$ and $(-+++)$ between texts.
- Taking $\theta$ in $\omega'=\gamma\omega(1-\beta\cos\theta)$ in the wrong frame.

## Gate questions

1. Why can the invariant mass be computed in any frame?
2. How do rapidities simplify successive boosts?
3. Why is the photon four-vector null and what does that imply for $\omega'$?

## One-page cheat sheet contents

Lorentz transformation and rapidity; four-vectors and invariants; $p\cdot p=m^2c^2$; Doppler and aberration; thresholds.
