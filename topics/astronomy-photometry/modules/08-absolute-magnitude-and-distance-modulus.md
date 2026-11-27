# Module 08: Absolute magnitude and distance modulus

[← 07 Bolometric magnitude and correction](07-bolometric-magnitude-and-correction.md) · [README](../README.md) · [Next: 09 Interstellar extinction →](09-interstellar-extinction.md)

**Source:** Karttunen, §4.4, pp. 96–97, eqs (4.12)–(4.14), Fig. 4.7; Examples 4.4 and 4.5, pp. 100–101; Exercises 4.2 and 4.3, pp. 101–102.

---

## Session A: read

- Read §4.4 (pp. 96–97) and Examples 4.4, 4.5 (pp. 100–101).
- Key ideas:
  - The **absolute magnitude** $M$ is the apparent magnitude the star would have at 10 pc (IAU, 1922).
  - The **distance modulus** is $m-M=5\lg(r/10\,{\rm pc})$ (4.12).
  - Eq (4.13), $m-M=5\lg r-5$, holds only for $r$ in **parsecs**. The book recommends (4.12).
  - Capital letters: $U$, $B$, $V$ are apparent magnitudes; the absolute ones are $M_U$, $M_B$, $M_V$.
- Derivation of (4.12):
  1. The flux density from a star goes as $1/r^2$, so $F(r)/F(10)=(10\,{\rm pc}/r)^2$.
  2. $m-M=-2.5\lg[F(r)/F(10)]=-2.5\lg(10\,{\rm pc}/r)^2$.
  3. This is $5\lg(r/10\,{\rm pc})$.

---

## Session B: compute

**Problem 1: converters**

- Write `dist_modulus(r_pc)` and `distance_pc(mu)`.
- Verify the table of checkpoints below, including the unit trap: for $r$ in kpc the constant in (4.13) changes. Find it.

**Problem 2: Examples 4.4 and 4.5**

- A star at 100 pc has $m=6$. Find $M$.
- A star has $M=-2$ and $m=8$. Find $r$.

**Problem 3: Exercise 4.2 (a supernova in Andromeda)**

- A star in the Andromeda galaxy (690 kpc) has $M=5$. It explodes and becomes $10^9$ times brighter. What is its apparent magnitude?

<details>
<summary>Answer</summary>

Before the explosion $m=29.19$; after it, $m=6.69$.

</details>

**Problem 4: Exercise 4.3 (star counts) by simulation**

- Assume all stars have the same absolute magnitude and are uniformly distributed in space.
- Draw $4\times10^6$ stars uniformly in a sphere of radius 1000 pc ($M=0$), compute their apparent magnitudes, and count $N(<m)$ for $m=4,5,\dots,9$.
- Compute $N(m+1)/N(m)$. Compare with the value you derive analytically.

<details>
<summary>Hint</summary>

Stars brighter than $m$ lie within a radius $r_m$ with $m-M=5\lg(r_m/10\,{\rm pc})$, and $N\propto r_m^3$. Take care that $r_m$ stays inside your sphere.

</details>

**Problem 5: absolute bolometric magnitude from luminosity (4.14)**

- A star has $L=100\,L_\odot$. Find $M_{bol}$ using $M_{bol,\odot}=4.74$.

---

## Checkpoints

| $r$ | $m-M$ |
|---|---|
| 10 pc | 0 |
| 100 pc | 5 |
| 1 kpc | 10 |
| 10 kpc | 15 |
| 690 kpc | 19.19 |
| 1 Mpc | 25 |

| Quantity | Value |
|---|---|
| Example 4.4: $M$ | 1.0 |
| Example 4.5: $r$ | 1000 pc |
| constant in $m-M=5\lg r_{\rm kpc}+{\rm const}$ | +10 |
| Exercise 4.3, analytic ratio | $10^{0.6}=3.98$ |
| Exercise 4.3, simulation | 3.9–4.0 (about 3 % noise) |
| $M_{bol}$ for $100\,L_\odot$ | −0.26 |

---

## Done when

- You can derive $m-M=5\lg(r/10\,{\rm pc})$ from the inverse-square law.
- You can explain why the star-count ratio is $10^{0.6}$, and what a lower observed ratio at faint magnitudes would tell you about the stellar distribution.
