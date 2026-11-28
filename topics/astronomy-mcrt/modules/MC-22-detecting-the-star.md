# Module MC-22: Detecting the star at a distance

[← MC-21](MC-21-spectrum-and-balmer-lines.md) · [README](../README.md) · [Next: MC-23 The inverse problem →](MC-23-inverse-problem.md)

**Source:** Forgan §6.1 (binning escaping packets, wavelength and direction), §6.2 (eqs 51–52, flux normalisation) and §7 (eq 53, Poisson errors), pp. 15–16. Photometry: PH-04 (apparent magnitudes), PH-05 (magnitude systems, colour indices, the toy Gaussian filters), PH-07 (bolometric magnitude), PH-08 (distance modulus), PH-24 (colour temperature).

---

## Session A: read

- Forgan §6 and §7 again, with MC-07 and MC-08 open.
- PH-05 for the five toy filters and the colour-index zero point.
- Optional: Bessell (2005), *Standard photometric systems*, ARA&A 43, 293, for how real zero points are defined (Vega, AB, ST).

**Key ideas**

- The star is a **point source**. All the packets that matter are those leaving towards the observer. For a spherical star the answer is exact without any packet: $F_\lambda^{\rm obs}=F_\lambda^{\rm surf}(R/d)^2$. Monte Carlo packets are the right tool when the object is **not** spherically symmetric (spots, discs, a companion). The spherical case is the calibration.
- Two kinds of noise must not be confused:
  - **Monte Carlo noise** from the number of packets you chose (eq 53): relative error $1/\sqrt n$ on a bin with $n$ packets;
  - **Photon-counting noise** of the real detector: relative error $1/\sqrt{N_{\rm ph}}$ with $N_{\rm ph}$ the real photon count.
  The simulation should be run with enough packets that the first is below the second, or the "observation" is limited by your code.
- Magnitudes and colours are ratios, so they do not depend on the flux scale (distance, area), only on the spectral shape.

**Derivation to see once: from packets to a band count**

- Packets carry equal energy $E_\gamma$ and are drawn with wavelength density $p(\lambda)=F_\lambda/\int F_\lambda d\lambda$ (equal-energy sampling, MC-03/MC-02).
- A band with response $S(\lambda)$ collects, in expectation, the fraction $\int pS\,d\lambda$ of the packets, weighted by $S$.
- The expected number of real photons: $N_{\rm ph}=A\,t\int F_\lambda S(\lambda)\dfrac{\lambda}{hc}d\lambda$. The factor $\lambda/hc$ turns energy into photon number (one photon of energy $hc/\lambda$).
- Check on the scale: a $V=0$ star gives about $9\times10^{9}$ photons s⁻¹ m⁻². The Sun at 10 pc ($V=4.83$) gives $9\times10^9\times10^{-0.4\times4.83}=1.05\times10^8$, in line with the $1.07\times10^8$ you will compute with the toy filter.

---

## Session B: do

**Problem 1: the filters and colours**

- Implement `response(lam_nm, band)` for the five Gaussian filters ($U,B,V,R,I$: centre, FWHM in nm: 365/66, 440/98, 550/89, 700/220, 900/240) and `inst_mag(lam, F, band)`, the instrumental magnitude $-2.5\log_{10}\int F_\lambda S\,d\lambda$.
- Implement `colour(lam, F, F_ref, b1, b2)` with the reference spectrum a 10000 K blackbody (toy "Vega"). Compute $B-V$, $U-B$, $V-R$ for blackbodies of 3500, 5772, 10000, 30000 K.

**Problem 2: photon counts**

- Using `detector.photon_counts`, compute the photon rate through the $V$ filter for a 5772 K blackbody of radius $R_\odot$ at 10 pc, with $A=1$ m², $t=1$ s. Do the same for $B$. Report the photon-counting relative error for 1 s and for $10^{-3}$ s.

**Problem 3: equal-energy packets**

- Implement `sample_wavelengths(rng, lam, F_lam, n)`. Draw $2\times10^5$ packets from a 5772 K blackbody. Check that the mean wavelength equals the energy-weighted mean and that the fraction in 520–580 nm equals the integral.
- Implement `band_packet_fraction(samples, lo, hi)`.

**Problem 4: how many packets do you need?**

- You want the $V$ band to have Monte Carlo noise equal to the real photon-counting noise of a $1\ {\rm m^2}$, 1 s observation. Use `packets_needed` (MC-08) with the packet fraction in the band. Is it feasible? What does that tell you about when to use packets and when to use the analytic dilution factor?

---

## Translation: text → code

