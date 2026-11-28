# Module MC-04: Scattering, phase functions and the albedo

[← MC-03](MC-03-emitting-packets-and-planck.md) · [README](../README.md) · [Next: MC-05 Rays through grids and shells →](MC-05-rays-grids-and-shells.md)

**Source:** Forgan, §1.2 (eqs 5–7), §5.1 (eqs 36–37), §5.2 and §5.2.1 (eqs 38–48), pp. 5, 12–14.

---

## Session A: read

- Forgan §1.2, eqs (5)–(7): the albedo and the isotropic and Rayleigh phase functions.
- Forgan §5.1, eqs (36)–(37): isotropic scattering.
- Forgan §5.2.1, eqs (44)–(48): the Henyey–Greenstein function and its inverse CDF. **Skip the Stokes vector, eqs (38)–(43) and (45)–(47)**: polarisation is not needed for a star.
- Optional: Chandrasekhar, *Radiative Transfer* (1960), Ch. I, §§15–16 (the Rayleigh phase function); Henyey & Greenstein (1941), ApJ 93, 70.

**Key ideas**

- At each interaction draw one random number against the albedo $a$: scatter if $\zeta<a$, otherwise absorb (eq 5).
- A scattering is described by a polar angle $\Theta$ from the incoming direction and an azimuth $\varphi$ about it. $\varphi$ is uniform.
- In a star the dominant scatterer is the free electron (Thomson), whose phase function is Rayleigh-like. In an optically thick interior the direction is lost after a few steps, so isotropic scattering is a good first model.

**Derivation to see once: sampling the Rayleigh angle**

- $P(\mu)=\tfrac38(1+\mu^2)$ on $[-1,1]$, with $\mu=\cos\Theta$. It is normalised: $\tfrac38(2+\tfrac23)=1$.
- CDF: $\psi(\mu)=\tfrac38(\mu+\tfrac{\mu^3}{3})+\tfrac12$.
- Set $\zeta=\psi(\mu)$. This gives $\mu^3+3\mu=2w$ with $w=4\zeta-2$.
- Cardano for $\mu^3+3\mu-2w=0$: $\mu=\sqrt[3]{w+\sqrt{w^2+1}}+\sqrt[3]{w-\sqrt{w^2+1}}$. There is a single real root because the cubic is monotonic.
- Check: $\langle\mu^2\rangle=\tfrac38\int\mu^2(1+\mu^2)d\mu=\tfrac38(\tfrac23+\tfrac25)=0.4$.

**Derivation to see once: sampling Henyey–Greenstein (eq 48)**

- Normalised density in $\mu$: $P(\mu)=\dfrac{1-g^2}{2(1+g^2-2g\mu)^{3/2}}$.
- Since $\partial_\mu(1+g^2-2g\mu)^{-1/2}=g(1+g^2-2g\mu)^{-3/2}$, the CDF is $\psi(\mu)=\dfrac{1-g^2}{2g}\Big[(1+g^2-2g\mu)^{-1/2}-\dfrac1{1+g}\Big]$.
- Set $\zeta=\psi$ and solve: $(1+g^2-2g\mu)^{-1/2}=\dfrac{1-g+2g\zeta}{1-g^2}$.
- Hence $\mu=\dfrac1{2g}\Big[1+g^2-\Big(\dfrac{1-g^2}{1-g+2g\zeta}\Big)^2\Big]$, which is Forgan's eq (48).
- The mean cosine is $\langle\mu\rangle=g$ (this is why $g$ is called the asymmetry parameter).

**Flags on the text**

- Eq (44): $M_1$ is the **unnormalised** HG function. The density used for sampling is the one above, with the factor $1/2$.
- §5.2.1 says $g$ lies between 0 and 1. In general $-1<g<1$; negative $g$ is backward scattering.
- Eq (48) is $0/0$ as $g\to0$. In code switch to $\mu=-1+2\zeta$ when $|g|<10^{-3}$.

---

## Session B: do

**Problem 1: albedo decision**

- For a medium with $n_s\sigma_s=0.3$ and $n_a\sigma_a=0.1$ (same units) compute $a$ from eq (5). Simulate $10^6$ interactions and count the scattered fraction.

**Problem 2: Rayleigh sampler**

- Implement the Cardano sampler. Show $\langle\mu\rangle=0$, $\langle\mu^2\rangle=0.4$. Plot a histogram against $\tfrac38(1+\mu^2)$.

