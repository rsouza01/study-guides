# Module 20: Wien displacement law

[← 19 Stefan–Boltzmann law and stellar luminosity](19-stefan-boltzmann-and-luminosity.md) · [README](../README.md) · [Next: 21 Wien and Rayleigh–Jeans limits →](21-wien-and-rayleigh-jeans.md)

**Source:** Karttunen, §5.7, p. 113, eq (5.22); Example 5.3, pp. 118–119; Fig. 5.10.

---

## Session A: read

- Read the paragraph around eq (5.22) on p. 113 and then Example 5.3 (pp. 118–119), which contains the full derivation.
- Key ideas:
  - The wavelength of maximum intensity obeys $\lambda_{\max}T=b=2.898\times10^{-3}$ K m (5.22).
  - The maximum of $B_\nu$ occurs at a different place: $\nu_{\max}\neq c/\lambda_{\max}$, because the two forms of Planck's function are densities with respect to different variables.
- Derivation (Example 5.3 in outline):
  1. With $x=hc/\lambda kT$, $B_\lambda\propto f(x)=x^5/(e^x-1)$ at fixed $T$.
  2. $f'(x)=0$ gives $5(1-e^{-x})=x$. No closed form with elementary functions, so iterate $x\leftarrow5(1-e^{-x})$.
  3. The root is $x\approx4.965$, so $\lambda_{\max}T=hc/(4.965\,k)$.
  4. For $B_\nu$ the same steps give $x^3/(e^x-1)$, hence $3(1-e^{-x})=x$ and $x\approx2.821$.

---

## Session B: compute

**Problem 1: three ways to solve $x=5(1-e^{-x})$**

- Fixed-point iteration from $x_0=5$ (print the first six iterates), then a bracketing root finder, then the closed form $x=5+W_0(-5e^{-5})$ using `scipy.special.lambertw`.

**Problem 2: the constants**

- Compute $b=hc/(xk)$ and, for the frequency form, $b'=x'k/h$ (in Hz K⁻¹) and $T/\nu_{\max}$ (in K s).

**Problem 3: the Sun**

- At 5772 K compute $\lambda_{\max}$ and $\nu_{\max}$, then $c/\nu_{\max}$. Explain the difference in your own words.

**Problem 4: Fig. 5.10**

- Check the three wavelengths of maxima for 12,000, 9000 and 6000 K. They are in the ratio 1 : 4/3 : 2.

**Problem 5 (bonus): the peak per logarithmic interval**

- $\nu B_\nu=\lambda B_\lambda$ peaks where $4(1-e^{-x})=x$. Solve it and find the wavelength for the Sun.

---

## Checkpoints

| Quantity | Value |
|---|---|
| iterates $x_1,\dots,x_6$ | 4.96631, 4.96516, 4.965116, 4.9651143, 4.9651142, 4.9651142 |
| root $x$ (wavelength form) | 4.965114 |
| root $x'$ (frequency form) | 2.821439 |
| $b$ | $2.89777\times10^{-3}$ K m |
| $b'$ | $5.8789\times10^{10}$ Hz K⁻¹ |
| $T/\nu_{\max}$ | $1.7010\times10^{-11}$ K s |
| Sun: $\lambda_{\max}$ | 502.0 nm |
| Sun: $\nu_{\max}$ and $c/\nu_{\max}$ | $3.393\times10^{14}$ Hz and 883.5 nm |
| $\lambda_{\max}$ at 12,000 / 9000 / 6000 K | 241.5 / 322.0 / 483.0 nm |
| bonus: $x$ for $\nu B_\nu$ | 3.9207 |
| bonus: Sun's peak per log interval | about 636 nm |

---

## Done when

- You can derive $5(1-e^{-x})=x$ from $f(x)=x^5/(e^x-1)$ on paper.
- You can explain why the Sun peaks at "500 nm" or "880 nm" depending on whether you plot per wavelength or per frequency.
- You know how fast the fixed-point iteration converges and why.
