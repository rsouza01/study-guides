# Module 14: Line profiles

[← 13 The hydrogen atom](13-hydrogen-atom.md) · [README](../README.md) · [Next: 15 Quantum numbers and selection rules →](15-quantum-numbers-and-selection-rules.md)

**Source:** Karttunen, §5.3, pp. 107–108, eqs (5.9)–(5.10), Figs 5.5–5.6.

---

## Session A: read

- Read §5.3 (pp. 107–108).
- Key ideas:
  - Lines are not infinitely sharp. The uncertainty relation $\Delta E\,\Delta t\approx\hbar$ gives each line a **natural width**.
  - A level with lifetime $T$ has an energy uncertainty $\hbar/T$, so $\Delta\nu=\Delta E/h=1/(2\pi T)$. Both levels contribute (5.9).
  - The natural profile is a **Lorentzian** (5.10).
  - Gas motions add **Doppler broadening** (Gaussian). The combination is the **Voigt profile**: Gaussian core, Lorentzian wings.
  - Two measures of a line: the **FWHM** (width at half depth) and the **equivalent width** (the width of a rectangle with the same area that is totally dark).
- **A caution about units.** Eq (5.9) defines $\gamma=1/T_i+1/T_f$ in rad s⁻¹. Eq (5.10) then uses $\gamma$ as a width in Hz (the FWHM is $\gamma$ in the variable $\nu$). A width in Hz is $\gamma/2\pi$, as the sentence before (5.9) says. In this module, $\gamma$ means the FWHM **in Hz**: $\gamma=(1/T_i+1/T_f)/2\pi$.

---

## Session B: compute

**Problem 1: the Lorentzian (5.10)**

- Implement $I_\nu=\dfrac{\gamma}{2\pi}\dfrac{I_0}{(\nu-\nu_0)^2+\gamma^2/4}$.
- Check: the peak is $2I_0/(\pi\gamma)$; the value at $\nu_0\pm\gamma/2$ is half of it.
- Integrate numerically over $\nu_0\pm100\gamma$ and compare with $I_0$. Explain the missing fraction.

**Problem 2: natural widths**

- For an upper-level lifetime $T_i=10^{-8}$ s and a stable lower level, compute $\gamma$ in Hz, and the corresponding width in wavelength at 500 nm ($\Delta\lambda=\lambda^2\,\Delta\nu/c$).

**Problem 3: Doppler broadening**

- The line-of-sight velocity of atoms of mass $m$ at temperature $T$ is Gaussian with $\sigma_v=\sqrt{kT/m}$. Then $\sigma_\nu=\nu_0\sigma_v/c$ and ${\rm FWHM}=2\sqrt{2\ln2}\,\sigma_\nu$.
- Compute the Doppler FWHM of $H_\alpha$ (656.3 nm) for hydrogen at $10^4$ K and at 5772 K, in nm.

**Problem 4: the Voigt profile**

- Convolve a Gaussian ($\sigma=1$) with a Lorentzian (HWHM 0.5) numerically, for example by direct summation or FFT, normalised to unit area.
- Compare with `scipy.special.voigt_profile(x, sigma, gamma)` (here `gamma` is the HWHM) at $x=0,1,3$.
- Compare the Voigt peak with the pure Gaussian peak and the pure Lorentzian peak of the same area.

**Problem 5: equivalent width**

- Take an absorption line with residual intensity $1-d\,\phi(\lambda)$, where $\phi$ is a Gaussian of unit peak and width $\sigma$, and $d=0.6$.
- Compute the equivalent width by integration and compare with $d\sigma\sqrt{2\pi}$, and with the FWHM.

---

## Checkpoints

| Quantity | Value |
|---|---|
| Lorentzian peak | $2I_0/(\pi\gamma)$ |
| area within $\pm100\gamma$ | 0.9968 $I_0$ ($=\tfrac2\pi\arctan200$) |
| natural width, $T_i=10^{-8}$ s | $1.59\times10^{7}$ Hz |
| in wavelength at 500 nm | $1.33\times10^{-5}$ nm |
| $H_\alpha$ Doppler FWHM at $10^4$ K | 0.0468 nm |
| $H_\alpha$ Doppler FWHM at 5772 K | 0.0356 nm |
| Voigt at $x=0,1,3$ ($\sigma=1$, HWHM 0.5) | 0.27896, 0.20018, 0.02834 |
| Gaussian peak / Lorentzian peak (unit area) | 0.39894 / 0.63662 |
| equivalent width / FWHM, Gaussian | $d\cdot1.064$ (for $d=0.6$: 0.638 of the FWHM) |

---

## Done when

- You can explain why the Doppler width is much larger than the natural width in stellar atmospheres, and which one sets the wings.
- You can explain the difference between FWHM and equivalent width, and when each is useful.
- You can explain the factor $2\pi$ between $\gamma$ in rad s⁻¹ and in Hz.
