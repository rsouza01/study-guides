# Module 05: Magnitude systems and colour indices

[← 04 Apparent magnitudes](04-apparent-magnitudes.md) · [README](../README.md) · [Next: 06 AB magnitudes and SDSS transformations →](06-ab-magnitudes-and-sdss.md)

**Source:** Karttunen, §4.3, pp. 94–96, Table 4.1, Fig. 4.6.

---

## Session A: read

- Read §4.3 from its start (p. 94) to the start of §4.4 (p. 96), skipping eq (4.10) and the AB paragraph for now (Modules 06 and 07).
- Key ideas:
  - An apparent magnitude depends on the **detector and its passband**. Different systems have different zero points $F_0$.
  - Names: visual $m_v$ (eye), photographic $m_{pg}$, photovisual $m_{pv}$, bolometric $m_{bol}$.
  - **UBV** (Johnson and Morgan, 1950s), extended to **UBVRI**. **Strömgren uvby** uses narrower bands. Table 4.1 gives band widths and effective wavelengths.
  - A **colour index** is the difference of two magnitudes, for example $B-V$ and $U-B$.
  - The $F_0$ values are chosen so that $B-V=U-B=0$ for A0 stars (about 10,000 K). Vega: $V=0.04$, $B-V=0$. Sun: $V=-26.8$, $B-V=0.64$, $U-B=0.12$.
  - Older colour index: C.I. $=m_{pg}-m_v=(B-V)-0.11$.

---

## Session B: compute (a toy synthetic photometer)

You will build a simple model. It is not the real UBV system. The goal is to see where colours come from.

**Problem 1: filters**

- Model each passband as a Gaussian in wavelength, centred on the effective wavelength of Table 4.1, with FWHM equal to the band width in the table. Use U, B, V, R and I.

**Problem 2: synthetic magnitudes of a blackbody**

- For a blackbody of temperature $T$, the signal in band $b$ is $f_b(T)=\int B_\lambda(T)\,S_b(\lambda)\,d\lambda$.
- Define $m_b(T)=-2.5\lg f_b(T)+C_b$, with $C_b$ chosen so that $m_b=0$ at $T=10{,}000$ K for **every** band. That is the book's A0 convention.

**Problem 3: colours of blackbodies**

- Compute $B-V$, $U-B$ and $V-R$ for $T=3500,\,5772,\,10{,}000,\,30{,}000$ K.

**Problem 4: curves**

- Plot $B-V$ against $\log_{10}T$. Is it monotonic?
- Plot $U-B$ against $B-V$ (a two-colour diagram) for $T=3000$–$30{,}000$ K.

**Problem 5: compare with the Sun**

- The book gives $B-V=0.64$ and $U-B=0.12$ for the Sun. Compare with your 5772 K blackbody and list reasons for the differences.

**Problem 6: the old colour index**

- Write `ci_from_bv(bv)` for C.I. $=(B-V)-0.11$ and convert the Sun and Vega.

---

## Checkpoints

Toy model as defined above (Gaussian filters, FWHM = band width):

| $T$ (K) | $B-V$ | $U-B$ | $V-R$ |
|---|---|---|---|
| 3500 | 1.25 | 1.19 | 0.70 |
| 5772 | 0.50 | 0.46 | 0.26 |
| 10,000 | 0.00 | 0.00 | 0.00 |
| 30,000 | −0.41 | −0.36 | −0.19 |

- For the Sun the book has $B-V=0.64$, $U-B=0.12$. Your blackbody gives 0.50 and 0.46: it is too blue in $B-V$, and far too red in $U-B$.
- C.I. of the Sun: $0.64-0.11=0.53$. Vega: $-0.11$.

---

## Done when

- You can explain where a colour index comes from physically: the ratio of fluxes in two bands.
- You can explain why hotter stars have more negative $B-V$.
- You can name two reasons a real star's colours differ from a blackbody's (hint: look at what happens near 365 nm in a stellar spectrum, and at the filter shapes).
