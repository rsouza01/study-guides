# Module MC-12: Nuclear energy sources as a diffuse emitter

[← MC-11](MC-11-radiative-diffusion.md) · [README](../README.md) · [Next: MC-13 Convection →](MC-13-convection.md)

**Source:** Forgan §3, eq (17) and the discussion of "point source emission" in §9.1, p. 18. Nuclear rates: Hansen, Kawaler & Trimble, *Stellar Interiors*, the chapters on nuclear reactions and on hydrogen burning; Carroll & Ostlie, the pp-chain and CNO-cycle sections; Kippenhahn, Weigert & Weiss, the chapter on nuclear reaction rates. (Look up by title.)

---

## Session A: read

- Forgan §3, eq (17): energy sources are sampled in proportion to their luminosity.
- One of the nuclear references above for the pp chain, the CNO cycle and the Gamow peak.

**Key ideas**

- Forgan emits packets from a **point** source (a star in a dust disc) or from emitting cells (eq 20). A stellar core is neither. The luminosity is **distributed**: shell $i$ produces $\Delta L_i=\epsilon_i\,\Delta m_i$, with $\epsilon$ in erg g⁻¹ s⁻¹.
- So the packet count in shell $i$ is $N_i=N_{\rm tot}\Delta L_i/L$ (eq 17 again), and the radius inside the shell is sampled uniformly in volume (MC-03, `sample_radius_from_shells`).
- Only the **temperature dependence** of $\epsilon$ matters here: we rescale $\sum_i\Delta L_i=L_\odot$. The absolute normalisation of a real burning calculation does not enter.

**The two rates used (cgs; $T_9=T/10^9$ K)**

$$\epsilon_{\rm pp}=2.4\times10^{4}\,\rho X^2\,T_9^{-2/3}\,e^{-3.380/T_9^{1/3}}$$
$$\epsilon_{\rm CNO}=4.4\times10^{25}\,\rho X X_{\rm CNO}\,T_9^{-2/3}\,e^{-15.228/T_9^{1/3}-(T_9/0.8)^2}$$

with $X_{\rm CNO}=0.7Z$.

**Derivation to see once: where the $-3.380/T_9^{1/3}$ comes from**

- Two nuclei of charges $Z_1,Z_2$ must tunnel through a Coulomb barrier. The tunnelling probability at relative energy $E$ is $\propto e^{-\sqrt{E_G/E}}$ with the Gamow energy $E_G=2m_rc^2(\pi\alpha Z_1Z_2)^2$ ($m_r$ the reduced mass, $\alpha$ the fine-structure constant).
- The thermal tail is $\propto e^{-E/kT}$. So the rate integrand is $e^{-E/kT-\sqrt{E_G/E}}$.
- It peaks where the derivative of the exponent vanishes: $-\dfrac1{kT}+\dfrac12\sqrt{E_G}E^{-3/2}=0$, so $E_0=\Big(\dfrac{\sqrt{E_G}\,kT}{2}\Big)^{2/3}$.
- At the peak the exponent equals $-3E_0/kT=-3\Big(\dfrac{E_G}{4kT}\Big)^{1/3}$ (check: $E_0/kT=(E_G/4kT)^{1/3}$).
- Number check for $p+p$: $m_r=m_p/2$ gives $E_G=m_pc^2(\pi\alpha)^2=0.493$ MeV. With $kT=0.08617\,T_9$ MeV, $3(E_G/4kT)^{1/3}=3.381/T_9^{1/3}$. This is the 3.380.
- Number check for $p+{}^{14}$N: $Z_1Z_2=7$, $m_r\simeq0.933\,m_u$ gives $E_G=44.8$ MeV and $15.20/T_9^{1/3}$, close to the 15.228.
- The **local temperature exponent** $\nu=\partial\ln\epsilon/\partial\ln T$ follows: for pp, $\nu\simeq\dfrac{3.38}{3T_9^{1/3}}-\dfrac23\simeq4.2$ at $1.2\times10^7$ K. For CNO it is about 21. This is why CNO takes over only in hotter, more massive stars.

---

## Session B: do

**Problem 1: the rates**

