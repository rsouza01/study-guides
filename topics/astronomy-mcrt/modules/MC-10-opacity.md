# Module MC-10: Opacity in a stellar interior

[← MC-09](MC-09-toy-star-polytrope.md) · [README](../README.md) · [Next: MC-11 Radiative diffusion →](MC-11-radiative-diffusion.md)

**Source:** Forgan §1.1 (the definition of $\kappa_\nu$, eq 4) and §9.1.1 (Planck mean, eq 63). Stellar opacity: Carroll & Ostlie, the opacity section of the chapter on stellar interiors; Kippenhahn, Weigert & Weiss, the chapter on opacity; Hansen, Kawaler & Trimble, *Stellar Interiors*, the opacity chapter. Link back to PH-14 and PH-17 for lines and continua.

---

## Session A: read

- Forgan §1.1, eq (4), and §1.2, eq (5): $\kappa$ per unit mass, $\rho\kappa$ per unit length, the albedo.
- One of the opacity chapters above. You need four contributions:
  - **electron scattering** (Thomson): independent of $\rho$ and $T$;
  - **free–free** (bremsstrahlung) and **bound–free** (photoionisation): Kramers laws $\kappa\propto\rho T^{-7/2}$;
  - **H⁻** (important below about $10^4$ K): $\kappa\propto\rho^{1/2}T^{9}$.
- Skim PH-12, PH-13 and PH-17 for where the bound–free edges come from.

**Key ideas**

- Opacity is not one number. It is a function $\kappa_\nu(\rho,T,{\rm composition})$. Monte Carlo can use $\kappa_\nu$ directly (a frequency per packet) but a star needs a **mean** to be affordable. Which mean depends on the regime:
  - **Rosseland mean** $\kappa_R$ in the optically thick, diffusive interior;
  - **Planck mean** $\kappa_P$ for emission (eq 63).
- Opacities add: $\kappa=\kappa_{\rm es}+\kappa_{\rm ff}+\kappa_{\rm bf}+\dots$, but means of a sum are not sums of means. The Rosseland mean adds **inverse** opacities, frequency by frequency.

**The four formulas used here (cgs, $\kappa$ in cm² g⁻¹)**

$$\kappa_{\rm es}=\frac{\sigma_T(1+X)}{2m_u}=0.3405\ (X=0.70)$$
$$\kappa_{\rm ff}=3.68\times10^{22}\,g_{\rm ff}\,(1-Z)(1+X)\,\rho\,T^{-7/2}$$
$$\kappa_{\rm bf}=4.34\times10^{25}\,\frac{g_{\rm bf}}{t}\,Z(1+X)\,\rho\,T^{-7/2}$$
$$\kappa_{{\rm H}^-}=2.5\times10^{-31}\,\frac{Z}{0.02}\,\rho^{1/2}\,T^{9}$$

- $g_{\rm ff}=g_{\rm bf}=1$ here; $t$ is the Guillotine factor (about 1 to 100), set to 10.
- **Combination used by the code**: $\kappa_R\simeq\kappa_{\rm es}+\Big(\dfrac1{\kappa_{\rm ff}+\kappa_{\rm bf}}+\dfrac1{\kappa_{{\rm H}^-}}\Big)^{-1}$. The harmonic combination of "Kramers" and "H⁻" is a standard rough interpolation: whichever is smaller dominates the *transparency windows*. This is a **toy**, not a table. A real code reads OPAL or OP tables (see the README bibliography).

**Derivation to see once: electron scattering opacity**

- Thomson cross-section $\sigma_T=6.652\times10^{-25}$ cm² per electron, independent of frequency.
- Opacity per gram is (electrons per gram) $\times\,\sigma_T$.
- For fully ionised H and He, electrons per gram: $\dfrac{X+Y/2}{m_u}=\dfrac{(1+X)}{2m_u}$ (using $Y=1-X$, i.e. ignoring metals). So $\kappa_{\rm es}=0.2(1+X)\ {\rm cm^2\,g^{-1}}$, which is 0.34 for $X=0.70$.

---

## Session B: do

**Problem 1: implement the four opacities**

