# Module MC-13: Convection and the Schwarzschild criterion

[← MC-12](MC-12-nuclear-energy-sources.md) · [README](../README.md) · [Next: MC-14 Radiative equilibrium by Monte Carlo →](MC-14-radiative-equilibrium-by-monte-carlo.md)

**Source:** not in Forgan, which treats radiative transport only. Background: Kippenhahn, Weigert & Weiss, the sections on the Schwarzschild criterion and on convective energy transport; Carroll & Ostlie, the section on energy transport in the stellar-interiors chapter; Hansen, Kawaler & Trimble, the chapter on convection.

---

## Session A: read

- One of the references above on $\nabla_{\rm rad}$, $\nabla_{\rm ad}$ and the Schwarzschild criterion.
- Re-read MC-11 for the radiative gradient.

**Key ideas**

- Radiative diffusion needs a steep temperature gradient to carry the flux. When that gradient exceeds the **adiabatic** gradient, a displaced blob keeps rising: the layer is unstable, and **convection** carries the flux.
- With $\nabla\equiv\partial\ln T/\partial\ln P$, the criterion is $\nabla_{\rm rad}>\nabla_{\rm ad}$ (Schwarzschild).
- Convection is very efficient in a stellar interior. To first order a convective zone is **well mixed**: nearly adiabatic, nearly uniform in composition and entropy.

**Derivation to see once: $\nabla_{\rm rad}$**

- Radiative diffusion (MC-11): $\partial_r(aT^4/3)=-\kappa\rho L/(4\pi r^2c)$.
- Hydrostatic equilibrium: $\partial_rP=-Gm\rho/r^2$.
- Divide: $\dfrac{a}{3}\dfrac{d(T^4)}{dP}=\dfrac{\kappa L}{4\pi cGm}$, so $\dfrac{dT^4}{dP}=\dfrac{3\kappa L}{4\pi acGm}$.
- Then $\nabla_{\rm rad}=\dfrac{P}{T}\dfrac{dT}{dP}=\dfrac{P}{4T^4}\dfrac{dT^4}{dP}=\boxed{\dfrac{3\kappa LP}{16\pi acGmT^4}}$.

**Derivation to see once: $\nabla_{\rm ad}=0.4$**

- A monatomic ideal gas has $\Gamma_2=5/3$: an adiabatic change obeys $P\propto\rho^{5/3}$. The ideal-gas law gives $\rho\propto P/T$.
- Combine: $P\propto(P/T)^{5/3}$, so $P^{-2/3}\propto T^{-5/3}$, that is $T\propto P^{2/5}$.
- So $\nabla_{\rm ad}=2/5=0.4$, and also $T\propto\rho^{2/3}$ along the adiabat (used in the code).
- With radiation pressure $\nabla_{\rm ad}$ is smaller (down to 0.25 when radiation pressure dominates); the guide ignores that.

**How the Monte Carlo handles a convective zone**

- Radiative packets move by random walk. In a convective zone the real energy flux is carried by gas motion, not by photons, and the temperature is set by the adiabat.
- Prescription used here: **a packet entering a convective zone is relocated to the zone top** (outer edge) with a Lambert-distributed direction (MC-03, Problem 4), instead of being followed through the zone. This respects the physical statement that convection transports energy outward efficiently, and costs nothing.
- Consequence: the energy-density estimator of MC-14 is **zero** in the convective zone (no packets walk there). Its temperature must come from the adiabat, as in the ODE solver.

---

## Session B: do

**Problem 1: $\nabla_{\rm rad}$**

- Implement `nabla_rad(kappa, L, P, m, T)`. Check it against the closed form for $\kappa=1$, $L=L_\odot$, $P=10^{17}$, $m=0.1M_\odot$, $T=1.5\times10^7$.

**Problem 2: convective blocks**

- Implement `convective_blocks(flags)` returning the list of `(i_lo, i_hi)` shell ranges (hi exclusive) where `flags` is true. Test on `[1,1,0,0,1,0,1,1,1]`.

**Problem 3: the solver with convection**

- Extend MC-11's solver (`radiative_equilibrium_T`). At each iteration, after the inward integration:
  - compute $\nabla_{\rm rad}$ at every shell with the current $T$, $L$, $P$ (use `pressure` and the mass at shell mid-points);
  - mark shells with $\nabla_{\rm rad}>0.4$ as convective;
  - for every convective block anchor $T$ at the outermost shell of the block (the radiative value) and set $T=T_{\rm anchor}(\rho/\rho_{\rm anchor})^{2/3}$ inward;
  - relax: `T = 0.5*T_new + 0.5*T_old`; stop when the largest relative change is below $10^{-6}$.
