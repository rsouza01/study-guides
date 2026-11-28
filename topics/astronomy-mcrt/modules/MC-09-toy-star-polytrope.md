# Module MC-09: A toy star, the $n=3$ polytrope

[← MC-08](MC-08-errors-and-cost.md) · [README](../README.md) · [Next: MC-10 Opacity →](MC-10-opacity.md)

**Source:** not in Forgan. Background: Kippenhahn, Weigert & Weiss, *Stellar Structure and Evolution*, the section on polytropic models (Lane–Emden); Carroll & Ostlie, the polytropes section of the chapter on the Sun; Chandrasekhar (1939), *An Introduction to the Study of Stellar Structure*, the chapter on polytropic gas spheres. (Section numbers differ between editions; look them up by title.)

---

## Session A: read

- One of the three references above, on the Lane–Emden equation and the tabulated solutions for $n=3$.
- Re-read PH-19 for $L=4\pi R^2\sigma T^4$ and PH-22 for $T_{\rm eff}$.

**Why a polytrope.** Forgan's code takes a density grid as **input**. For a star we need a density structure $\rho(r)$ before we can transport anything. The $n=3$ polytrope is the cheapest model with a Sun-like central concentration. It is a *toy*: it is not a solar model and the guide never pretends otherwise.

**Derivation to see once: the Lane–Emden equation**

- Hydrostatic equilibrium: $\partial_rP=-G\,m\,\rho/r^2$, with $\partial_rm=4\pi r^2\rho$.
- Multiply by $r^2/\rho$ and differentiate: $\partial_r\!\big(\tfrac{r^2}{\rho}\partial_rP\big)=-G\,\partial_rm=-4\pi G r^2\rho$. So $\tfrac1{r^2}\partial_r\!\big(\tfrac{r^2}{\rho}\partial_rP\big)=-4\pi G\rho$.
- Polytropic relation $P=K\rho^{1+1/n}$. Write $\rho=\rho_c\theta^n$, so $P=P_c\theta^{n+1}$ with $P_c=K\rho_c^{1+1/n}$.
- Then $\tfrac1\rho\partial_rP=(n+1)\tfrac{P_c}{\rho_c}\partial_r\theta$. Inserting and defining $r=a\xi$ with $a^2=\dfrac{(n+1)P_c}{4\pi G\rho_c^2}$:
$$\frac1{\xi^2}\partial_\xi\big(\xi^2\partial_\xi\theta\big)=-\theta^n,\qquad\text{i.e.}\quad\partial_\xi^2\theta+\frac2\xi\partial_\xi\theta+\theta^n=0.$$
- Boundary conditions at the centre: $\theta(0)=1$ and $\partial_\xi\theta(0)=0$. The surface is the first zero $\xi_1$ where $\theta=0$.
- Series start: $\theta\simeq1-\xi^2/6$ for small $\xi$ (integrate from $\xi_0=10^{-6}$ to avoid the singular $2/\xi$ term).

**Derivation to see once: mass, central density and pressure**

- Mass inside $\xi$: $m=4\pi a^3\rho_c\,(-\xi^2\partial_\xi\theta)$. At the surface $M=4\pi a^3\rho_c(-\xi_1^2\partial_\xi\theta|_1)$.
- With $R=a\xi_1$ and mean density $\bar\rho=3M/4\pi R^3$: $\dfrac{\rho_c}{\bar\rho}=\dfrac{\xi_1}{3(-\partial_\xi\theta|_1)}$.
- Central pressure: $P_c=\dfrac{4\pi G\rho_c^2a^2}{n+1}$.
- Ideal gas at the centre, $T_c=\dfrac{P_c\,\mu\,m_u}{\rho_c k}$, with $\mu$ the mean molecular weight of a fully ionised mixture, $\mu^{-1}=2X+\tfrac34Y+\tfrac12Z$.

---

## Session B: do

**Problem 1: integrate Lane–Emden for $n=3$**

- Use `scipy.integrate.solve_ivp` with `rtol=1e-11`, an event on $\theta=0$ (terminal, decreasing). Report $\xi_1$ and $\partial_\xi\theta|_1$.
- Check $-\xi_1^2\partial_\xi\theta|_1=2.01824$.

**Problem 2: build the Sun-like star**

