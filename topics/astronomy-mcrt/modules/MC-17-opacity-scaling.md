# Module MC-17: Opacity scaling, a similarity law for diffusion

[← MC-16](MC-16-why-direct-mcrt-fails.md) · [README](../README.md) · [Next: MC-18 The modified random walk →](MC-18-modified-random-walk.md)

**Source:** not in Forgan. Idea: in the diffusion limit the transport equation is scale-free in $\kappa\rho$ (MC-11). Compare with the same trick in dust codes (Min et al. 2009, A&A 497, 155, §2) and with the standard discussion of similarity in diffusion problems in Rybicki & Lightman, Ch. 1.

---

## Session A: read

- Re-read MC-11 (the diffusion equation) and MC-16 (the budget).
- Skim Min et al. (2009) for the modified random walk. It reappears in MC-18.

**Key ideas**

- In the diffusive regime the packets do not "know" the mean free path; only the optical depth $\tau$ of the whole body matters. Replace $\kappa\rho$ by $\kappa\rho/S$ everywhere, so $\tau'=\tau/S$, and the same random walk takes $S^2$ times fewer steps.
- What changes under the rescaling is determined by the diffusion equation itself:
  - **times and path lengths** scale by $S$;
  - **energy-density differences** scale by $S$;
  - the **surface boundary value** of $u$ does not scale. That is a property of the free-streaming layer, not of the diffusive interior.

**Derivation to see once: the three scalings**

- From MC-11, for a steady flux through radius $r$: $\partial_ru=-\dfrac{3\kappa\rho L}{4\pi cr^2}$ (with $u=aT^4$).
- Integrate from $r$ to the surface $R$: $u(r)-u_s=\dfrac{3L}{4\pi c}\displaystyle\int_r^R\dfrac{\kappa\rho}{r'^2}dr'$.
- Replace $\kappa\rho\to\kappa\rho/S$: the integral drops by $S$. So $u'(r)-u'_s=\big(u(r)-u_s\big)/S$. Inverting:
$$\boxed{\ u(r)=u_s+S\,\big[u'(r)-u'_s\big]\ }$$
- Time: $\langle t\rangle=\dfrac1c\!\int\kappa\rho\,r\,dr$ scales by $1/S$ for the scaled star, so $t=S\,t'$, where $t'=\text{(path length in scaled star)}/c$.
- The **surface value** $u_s$ is not rescaled: use the real value, from the atmosphere (MC-20) or the boundary temperature you imposed.

**Where the similarity breaks**

- In the **outer layers** the scaled $\tau'$ to the surface is small and diffusion no longer holds. For the toy star with $\tau'_{\rm tot}=300$ the scaled optical depth to the surface is 8.2 at $0.5R$, 2.6 at $0.6R$, 0.7 at $0.7R$ and 0.1 at $0.8R$.
- So validate only where $\tau'_{\rm out}\gtrsim10$. In practice that means $r\lesssim0.5R$ for $\tau'_{\rm tot}=300$. Outside, the real star is optically thick but the scaled star is not. In the capstone the outer layers are handed to the atmosphere module.
- The exit-angle distribution and the **flux at the surface** are also not preserved: the scaled star leaks more directly.

---

## Session B: do

**Problem 1: the time**

- Release $2\times10^3$ packets at the centre of the toy star (no convection, $T$ from `convect=False`) with $\kappa\rho/S$ and $\tau'_{\rm tot}=200$. Compute $\langle t\rangle=S\langle\text{path}\rangle/c$ in years. Compare with $\tfrac1c\int\kappa\rho\,r\,dr$ from MC-11.

**Problem 2: convergence in $\tau'$**

- Repeat for $\tau'_{\rm tot}=30,100,300,1000$. Tabulate the ratio to the diffusion time. It should approach 1 from above: the offset is the surface layer.

**Problem 3: the energy-density profile**

- Distribute the sources with $\Delta L_i$ (MC-12), run the scaled star ($\tau'=300$), estimate $u'_i$ with MC-14 and rescale with the boxed formula, using $u_s=aT_{\rm out}^4$ from the RE solution.
- Compare $T_{\rm MC}=(u/a)^{1/4}$ with the RE solution of MC-13 at $0.2$–$0.5R$.

**Problem 4: what goes wrong at $0.7R$?**

- Repeat Problem 3 and print the ratio $T_{\rm MC}/T_{\rm RE}$ out to $0.95R$. Explain the divergence with the numbers of the box above (scaled optical depth to the surface).

---

## Translation: text → code

| Quantity | Code |
|---|---|
| $S$ | `S = tau_tot / tau_target` |
| scaled opacity | `kr_scaled = kr / S` |
| time | `t = S * path / c` |
| energy density | `u = u_s + S*(u_scaled - u_scaled[-1])` |

---

## Contract

```text
starmc/scaling.py
  scale_factor(tau_tot, tau_target) -> S
  path_to_time(path, S) -> seconds, S * path / c
  physical_energy_density(u_scaled, S, u_surface) -> u_surface + S*(u_scaled - u_scaled[-1])
```

- The tests below use `transport.run_packets` from MC-06. They take a few seconds.

```python
# acceptance-test
import numpy as np
from starmc.star import polytrope_star
from starmc.thermal import radiative_equilibrium_T, diffusion_time_centre
from starmc.opacity import kappa_rosseland
from starmc.transport import run_packets
from starmc.scaling import scale_factor, path_to_time, physical_energy_density
from starmc.budget import optical_depth_radial
from starmc import consts as C
assert scale_factor(2.3e12, 300.0) == 2.3e12 / 300.0
assert np.isclose(path_to_time(np.array([C.c]), 10.0)[0], 10.0)
u = physical_energy_density(np.array([5.0, 3.0, 1.0]), 10.0, 2.0)
assert np.allclose(u, [42.0, 22.0, 2.0])
s = polytrope_star(n_shells=100)
T, L, conv, nab = radiative_equilibrium_T(s, convect=False)
kr = kappa_rosseland(s.rho, T, s.X, s.Z) * s.rho
tau = optical_depth_radial(s, kr)
S = scale_factor(tau, 200.0)
rng = np.random.default_rng(3)
o = run_packets(rng, np.zeros(2000), s.r_edges, kr / S, 1.0)
assert (o["state"] == 1).all()
t_mc = path_to_time(o["path"].mean(), S)
t_diff = diffusion_time_centre(s, kr)
assert abs(t_mc / t_diff - 1) < 0.08, t_mc / t_diff
print("MC-17 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| $\tau'_{\rm tot}=30,100,300,1000$: $t_{\rm MC}/t_{\rm diff}$ (centre release) | about 1.16, 1.04, 1.03, 1.00 |
| scaled $\tau'$ to the surface at $0.5R,0.6R,0.7R,0.8R$ ($\tau'_{\rm tot}=300$) | 8.2, 2.6, 0.66, 0.12 |
| $T_{\rm MC}/T_{\rm RE}$, no convection, $0.2$–$0.5R$ | within 0.5 % |
| $T_{\rm MC}/T_{\rm RE}$ at $0.6,0.7,0.8,0.9R$, run with the convective core | 1.04, 1.12, 1.34, 2.05 (do not trust) |

---

## Done when

- You can derive the three scalings and say which quantity does **not** scale and why.
- You can say where the similarity fails, and tell from $\tau'_{\rm out}$ where to stop trusting the scaled run.
- You can explain why the surface value of $u$ must come from somewhere else than the scaled run.
