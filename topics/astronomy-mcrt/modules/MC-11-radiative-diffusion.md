# Module MC-11: Radiative diffusion and the temperature structure

[← MC-10](MC-10-opacity.md) · [README](../README.md) · [Next: MC-12 Nuclear energy sources →](MC-12-nuclear-energy-sources.md)

**Source:** not in Forgan (Forgan §9.1 supplies the Monte Carlo version, MC-14). Continues PH-27. Background: Kippenhahn, Weigert & Weiss, the section on radiative energy transport; Carroll & Ostlie, the energy-transport section of the stellar-interiors chapter; Rybicki & Lightman, Ch. 1 (moments of the transfer equation).

---

## Session A: read

- One of the references above on the radiative temperature gradient and the Rosseland mean.
- Re-read PH-27 and Forgan §1.1 eq (3).

**Why this module exists.** A Monte Carlo star needs a temperature in every shell to define opacities and emissivities. We get that from the **diffusion limit** first. MC-14 then asks whether a packet simulation reproduces it.

**Derivation to see once: the diffusion equation from the moments of the transfer equation**

- Along a ray at angle $\theta$ to the radius, with $\mu=\cos\theta$, the grey transfer equation is $\mu\,\partial_rI+\dfrac{1-\mu^2}{r}\partial_\mu I=-\kappa\rho(I-S)$.
- Multiply by $\mu$ and integrate over solid angle. The left side gives $\partial_rK+\dfrac{3K-J}{r}$ where $J=\tfrac1{4\pi}\!\oint I\,d\Omega$ is the mean intensity and $K=\tfrac1{4\pi}\!\oint I\mu^2d\Omega$. The source term has no $\mu$-dependence and integrates to zero. The right side is $-\kappa\rho H$ with the Eddington flux $H=\tfrac1{4\pi}\!\oint I\mu\,d\Omega=F/4\pi$.
- In the interior the radiation is nearly isotropic, so $K\simeq J/3$ (Eddington approximation). Then $3K-J=0$ and
$$\tfrac13\,\partial_rJ=-\kappa\rho\,H.$$
- In LTE $J=B=\sigma T^4/\pi$. With $F=4\pi H$ and $u=aT^4=4\pi J/c$:
$$F=-\frac{c}{3\kappa\rho}\,\partial_r(aT^4)=-\frac{16\sigma T^3}{3\kappa\rho}\,\partial_rT.$$
- For a star the flux through radius $r$ is $F=L(r)/4\pi r^2$. Therefore
$$\boxed{\ \partial_r(T^4)=-\frac{3\kappa_R\rho\,L(r)}{4\pi\,a\,c\,r^2}\ }$$
- The $\kappa$ that appears when you do this frequency by frequency and then integrate is the **Rosseland mean**: $\dfrac1{\kappa_R}=\dfrac{\int\kappa_\nu^{-1}\,\partial_TB_\nu\,d\nu}{\int\partial_TB_\nu\,d\nu}$. (Carry the same derivation for $F_\nu=-\tfrac{4\pi}{3\kappa_\nu\rho}\partial_rB_\nu$, then integrate over $\nu$ and use $\int\partial_TB_\nu d\nu=4\sigma T^3/\pi$.)

**Derivation to see once: the photon-diffusion time**

- Radiation diffuses with coefficient $D=c/(3\kappa\rho)$ (read off from $F=-D\,\partial_ru$ above).
- Let $t(r)$ be the mean time to reach the surface for a packet released at radius $r$. The backward equation for a diffusing particle is $\dfrac1{r^2}\partial_r\big(r^2D\,\partial_rt\big)=-1$, with $t(R)=0$ and $t$ regular at the centre.
- Integrate once: $r^2D\,\partial_rt=-r^3/3$, so $\partial_rt=-\dfrac{r}{3D}=-\dfrac{\kappa\rho\,r}{c}$.
- Integrate again from the centre to the surface:
$$\langle t\rangle_{r=0}=\frac1c\int_0^R\kappa\rho\,r\,dr.$$
- Check with constant $\kappa\rho$: $\langle t\rangle=\dfrac{\kappa\rho R^2}{2c}=\dfrac{R^2}{6D}$, the textbook result.
- This is the **photon diffusion time**, not the Kelvin–Helmholtz (thermal) time of the star. For the real Sun the first is of order $10^5$ yr and the second about $3\times10^7$ yr.

