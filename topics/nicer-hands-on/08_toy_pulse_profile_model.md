# Module 08 (Level 4): a toy pulse-profile model: why compactness is measurable, and fragile

**Resources:** `nicerkit/ppm.py`; `examples/ex08_toy_ppm.py`; Beloborodov (2002) for the light-bending approximation; Poutanen & Beloborodov (2006); Bogdanov et al. 2019 (ApJL 887, L26) for the full PPM framework; Riley et al. 2023 (JOSS 8, 4977) for X-PSI.
**Time:** 2 sessions. **Fully offline.**

## Why this matters

NICER does not "see" a radius. It sees how a hot spot's light curve is warped by gravity: strong light bending lets you see more than half the star and **washes out** the pulse, so the pulsed amplitude and shape carry the compactness $u=2GM/Rc^2$. Building the simplest version yourself shows (i) the physics that makes a radius measurable, (ii) why it is degenerate with geometry, and (iii) why a wrong hot-spot model biases the answer, which is the central systematic of real analyses (J0030's two hot-spot models gave 11.7 and 14.4 km in 2024).

## Diagnostic (15 minutes)

1. Why does stronger gravity reduce the pulsed fraction?
2. What does Beloborodov's relation $1-\cos\alpha=(1-u)(1-\cos\psi)$ say, and when is a spot visible?
3. Name three things a real model has that this toy lacks.

## Detailed topics (checklist)

- **Light bending (Schwarzschild, Beloborodov 2002):** a photon that reaches the observer from a surface point at angle $\psi$ from the line of sight left the surface at angle $\alpha$ from the normal with $\cos\alpha=u+(1-u)\cos\psi$. The spot is visible while $\cos\alpha>0$, i.e. for $\cos\psi>-u/(1-u)$; for $u=0.35$ a spot is visible even when it is slightly "behind" the limb, and for $u>2/3$ the entire surface is visible.
- **Flux from a point spot:** isotropic emission gives flux $\propto\cos\alpha$ (the lensing factor $d\cos\alpha/d\cos\psi=1-u$ is constant); optional beaming; rotation adds Doppler boosting (here a first-order $\delta^4$ with $\beta=2\pi\nu R\sin\theta/(c\sqrt{1-u})$, ignoring time delays and oblateness).
- **Two antipodal spots** (`two_spot_profile`) are a centred-dipole caricature; real NICER analyses allow arbitrary, non-antipodal, extended, multi-temperature spots (hot-spot models ST, PST, ST+PDT, PDT-U).
- **Inference toy:** `fit_profile` maximises the Poisson likelihood over $(u,\cos i,\theta,{\rm amplitude},{\rm background})$; `profile_likelihood_u` fixes $u$ on a grid to show what the profile alone says about compactness.
- **What real analyses add:** oblate shape (spin 205 Hz, 4.87 ms), finite spot shape/size and temperature structure, atmosphere models (energy- and angle-dependent emission), interstellar absorption, instrument response and background, **energy** resolution (PI channels), and **joint** XMM-Newton spectra and radio-timing priors on mass and inclination.

## Tasks

1. `python ex08_toy_ppm.py`: three panels (profiles vs $u$; profile likelihood vs $u$; bias vs spot size).
2. Fix $i=\theta=55^\circ$, $\nu=205$ Hz. Print the amplitude pulsed fraction for $u=0.05\ldots0.6$.
3. Simulate Poisson data at $10^5,10^6,10^7$ counts from a known $(u,i,\theta)$ and fit.

## Exercises (with expected results)

1. **Pulsed fraction vs compactness:** with $i=\theta=55^\circ$ and Doppler boosting on: $u=0.1,0.25,0.35,0.5\to$ amplitude PF $=0.70,0.40,0.25,0.07$ (without Doppler: $0.67,0.33,0.18,0.00$). Stronger bending fills in the minima. A more compact star is *harder* to see pulsing, which is why NICER's best targets are those with sufficient counts and geometry.
2. **Visibility:** the fraction of the rotation during which one spot is visible: $0.73$ ($u=0.1$), $0.95$ ($u=0.25$), $1.00$ ($u\geq0.35$) for this geometry.
3. **Newtonian limit test:** $u\to0$, equatorial spot, edge-on, no Doppler: visible exactly half the time (unit test `test_newtonian_limit_visible_half_only`).
4. **Profile likelihood:** with about $3.6\times10^5$ counts the toy gives $\Delta\chi^2=0$ at the true $u=0.35$ and $\approx12.8$ at $u=0.30$, $\approx62$ at $u=0.40$ (the toy model is *correctly specified*, so no degeneracy shows: this is the optimistic case). With $10\times$ more counts the curve is $\sim10\times$ steeper.
5. **Misspecification bias (the real lesson):** generate data from finite caps of angular radius $\zeta=0.05,0.3,0.6,0.9$ rad at $u=0.35$ and fit the *point-spot* model: best-fit $u=0.355,0.341,0.335,0.329$. At fixed mass $1.4\,M_\odot$ ($r_s=4.135$ km), $u=0.329$ means $R=r_s/u=12.57$ km versus the true $11.81$ km: **a model error of 6% in $u$ becomes $+0.76$ km in radius**, comparable to the statistical error of NICER measurements.
6. **Degeneracy exploration:** at low counts, scan $(u,i)$ on a grid with the other parameters re-optimised; plot the $\Delta\chi^2$ valley. Does the valley run along constant $\cos i\cdot\sin\theta$ type combinations? Why is a radio-timing prior on inclination valuable (J0740, J0437, J0614)?
7. **Add one real ingredient:** implement either (a) a second hot spot with free colatitude, or (b) beaming $I\propto1+b\cos\alpha$ and show how $b$ trades off with $u$.
8. **Time delays:** estimate the light-travel-time difference across the star ($\sim2R/c\approx80\,\mu$s) versus the rotation period 4.87 ms: why does ignoring it matter at the percent level for the profile shape at 205 Hz?

## Pitfalls

- Reading the toy's tight $u$ constraint as a prediction for NICER (real data have extended spots, background, calibration and model uncertainty).
- Forgetting that radius follows from $u$ only if mass is known (radio-timing priors) or from the joint $M$-$R$ posterior.
- Sign errors in Doppler direction (check with the unit tests and a $\nu\to0$ comparison).

## Gate questions

1. Why is NICER's radius constraint dominated by modeling systematics rather than photon counts for the brightest targets?
2. How does a prior on mass or inclination reduce the degeneracy?
3. Why does extending the hot-spot model (ST+PDT to PDT-U) change the posterior?

## One-page cheat sheet contents

Light-bending relation and visibility condition; pulsed fraction vs $u$ table; the misspecification-bias numbers; list of ingredients real models add.
