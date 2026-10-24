# CA09: Capstone, the three Green functions, Wick rotation and the gate

**Books:** none new. This module uses your CA07 and CA08 results. Read afterwards: Jackson 6.4 (EM Module 11) and, for the Fourier side, Figueiredo Chapter 6 (linear algebra and Fourier path). **Time:** 2 sessions (Must: 2). **Tier note:** this is the deliverable of the guide. Do not skip it, and do not start it before the CA08 exercises 1 to 5 are clean.

## Why this matters

This is EM Module 11 in miniature. Jackson Fourier-transforms the wave equation and gets $\tilde G\propto1/k^2$ with poles on the real axis. The integral is undefined until you choose a contour, and the three choices give $G_{\rm ret}$, $G_{\rm adv}$ and the Feynman propagator. If you can do the one-oscillator version here cold, the field version is a change of notation, and the Klein–Gordon propagator in QFT is the same calculation with $\omega_0^2\to k^2+m^2$. The choice of contour is a choice of boundary condition in time: retarded means no response before the source acts; Feynman means positive frequencies propagate forward and negative frequencies backward, which is the origin of antiparticles in the field picture. This module also gives the justification of Wick rotation and the causality-to-analyticity chain behind Kramers–Kronig.

## Skip-test (40 minutes, no notes)

1. Write the equation for the Green function of $\ddot q+\omega_0^2q=\delta(t)$, Fourier transform it, and say why the result is undefined on the real axis.
2. List the three prescriptions, where the poles sit, and the half-plane you close in for each sign of $t$.
3. State which prescription allows Wick rotation, and why.
4. State the Sokhotski formula.
5. Explain why a causal response function is analytic in the upper half-plane.

## Prerequisites

CA07, CA08. Conventions: appendix, section 4 (time dependence $e^{-i\omega t}$, which is the physics convention and the one EM Module 02 uses).

## Detailed topics (checklist)

**[Must]** The oscillator Green function $\ddot q+\omega_0^2q=\delta(t)$. With $q(t)=\int\frac{d\omega}{2\pi}e^{-i\omega t}\tilde q(\omega)$, $\tilde q=\frac1{\omega_0^2-\omega^2}$, with poles at $\pm\omega_0$ on the real axis.

**[Must]** The three prescriptions:

| Name | Prescription | Poles | Result |
|---|---|---|---|
| Retarded | $\omega\to\omega+i\epsilon$ | both at $\pm\omega_0-i\epsilon$ (below the axis) | $\theta(t)\,\dfrac{\sin\omega_0t}{\omega_0}$ |
| Advanced | $\omega\to\omega-i\epsilon$ | both at $\pm\omega_0+i\epsilon$ (above the axis) | $-\theta(-t)\,\dfrac{\sin\omega_0t}{\omega_0}$ |
| Feynman | $\omega_0^2\to\omega_0^2-i\epsilon$ | $+\omega_0-i\epsilon'$ below, $-\omega_0+i\epsilon'$ above | $\dfrac{i}{2\omega_0}e^{-i\omega_0\lvert t\rvert}$ |

**[Must]** Wick rotation: rotating the contour $\omega\to i\omega_E$ sweeps the first and third quadrants. It is legal only if no pole lies there. The Feynman poles sit in the second and fourth quadrants, so the rotation is allowed; the retarded poles at $\pm\omega_0-i\epsilon$ include one in the third quadrant, so it is blocked.

**[Should]** The field version: spatial Fourier transform reduces $\Box G=-4\pi\delta^3(\mathbf x)\delta(t)$ to the oscillator with $\omega_0=ck$.

