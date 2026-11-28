# Module MC-18: The modified random walk

[← MC-17](MC-17-opacity-scaling.md) · [README](../README.md) · [Next: MC-19 The star engine →](MC-19-the-star-engine.md)

**Source:** not in Forgan. Min, Dullemond, Dominik, de Koter & Hovenier (2009), A&A 497, 155 (the modified random walk); Robitaille (2010), A&A 520, A70 (the improved version, with the first-passage distribution). Connection to PH-19 and to the Riemann guide: $\zeta$ and $\eta$ appear in the mean time.

---

## Session A: read

- Min et al. (2009): the method and the first-passage distribution in a sphere.
- Robitaille (2010): the refinements (the radius of the sphere, the boundary treatment).
- Re-read MC-17 (the scaling) and MC-16 (why you need a shortcut at all).

**Key ideas**

- In a very thick cell a packet takes thousands of tiny steps. If the cell is uniform, you can replace them by **one jump**: draw the packet's position on a sphere of radius $R_0$ centred on it that lies inside the cell, and draw the elapsed time from the exact first-passage distribution of a diffusing particle leaving that sphere.
- The first-passage time to the sphere $R_0$ is a function of $y=Dt/R_0^2$ only, with $D=c\ell/3$. So one table serves every jump.

**Derivation to see once: the first-passage law from the centre of a sphere**

- Let $p(r,t)$ be the density of a particle diffusing from the centre of a sphere of radius $R_0$ with an absorbing wall. Put $w=rp$. For spherical symmetry $\partial_tw=D\,\partial_r^2w$ with $w(0)=w(R_0)=0$.
- The eigenfunctions are $\sin(n\pi r/R_0)$ with decay rates $n^2\pi^2D/R_0^2$. A point source at the centre excites them with alternating signs: the survival probability is
$$S(t)=2\sum_{n=1}^\infty(-1)^{n+1}e^{-n^2\pi^2y},\quad y=\frac{Dt}{R_0^2}.$$
- The first-passage CDF is $P(y)=1-S=1+2\sum_{n\ge1}(-1)^ne^{-n^2\pi^2y}$. This is the Jacobi theta function $\vartheta_4(0,e^{-\pi^2y})$.
- At small $y$ the alternating series converges slowly. Write it as $P(y)=\sum_{n\in\mathbb Z}(-1)^ne^{-\pi^2n^2y}$ and apply Poisson summation (the Jacobi transformation): $\sum_{n\in\mathbb Z}(-1)^ne^{-an^2}=\sqrt{\pi/a}\sum_{k\in\mathbb Z}e^{-\pi^2(k+1/2)^2/a}$. With $a=\pi^2y$ this becomes
$$P(y)=\frac{2}{\sqrt{\pi y}}\sum_{k\ge0}e^{-(k+1/2)^2/y},$$
which converges in a handful of terms for $y\le0.1$.
- **Mean time.** $\langle y\rangle=\int_0^\infty S\,dy=2\sum_{n\ge1}(-1)^{n+1}\dfrac1{n^2\pi^2}=\dfrac{2}{\pi^2}\eta(2)$, where $\eta(s)=\sum(-1)^{n+1}n^{-s}$ is the Dirichlet eta function. Since $\eta(2)=\pi^2/12$, $\langle y\rangle=1/6$, so $\langle t\rangle=R_0^2/6D$. This is the same $R^2/6D$ as in MC-11, now seen as a $\zeta/\eta$ value.
- **Jump geometry.** The new position is uniform on the sphere of radius $R_0$ about the old one. If the old radius is $r$ and $u$ is uniform in $[-1,1]$, the new radius is $r'=\sqrt{r^2+R_0^2+2rR_0u}$ (law of cosines). The path charged is $c\,t=3R_0^2y/\ell$, because $D=c\ell/3$.

**Limits of the method (found while building this guide)**

