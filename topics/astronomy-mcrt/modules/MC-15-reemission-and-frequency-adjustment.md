# Module MC-15: Re-emission and frequency adjustment

[← MC-14](MC-14-radiative-equilibrium-by-monte-carlo.md) · [README](../README.md) · [Next: MC-16 Why a direct run fails →](MC-16-why-direct-mcrt-fails.md)

**Source:** Forgan §9.1.2 (eqs 70–74), pp. 19–20. Original method: Bjorkman & Wood (2001), ApJ 554, 615. Planck mean: Forgan eq (63) and PH-18.

---

## Session A: read

- Forgan §9.1.2, eqs (70)–(74).
- Bjorkman & Wood (2001): the section on the temperature correction.
- Re-read MC-03, the $\zeta(4)$ derivation. You will need it again.

**Key ideas**

- In non-grey RE a packet absorbed in a cell is re-emitted at a new frequency drawn from the cell's emissivity at the **current** temperature.
- The temperature keeps changing as packets arrive, so the early re-emissions used a wrong (cooler) emissivity. Bjorkman–Wood fix this packet by packet: when a packet raises the temperature by $\Delta T$, the extra energy the cell must radiate away has the spectrum $\Delta j_\nu\propto\kappa_\nu\,\partial_TB_\nu\,\Delta T$ (eq 72).
- So the frequency of the re-emitted packet is drawn from $P(\nu)=\kappa_\nu\,\partial_TB_\nu/C$ (eqs 73–74).

**Derivation to see once: the sampling density and its moments**

- Write $x=h\nu/kT$. Then $\partial_TB_\nu=\dfrac{2h\nu^3}{c^2}\cdot\dfrac{h\nu}{kT^2}\dfrac{e^x}{(e^x-1)^2}\propto x^4\dfrac{e^x}{(e^x-1)^2}$.
- For a power-law opacity $\kappa_\nu\propto\nu^\beta$, the density to sample is $p(x)\propto x^{4+\beta}\dfrac{e^x}{(e^x-1)^2}$.
- Integrate by parts: $\displaystyle\int_0^\infty\frac{x^ne^x}{(e^x-1)^2}dx=n\int_0^\infty\frac{x^{n-1}}{e^x-1}dx=n\,\Gamma(n)\zeta(n)=\Gamma(n+1)\zeta(n)$.
- Hence the normalisation is $\Gamma(5+\beta)\zeta(4+\beta)$ and the mean is
$$\langle x\rangle=\frac{\Gamma(6+\beta)\zeta(5+\beta)}{\Gamma(5+\beta)\zeta(4+\beta)}=(5+\beta)\frac{\zeta(5+\beta)}{\zeta(4+\beta)}.$$
- For $\beta=0$: $5\zeta(5)/\zeta(4)=4.7907$. For $\beta=2$: $7\zeta(7)/\zeta(6)=6.9384$.
- The Planck mean for the same power law, from MC-03: $\kappa_P/\kappa_0(kT/h)^\beta=\dfrac{\Gamma(4+\beta)\zeta(4+\beta)}{\Gamma(4)\zeta(4)}$. For $\beta=0$ it is 1; for $\beta=1$, $3.832$; for $\beta=2$, $18.80$ (the value of $\langle x^2\rangle$ from MC-03).

**Where this matters for the star**

- A grey interior does not need it (MC-14). Use it when you want the **emergent spectrum from interior layers**, or a non-grey opacity (e.g. a Rosseland mean per frequency band) in the envelope.

---

## Session B: do

**Problem 1: Planck mean of a power law**

- Implement `planck_mean_ratio(beta)`. Check against direct numerical integration for $\beta=0,1,2$.

**Problem 2: the adjustment density**

- Implement `dBdT_x_pdf(x, beta)` (unnormalised) and `sample_dBdT_x(rng, n, beta)` by a tabulated inverse CDF on $x\in[0,80]$.
- Check $\langle x\rangle$ against $(5+\beta)\zeta(5+\beta)/\zeta(4+\beta)$ for $\beta=0$ and 2.

