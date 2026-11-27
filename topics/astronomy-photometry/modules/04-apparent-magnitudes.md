# Module 04: Apparent magnitudes

[← 03 Surface brightness and energy density](03-surface-brightness-and-energy-density.md) · [README](../README.md) · [Next: 05 Magnitude systems and colour indices →](05-magnitude-systems-and-colour-indices.md)

**Source:** Karttunen, §4.2, pp. 93–94, eqs (4.8)–(4.9); Example 4.3, p. 100; Exercise 4.1, p. 101.

---

## Session A: read

- Read §4.2 (pp. 93–94) and Example 4.3 (p. 100).
- Key ideas:
  - Hipparchos sorted stars into six brightness classes. Human brightness perception is roughly logarithmic.
  - Pogson (1856) fixed the ratio of brightness between successive classes at $\sqrt[5]{100}=2.5119$.
  - The magnitude is defined from the flux density: $m=-2.5\lg(F/F_0)$ (4.8). The coefficient is exactly 2.5, not 2.512.
  - Two stars: $m_1-m_2=-2.5\lg(F_1/F_2)$ (4.9).
  - Magnitudes are logarithmic, so **they cannot be added**. Add the flux densities and convert back.
- Derivation (that 4.8 is Pogson's rule):
  1. For magnitudes $m$ and $m+1$: $m-(m+1)=-2.5\lg(F_m/F_0)+2.5\lg(F_{m+1}/F_0)=-2.5\lg(F_m/F_{m+1})$.
  2. The left side is $-1$, so $\lg(F_m/F_{m+1})=0.4$.
  3. Hence $F_m/F_{m+1}=10^{0.4}=\sqrt[5]{100}$.

---

## Session B: compute

**Problem 1: the basic converters**

- Write `flux_ratio(dm)` $=10^{0.4\,\Delta m}$ and `mag_diff(F1_over_F2)`.
- Tabulate flux ratios for $\Delta m=1,\dots,10$. Check that 5 mag is exactly a factor 100.

**Problem 2: how bad is 2.512?**

- Compare $2.512^{\Delta m}$ with $10^{0.4\Delta m}$ for $\Delta m=10,20,30$. Give the relative error as a percentage.

**Problem 3: Sun versus full Moon**

- Using $m_\odot=-26.8$ and $m_{\rm Moon}=-12.5$, how many times brighter is the Sun?

**Problem 4: adding magnitudes (Example 4.3)**

- Write `total_mag(list_of_mags)`.
- Verify the binary-star example: components of magnitudes 1 and 2 give a total of 0.64, not 3.

**Problem 5: Exercise 4.1**

- The total magnitude of a triple star is 0.0. Two components have magnitudes 1.0 and 2.0. Find the magnitude of the third.

<details>
<summary>Answer to Problem 5</summary>

The third component has magnitude 0.88.

</details>

**Problem 6: photometric errors**

- Show that a fractional flux error $\delta F/F$ gives $\delta m=1.0857\,\delta F/F$.
- What magnitude error corresponds to a 1 % flux error?

---

## Checkpoints

| Quantity | Value |
|---|---|
| $\sqrt[5]{100}$ | 2.51189 |
| $2.512^5$ | 100.023 |
| error of using 2.512 | 0.045 % (10 mag), 0.09 % (20 mag), 0.14 % (30 mag) |
| Sun / full Moon flux ratio | $5.25\times10^{5}$ |
| total of $m=1$ and $m=2$ | 0.636 |
| 1 % flux error | 0.0109 mag |

---

## Done when

- You can derive Pogson's ratio from (4.8) without looking.
- You can say why the magnitude of a binary is brighter than both components but nowhere near their sum.
- You know that "the coefficient is exactly 2.5" is the definition and 2.512 is a consequence.
