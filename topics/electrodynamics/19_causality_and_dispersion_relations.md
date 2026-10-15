# Module 19: Causality, analyticity and dispersion relations (★)

**Books:** Jackson 7.8 (superposition of waves: group velocity and pulse propagation in a dispersive medium), 7.9 (pulse spreading: light), **7.10 (causality in the connection between $\mathbf D$ and $\mathbf E$; the Kramers-Kronig relations)**, 7.11 (arrival of a signal: optional, lovely); Griffiths 9.3 to 9.4 (waves in matter, absorption and dispersion). Module 02 (contour integrals, Sokhotski) is the prerequisite.
**Time:** 2 weeks (four sessions).

## Why this matters

**Causality alone**, the response cannot precede the stimulus, forces the response function to be analytic in the upper half plane, which forces an integral relation between its real and imaginary parts. Causality $\to$ analyticity $\to$ dispersion relation: that implication chain is one of the deepest structural facts in physics, and here it is derived in three pages with nothing but contour integration. In QFT the same chain gives dispersion relations for scattering amplitudes and the analytic structure of propagators; in astrophysics it gives you the dispersion of radio pulses from pulsars.

## Skip-test (40 minutes, no notes)

1. Write the Lorentz-oscillator dielectric function $\frac{\epsilon(\omega)}{\epsilon_0}=1+\frac{\omega_p^2}{\omega_0^2-\omega^2-i\gamma\omega}$ and identify the real and imaginary parts, absorption and anomalous dispersion.
2. Write the causal relation $\mathbf D(t)=\epsilon_0\left[\mathbf E(t)+\int_0^\infty G(\tau)\mathbf E(t-\tau)d\tau\right]$ and show that $\chi(\omega)=\int_0^\infty G(\tau)e^{i\omega\tau}d\tau$ is analytic in the upper half $\omega$-plane.
3. Derive the Kramers-Kronig relations $\frac{\mathrm{Re}\,\epsilon(\omega)}{\epsilon_0}=1+\frac2\pi\mathrm P\!\!\int_0^\infty\frac{\omega'\,\mathrm{Im}\,\epsilon(\omega')/\epsilon_0}{\omega'^2-\omega^2}d\omega'$ and $\frac{\mathrm{Im}\,\epsilon(\omega)}{\epsilon_0}=-\frac{2\omega}{\pi}\mathrm P\!\!\int_0^\infty\frac{\mathrm{Re}\,\epsilon(\omega')/\epsilon_0-1}{\omega'^2-\omega^2}d\omega'$.
4. Define phase velocity $\frac\omega k$ and group velocity $\frac{d\omega}{dk}$, and compute both for $\omega^2=c^2k^2+\omega_p^2$.
5. State the high-frequency limit $\frac{\epsilon}{\epsilon_0}\to1-\frac{\omega_p^2}{\omega^2}$ and the sum rule it implies.

## Prerequisites

Module 02 (residues, principal value, $\frac{1}{x\pm i\epsilon}$); Module 12 (plane waves).

## Detailed topics (checklist)

**Dispersion and wave packets (7.8 to 7.9) [Should]**
- Superposition of plane waves with $\omega(k)$; phase velocity $v_p=\frac\omega k$, group velocity $v_g=\frac{d\omega}{dk}$; pulse spreading from the curvature of $\omega(k)$; the Lorentz-oscillator and plasma models; refractive index $n(\omega)=\sqrt{\epsilon/\epsilon_0}$; absorption coefficient $\alpha\propto\mathrm{Im}\,n$; anomalous dispersion near a resonance.
- **Plasma:** $\epsilon(\omega)/\epsilon_0=1-\frac{\omega_p^2}{\omega^2}$, $\omega_p^2=\frac{4\pi ne^2}{m}$ (Gaussian), $\omega^2=c^2k^2+\omega_p^2$: the same dispersion relation as the Proca field of Module 17 with $\mu c=\omega_p$ (the plasma as a "massive photon"), $v_pv_g=c^2$.

**Causality and analyticity (7.10) [Must]**
- $\mathbf D(t)=\epsilon_0\left[\mathbf E(t)+\int_0^\infty G(\tau)\mathbf E(t-\tau)d\tau\right]$ with $G(\tau)=0$ for $\tau<0$ (causality); the Fourier transform $\chi(\omega)=\int_0^\infty G(\tau)e^{i\omega\tau}d\tau$ converges for $\mathrm{Im}\,\omega>0$, so $\chi$ is **analytic in the upper half-plane**; reality of $G$ gives $\chi(-\omega^*)=\chi^*(\omega)$.
- **Kramers-Kronig:** apply Cauchy's theorem to $\frac{\chi(\omega')}{\omega'-\omega}$ over the real axis plus a large semicircle, with the pole on the contour treated by the Sokhotski formula: $\chi(\omega)=\frac{1}{i\pi}\mathrm P\!\!\int_{-\infty}^\infty\frac{\chi(\omega')}{\omega'-\omega}d\omega'$; separate real and imaginary parts and use the symmetry to restrict to positive frequencies.
- Consequences: a medium with absorption must have dispersion; the **sum rule** $\int_0^\infty\omega\,\frac{\mathrm{Im}\,\epsilon(\omega)}{\epsilon_0}d\omega=\frac{\pi}{2}\omega_p^2$ from the high-frequency limit; the static limit $\frac{\epsilon(0)}{\epsilon_0}=1+\frac2\pi\int_0^\infty\frac{\mathrm{Im}\,\epsilon(\omega')/\epsilon_0}{\omega'}d\omega'$.

**Signals (7.11) [Could]**
- The signal velocity and the front velocity: the front of a pulse travels at $c$ even when $v_g>c$ or $v_g<0$ (anomalous dispersion); precursors.

## Method card

**Kramers-Kronig derivation:** (1) write $\chi(\omega)=\int_0^\infty G(\tau)e^{i\omega\tau}d\tau$ and state analyticity in $\mathrm{Im}\,\omega>0$; (2) consider $\oint\frac{\chi(\omega')}{\omega'-\omega}d\omega'$ with $\omega$ real, closing in the upper half-plane (the semicircle vanishes if $\chi\to0$ fast enough); (3) indent around the pole (half-residue) to get $\mathrm P\!\!\int\frac{\chi(\omega')}{\omega'-\omega}d\omega'=i\pi\chi(\omega)$; (4) split into $\mathrm{Re}$ and $\mathrm{Im}$; (5) use $\chi(-\omega)=\chi^*(\omega)$ to fold onto $\omega'>0$.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Jackson 7.8 to 7.9 (skim 7.9); Griffiths 9.3 to 9.4; group velocity (exercises 1 and 6) |
| B1 | Exercises 1 and 6 |
| A2 | Jackson 7.10; the derivation (method card) |
| B2 | Exercises 2 to 4 |
| A3 | Sum rules; pulsar dispersion |
| B3 | Exercises 5 and 7 |
| A4 | Jackson 7.11 (optional); **Jackson targets** (exercise 10) |
| B4 | Spare session |

## Derive from scratch

1. Analyticity of $\chi(\omega)$ in the upper half-plane from causality.
2. The Kramers-Kronig relations by contour integration.
3. The sum rule $\int_0^\infty\omega\,\mathrm{Im}\,\epsilon\,d\omega=\frac{\pi}2\epsilon_0\omega_p^2$.
4. Phase and group velocity for the plasma dispersion.
5. The Lorentz-model real and imaginary parts.

## Bare-minimum exercises (with expected results)

1. **Lorentz model:** $\frac{\epsilon}{\epsilon_0}=1+\omega_p^2\frac{(\omega_0^2-\omega^2)+i\gamma\omega}{(\omega_0^2-\omega^2)^2+\gamma^2\omega^2}$; $\mathrm{Im}\,\epsilon$ has a Lorentzian peak at $\omega_0$ with width $\approx\gamma$; $\mathrm{Re}\,\epsilon$ decreases between the two points $\omega_0\pm\frac\gamma2$ (anomalous dispersion) and equals $1+\frac{\omega_p^2}{\omega_0^2}$ at $\omega=0$.
2. **Analyticity:** for $G(\tau)=0$ for $\tau<0$ and $|G|$ bounded, $|e^{i\omega\tau}|=e^{-\tau\,\mathrm{Im}\,\omega}\le1$ for $\mathrm{Im}\,\omega>0$; hence $\chi$ is analytic there. For the Lorentz model check that the poles $\omega=\pm\sqrt{\omega_0^2-\gamma^2/4}-\frac{i\gamma}{2}$ lie in the *lower* half-plane.
3. **Kramers-Kronig:** carry out the contour derivation and obtain the two integral relations above; show $\chi(-\omega)=\chi^*(\omega)$ for real $G$.
4. **Static limit check:** for the Lorentz model verify $1+\frac{\omega_p^2}{\omega_0^2}=1+\frac2\pi\int_0^\infty\frac{\mathrm{Im}\,\epsilon/\epsilon_0}{\omega'}d\omega'$ (do the integral with $\gamma\to0$: the Lorentzian becomes $\frac{\pi\omega_p^2}{2\omega_0}\delta(\omega-\omega_0)$).
5. **Sum rule:** at high frequency $\frac{\epsilon}{\epsilon_0}\approx1-\frac{\omega_p^2}{\omega^2}$; the Kramers-Kronig relation then requires $\frac2\pi\int_0^\infty\omega'\,\mathrm{Im}\frac{\epsilon}{\epsilon_0}d\omega'=\omega_p^2$, i.e. $\int_0^\infty\omega\,\mathrm{Im}\frac{\epsilon}{\epsilon_0}d\omega=\frac\pi2\omega_p^2$ (the f-sum rule: the total oscillator strength equals the number of electrons).
6. **Plasma waves:** $\omega^2=c^2k^2+\omega_p^2$ gives $v_p=\frac{c}{\sqrt{1-\omega_p^2/\omega^2}}>c$, $v_g=c\sqrt{1-\omega_p^2/\omega^2}<c$, $v_pv_g=c^2$; waves with $\omega<\omega_p$ are evanescent; $\omega_p=5.64\times10^4\sqrt{n/{\rm cm}^{-3}}$ rad/s (for $n=10^8$ cm$^{-3}$ in the solar corona $\omega_p/2\pi\approx90$ MHz).
7. **Pulsar dispersion:** a radio pulse travels through the interstellar plasma with $v_g\approx c\left(1-\frac{\omega_p^2}{2\omega^2}\right)$; the arrival delay relative to infinite frequency is $\Delta t=\frac{1}{2c}\frac{\omega_p^2}{\omega^2}L\to\frac{e^2}{2\pi m_ec}\frac{\mathrm{DM}}{\nu^2}\approx4.15\ {\rm ms}\times\mathrm{DM}\,\nu_{\rm GHz}^{-2}$ with the dispersion measure $\mathrm{DM}=\int n\,dl$ in pc cm$^{-3}$; this is how pulsar distances and the interstellar electron density are measured.
8. **Pulse spreading:** a Gaussian packet of initial width $\sigma_0$ in a medium with $\omega''(k)\ne0$ broadens as $\sigma(t)=\sigma_0\sqrt{1+\left(\frac{\omega''t}{2\sigma_0^2}\right)^2}$; estimate for visible light in glass over a metre ($\omega''$ small, negligible) versus a pulse in a fibre over kilometres.
9. **Signal velocity (optional):** explain why anomalous dispersion with $v_g>c$ does not violate causality (the front travels at $c$ because $\chi\to0$ as $\omega\to\infty$).
10. **Jackson targets (about 7.22 and a group-velocity problem):** (a) apply the Kramers-Kronig relations to a model dielectric (exercises 3 and 4) and check them numerically; (b) a group-velocity problem such as exercise 6 or 8.

## Optional extension

Show that a response function with a *finite* high-frequency limit that is not analytic (for instance one with a branch cut in the upper half-plane) would violate causality; and apply the same argument to the quantum-mechanical forward scattering amplitude $f(E)$ to derive the first dispersion relation (the optical theorem: Appendix A of the guide).

## Pitfalls

- Using the wrong sign of the Fourier exponent: analyticity in the *upper* half-plane goes with $e^{-i\omega t}$ and $\chi(\omega)=\int G(\tau)e^{+i\omega\tau}d\tau$.
- Forgetting the principal value and the half-residue from the pole on the contour.
- Folding the integrals to $\omega>0$ without using $\chi(-\omega)=\chi^*(\omega)$.
- Equating group velocity with signal velocity.

## Gate questions

1. Why does causality imply analyticity of the response function in the upper half-plane?
2. Why does absorption imply dispersion?
3. Why can the group velocity exceed $c$ without violating causality?

## One-page cheat sheet contents

Lorentz and plasma models; Kramers-Kronig relations; sum rule; group and phase velocity; pulsar delay formula.
