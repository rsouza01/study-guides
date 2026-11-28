# Module MC-20: The surface layer, a grey atmosphere by Monte Carlo

[← MC-19](MC-19-the-star-engine.md) · [README](../README.md) · [Next: MC-21 Spectrum and Balmer lines →](MC-21-spectrum-and-balmer-lines.md)

**Source:** Forgan §6 (outputs: binning escaping packets by direction), §9.1 (the energy-density estimator), applied to a plane-parallel slab. Theory: Mihalas, *Stellar Atmospheres* (2nd ed.), the grey-atmosphere and Milne–Eddington sections; Carroll & Ostlie, the section on the grey atmosphere in the stellar-atmospheres chapter; Rybicki & Lightman, Ch. 1. Limb darkening: PH-27.

---

## Session A: read

- One of the grey-atmosphere references above: the Eddington approximation, the Hopf function, limb darkening.
- Forgan §6.1: why you keep the exit direction of each packet.
- Re-read MC-17: the scaled star could not give the surface.

**Key ideas**

- The interior engine cannot reach the photosphere (MC-17). The outermost layers are handled by their own small Monte Carlo: a **plane-parallel slab**, grey, conservative scattering, energy injected deep and escaping through the top.
- It answers three questions at once: the **temperature structure** $T(\tau)$, the **angular distribution** of the emergent intensity (limb darkening), and the surface value of the energy density that the scaled interior run needed in MC-17.

**Derivation to see once: the Eddington grey atmosphere**

- Constant net flux $F$. Radiative equilibrium with $J=S=B$. The first moment gives $\partial_\tau K=H$ with $H=F/4\pi$, and Eddington's closure $K=J/3$ gives $J=\dfrac{3F}{4\pi}(\tau+c_0)$.
- The constant $c_0$ comes from the boundary condition at the top, where there is no incoming radiation: $H(0)=\tfrac12J(0)$ for the two-stream form, which gives $c_0=2/3$. So
$$J(\tau)=\frac{3F}{4\pi}\Big(\tau+\frac23\Big),\qquad T^4=\frac34T_{\rm eff}^4\Big(\tau+\frac23\Big).$$
- Note $T(\tau=2/3)=T_{\rm eff}$: the temperature at optical depth 2/3 equals the effective temperature. The exact solution (Milne) replaces $2/3$ by the Hopf function $q(\tau)$, with $q(0)=0.5774$ and $q(\infty)=0.7104$ (the 3-digit fit $q=0.7104-0.1331e^{-3.4488\tau}$ is used in the code).

**Derivation to see once: limb darkening**

- The emergent intensity at angle $\theta$, $\mu=\cos\theta$, is the formal solution $I(0,\mu)=\displaystyle\int_0^\infty S(\tau)e^{-\tau/\mu}\frac{d\tau}{\mu}$.
- With $S=J=\dfrac{3F}{4\pi}(\tau+\tfrac23)$ the integral is $\dfrac{3F}{4\pi}\big(\mu+\tfrac23\big)$.
- Normalised to disc centre: $\dfrac{I(0,\mu)}{I(0,1)}=\dfrac{\mu+2/3}{1+2/3}=\dfrac{3\mu+2}{5}$. At the limb ($\mu\to0$) it is $2/5$.
- Averages over the escaping flux ($dN\propto I\mu\,d\mu$): $\langle\mu\rangle=\dfrac{\int(3\mu+2)\mu^2}{\int(3\mu+2)\mu}=0.7083$ and $\langle\mu^2\rangle=0.55$.

**What the Monte Carlo slab does**

- Packets start at $\tau_s=15$, isotropic. Free path in optical depth $-\ln(1-\zeta)$; the vertical step is $\mu\,\ell$.
- Absorb-and-re-emit is replaced by isotropic scattering (grey, LTE: MC-14).
- Bottom at $\tau_b=40$: **reflecting** (mirror image). Top at $\tau=0$: packets leave. Record the exit $\mu$.
- Tally the path length per unit optical depth in bins of $\tau$: $u\,c/F=\sum_js_j/(N\,\Delta\tau)$ (MC-14 estimator, with $\sum$ over packets).

---

## Session B: do

**Problem 1: the Eddington values**

