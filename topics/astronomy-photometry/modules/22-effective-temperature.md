# Module 22: Effective temperature

[← 21 Wien and Rayleigh–Jeans limits](21-wien-and-rayleigh-jeans.md) · [README](../README.md) · [Next: 23 Brightness and antenna temperature →](23-brightness-and-antenna-temperature.md)

**Source:** Karttunen, §5.8, p. 114, eqs (5.25)–(5.26); Example 5.5, pp. 119–120.

---

## Session A: read

- Read the opening of §5.8 and the effective-temperature paragraphs (p. 114), then Example 5.5.
- Key ideas:
  - There is no single "temperature" of a star. Each definition answers a different question.
  - The **effective temperature** $T_{\rm e}$ is the temperature of a blackbody that radiates the same total flux density as the star. It depends only on the integrated power, so it is well defined even for spectra far from Planck's.
  - $F=\sigma T_{\rm e}^4$ at the surface (5.25). At distance $r$, with $\alpha=2R/r$ the angular diameter, the observed flux density is $F_\oplus=(R/r)^2F=(\alpha/2)^2\sigma T_{\rm e}^4$ (5.26).
  - So $T_{\rm e}$ can be measured directly if you know the total flux density **and** the angular diameter (interferometry).
- Derivation of (5.26):
  1. Luminosity $L=4\pi R^2F$ spreads over $4\pi r^2$: $F_\oplus=L/4\pi r^2=(R/r)^2F$.
  2. With $\alpha=2R/r$, $R/r=\alpha/2$.
  3. Insert $F=\sigma T_{\rm e}^4$.

---

## Session B: compute

**Problem 1: the Sun**

- Use the solar constant $S=1370$ W m⁻² and the angular diameter 32′ to compute $T_{\rm e}$.

**Problem 2: Example 5.5 (Arcturus)**

- Observed flux density $4.5\times10^{-8}$ W m⁻², angular diameter 0.020″. Compute $T_{\rm e}$.

**Problem 3: how well do we know it?**

- $T_{\rm e}\propto F^{1/4}\alpha^{-1/2}$. Derive the fractional error propagation formula.
- Assume 5 % on $F$ and 10 % on $\alpha$ for Arcturus. Compute the predicted fractional error, then confirm with $2\times10^5$ Monte Carlo draws.

**Problem 4: from the other side**

- Compute $T_{\rm e}$ from $L$ and $R$ using (5.19), $T_{\rm e}=\big[L/(4\pi\sigma R^2)\big]^{1/4}$, for the Sun and for the red giant of Module 19 (radius $100R_\odot$, $L=352L_\odot$).

---

## Checkpoints

| Quantity | Value |
|---|---|
| angular radius of the Sun (32′ diameter) | $4.654\times10^{-3}$ rad |
| $T_{\rm e}$ of the Sun from $S$ and 32′ | 5779 K |
| Arcturus: $\alpha/2$ | $4.848\times10^{-8}$ rad |
| Arcturus: $T_{\rm e}$ | 4287 K (the book: 4300 K) |
| predicted $\delta T/T$ | 5.15 % |
| Monte Carlo $\delta T/T$ | about 5.2 % |
| $T_{\rm e}$ from $L,R$ for the Sun | 5772 K |
| $T_{\rm e}$ of the red giant | 2500 K |

---

## Done when

- You can say what "effective" means and why it is independent of the shape of the spectrum.
- You can explain why the angular diameter, not the distance, is what you need for a direct measurement.
- You can say which of $F$ or $\alpha$ limits the accuracy of $T_{\rm e}$ in a typical case.
