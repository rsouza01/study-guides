# Module MC-16: Why a direct run in a star fails

[← MC-15](MC-15-reemission-and-frequency-adjustment.md) · [README](../README.md) · [Next: MC-17 Opacity scaling →](MC-17-opacity-scaling.md)

**Source:** Forgan §8 (eqs 54–59), pp. 16–17, applied to the toy star of MC-09 to MC-13. Photon-diffusion time of the Sun: Mitalas & Sills (1992), ApJ 401, 759. Thermal time: Stix (2003), the lecture notes on the solar interior, and Kippenhahn et al. on the Kelvin–Helmholtz timescale.

---

## Session A: read

- Forgan §8 once more, with MC-08 open.
- Re-read MC-11 for the photon diffusion time.

**Key ideas**

- Forgan's code is built for dust discs, where $\tau\sim1$–$10^3$. A stellar interior has $\tau\sim10^{12}$. This is not a quantitative difference: it changes which algorithm is usable.
- Cost per packet: $N_{\rm steps}\sim N_{\rm sc}\sim\tau^2/2$ (MC-08). With $\tau=2.3\times10^{12}$ that is $2.7\times10^{24}$ steps per packet.
- Three different timescales appear and must not be confused:
  - the **free-flight time** $\ell/c$ (about $3\times10^{-10}$ s at the centre);
  - the **photon diffusion time** $\tau R/2c$ (order $10^4$–$10^5$ yr);
  - the **thermal (Kelvin–Helmholtz) time** $\sim GM^2/RL$ (about $3\times10^7$ yr).

**Derivation to see once: the three numbers for the toy star**

- Mean free path at the centre: $\ell=1/\kappa\rho$. With $\kappa_R=2.7$ cm² g⁻¹ and $\rho=76$ g cm⁻³ the toy star gives about $5\times10^{-3}$–$10^{-2}$ cm. Divide $R_\odot=6.96\times10^{10}$ cm: $R/\ell\sim10^{13}$.
- Optical depth: $\tau_{\rm tot}=\int\kappa\rho\,dr=2.3\times10^{12}$ for the toy profile (you compute it in Problem 1).
- Scatterings: $\tau^2/2+0.68\tau=2.7\times10^{24}$.
- At $10^8$ steps per second one packet takes $2.7\times10^{16}$ s, which is about $8.5\times10^{8}$ yr. You would need many packets. So the direct simulation cannot be run.
- Diffusion time: $\tau R/2c=\dfrac{2.3\times10^{12}\times6.96\times10^{10}}{2\times3\times10^{10}}\simeq2.7\times10^{12}$ s $\approx8\times10^4$ yr for uniform opacity, and $3.1\times10^4$ yr for the toy profile (opacity is higher where $r$ is small, but $r\,dr$ weights the outer layers).
- Thermal time: $GM_\odot^2/(R_\odot L_\odot)\approx3\times10^7$ yr. The luminosity of the Sun is **not** "the energy released in one diffusion time" from stored heat; the core is continuously resupplied by fusion, and the heat reservoir is regulated on the thermal time.

**The three ways out (and where each is used)**

- **Scale the opacity** so that $\tau\sim10^2$–$10^3$: steps fall as $\tau'^2$. Diffusion is scale-free, so the answer can be rescaled (MC-17).
- **Modified random walk**: replace thousands of tiny steps by one large jump inside a sphere of free movement (MC-18).
- **Use diffusion directly** in the deep interior and Monte Carlo only where $\tau\lesssim10$. This is the standard hybrid used in the capstone (MC-24).

---

## Session B: do

**Problem 1: the budget**

- Using the radiative-equilibrium temperature of MC-13, compute $\kappa_R\rho$ in each of 100 shells and:
  - the mean free path at the centre and at $0.5R$;
  - $\tau_{\rm tot}$;
  - $N_{\rm sc}=\tau^2/2+0.68\tau$;
  - the time one packet would take at $10^8$ steps per second.

