# Module 20: Canonical perturbation theory and adiabatic invariants (optional, recommended)

**Books:** Goldstein Chapter 12 (12.1 introduction, 12.2 to 12.3 time-dependent perturbation theory, 12.4 time-independent perturbation theory, 12.5 adiabatic invariants); Landau and Lifshitz *Mechanics* sections 49 to 52 (adiabatic invariants and related material); your Zettili guide (Module 08 on time-independent perturbation theory and Module 09 on time-dependent perturbation theory).
**Time:** 2 weeks (four sessions). *Optional* because it is not on the minimal path, but **recommended** because it is the closest classical analogue of perturbation theory in quantum mechanics, and because adiabatic invariance is the classical Berry-phase story.

## Why this matters for the bridge

When a Hamiltonian is a small perturbation of an integrable one, $H=H_0(J)+\epsilon H_1(J,w)$, the first-order effect on the actions is an **average over the angle variables**, the exact classical counterpart of first-order quantum perturbation theory (the energy shift is the expectation value of the perturbation in the unperturbed state). The same machinery produces the **small denominators** $m\cdot\nu_0$ that signal resonances and, for many degrees of freedom, the breakdown of perturbation theory (KAM). And **adiabatic invariance**, the statement that the action $J$ is conserved under a slow change of parameters, is the classical statement of the quantum adiabatic theorem: the quantum number $n$ does not change.

## Skip-test (40 minutes, no notes)

1. Write $H=H_0(J)+\epsilon H_1(J,w)$ and expand $H_1=\sum_{\mathbf m}H_{1,\mathbf m}(J)e^{2\pi i\mathbf m\cdot\mathbf w}$; state that to first order the new action-dependent Hamiltonian is the average $\bar H=H_0(\bar J)+\epsilon\langle H_1\rangle(\bar J)$.
2. Compute the first-order energy shift of $H=\frac{p^2}{2m}+\frac12m\omega^2q^2+\epsilon q^4$ by averaging over an orbit: $\Delta E=\epsilon\langle q^4\rangle=\frac{3\epsilon E^2}{2m^2\omega^4}$.
3. State the adiabatic invariance of the action: if a parameter $\lambda(t)$ varies slowly compared with the orbital period, $J=\oint p\,dq$ is conserved to all orders in the slowness.
4. Show that for a harmonic oscillator with slowly varying frequency $E/\omega$ is constant.
5. State what a small denominator is and where it appears.

## Prerequisites

Modules 14, 15.

## Detailed topics (checklist)

**Time-dependent perturbation theory (12.2 to 12.3) [Should]**
- $H=H_0+\epsilon H_1(t)$; variation of constants: in terms of the action-angle variables $(J,w)$ of $H_0$, $\dot J=-\epsilon\frac{\partial H_1}{\partial w}$, $\dot w=\nu(J)+\epsilon\frac{\partial H_1}{\partial J}$; first-order integration along the unperturbed motion; the forced oscillator and resonance.
- Compare with the quantum time-dependent perturbation theory: the classical change in action is the analogue of the transition amplitude (Zettili Module 09).

**Time-independent perturbation theory (12.4) [Must]**
- The canonical transformation to new action-angle variables $(\bar J,\bar w)$ in which the perturbed Hamiltonian is a function of $\bar J$ only (order by order): generating function $S(w,\bar J)=w\bar J+\epsilon S_1+\dots$; first order: $\bar H=H_0(\bar J)+\epsilon\langle H_1\rangle(\bar J)$ with $\langle H_1\rangle=\frac{1}{(2\pi)^n}\oint H_1\,d^nw$; the frequency shift $\bar\nu=\partial\bar H/\partial\bar J$.
- **Small denominators:** $S_1=\sum_{\mathbf m\ne0}\frac{H_{1,\mathbf m}}{i\,\mathbf m\cdot\boldsymbol\nu}e^{2\pi i\mathbf m\cdot\mathbf w}$ diverges at resonances $\mathbf m\cdot\boldsymbol\nu=0$; the series generally diverges (Poincaré); the KAM theorem (statement): most invariant tori survive small perturbations. (Awareness; chaos is outside this guide.)
- Lie-series (von Zeipel) methods as a cleaner formulation (awareness).

**Adiabatic invariants (12.5) [Must]**
- If $H(q,p;\lambda(t))$ with $\lambda$ changing slowly, the action $J=\oint p\,dq$ is invariant (to exponentially small corrections for analytic $H$); applications: $E/\omega$ for the oscillator, the magnetic moment $\mu=\frac{mv_\perp^2}{2B}$ of a charged particle in a slowly varying field (magnetic mirrors, the Van Allen belts), the pendulum with slowly changing length.
- Quantum analogue: the adiabatic theorem: a slowly varied system stays in its quantum number $n$, so $E_n(t)=(n+\frac12)\hbar\omega(t)$ and $E/\omega$ is conserved; with $J=nh$ the classical and quantum statements coincide. The geometric (Hannay and Berry) phases are the next-order effect (awareness).

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Goldstein 12.1 and 12.4; derive first-order time-independent perturbation theory in action-angle form |
| B1 | Exercises 1 to 4 |
| A2 | Goldstein 12.5; derive adiabatic invariance heuristically (averaging over a period) |
| B2 | Exercises 5 to 10; Goldstein 12.2 to 12.3 (skim); cheat sheet |