- Implement `eps_pp`, `eps_cno`, `eps_total(rho,T,X,Z)`. Evaluate at the toy-star centre ($\rho=76.4$, $T=1.21\times10^7$, $X=0.70$, $Z=0.02$). Which dominates?

**Problem 2: the exponent**

- Compute $\nu_{\rm pp}$ and $\nu_{\rm CNO}$ numerically by a centred difference of $\ln\epsilon$ in $\ln T$ and compare with the formula above.

**Problem 3: the luminosity profile**

- Implement `luminosity_profile(star, T, Ltot)` returning $L(r)$ at the outer edge of each shell and the per-shell $\Delta L$. Use the polytropic temperature. At which radius does $L(r)$ reach $L_\odot/2$? What fraction is inside $0.1R$?

**Problem 4: packets from a diffuse source**

- Choose $N=10^5$ packets, assign them to shells with `packet_counts`, and place them with `sample_radius_from_shells`. Verify that the radial histogram, weighted by shell volume, reproduces $\Delta L_i$.

---

## Translation: text → code

| Forgan | Meaning | Code |
|---|---|---|
| eq (17) | $N_i=N_{\rm tot}L_i/L$ | `packet_counts(dL, N)` |
| §9.1, "only point source emission needs to be added" | distributed source here | `sample_radius_from_shells(rng, r_edges, dL, N)` |
| — | $\Delta L_i=\epsilon_i\Delta m_i$ | `dL = eps * star.dm`, then rescale |

---

## Contract

```text
starmc/thermal.py
  eps_pp(rho, T, X)
  eps_cno(rho, T, X, Xcno)
  eps_total(rho, T, X, Z)           = eps_pp + eps_cno(Xcno = 0.7 Z)
  luminosity_profile(star, T, Ltot=Lsun) -> (L_outer_edge (n,), dL (n,))
```

```python
# acceptance-test
import numpy as np
from starmc.star import polytrope_star
from starmc.thermal import eps_pp, eps_cno, eps_total, luminosity_profile
from starmc import consts as C
s = polytrope_star(n_shells=100)
e1 = eps_pp(s.rho[0], s.T[0], 0.7)
e2 = eps_cno(s.rho[0], s.T[0], 0.7, 0.014)
assert abs(e1 - 6.862) < 0.02 and abs(e2 - 0.00968) < 2e-4, (e1, e2)
assert abs(eps_total(s.rho[0], s.T[0], 0.7, 0.02) - (e1 + e2)) < 1e-9
T = np.array([1.2e7, 1.2e7 * 1.001])
nu = np.diff(np.log(eps_pp(1.0, T, 0.7))) / np.diff(np.log(T))
assert abs(nu[0] - 4.24) < 0.1, nu
L, dL = luminosity_profile(s, s.T)
assert abs(L[-1] / C.Lsun - 1) < 1e-9 and abs(dL.sum() / C.Lsun - 1) < 1e-9
assert np.all(dL >= 0) and np.all(np.diff(L) >= 0)
rh = s.r_edges[1:] / C.Rsun
assert abs(np.interp(0.5, L / C.Lsun, rh) - 0.128) < 0.01
assert abs(np.interp(0.1, rh, L / C.Lsun) - 0.311) < 0.02
print("MC-12 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| $\epsilon_{\rm pp}$ at the toy centre | 6.86 erg g⁻¹ s⁻¹ (before rescaling) |
| $\epsilon_{\rm CNO}$ at the toy centre | 0.0097 erg g⁻¹ s⁻¹ |
| $\nu_{\rm pp}$ at $1.2\times10^7$ K | about 4.2 |
| $L_\odot/2$ radius (polytropic $T$) | $0.128\,R_\odot$ |
| fraction of $L$ inside $0.1R$ | 0.31 |

---

## Done when

- You can derive the Gamow peak energy and the exponent $3(E_G/4kT)^{1/3}$, and reproduce the 3.38 for $p+p$.
- You can say why the nuclear source is spread over the core and why this means "emit from shells" rather than "emit from a point".
- You can explain what the rescaling to $L_\odot$ throws away and why that is acceptable here.
