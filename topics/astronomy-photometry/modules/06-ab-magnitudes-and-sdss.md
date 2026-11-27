# Module 06: AB magnitudes and SDSS transformations

[← 05 Magnitude systems and colour indices](05-magnitude-systems-and-colour-indices.md) · [README](../README.md) · [Next: 07 Bolometric magnitude and correction →](07-bolometric-magnitude-and-correction.md)

**Source:** Karttunen, §4.3, p. 96, eq (4.11).

---

## Session A: read

- Read the AB paragraph and eq (4.11) at the top of p. 96.
- Key ideas:
  - In the **AB system** the zero point is the same for all bands: $F_0=3631$ Jy. So $m_{AB}=-2.5\lg(F_\nu/3631\,{\rm Jy})$.
  - A source with flat $F_\nu$ has all AB colours equal to zero.
  - The SDSS magnitudes **ugriz** are on (approximately) this system.
  - Eq (4.11) gives six linear transformations from ugriz colours to $V$, $R$ and $I$, valid for ordinary stars.
- A derivation worth seeing: in cgs units $3631\,{\rm Jy}=3.631\times10^{-20}$ erg s⁻¹ cm⁻² Hz⁻¹, so
  $m_{AB}=-2.5\lg F_\nu-48.60$ (with $F_\nu$ in cgs). Check that $-2.5\lg(3.631\times10^{-20})=48.60$.

---

## Session B: compute

**Problem 1: AB magnitudes**

- Write `ab_mag(F_nu_jy)` and its inverse `ab_flux_jy(m)`.
- Evaluate for 1 Jy, 1 mJy and 3631 Jy.

**Problem 2: from $F_\lambda$ to AB**

- A source has $F_\lambda=3.6\times10^{-11}$ W m⁻² nm⁻¹ at 550 nm. Convert to $F_\nu$ with $F_\nu=F_\lambda\lambda^2/c$ and then to an AB magnitude.

**Problem 3: implement eq (4.11)**

- Write one function per line of (4.11): $V$ from $(u,g)$ and from $(g,r)$; $R$ from $(g,r)$ and from $(r,i)$; $I$ from $(r,i)$ and from $(i,z)$. Copy the coefficients from p. 96 exactly.
- Test on a star with $(u,g,r,i,z)=(16.0,\,14.8,\,14.3,\,14.1,\,14.0)$.
- The two estimates of each band should agree to a few hundredths of a magnitude.

**Problem 4: a flat-spectrum source**

- Feed $u=g=r=i=z=m$ into the two $V$ lines of (4.11). By how much do they disagree? What does that tell you about where (4.11) may be used?

**Problem 5: sensitivity to colour**

- Plot $V-g$ against $g-r$ from the second line of (4.11). What is the slope?

---

## Checkpoints

| Quantity | Value |
|---|---|
| $m_{AB}$ of 1 Jy | 8.900 |
| $m_{AB}$ of 1 mJy | 16.400 |
| $m_{AB}$ of 3631 Jy | 0 |
| $V$ from $(u,g)$ / from $(g,r)$ | 14.540 / 14.507 |
| $R$ from $(g,r)$ / from $(r,i)$ | 14.111 / 14.097 |
| $I$ from $(r,i)$ / from $(i,z)$ | 13.669 / 13.665 |
| two $V$ lines for a flat spectrum | differ by 0.092 mag |

---

## Done when

- You can explain why a "zero point the same in all bands" system is convenient for surveys.
- You can say why eq (4.11) is stated "for ordinary stars" and not as a universal law.
