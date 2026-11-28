# Module MC-05: Rays through grids and shells

[← MC-04](MC-04-scattering-and-phase-functions.md) · [README](../README.md) · [Next: MC-06 The packet loop →](MC-06-the-packet-loop.md)

**Source:** Forgan, §4 (eqs 23–35), pp. 8–11. The star uses the spherical-shell variant of §4.2.2.

---

## Session A: read

- Forgan §4.1 (gridding), §4.2.1 (Cartesian grids, eqs 24–30), §4.2.2 (spherical polar grids, eqs 31–34) and §4.3 (finding the interaction point, eq 35).
- Optional: Amanatides & Woo (1987), *A fast voxel traversal algorithm for ray tracing*, Eurographics '87 (the algorithm behind eqs 26–30).
- Optional: Lucy (1999) for the idea of accumulating path length per cell.

**Key ideas**

- The medium is cut into cells with constant $\rho\kappa$. A ray accumulates $\tau_{\rm cell}=\rho\kappa s$ (eq 23) crossing each, until the running total reaches the sampled $\tau_{\rm scatter}$.
- The interaction point is in the **last** cell, at distance $ds=(\tau_{\rm scatter}-\tau_{\rm run})/\rho\kappa$ from its entry (eq 35).
- A star is spherically symmetric, so concentric shells suffice. The geometry reduces to "distance to the next sphere", and the state of a packet is just $(r,\mu)$ with $\mu=\cos$ of the angle to the radius.

**Misprint flags**

- Eq (32): the quadratic in $s$ is printed without the factor 2 on the linear term. The correct expansion of $|\mathbf r_1+s\mathbf n|^2=r_f^2$ is $s^2+2s\,\mathbf r_1\!\cdot\!\mathbf n+r_1^2-r_f^2=0$.
- Eq (33): the cone is written with the wrong sign; it should be $x^2+y^2-z^2\tan^2\theta_f=0$.
- Eq (35): in the text $\tau_{\rm run}$ is the total **including** the last cell, so the sign as printed gives a negative distance. Use $ds=(\tau_{\rm scatter}-\tau_{\rm before})/\rho\kappa$ where $\tau_{\rm before}$ excludes the last cell.

**Derivation to see once: distance to a sphere along a ray**

- A packet at radius $r$ with radial cosine $\mu$ is at position $\mathbf r$ with $\mathbf r\cdot\mathbf n=r\mu$.
- After moving $s$: $|\mathbf r+s\mathbf n|^2=r^2+2r\mu s+s^2$. This equals $r_f^2$ when $s^2+2r\mu s-(r_f^2-r^2)=0$.
- Let $b=r\mu$ and $d=r_f^2-r^2$. The positive root is $s=-b+\sqrt{b^2+d}$.
- For the **outer** sphere, $d\ge0$. When $b\ge0$ the subtraction cancels badly, so use the equivalent form $s_{\rm out}=\dfrac{d}{b+\sqrt{b^2+d}}$.
- For the **inner** sphere, $d=r_{\rm in}^2-r^2<0$: the ray hits it only if $b<0$ and the discriminant $D=r_{\rm in}^2-r^2(1-\mu^2)\ge0$. The nearer root is $s_{\rm in}=\dfrac{r^2-r_{\rm in}^2}{-b+\sqrt D}$.
- The exit distance from a shell is $\min(s_{\rm out},s_{\rm in})$.
- After a step $s$: $r'=\sqrt{r^2+2r\mu s+s^2}$ and $\mu'=(r\mu+s)/r'$ (the new radial component of the same fixed direction).

---

## Session B: do

**Problem 1: Cartesian traversal (Forgan eqs 24–30)**

- Build a cube $[0,1]^3$ with $N^3$ cells and a constant $\rho\kappa=\tau_0$ per unit length. Trace rays from the centre in random directions to the face.
- The total $\tau$ must equal $\tau_0\times$ (geometric distance to the face). Verify for $10^3$ rays.
- Implement the step to the next face as $s_x=(x_{\rm face}-x_1)/n_x$ per axis and take the minimum (eq 30).

**Problem 2: distance to a shell boundary**

- Implement `distance_to_shell_boundary(r, mu, r_in, r_out)` vectorised over packets, returning the distance and a flag telling whether the inner sphere was hit.
- Test: $r=0.5,\mu=1$ in $[0,1]$ gives $0.5$; $r=0.5,\mu=-1$ in $[0.2,1]$ hits the inner sphere at $0.3$; $r=0.5,\mu=0$ gives $\sqrt{0.75}$.

