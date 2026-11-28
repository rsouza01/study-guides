# Module MC-21: The emergent spectrum and the Balmer lines

[← MC-20](MC-20-grey-atmosphere.md) · [README](../README.md) · [Next: MC-22 Detecting the star →](MC-22-detecting-the-star.md)

**Source:** Forgan §1.1, eqs (2)–(4) (the transfer equation with a line opacity added to the continuum) and §6 (spectra by binning). Atomic physics: PH-12 to PH-17 (hydrogen levels, Boltzmann, line profiles), PH-25 (Saha, excitation and ionisation). Background: Gray, *The Observation and Analysis of Stellar Photospheres* (3rd ed.), the chapters on line absorption and on the formation of spectral lines; Carroll & Ostlie, the section on the Balmer lines and the Saha–Boltzmann discussion.

---

## Session A: read

- PH-16 (Boltzmann) and PH-25 (Saha) for the populations; PH-14 for line profiles.
- One reference above on the strength of the Balmer lines against temperature.

**Key ideas**

- Add a line opacity to the grey continuum opacity: $\kappa_\nu=\kappa_c\,(1+\eta_\nu)$ with $\eta_\nu=\kappa_{\rm line}/\kappa_c$. Then $d\tau_\nu=(1+\eta_\nu)\,d\tau_c$.
- The emergent flux at frequency $\nu$ comes from the layer where $\tau_\nu\sim1$. In a line core that layer is higher and cooler, so the flux is lower: an **absorption line**.
- A Balmer line needs hydrogen in level $n=2$. At low $T$ almost none is excited; at high $T$ hydrogen is ionised. So the line strength **peaks at an intermediate temperature**.

**Derivation to see once: Saha ionisation for pure hydrogen**

- The ratio of ionised to neutral populations for a gas in thermal equilibrium is
$$\frac{n_pn_e}{n_{\rm H}}=\frac{2g_+}{g_0}\Big(\frac{2\pi m_ekT}{h^2}\Big)^{3/2}e^{-\chi/kT}$$
with $g_+=1$ (proton), $g_0=2$ (hydrogen ground state), the factor 2 being the electron's spin. So $\dfrac{2g_+}{g_0}=1$ and $\chi=13.598$ eV.
- Let $x$ be the ionised fraction of hydrogen nuclei, $n_{\rm tot}=\rho X/m_u$. Then $n_p=n_e=xn_{\rm tot}$ and $n_{\rm H}=(1-x)n_{\rm tot}$. Define $S=\dfrac1{n_{\rm tot}}\Big(\dfrac{2\pi m_ekT}{h^2}\Big)^{3/2}e^{-\chi/kT}$.
- Then $x^2/(1-x)=S$, whose positive root is $x=\tfrac12\big(-S+\sqrt{S^2+4S}\big)$.
- This takes electrons from hydrogen only; helium and metals are neglected (a toy).

**Derivation to see once: the occupation of level $n=2$**

- Boltzmann: $n_2/n_{\rm H}=\dfrac{g_2e^{-E_2/kT}}{Z}$ with $g_n=2n^2$, $E_n=13.598\,(1-1/n^2)$ eV above the ground state, and $Z=\sum_ng_ne^{-E_n/kT}$.
- The sum diverges for an isolated atom. Truncate at $n_{\max}=12$ (a stand-in for pressure ionisation, which lowers the highest bound level).

**The line opacity per gram**

$$\kappa_{\rm line}(\nu)=\frac{\pi e^2}{m_ec}\,f_{lu}\,\frac{n_2}{\rho}\,\big(1-e^{-h\nu/kT}\big)\,\phi(\nu)$$

