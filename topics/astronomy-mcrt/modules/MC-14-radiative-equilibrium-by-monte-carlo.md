# Module MC-14: Radiative equilibrium by Monte Carlo

[← MC-13](MC-13-convection.md) · [README](../README.md) · [Next: MC-15 Re-emission and frequency adjustment →](MC-15-reemission-and-frequency-adjustment.md)

**Source:** Forgan §9.1 and §9.1.1 (eqs 60–69), pp. 17–19. Estimator: Lucy (1999), *Computing radiative equilibria with Monte Carlo techniques*, A&A 344, 282.

---

## Session A: read

- Forgan §9.1 (the idea) and §9.1.1 (eqs 60–69, the temperature of a cell).
- Lucy (1999), the introduction and the section on the path-length estimator of the absorbed energy.
- Re-read MC-11 (the diffusion temperature you want to reproduce) and PH-19 (the $\sigma T^4$ factor).

**Key ideas**

- In radiative equilibrium (RE) every cell **re-emits** what it absorbs (eq 60), so a cell's temperature is fixed by how many packets it absorbs.
- Forgan counts absorption events. Lucy's estimator counts **path length** instead. Same expectation, far smaller variance, because *every* packet passing through a cell contributes, not only the few absorbed.

**Derivation to see once: eqs 60–69, step by step**

- Absorbed: each packet carries $E_\gamma=L\Delta t/N_{\rm tot}$, so $E^{\rm abs}_i=N_iE_\gamma$ (eq 67).
- Emitted: $E^{\rm em}_i=4\pi\Delta t\int dV\!\int\rho\kappa_\nu B_\nu\,d\nu$ (eq 62). With the Planck mean $\kappa_P=\int\kappa_\nu B_\nu d\nu/\int B_\nu d\nu$ (eq 63) and $\int B_\nu d\nu=\sigma T^4/\pi$ (eq 64): $E^{\rm em}_i=4\pi\Delta t\,\kappa_PB\,m_i$ (eq 66, constant $\rho$ and $T$ in the cell).
- Equate (eq 60): $N_i\dfrac{L\Delta t}{N_{\rm tot}}=4\sigma T_i^4\kappa_Pm_i\Delta t$. So
$$\boxed{\sigma T_i^4=\frac{N_iL}{4N_{\rm tot}\kappa_P(T_i)\,m_i}}\qquad\text{(eq 69)}$$
- The right side contains $\kappa_P(T_i)$, so eq (69) is implicit, solved by iteration (Forgan notes $\kappa_P$ varies slowly).

**Derivation to see once: the path-length estimator**

- In a cell of volume $V$ with energy density $u$ and opacity $\kappa\rho$ per unit length, the absorbed power is $c\,u\,\kappa\rho\,V$ (every photon travels at $c$ and is absorbed at rate $\kappa\rho$ per unit length).
- A packet with path length $s_j$ inside the cell contributes $E_\gamma\kappa\rho\,s_j$ to the **expected** absorbed energy. Summing over packets: $E^{\rm abs}=E_\gamma\kappa\rho\sum_js_j$.
- The cell's own emission is $4\pi\kappa_P B\rho V=\kappa\rho\,c\,aT^4V$ (grey case, $4\pi B=c\,aT^4$). Equating gives
$$\boxed{\ u_i=aT_i^4=\frac{L}{N_{\rm tot}\,c\,V_i}\sum_js_{j,i}\ }$$
- $\kappa$ cancels. In the grey case the estimator needs no opacity at all, only path lengths. This is the estimator used from MC-17 on.

**Grey stellar interior: why no "re-emission" is needed**

- In the grey limit, absorbing and re-emitting a packet at the local temperature is equivalent to an isotropic **scattering**: the packet's energy is unchanged and its direction is forgotten. So the transport of MC-06 with albedo $a=1$ already conserves energy and gives the RE solution. The nuclear sources supply the energy; $L$ at the surface equals the sum of sources.
- Re-emission with frequency selection matters when you want a spectrum from the interior. That is MC-15.

---

## Session B: do

**Problem 1: eq (69)**

- Implement `temperature_from_absorbed(N_abs, L, N_tot, kappa_P, m_cell, sigma)`. Check $N_i=100$, $L=1$, $N_{\rm tot}=1000$, $\kappa_P=1$, $m_i=1$ in SI gives 25.77 K.

