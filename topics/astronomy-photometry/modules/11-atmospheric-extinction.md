# Module 11: Atmospheric extinction and air mass

[← 10 Colour excess and reddening](10-colour-excess-and-reddening.md) · [README](../README.md) · [Next: 12 Photons and energy levels →](12-photons-and-energy-levels.md)

**Source:** Karttunen, §4.5, pp. 98–99, eqs (4.23)–(4.24), Fig. 4.9; Example 4.8, p. 101.

---

## Session A: read

- Read "Atmospheric Extinction" (pp. 98–99) and Example 4.8 (p. 101).
- Key ideas:
  - Observations must be **reduced** to remove the atmosphere before they are compared.
  - In a plane-parallel atmosphere the light path grows as $X=\sec z$, the **air mass** (4.23), where $z$ is the zenith distance.
  - Magnitude then grows linearly with air mass: $m=m_0+kX$ (4.24), with extinction coefficient $k$ and out-of-atmosphere magnitude $m_0$.
  - Observe the same star over a wide range of $z$, plot $m$ against $X$, and fit a line. Its slope is $k$ and its intercept at $X=0$ is $m_0$.
  - Do not use $z>70^\circ$ (altitude below 20°): the curvature of the atmosphere spoils the plane-parallel model. $k$ depends on place, time and wavelength; it is larger in the blue.
- Derivation of $X=\sec z$: the vertical thickness is $H$, and a ray at angle $z$ crosses it along a path $H/\cos z$.

---

## Session B: compute

**Problem 1: air mass table**

- Compute $X=\sec z$ for altitudes 50°, 35°, 25°, 20°.

**Problem 2: Example 4.8 by least squares**

- Measurements of one star during a night:

| Altitude | 50° | 35° | 25° | 20° |
|---|---|---|---|---|
| Magnitude | 0.90 | 0.98 | 1.07 | 1.17 |

- Fit $m=m_0+kX$ by solving the normal equations yourself (no `polyfit`). Report $m_0$ and $k$.
- Compute the residuals and an estimate of the uncertainty of $k$.

**Problem 3: how good is $\sec z$?**

- A better empirical air-mass formula (Kasten and Young, 1989; this is beyond the book) is
  $$X=\frac{1}{\cos z+0.50572\,(96.07995^\circ-z)^{-1.6364}},$$
  with $z$ in degrees.
- Compare it with $\sec z$ at $z=40^\circ,\,55^\circ,\,65^\circ,\,70^\circ,\,80^\circ,\,88^\circ$.

**Problem 4: simulate a night**

- Choose $m_0=10.0$ and $k=0.25$. Generate 30 observations at random zenith distances in $[0^\circ,70^\circ]$ with 0.01 mag Gaussian noise. Fit and compare. Repeat 1000 times and look at the scatter of the recovered $k$.
- Repeat with observations only in $[0^\circ,30^\circ]$. What happens to the error on $k$? Why?

---

## Checkpoints

| Altitude | $z$ | $\sec z$ | the book |
|---|---|---|---|
| 50° | 40° | 1.3054 | 1.31 |
| 35° | 55° | 1.7434 | 1.74 |
| 25° | 65° | 2.3662 | 2.37 |
| 20° | 70° | 2.9238 | 2.92 |

| Quantity | Value |
|---|---|
| fit: $m_0$ | 0.687 (the book, graphically: 0.68) |
| fit: $k$ | 0.164 (the book: 0.17) |

| $z$ | $\sec z$ | Kasten–Young |
|---|---|---|
| 70° | 2.924 | 2.903 |
| 80° | 5.759 | 5.586 |
| 88° | 28.65 | 19.43 |

---

## Done when

- You can explain why the intercept at $X=0$ is the magnitude outside the atmosphere.
- You can explain, from Problems 3 and 4, why the book excludes low altitudes and why a wide range of $z$ gives a better $k$.