**Problem 2: three timescales**

- Compute the free-flight time $\ell/c$ at the centre, the diffusion time $\langle t\rangle$ (MC-11), and the Kelvin–Helmholtz time $GM^2/RL$. Present them in a table in years or seconds.
- Explain why the neutrino-free photon flux seen today reflects fusion in the core now, not the stored energy delivered after a diffusion time.

**Problem 3: how much opacity can you cut?**

- If you divide $\kappa\rho$ by $S$, the number of steps goes as $(\tau/S)^2$. What value of $S$ gets the cost down to $\sim10^4$ steps per packet?

**Problem 4: does diffusion even apply?**

- The diffusion approximation requires $\tau\gg1$ over the length scale of the gradient. Compute $\tau_{\rm out}(r)=\int_r^R\kappa\rho\,dr'$ for each shell.
- In this toy star $\tau_{\rm out}$ stays above $10^4$ even at $0.99R$: 100 uniform shells do not resolve the real photosphere, which is a thin layer at the very top. State why that is a limitation of the toy.
- After dividing $\kappa\rho$ by $S$ so that $\tau'_{\rm tot}=300$, find the radius where $\tau'_{\rm out}$ drops below 10. This radius will matter in MC-17 and MC-20.

---

## Translation: text → code

| Forgan | Meaning | Code |
|---|---|---|
| eq (54) | $T\sim N_\gamma N_{\rm steps}$ | `cost = N * N_steps` |
| eq (57) | $N_{\rm sc}=3\tau^2$ | **use** `scatterings_estimate` instead |
| eq (59) | $T\sim N_\gamma\,\langle\tau\rangle R/dx$ | not applicable here |

---

## Contract

```text
starmc/budget.py
  optical_depth_radial(star, kappa_rho) -> tau_tot
  scatterings_estimate(tau) -> tau**2/2 + 0.68*tau
  direct_run_years(tau, steps_per_second=1e8) -> years per packet
```

```python
# acceptance-test
import numpy as np
from starmc.star import polytrope_star
from starmc.thermal import radiative_equilibrium_T
from starmc.opacity import kappa_rosseland
from starmc.budget import optical_depth_radial, scatterings_estimate, direct_run_years
from starmc import consts as C
assert abs(scatterings_estimate(10.0) - 56.8) < 1e-9
s = polytrope_star(n_shells=100)
T, L, conv, nab = radiative_equilibrium_T(s, convect=True)
kr = kappa_rosseland(s.rho, T, s.X, s.Z) * s.rho
tau = optical_depth_radial(s, kr)
assert 2.1e12 < tau < 2.5e12, tau
assert abs(1 / kr[0] - 0.00967) < 0.0005
n_sc = scatterings_estimate(tau)
assert 2.4e24 < n_sc < 2.9e24
assert 5e8 < direct_run_years(tau) < 1.2e9
tau_out = np.cumsum((kr * np.diff(s.r_edges))[::-1])[::-1]
assert tau_out[-1] > 1e3
i10 = np.where(tau_out * 300.0 / tau < 10)[0][0]
assert 0.4 < s.r_edges[i10] / C.Rsun < 0.6, s.r_edges[i10] / C.Rsun
print("MC-16 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| $\tau_{\rm tot}$ (toy star) | $2.30\times10^{12}$ |
| $\ell$ at the centre | 0.0097 cm |
| $N_{\rm sc}$ per packet | $2.7\times10^{24}$ |
| direct-run time per packet at $10^8$ steps s⁻¹ | about $8.5\times10^8$ yr |
| diffusion time, toy profile | about $3.1\times10^4$ yr |
| thermal time | about $3\times10^7$ yr |

---

## Done when

- You can give the three timescales, say what each measures, and say which one a luminosity measurement sees.
- You can explain why $\tau\sim10^{12}$ rules out a direct run without any appeal to computer speed.
- You can name the three strategies of the "ways out" and say which part of the star each applies to.