- $\dfrac{\pi e^2}{m_ec}$ is the classical integrated cross-section of a bound electron treated as a damped oscillator; $f_{lu}$ (the oscillator strength) is the quantum correction: $f=0.6407,\,0.1193,\,0.0447$ for H$\alpha$ (656.28 nm), H$\beta$ (486.13 nm), H$\gamma$ (434.05 nm).
- $(1-e^{-h\nu/kT})$ corrects for stimulated emission.
- $\phi(\nu)$ is the Voigt profile in frequency, normalised to 1. Doppler part: Gaussian of standard deviation $\sigma_D=\Delta\nu_D/\sqrt2$ with $\Delta\nu_D=\dfrac{\nu_0}{c}\sqrt{2kT/m_u+\xi^2}$ ($\xi=1$ km s⁻¹ microturbulence). Lorentz part: half-width $\gamma=a\,\Delta\nu_D$ with $a=0.05$ (a **constant** damping; a real code uses Stark and van der Waals widths).
- `scipy.special.voigt_profile(x, sigma, gamma)`.

**The formal solution used**

- LTE, no line scattering: $S_\nu=B_\nu(T)$. The flux is $F_\nu=2\pi\displaystyle\int_0^\infty B_\nu(T(\tau_c))\,(1+\eta_\nu)\,E_2(\tau_\nu)\,d\tau_c$, with $E_2$ the second exponential integral (`scipy.special.expn(2, ·)`).
- $T(\tau_c)$ is the grey structure of MC-20. Hydrostatic equilibrium with constant $\kappa_c=0.4$ cm² g⁻¹ gives $P_{\rm gas}=g\tau_c/\kappa_c$; the density follows from the ideal gas with $\mu^{-1}=X(1+x)+Y/4$, iterated with Saha (40 sweeps, damping 0.5, starting at $x=0.01$).

---

## Session B: do

**Problem 1: populations**

- Implement `saha_x(rho, T, X)` and `level_fraction(T, n=2, nmax=12)`. Check $x=1.81\times10^{-4}$ at $(\rho,T)=(1.23\times10^{-7},5808)$ and $x=0.246$ at $(10^{-8},10^4)$.

**Problem 2: the atmosphere structure**

- Implement `atmosphere_structure(Teff, logg, kappa_c, X, tau_grid)` returning $(T,P_{\rm gas},\rho,x)$. For the Sun ($T_{\rm eff}=5772$, $\log g=4.44$) at $\tau=0.67$: $T=5808$ K, $P=4.61\times10^4$ dyn cm⁻², $\rho=1.23\times10^{-7}$ g cm⁻³.

**Problem 3: line opacity and the flux**

- Implement `line_opacity`, `planck_nu` and `emergent_flux(lam_nm, Teff, logg, kappa_c, X, names, a_damp)`. Use $\tau_c=$ `np.logspace(-4, 2, 500)`.
- First switch the lines off and check that $\int F^{c}_\nu d\nu=\sigma T_{\rm eff}^4$ to $10^{-3}$ (over 50 nm to 100 μm). This validates the structure and the formal solution before any line is added.

**Problem 4: the strength of H$\alpha$ against temperature**

- `equivalent_width_nm(name, Teff, ...)`: $W=\int(1-F/F^c)\,d\lambda$ over $\lambda_0\pm3$ nm with 1201 points. Compute it for $T_{\rm eff}=4000$–$20000$ K. Find the maximum. Explain it in terms of the two populations above.
- Is the $W_{\rm max}$ temperature right? (The real maximum of the Balmer lines is near A0, about $9500$ K; this toy peaks at about 11000 K. Name two missing ingredients.)

---

## Translation: text → code

| Quantity | Code |
|---|---|
| Saha root | `0.5*(-S + np.sqrt(S*S + 4*S))` |
| $n_2$ | `(rho*X/m_u)*(1-x)*level_fraction(T, 2)` |
| Doppler width | `dnuD = nu0/c*np.sqrt(2*k*T/m_u + (xi*1e5)**2)` |
| Voigt | `voigt_profile(nu - nu0, dnuD/np.sqrt(2), a*dnuD)` |
| optical depth | cumulative trapezoid of $(1+\eta)$ over $\tau_c$ |
| flux | `2*np.pi*np.trapezoid(B*(1+eta)*expn(2, tau_nu), tau_c)` plus the first-cell term |

---

## Contract