- The sphere must stay inside the **current shell**: $R_0=\gamma\min(r-r_{\rm in},r_{\rm out}-r)$ with $\gamma\simeq0.95$. Near a shell boundary $R_0\to0$ and the method stops helping.
- If the walk is *near* a hard boundary the packet keeps taking small jumps toward it (a gambler's-ruin problem), and the cost grows with the shell's optical thickness. In the toy star with $10^2$ shells of $\tau\sim10^{10}$ each the numpy and numba MRW codes ran for minutes without finishing.
- Hence this guide uses MRW **only inside a validated regime** (a few thick, uniform cells), and opacity scaling in the star (MC-17).
- The jump gives the time and position exactly but **not the direction**: after a jump the packet is isotropised. The exit-angle distribution from MRW is therefore not trustworthy ($\langle\mu\rangle$ about 0.68 against 0.71 for plain Monte Carlo).

---

## Session B: do

**Problem 1: the CDF**

- Implement `theta4_cdf(y)` with the two series (large $y$: $n\le7$; small $y\le0.1$: $k\le11$). Check continuity at $y=0.1$ and $P(\infty)=1$.

**Problem 2: sample the jump time**

- Build a log-spaced table of $P(y)$ for $y\in[10^{-4},10^{1.3}]$, enforce monotonicity, and invert with `np.interp` in $\log y$. Implement `sample_exit_y(rng, n)`.
- Check $\langle y\rangle=1/6$ and the median 0.139.

**Problem 3: mean time from the series**

- Sum $2\sum(-1)^{n+1}/(n^2\pi^2)$ numerically and confirm it equals $1/6$. Identify $\eta(2)$ and the identity $\eta(s)=(1-2^{1-s})\zeta(s)$; use it to recover $\eta(2)=\pi^2/12$.

**Problem 4: one jump against many steps**

- In a uniform sphere ($R=1$, $\tau_0=100$) compare the cost of reaching the surface with plain steps (about 5000) to MRW (about 10 steps). You will implement this comparison in MC-19.

---

## Translation: text → code

| Quantity | Code |
|---|---|
| $P(y)$, large $y$ | `1 + 2*sum((-1)**n * exp(-n**2*pi**2*y))` |
| $P(y)$, small $y$ | `2/sqrt(pi*y) * sum(exp(-(k+.5)**2/y))` |
| inverse | `np.exp(np.interp(u, P, np.log(y)))` |
| path charged | `s = 3*R0**2*y/ell` |
| new radius | `r' = sqrt(r**2 + R0**2 + 2*r*R0*u)` |

---

## Contract

```text
starmc/mrw.py
  theta4_cdf(y) -> ndarray, P(y)
  sample_exit_y(rng, n) -> ndarray of y = D t / R0^2
```

```python
# acceptance-test
import numpy as np
from starmc.mrw import theta4_cdf, sample_exit_y
y = np.array([0.05, 0.1, 0.2, 0.5, 1.0])
P = theta4_cdf(y)
assert np.allclose(P, [0.034001, 0.292900, 0.722922, 0.985616, 0.999897], atol=2e-5), P
e = 1e-9
assert abs(theta4_cdf(np.array([0.1 - e]))[0] - theta4_cdf(np.array([0.1 + e]))[0]) < 1e-6
assert abs(theta4_cdf(np.array([30.0]))[0] - 1.0) < 1e-12
n = np.arange(1, 200000)
assert abs(2 * np.sum((-1.0) ** (n + 1) / (n**2 * np.pi**2)) - 1 / 6) < 1e-6
rng = np.random.default_rng(2)
s = sample_exit_y(rng, 200_000)
assert abs(s.mean() - 1 / 6) < 0.003, s.mean()
assert abs(np.median(s) - 0.1388) < 0.004
print("MC-18 ok")
```

---

## Checkpoints

| $y$ | $P(y)$ |
|---|---|
| 0.05 | 0.0340 |
| 0.1 | 0.2929 |
| 0.2 | 0.7229 |
| 0.5 | 0.9856 |
| 1.0 | 0.99990 |

| Quantity | Value |
|---|---|
| $\langle y\rangle$ | $1/6=0.16667$ |
| median of $y$ | 0.139 |
| $\eta(2)$ | $\pi^2/12=0.822467$ |

---

## Done when

- You can derive the survival series from the eigenmodes and identify $\vartheta_4$.
- You can show $\langle t\rangle=R_0^2/6D$ from the series and name $\eta(2)$.
- You can state two limits of the method (shell boundaries, lost direction) and which later module avoids each.
