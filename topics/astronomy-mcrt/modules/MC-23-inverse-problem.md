# Module MC-23: The inverse problem, from light back to the star

[← MC-22](MC-22-detecting-the-star.md) · [README](../README.md) · [Next: MC-24 Capstone →](MC-24-capstone-the-functioning-star.md)

**Source:** Forgan §6 (outputs as data) and §7 (errors) set the stage; the fits follow PH-22 (effective temperature), PH-24 (colour temperature), PH-25 (ionisation and excitation temperatures). Background: Gray, *The Observation and Analysis of Stellar Photospheres*, the chapters on temperature and on abundance analysis; Hogg, Bovy & Lang (2010), *Data analysis recipes: fitting a model to data* (arXiv:1008.4686).

---

## Session A: read

- PH-24 (colour temperature) and PH-22 (effective temperature).
- Hogg et al. (2010) on least squares and why the errors enter as weights.
- Your own MC-21 table of $W({\rm H}\alpha)$ against $T_{\rm eff}$.

**Key ideas**

- Everything so far was forward: star in, spectrum out. A telescope gives the opposite, spectrum in, star out. You fit the model to the data.
- Several "temperatures" are different numbers for the same star:
  - **effective temperature** from $L=4\pi R^2\sigma T_{\rm eff}^4$ (the definition);
  - **colour temperature**, the $T$ of the Planck curve that matches the *shape* of the spectrum;
  - **excitation / ionisation temperatures** from line strengths.
  They agree only for a perfect blackbody.
- Fitting a Planck curve to the toy Sun's spectrum returns about **6000 K**, not 5772 K: the model spectrum is not a blackbody (grey atmosphere, Balmer lines). That is a **systematic error** of about 4 %, larger than the statistical error of a good dataset.
- **Degeneracy.** Two parameters that affect the data in nearly the same way cannot be separated. In this toy, the hydrogen fraction $X$ and $T_{\rm eff}$ both change the strength of H$\alpha$.

**Derivation to see once: angular diameter from flux and $T$**

- Surface flux $\sigma T_{\rm eff}^4$. Observed flux $F=\sigma T_{\rm eff}^4(R/d)^2=\sigma T_{\rm eff}^4(\theta/2)^2$ with $\theta=2R/d$ the angular diameter in radians.
- So $\theta=2\sqrt{F/(\sigma T_{\rm eff}^4)}$. (PH-22, Karttunen eq 5.26.) If you plug in a **colour** temperature instead of $T_{\rm eff}$, $\theta$ is wrong by $(T_{\rm eff}/T_{\rm col})^2$: 7.5 % low for 6000 against 5772.

**Derivation to see once: the weighted least-squares fit and its error**

- Minimise $\chi^2=\sum_i\big[(d_i-m_i(\mathbf p))/\sigma_i\big]^2$ with $\sigma_i$ the Poisson error of each datum.
- Near the minimum, $\chi^2\simeq\chi^2_{\min}+\Delta\mathbf p^{\!\top}\,\mathsf H\,\Delta\mathbf p$ with $\mathsf H_{jk}=\tfrac12\partial_{p_j}\partial_{p_k}\chi^2$. The covariance matrix of the fit parameters is $\mathsf H^{-1}$ (for $\chi^2$ normalised as above). Its diagonal gives the parameter variances; the off-diagonals give the **degeneracies**.

---

## Session B: do

**Problem 1: recover a blackbody**

- Implement `fit_blackbody(lam_nm, F_lam, sigma=None, T0=6000)` with `scipy.optimize.least_squares` on $(T,\ln A)$ for $F_\lambda=A\,B_\lambda(T)$ (shape fit, amplitude free). Feed it an exact 7000 K Planck curve on 380–720 nm; it must return 7000 K.

**Problem 2: recover a real model**

- Generate the toy Sun spectrum with lines (MC-21) on 380–720 nm, add Poisson noise for $4\times10^4$ counts at the peak, and fit. Report $T$. Repeat for $T_{\rm eff}=8000$ K.

**Problem 3: angular diameter**

- Implement `angular_diameter(F_Wm2, T_eff)`. For $F=1361.17$ W m⁻² and 5772 K: 1918″. Redo with the colour temperature from Problem 2 and report the error.