- Implement `hopf_q(tau)` and `T_of_tau(tau, Teff)`. Check $T(2/3)\simeq T_{\rm eff}$ to about 1 % and the ratio $T(0)/T_{\rm eff}=(\tfrac34 q(0))^{1/4}=0.8113$ for the Hopf function. (With Eddington's $2/3$ it is $0.8409$.)

**Problem 2: the slab Monte Carlo**

- Implement `milne_slab(n, tau_s, tau_b, edges, seed)` with `numba`. Use bins `edges = [0, .05, .1, .2, .4, .7, 1, 2, ..., 10]`.
- Compare $u\,c/F$ with $3(\tau+q(\tau))$ and with Eddington's $3(\tau+2/3)$.

**Problem 3: limb darkening**

- Histogram $\mu_{\rm exit}$ in 10 bins. Convert to intensity: $I(\mu)\propto\dfrac{dN/d\mu}{\mu}$. Normalise to the last bin, and compare with $(3\mu+2)/5$.
- Which is right at the limb, Eddington or the Monte Carlo? (The exact solution lies below Eddington there; the MC gives about 0.415 at $\mu=0.05$ against 0.43.)

**Problem 4: the surface value for MC-17**

- The rescaling formula of MC-17 needs a surface value $u_s$. From Problem 2 at the top bin, $u_s=(F/c)\,(uc/F)_{\tau\to0}$ with $F=\sigma T_{\rm eff}^4$. Show that this is $u_s\simeq1.9\,\sigma T_{\rm eff}^4/c=0.47\,aT_{\rm eff}^4$.
- In MC-17 and MC-19 you used $aT^4$ of the outermost RE shell instead. Show that at $0.5R$ the two choices differ by less than one part in $10^{6}$ in $u$, because $u_s\ll u$ in the deep interior. The surface value only matters where $\tau'_{\rm out}\lesssim10$.

---

## Translation: text → code

| Quantity | Code |
|---|---|
| free path | `l = -np.log(1.0 - np.random.random())` |
| vertical step | `z_new = z + mu*l` |
| reflecting bottom | `if z_new > tau_b: z_new = 2*tau_b - z_new; mu = -mu` |
| exit | `if z_new < 0: mu_exit = abs(mu)` |
| path tally per bin | overlap of $[z,z_{\rm new}]$ with the bin, scaled by $\ell/\lvert z_{\rm new}-z\rvert$ |

---

## Contract

```text
starmc/atmosphere.py
  hopf_q(tau) -> 0.7104 - 0.1331 exp(-3.4488 tau)
  T_of_tau(tau, Teff) -> Teff * (0.75*(tau + hopf_q(tau)))**0.25
  milne_slab(n, tau_s=15.0, tau_b=40.0, edges=None, seed=1) -> dict
      edges (nb+1,), ucF (nb,), mu_exit (n,), nsc (n,)
```

```python
# acceptance-test
import numpy as np
from starmc.atmosphere import hopf_q, T_of_tau, milne_slab
assert abs(hopf_q(0.0) - 0.5773) < 1e-3
assert abs(hopf_q(50.0) - 0.7104) < 1e-9
assert abs(T_of_tau(2 / 3, 5772.0) / 5772.0 - 1) < 0.01
assert abs(T_of_tau(0.0, 5772.0) / 5772.0 - (0.75 * hopf_q(0.0)) ** 0.25) < 1e-12
o = milne_slab(150_000, seed=2)
e = o["edges"]
mid = 0.5 * (e[1:] + e[:-1])
ref = 3 * (mid + hopf_q(mid))
assert np.all(np.abs(o["ucF"] / ref - 1) < 0.04), o["ucF"] / ref
mu = o["mu_exit"]
assert abs(mu.mean() - 0.711) < 0.004 and abs((mu**2).mean() - 0.553) < 0.004
h, b = np.histogram(mu, bins=np.linspace(0, 1, 11))
c = 0.5 * (b[1:] + b[:-1])
I = h / np.diff(b) / c
I /= I[-1]
ref_I = np.array([0.415, 0.479, 0.549, 0.615, 0.677, 0.746, 0.814, 0.872, 0.942, 1.0])
assert np.all(np.abs(I - ref_I) < 0.04), I
print("MC-20 ok")
```

---

## Checkpoints

| $\tau$ (bin centre) | MC $u c/F$ | $3(\tau+q)$ | Eddington $3(\tau+2/3)$ |
|---|---|---|---|
| 0.025 | 1.87 | 1.84 | 2.08 |
| 0.3 | 2.88 | 2.89 | 2.90 |
| 1.5 | 6.60 | 6.63 | 6.50 |
| 5.5 | 18.60 | 18.63 | 18.50 |

| Quantity | Value |
|---|---|
| $\langle\mu\rangle$, $\langle\mu^2\rangle$ of escaping packets | 0.711, 0.553 (Eddington 0.7083, 0.55) |
| $I(\mu=0.05)/I(0.95)$ | 0.415 (Eddington 0.43) |
| $T(0)/T_{\rm eff}$ | 0.811 |
| slab cost | about 1550 scatterings per packet, 25 s for $4\times10^5$ packets in numba |

---

## Done when

- You can derive $T^4=\tfrac34T_{\rm eff}^4(\tau+\tfrac23)$ and $(3\mu+2)/5$ from the two-stream closure.
- You can say why $T=T_{\rm eff}$ at $\tau=2/3$ and what limb darkening tells you about the temperature gradient.
- You can say which part of the star this module replaces and why the interior engine could not do it.
