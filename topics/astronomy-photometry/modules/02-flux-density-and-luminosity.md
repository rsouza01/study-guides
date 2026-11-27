# Module 02: Flux density and luminosity

[← 01 Intensity and solid angle](01-intensity-and-solid-angle.md) · [README](../README.md) · [Next: 03 Surface brightness and energy density →](03-surface-brightness-and-energy-density.md)

**Source:** Karttunen, §4.1, pp. 92–93, eq (4.5).

---

## Session A: read

- Read pp. 92–93, from "The flux density $F_\nu$ at a frequency..." to the paragraph ending with $L=4\pi r^2F$ (4.5).
- Key ideas:
  - **Flux density** $F$ is power per unit area (W m⁻², or W m⁻² Hz⁻¹ per frequency). **Flux** or **luminosity** $L$ is power (W).
  - For an isotropic source, $L=4\pi r^2F$ (4.5). Luminosity does not depend on distance, flux density falls as $1/r^2$.
  - For a source radiating into solid angle $\Omega$ only, $L=\Omega r^2F$.
  - The book warns that "flux", "flux density" and "intensity" are used loosely in the literature. Always check which one is meant.
- Derivation (the inverse-square law):
  1. Energy is conserved between two concentric spheres, so the same power crosses both.
  2. Power through a sphere = $F\cdot4\pi r^2$.
  3. Equal power through radii $r_1$ and $r_2$ gives $F_1/F_2=(r_2/r_1)^2$.

---

## Session B: compute

**Problem 1: the solar luminosity**

- Use the solar constant $S=1370$ W m⁻² and 1 AU to compute $L_\odot$.

**Problem 2: inverse square by simulation**

- Emit $10^7$ rays isotropically from a point.
- A circular detector of radius $a$ sits at distance $r$, facing the source. Count the fraction of rays that hit it.
- Compare with the exact fraction $(1-\cos\theta_0)/2$, where $\tan\theta_0=a/r$, and with the small-angle estimate $a^2/(4r^2)$.
- At what ratio $r/a$ does the small-angle estimate drift by 1 %?

**Problem 3: flux density at the planets**

- With $F=S/r^2$ in AU, tabulate $F$ at Mercury (0.387 AU), Earth, Jupiter (5.20 AU) and Neptune (30.1 AU).

**Problem 4: frequency versus wavelength**

- Starting from $F_\nu\,d\nu=F_\lambda\,d\lambda$, show that $F_\lambda=F_\nu\,c/\lambda^2$ (in absolute value).
- Convert 3631 Jy at 550 nm to $F_\lambda$ in W m⁻² nm⁻¹.

**Problem 5: beamed emission**

- A source radiates only into solid angle $\Omega=0.01$ sr and you measure $F=10^{-12}$ W m⁻² at 1 kpc. What is $L$? What would you have inferred wrongly assuming isotropy?

<details>
<summary>Hint (Problem 5)</summary>

Use $L=\Omega r^2F$ and $L_{\rm iso}=4\pi r^2F$. Their ratio is $\Omega/4\pi$.

</details>

---

## Checkpoints

| Quantity | Value |
|---|---|
| $L_\odot=4\pi\,(1\,{\rm AU})^2S$ | $3.853\times10^{26}$ W |
| fraction hit at $r/a=10$ (exact) | 0.002481 |
| small-angle estimate at $r/a=10$ | 0.002500 (0.75 % off) |
| 3631 Jy at 550 nm | 0.0360 W m⁻² m⁻¹ $=3.6\times10^{-11}$ W m⁻² nm⁻¹ |
| beamed vs isotropic luminosity | ratio $\Omega/4\pi=7.96\times10^{-4}$ |

---

## Done when

- You can state which of intensity, flux density and luminosity depends on distance, and how.
- Your simulation reproduces the $1/r^2$ law and you know where the small-angle approximation fails.