- Report the number of convective shells and the radius of the core's edge.

**Problem 4: check the physics**

- Run with `convect=False` and compare. How does $T_c$ change? Why is the core convective in the toy star? (Hint: look at how $\nabla_{\rm rad}$ depends on $\epsilon$ through $L$ and on $\kappa$.)
- The toy Sun's **envelope** stays radiative. The real Sun has a convective envelope, which this toy opacity and polytropic density do not reproduce. A star of about $1.5\,M_\odot$ really has a convective core and a radiative envelope. Note which of the two is the toy artefact.

---

## Translation: text → code

| Quantity | Code |
|---|---|
| $\nabla_{\rm rad}$ | `3*kap*L*P/(16*pi*a_rad*c*G*m*T**4)` |
| criterion | `conv = nab > 0.4` |
| adiabat | `T[q] = anchor * (rho[q]/rho[i])**(2/3)` |
| relocation rule | in the transport engine, MC-19 |

---

## Contract

```text
starmc/convection.py
  nabla_rad(kappa, L, P, m, T)
  convective_blocks(flags) -> [(i_lo, i_hi), ...]   hi exclusive
starmc/thermal.py
  radiative_equilibrium_T(star, T_surface=5772.0, t_guill=10.0, n_iter=60,
                          convect=True, grad_ad=0.4, relax=0.5)
      -> (T, L, conv, nabla_rad)
         T     (n,) shell temperatures
         L     (n,) luminosity at the outer edge of each shell
         conv  (n,) bool, convective flags
         nabla_rad (n,)
  Details: the luminosity profile comes from luminosity_profile(star, T) at every
  iteration; L at the shell centre is L_outer - dL/2; kappa from kappa_rosseland;
  pressure from pressure(rho, T, mu); mass at the shell centre m_outer - dm/2.
```

```python
# acceptance-test
import numpy as np
from starmc.star import polytrope_star
from starmc.thermal import radiative_equilibrium_T
from starmc.convection import nabla_rad, convective_blocks
from starmc import consts as C
expect = 3 * 1.0 * C.Lsun * 1e17 / (16 * np.pi * C.a_rad * C.c * C.G * 0.1 * C.Msun * (1.5e7) ** 4)
assert abs(nabla_rad(1.0, C.Lsun, 1e17, 0.1 * C.Msun, 1.5e7) / expect - 1) < 1e-12
assert convective_blocks(np.array([1, 1, 0, 0, 1, 0, 1, 1, 1], bool)) == [(0, 2), (4, 5), (6, 9)]
s = polytrope_star(n_shells=100)
T, L, conv, nab = radiative_equilibrium_T(s, convect=True)
assert 12 <= conv.sum() <= 18, conv.sum()
assert conv[: conv.sum()].all(), "convective zone must be a core"
assert abs(T[0] / 1.58e7 - 1) < 0.05, T[0]
assert abs(L[-1] / C.Lsun - 1) < 1e-6 and np.all(np.diff(L) >= 0)
assert abs(nab[0] - 0.502) < 0.02, nab[0]
assert nab[30] < 0.4
T2, L2, conv2, nab2 = radiative_equilibrium_T(s, convect=False)
assert abs(T2[0] / 1.47e7 - 1) < 0.05, T2[0]
assert nab2.max() > 0.4
print("MC-13 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| $\nabla_{\rm rad}$ for the closed-form test | 0.1499 |
| convective shells (100 uniform shells) | about 15 (core to $r\simeq0.15R$) |
| $T_c$ with convection | $1.58\times10^7$ K |
| $T_c$ radiative only | $1.47\times10^7$ K |
| $\nabla_{\rm rad}$ at the centre, radiative only | 0.499 (above 0.4, so the core is unstable) |
| $\nabla_{\rm rad}$ at $0.3R$ | 0.28 |

---

## Done when

- You can derive $\nabla_{\rm rad}$ and $\nabla_{\rm ad}=0.4$ and say which physical quantities set whether a layer is convective.
- You can say why the packet-relocation prescription is physically reasonable and what it leaves unmodelled.
- You can name which features of the toy star (core convection, radiative envelope) are artefacts of its simplifications.
