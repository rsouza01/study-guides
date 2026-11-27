# Module 12: Photons and energy levels

[← 11 Atmospheric extinction and air mass](11-atmospheric-extinction.md) · [README](../README.md) · [Next: 13 The hydrogen atom →](13-hydrogen-atom.md)

**Source:** Karttunen, §5.1, pp. 103–105, eq (5.1), Figs 5.1–5.3.

---

## Session A: read

- Read §5.1 (pp. 103–105).
- Key ideas:
  - A photon has energy $\Delta E=h\nu$ (5.1). An atom emits or absorbs a photon when it moves between energy levels, so atoms have **line spectra**.
  - **Emission** lines come from hot low-pressure gas; **absorption** lines appear when the same gas is seen against a continuum.
  - Excited states decay by **spontaneous emission** (typical lifetime $10^{-8}$ s) or are pushed down by **induced (stimulated) emission**. Collisions also cause transitions without photons.
  - Zero of energy: a bound electron has $E<0$, a free electron $E>0$. Transition types: bound–bound (absorption or emission), bound–free (ionisation), free–bound (recombination), free–free (bremsstrahlung).
  - Scattering is absorption followed by instant re-emission at the same wavelength; scattered light is polarised. Polarised light rotates in a magnetic field (Faraday rotation), by an amount that grows with the field component along the line of sight, the electron column, the path, and $\lambda^2$.

---

## Session B: compute

**Problem 1: a unit converter**

- Write `convert(value, unit_from, unit_to)` for energy in J, eV, frequency in Hz, wavelength in m or nm, and temperature equivalent $E/k$ in K.
- Test with the checkpoints below.

**Problem 2: spontaneous decay by Monte Carlo**

- Take $2\times10^5$ excited atoms with mean lifetime $T=10^{-8}$ s. Draw each decay time from an exponential distribution.
- Check: the mean decay time, the median, and the fraction still excited at $t=3T$.

**Problem 3: ionisation**

- A hydrogen atom in its ground state ($-13.6$ eV) absorbs a 50 nm photon. What is the photon energy, the kinetic energy of the freed electron, and its speed?

**Problem 4: which transitions can this photon do?**

- Which of the following, if any, can ionise ground-state hydrogen: 21 cm radio, 550 nm light, 121.6 nm, 91.0 nm?

---

## Checkpoints

| Quantity | Value |
|---|---|
| 13.6 eV ↔ wavelength | 91.16 nm |
| 550 nm ↔ energy | 2.254 eV |
| 21.106 cm ↔ energy | $5.874\times10^{-6}$ eV |
| 1 eV ↔ temperature | 11,604.5 K |
| mean decay time | $\approx10^{-8}$ s |
| median decay time | $6.93\times10^{-9}$ s ($T\ln2$) |
| fraction left at $3T$ | 0.0498 ($e^{-3}$) |
| 50 nm photon energy | 24.80 eV |
| electron kinetic energy | 11.19 eV |
| electron speed | $1.98\times10^{6}$ m s⁻¹ |

---

## Done when

- You can convert between eV, Hz, nm and K without looking up the constants.
- You can say why decay times are exponential and why the median is below the mean.
- You can name the four kinds of transition in Fig. 5.2 and say which ones give lines and which give continua.
