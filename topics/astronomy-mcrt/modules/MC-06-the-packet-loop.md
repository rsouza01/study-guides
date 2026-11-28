# Module MC-06: The packet loop

[← MC-05](MC-05-rays-grids-and-shells.md) · [README](../README.md) · [Next: MC-07 Outputs and flux →](MC-07-outputs-images-and-flux.md)

**Source:** Forgan, §2 (the algorithm outline, p. 6), §4.3 (eq 35) and §5 (scattering), assembled with MC-02 to MC-05.

---

## Session A: read

- Forgan §2, the paragraph that lists the steps of a photon's life; §4.3; §5.1.
- Re-read your own MC-03, MC-04 and MC-05 code. This module writes no new physics, only the loop that joins them.

**Key ideas**

- One packet's life is a loop:
  - sample $\tau$ to the next interaction (MC-02);
  - walk it across shells, subtracting each $\tau_{\rm cell}$ from what is left (MC-05);
  - if the budget runs out inside a shell, move to the interaction point (eq 35);
  - draw absorb or scatter (MC-04); on scatter draw a new direction and a new $\tau$;
  - stop when the packet leaves the outer shell (escaped) or is absorbed.
- **Vectorise over packets**, not over steps: keep arrays `r, mu, shell, tau_left, state` and update the subset still active each iteration. Python loops over single packets are about 1000× too slow.
- Record, per packet: number of scatterings, total path length, exit direction. Record, per shell: the **summed path length**. The last one is the estimator used in MC-14.

**Derivation to see once: why the shell-by-shell budget is exact**

- The optical depth along a path is additive across cells. If the packet needs $\tau_{\rm left}$ more, and the shell it is in offers $\tau_{\rm cell}=\rho\kappa\,s_b$ to its boundary, then:
  - if $\tau_{\rm left}\ge\tau_{\rm cell}$, the packet crosses, and $\tau_{\rm left}\leftarrow\tau_{\rm left}-\tau_{\rm cell}$;
  - otherwise it interacts after a distance $s=\tau_{\rm left}/\rho\kappa$ (eq 35 written for one cell).
- Because the exponential law is memoryless, discarding the unused budget at a scattering and drawing a new one is exact, not an approximation.

---

## Session B: do

**Problem 1: absorption only**

- A homogeneous sphere of radius 1 with $\rho\kappa=\tau_0$ and albedo $a=0$. Emit $2\times10^4$ packets from the centre.
- The escaped fraction must be $e^{-\tau_0}$. Check $\tau_0=1$ and $\tau_0=10$.

**Problem 2: conservative scattering**

- Same sphere with $a=1$ and isotropic scattering. Every packet must escape. Record the mean number of scatterings $\langle N_{\rm sc}\rangle$ for $\tau_0=5,10,20$.
- Compare with Forgan's eq (57), which implies $N_{\rm sc}\approx3\tau_0^2$, and with the better estimate $\tau_0^2/2+0.68\,\tau_0$. Which is right? By how much is eq (57) off at $\tau_0=20$?

**Problem 3: the exit-angle distribution**

- For $\tau_0=20$ record the exit cosine $\mu_{\rm exit}$ and plot its histogram. Preview of MC-20: the distribution is not isotropic outward but is weighted towards $\mu=1$ (limb darkening).

**Problem 4: path-length bookkeeping**

- Check that the sum over shells of `path_shell` equals the sum over packets of `path`.
- In the absorbing case (Problem 1) with $\tau_0\to\infty$ every packet is absorbed after one free path, so the mean path length must tend to $1/\rho\kappa$. Verify with $\tau_0=50$ and $\rho\kappa=50$ (expected mean path 0.02).

---

## Translation: text → code

| Forgan | Meaning | Code |
|---|---|---|
| eq (16) | $\tau_{\rm scatter}$ | `tau_rem = -np.log1p(-rng.random(n))` |
| §4.3 | accumulate, stop | `cross = tau_rem >= kr*s_b` |
| eq (35) | last-cell distance | `s = tau_rem / kr` |
| eq (5) | absorb or scatter | `scat = rng.random(m) < albedo[shell]` |
| eqs (36)–(37) / (48) | new direction | `phase` = `"iso"`, `"hg"` or `"rayleigh"` |
| eq (57) | $N_{\rm sc}\approx3\tau^2$ | **overestimate**, see Problem 2 |

---

## Contract

```text
starmc/transport.py
  run_packets(rng, r0, r_edges, kapparho, albedo, phase="iso", g=0.0, mu0=None)
      r0:        (n,) starting radii
      r_edges:   (M+1,) shell edges, r_edges[0] = 0
      kapparho:  (M,) kappa*rho per shell (per unit length)
      albedo:    (M,) or scalar
      returns dict:
        state    (n,) int, 1 = escaped, 2 = absorbed
        nsc      (n,) int, number of scatterings
        path     (n,) total path length
        path_shell (M,) path length summed over packets, per shell
        mu_exit  (n,) radial cosine at exit, nan if absorbed
```

```python
# acceptance-test
import numpy as np
from starmc.transport import run_packets
rng = np.random.default_rng(7)
edges = np.array([0.0, 1.0])
for tau in (1.0, 3.0):
    o = run_packets(rng, np.zeros(40_000), edges, np.array([tau]), 0.0)
    p = np.exp(-tau)
    f = (o["state"] == 1).mean()
    assert abs(f - p) < 4 * np.sqrt(p * (1 - p) / 40_000), (tau, f, p)
    assert (o["state"] != 0).all()
for tau in (5.0, 10.0, 20.0):
    o = run_packets(rng, np.zeros(20_000), edges, np.array([tau]), 1.0)
    assert (o["state"] == 1).all()
    ref = tau**2 / 2 + 0.68 * tau
    assert abs(o["nsc"].mean() / ref - 1) < 0.04, (tau, o["nsc"].mean(), ref)
assert abs(o["path"].sum() - o["path_shell"].sum()) < 1e-6 * o["path"].sum()
assert o["mu_exit"].min() > 0 and 0.5 < o["mu_exit"].mean() < 1.0
print("MC-06 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| escaped fraction, $a=0$, $\tau_0=1$ | 0.3679 |
| escaped fraction, $a=0$, $\tau_0=10$ | $4.5\times10^{-5}$ |
| $\langle N_{\rm sc}\rangle$ at $\tau_0=5,10,20$ | about 16.3, 57.4, 213 |
| $\tau_0^2/2+0.68\tau_0$ at the same values | 15.9, 56.8, 213.6 |
| Forgan eq (57), $3\tau_0^2$ at $\tau_0=20$ | 1200 (about 5.6× too large) |

---

## Done when

- You can narrate one packet's life in six steps and say which module each step comes from.
- You can say why a new $\tau$ may be drawn after every scattering.
- You can explain why $N_{\rm sc}\propto\tau^2$ and not $\tau$, and what that means for the cost of the Sun (MC-16).
