# Module MC-07: Outputs, images and flux normalisation

[← MC-06](MC-06-the-packet-loop.md) · [README](../README.md) · [Next: MC-08 Errors and cost →](MC-08-errors-and-cost.md)

**Source:** Forgan, §6.1 (eqs 49–50) and §6.2 (eqs 51–52), pp. 15–16. Magnitudes as in PH-04, PH-07, PH-08.

---

## Session A: read

- Forgan §6.1: the image plane defined by the viewing angles $(\theta_v,\varphi_v)$; eqs (49)–(50).
- Forgan §6.2: flux normalisation; eqs (51)–(52).
- PH-04 (apparent magnitudes), PH-07 (bolometric magnitude) and PH-08 (distance modulus) for the conversions to magnitudes.

**Key ideas**

- A packet that escapes carries an energy $E_\gamma=L\Delta t/N_{\rm tot}$ (eq 51). You may count in "packet units" and multiply by $E_\gamma$ at the end.
- To make an image or a flux, keep **where** and **in which direction** each packet left.
- A distant observer sees only packets that leave **towards** them. For an isotropic star, the flux at distance $d$ is $L/4\pi d^2$.

**Misprint flag (eq 52).** Printed: $f=L_{\rm tot}/d^2$. This lacks the $N_{\gamma,{\rm tot}}$, the bin solid angle and a $4\pi$. The correct statement, for $n$ packets caught in a cone of solid angle $\Delta\Omega$ about the line of sight, is
$$F=\frac{L}{N_{\rm tot}}\,\frac{n}{\Delta\Omega\,d^2}.$$

**Derivation to see once: the corrected eq (52)**

- A fraction $n/N_{\rm tot}$ of the packets leave into the solid angle $\Delta\Omega$. They carry energy per time $L\,n/N_{\rm tot}$.
- So the luminosity per steradian towards the observer is $\dfrac{L\,n}{N_{\rm tot}\Delta\Omega}$.
- At distance $d$ that luminosity per steradian is spread over area $d^2$ per steradian, giving $F=\dfrac{L\,n}{N_{\rm tot}\Delta\Omega\,d^2}$.
- Check: an isotropic star has $n/N_{\rm tot}=\Delta\Omega/4\pi$, so $F=L/4\pi d^2$, as it must.

**Derivation to see once: the image-plane axes (eqs 49–50)**

- The line of sight is $\mathbf n=(\sin\theta_v\cos\varphi_v,\sin\theta_v\sin\varphi_v,\cos\theta_v)$.
- Two unit vectors orthogonal to $\mathbf n$ and to each other:
  - $\mathbf e_x=(-\cos\theta_v\cos\varphi_v,-\cos\theta_v\sin\varphi_v,\sin\theta_v)$
  - $\mathbf e_y=(-\sin\varphi_v,\cos\varphi_v,0)$
- The image coordinates are $x_{\rm image}=\mathbf r\cdot\mathbf e_x$ and $y_{\rm image}=\mathbf r\cdot\mathbf e_y$, which are exactly eqs (49)–(50). Note $\mathbf e_x\times\mathbf e_y=-\mathbf n$: the frame is left-handed as seen from the observer, which is the sky convention.

---

## Session B: do

**Problem 1: the image basis**

- Implement `image_basis(theta_v, phi_v)` returning $(\mathbf e_x,\mathbf e_y,\mathbf n)$. Verify orthonormality and that eqs (49)–(50) give the same coordinates as the dot products.

**Problem 2: flux from packets**

- Take $N=2\times10^6$ isotropic packets from a source of luminosity $L_\odot$. Count those inside a cone of half-angle $5^\circ$ about the $z$-axis and apply the corrected eq (52) at $d=10$ pc.
- Compare with $L/4\pi d^2$. What relative error do you expect from the count $n$?

**Problem 3: from flux to magnitude**

- Use $F_{m_{\rm bol}=0}=2.518\times10^{-8}\ {\rm W\,m^{-2}}$ (IAU 2015 B2) to convert. The Sun at 1 AU: $m_{\rm bol}=-26.83$. At 10 pc: $M_{\rm bol}=4.74$.
- Check against PH-07.

