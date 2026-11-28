# Module MC-24: Capstone, the functioning star

[← MC-23](MC-23-inverse-problem.md) · [README](../README.md)

**Source:** assembles MC-01 to MC-23. Forgan's pipeline (§§2–7 and §9.1) supplies the Monte Carlo skeleton; the stellar physics, the scalings and the atmosphere are the additions of this guide.

---

## Session A: read

- Re-read the README section "Capstone architecture" and the **Limits** list there. This module is honest about what the simulator is not.
- Skim your own contract lists of MC-09, MC-13, MC-17, MC-19, MC-20, MC-21, MC-22 and MC-23. You will connect them, not rewrite them.

**The pipeline, in the order a photon would see it**

```text
 1. structure      MC-09  polytrope density, shells
 2. opacity        MC-10  Rosseland kappa(rho, T)
 3. temperature    MC-11, MC-12, MC-13  radiative equilibrium + convective core
 4. interior MC    MC-17, MC-19, MC-14  opacity-scaled packets, path-length estimator
                   -> checks T(r) for r < 0.5 R   (the validated region)
 5. surface        MC-20  grey atmosphere, T(tau), limb darkening
 6. spectrum       MC-21  Saha, Balmer lines, emergent flux
 7. detector       MC-22  distance, filters, magnitudes, counts, noise
 8. inverse        MC-23  colour temperature, angular size, T-X degeneracy
```

**What each stage guarantees, and what it does not**

