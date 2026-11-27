# Module 18: Planck's law

[← 17 From lines to continuum](17-lines-to-continuum.md) · [README](../README.md) · [Next: 19 Stefan–Boltzmann law and stellar luminosity →](19-stefan-boltzmann-and-luminosity.md)

**Source:** Karttunen, §5.7, pp. 111–112, eqs (5.12)–(5.15), Fig. 5.10.

---

## Session A: read

- Read the first half of §5.7 (pp. 111–112), up to "Let us now try to find the total intensity".
- Key ideas:
  - A **blackbody** absorbs and re-emits all radiation. Its radiation depends only on its temperature, not on shape, material or interior.
  - Planck's law gives the intensity per unit frequency:
    $$B_\nu(T)=\frac{2h\nu^3}{c^2}\,\frac{1}{e^{h\nu/kT}-1}\qquad[{\rm W\,m^{-2}\,Hz^{-1}\,sr^{-1}}].$$
  - Per unit wavelength:
    $$B_\lambda(T)=\frac{2hc^2}{\lambda^5}\,\frac{1}{e^{hc/\lambda kT}-1}\qquad[{\rm W\,m^{-2}\,m^{-1}\,sr^{-1}}].$$
  - The two are the same radiation expressed per different variable, related by a Jacobian.
- Derivation of $B_\lambda$ from $B_\nu$ (5.13)–(5.15):
  1. The same power lies in matching intervals: $B_\nu\,d\nu=-B_\lambda\,d\lambda$ (the minus sign because $\nu$ falls as $\lambda$ rises).
  2. With $\nu=c/\lambda$, $d\nu/d\lambda=-c/\lambda^2$, so $B_\lambda=B_\nu\,c/\lambda^2$.
  3. Substitute $\nu=c/\lambda$ into $B_\nu$ to get the form above.

---

## Session B: compute

**Problem 1: the two Planck functions**

- Implement `B_nu(nu, T)` and `B_lam(lam, T)`. Make them safe against overflow for large $h\nu/kT$ (use `numpy.expm1`).

**Problem 2: total intensity both ways**

- At $T=5772$ K integrate $B_\nu\,d\nu$ over frequency and $B_\lambda\,d\lambda$ over wavelength. Both must equal $\sigma T^4/\pi$. Use wide enough ranges.

**Problem 3: a trap**

- Evaluate $B_\lambda$ at 550 nm and $B_\nu$ at $c/550$ nm, both at 5772 K. Show that their ratio is $\lambda^2/c$, and say why the numbers are not equal.

**Problem 4: Fig. 5.10**

- Find, numerically, the wavelength of the maximum of $B_\lambda$ for $T=6000,\,9000,\,12{,}000$ K. Compare the total intensities ($\propto T^4$) for the three curves.

**Problem 5: the same plot, two ways**

- Show analytically that $\lambda B_\lambda=\nu B_\nu$ (the power per logarithmic interval of the variable). Plot it for 5772 K against $\lambda$ on a log axis.

---

## Checkpoints

| Quantity | Value |
|---|---|
| $B_\lambda(550\ {\rm nm},\,5772\ {\rm K})$ | $2.573\times10^{13}$ W m⁻² m⁻¹ sr⁻¹ |
| $B_\nu(c/550\ {\rm nm},\,5772\ {\rm K})$ | $2.597\times10^{-8}$ W m⁻² Hz⁻¹ sr⁻¹ |
| ratio $B_\nu/B_\lambda$ | $1.009\times10^{-21}$ s ($=\lambda^2/c$) |
| $\int B_\nu d\nu=\int B_\lambda d\lambda$ at 5772 K | $2.0034\times10^{7}$ W m⁻² sr⁻¹ |
| $\lambda_{\max}$ at 6000, 9000, 12,000 K | 483.0, 322.0, 241.5 nm |
| total-intensity ratios | $256:81:16$ for 12,000 : 9000 : 6000 K |

---

## Done when

- You can derive $B_\lambda$ from $B_\nu$ and say what the Jacobian does.
- You can explain why $B_\lambda(550\,{\rm nm})$ and $B_\nu(c/550\,{\rm nm})$ are different numbers for the same radiation.
- You see that the area under the curves in Fig. 5.10 grows as $T^4$.
