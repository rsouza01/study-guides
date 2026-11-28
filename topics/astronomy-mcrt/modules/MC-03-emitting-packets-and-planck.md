# Module MC-03: Emitting packets, directions and the Planck spectrum

[← MC-02](MC-02-sampling-cdf-and-accept-reject.md) · [README](../README.md) · [Next: MC-04 Scattering →](MC-04-scattering-and-phase-functions.md)

**Source:** Forgan, §3 (eqs 17–22), pp. 7–8. Planck and Stefan–Boltzmann as in PH-18 and PH-19.

---

## Session A: read

- Forgan §3, eqs (17)–(22): packet counts, source energy, frequency sampling from $B_\nu$, isotropic direction.
- PH-18 (Planck) and PH-19 (Stefan–Boltzmann with $\zeta(4)$): you need $\int_0^\infty x^3/(e^x-1)dx=\pi^4/15$.
- Optional: Lucy (1999), *Computing radiative equilibria with Monte Carlo techniques*, A&A 344, 282, the section on packet energies.

**Key ideas**

- A **packet** is a bundle of $N_\gamma$ photons treated as one object. Equal-energy packets are the simplest choice: $E_\gamma=L\Delta t/N_{\rm tot}$ (eqs 17, 51).
- A source with luminosity $L_i$ emits $N_i=N_{\rm tot}L_i/L$ packets. Rounding must keep $\sum N_i=N_{\rm tot}$.
- Direction is sampled isotropically: $\mu=-1+2\zeta$, $\varphi=2\pi\zeta$ (eqs 21–22, again 36–37).
- Frequency is sampled from the Planck shape, which in $x=h\nu/kT$ is $x^3/(e^x-1)$.

**Derivation to see once: isotropic direction**

- Isotropy means uniform density on the sphere: $dN\propto d\Omega=d\mu\,d\varphi$.
- So $\mu$ is uniform on $[-1,1]$ and $\varphi$ uniform on $[0,2\pi)$, independent. Invert each: $\mu=-1+2\zeta_1$, $\varphi=2\pi\zeta_2$.
- Taking $\theta$ uniform instead would pile packets at the poles, because $d\Omega=\sin\theta\,d\theta\,d\varphi$.

**Derivation to see once: Planck sampling through $\zeta(4)$**

- The target density is $p(x)=\dfrac{15}{\pi^4}\dfrac{x^3}{e^x-1}$.
- Expand $\dfrac1{e^x-1}=\sum_{l\ge1}e^{-lx}$. Then $p(x)=\dfrac{15}{\pi^4}\sum_{l\ge1}x^3e^{-lx}$.
- Each term is a Gamma(4) shape in $lx$: $\int_0^\infty x^3e^{-lx}dx=6/l^4$. So $p$ is a **mixture** of Gamma densities with weights $w_l=\dfrac{1}{\zeta(4)\,l^4}$, using $\sum l^{-4}=\zeta(4)=\pi^4/90$ and $\dfrac{15}{\pi^4}\cdot6=\dfrac1{\zeta(4)}$.
- Recipe: pick $l$ with probability $l^{-4}/\zeta(4)$, then draw $x=(\text{sum of 4 exponentials})/l$. No tabulation needed.
- Moments follow from the same series: $\langle x\rangle=4\zeta(5)/\zeta(4)=3.8322$ and $\langle x^2\rangle=20\zeta(6)/\zeta(4)$.

---

## Session B: do

**Problem 1: packet counts with a remainder**

- Write `packet_counts(L, N_tot)` that gives each source an integer count proportional to its luminosity and sums exactly to `N_tot` (largest-remainder rule).
- Test with `L = [1, 2, 3, 4]` and `N_tot = 10`.

**Problem 2: isotropic directions**

- Sample $10^5$ directions. Show that the mean of each component is 0 and the mean of $\mu^2$ is $1/3$.
- Show that sampling $\theta$ uniformly breaks this (mean of $\cos^2\theta$ is not 1/3).

**Problem 3: two Planck samplers**

- Build a table sampler (MC-02, Problem 3) and the $\zeta(4)$ mixture sampler. Compare $\langle x\rangle$ and $\langle x^2\rangle$ of both with the exact values.
- Which is faster? Which is more accurate in the tail?

**Problem 4: emission from a surface**

