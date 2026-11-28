# Module MC-19: The star engine

[← MC-18](MC-18-modified-random-walk.md) · [README](../README.md) · [Next: MC-20 A grey atmosphere →](MC-20-grey-atmosphere.md)

**Source:** assembles Forgan §2, §4.2.2, §4.3, §5.1 (MC-02 to MC-06), the path-length estimator of §9.1 (MC-14), the relocation rule of MC-13, the scaling of MC-17 and the jump of MC-18.

---

## Session A: read

- Re-read your own code for MC-05 (`distance_to_shell_boundary`), MC-06 (`run_packets`), MC-18 (`sample_exit_y`) and the "convection" section of MC-13.
- numba: the "5-minute guide" of the numba documentation, in particular `@njit(cache=True)` and why Python objects must stay out of the hot loop.

**Why a second transport code.** `run_packets` (MC-06) is vectorised numpy. It is clear, and fast enough for $\tau\lesssim10^3$ in a few seconds. Past that you want a compiled loop that follows **one packet at a time** with no array overhead: `numba` gives about $10^7$ steps per second, enough for $\tau'=300$ with $10^3$–$10^4$ packets.

**Design of one packet's walk (what the loop does)**

- State: radius $r$, radial cosine $\mu$, shell index, $\tau_{\rm left}$ (optical budget to the next interaction).
- At the start: if the shell is **convective**, relocate to the top of the convective block with $\mu=\sqrt\zeta$ (MC-03 Problem 4). If that is outside the star, done.
- Loop:
  - **Optional MRW jump** (only when a fresh interaction is needed): take $d=\min(r-r_{\rm in},r_{\rm out}-r)$, $R_0=\gamma d$. If $R_0\ge k_{\min}\ell$, jump: draw $y$ (MC-18), charge path $3R_0^2y/\ell$ to the current shell, move to a random point on the sphere, isotropise $\mu$, continue.
  - **Plain step**: draw $\tau_{\rm left}=-\ln(1-\zeta)$ if needed. Compute the distance to the shell boundary (MC-05) and $\tau_{\rm cell}=\rho\kappa\,s_b$.
    - If $\tau_{\rm left}\ge\tau_{\rm cell}$: cross the boundary, subtract, add $s_b$ to the shell's path length. If the new shell is convective, relocate to its top. If it is beyond the last shell, the packet escaped: return.
    - Otherwise: interact after $s=\tau_{\rm left}/\rho\kappa$, move, add $s$ to the path in this shell, draw an isotropic $\mu$ (albedo 1).
- Return: total path, steps, jumps, exit $\mu$, a `done` flag. Keep a per-shell array `path_shell` (summed over packets) for the estimator.

**What the engine does *not* do**

- It does not model absorption (albedo 1; see the grey argument in MC-14).
- It does not model frequency. It is a **grey** transport engine.
- Its $\mu_{\rm exit}$ and the flux at the outer shells are **not** the physical surface values (MC-17). The atmosphere module gives those.

---

## Session B: do

**Problem 1: write the engine**

- Implement `run_engine` with `numba.njit`. Pass shell edges, $\kappa\rho$ per shell, a boolean convective flag per shell, and the arrays of the MRW table. Seed the numba RNG inside the compiled function with `np.random.seed(seed)`.

**Problem 2: check against MC-06 and MC-14**

- Single uniform shell, $\tau=100$, packets from the centre, `use_mrw=False`. The mean path must be about $\tau/2+1$ (50 to 52). Compare with `run_packets` from MC-06 at equal $N$.

**Problem 3: MRW against plain steps**

- Same case with `use_mrw=True`. The mean path must agree within about 3 % and the number of plain steps must fall from $\sim5000$ to $\sim10$. Compare $\langle\mu_{\rm exit}\rangle$ and say which one is trustworthy.

**Problem 4: the scaled star with a convective core**

- Take the RE star of MC-13, distribute $10^3$–$3\times10^3$ packets with $\Delta L_i$ (MC-12), scale the opacity to $\tau'=300$ (MC-17), run with the convective flags, estimate $u'_i$ (MC-14), rescale with the boxed formula of MC-17 and compare $T_{\rm MC}$ with $T_{\rm RE}$ for $0.2$–$0.5R$.
- Verify that the path length in the convective core is exactly zero.

