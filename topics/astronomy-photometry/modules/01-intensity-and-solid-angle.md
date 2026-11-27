# Module 01: Intensity and solid angle

[← README](../README.md) · [Next: 02 Flux density and luminosity →](02-flux-density-and-luminosity.md)

**Source:** Karttunen, *Fundamental Astronomy*, §4.1, pp. 91–92, eqs (4.1)–(4.4), Figs 4.1–4.2.

---

## Session A: read

- Read §4.1 from the start of the chapter up to eq (4.4) (pp. 91–92).
- Key ideas:
  - The **specific intensity** $I_\nu$ is the energy per unit projected area, per unit time, per unit frequency, per unit solid angle. Units: W m⁻² Hz⁻¹ sr⁻¹.
  - Eq (4.1) has a factor $\cos\theta$ because a surface tilted by $\theta$ presents only $dA\cos\theta$ to the radiation.
  - The **flux density** is the intensity summed over directions, weighted by $\cos\theta$:
    $$F_\nu=\int I_\nu\cos\theta\,d\Omega .$$
  - A solid-angle element is $d\Omega=\sin\theta\,d\theta\,d\phi$.
  - For isotropic radiation the net flux through a surface is zero (as much goes in as comes out). The flux leaving one side is $\pi I$.
  - 1 Jansky = $10^{-26}$ W m⁻² Hz⁻¹.
- Derivation worth doing once on paper (eq 4.4):
  1. Isotropic $I$, outward hemisphere $0\le\theta\le\pi/2$.
  2. $F=I\int_0^{2\pi}d\phi\int_0^{\pi/2}\cos\theta\sin\theta\,d\theta$.
  3. Substitute $u=\sin\theta$: the $\theta$ integral is $1/2$.
  4. So $F=2\pi\cdot I\cdot\tfrac12=\pi I$.

---

## Session B: compute

**Problem 1: the hemisphere integral by brute force**

- Compute $\int_{\rm hemisphere}\cos\theta\,d\Omega$ with a midpoint rule on an $N\times N$ grid in $(\theta,\phi)$.
- Plot the error against $N$ on log–log axes and read off the convergence order.
- Then integrate over the **full sphere**. What do you get, and why?

**Problem 2: Monte Carlo directions**

- Draw $10^6$ random directions uniformly distributed on the sphere.
- Estimate $\int_{\rm hemisphere}\cos\theta\,d\Omega$ as $4\pi\times\langle\max(\cos\theta,0)\rangle$.
- Repeat with $\theta$ drawn uniformly in $[0,\pi]$ instead. What goes wrong?

<details>
<summary>Hint</summary>

A direction is uniform on the sphere when $\cos\theta$ is uniform on $[-1,1]$ and $\phi$ is uniform on $[0,2\pi)$. Uniform $\theta$ crowds directions near the poles.

</details>

**Problem 3: an anisotropic intensity**

- Take $I(\theta)=I_0\,(1-u+u\cos\theta)$ on the outward hemisphere, with $u=0.6$.
- Compute $F/I_0$ numerically and compare with the closed form $\pi(1-u/3)$.
- This is a simple "limb-darkening law". It returns in Module 27.

**Problem 4: a uniform disc**

- A source subtends a disc of angular radius $\alpha_0$ and has constant intensity $I$.
- Show analytically that $F=\pi I\sin^2\alpha_0$, then confirm numerically for $\alpha_0=10^\circ$ and $60^\circ$.

**Problem 5: units**

- Write `jy_to_si(F_jy)`.
- Convert 1 Jy and 3631 Jy to W m⁻² Hz⁻¹.

---

## Checkpoints

| Quantity | Value |
|---|---|
| $F/I$, outward hemisphere | 3.14159265 |
| $F/I$, full sphere | $\lvert\cdot\rvert<10^{-12}$ |
| $F/I_0$ for $u=0.6$ | 2.51327 ($=0.8\pi$) |
| Monte Carlo, $N=10^6$ | within about 0.01 of $\pi$ |
| 3631 Jy | $3.631\times10^{-23}$ W m⁻² Hz⁻¹ |

---

## Done when

- You can explain in your own words why $\cos\theta$ appears in eq (4.1).
- You can explain why the full-sphere net flux of an isotropic field is zero while the one-sided flux is $\pi I$.
- You have seen that uniform in $\cos\theta$, not in $\theta$, is what "uniform on the sphere" means.