- Write `kappa_es(X)`, `kappa_ff(rho,T,X,Z)`, `kappa_bf(rho,T,X,Z,t)`, `kappa_hminus(rho,T,Z)` and `kappa_rosseland(rho,T,X,Z,t=10)` with array arguments.

**Problem 2: the four points**

- Evaluate at $(\rho,T)=(150,1.5\times10^7)$, $(1,10^6)$, $(10^{-7},5772)$, $(0.1,5\times10^5)$. Which process dominates at each? Report $\kappa_R$.

**Problem 3: the opacity profile of the toy star**

- Use the temperature profile of MC-11 (or, for now, the polytropic one) and plot $\kappa_R(r)$ across the toy Sun. Where is the maximum? Where does $\kappa_{\rm es}$ take over?

**Problem 4: total optical depth**

- Compute $\tau_{\rm tot}=\int_0^R\kappa_R\rho\,dr$ for the toy star (after MC-11). Compare with the order of magnitude you get from $\bar\kappa\,\bar\rho\,R$. This number drives everything from MC-16 on.

---

## Translation: text → code

| Quantity | Code |
|---|---|
| $\kappa_{\rm es}=\sigma_T(1+X)/2m_u$ | `C.sigma_T * (1+X) / (2*C.m_u)` |
| Kramers | `3.68e22*(1-Z)*(1+X)*rho*T**-3.5` |
| bound–free | `4.34e25/t*Z*(1+X)*rho*T**-3.5` |
| H⁻ | `2.5e-31*(Z/0.02)*np.sqrt(rho)*T**9` |
| Rosseland (toy) | `kes + 1/(1/(kff+kbf) + 1/khm)` |

---

## Contract

```text
starmc/opacity.py   (cgs, all arrays broadcast)
  kappa_es(X)
  kappa_ff(rho, T, X, Z, g_ff=1.0)
  kappa_bf(rho, T, X, Z, t=10.0, g_bf=1.0)
  kappa_hminus(rho, T, Z)
  kappa_rosseland(rho, T, X, Z, t=10.0)
        = kappa_es(X) + 1 / (1/(kappa_ff+kappa_bf) + 1/kappa_hminus)
```

```python
# acceptance-test
import numpy as np
from starmc.opacity import kappa_es, kappa_ff, kappa_bf, kappa_hminus, kappa_rosseland
X, Z = 0.70, 0.02
assert abs(kappa_es(X) - 0.34053) < 1e-4
r = kappa_rosseland(150.0, 1.5e7, X, Z)
assert abs(r - 2.7374) < 0.01, r
assert abs(kappa_ff(150.0, 1.5e7, X, Z) - 0.70355) < 1e-3
assert abs(kappa_bf(150.0, 1.5e7, X, Z) - 1.69333) < 1e-3
assert abs(kappa_rosseland(1.0, 1e6, X, Z) - 209.21) < 0.1
assert abs(kappa_rosseland(1e-7, 5772.0, X, Z) - 0.90249) < 2e-3
assert abs(kappa_hminus(1e-7, 5772.0, Z) - 0.56218) < 1e-3
rho = np.array([1.0, 10.0]); T = np.array([1e6, 2e6])
assert kappa_rosseland(rho, T, X, Z).shape == (2,)
print("MC-10 ok")
```

---

## Checkpoints

| $(\rho,T)$ | $\kappa_{\rm es}$ | $\kappa_{\rm ff}$ | $\kappa_{\rm bf}$ | $\kappa_{{\rm H}^-}$ | $\kappa_R$ |
|---|---|---|---|---|---|
| $(150,\,1.5\times10^7)$ | 0.341 | 0.704 | 1.693 | huge | 2.737 |
| $(1,\,10^6)$ | 0.341 | 61.3 | 147.6 | huge | 209.2 |
| $(10^{-7},\,5772)$ | 0.341 | 420 | 1010 | 0.562 | 0.902 |

- All in cm² g⁻¹.

---

## Done when

- You can derive $\kappa_{\rm es}=0.2(1+X)$ and say why it sets a floor.
- You can say why Kramers falls with temperature but H⁻ rises, and what that does to the surface layers.
- You can explain why this $\kappa_R$ is a toy and name what replaces it in a real code.
