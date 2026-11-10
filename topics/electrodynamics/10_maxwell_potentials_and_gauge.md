# Module 10: Faraday, Maxwell, potentials and gauge (★)

**Books:** Griffiths §7.1 (pp. 298 to 316), §7.2 (pp. 316 to 335), §7.3 Maxwell's Equations (pp. 335 to 347), §10.1 The Potential Formulation (pp. 442 to 450); Purcell and Morin 3rd ed. chapter 7 §7.1 to §7.5 (pp. 343 to 359), §7.10 (p. 368), chapter 9 §9.1 to §9.3 (pp. 430 to 438); Jackson 5.15 (pp. 208 to 212), 6.1 Maxwell's displacement current (pp. 237 to 239), 6.2 Vector and scalar potentials (pp. 239 to 240), **6.3 Gauge transformations, Lorenz gauge, Coulomb gauge (pp. 240 to 243)**.
**Time:** 2 weeks (four sessions).
**Pinned to:** Griffiths 5th ed. (2024), Jackson 3rd ed. (1999), Purcell and Morin 3rd ed. (2013, SI), Riley, Hobson and Bence 3rd ed. Page numbers are the printed book pages.

## Why this matters

$A_\mu\to A_\mu+\partial_\mu\Lambda$ leaves the fields untouched. This looks like a nuisance; it is the central organising principle of the Standard Model. Notice that the **Lorenz condition decouples** the equations into $\Box\Phi=-\rho/\epsilon_0$ and $\Box\mathbf A=-\mu_0\mathbf J$ (with $\Box=\nabla^2-\frac1{c^2}\partial_t^2$): four copies of one scalar wave equation. Solve it once and you have solved it four times: that is precisely why the scalar propagator is built first in QFT. Also, with a mechanics background you already met the canonical momentum $\mathbf p=m\mathbf v+q\mathbf A$; this module is where $\mathbf A$ as the gauge field earns its place.

## Skip-test (40 minutes, no notes)

1. Write Maxwell's equations in SI units and show that adding the displacement current is required for charge conservation: $\nabla\cdot(\nabla\times\mathbf B)=0\Rightarrow\partial_t\rho+\nabla\cdot\mathbf J=0$.
2. Define $\mathbf E=-\nabla\Phi-\partial_t\mathbf A$, $\mathbf B=\nabla\times\mathbf A$ and verify the two homogeneous Maxwell equations hold identically.
3. Show the Lorenz condition $\nabla\cdot\mathbf A+\frac1{c^2}\partial_t\Phi=0$ yields $\Box\Phi=-\rho/\epsilon_0$ and $\Box\mathbf A=-\mu_0\mathbf J$ ($\Box=\nabla^2-\frac1{c^2}\partial_t^2$, sign convention as in Jackson).
4. Show that the Lorenz condition can always be reached, and that the residual freedom is $\Box\Lambda=0$.
5. Count the physical degrees of freedom: $4-1-1=2$.

## Prerequisites

Modules 03 and 09; Module 01 (the identities $\nabla\times\nabla f=0$, $\nabla\cdot\nabla\times\mathbf F=0$); mechanics guide Module 02 (the velocity-dependent potential) if you have it.

## Detailed topics (checklist)

**Induction and Maxwell's equations (5.15, 6.1) [Must]**
- Faraday's law $\oint\mathbf E\cdot d\boldsymbol\ell=-\frac{d}{dt}\int\mathbf B\cdot d\mathbf a$ $\Leftrightarrow\nabla\times\mathbf E=-\partial_t\mathbf B$; motional emf and the flux rule; Maxwell's displacement current $\mu_0\epsilon_0\partial_t\mathbf E$ and why it is required; the four equations $\nabla\cdot\mathbf E=\rho/\epsilon_0$, $\nabla\cdot\mathbf B=0$, $\nabla\times\mathbf E=-\partial_t\mathbf B$, $\nabla\times\mathbf B=\mu_0\mathbf J+\mu_0\epsilon_0\partial_t\mathbf E$; $c=\frac{1}{\sqrt{\mu_0\epsilon_0}}$; the Lorentz force $\mathbf F=q(\mathbf E+\mathbf v\times\mathbf B)$.
- Charge conservation as a *consequence* of Maxwell's equations.

**Potentials (6.2) [Must]**
- $\mathbf B=\nabla\times\mathbf A$; $\mathbf E=-\nabla\Phi-\partial_t\mathbf A$; the two inhomogeneous equations in terms of $\Phi,\mathbf A$: $\nabla^2\Phi+\partial_t(\nabla\cdot\mathbf A)=-\rho/\epsilon_0$ and $\left(\nabla^2\mathbf A-\frac1{c^2}\partial_t^2\mathbf A\right)-\nabla\left(\nabla\cdot\mathbf A+\frac1{c^2}\partial_t\Phi\right)=-\mu_0\mathbf J$.