**Problem 3: Henyey–Greenstein**

- Implement eq (48) with the small-$g$ guard. For $g=0,0.5,0.9$ check $\langle\mu\rangle=g$. For $g=0.9$ also check $\langle\mu^2\rangle=0.873$.
- Explain why $g=0.9$ needs many more scatterings to forget its direction than $g=0$.

**Problem 4: turning $(\Theta,\varphi)$ into a new direction**

- Given the old unit vector $\mathbf n$, build an orthonormal frame $(\mathbf e_1,\mathbf e_2,\mathbf n)$ and form $\mathbf n'=\cos\Theta\,\mathbf n+\sin\Theta(\cos\varphi\,\mathbf e_1+\sin\varphi\,\mathbf e_2)$.
- Check $\mathbf n'\cdot\mathbf n=\cos\Theta$ for $10^5$ random cases.
- In a spherical star you only track the radial cosine $\mu$. Show that after scattering $\mu'=\mu\cos\Theta+\sqrt{1-\mu^2}\sqrt{1-\cos^2\Theta}\cos\varphi$.

---

## Translation: text → code

| Forgan | Meaning | Code |
|---|---|---|
| eq (5) | $a=n_s\sigma_s/(n_s\sigma_s+n_a\sigma_a)$ | `scatter = rng.random(n) < albedo` |
| eqs (6), (36) | isotropic | `mu = -1 + 2*rng.random(n)` |
| eq (7) | Rayleigh | `sample_rayleigh_mu` |
| eq (48) | Henyey–Greenstein | `sample_hg_mu(rng, n, g)` |
| eqs (38)–(47) | polarisation | not used |

---

## Contract

```text
starmc/scatter.py
  sample_rayleigh_mu(rng, n) -> ndarray of cos(Theta)
  sample_hg_mu(rng, n, g) -> ndarray of cos(Theta)
  rotate_direction(n_old, cos_t, phi) -> (n, 3) new unit vectors
  scatter_mu_radial(mu, cos_t, phi) -> ndarray, new radial cosine
```

```python
# acceptance-test
import numpy as np
from starmc.scatter import sample_rayleigh_mu, sample_hg_mu, rotate_direction, scatter_mu_radial
rng = np.random.default_rng(1)
r = sample_rayleigh_mu(rng, 400_000)
assert abs(r.mean()) < 0.005 and abs((r**2).mean() - 0.4) < 0.005
assert r.min() >= -1 and r.max() <= 1
for g, m2 in [(0.0, 1 / 3), (0.5, 0.49986), (0.9, 0.87345)]:
    h = sample_hg_mu(rng, 400_000, g)
    assert abs(h.mean() - g) < 0.005, (g, h.mean())
    assert abs((h**2).mean() - m2) < 0.005, (g, (h**2).mean())
n_old = rng.normal(size=(50_000, 3))
n_old /= np.linalg.norm(n_old, axis=1, keepdims=True)
ct = -1 + 2 * rng.random(50_000)
ph = 2 * np.pi * rng.random(50_000)
n_new = rotate_direction(n_old, ct, ph)
assert np.allclose(np.linalg.norm(n_new, axis=1), 1.0)
assert np.allclose((n_new * n_old).sum(axis=1), ct, atol=1e-9)
mu = np.clip(rng.normal(size=1000), -1, 1) * 0.9
mu_new = scatter_mu_radial(mu, ct[:1000], ph[:1000])
assert np.all(np.abs(mu_new) <= 1 + 1e-12)
print("MC-04 ok")
```

---

## Checkpoints

| Quantity | Value |
|---|---|
| albedo, Problem 1 | 0.75 |
| Rayleigh $\langle\mu^2\rangle$ | 0.4 |
| HG $g=0.5$: $\langle\mu\rangle$, $\langle\mu^2\rangle$ | 0.5, 0.4999 |
| HG $g=0.9$: $\langle\mu\rangle$, $\langle\mu^2\rangle$ | 0.9, 0.8735 |

---

## Done when

- You can derive eq (48) from the HG density, and the Rayleigh cubic from its CDF.
- You can say why a guard is needed at $g\to0$ and what goes wrong without it.
- You can explain why in a star a scattering model matters less than the opacity itself (the diffusion limit forgets the phase function).
