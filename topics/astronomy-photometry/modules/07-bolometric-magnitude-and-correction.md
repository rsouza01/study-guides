# Module 07: Bolometric magnitude and correction

[← 06 AB magnitudes and SDSS transformations](06-ab-magnitudes-and-sdss.md) · [README](../README.md) · [Next: 08 Absolute magnitude and distance modulus →](08-absolute-magnitude-and-distance-modulus.md)

**Source:** Karttunen, §4.3, p. 95, eq (4.10); §4.4, p. 97, eq (4.14).

---

## Session A: read

- Read the bolometric paragraphs on p. 95 (eq 4.10) and the end of §4.4 on p. 97 (eq 4.14 and the sentence that follows it).
- Key ideas:
  - The **bolometric magnitude** $m_{bol}$ would be measured over all wavelengths.
  - $m_{bol}=m_v-{\rm BC}$ (4.10). The bolometric correction BC is zero by definition for solar-type stars (precisely, class F5). The book's convention gives ${\rm BC}\ge0$; some authors use $m_{bol}=m_v+{\rm BC}$ with ${\rm BC}\le0$.
  - The correction is positive for stars both hotter and cooler than the Sun, because the visual band then captures a smaller fraction of the total flux.
  - The bolometric flux density is always larger than the visual one, even when the magnitudes are equal. The reason is the different zero points $F_0$.
  - $M_{bol}-M_{bol,\odot}=-2.5\lg(L/L_\odot)$ (4.14), and $M_{bol}=0$ corresponds to $L_0=3.0\times10^{28}$ W.

---

## Session B: compute

**Problem 1: luminosity and bolometric magnitude**

- Write `mbol_from_L(L)` and `L_from_mbol(M)` using $L_0=3.0128\times10^{28}$ W.
- Compute $M_{bol,\odot}$. Repeat with the book's $L_0=3.0\times10^{28}$ W.

**Problem 2: the two sign conventions**

- Write `mbol(mv, bc, convention)`. For a star with $m_v=5.0$ and BC magnitude 0.5, give both conventions.

**Problem 3: a toy bolometric correction**

- Use the toy V filter and blackbody from Module 05.
- Define $\mathrm{BC}(T)=2.5\lg\big[F_{\rm bol}(T)/f_V(T)\big]-K$, with $F_{\rm bol}=\sigma T^4/\pi$ and $K$ chosen as the minimum of the first term over $T=3000$–$30{,}000$ K.
- Compute BC at several temperatures and find the temperature of the minimum.

**Problem 4: why is the minimum there? (on paper)**

- In the monochromatic approximation at $\lambda_V=545$ nm, the in-band fraction is proportional to $g(T)=1/\big[T^4(e^{x}-1)\big]$ with $x=hc/\lambda kT$.
- Show that its maximum satisfies $x\,e^x/(e^x-1)=4$. Solve numerically for $x$ and then $T$.

**Problem 5: the fraction in the band**

- Compute the fraction of the Sun's bolometric flux that passes through your toy V filter at 5772 K, and explain why $F_{\rm bol}>F_V$ even when $m_{bol}=m_V$.

---

## Checkpoints

| Quantity | Value |
|---|---|
| $M_{bol,\odot}$ ($L_0=3.0128\times10^{28}$ W) | 4.740 |
| $M_{bol,\odot}$ ($L_0=3.0\times10^{28}$ W) | 4.735 (the book uses 4.7) |
| position of the BC minimum (toy) | about 6800 K |
| solution of $xe^x/(e^x-1)=4$ | $x\approx3.92$ |
| the corresponding $T$ at 545 nm | about 6700 K |

Toy BC, with $K$ at the minimum:

| $T$ (K) | BC |
|---|---|
| 3000 | 1.80 |
| 4000 | 0.68 |
| 5772 | 0.06 |
| 6500 | 0.00 |
| 8000 | 0.05 |
| 10,000 | 0.25 |
| 20,000 | 1.55 |
| 30,000 | 2.58 |

---

## Done when

- Your BC curve is non-negative on both sides of a minimum near 6500–6800 K, as the book states, and you can explain why.
- You can explain what "the zero points differ" means for the bolometric and visual flux densities.