**Gauge transformations (6.3) [Must]**
- $\mathbf A\to\mathbf A+\nabla\Lambda$, $\Phi\to\Phi-\partial_t\Lambda$ leaves $\mathbf E,\mathbf B$ unchanged. **Lorenz gauge** $\nabla\cdot\mathbf A+\frac{1}{c^2}\partial_t\Phi=0$: decouples into four wave equations; always reachable (solve $\Box\Lambda=-(\nabla\cdot\mathbf A+\frac1{c^2}\partial_t\Phi)$); residual gauge freedom $\Box\Lambda=0$. **Coulomb gauge** $\nabla\cdot\mathbf A=0$: $\Phi$ is instantaneous Coulomb, $\nabla^2\Phi=-\rho/\epsilon_0$, and is non-dynamical; the transverse wave equation for $\mathbf A$ with a source $\mathbf J_\perp$.
- **Degree-of-freedom count:** $4$ components minus $1$ (Lorenz constraint) minus $1$ (residual gauge) $=2$ physical (transverse) polarizations; in Coulomb gauge $\Phi$ carries no dynamics and $\mathbf A$ has 2 transverse components.

## Method cards

**Faraday emf problem:** (1) define the loop and its orientation; (2) compute the flux $\Phi_B(t)$ through it (including motion of the loop or changing $\mathbf B$); (3) $\mathcal E=-\frac{d\Phi_B}{dt}$; (4) find the direction (Lenz); (5) check the power balance (mechanical work $=$ electrical dissipation).
**Potential formulation:** (1) write $\mathbf E=-\nabla\Phi-\partial_t\mathbf A$, $\mathbf B=\nabla\times\mathbf A$; (2) pick a gauge; (3) substitute in the two inhomogeneous equations; (4) simplify with the gauge condition; (5) recognize the wave equations.

## Reading plan (pinned to your editions)

A session is part A (read, derive) followed by part B (exercises), about two and a half hours in all. Page numbers are the printed ones.

| Session | A: read and derive | B: do | Done when |
| --- | --- | --- | --- |
| 1 | Griffiths §7.1 to §7.2 (pp. 298 to 335). Purcell §7.1 to §7.5 (pp. 343 to 359). The Faraday method card. | Module exercises 1 to 3. Griffiths Problems 7.7, 7.10, 7.8. Purcell Problems 7.3 and 7.2. | Rod and rotating loop agree by flux rule and by Lorentz force. |
| 2 | Griffiths §7.3 (pp. 335 to 347). Jackson 6.1 (pp. 237 to 239). Purcell §9.1 to §9.3. | Module exercise 4. Griffiths Problems 7.35 and 5.22. Purcell Problems 9.1 and 9.4. | Displacement current fixes Ampère in the capacitor gap. |
| 3 | Griffiths §10.1 (pp. 442 to 450). Jackson 6.2 to 6.3 (pp. 239 to 243). | Module exercises 5 to 8. Griffiths Problems 10.1, 10.4, 10.5, 10.6. | Gauge invariance of E and B shown; Coulomb gauge scalar potential instantaneous. |
| 4 | **Jackson target:** Problem 6.20 (with 6.21, 6.22). Redo the Lorenz-gauge derivation from a blank page. | Module exercises 9 and 10; spare. | Wave equations for $\Phi$ and $\mathbf A$ derived in under 15 minutes. |

## Problem set (pinned)

**Pin status:** Pinned: sections and problems in all three books (verified).

Tiers: **Must** (do all), **Should** (do when time allows), **Could** (only if the module is going well). A dash in the exercise column means the problem supports the reading rather than a module exercise. Purcell and Morin: stars give difficulty; problems are solved in Chapter 12 (the exercises are not).

| Book | Problem | What it asks | Module exercise | Tier |
| --- | --- | --- | --- | --- |
| Griffiths | 7.7 | metal bar sliding on rails | 1 | Must |
| Griffiths | 7.10 | square loop on a rotating shaft | 2 | Must |
| Griffiths | 7.35 | fat wire with a gap: displacement current | 3 | Must |
| Griffiths | 10.1 | differential equations for V and A | 5 | Must |
| Jackson | 6.20 | causality in the Coulomb gauge, an example | 9 | Must |
| Griffiths | 7.8 | square loop on a table near a wire | 1 | Should |
| Griffiths | 5.22 | is Ampere's law consistent with charge conservation | 4 | Should |
| Griffiths | 10.4 | a (V, A) pair: find the fields | 6 | Should |
| Griffiths | 10.5 | which potentials are in which gauge | 6 | Should |
| Griffiths | 10.6 | Coulomb gauge can always be reached | 8 | Should |
| Purcell | 7.3 ** | pulling a square frame | 1 | Should |
| Purcell | 9.1 ** | the missing term | 4 | Should |
| Purcell | 7.2 | what's doing work (B into the page) | 1 | Could |
| Purcell | 9.4 ** | B in a discharging capacitor | 4 | Could |
| Jackson | 6.21 | dipole in the Coulomb gauge | 9 | Could |
| Jackson | 6.22 | slowly moving off-centre dipole | 9 | Could |

## Derive from scratch

