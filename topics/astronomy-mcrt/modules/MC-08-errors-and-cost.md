# Module MC-08: Errors and cost

[← MC-07](MC-07-outputs-images-and-flux.md) · [README](../README.md) · [Next: MC-09 A toy star →](MC-09-toy-star-polytrope.md)

**Source:** Forgan, §7 (eq 53) and §8 (eqs 54–59), pp. 16–17.

---

## Session A: read

- Forgan §7: Poisson errors on bins.
- Forgan §8: the cost of a run, $T\sim N_\gamma N_{\rm steps}$, and the estimate for a sphere.
- Optional: Whitney (2011), *Monte Carlo radiative transfer*, Bull. Astr. Soc. India 39, 101, the section on efficiency and variance reduction.

**Key ideas**

- Counting packets in a bin is a Poisson process. If a bin holds $n$ packets, the standard deviation is $\sqrt n$, so the relative error is $1/\sqrt n$ (eq 53 with $E_{ijk}=E_\gamma N_{ijk}$).
- To get a 1 % error in a bin you need $10^4$ packets **in that bin**. If the bin gets a fraction $f$ of all packets, you need $N_{\rm tot}=10^4/f$.
- Cost: $T\sim N_\gamma\times N_{\rm steps}$ (eq 54). $N_{\rm steps}$ grows with optical depth, and for a scattering medium it grows like $\tau^2$.

**Derivation to see once: why $N_{\rm sc}\sim\tau^2$ (and what eq 57 gets wrong)**

- Between interactions the packet flies a distance $s$ with density $e^{-s/\ell}/\ell$, whose second moment is $\langle s^2\rangle=2\ell^2$. Directions are independent after each scattering.
- For independent random steps, $\langle|\mathbf r_N|^2\rangle=N\langle s^2\rangle=2N\ell^2$ (the cross terms average to zero).
- Escape from a sphere of radius $R$ needs $|\mathbf r_N|\sim R$, so $N_{\rm sc}\sim R^2/2\ell^2=\tau^2/2$ with $\tau=R/\ell$.
- Forgan writes $R=\sqrt{N_{\rm sc}/3}\,\ell$ (eq 57), which gives $N_{\rm sc}=3\tau^2$: it uses a step of fixed length $\ell$ with a per-axis share of $1/3$, and drops the factor 2 from the exponential step distribution. The more careful first-passage count for a packet released at the centre is close to $\tau^2/2+0.68\,\tau$ (the second term is the surface layer). So eq (57) overestimates by about a factor 6 at large $\tau$. The scaling $\tau^2$ is right; the prefactor is not.
- You measured this in MC-06, Problem 2.

---

## Session B: do

**Problem 1: Poisson error of a bin**

- Run MC-07's cone test for $N=10^5,10^6,10^7$ (or the same count in repeated runs). Show that the scatter of the recovered flux scales as $1/\sqrt n$.

**Problem 2: how many packets?**

- Implement `packets_needed(frac_in_bin, rel_err)`. How many packets do you need for 1 % in a bin that gets $10^{-2}$ of them? In a cone of $1^\circ$ half-angle out of $4\pi$ ($f=7.6\times10^{-5}$)?

**Problem 3: measure the cost scaling**

- Time `run_packets` for conservative scattering in a unit sphere at $\tau_0=5,10,20,40$. Fit $\log T$ against $\log\tau_0$. The slope should be close to 2.

**Problem 4: extrapolate to the Sun**

- Take $\tau_{\rm tot}\simeq2.3\times10^{12}$ (MC-16) and $N_{\rm sc}\simeq\tau^2/2$. How many scatterings does one packet need? At $10^8$ steps per second, how long for one packet?
- Conclusion: what must change, and which later modules change it (MC-17, MC-18)?

---

## Translation: text → code

| Forgan | Meaning | Code |
|---|---|---|
| eq (53) | $\sigma=E_\gamma\sqrt N$ | `poisson_sigma(counts, E_gamma)` |
| eq (54) | $T\sim N_\gamma N_{\rm steps}$ | timing loop |
| eq (57) | $N_{\rm sc}\approx3\tau^2$ | **prefactor flag** |
| eq (59) | $T\sim N_\gamma R/dx\,\langle\tau\rangle$ | derived for dust, see MC-16 |

---

## Contract

```text
starmc/stats.py
  poisson_sigma(counts, E_gamma=1.0) -> E_gamma * sqrt(counts)
  packets_needed(frac_in_bin, rel_err) -> N_tot = 1 / (frac_in_bin * rel_err**2)
```

```python
# acceptance-test
import numpy as np
from starmc.stats import poisson_sigma, packets_needed
assert np.isclose(poisson_sigma(100, 2.0), 20.0)
assert np.allclose(poisson_sigma(np.array([4, 9, 16])), [2, 3, 4])
assert np.isclose(packets_needed(1e-2, 1e-2), 1e6)
assert np.isclose(packets_needed(1.0, 0.1), 100.0)
rng = np.random.default_rng(3)
f = 0.01
est = rng.binomial(10**6, f, size=4000) / 10**6
rel = est.std() / est.mean()
assert abs(rel - 1 / np.sqrt(f * 10**6)) < 0.1 * rel + 0.002
print("MC-08 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| $N_{\rm tot}$ for 1 % in a bin with $f=10^{-2}$ | $10^6$ |
| $N_{\rm tot}$ for 1 % in a $1^\circ$ cone | $1.3\times10^{8}$ |
| slope of $\log T$ against $\log\tau_0$ | about 2 |
| solar $N_{\rm sc}$ per packet | about $2.7\times10^{24}$ |

---

## Done when

- You can say why the cost of a bin goes as $1/(f\,\epsilon^2)$.
- You can explain the $\tau^2$ scaling with a random-walk argument and name what is wrong in eq (57).
- You can state in one sentence why direct MCRT cannot be run on the Sun as it stands.
