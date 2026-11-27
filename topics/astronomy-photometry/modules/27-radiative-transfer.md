# Module 27: Radiative transfer

[← 26 Masers and population inversion](26-masers-and-population-inversion.md) · [README](../README.md)

**Source:** Karttunen, §5.9, pp. 116–117, eqs (5.35)–(5.43), Figs 5.11–5.12.

---

## Session A: read

- Read §5.9 (pp. 116–117).
- Key ideas:
  - Along a ray, intensity changes by absorption ($-\kappa\rho I$) and emission ($+j$). With optical depth $d\tau=\kappa\rho\,ds$ and **source function** $S=j/\kappa\rho$, the transfer equation is
    $$\frac{dI}{d\tau}=-I+S .$$
  - Formal solution: $I(\tau)=I_0e^{-\tau}+\displaystyle\int_0^\tau S(t)\,e^{-(\tau-t)}\,dt$.
  - In LTE, $S=B_\nu(T)$ (Kirchhoff).
  - **Plane-parallel atmosphere**: depth $\tau$ measured vertically, ray at angle $\theta$ with $\mu=\cos\theta$, so the path in optical depth is $\tau/\mu$.
  - **Eddington–Barbier relation**: the emergent intensity at $\mu$ comes from where the slant optical depth is about 1, so $I(0,\mu)\approx S(\tau=\mu)$. This explains limb darkening.
- Derive on paper: multiply $dI/d\tau=-I+S$ by $e^{\tau}$ to get $d(Ie^{\tau})/d\tau=Se^{\tau}$, then integrate.

---

## Session B: compute

**Problem 1: constant source function**

- For constant $S$, the solution is $I(\tau)=I_0e^{-\tau}+S(1-e^{-\tau})$. Evaluate for $S=2$, $I_0=5$ at $\tau=0.1,1,3,10$.

**Problem 2: numerical integration**

- Write a RK4 integrator for $dI/d\tau=-I+S(\tau)$. Test against Problem 1 with $n=4,16,64$ steps at $\tau=1$ and check the error scales as $h^4$.

**Problem 3: a radio cloud**

- In the Rayleigh–Jeans regime the brightness temperature of a cloud with excitation temperature $T_{\rm ex}$ in front of a background $T_{bg}$ is $T_b=T_{\rm ex}(1-e^{-\tau})+T_{bg}e^{-\tau}$.
- For $T_{\rm ex}=100$ K and $T_{bg}=2.725$ K compute $T_b$ for $\tau=0.1,1,5$. Describe the optically thin and thick limits.

**Problem 4: Eddington–Barbier and limb darkening**

- Take $S(\tau)=a+b\tau$ with $a=1$, $b=0.6$. The exact emergent intensity is $I(0,\mu)=a+b\mu$. Compute it for $\mu=1,0.5,0.1$ and the ratios to the disc centre.
- Then compute the disc-integrated flux $F=2\pi\int_0^1I(0,\mu)\mu\,d\mu$ relative to $\pi I(0,1)$. With $u=b/(a+b)$ the ratio is $1-u/3$. (Compare with Module 01.)

---

## Checkpoints

| $\tau$ | $I(\tau)$ for $S=2$, $I_0=5$ |
|---|---|
| 0.1 | 4.7145 |
| 1 | 3.1036 |
| 3 | 2.1494 |
| 10 | 2.00014 |

| RK4 steps | error at $\tau=1$ |
|---|---|
| 4 | $4.4\times10^{-5}$ |
| 16 | $1.5\times10^{-7}$ |
| 64 | $5.6\times10^{-10}$ |

| $\tau$ | $T_b$ |
|---|---|
| 0.1 | 11.98 K |
| 1 | 64.21 K |
| 5 | 99.34 K |

| $\mu$ | $I(0,\mu)$ | ratio to centre |
|---|---|---|
| 1 | 1.6 | 1 |
| 0.5 | 1.3 | 0.8125 |
| 0.1 | 1.06 | 0.6625 |

- Disc-integrated ratio: $u=0.375$, $F/\pi I(0,1)=0.875$.

---

## Done when

- You can derive the formal solution and say what each term means.
- You can explain why the Sun looks darker at the limb, using Eddington–Barbier and a source function that rises with depth.
- You can give the optically thin and thick limits of the radio-cloud formula and say what each tells you about the cloud.