**Problem 3: why the re-emitted packets are hotter**

- Compare $\langle x\rangle$ of the adjustment density (4.79 for $\beta=0$) with that of the Planck density (3.83). Explain physically why correcting a temperature rise re-emits at higher frequency than the plain Planck spectrum.

**Problem 4: size of $\Delta T$**

- A cell of mass $m=10^{31}$ g at $T=10^7$ K with heat capacity per mass $c_V\simeq10^8$ erg g⁻¹ K⁻¹ absorbs one packet of energy $E_\gamma=L\Delta t/N_{\rm tot}$. Take $L=L_\odot$, $\Delta t=3\times10^{11}$ s (about $10^4$ yr, the order of the core diffusion time) and $N_{\rm tot}=10^5$.
- Estimate $\Delta T/T=E_\gamma/(m\,c_V\,T)$. Is the linearisation of eq (72) justified? (About $10^{-6}$: yes.)

---

## Translation: text → code

| Forgan | Meaning | Code |
|---|---|---|
| eq (70) | $j'_\nu=\kappa_\nu B_\nu(T-\Delta T)$ | the emission already done |
| eq (71) | $\Delta j_\nu=\kappa_\nu[B_\nu(T)-B_\nu(T-\Delta T)]$ | the extra to radiate |
| eq (72) | $\Delta j_\nu\simeq\kappa_\nu\,\partial_TB_\nu\,\Delta T$ | linearised |
| eqs (73)–(74) | $P(\nu)=\kappa_\nu\partial_TB_\nu/C$ | `sample_dBdT_x(rng, n, beta)` |

---

## Contract

```text
starmc/radeq.py
  planck_mean_ratio(beta)                  Gamma(4+b) zeta(4+b) / (Gamma(4) zeta(4))
  dBdT_x_pdf(x, beta=0.0)                  x^(4+beta) e^x / (e^x - 1)^2, unnormalised
  sample_dBdT_x(rng, n, beta=0.0, xmax=80.0, ngrid=40001) -> ndarray of x
```

```python
# acceptance-test
import numpy as np
from scipy.special import zeta
from starmc.radeq import planck_mean_ratio, dBdT_x_pdf, sample_dBdT_x
assert abs(planck_mean_ratio(0.0) - 1.0) < 1e-12
assert abs(planck_mean_ratio(1.0) - 4 * zeta(5) / zeta(4)) < 1e-12
assert abs(planck_mean_ratio(2.0) - 20 * zeta(6) / zeta(4)) < 1e-12
x = np.linspace(1e-6, 60, 400001)
for b in (0.0, 1.0, 2.0):
    f = x**3 * x**b / np.expm1(x)
    num = np.trapezoid(f, x) / np.trapezoid(x**3 / np.expm1(x), x)
    assert abs(num - planck_mean_ratio(b)) < 1e-4 * num
assert np.all(dBdT_x_pdf(np.array([0.5, 2.0, 10.0])) > 0)
rng = np.random.default_rng(2)
for b in (0.0, 2.0):
    s = sample_dBdT_x(rng, 300_000, b)
    ref = (5 + b) * zeta(5 + b) / zeta(4 + b)
    assert abs(s.mean() - ref) < 0.03, (b, s.mean(), ref)
print("MC-15 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| $\kappa_P$ ratio, $\beta=0,1,2$ | 1, 3.832, 18.80 |
| $\langle x\rangle$ of the adjustment density, $\beta=0$ | 4.791 |
| $\langle x\rangle$, $\beta=2$ | 6.938 |
| Planck $\langle x\rangle$ | 3.832 |

---

## Done when

- You can derive the density in eq (73) from eqs (70)–(72) and write its mean in terms of $\zeta$.
- You can say why the grey stellar interior does not need frequency adjustment but a spectrum does.
- You can explain what happens to eq (72) if $\Delta T$ is not small (many fewer packets).