**Problem 3: why the stable form matters**

- Take $r=1-10^{-9}$, $\mu=1$ in $[0,1]$. Compare the naive $-b+\sqrt{b^2+d}$ with the stable form. Which one has lost digits and by how much?

**Problem 4: advance and conserve**

- Implement `advance(r, mu, s)`. Move $10^5$ random packets by a distance $s$ and check that $r'^2=r^2+2r\mu s+s^2$ and that $|\mu'|\le1$.
- Then use the vector form to check that the position after two half-steps equals the position after one full step.

---

## Translation: text → code

| Forgan | Meaning | Code |
|---|---|---|
| eq (23) | $\tau_{\rm cell}=\rho\kappa s$ | `tau_cell = kappa_rho * s` |
| eqs (26)–(30) | next-face distances, minimum | `trace_ray_tau` |
| eqs (31)–(32) | sphere crossing | `distance_to_shell_boundary` (**factor-2 flag**) |
| eq (33) | cone | not needed in a 1D star (**sign flag**) |
| eq (35) | last-cell distance | inside `run_packets` (MC-06) |

---

## Contract

```text
starmc/grid.py
  trace_ray_tau(pos, n, edges, kapparho) -> (tau_total, [((i,j,k), s), ...])
starmc/shells.py
  distance_to_shell_boundary(r, mu, r_in, r_out) -> (s, hit_inner)   arrays
  advance(r, mu, s) -> (r_new, mu_new)
```

- `edges` is a 1D array of cell edges used on all three axes; `kapparho` has shape `(N, N, N)`.

```python
# acceptance-test
import numpy as np
from starmc.grid import trace_ray_tau
from starmc.shells import distance_to_shell_boundary, advance
rng = np.random.default_rng(5)
edges = np.linspace(0.0, 1.0, 9)
kr = np.full((8, 8, 8), 2.5)
for _ in range(200):
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    p = np.array([0.5, 0.5, 0.5])
    tau, segs = trace_ray_tau(p, n, edges, kr)
    s_geo = min(((1.0 if n[k] > 0 else 0.0) - 0.5) / n[k] for k in range(3) if n[k] != 0)
    assert abs(tau - 2.5 * s_geo) < 1e-9, (tau, 2.5 * s_geo)
s, hit = distance_to_shell_boundary(np.array([0.5, 0.5, 0.5]), np.array([1.0, -1.0, 0.0]), 0.0, 1.0)
assert np.allclose(s, [0.5, 1.5, np.sqrt(0.75)]) and not hit.any()
s, hit = distance_to_shell_boundary(np.array([0.5]), np.array([-1.0]), 0.2, 1.0)
assert np.allclose(s, 0.3) and hit[0]
s, hit = distance_to_shell_boundary(np.array([1 - 1e-9]), np.array([1.0]), 0.0, 1.0)
assert abs(s[0] - 1e-9) < 1e-15, s
r = rng.random(100_000) + 0.01
mu = -1 + 2 * rng.random(100_000)
st = rng.random(100_000) * 0.5
r2, mu2 = advance(r, mu, st)
assert np.allclose(r2**2, r**2 + 2 * r * mu * st + st**2, rtol=1e-10)
assert np.all(np.abs(mu2) <= 1)
ra, ma = advance(r, mu, st / 2)
rb, mb = advance(ra, ma, st / 2)
assert np.allclose(rb, r2, rtol=1e-8)
print("MC-05 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| trace through $\tau_0=2.5$ cube | $\tau=2.5\times$ distance to the face |
| outward from $r=0.5$ in $[0,1]$ | $s=0.5$ |
| inward from $r=0.5$ to inner sphere $0.2$ | $s=0.3$ |
| tangential, $r=0.5$ | $s=\sqrt{0.75}=0.8660$ |
| $r=1-10^{-9},\mu=1$ | $s=10^{-9}$ to full precision |

---

## Done when

- You can derive the shell-crossing distance and say why the inner sphere needs $D\ge0$.
- You can explain the cancellation in $-b+\sqrt{b^2+d}$ and which sign of $\mu$ causes it.
- You can say why the 1D radial state $(r,\mu)$ is enough in a spherical star and what is lost (no azimuthal position).
