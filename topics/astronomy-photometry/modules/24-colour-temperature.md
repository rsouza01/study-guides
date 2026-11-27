# Module 24: Colour temperature

[← 23 Brightness and antenna temperature](23-brightness-and-antenna-temperature.md) · [README](../README.md) · [Next: 25 Kinetic, excitation and ionisation temperatures →](25-kinetic-excitation-ionisation.md)

**Source:** Karttunen, §5.8, pp. 115–116, eq (5.31); Example 5.6, p. 120; Exercise 5.7, p. 120.

---

## Session A: read

- Read the colour-temperature paragraph of §5.8 (pp. 115–116), then Example 5.6.
- Key ideas:
  - The **colour temperature** $T_c$ is the temperature of the blackbody whose *shape* of spectrum, between two wavelengths, matches the star's. Only the ratio of flux densities matters, not their absolute level.
  - For two wavelengths: $\dfrac{F_1}{F_2}=\dfrac{B_{\lambda_1}(T_c)}{B_{\lambda_2}(T_c)}$.
  - It is closely tied to the colour index: a hotter star is bluer, so $B-V$ (or $U-B$) maps to $T_c$.
  - For a real star, $T_c$ differs from $T_e$ and depends on which wavelength pair you choose.

---

## Session B: compute

**Problem 1: Example 5.6**

- Two flux densities are observed at $\lambda_1$ and $\lambda_2$. Solve $F_1/F_2=B_{\lambda_1}(T_c)/B_{\lambda_2}(T_c)$ for $T_c$ with a root finder.
- Use the book's data. Check your answer against the checkpoint: the book prints 7545 K, but a careful solution gives a different value (see below).

**Problem 2: Exercise 5.7 (colour index to temperature)**

- Use the approximation $B-V=a+b/T_c$. From two calibrations, find $a$ and $b$ so that $B-V=0$ at 15,000 K and $B-V=0.64$ at 5800 K. Then solve for $T_c$ as a function of $B-V$.

**Problem 3: how good is the formula?**

- Compute exact $B-V$ for blackbodies (same effective wavelengths, $B-V=0$ at 15,000 K) and invert with the formula. Tabulate the error.

**Problem 4: a non-blackbody star**

- Take $S(\lambda)=0.7\,\tilde B(4000\ {\rm K})+0.3\,\tilde B(12{,}000\ {\rm K})$, each normalised to 1 at 500 nm. Compute $T_c$ for the pairs (400, 450), (450, 550), (550, 700), (700, 1000) nm.
- What does the spread say about quoting a single colour temperature?

---

## Checkpoints

| Quantity | Value |
|---|---|
| Example 5.6, correct $T_c$ | 7855 K (the book: 7545 K, a misprint) |
| the book's 7545 K gives $F_1/F_2$ | 1.259 (inconsistent with the data) |
| Exercise 5.7: $b$ | 6997 K |
| Exercise 5.7: $a$ | −0.4665 |
| result | $T_c\approx7000/(B-V+0.47)$ |

| $B-V$ | formula | exact Planck |
|---|---|---|
| 0 | 14,894 K | 15,000 K |
| 0.3 | 9091 K | 8579 K |
| 0.64 | 6306 K | 5957 K |
| 1.0 | 4762 K | 4541 K |
| 1.5 | 3553 K | 3425 K |
| −0.2 | 25,926 K | 37,602 K |

| Pair (nm) | $T_c$ of the two-component star |
|---|---|
| 400, 450 | 5905 K |
| 450, 550 | 5003 K |
| 550, 700 | 4440 K |
| 700, 1000 | 4186 K |

---

## Done when

- You can explain why $T_c$ is insensitive to distance and absolute calibration.
- You can say why a star has no unique colour temperature.
- You can say where the $B-V$ formula works and where it fails, from your table.
