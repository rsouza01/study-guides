# Module 23: Brightness and antenna temperature

[← 22 Effective temperature](22-effective-temperature.md) · [README](../README.md) · [Next: 24 Colour temperature →](24-colour-temperature.md)

**Source:** Karttunen, §5.8, pp. 114–115, eqs (5.27)–(5.30); Exercise 5.6, p. 120.

---

## Session A: read

- Read the brightness-temperature and antenna-temperature paragraphs of §5.8 (pp. 114–115).
- Key ideas:
  - The **brightness temperature** $T_b$ at a wavelength is the temperature a blackbody would need to match the observed intensity there. For a star with angular diameter $\alpha$, the observed flux density is $F_\lambda'=(\alpha/2)^2\pi B_\lambda(T_b)$ (5.27). It depends on wavelength because a star is not a blackbody.
  - In radio astronomy $h\nu\ll kT$ almost always, so Rayleigh–Jeans applies and $T_b=\dfrac{c^2}{2k\nu^2}I_\nu=\dfrac{\lambda^2}{2k}I_\nu$ (5.28).
  - The signal in a radio telescope is the **antenna temperature**: $T_A=\eta\,T_b$ (5.29), with beam efficiency $\eta\approx0.4$–0.8, if the source fills the beam. For a smaller source, $T_A=\eta\,(\Omega_S/\Omega_A)\,T_b$ (5.30).
- Derivation of (5.28):
  1. Expand $e^{h\nu/kT_b}\approx1+h\nu/kT_b$.
  2. $B_\nu\approx\dfrac{2h\nu^3}{c^2}\dfrac{kT_b}{h\nu}=\dfrac{2k\nu^2}{c^2}T_b$.
  3. Set $I_\nu=B_\nu(T_b)$ and solve.

---

## Session B: compute

**Problem 1: the exact inverse of Planck**

- Write `Tb_exact(nu, I)` from $T_b=\dfrac{h\nu/k}{\ln\!\big(1+2h\nu^3/c^2I_\nu\big)}$, and `Tb_RJ(nu, I)` from (5.28).
- Round-trip test: generate $I_\nu=B_\nu(10\ {\rm K})$ at 230 GHz and recover 10 K. Then see what the Rayleigh–Jeans version gives, and why.

**Problem 2: Exercise 5.6 (the Sun at 300 nm)**

- The observed flux density of the Sun at 300 nm is 0.59 W m⁻² nm⁻¹. Taking the angular diameter as 32′, find the brightness temperature from (5.27).

**Problem 3: a radio source**

- A source of flux density 1 Jy is a uniform disc of angular diameter 1″ at 1.4 GHz. Compute its brightness temperature from (5.28), using $I_\nu=F_\nu/\Omega$. Verify that $h\nu\ll kT_b$.

**Problem 4: antenna temperature**

- A telescope has $\eta=0.6$. A source with $T_b=1000$ K fills 40 % of the beam. What is $T_A$?

**Problem 5: where does Rayleigh–Jeans fail?**

- For a 10 K blackbody, compute $T_b$ by (5.28) at 1, 10, 100, 230 and 345 GHz. At which frequency does it first deviate by more than 10 %?

---

## Checkpoints

| Quantity | Value |
|---|---|
| 10 K at 230 GHz: $h\nu/kT$ | 1.104 |
| Rayleigh–Jeans $T_b$ for that case | 5.48 K |
| exact inverse of Planck | 10.0 K |
| Exercise 5.6: surface $B_\lambda$ | $8.67\times10^{12}$ W m⁻³ sr⁻¹ |
| Exercise 5.6: $T_b$ at 300 nm | 5551 K |
| 1 Jy, 1″ disc, 1.4 GHz: $\Omega$ | $1.846\times10^{-11}$ sr |
| same: $T_b$ | $9.0\times10^{5}$ K |
| $T_A$ for $\eta=0.6$, 40 % fill, $T_b=1000$ K | 240 K |

---

## Done when

- You can derive (5.28) and say exactly when it fails.
- You can explain why $T_b$ is not a physical temperature unless the source is a blackbody.
- You can explain the difference between $T_b$ and $T_A$ and what the beam efficiency and filling factor each do.
