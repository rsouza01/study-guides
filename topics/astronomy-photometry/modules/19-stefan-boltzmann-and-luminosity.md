# Module 19: Stefan–Boltzmann law and stellar luminosity

[← 18 Planck's law](18-plancks-law.md) · [README](../README.md) · [Next: 20 Wien displacement law →](20-wien-displacement-law.md)

**Source:** Karttunen, §5.7, pp. 112–113, eqs (5.16)–(5.21); Example 5.2, p. 118; Exercises 5.4 and 5.5, p. 120.

---

## Session A: read

- Read pp. 112–113 from "Let us now try to find the total intensity" to eq (5.21), then Example 5.2.
- Key ideas:
  - Integrating Planck's law over frequency gives $B(T)=AT^4$ (5.16).
  - The flux density from an isotropic surface is $F=\pi B=\sigma T^4$ (5.18), the **Stefan–Boltzmann law**. $\sigma=\pi A=5.67\times10^{-8}$ W m⁻² K⁻⁴.
  - A star of radius $R$ radiating like a blackbody: $L=4\pi\sigma R^2T^4$ (5.19). This defines the effective temperature.
  - Combining with $M_{bol}-M_{bol,\odot}=-2.5\lg(L/L_\odot)$ gives (5.21): $M_{bol}-M_{bol,\odot}=-5\lg(R/R_\odot)-10\lg(T/T_\odot)$.
- Derivation of (5.16):
  1. $B(T)=\dfrac{2h}{c^2}\displaystyle\int_0^\infty\dfrac{\nu^3\,d\nu}{e^{h\nu/kT}-1}$.
  2. Put $x=h\nu/kT$, so $d\nu=(kT/h)\,dx$.
  3. $B(T)=\dfrac{2k^4}{c^2h^3}\,T^4\displaystyle\int_0^\infty\dfrac{x^3dx}{e^x-1}$.
  4. The integral is a number: $\Gamma(4)\,\zeta(4)=6\cdot\dfrac{\pi^4}{90}=\dfrac{\pi^4}{15}$.
  5. So $A=\dfrac{2\pi^4k^4}{15c^2h^3}$.
- Step 4 uses the Riemann zeta function, the same function as in the Riemann Hypothesis guide. The book says so in a parenthesis on p. 112.

---

## Session B: compute

**Problem 1: the integral**

- Evaluate $\int_0^\infty x^3/(e^x-1)\,dx$ numerically. Compare with $\pi^4/15$ and with $\Gamma(4)\,\zeta(4)$, using your own $\zeta(4)$ from Module 03 of the Riemann guide if you have it.

**Problem 2: the constants**

- Compute $A$ and $\sigma=\pi A$ from $h$, $k$, $c$.

**Problem 3: the Sun**

- Compute $L_\odot=4\pi\sigma R_\odot^2T_\odot^4$.

**Problem 4: Example 5.2**

- A star has $T_{\rm eff}=12{,}000$ K and $M_{bol}=0.0$. Find its radius in solar radii from (5.21), once with the book's solar values ($T_\odot=5800$ K, $M_{bol,\odot}=4.7$) and once with modern ones. The book's text says 5000 K for the Sun but calculates with 5800 K.

**Problem 5: Exercise 5.4 (a red giant)**

- A red giant has $T=2500$ K and radius $100\,R_\odot$.
- (a) Find its total luminosity and its luminosity in the visual band 400–700 nm.
- (b) A 100 W lamp radiates 5 % of its energy in the visual band. At what distance does the lamp look as bright as the star? The star's distance is not given, so express the lamp's distance as a multiple of the star's.

<details>
<summary>Answer</summary>

$L=1.35\times10^{29}$ W $=352\,L_\odot$. Visual fraction 3.34 %, so $L_{\rm vis}=4.50\times10^{27}$ W. The lamp (5 W in the visual) must be at $3.3\times10^{-14}$ times the star's distance. For a star at 100 pc, that is about 100 km.

</details>

**Problem 6: Exercise 5.5 (the radius of Sirius)**

- Sirius has $T_{\rm eff}=10{,}000$ K, $V=-1.5$, distance 2.67 pc (the book prints kpc, a misprint), and BC = 0.5. Find its radius.
- Use $m_{bol}=V-{\rm BC}$ (the book's convention), then $M_{bol}$, then $L$, then $R$.

<details>
<summary>Answer</summary>

$m_{bol}=-2.0$, $M_{bol}=0.87$, $L=35\,L_\odot$, $R=1.98\,R_\odot$.

</details>

---

## Checkpoints

| Quantity | Value |
|---|---|
| $\int x^3/(e^x-1)\,dx$ | 6.493939 |
| $\Gamma(4)\,\zeta(4)=6\times1.0823232$ | 6.493939 |
| $A=\sigma/\pi$ | $1.80494\times10^{-8}$ W m⁻² K⁻⁴ sr⁻¹ |
| $\sigma$ | $5.67037\times10^{-8}$ W m⁻² K⁻⁴ |
| $L_\odot$ | $3.828\times10^{26}$ W |
| Example 5.2 radius, book values | 2.035 $R_\odot$ (the book: 2.0) |
| Example 5.2 radius, modern values | 2.05 $R_\odot$ |

---

## Done when

- You can carry out the substitution $x=h\nu/kT$ and say where $T^4$ comes from.
- You can say why the zeta function appears here.
- You can go from a magnitude, a distance and a temperature to a stellar radius, step by step, and say which step carries the largest uncertainty.