**Problem 4: the $T$–$X$ degeneracy**

- `invert_teff_from_ew(ew_obs, name, X, bracket)` finds the $T_{\rm eff}$ where the model equivalent width matches. Generate $W({\rm H}\alpha)$ for $T_{\rm eff}=7500$, $X=0.7$. Invert it assuming $X=0.5$ and $0.9$.
- Repeat with H$\beta$. Show that both lines give almost the same $T$ for a given $X$ and that $W({\rm H}\beta)/W({\rm H}\alpha)$ is nearly independent of $X$. What does that say about breaking the degeneracy? (You need a different species, or the Balmer jump, or gravity-sensitive features.)

---

## Translation: text → code

| Quantity | Code |
|---|---|
| shape fit | `least_squares(res, [T0, log(A0)], x_scale=[1000, 1])` |
| residual | `(A*B_lam(T) - F)/F.max()` weighted by $1/\sigma$ |
| $\theta$ | `2*np.sqrt(F/(sigma*T**4))` |
| EW inversion | `brentq(lambda T: EW(T, X) - ew_obs, lo, hi)` |

---

## Contract

```text
starmc/inverse.py
  fit_blackbody(lam_nm, F_lam, sigma=None, T0=6000.0) -> (T, A)
  angular_diameter(F_Wm2, T_eff) -> radians
  invert_teff_from_ew(ew_obs, name, X, bracket=(5000, 9500)) -> Teff
```

```python
# acceptance-test
import numpy as np
from starmc.inverse import fit_blackbody, angular_diameter, invert_teff_from_ew
from starmc.lines import emergent_flux, equivalent_width_nm
from starmc import consts as C
lam = np.linspace(380.0, 720.0, 300)
def Bl(l_nm, T):
    l = l_nm * 1e-7
    return 2 * C.h * C.c**2 / l**5 / np.expm1(C.h * C.c / (l * C.k * T))
T, A = fit_blackbody(lam, Bl(lam, 7000.0))
assert abs(T - 7000.0) < 1.0, T
th = angular_diameter(1361.17, 5772.0)
assert abs(np.degrees(th) * 3600 - 1918.5) < 1.0
Fnu, Fc, *_ = emergent_flux(lam, 5772.0)
Fl = Fnu * C.c / (lam * 1e-7) ** 2
rng = np.random.default_rng(3)
obs = rng.poisson(Fl / Fl.max() * 4e4).astype(float)
Tfit, _ = fit_blackbody(lam, obs, sigma=np.sqrt(np.maximum(obs, 1.0)))
assert 5900 < Tfit < 6150, Tfit
ew = equivalent_width_nm("Halpha", 7500.0, X=0.7)
t7 = invert_teff_from_ew(ew, "Halpha", 0.7)
t5 = invert_teff_from_ew(ew, "Halpha", 0.5)
t9 = invert_teff_from_ew(ew, "Halpha", 0.9)
assert abs(t7 - 7500.0) < 2.0
assert abs(t5 - 7684.0) < 30.0 and abs(t9 - 7368.0) < 30.0
print("MC-23 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| fit of the exact 7000 K Planck curve | 7000 K |
| colour temperature of the toy Sun (noisy fit) | about 6000 K (+4 %) |
| colour temperature of the 8000 K model | about 8230 K (+2.9 %) |
| angular diameter of the Sun at 1 AU ($F=1361.17$, 5772 K) | 1918″ |
| $T$ from H$\alpha$ at fixed $X=0.5,0.7,0.9$ | 7684, 7500, 7368 K |
| $T$ from H$\beta$ at $X=0.5,0.7,0.9$ | 7698, 7500, 7358 K |
| $W({\rm H}\beta)/W({\rm H}\alpha)$ at the inferred $T$ | 0.607, 0.612, 0.616 |

---

## Done when

- You can explain why a blackbody fit gives the wrong $T_{\rm eff}$ for a real spectrum and how big the error is here.
- You can show how a wrong $T$ propagates into the angular diameter.
- You can say why two lines of the same series cannot break the $T$–$X$ degeneracy and name what would.
