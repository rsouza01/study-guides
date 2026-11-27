# Module 21: Wien and Rayleigh–Jeans limits

[← 20 Wien displacement law](20-wien-displacement-law.md) · [README](../README.md) · [Next: 22 Effective temperature →](22-effective-temperature.md)

**Source:** Karttunen, §5.7, p. 113, eqs (5.23)–(5.24); Example 5.4, p. 119; Exercises 5.1 and 5.3, p. 120.

---

## Session A: read

- Read the last paragraphs of §5.7 (p. 113), then Example 5.4 (p. 119).
- Key ideas:
  - With $x=hc/\lambda kT$, near and below the peak ($x\gg1$) one has $e^x-1\approx e^x$: the **Wien approximation** $B_\lambda\approx\dfrac{2hc^2}{\lambda^5}e^{-hc/\lambda kT}$ (5.23).
  - Far above the peak ($x\ll1$) one has $e^x-1\approx x$: the **Rayleigh–Jeans approximation** $B_\lambda\approx\dfrac{2ckT}{\lambda^4}$ (5.24). It is the classical result, and it is useful in radio astronomy.
  - If Rayleigh–Jeans were true at all wavelengths, the intensity would diverge at short wavelengths: the **ultraviolet catastrophe**.

---

## Session B: compute

**Problem 1: Exercise 5.1**

- Show analytically that in the Wien approximation the relative error of $B_\lambda$ is $\Delta B_\lambda/B_\lambda=-e^{-hc/\lambda kT}$.
- Define the relative error of Rayleigh–Jeans similarly and derive it: $(e^x-1)/x-1$.

**Problem 2: error curves**

- Plot both relative errors against $x$ on a log axis from $x=0.01$ to 10.
- Find the $x$ at which each approximation is off by 1 % and by 10 %.

**Problem 3: what does that mean for the Sun?**

- For $T=5772$ K convert the 1 % limits into wavelengths. At what wavelengths are Wien and Rayleigh–Jeans each good to 1 %?

**Problem 4: Example 5.4 (radio from a lamp)**

- (a) Show that the fraction of blackbody radiation emitted at wavelengths above $\lambda_1$ (with $\lambda_1\gg\lambda_{\max}$) is, in the Rayleigh–Jeans approximation, $\dfrac{5c^3h^3}{\pi^4k^3T^3}\,\dfrac{1}{\lambda_1^3}$.
- (b) A 100 W bulb has $T=2500$ K. How much power does it radiate at $\lambda\ge1$ cm? Compare with the exact Planck integral.

**Problem 5: Exercise 5.3 (the cosmic background)**

- The background radiation is a blackbody at 2.7 K. Find $\lambda_{\max}$ and the total intensity.
- Compare with the Sun's intensity in the visual band, 400–700 nm (one reasonable reading of "at visual wavelengths").

**Problem 6: the catastrophe**

- Integrate the Rayleigh–Jeans $B_\lambda$ from $\lambda_{\min}$ to infinity. Show how it grows as $\lambda_{\min}\to0$.

---

## Checkpoints

| Quantity | Value |
|---|---|
| Rayleigh–Jeans error, $x=0.02$ / 0.1 / 0.2 / 1 | +1.0 % / +5.2 % / +10.7 % / +71.8 % |
| Wien error, $x=2.30$ / 4.61 | −10 % / −1 % |
| RJ off by 1 % at | $x=0.01987$ |
| RJ off by 10 % at | $x=0.1877$ |
| Sun (5772 K): RJ within 1 % for | $\lambda\gtrsim125\ \mu{\rm m}$ |
| Sun (5772 K): Wien within 1 % for | $\lambda\lesssim541$ nm |
| Example 5.4 fraction ($\ge1$ cm, 2500 K), RJ | $9.784\times10^{-12}$ |
| same, exact Planck | $9.782\times10^{-12}$ |
| power in the radio from a 100 W bulb | $9.8\times10^{-10}$ W |
| background: $\lambda_{\max}$ | 1.073 mm |
| background: total intensity $\sigma T^4/\pi$ | $9.59\times10^{-7}$ W m⁻² sr⁻¹ |
| Sun, 400–700 nm | $7.34\times10^{6}$ W m⁻² sr⁻¹ |
| ratio background / Sun | $1.3\times10^{-13}$ |

---

## Done when

- You can derive both limits and the error of each from the Planck function.
- You can say which regime applies to a star's visual light, to a bulb's radio emission, and to the cosmic background at 1 mm.
- You can explain what the ultraviolet catastrophe was and what resolved it.
