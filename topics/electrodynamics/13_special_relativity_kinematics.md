# Module 13: Special relativity: postulates, Lorentz transformations, kinematics

**Books:** Jackson 11.1 (historical: fast), **11.2** (postulates and implications), **11.3** (Lorentz transformations and four-vectors), **11.4** (velocity addition, four-velocity), **11.5** (relativistic momentum and energy); Griffiths 12.1 to 12.2 (special relativity, relativistic mechanics: the problem-solving engine); Purcell chapter 5 (the fields of moving charges, with a clean relativity primer). **Units switch to Gaussian from Jackson Chapter 11 onward** (kinematics is unit-free; the dictionary is in the appendix).
**Time:** 2 weeks (four sessions).

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

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Griffiths 12.1; Jackson 11.1 to 11.2; derive the Lorentz transformation |
| B1 | Exercises 1 to 4 |
| A2 | Jackson 11.3 to 11.4; four-vectors and velocity addition |
| B2 | Exercises 5 and 6 |
| A3 | Griffiths 12.2; Jackson 11.5 |
| B3 | Exercises 7 to 9 |
| A4 | **Jackson targets** (exercise 10) |
| B4 | Spare session; Purcell chapter 5 |

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
