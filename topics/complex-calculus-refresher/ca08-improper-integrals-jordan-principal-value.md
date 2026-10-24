# CA08: Improper integrals, Jordan's lemma and principal values

**Books:** Ávila Chapter 5, pp. 161 to 169 (rational integrands, Jordan's lemma) and pp. 173 to 174 (trigonometric integrals). Exercise sets on pp. 163, 168 and 174; answers on pp. 164 and 169. **Churchill Chapter 7** for indented contours and the Cauchy principal value: **Ávila's table of contents has no section on them, so Churchill (or Boas) carries that part.** **Time:** 4 sessions (Must: 4). **Tier note:** the three-star module. Do all of exercises 1 to 5, and do not leave it before exercise 6 is clear.

## Why this matters

Jackson's Green function for the wave equation is a Fourier integral whose denominator vanishes on the real axis. It is undefined until you choose how to go around the poles. The calculation is exactly this module: close the real line with a large semicircle, justify the closure with Jordan's lemma, and collect residues. Indenting the contour around a pole on the real axis, and the principal value that results, is what makes retarded, advanced and Feynman different, and it is the tool behind the Kramers–Kronig relations in EM Module 19. In your own words: the indentation direction is the physical boundary condition.

## Skip-test (40 minutes, no notes)

1. Evaluate $\int_{-\infty}^\infty\frac{dx}{x^2+1}$ by closing the contour, and justify discarding the arc.
2. State Jordan's lemma.
3. Evaluate $\int_{-\infty}^\infty\frac{\cos kx}{x^2+a^2}\,dx$ for $k,a>0$.
4. Explain which half-plane to close in for $e^{iax}$ with $a>0$ and with $a<0$.
5. Evaluate $\int_{-\infty}^\infty\frac{\sin x}{x}\,dx$ with an indented contour.
6. Write $\frac1{x\pm i\epsilon}$ in terms of the principal value and a delta function.

## Prerequisites

CA04 (the ML-estimate), CA07 (residues). Stewart 7.8 (improper integrals, convergence at both ends).

## Detailed topics (checklist)

**[Must]** Rational integrands on the real line: close with a large semicircle $C_R$; show $\int_{C_R}\to0$ by the ML-estimate when the degree of the denominator exceeds that of the numerator by at least 2.

**[Must]** Jordan's lemma: if $g$ is continuous in the upper half-plane for $\lvert z\rvert\ge R_0$ and $\max_{C_R}\lvert g\rvert\to0$, then for $a>0$, $\int_{C_R}g(z)e^{iaz}\,dz\to0$. For $a<0$ close in the lower half-plane. The proof uses $\sin\theta\ge2\theta/\pi$ on $[0,\pi/2]$ to get $\int_0^\pi e^{-aR\sin\theta}\,d\theta<\pi/(aR)$.

**[Must]** Trigonometric integrals $\int_0^{2\pi}R(\cos\theta,\sin\theta)\,d\theta$: put $z=e^{i\theta}$, $\cos\theta=\frac12(z+z^{-1})$, $\sin\theta=\frac1{2i}(z-z^{-1})$, $d\theta=dz/(iz)$, and integrate over the unit circle (Ávila pp. 173 to 174).

**[Must]** Poles on the real axis: indent the contour with a small semicircle. A small semicircle of radius $\rho$ around a simple pole, traversed clockwise (passing above it), contributes $-i\pi\,\mathrm{Res}$ as $\rho\to0$. The result is the Cauchy principal value (Churchill Chapter 7).

**[Should]** The Sokhotski formula $\frac1{x\pm i\epsilon}=\mathrm{PV}\frac1x\mp i\pi\delta(x)$ and its use with the $\pm i\epsilon$ prescription.

**[Could]** The multivalued integrands of Ávila pp. 169 to 173 (keyhole contours) are deferred to Part 2 (appendix).

## Method cards

**Closing a contour.** (1) Write the integrand, often $e^{iax}g(x)$. (2) Decide the half-plane: $a>0$ upward, $a<0$ downward. For a rational integrand with no exponential, either, by the ML-estimate. (3) Find the poles in that half-plane; $\pm i\epsilon$ tells you which side of the real axis each real pole moves to. (4) Sum $2\pi i\times$ residues (counterclockwise, upward) or $-2\pi i\times$ residues (clockwise, downward). (5) Check the limit $x\to0$ and any symmetry.

**Indenting.** (1) Take the principal value outside small neighbourhoods of the real poles. (2) Close with the big semicircle. (3) Add a small semicircle above each real pole (pole outside the contour). (4) Then $\mathrm{PV}\!\int=2\pi i\sum_{\rm inside}\mathrm{Res}+i\pi\sum_{\rm on\ axis}\mathrm{Res}$ when closing upward.

**Trigonometric integral.** (1) Substitute $z=e^{i\theta}$. (2) Find the poles inside the unit circle. (3) Residues, times $2\pi i$.

## Reading plan

| Session | Task |
|---|---|
| A1 | Ávila pp. 161 to 168 (rational integrands, Jordan's lemma). Derive items 1 and 2 |
| B1 | Exercises 1 to 3 and the Ávila sets on pp. 163 and 168 |
| A2 | Ávila pp. 173 to 174 (trigonometric integrals), then Churchill Chapter 7 (indented paths, principal value). Derive items 3 and 4 |
| B2 | Exercises 4 to 10 and the Ávila set on p. 174. Cheat sheet |

## Derive from scratch

1. $\int_{-\infty}^\infty\frac{dx}{x^2+1}=\pi$, including the arc estimate.
2. Jordan's lemma, from $\sin\theta\ge2\theta/\pi$.
3. The indentation lemma: a small clockwise semicircle around a simple pole gives $-i\pi\,\mathrm{Res}$.
4. $\int_{-\infty}^\infty\frac{\sin x}{x}\,dx=\pi$ from $\mathrm{PV}\!\int\frac{e^{ix}}{x}\,dx=i\pi$.

## Exercises (with expected results)

1. **(Must)** $\int_{-\infty}^\infty\frac{dx}{x^2+1}$. *Expected:* $\pi$.
2. **(Must)** $\int_{-\infty}^\infty\frac{\cos kx}{x^2+a^2}\,dx$ for $k,a>0$. *Expected:* $\frac\pi ae^{-ka}$. (Use $e^{ikx}$ and Jordan's lemma.)
3. **(Must)** $\int_0^\infty\frac{dx}{x^4+1}$. *Expected:* $\frac{\pi}{2\sqrt2}\approx1.1107$ (the whole-line integral is $\frac\pi{\sqrt2}$; the integrand is even).
4. **(Must)** $\int_0^{2\pi}\frac{d\theta}{2+\cos\theta}$. *Expected:* $\frac{2\pi}{\sqrt3}$. Hint: the integral becomes $\oint\frac{2\,dz}{i(z^2+4z+1)}$ with the pole $-2+\sqrt3$ inside.
5. **(Must)** $\int_{-\infty}^\infty\frac{\sin x}{x}\,dx$, by the indented contour. *Expected:* $\pi$ (from $\mathrm{PV}\!\int\frac{e^{ix}}{x}\,dx=i\pi$ and taking the imaginary part).
6. **(Should)** $\int_{-\infty}^\infty\frac{e^{ikx}}{k^2-m^2\pm i\epsilon}\,dk$, closing for $x>0$ and $x<0$. *Expected:* for $+i\epsilon$, $-\frac{i\pi}{m}e^{-im\lvert x\rvert}$; for $-i\epsilon$, $+\frac{i\pi}{m}e^{+im\lvert x\rvert}$. (EM Module 02, exercise 7.)
7. **(Should)** $\int_{-\infty}^\infty\frac{x\sin kx}{x^2+a^2}\,dx$ for $k,a>0$. *Expected:* $\pi e^{-ka}$.
8. **(Should)** For the damped oscillator response $\chi(\omega)=\frac1{\omega_0^2-\omega^2-i\gamma\omega}$ (with $e^{-i\omega t}$ time dependence): find its poles and show they lie in the lower half-plane, so $\chi$ is analytic in the upper half-plane; then verify numerically at one frequency that $\mathrm{Re}\,\chi(\omega)=\frac1\pi\mathrm{PV}\!\int\frac{\mathrm{Im}\,\chi(\omega')}{\omega'-\omega}\,d\omega'$. *Expected:* poles at $\omega=\frac{-i\gamma\pm\sqrt{4\omega_0^2-\gamma^2}}{2}$; for $\omega_0=1$, $\gamma=0.5$, $\omega=0.7$, $\chi\approx1.3330+0.9148\,i$ and both sides of the relation agree.
9. **(Could)** $\mathrm{PV}\!\int_{-\infty}^\infty\frac{\cos x}{x^2-1}\,dx$. *Expected:* $-\pi\sin1\approx-2.6436$. Hint: poles at $\pm1$ on the axis with residues $\frac{e^{i}}{2}$ and $-\frac{e^{-i}}{2}$.
10. **(Could)** $\int_{-\infty}^\infty\frac{dx}{(x^2+1)^2}$. *Expected:* $\frac\pi2$ (a double pole at $i$ with residue $-\frac i4$).

## Optional extension

Do exercise 6 with finite $\epsilon$ and check that as $\epsilon\to0$ you recover the stated results. Then do exercise 5 again with an indentation below the pole, and show you get the same real integral.

## Pitfalls

* Closing on the wrong side: check where $e^{iax}$ decays.
* Forgetting that real-axis poles make the integral undefined until a prescription is chosen.
* Dropping the arc without checking Jordan's lemma or the ML-estimate.
* Taking the full residue instead of half when the pole is on the contour.
* Getting the sign wrong when closing downward (clockwise).

## Gate questions

1. Why is the choice of how to go around a real-axis pole a physical choice and not a convention?
2. Why does Jordan's lemma work, and what happens for $a<0$?
3. Why does a small semicircle around a simple pole contribute exactly $\mp i\pi\,\mathrm{Res}$?

## One-page cheat sheet contents

The closing-contour recipe; Jordan's lemma; the indentation lemma; the principal-value formula; Sokhotski; the trigonometric substitution; the results of exercises 1 to 3, 5 and 6.

## Where this is used

CA09 and EM Module 11 (Green functions of the wave equation), EM Module 19 (Kramers–Kronig), EM Module 02 (exercises 6 to 8).