- For $M=M_\odot,R=R_\odot$, $X=0.70,Z=0.02$, $Y=1-X-Z$: compute $\mu$, $\rho_c$, $P_c$, $T_c$.
- Cut into $N=100$ uniform shells in radius. In each shell the density is the **shell mean**, $\bar\rho_i=\Delta m_i/V_i$ with $m(r)$ from the mass formula above. This conserves total mass exactly.

**Problem 3: how bad is the toy?**

- Compare with the real Sun: $\rho_c\simeq150\ {\rm g\,cm^{-3}}$, $T_c\simeq1.57\times10^7$ K, $P_c\simeq2.4\times10^{17}$ dyn cm⁻². Which is off by how much, and why? (The real Sun is not a polytrope; its composition has changed with 4.6 Gyr of burning.)

**Problem 4: mass and density profiles**

- Plot $\rho(r)$ on a log axis and $m(r)/M$. What fraction of the mass lies inside $0.1R$ and $0.5R$?

---

## Translation: text → code

| Quantity | Formula | Code |
|---|---|---|
| Lane–Emden | $\partial_\xi^2\theta+\tfrac2\xi\partial_\xi\theta+\theta^3=0$ | `rhs = [dth, -max(th,0)**n - 2*dth/x]` |
| $\rho_c/\bar\rho$ | $\xi_1/(3(-\partial_\xi\theta\rvert_1))$ | `rho_c = rho_bar * xi1 / (3 * -dth1)` |
| $P_c$ | $4\pi G\rho_c^2a^2/(n+1)$ | `P_c = 4*pi*G*rho_c**2*(R/xi1)**2/4` |
| shell mean density | $\Delta m/V$ | `rho = dm / vol` |

---

## Contract

```text
starmc/star.py
  lane_emden(n=3.0) -> scipy OdeResult with .sol (dense), .t_events[0][0] = xi1
  polytrope_star(M=Msun, R=Rsun, X=0.70, Z=0.02, n_shells=200, spacing="uniform") -> Star
  Star attributes (cgs):
    M, R, X, Y, Z, mu, xi1, dth1, rho_c, P_c, T_c
    r_edges (n+1,), m_edges (n+1,), dm (n,), vol (n,), rho (n,), r_mid (n,)
    T (n,)  polytropic temperature  T_c * theta(r_mid)
    P (n,)  P_c * theta(r_mid)**4
```

```python
# acceptance-test
import numpy as np
from starmc.star import lane_emden, polytrope_star
from starmc import consts as C
sol = lane_emden(3.0)
xi1 = sol.t_events[0][0]
dth1 = sol.sol(xi1)[1]
assert abs(xi1 - 6.89685) < 1e-4, xi1
assert abs(-xi1**2 * dth1 - 2.01824) < 1e-4
s = polytrope_star(n_shells=100)
assert abs(s.dm.sum() / C.Msun - 1) < 1e-9
assert abs(s.mu - 0.617284) < 1e-5
rho_bar = 3 * C.Msun / (4 * np.pi * C.Rsun**3)
assert abs(s.rho_c / rho_bar - 54.18) < 0.05
assert abs(s.T_c / 1.2099e7 - 1) < 2e-3, s.T_c
assert abs(s.P_c / 1.2449e17 - 1) < 2e-3, s.P_c
assert np.all(np.diff(s.rho) < 0)
assert abs(np.interp(0.1, s.r_edges[1:] / C.Rsun, s.m_edges[1:] / C.Msun) - 0.0472) < 0.003
print("MC-09 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| $\xi_1$ | 6.89685 |
| $-\xi_1^2\partial_\xi\theta\rvert_1$ | 2.01824 |
| $\rho_c/\bar\rho$ | 54.18 |
| $\mu$ ($X=0.70,Z=0.02$) | 0.6173 |
| $\rho_c$ | 76.4 g cm⁻³ |
| $P_c$ | $1.245\times10^{17}$ dyn cm⁻² |
| $T_c$ | $1.210\times10^7$ K |
| mass inside $0.1R$ | 0.047 $M_\odot$ |

---

## Done when

- You can derive the Lane–Emden equation from hydrostatic equilibrium and the polytropic law.
- You can say how $\rho_c/\bar\rho$ and $P_c$ follow from the boundary values.
- You can list two ways in which this star is not the Sun, and why the guide still uses it.