**Problem 4: counting photons, not energy**

- A detector with effective area $A$ and exposure $t$ collects $N_{\rm ph}=\int F_\lambda S(\lambda)\,\dfrac{\lambda}{hc}A\,t\,d\lambda$. Write `photon_counts`.
- Explain why $E_\gamma$ (energy per packet) and the real photon energy $hc/\lambda$ are different things.

---

## Translation: text → code

| Forgan | Meaning | Code |
|---|---|---|
| eqs (49)–(50) | image coordinates | `image_basis`, `image_coords` |
| eq (51) | $E_\gamma=L\Delta t/N_{\rm tot}$ | `E_gamma = L / N_tot` |
| eq (52) | **misprint** | `flux_from_packets(L, N_tot, n_bin, d_omega, d)` |
| eq (53) | Poisson error | MC-08 |

---

## Contract

```text
starmc/detector.py
  image_basis(theta_v, phi_v) -> (ex, ey, n)   three unit 3-vectors
  image_coords(pos, theta_v, phi_v) -> (x_img, y_img)
  flux_from_packets(L, N_tot, n_bin, d_omega, d) -> flux  (L/N)*n/(d_omega d^2)
  m_bol_from_flux(F_Wm2) -> m_bol
  photon_counts(F_lam, lam, S, area, t) -> expected photons
```

- Flux and luminosity in `flux_from_packets` use the same unit system you give them (cgs in this package). `m_bol_from_flux` takes **W m⁻²**.

```python
# acceptance-test
import numpy as np
from starmc.detector import image_basis, image_coords, flux_from_packets, m_bol_from_flux
from starmc.emission import isotropic_directions
rng = np.random.default_rng(21)
ex, ey, n = image_basis(0.7, 1.9)
assert np.isclose(ex @ ex, 1) and np.isclose(ey @ ey, 1) and abs(ex @ ey) < 1e-12
assert abs(ex @ n) < 1e-12 and abs(ey @ n) < 1e-12
p = rng.normal(size=(5, 3))
xi, yi = image_coords(p, 0.7, 1.9)
th, ph = 0.7, 1.9
x_ref = p[:, 2] * np.sin(th) - p[:, 1] * np.cos(th) * np.sin(ph) - p[:, 0] * np.cos(th) * np.cos(ph)
y_ref = p[:, 1] * np.cos(ph) - p[:, 0] * np.sin(ph)
assert np.allclose(xi, x_ref) and np.allclose(yi, y_ref)
L, pc_m = 3.828e26, 3.0856775814913673e16
d = 10 * pc_m
N = 2_000_000
dirs = isotropic_directions(rng, N)
ch = np.cos(np.radians(5.0))
nb = int((dirs[:, 2] > ch).sum())
dom = 2 * np.pi * (1 - ch)
F = flux_from_packets(L, N, nb, dom, d)
F0 = L / (4 * np.pi * d**2)
assert abs(F / F0 - 1) < 4 / np.sqrt(nb), (F / F0, nb)
assert abs(m_bol_from_flux(F0) - 4.74) < 0.01
au = 1.495978707e11
assert abs(m_bol_from_flux(L / (4 * np.pi * au**2)) + 26.83) < 0.01
print("MC-07 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| $L_\odot/4\pi(10\,{\rm pc})^2$ | $3.199\times10^{-10}$ W m⁻² |
| $M_{\rm bol,\odot}$ | 4.74 |
| $m_{\rm bol,\odot}$ at 1 AU | −26.83 |
| packets in a $5^\circ$ cone out of $2\times10^6$ | about 3800 (so about 1.6 % noise) |
| solar angular diameter at 1 AU (MC-23) | 1918″ |

---

## Done when

- You can derive the corrected eq (52) and show it reduces to $L/4\pi d^2$.
- You can explain why the observer sees only packets inside a small cone and what that costs in statistics.
- You can say how the image-plane axes follow from the line of sight.