- A packet leaving a surface outward has a Lambert (cosine-weighted) distribution: density $\propto\mu\,d\mu$. Derive $\mu=\sqrt\zeta$ and check $\langle\mu\rangle=2/3$, $\langle\mu^2\rangle=1/2$.
- Where will you need it? (Hint: MC-19, relocating packets at the top of a convective zone.)

---

## Translation: text → code

| Forgan | Meaning | Code |
|---|---|---|
| eq (17) | $N_{\gamma,{\rm obj}}=N_{\gamma,{\rm tot}}L_{\rm obj}/L_{\rm tot}$ | `packet_counts(L, N_tot)` |
| eqs (18)–(19) | Planck normalisation $\int B_\nu d\nu=\sigma T^4/\pi$ | cumulative table or the $\zeta(4)$ sampler |
| eq (20) | cell luminosity $4\pi m\int\kappa_\nu B_\nu d\nu$ | MC-14 |
| eqs (21)–(22) | $\mu=-1+2\zeta$, $\varphi=2\pi\zeta$ | `isotropic_directions(rng, n)` |

---

## Contract

```text
starmc/emission.py
  isotropic_directions(rng, n) -> (n, 3) unit vectors
  lambert_mu(rng, n) -> ndarray
  packet_counts(L, N_tot) -> int ndarray, sums to N_tot
  sample_radius_from_shells(rng, r_edges, weights, n) -> (r, shell_index)
starmc/planck.py
  planck_x_pdf(x)                      normalised, int = 1
  planck_x_cdf_table(xmax=60.0, n=20001) -> (x_grid, cdf)
  sample_planck_x(rng, n, method="table" | "zeta") -> ndarray of x = h nu / kT
  sample_gamma_mixture(rng, n, k, extra_power=0)
```

- `sample_radius_from_shells` draws the radius uniformly in **volume** inside a shell, chosen with probability proportional to `weights`: $r=(r_{\rm in}^3+\zeta(r_{\rm out}^3-r_{\rm in}^3))^{1/3}$.

```python
# acceptance-test
import numpy as np
from scipy.special import zeta
from starmc.emission import isotropic_directions, lambert_mu, packet_counts, sample_radius_from_shells
from starmc.planck import sample_planck_x
rng = np.random.default_rng(1)
pc = packet_counts(np.array([1.0, 2.0, 3.0, 4.0]), 10)
assert list(pc) == [1, 2, 3, 4]
assert packet_counts(np.array([1.0, 1.0, 1.0]), 10).sum() == 10
d = isotropic_directions(rng, 200_000)
assert np.allclose(np.linalg.norm(d, axis=1), 1.0)
assert np.all(np.abs(d.mean(axis=0)) < 0.01)
assert abs((d[:, 2] ** 2).mean() - 1 / 3) < 0.005
lm = lambert_mu(rng, 200_000)
assert abs(lm.mean() - 2 / 3) < 0.005 and abs((lm**2).mean() - 0.5) < 0.005
m1, m2 = 4 * zeta(5) / zeta(4), 20 * zeta(6) / zeta(4)
for method in ("table", "zeta"):
    x = sample_planck_x(rng, 400_000, method)
    assert abs(x.mean() - m1) < 0.02, (method, x.mean())
    assert abs((x**2).mean() - m2) < 0.15, (method, (x**2).mean())
edges = np.linspace(0.0, 1.0, 5)
r, i = sample_radius_from_shells(rng, edges, np.array([0.0, 1.0, 0.0, 0.0]), 20_000)
assert np.all(i == 1) and np.all((r >= 0.25) & (r < 0.5))
print("MC-03 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| `packet_counts([1,2,3,4], 10)` | `[1, 2, 3, 4]` |
| $\langle x\rangle$, Planck in $x$ | 3.8322 |
| $\langle x^2\rangle$ | 18.7992 |
| Lambert $\langle\mu\rangle$, $\langle\mu^2\rangle$ | 2/3, 1/2 |
| isotropic $\langle\mu^2\rangle$ | 1/3 |

---

## Done when

- You can derive $\mu=-1+2\zeta$ from "uniform on the sphere" and say why uniform $\theta$ is wrong.
- You can follow the $\zeta(4)$ mixture derivation and say where $\sum l^{-4}$ comes from.
- You can say why packets are equal-energy here and what you would change for importance sampling.