| Forgan | Meaning | Code |
|---|---|---|
| §6.1 | bin escaping packets in $\lambda$ | `np.histogram(samples, bins=...)` |
| eq (51) | $E_\gamma=L\Delta t/N_{\rm tot}$ | energy per packet |
| eq (52) | **misprint** (MC-07) | $F=(L/N)\,n/(\Delta\Omega\,d^2)$ |
| eq (53) | $\sigma=E_\gamma\sqrt N$ | `poisson_sigma` |
| PH-05 | Gaussian filters | `response` |

---

## Contract

```text
starmc/photometry.py
  FILTERS = {"U": (365,66), "B": (440,98), "V": (550,89), "R": (700,220), "I": (900,240)}
  response(lam_nm, band)                     exp(-0.5 ((lam-l0)/sigma)^2), sigma = FWHM/(2 sqrt(2 ln 2))
  planck_lambda(lam_nm, T)                   cgs, per cm
  inst_mag(lam_nm, F_lam, band)              -2.5 log10( trapz(F S, lam) )
  colour(lam_nm, F_lam, F_ref, b1, b2)       (m_b1 - m_b1,ref) - (m_b2 - m_b2,ref)
  sample_wavelengths(rng, lam_nm, F_lam, n)  density proportional to F_lam
  band_packet_fraction(samples, lo_nm, hi_nm)
starmc/detector.py
  photon_counts(F_lam, lam_m, S, area_m2, t_s)   F in W m^-2 m^-1, lam in m
```

```python
# acceptance-test
import numpy as np
from starmc.photometry import response, planck_lambda, inst_mag, colour, sample_wavelengths, band_packet_fraction
from starmc.detector import photon_counts
from starmc import consts as C
lam = np.linspace(250.0, 1200.0, 4000)
assert abs(response(550.0, "V") - 1.0) < 1e-12
assert abs(response(550.0 + 89.0 / 2, "V") - 0.5) < 1e-9
ref = planck_lambda(lam, 10000.0)
cols = {3500.0: (1.238, 1.283, 0.957), 5772.0: (0.498, 0.494, 0.338), 10000.0: (0.0, 0.0, 0.0), 30000.0: (-0.408, -0.384, -0.231)}
for T, (bv, ub, vr) in cols.items():
    f = planck_lambda(lam, T)
    assert abs(colour(lam, f, ref, "B", "V") - bv) < 2e-3
    assert abs(colour(lam, f, ref, "U", "B") - ub) < 2e-3
    assert abs(colour(lam, f, ref, "V", "R") - vr) < 2e-3
f = 3.7 * planck_lambda(lam, 5772.0)
assert abs(colour(lam, f, ref, "B", "V") - colour(lam, planck_lambda(lam, 5772.0), ref, "B", "V")) < 1e-12
d = 10 * C.pc
F = np.pi * planck_lambda(lam, 5772.0) * (C.Rsun / d) ** 2 * 0.1
nV = photon_counts(F, lam * 1e-9, response(lam, "V"), 1.0, 1.0)
nB = photon_counts(F, lam * 1e-9, response(lam, "B"), 1.0, 1.0)
assert abs(nV / 1.0664e8 - 1) < 0.01 and abs(nB / 9.091e7 - 1) < 0.01
rng = np.random.default_rng(5)
Fe = np.pi * planck_lambda(lam, 5772.0)
s = sample_wavelengths(rng, lam, Fe, 200_000)
m = (lam > 520) & (lam < 580)
exp = np.trapezoid(Fe[m], lam[m]) / np.trapezoid(Fe, lam)
fr = band_packet_fraction(s, 520.0, 580.0)
assert abs(fr - exp) < 4 * np.sqrt(exp * (1 - exp) / 200_000)
assert abs(s.mean() - 659.5) < 1.5
print("MC-22 ok")
```

---

## Checkpoints

| Blackbody $T$ (K) | $B-V$ | $U-B$ | $V-R$ |
|---|---|---|---|
| 3500 | 1.238 | 1.283 | 0.957 |
| 5772 | 0.498 | 0.494 | 0.338 |
| 10000 | 0 (reference) | 0 | 0 |
| 30000 | −0.408 | −0.384 | −0.231 |

| Quantity | Value |
|---|---|
| $V$ photons s⁻¹ m⁻² for the Sun at 10 pc (toy filter) | $1.066\times10^8$ |
| $B$ photons s⁻¹ m⁻² | $9.09\times10^7$ |
| photon-counting noise, 1 s, 1 m² ($V$) | $10^{-4}$ |
| packets in 520–580 nm out of $2\times10^5$ (5772 K) | about 19 400 ($f=0.0967$) |
| mean wavelength of equal-energy packets | 659.5 nm |

---

## Done when

- You can say why colours do not depend on distance and why a count does.
- You can separate Monte Carlo noise from photon-counting noise and say which dominates for your run.
- You can state when the analytic dilution factor $(R/d)^2$ replaces packets and when packets are needed.