```text
starmc/lines.py   (cgs)
  saha_x(rho, T, X)
  level_fraction(T, n=2, nmax=12)
  atmosphere_structure(Teff, logg, kappa_c, X, tau_grid) -> (T, Pg, rho, x)
  line_opacity(lam_nm, name, T, rho, x, X, a_damp=0.05, xi_kms=1.0) -> (nT, nlam) cm^2/g
  planck_nu(nu, T)
  emergent_flux(lam_nm, Teff, logg=4.44, kappa_c=0.4, X=0.7,
                names=("Halpha","Hbeta","Hgamma"), a_damp=0.05) -> (F_nu, F_nu_cont, T, rho, x)
  equivalent_width_nm(name, Teff, **kw)
```

- The first cell (from $\tau_c=0$ to the first grid point $10^{-4}$) is added as $2\pi B_0(1+\eta_0)E_2(\tau_{\nu,0})\,\tau_0$.

```python
# acceptance-test
import numpy as np
from starmc.lines import saha_x, level_fraction, atmosphere_structure, emergent_flux, equivalent_width_nm
from starmc import consts as C
assert abs(saha_x(1.232e-7, 5808.0, 0.7) / 1.807e-4 - 1) < 0.01
assert abs(saha_x(1e-8, 1e4, 0.7) - 0.2461) < 2e-3
lf = level_fraction(np.array([5772.0, 1e4]), 2)
assert abs(lf[1] / 2.8985e-5 - 1) < 0.02
T, Pg, rho, x = atmosphere_structure(5772.0, 4.44, 0.4, 0.7, np.array([0.67]))
assert abs(T[0] - 5808.3) < 1.0 and abs(Pg[0] / 4.6133e4 - 1) < 0.01 and abs(rho[0] / 1.2324e-7 - 1) < 0.01
lam = np.logspace(np.log10(50), np.log10(1e5), 4000)
Fnu, Fc, *_ = emergent_flux(lam, 5772.0, names=())
nu = C.c / (lam * 1e-7)
flux = np.trapezoid(Fc[::-1], nu[::-1])
assert abs(flux / (C.sigma * 5772.0**4) - 1) < 1e-3, flux / (C.sigma * 5772.0**4)
F, Fcc, *_ = emergent_flux(np.array([656.28]), 5772.0)
assert abs(F[0] / Fcc[0] - 0.4435) < 0.01
assert abs(equivalent_width_nm("Halpha", 5772.0) - 0.317) < 0.01
assert abs(equivalent_width_nm("Hbeta", 5772.0) - 0.1625) < 0.01
assert abs(equivalent_width_nm("Halpha", 9000.0) - 1.921) < 0.05
Ts = np.arange(7000.0, 15001.0, 1000.0)
W = [equivalent_width_nm("Halpha", t) for t in Ts]
assert 10000 <= Ts[int(np.argmax(W))] <= 12000
print("MC-21 ok")
```

---

## Checkpoints

| $T_{\rm eff}$ (K) | $W({\rm H}\alpha)$ (nm) | $W({\rm H}\beta)$ (nm) |
|---|---|---|
| 4000 | 0.017 | 0.009 |
| 5000 | 0.115 | 0.058 |
| 5772 | 0.317 | 0.162 |
| 7000 | 0.899 | 0.518 |
| 8000 | 1.473 | 0.960 |
| 9000 | 1.921 | 1.441 |
| 10000 | 2.142 | 1.835 |
| 11000 | 2.175 | 2.068 |
| 12000 | 2.115 | 2.139 |
| 14000 | 1.930 | 1.993 |
| 20000 | 1.482 | 1.314 |

| Quantity | Value |
|---|---|
| continuum flux integral over $\sigma T_{\rm eff}^4$ (Sun) | 1.0001 |
| $F/F_c$ at H$\alpha$ line centre (Sun) | 0.444 |
| $x$ at the Sun's $\tau=0.67$ | $1.8\times10^{-4}$ |
| fraction of H in $n=2$ at 10000 K | $2.9\times10^{-5}$ |

---

## Done when

- You can derive Saha for hydrogen and the occupation of $n=2$, and say why Balmer lines peak.
- You can explain why a line appears in absorption from $\tau_\nu\sim1$ and the temperature gradient.
- You can name the physical ingredients missing from this spectrum (non-LTE, Stark broadening, helium and metals, convective velocity fields).