---

## Translation: text → code

| Step | Where it came from | Code |
|---|---|---|
| draw $\tau$ | MC-02 | `tau_rem = -np.log(1 - np.random.random())` |
| boundary distance | MC-05 | `_dist(r, mu, r_in, r_out)` |
| interaction point | Forgan eq (35) | `s = tau_rem / kr[i]` |
| new direction | MC-04 | `mu = 2*np.random.random() - 1` |
| relocation | MC-13 | `mu = np.sqrt(np.random.random())` |
| jump | MC-18 | `s = 3*R0*R0*y/ell` |

---

## Contract

```text
starmc/engine.py
  run_engine(r0, r_edges, kapparho, convective=None, gamma=0.95, kmin=2.0,
             use_mrw=True, seed=1, max_steps=10**9) -> dict
      r0         (n,) starting radii
      r_edges    (M+1,)
      kapparho   (M,) or scalar, per unit length
      convective (M,) bool or None
      returns:
        path (n,)  total path length per packet
        nstep (n,) plain steps    njump (n,) MRW jumps
        mu_exit (n,)   done (n,) bool
        path_shell (M,) path length summed over packets, per shell
```

```python
# acceptance-test
import numpy as np
from starmc.engine import run_engine
from starmc.star import polytrope_star
from starmc.thermal import radiative_equilibrium_T, luminosity_profile
from starmc.opacity import kappa_rosseland
from starmc.emission import sample_radius_from_shells
from starmc.budget import optical_depth_radial
from starmc.scaling import scale_factor, physical_energy_density
from starmc.radeq import energy_density_from_paths
from starmc import consts as C
E1 = np.array([0.0, 1.0])
N = 3000
a = run_engine(np.zeros(N), E1, np.array([100.0]), use_mrw=False, seed=1)
b = run_engine(np.zeros(N), E1, np.array([100.0]), use_mrw=True, seed=2)
assert a["done"].all() and b["done"].all()
assert 49.5 < a["path"].mean() < 53.0, a["path"].mean()
assert abs(b["path"].mean() / a["path"].mean() - 1) < 0.03
assert b["nstep"].mean() < a["nstep"].mean() / 100
assert 0.69 < np.nanmean(a["mu_exit"]) < 0.73
s = polytrope_star(n_shells=100)
T, L, conv, nab = radiative_equilibrium_T(s, convect=True)
kr = kappa_rosseland(s.rho, T, s.X, s.Z) * s.rho
tau = optical_depth_radial(s, kr)
S = scale_factor(tau, 300.0)
Lc, dL = luminosity_profile(s, T)
rng = np.random.default_rng(8)
Np = 3000
r0, _ = sample_radius_from_shells(rng, s.r_edges, dL, Np)
o = run_engine(r0, s.r_edges, kr / S, convective=conv, use_mrw=False, seed=5)
assert o["done"].all()
assert np.all(o["path_shell"][conv] == 0.0)
usc = energy_density_from_paths(C.Lsun, Np, o["path_shell"], s.vol)
uph = physical_energy_density(usc, S, C.a_rad * T[-1] ** 4)
Tm = (np.maximum(uph, 0.0) / C.a_rad) ** 0.25
for f in (0.2, 0.3, 0.4, 0.5):
    i = np.searchsorted(s.r_edges[1:] / C.Rsun, f)
    assert abs(Tm[i] / T[i] - 1) < 0.04, (f, Tm[i] / T[i])
print("MC-19 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| single shell, $\tau=100$: mean path, plain | about 51.2 |
| same, MRW | about 50.9 |
| plain steps per packet / MRW steps per packet | about 5100 / about 10 (plus 11 jumps) |
| $\langle\mu_{\rm exit}\rangle$ plain / MRW | 0.707 / 0.679 |
| scaled star, $T_{\rm MC}/T_{\rm RE}$ at $0.2,0.3,0.4,0.5R$ | 1.005, 1.007, 1.005, 1.015 |
| convective core ($15$ shells) path length | exactly 0 |

---

## Done when

- You can narrate the loop and say where each earlier module's code is called.
- You can explain why the relocation rule makes the core's path length zero and what temperature you then use there.
- You can say which outputs of the engine are trustworthy (time, $u$ in the deep interior) and which are not (exit angle, outer-shell flux).