1. Charge conservation from the Ampere-Maxwell equation.
2. $\nabla\times\mathbf E=-\partial_t\mathbf B$ and $\nabla\cdot\mathbf B=0$ hold identically in terms of $\Phi,\mathbf A$.
3. The wave equations for $\Phi,\mathbf A$ in Lorenz gauge.
4. The reachability of the Lorenz gauge and the residual freedom.
5. The Coulomb-gauge equations for $\Phi$ and $\mathbf A$.

## Bare-minimum exercises (with expected results)

1. **Sliding rod:** a rod of length $\ell$ sliding at speed $v$ on rails in a uniform $B$ gives $\mathcal E=B\ell v$; the current $I=\frac{B\ell v}{R}$; the magnetic force $\frac{B^2\ell^2v}{R}$; the mechanical power equals $I^2R$.
2. **Rotating loop:** a loop of area $A$ rotating at angular velocity $\omega$ in a uniform $B$ has $\mathcal E=\omega BA\sin\omega t$.
3. **Displacement current:** a charging parallel-plate capacitor (circular plates of radius $R$) with current $I$ has, between the plates at radius $s<R$, $B=\frac{\mu_0Is}{2\pi R^2}$; check continuity with the wire field $\frac{\mu_0I}{2\pi s}$ at $s=R$.
4. **Charge conservation:** take the divergence of $\nabla\times\mathbf B=\mu_0\mathbf J+\mu_0\epsilon_0\partial_t\mathbf E$ and use Gauss's law to get $\partial_t\rho+\nabla\cdot\mathbf J=0$; without the displacement current this fails.
5. **Potentials:** in Lorenz gauge $\Box\Phi=-\frac{\rho}{\epsilon_0}$ and $\Box\mathbf A=-\mu_0\mathbf J$ with $\Box=\nabla^2-\frac{1}{c^2}\partial_t^2$ (check by substituting into Gauss's and Ampere-Maxwell's law).
6. **Gauge transformation:** show $\mathbf E,\mathbf B$ are invariant under $\mathbf A'=\mathbf A+\nabla\Lambda$, $\Phi'=\Phi-\partial_t\Lambda$; show $\Lambda$ with $\Box\Lambda=-\left(\nabla\cdot\mathbf A+\frac{1}{c^2}\partial_t\Phi\right)$ reaches the Lorenz gauge and that any $\Lambda$ with $\Box\Lambda=0$ preserves it.
7. **Counting:** explain why the Lorenz gauge leaves $4-1-1=2$ degrees of freedom and identify them as the two transverse polarizations of a plane wave $\mathbf A\propto\boldsymbol\epsilon e^{i(\mathbf k\cdot\mathbf x-\omega t)}$ with $\mathbf k\cdot\boldsymbol\epsilon=0$.
8. **Coulomb gauge:** in Coulomb gauge $\nabla^2\Phi=-\rho/\epsilon_0$ (instantaneous: no retardation) and $\Box\mathbf A=-\mu_0\mathbf J+\frac1{c^2}\nabla\partial_t\Phi$; show the right side is the transverse part $-\mu_0\mathbf J_\perp$ (use $\nabla\cdot\mathbf J=-\partial_t\rho$).
9. **Jackson target (about 6.20):** an explicit gauge transformation between the Coulomb and Lorenz gauges: given Lorenz-gauge $(\Phi_L,\mathbf A_L)$ find $\Lambda$ with $\nabla^2\Lambda=-\nabla\cdot\mathbf A_L$ so that $\mathbf A_C=\mathbf A_L+\nabla\Lambda$ is transverse and $\Phi_C=\Phi_L-\partial_t\Lambda$; verify $\Phi_C$ satisfies $\nabla^2\Phi_C=-\rho/\epsilon_0$ (use $\nabla\cdot\mathbf A_L=-\frac1{c^2}\partial_t\Phi_L$).
10. **Jackson target (a derivation):** derive the wave equations for the potentials from Maxwell's equations, in your own words, as in your Month-3 gate.

## Optional extension

Show that the gauge invariance $\mathbf A\to\mathbf A+\nabla\Lambda$ is the same as the freedom to shift the canonical momentum $\mathbf p=m\mathbf v+q\mathbf A$ you met in mechanics (mechanics guide Module 02), and that the physical (kinetic) momentum is gauge-invariant.

## Pitfalls

- Believing $\Phi$ and $\mathbf A$ are separately meaningful (only $\mathbf E$ and $\mathbf B$ are).
- Using the Lorenz gauge and forgetting the residual freedom.
- Sign errors in $\Box=\nabla^2-\frac{1}{c^2}\partial_t^2$ between texts.
- Thinking Coulomb gauge violates relativity (the *fields* $\mathbf E,\mathbf B$ are still retarded).

## Gate questions

1. Why is the displacement current required by charge conservation?
2. Why does the Lorenz gauge make the potential equations four copies of the scalar wave equation?
3. Why are there only two physical degrees of freedom?

## One-page cheat sheet contents

Maxwell's equations; potentials and gauge transformation; Lorenz and Coulomb gauge equations; DOF count.
