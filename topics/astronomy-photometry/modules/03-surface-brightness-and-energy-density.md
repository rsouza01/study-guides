# Module 03: Surface brightness and energy density

[← 02 Flux density and luminosity](02-flux-density-and-luminosity.md) · [README](../README.md) · [Next: 04 Apparent magnitudes →](04-apparent-magnitudes.md)

**Source:** Karttunen, §4.1, p. 93, eqs (4.6)–(4.7), Figs 4.3–4.5; Examples 4.1 and 4.2, pp. 99–100.

---

## Session A: read

- Read the top of p. 93 (surface brightness, energy density) and then Examples 4.1 and 4.2 (pp. 99–100).
- Key ideas:
  - **Surface brightness** is flux density per unit solid angle, $B=F/\Omega$. For a resolved source it does not depend on distance: the flux falls as $1/r^2$, and so does the solid angle.
  - Intensity is constant along a ray in empty space (Example 4.1).
  - The **energy density** of radiation is $u=\tfrac1c\int I\,d\Omega$ (4.6). For isotropic radiation, $u=4\pi I/c$ (4.7).
- Derivation of (4.6):
  1. Radiation with intensity $I$ arrives from solid angle $d\Omega$, perpendicular to a surface $dA$.
  2. In time $dt$ it fills a volume $dV=c\,dt\,dA$.
  3. The energy in it is $dE=I\,dA\,d\Omega\,dt=\tfrac1c I\,d\Omega\,dV$.
  4. Dividing by $dV$ gives $du=\tfrac1c I\,d\Omega$. Integrate over directions.

---

## Session B: compute

**Problem 1: the distance independence of surface brightness**

- A uniform disc of radius $R$ with intensity $I$ is seen at distance $r$.
- Using the exact solid angle $\Omega=2\pi(1-\cos\alpha_0)$ and flux $F=\pi I\sin^2\alpha_0$ (Module 01), with $\sin\alpha_0=R/r$, compute $B/I$ for $r/R=1.5,\,3,\,10,\,100$.
- Show analytically that $B/I=(1+\cos\alpha_0)/2$.

**Problem 2: Example 4.1 as a numerical test**

- Pick two small facing patches with random orientations and separation $r$.
- The power from 1 into 2 is $I\cos\theta_1\cos\theta_2\,dA_1dA_2/r^2$.
- From the power received, reconstruct the intensity at patch 2 using its own $\cos\theta_2\,dA_2$ and the solid angle of patch 1 as seen from 2. Check that you recover $I$ for any $r$.

**Problem 3: surface brightness of the Sun (Example 4.2)**

- Use $S=1370$ W m⁻² and the Sun's angular diameter of 32′. Compute the solid angle and $B=S/\Omega$.
- Compare with $\sigma T_\odot^4/\pi$ and explain why they should agree.

**Problem 4: energy density**

- Compute the radiation energy density at Earth from sunlight as $u=S/c$.
- Compute it again with the isotropic formula $4\pi I/c$, using $I=B$ from Problem 3. The two disagree by five orders of magnitude. Explain why with the general formula (4.6).
- Compute $u$ for the cosmic microwave background at 2.725 K from $u=\frac{4\sigma}{c}T^4$, and verify that this equals $4\pi B/c$ with $B=\sigma T^4/\pi$.

---

## Checkpoints

| Quantity | Value |
|---|---|
| $B/I$ at $r/R=1.5$ | 0.87268 |
| $B/I$ at $r/R=3$ | 0.97140 |
| $B/I$ at $r/R=10$ | 0.99749 |
| $B/I$ at $r/R=100$ | 0.99997 |
| solar $\Omega$ (32′) | $6.81\times10^{-5}$ sr |
| $B=S/\Omega$ | $2.01\times10^{7}$ W m⁻² sr⁻¹ |
| $\sigma T_\odot^4/\pi$ | $2.003\times10^{7}$ W m⁻² sr⁻¹ |
| $u$ from sunlight at Earth, $S/c$ | $4.57\times10^{-6}$ J m⁻³ |
| $4\pi I/c$ with $I=B$ | 0.84 J m⁻³ (wrong at Earth) |
| CMB, 2.725 K | $4.17\times10^{-14}$ J m⁻³ |

---

## Done when

- You can explain why surface brightness is independent of distance and why a star (unresolved) does not have that property.
- You can say when $u=4\pi I/c$ applies and when it does not.
- You can say what the Sun's surface brightness equals physically (the intensity at its surface).
