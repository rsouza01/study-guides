# Module 10: Colour excess and reddening

[← 09 Interstellar extinction](09-interstellar-extinction.md) · [README](../README.md) · [Next: 11 Atmospheric extinction and air mass →](11-atmospheric-extinction.md)

**Source:** Karttunen, §4.5, p. 98 ("Colour Excess"), eqs (4.20)–(4.22); Exercise 4.4, p. 102.

---

## Session A: read

- Read the "Colour Excess" paragraphs on p. 98.
- Key ideas:
  - Dust scatters and absorbs blue light more than red, so stars look **redder**: $B-V$ increases.
  - $V=M_V+5\lg(r/10\,{\rm pc})+A_V$ (4.20), and similarly for $B$.
  - The observed colour is $B-V=(B-V)_0+E_{B-V}$ (4.21), with intrinsic colour $(B-V)_0=M_B-M_V$ and **colour excess** $E_{B-V}=A_B-A_V$.
  - The ratio $R=A_V/E_{B-V}$ is nearly constant, about 3.0, so $A_V\approx3.0\,E_{B-V}$ (4.22).
- Derivation of (4.21):
  1. Subtract the equation for $V$ from the one for $B$.
  2. The distance terms cancel: $B-V=M_B-M_V+A_B-A_V$.
  3. The right side is intrinsic colour plus colour excess.

---

## Session B: compute

**Problem 1: Exercise 4.4**

- A star has $V=15.1$, $B-V=1.6$, $M_V=1.3$. The extinction in the direction of the star in the visual band is $a_V=1$ mag kpc⁻¹.
- Find the distance, then $A_V$, then $E_{B-V}$ using $R=3.0$, and finally the intrinsic colour.

<details>
<summary>Answer</summary>

Distance about 2144 pc, $A_V=2.14$, $E_{B-V}=0.71$, intrinsic $B-V=0.89$.

</details>

**Problem 2: what if you ignore extinction?**

- For the same star, compute the distance as if there were no extinction. By what factor does it overestimate?
- Show analytically that the factor is $10^{A_V/5}$.

**Problem 3: a power-law extinction curve (a toy)**

- Suppose $A_\lambda\propto\lambda^{-p}$. With the effective wavelengths of Table 4.1 ($\lambda_B=436$ nm, $\lambda_V=545$ nm), find $p$ such that $R=A_V/E_{B-V}=3.0$.
- With that $p$, what is $A_U/A_V$ at 367 nm?
- Comment on how realistic a single power law is.

**Problem 4: a reddening vector**

- Generate 500 stars with intrinsic $(B-V)_0$ drawn from a normal distribution with mean 0.6 and σ 0.3, and $M_V$ with mean 3 and σ 1, all at 500 pc.
- Apply $A_V=3.0\,E$ with $E=0.5$. Plot the colour–magnitude diagram before and after, and check that the shift is $(+0.5,\,+1.5)$ in $(B-V,\,V)$.

---

## Checkpoints

| Quantity | Value |
|---|---|
| Exercise 4.4 distance | 2144 pc |
| $A_V$ | 2.14 mag |
| $E_{B-V}$ | 0.715 |
| intrinsic $(B-V)_0$ | 0.885 |
| naive distance, no extinction | 5754 pc ($\times2.7$ too large) |
| power-law index $p$ for $R=3.0$ | 1.289 |
| $A_U/A_V$ for that $p$ | 1.67 |
| reddening vector for $E=0.5$ | $(+0.5,\ +1.5)$ |

---

## Done when

- You can derive $B-V=(B-V)_0+E_{B-V}$ and explain why the distance terms cancel.
- You can say how a measured colour excess lets you correct a distance, step by step.
