# Module MC-01: The transfer equation and the free path

[README](../README.md) · [Next: MC-02 Sampling →](MC-02-sampling-cdf-and-accept-reject.md)

**Source:** Forgan, §1.1 (eqs 1–4) and §1.2 (eqs 8–13), pp. 4–6. Continues PH-27 (radiative transfer) and PH-19 (Stefan–Boltzmann).

---

## Session A: read

- Forgan §1.1, eqs (1)–(4): specific intensity, the transfer equation, the source function, optical depth.
- Forgan §1.2, eqs (8)–(13): mean free path and the probability of reaching a depth without interacting.
- Re-read PH-27 for the same equation in Karttunen's notation (there $\alpha$ is the opacity; here $\kappa_\nu$ is per unit mass and $\rho\kappa_\nu$ per unit length).
- Extra reading (optional):
  - Rybicki & Lightman, *Radiative Processes in Astrophysics*, Ch. 1 (the transfer equation, §1.3–1.4).
  - Carroll & Ostlie, *An Introduction to Modern Astrophysics*, the section on the equation of transfer in the chapter on stellar atmospheres.

**Key ideas**

- $\partial_\ell I_\nu=-\rho\kappa_\nu I_\nu+j_\nu$, so along a ray $I_\nu$ is attenuated at rate $\rho\kappa_\nu$ and fed at rate $j_\nu$.
- Monte Carlo does not integrate this equation. It simulates the **microscopic process** whose average is this equation: a packet flies, interacts at a random depth, is absorbed or scattered.
- Everything rests on one fact: the optical depth to the first interaction is a random number with density $e^{-\tau}$.

**Derivation to see once: the free-path law**

- Let $P(\tau)$ be the probability of travelling optical depth $\tau$ with no interaction.
- Over a further $d\tau$ the interaction probability is $d\tau$ (that is what optical depth means), so $P(\tau+d\tau)=P(\tau)(1-d\tau)$.
- Hence $\partial_\tau P=-P$ with $P(0)=1$, giving $P(\tau)=e^{-\tau}$.
- Forgan reaches the same result by splitting $x$ into $N$ pieces: $(1-\rho\kappa x/N)^N\to e^{-\rho\kappa x}$.
- The probability of interacting before $\tau$ is $1-e^{-\tau}$ (eq 13).

**Misprint flag (eqs 11–12).** The printed eq (12) reads $P(x)=1-\rho\kappa x=e^{-\tau}$. The middle term is the first-order Taylor term, not the limit. The correct chain is $P(x)=\lim_{N\to\infty}(1-\rho\kappa x/N)^N=e^{-\rho\kappa x}=e^{-\tau}$.

---

## Session B: do

**Problem 1: transmitted fraction**

- Draw $10^6$ optical depths to first interaction from the law $P(\tau)=e^{-\tau}$ (use $\tau=-\ln(1-\zeta)$ for now; MC-02 derives it).
- Count the fraction larger than $\tau_0=2$. Compare with $e^{-2}$ and with the binomial error $\sqrt{p(1-p)/N}$.

**Problem 2: number of interactions along a path**

- Place interactions along a line as a unit-rate Poisson process: successive gaps are independent draws from $e^{-\tau}$.
- For a path of optical depth 3, count the interactions for $5\times10^5$ lines. Show that the mean and the variance are both close to 3.
- Explain why this is a Poisson distribution with parameter $\tau$.

**Problem 3: the equation without a computer**

- A uniform slab has $S_\nu$ constant, thickness $\tau_0$, and a background $I_\nu(0)=I_0$ entering from one side.
- Solve eq (3) and show $I_\nu(\tau_0)=I_0e^{-\tau_0}+S_\nu(1-e^{-\tau_0})$.
- Say which two limits ($\tau_0\to0$, $\tau_0\to\infty$) you recover and what each means for a star.

**Problem 4: mean free path in the Sun**

- At the solar centre take $\rho\simeq150\ {\rm g\,cm^{-3}}$ and $\kappa\simeq1\ {\rm cm^2\,g^{-1}}$. Compute $\ell$ from eq (8).
- Compare with the solar radius. Preview of MC-16: how many mean free paths fit in $R_\odot$?

---

## Translation: text → code

| Forgan | Meaning | Code |
|---|---|---|
| eq (4) | $\tau_\nu=\int\rho\kappa_\nu d\ell$ | `tau = np.sum(kappa_rho * ds)` |
| eq (8) | $\ell=1/\rho\kappa$ | `mfp = 1.0 / kappa_rho` |
| eq (13) | $P(\tau)=1-e^{-\tau}$ | the CDF you invert in MC-02 |
| eq (12) | **misprint** | use $e^{-\tau}$ |

---

## Contract

Package layout used by every module (the tests import it):

```text
starmc/
  consts.py      cgs constants
  freepath.py    transmitted_fraction(rng, tau, n), interaction_counts(rng, tau, n)
```

- `consts.py` is in **cgs** from here on, as is usual in stellar structure. PH-xx were in SI. Names: `G, c, k, h, sigma, a_rad, m_u, Msun, Rsun, Lsun, yr, pc, AU, sigma_T, eV, m_e, e_esu`. Use $L_\odot=3.828\times10^{33}$ erg s⁻¹.
- `transmitted_fraction(rng, tau, n)` returns the fraction of $n$ packets whose first-interaction depth exceeds `tau`.
- `interaction_counts(rng, tau, n)` returns an integer array of length `n`.

```python
# acceptance-test
import numpy as np
from starmc.freepath import transmitted_fraction, interaction_counts
rng = np.random.default_rng(21)
n = 1_000_000
f = transmitted_fraction(rng, 2.0, n)
p = np.exp(-2.0)
assert abs(f - p) < 4 * np.sqrt(p * (1 - p) / n), f
c = interaction_counts(rng, 3.0, 400_000)
assert abs(c.mean() - 3.0) < 0.02, c.mean()
assert abs(c.var() - 3.0) < 0.06, c.var()
print("MC-01 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| transmitted fraction, $\tau_0=2$ | $e^{-2}=0.13534$ |
| mean and variance of interaction count, $\tau=3$ | 3 and 3 |
| solar-centre mean free path (Problem 4) | about 0.0067 cm for the round numbers; 0.0097 cm with the toy Rosseland opacity of MC-10 |

---

## Done when

- You can explain why the exponential law follows from "interaction probability $=d\tau$ per step" and nothing else.
- You can say why the number of interactions is Poisson and why its variance equals its mean.
- You can state what the two limits of Problem 3 mean for a stellar interior and for its surface.