**[Should]** Causality and Kramers–Kronig: $\chi(t)=0$ for $t<0$ implies $\chi(\omega)=\int_0^\infty\chi(t)e^{i\omega t}\,dt$ is analytic in the upper half-plane, and Cauchy's formula with an indentation gives $\mathrm{Re}\,\chi=\frac1\pi\mathrm{PV}\!\int\frac{\mathrm{Im}\,\chi(\omega')}{\omega'-\omega}\,d\omega'$ and $\mathrm{Im}\,\chi=-\frac1\pi\mathrm{PV}\!\int\frac{\mathrm{Re}\,\chi(\omega')}{\omega'-\omega}\,d\omega'$.

**[Could]** The Yukawa potential as a static limit with $\omega_0^2\to k^2+\mu^2$.

## Method cards

**The three prescriptions.** (1) Write the denominator with the $\pm i\epsilon$ placed as required. (2) Find the poles and mark which side of the real axis each lies on. (3) For $t>0$ close below (since $e^{-i\omega t}$ decays for $\mathrm{Im}\,\omega<0$), clockwise, so $-2\pi i\sum\mathrm{Res}$; for $t<0$ close above, counterclockwise, $+2\pi i\sum\mathrm{Res}$. (4) If no pole is enclosed the result is $0$. (5) Check with the differential equation: the result must solve it away from $t=0$ and have the right jump at $t=0$.

**Residues for this integrand.** Near $\omega=\omega_0$ the denominator behaves like $-2\omega_0(\omega-\omega_0)$, so the residue of $e^{-i\omega t}/(\omega_0^2-\omega^2)$ is $-\frac{e^{-i\omega_0t}}{2\omega_0}$. Near $\omega=-\omega_0$ it is $+\frac{e^{i\omega_0t}}{2\omega_0}$.

**Wick rotation.** (1) Locate the poles. (2) Check the first and third quadrants are free of poles. (3) Rotate; the arcs vanish by Jordan's lemma. (4) Continue $t\to-i\tau$ to get the Euclidean propagator.

## Reading plan

| Session | Task |
|---|---|
| A1 | Derive items 1 and 2 below. Exercises 1 to 5 |
| B1 | Exercises 6 to 8, the written page (exercise 10), the gate, the cheat sheet |

## Derive from scratch

1. The retarded, advanced and Feynman functions of the oscillator, with each pole and each half-plane.
2. $G_{\rm ret}-G_{\rm adv}=\sin(\omega_0t)/\omega_0$, and $G_F=\tfrac12(G_{\rm ret}+G_{\rm adv})+\frac{i\cos\omega_0t}{2\omega_0}$.
3. The reason Wick rotation works for $G_F$ and not for $G_{\rm ret}$.
4. The field version: from $\tilde G(k,t)$ to $\delta(t-R/c)/R$ (exercise 8).

## Exercises (with expected results)

1. **(Must)** The three prescriptions for $\int\frac{d\omega}{2\pi}\frac{e^{-i\omega t}}{\omega_0^2-\omega^2}$. *Expected:* retarded $\theta(t)\frac{\sin\omega_0t}{\omega_0}$; advanced $-\theta(-t)\frac{\sin\omega_0t}{\omega_0}$; Feynman $\frac{i}{2\omega_0}e^{-i\omega_0\lvert t\rvert}$. (With a finite $\epsilon$ the retarded result carries a factor $e^{-\epsilon t}$.)
2. **(Must)** Show $G_{\rm ret}-G_{\rm adv}=\frac{\sin\omega_0t}{\omega_0}$ for all $t$. *Expected:* the two step functions add to $1$.
3. **(Must)** Show $G_F=\frac12(G_{\rm ret}+G_{\rm adv})+\frac{i}{2\omega_0}\cos\omega_0t$. *Expected:* $\frac12(G_{\rm ret}+G_{\rm adv})=\frac{\sin\omega_0\lvert t\rvert}{2\omega_0}$, and $e^{-i\omega_0\lvert t\rvert}=\cos\omega_0t-i\sin\omega_0\lvert t\rvert$. So the Feynman function is the symmetric part plus a homogeneous solution.
4. **(Must)** Which prescription permits the rotation $\omega=i\omega_E$ without crossing a pole? *Expected:* Feynman (poles in quadrants 2 and 4). The retarded poles include one at $-\omega_0-i\epsilon$ in the third quadrant, so the rotation crosses it.
5. **(Must)** Compute the Euclidean function $\int\frac{d\omega_E}{2\pi}\frac{e^{i\omega_E\tau}}{\omega_0^2+\omega_E^2}$ and relate it to $G_F$. *Expected:* $\frac{e^{-\omega_0\lvert\tau\rvert}}{2\omega_0}$, and $G_F(t\to-i\tau)=i\,G_E(\tau)$.
6. **(Should)** Verify the Sokhotski formula for $f=e^{-x^2}$. *Expected:* $\int\frac{e^{-x^2}}{x-i\epsilon}\,dx\to\mathrm{PV}\!\int\frac{e^{-x^2}}x\,dx+i\pi f(0)=i\pi$ (the principal value vanishes by oddness). At finite $\epsilon$ the value is $i\pi e^{\epsilon^2}\mathrm{erfc}(\epsilon)$.
7. **(Should)** The Yukawa potential: $\int\frac{d^3k}{(2\pi)^3}\frac{4\pi e^{i\mathbf k\cdot\mathbf x}}{k^2+\mu^2}$. *Expected:* $\frac{e^{-\mu r}}{r}$. After the angular integral you need $\int_0^\infty\frac{k\sin kr}{k^2+\mu^2}\,dk=\frac\pi2e^{-\mu r}$ (half of CA08 exercise 7). Connect it to Jackson's screened-potential problem in EM Module 03 and to Proca.
8. **(Should)** The field version. Spatially Fourier transform $\Box G=\big(\nabla^2-\tfrac1{c^2}\partial_t^2\big)G=-4\pi\delta^3(\mathbf x)\delta(t)$. *Expected:* $\ddot{\tilde G}+c^2k^2\tilde G=4\pi c^2\delta(t)$, so $\tilde G_{\rm ret}(k,t)=4\pi c\,\theta(t)\frac{\sin ckt}{k}$. The angular integral gives $4\pi\frac{\sin kR}{kR}$, so $G=\frac{2c}{\pi R}\theta(t)\int_0^\infty\sin kR\sin ckt\,dk=\frac{c}{R}\delta(R-ct)=\frac{\delta(t-R/c)}{R}$, using $\int_0^\infty\cos(ka)\,dk=\pi\delta(a)$. This is Jackson's retarded Green function.
9. **(Could)** Derive the Kramers–Kronig relations from causality: analyticity in the upper half-plane, Cauchy's formula on a large semicircle with an indentation at $\omega$, and the principal value. *Expected:* $\chi(\omega)=\frac1{i\pi}\mathrm{PV}\!\int\frac{\chi(\omega')}{\omega'-\omega}\,d\omega'$, whose real and imaginary parts are the two relations above.
10. **(Could)** Write one page, in your own words, called "Where the three prescriptions went": the three contours, the three boundary conditions in time, which one allows Wick rotation, and what $G_F$ says about positive and negative frequencies. This is the artifact of the guide.

## Optional extension

Replace $\omega_0$ by $\sqrt{c^2k^2+m^2c^4/\hbar^2}$ and read off the Klein–Gordon propagator in the time-momentum representation. This is the first line of the Klein–Gordon chapter in a QFT text, and you will have derived it before opening one.

## Pitfalls

* Placing $i\epsilon$ in the wrong place (on $\omega$ versus on $\omega_0^2$ changes the prescription).
* Closing in the wrong half-plane for the sign of $t$.
* Treating Feynman as retarded plus advanced; it is the symmetric part plus a homogeneous solution.
* Forgetting that Wick rotation needs the pole-free quadrants and Jordan's lemma on the arcs.

## Gate questions

1. Why is the integral $\int\frac{e^{-i\omega t}}{\omega_0^2-\omega^2}\,d\omega$ undefined until a prescription is chosen?
2. State the three prescriptions, the pole positions, the half-plane for each sign of $t$, and the boundary condition each encodes.
3. Why is $G_F=\tfrac12(G_{\rm ret}+G_{\rm adv})+$ a homogeneous solution?
4. Why does Wick rotation work for the Feynman prescription and fail for the retarded one?
5. Derive $\delta(t-R/c)/R$ from $\tilde G(k,t)$.
6. State the chain causality to analyticity to dispersion relation.
7. Where does the principal value come from, and what does the Sokhotski formula add?
8. What changes in the three results when $\omega_0^2\to c^2k^2+m^2c^4/\hbar^2$?

Items 1, 2, 4 and 5 are the gate for EM Module 11.

## One-page cheat sheet contents

The table of three prescriptions; the residue values; the half-plane rule; the Wick-rotation criterion; Sokhotski; the Kramers–Kronig pair.

## Where this is used

EM Module 11 (the gate), EM Module 19, EM Module 18 (covariant Green functions), the Zettili scattering and propagator material, and the whole QFT track.
