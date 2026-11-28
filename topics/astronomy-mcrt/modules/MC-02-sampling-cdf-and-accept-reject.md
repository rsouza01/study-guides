# Module MC-02: Sampling random numbers

[← MC-01](MC-01-transfer-equation-and-free-path.md) · [README](../README.md) · [Next: MC-03 Emitting packets →](MC-03-emitting-packets-and-planck.md)

**Source:** Forgan, §2 and §2.1 (eqs 14–16), pp. 6–7.

---

## Session A: read

- Forgan §2.1.1 (the cumulative distribution method, eqs 14–16) and §2.1.2 (accept/reject).
- Optional: Press et al., *Numerical Recipes*, the chapter "Random Numbers", section on transformation and rejection methods.
- Optional: Kalos & Whitlock, *Monte Carlo Methods*, Vol. I, Ch. 3 (sampling from given distributions).

**Key ideas**

- A computer gives uniform numbers $\zeta\in[0,1)$. Every other distribution is a transformation or a filter of those.
- **Inverse CDF.** If $\psi(x)=\int_{-\infty}^xP$ is the CDF, then $x=\psi^{-1}(\zeta)$ has density $P$.
- **Accept/reject.** Draw $x$ uniform on $[a,b]$ and $y$ uniform on $[0,y_{\max}]$. Keep $x$ if $y<P(x)$. Efficiency is the accepted fraction.
- When $\psi$ has no closed inverse, tabulate it and interpolate. That is what the Planck sampler of MC-03 does.

**Derivation to see once: why the inverse CDF works**

- Let $x=\psi^{-1}(\zeta)$ with $\zeta$ uniform. Since $\psi$ is increasing, $x\le x_0\iff\zeta\le\psi(x_0)$.
- Therefore $\Pr(x\le x_0)=\psi(x_0)$, which is exactly the statement that $x$ has CDF $\psi$.
- For $P(\tau)=e^{-\tau}$ the CDF is $\psi=1-e^{-\tau}$. Setting $\zeta=1-e^{-\tau}$ gives eq (16): $\tau=-\ln(1-\zeta)$.
- Since $1-\zeta$ is also uniform, $\tau=-\ln\zeta$ works equally well. Prefer $-\ln(1-\zeta)$ with `rng.random()`, because `random()` can return 0 but never 1.

---

## Session B: do

**Problem 1: exponential by inversion**

- Draw $2\times10^5$ samples from $e^{-\tau/s}/s$ with scale $s=2$. Check the mean is 2 and the variance is 4.

**Problem 2: accept/reject on a sine**

- Sample $x\in[0,\pi]$ with density $\propto\sin x$ using accept/reject with $y_{\max}=1$.
- Show that the efficiency is $2/\pi$ (area under the curve over the area of the box). Report the sample mean, which must be $\pi/2$.

**Problem 3: tabulated inverse CDF**

- Take $P(x)\propto x^2e^{-x}$ on $[0,40]$. Build the CDF on a fine grid by cumulative trapezoids, normalise, and invert with `np.interp`.
- Compare the sample mean with the exact value 3 (a Gamma(3,1) law).

**Problem 4: efficiency is a cost**

- For a density with a tall narrow peak in a wide interval the efficiency is small. Estimate the efficiency of accept/reject for $P(x)\propto e^{-x^2/2\sigma^2}$ on $[-5,5]$ with $\sigma=0.1$.
- Say which method you would use instead and why.

---

## Translation: text → code

| Forgan | Meaning | Code |
|---|---|---|
| eq (14) | $\int^{x_0}P=\psi(x_0)$ | `cdf = cumulative trapezoid of pdf` |
| eq (15) | $\zeta=\psi(x_0)$ | `x = np.interp(rng.random(n), cdf, grid)` |
| eq (16) | $\tau=-\ln(1-\zeta)$ | `-np.log1p(-rng.random(n))` |
| §2.1.2 | accept/reject | `accept_reject(rng, pdf, a, b, ymax, n)` |

`-np.log1p(-z)` is the numerically safe form of $-\ln(1-z)$ for small $z$.

---

## Contract

```text
starmc/sampling.py
  sample_exponential(rng, n, scale=1.0) -> ndarray
  sample_from_cdf_table(rng, x_grid, cdf, n) -> ndarray
  accept_reject(rng, pdf, a, b, ymax, n) -> (samples, efficiency)
```

- `accept_reject` returns exactly `n` accepted samples and `efficiency = accepted / trials`.

```python
# acceptance-test
import numpy as np
from starmc.sampling import sample_exponential, sample_from_cdf_table, accept_reject
rng = np.random.default_rng(1)
e = sample_exponential(rng, 200_000, 2.0)
assert abs(e.mean() - 2.0) < 0.03 and abs(e.var() - 4.0) < 0.15
x, eff = accept_reject(rng, np.sin, 0.0, np.pi, 1.0, 200_000)
assert len(x) == 200_000
assert abs(eff - 2 / np.pi) < 0.005, eff
assert abs(x.mean() - np.pi / 2) < 0.01
g = np.linspace(0, 40, 40001)
f = g**2 * np.exp(-g)
cdf = np.concatenate(([0.0], np.cumsum(0.5 * (f[1:] + f[:-1]) * np.diff(g))))
cdf /= cdf[-1]
s = sample_from_cdf_table(rng, g, cdf, 200_000)
assert abs(s.mean() - 3.0) < 0.03, s.mean()
print("MC-02 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| sine accept/reject efficiency | $2/\pi=0.6366$ |
| sine sample mean | $\pi/2=1.5708$ |
| mean of $x^2e^{-x}$ sample | 3 |
| Problem 4 efficiency | about $\sigma\sqrt{2\pi}/10=0.025$ |

---

## Done when

- You can derive the inverse-CDF rule in two lines and apply it to a new density.
- You can say what accept/reject wastes and when a table beats it.
- You can explain why `log1p` is used for $-\ln(1-\zeta)$.