## Derive from scratch (A sessions, book closed)

1. First-order canonical perturbation theory: $\bar H=H_0+\epsilon\langle H_1\rangle$.
2. The first-order generating function with its small denominators.
3. The anharmonic-oscillator frequency shift.
4. The adiabatic invariance of $J$ (averaging argument).
5. The invariance of the magnetic moment.

## Bare-minimum exercises (with expected results)

1. **Anharmonic oscillator:** for $H=\frac{p^2}{2m}+\frac12m\omega^2q^2+\epsilon q^4$ the orbit average gives $\Delta E=\frac{3\epsilon E_0^2}{2m^2\omega^4}$; with $E_0=\frac{\omega J}{2\pi}$ derive $\bar H(J)$ and the frequency $\bar\nu=\partial\bar H/\partial J$ (it grows with amplitude for $\epsilon>0$).
2. **Quantum comparison:** the quantum first-order shift is $\epsilon\langle n|\hat q^4|n\rangle=\epsilon\frac{3\hbar^2}{4m^2\omega^2}(2n^2+2n+1)$; show it reduces to the classical result for $n\gg1$ with $E_0=n\hbar\omega$ (the correspondence principle).
3. **Pendulum:** treat $V=-mg\ell\cos\theta=\text{const}+\frac12mg\ell\theta^2-\frac1{24}mg\ell\theta^4$ as an oscillator plus a quartic perturbation and show the frequency is $\omega(\theta_0)=\omega_0\left(1-\frac{\theta_0^2}{16}\right)$.
4. **Forced oscillator, resonance:** for $H=H_0+\epsilon q\cos\Omega t$ with $H_0$ the harmonic oscillator show the amplitude grows linearly in time at resonance ($\Omega=\omega$), so the action grows without bound (like $t^2$ from rest), while off resonance it stays bounded and oscillates.
5. **Adiabatic invariance:** for an oscillator with slowly varying $\omega(t)$ show $E/\omega$ is constant; for a pendulum whose length is slowly shortened, the amplitude scales as $\theta_0\propto\ell^{-3/4}$ (use $E=\frac12mg\ell\theta_0^2$, $\omega=\sqrt{g/\ell}$).
6. **Magnetic moment:** for a charge in a slowly varying $B$ the quantity $\mu=\frac{mv_\perp^2}{2B}$ is invariant (the action of the gyration is $\frac{2\pi m}{q}\mu$); a magnetic mirror reflects particles whose pitch angle satisfies $\sin^2\alpha>B_{\rm min}/B_{\rm max}$ (the loss-cone criterion).
7. **Quantum adiabatic theorem:** show that for $\hat H=\hbar\omega(t)(\hat a^\dagger\hat a+\frac12)$ with slowly varying $\omega$ the state $|n\rangle$ remains $|n\rangle$ with energy $(n+\frac12)\hbar\omega(t)$; compare with $E/\omega=$ const.
8. **Small denominators:** for $H_0=\nu_1J_1+\nu_2J_2$ and $H_1=\cos(m_1w_1-m_2w_2)$ show $S_1$ has the denominator $m_1\nu_1-m_2\nu_2$ and diverges at resonance.
9. **First-order averaging with a degenerate unperturbed system:** for the Kepler problem with the perturbation $H_1=-\beta/r^2$ the orbit average is $\langle r^{-2}\rangle=\frac{1}{a^2\sqrt{1-e^2}}$; use it to find the slow precession of the perihelion and confirm the result $\Delta\phi=2\pi\mu\beta/L^2$ per orbit of Module 05.
10. **Hannay's angle (optional):** a bead on a hoop slowly carried around a closed loop in parameter space acquires a geometric shift of its angle in addition to the dynamical one; state how it parallels Berry's phase.

## Optional extension

Do the Lie-transform (von Zeipel) calculation to second order for the anharmonic oscillator and compare the second-order energy with the quantum second-order perturbation theory result in the large-$n$ limit.

## Pitfalls

- Believing perturbation theory in $\epsilon$ converges (it is asymptotic and has small denominators).
- Applying adiabatic invariance when the change is not slow compared with the orbital period.
- Forgetting that the unperturbed motion must be integrable and expressed in action-angle variables.
- Treating degenerate unperturbed frequencies without care (the denominators vanish identically).

## Gate questions

1. Why is first-order perturbation theory an average over the angle variables?
2. What does it mean for $J$ to be an adiabatic invariant, and what is its quantum meaning?
3. What are small denominators, and what do they imply?

## One-page cheat sheet contents

$\bar H=H_0+\epsilon\langle H_1\rangle$; the generating function and small denominators; anharmonic and pendulum frequency shifts; adiabatic invariants and the magnetic moment.
