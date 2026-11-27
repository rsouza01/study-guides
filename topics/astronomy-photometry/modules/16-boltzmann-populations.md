# Module 16: Boltzmann populations

[← 15 Quantum numbers and selection rules](15-quantum-numbers-and-selection-rules.md) · [README](../README.md) · [Next: 17 From lines to continuum →](17-lines-to-continuum.md)

**Source:** Karttunen, §5.4, p. 110 ("Population Numbers"), eq (5.11).

---

## Session A: read

- Read the "Population Numbers" paragraph on p. 110.
- Key ideas:
  - The **population number** $n_i$ is the number of atoms per unit volume in state $i$.
  - In thermal equilibrium, the **Boltzmann distribution** holds:
    $$\frac{n_i}{n_0}=\frac{g_i}{g_0}\,e^{-\Delta E/kT},\qquad\Delta E=E_i-E_0 .$$
  - $g_i$ is the **statistical weight**: the number of distinct states with energy $E_i$.
  - If the populations are not Boltzmann, one can still define an **excitation temperature** $T_{\rm exc}$ by inserting it in (5.11). It can differ from level to level.
- A worked check: hydrogen levels have $g_n=2n^2$, so $g_2/g_1=8/2=4$. The $n=2$ level lies 10.2 eV above the ground state.

---

## Session B: compute

**Problem 1: hydrogen $n=2$ relative to $n=1$**

- Compute $n_2/n_1=4e^{-10.2\,{\rm eV}/kT}$ at $T=5772$ K, $10^4$ K and $2\times10^4$ K.

**Problem 2: excitation temperature from a measured ratio**

- Invert (5.11): $T_{\rm exc}=\Delta E\big/\big[k\ln\!\big(g_ i\,n_0/(g_0\,n_i)\big)\big]$.
- Find $T_{\rm exc}$ for observed ratios $n_2/n_1=10^{-3},\,10^{-5},\,10^{-7}$.

**Problem 3: the 21 cm levels**

- The two spin states have $g=3$ (parallel) and $g=1$ (antiparallel) and an energy difference of $5.874\times10^{-6}$ eV.
- Compute the equivalent temperature $\Delta E/k$, and the population ratio at $T=100$ K.

**Problem 4: a sensitivity study**

- Plot $n_2/n_1$ against $T$ from 3000 to 30,000 K on a log scale. Over what range of $T$ does it change by a factor $10^{6}$? What does this say about using a hydrogen line as a thermometer?

---

## Checkpoints

| $T$ | $n_2/n_1$ |
|---|---|
| 5772 K | $4.97\times10^{-9}$ |
| 10,000 K | $2.89\times10^{-5}$ |
| 20,000 K | $1.08\times10^{-2}$ |

| Observed $n_2/n_1$ | $T_{\rm exc}$ |
|---|---|
| $10^{-3}$ | 14,271 K |
| $10^{-5}$ | 9176 K |
| $10^{-7}$ | 6762 K |

| Quantity | Value |
|---|---|
| 21 cm equivalent temperature | 0.0681 K |
| population ratio $n_{\rm upper}/n_{\rm lower}$ at 100 K | 2.998 (→ 3) |

---

## Done when

- You can explain why a tiny fraction of hydrogen atoms in $n=2$ nevertheless produces strong Balmer absorption lines in stars.
- You can explain what changes about the ratio when the temperature is far above the level spacing, and why it then approaches $g_i/g_0$.