---

## Session B: do

**Problem 1: from L(r) to T(r)**

- With the polytropic density of MC-09, a fixed luminosity profile $L(r)$ (see MC-12; for now use $L(r)=L_\odot$ everywhere) and $\kappa_R$ of MC-10, integrate $\partial_r(T^4)$ inward from the surface with $T_s=5772$ K. Use $T^4$ as the variable, evaluated at shell mid-points.
- Iterate: $\kappa_R$ depends on $T$ so repeat until $\max|\Delta T/T|<10^{-6}$ (relaxation factor 0.5 helps).

**Problem 2: central temperature**

- Report $T_c$. Compare with the polytropic $T_c=1.21\times10^7$ K and with the real Sun's $1.57\times10^7$ K. Is the toy star self-consistent? (No: density is fixed from a polytrope while $T$ comes from transport. Say which equation of the structure you are *not* solving.)

**Problem 3: diffusion time**

- Compute $\langle t\rangle=\tfrac1c\int\kappa_R\rho\,r\,dr$ for a packet released at the centre, in years. Compare with the real Sun.

**Problem 4: radiation versus gas pressure**

- Compute $P_{\rm rad}/P_{\rm gas}$ at the centre and at $0.5R$. Is the ideal-gas treatment of MC-09 justified?

---

## Translation: text → code

| Quantity | Code |
|---|---|
| $y=T^4$ increment over a shell | `dy = 3*kap*rho*L/(4*pi*c*r**2*a_rad)*dr` |
| inward integration | `y[i] = acc + 0.5*dy[i]; acc += dy[i]` (from the surface in) |
| photon diffusion time | `np.sum(kap*rho*r*dr)/c` |
| $P=\rho kT/\mu m_u+aT^4/3$ | `pressure(rho, T, mu)` |

---

## Contract

This module's code is folded into `thermal.radiative_equilibrium_T` (completed in MC-13). Write the piece below first:

```text
starmc/thermal.py
  pressure(rho, T, mu) -> rho*k*T/(mu*m_u) + a_rad*T**4/3
  diffusion_time_centre(star, kappa_rho) -> seconds, (1/c) * sum(kappa_rho * r_mid * dr)
```

```python
# acceptance-test
import numpy as np
from starmc.star import polytrope_star
from starmc.thermal import pressure, diffusion_time_centre
from starmc import consts as C
assert np.isclose(pressure(1.0, 1e6, 0.6), 1.0 * C.k * 1e6 / (0.6 * C.m_u) + C.a_rad * 1e24 / 3)
s = polytrope_star(n_shells=100)
dr = np.diff(s.r_edges)
kr = np.full(100, 1.0 / C.Rsun)        # tau_tot = 1, uniform
t = diffusion_time_centre(s, kr)
assert abs(t / (0.5 * C.Rsun / C.c) - 1) < 0.01, t     # (1/c) * kr * R^2/2
print("MC-11 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| uniform $\kappa\rho$, $\tau_{\rm tot}=1$: $\langle t\rangle$ | $R/2c=1.16$ s |
| toy-star diffusion time, centre release | about $3.1\times10^4$ yr (after MC-13) |
| real Sun | about $1.7\times10^5$ yr (Mitalas & Sills 1992) |

---

## Done when

- You can derive $\partial_r(T^4)=-3\kappa_R\rho L/(4\pi acr^2)$ from the $\mu$-moment of the transfer equation and the Eddington closure.
- You can say why the Rosseland mean (a harmonic mean) appears, and why it weights the windows of low opacity.
- You can explain the difference between the photon diffusion time and the thermal time.
