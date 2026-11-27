# Module 17: From lines to continuum

[← 16 Boltzmann populations](16-boltzmann-populations.md) · [README](../README.md) · [Next: 18 Planck's law →](18-plancks-law.md)

**Source:** Karttunen, §5.5 "Molecular Spectra" and §5.6 "Continuous Spectra", p. 111, Fig. 5.9.

---

## Session A: read

- Read §5.5 and §5.6 (p. 111).
- Key ideas:
  - Molecules have **vibrational** states (transitions in the infrared) and **rotational** states (microwave), on top of the electronic ones. The result is a **band spectrum**: narrow bands made of very many lines.
  - Continuous emission spectra arise from recombination and free–free transitions. Continuous absorption arises from ionisation and free–free transitions.
  - When pressure rises, collisions broaden lines until they overlap. Dense gas, liquids and solids give continuous spectra.
- This module turns the last two sentences into numbers. The overlap is a purely geometric effect you can compute.

---

## Session B: compute

**Problem 1: a comb of equally spaced lines**

- Sum Lorentzian lines of FWHM $w$ at spacing $\Delta$, using $\pm2000$ lines. Compute the ratio of the spectrum at a line centre to the value halfway between lines, for $w/\Delta=0.25,\,0.5,\,1,\,2$.
- Check against the exact result for the peak-to-valley ratio, $\coth^2(\pi w/2\Delta)$.

**Problem 2: randomly placed lines**

- Place lines at random (Poisson) positions with mean density $\rho$ per unit wavelength, all Lorentzian with FWHM $w$ and unit area. For $\rho w=1,10,100$ measure the relative standard deviation (std/mean) of the summed spectrum.
- Compare with the prediction $1/\sqrt{\pi\rho w}$ and explain how it follows from "shot noise" of overlapping lines.

**Problem 3: where is the continuum?**

- Describe in words, from your numbers, the value of $\rho w$ at which the spectrum starts to look continuous at 10 % contrast.

**Problem 4: a rotational ladder (the radio side of §5.5)**

- A rigid rotor has energies $E_J=hB\,J(J+1)$. Show that the transition $J\to J-1$ has frequency $2BJ$.
- For carbon monoxide, $B=57.636$ GHz. Compute the frequency and wavelength of the lines $J=1\to0$, $2\to1$, $3\to2$.

**Problem 5 (bonus): a vibration–rotation band**

- This goes beyond the book. For a diatomic molecule with vibration at wavenumber $\tilde\nu_0$ and the same rotational constant $\tilde B$ in both vibrational states, the lines lie at $\tilde\nu_0+2\tilde B(J+1)$ (R branch, $J=0,1,\dots$) and $\tilde\nu_0-2\tilde BJ$ (P branch, $J=1,2,\dots$).
- For CO use $\tilde\nu_0=2143.3$ cm⁻¹ and $\tilde B=1.9313$ cm⁻¹. Plot the first 30 lines of each branch. What is missing at $\tilde\nu_0$?

---

## Checkpoints

| $w/\Delta$ | peak/valley ratio |
|---|---|
| 0.25 | 7.16 |
| 0.5 | 2.33 |
| 1 | 1.19 |
| 2 | 1.0075 |

| $\rho w$ | relative std of the spectrum |
|---|---|
| 1 | 0.56 |
| 10 | 0.18 |
| 100 | 0.056 |

| CO rotational line | frequency | wavelength |
|---|---|---|
| $1\to0$ | 115.27 GHz | 2.60 mm |
| $2\to1$ | 230.54 GHz | 1.30 mm |
| $3\to2$ | 345.81 GHz | 0.867 mm |

- Bonus: R(0) at 2147.16 cm⁻¹, P(1) at 2139.44 cm⁻¹, a gap of $4\tilde B$ at the band origin.

---

## Done when

- You can say why lines that are separately visible at low pressure merge at high pressure, with numbers from your comb.
- You can say which part of the electromagnetic spectrum shows rotational and which shows vibrational molecular transitions.