- Stages 1 to 3: deterministic. The temperature is a radiative-equilibrium solution **for a fixed polytropic density**; hydrostatic equilibrium is not re-solved.
- Stage 4: Monte Carlo, validated to a few per cent for $r\le0.5R$ (the toy $\tau'_{\rm out}\ge8$ there). Not validated further out.
- Stage 5 and 6: the photosphere is a separate small problem, matched to the star only through $T_{\rm eff}$ and $\log g$.
- Stage 7: for a spherical star the observed flux is exactly the surface flux times $(R/d)^2$. Packets are used to teach noise, and to prepare for non-spherical stars.
- Stage 8: shows how far a clean model is from a clean inference.

---

## Session B: do

**Problem 1: the interior in one call**

- Write `run_interior(n_shells=100, tau_target=300, n_packets=3000, seed=5)`: build the star, solve the RE temperature with the convective core, scale the opacity, emit packets from the nuclear sources, run the engine, estimate $u$, rescale, return the dictionary below. Compare $T_{\rm MC}/T_{\rm RE}$ at $0.2$–$0.5R$ (within 4 %).

**Problem 2: the surface**

- Write `surface_teff(L, R)` and `surface_logg(M, R)`. For $L_\odot,R_\odot,M_\odot$: $T_{\rm eff}=5772$ K and $\log g=4.438$.

**Problem 3: the observed spectrum**

- Write `observe(L, R, M, d_cm, lam_nm, X, a_damp)` returning $F_\lambda$ in W m⁻² nm⁻¹ with and without lines, using `emergent_flux` and the dilution $(R/d)^2$. Conversions: $F_\lambda=F_\nu c/\lambda^2$ per unit wavelength; $1$ erg s⁻¹ cm⁻² = $10^{-3}$ W m⁻².
- Check the bolometric integral over 50 nm–100 μm equals $L/4\pi d^2$ to 0.3 %.

**Problem 4: the end-to-end test**

- At 10 pc compute three things, each on its own wavelength grid: $B-V$ relative to the 10000 K blackbody on 250–1200 nm with 4001 points (the filters need their wings); the H$\alpha$ equivalent width from the observed spectrum on a fine grid, 653.28–659.28 nm with 1201 points (the line is narrower than the 0.24 nm step of the coarse grid); the colour temperature from `fit_blackbody` on 380–720 nm. Report them in a results table.
- Check that the H$\alpha$ equivalent width recovered from the observed spectrum equals `equivalent_width_nm("Halpha", Teff)`.

**Problem 5 (open): change the star**

- Rerun the whole chain for a different composition ($X=0.5$, $Z=0.02$) and for a different mass and radius (say $M=1.5M_\odot$, $R=1.5R_\odot$; the polytrope code takes $M$ and $R$ as arguments). There are **no reference numbers** for these runs: you are exploring. Record what changes in the convective core, in $T_{\rm eff}$, in the Balmer lines and in the colours.
- Expect a convective core to be physically correct for the more massive star; but the solar-mass toy still has the wrong envelope (MC-13). Keep the two statements apart.

---

## Translation: text → code

| Stage | Call |
|---|---|
| interior | `run_interior(...)` |
| surface | `surface_teff`, `surface_logg` |
| spectrum | `observe(...)` which calls `emergent_flux` |
| photometry | `colour(lam, F, planck_lambda(lam, 1e4), "B", "V")` |
| inverse | `fit_blackbody`, `angular_diameter`, `invert_teff_from_ew` |

---

## Contract

```text
starmc/pipeline.py
  surface_teff(L, R) -> (L/(4 pi R^2 sigma))**0.25        cgs
  surface_logg(M, R) -> log10(G M / R^2)                  cgs
  observe(L, R, M, d_cm, lam_nm, X=0.7, a_damp=0.05) -> (F_lam, F_lam_cont)   W m^-2 nm^-1
  run_interior(n_shells=100, tau_target=300.0, n_packets=3000, seed=5,
               M=Msun, R=Rsun, X=0.70, Z=0.02) -> dict
      star (Star), T_re (n,), T_mc (n,), conv (n,) bool, S (scale factor),
      tau (total optical depth), done (bool), t_yr (mean exit time, years)
```

```python
# acceptance-test
import numpy as np
from starmc.pipeline import surface_teff, surface_logg, observe, run_interior
from starmc.photometry import colour, planck_lambda
from starmc.inverse import fit_blackbody
from starmc.lines import equivalent_width_nm
from starmc import consts as C
assert abs(surface_teff(C.Lsun, C.Rsun) - 5772.0) < 0.5
assert abs(surface_logg(C.Msun, C.Rsun) - 4.438) < 0.002
r = run_interior()
s = r["star"]
assert r["done"] and 12 <= r["conv"].sum() <= 18
for f in (0.2, 0.3, 0.4, 0.5):
    i = np.searchsorted(s.r_edges[1:] / C.Rsun, f)
    assert abs(r["T_mc"][i] / r["T_re"][i] - 1) < 0.04, (f, r["T_mc"][i] / r["T_re"][i])
assert 1.7e4 < r["t_yr"] < 2.3e4, r["t_yr"]
d = 10 * C.pc
wide = np.logspace(np.log10(50), np.log10(1e5), 6000)
F, Fc = observe(C.Lsun, C.Rsun, C.Msun, d, wide)
L_obs = C.Lsun * 1e-7 / (4 * np.pi * (d * 1e-2) ** 2)
assert abs(np.trapezoid(F, wide) / L_obs - 1) < 3e-3, np.trapezoid(F, wide) / L_obs
lam = np.linspace(250.0, 1200.0, 4001)
F, Fc = observe(C.Lsun, C.Rsun, C.Msun, d, lam)
assert abs(colour(lam, F, planck_lambda(lam, 1e4), "B", "V") - 0.4516) < 0.005
lw = np.linspace(653.28, 659.28, 1201)
F, Fc = observe(C.Lsun, C.Rsun, C.Msun, d, lw)
W = np.trapezoid(1 - F / Fc, lw)
assert abs(W - equivalent_width_nm("Halpha", 5772.0)) < 0.005, W
lf = np.linspace(380.0, 720.0, 3401)
F, Fc = observe(C.Lsun, C.Rsun, C.Msun, d, lf)
T, _ = fit_blackbody(lf, F)
assert 5900 < T < 6150, T
print("MC-24 ok")
```

---

## Checkpoints (the toy Sun)

| Quantity | Value |
|---|---|
| $T_{\rm eff}$, $\log g$ | 5772 K, 4.438 |
| convective core | 15 of 100 shells, $r<0.15R$; $T_c=1.58\times10^7$ K |
| $T_{\rm MC}/T_{\rm RE}$, $0.2$–$0.5R$ | 1.005, 1.007, 1.005, 1.015 |
| mean exit time (distributed source, scaled star) | $1.98\times10^4$ yr |
| $B-V$ (toy filters, 10000 K blackbody reference, 250–1200 nm) | 0.452 (0.449 without lines) |
| H$\alpha$ equivalent width | 0.317 nm |
| colour temperature from the shape fit | about 6000 K |
| $L_\odot/4\pi(10\,{\rm pc})^2$ | $3.199\times10^{-10}$ W m⁻² |

---

## Done when

- You can run the whole chain from one script and say, for every number in the results table, which stage produced it and how much to trust it.
- You can name the limits of the simulator (the README list) and say which would be first to remove.
- You can explain what changes when you move from a spherical star to a spotted or binary one (the observer sees only some packets; the dilution shortcut disappears).