**Problem 2: the estimator**

- Implement `energy_density_from_paths(L, N_tot, path_shell, vol, c)` and `temperature_from_paths(...)`.

**Problem 3: a test with a known answer**

- Uniform sphere $R=1$, $\rho\kappa=\tau_0=30$, conservative scattering, $N=2\times10^4$ packets released at the centre ($L=1$, $c=1$).
- The diffusion solution with a point source, with an extrapolated boundary at $R+0.71\ell$ (MC-20 explains the $0.71$), is $u(r)=\dfrac{3\tau_0}{4\pi}\Big(\dfrac1r-\dfrac1{R+0.71\ell}\Big)$ in units $L/c$.
- Compare the Monte Carlo $u(r)$ from the shell path lengths with it for $r=0.1$–$0.9$. Expect a few percent.

**Problem 4: variance, absorption counting against path length**

- Repeat Problem 3 estimating $u$ from the count of **absorptions** (give the sphere albedo $0.9$ so that packets are actually absorbed). Compare the scatter between repeated runs with that of the path-length estimator at equal $N$.

---

## Translation: text → code

| Forgan | Meaning | Code |
|---|---|---|
| eq (60) | $E^{\rm abs}=E^{\rm em}$ | the equation you solve |
| eq (63) | $\kappa_P$ | MC-15 |
| eq (67) | $E_i^{\rm abs}=N_iE_\gamma$ | `N_i * L / N_tot` |
| eq (69) | $\sigma T_i^4=N_iL/4N_{\rm tot}\kappa_Pm_i$ | `temperature_from_absorbed` |
| — | Lucy path-length estimator | `energy_density_from_paths` |

---

## Contract

```text
starmc/radeq.py
  temperature_from_absorbed(N_abs, L, N_tot, kappa_P, m_cell, sigma=5.670374419e-8)
  energy_density_from_paths(L, N_tot, path_shell, vol, c=2.99792458e10)   = L*path/(N*c*V)
  temperature_from_paths(L, N_tot, path_shell, vol, a_rad=7.565733e-15, c=2.99792458e10)
```

```python
# acceptance-test
import numpy as np
from starmc.radeq import temperature_from_absorbed, energy_density_from_paths, temperature_from_paths
from starmc.transport import run_packets
assert abs(temperature_from_absorbed(100, 1.0, 1000, 1.0, 1.0) - 25.768) < 1e-3
assert np.isclose(energy_density_from_paths(2.0, 10, np.array([5.0]), np.array([4.0]), 1.0)[0], 0.25)
a, c = 7.565733e-15, 2.99792458e10
u = energy_density_from_paths(1.0, 1, np.array([1.0]), np.array([1.0]))[0]
assert np.isclose(temperature_from_paths(1.0, 1, np.array([1.0]), np.array([1.0]))[0], (u / a) ** 0.25)
rng = np.random.default_rng(4)
tau0, M, N = 30.0, 40, 12_000
edges = np.linspace(0.0, 1.0, M + 1)
vol = 4 * np.pi / 3 * np.diff(edges**3)
o = run_packets(rng, np.zeros(N), edges, np.full(M, tau0), 1.0)
u = energy_density_from_paths(1.0, N, o["path_shell"], vol, 1.0)
rm = 0.5 * (edges[1:] + edges[:-1])
uth = 3 * tau0 / (4 * np.pi) * (1 / rm - 1 / (1 + 0.71 / tau0))
for f in (0.2, 0.3, 0.5, 0.7):
    i = np.searchsorted(edges[1:], f)
    assert abs(u[i] / uth[i] - 1) < 0.06, (f, u[i] / uth[i])
print("MC-14 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| eq (69), SI test of Problem 1 | 25.77 K |
| $u_{\rm MC}/u_{\rm diff}$, $\tau_0=30$, $r=0.1,0.2,0.3,0.5,0.7,0.9$ | 0.996, 1.008, 1.002, 1.015, 1.010, 1.001 (for $N=2\times10^4$) |
| $\kappa$ in the grey path-length estimator | cancels |

---

## Done when

- You can derive eq (69) from eq (60) and then replace absorption counts by path length, and say why the second has lower variance.
- You can explain why grey RE needs no re-emission step in the transport.
- You can say what the extrapolation length $0.71\ell$ is correcting (the breakdown of diffusion near the surface).
