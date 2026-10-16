# Module 08: Meson exchange and the Yukawa potential (★★, Week 7)

**Books:** **Walecka chapter 1**, the meson-exchange sections (the chapter's climax and the hinge of the book); Bertulani's one-boson-exchange discussion alongside. Optional second voice on the static Klein-Gordon and Proca equations: any electrodynamics text (your electrodynamics guide, Modules 05 and 17).
**Time:** 1 week (budget about 2 hours for the self-contained derivation).

## Why this matters

A massive mediator gives $V\propto\frac{e^{-mr}}{r}$ with range $\frac{\hbar}{mc}$; for the pion, $1.41$ fm. One-pion exchange (OPEP) comes out as
$$V_{\rm OPEP}=\frac{f_\pi^2}{4\pi}\frac{m_\pi}{3}(\boldsymbol\tau_1\cdot\boldsymbol\tau_2)\left[\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2+S_{12}\left(1+\frac{3}{m_\pi r}+\frac{3}{(m_\pi r)^2}\right)\right]\frac{e^{-m_\pi r}}{m_\pi r}\quad\left(\tfrac{f_\pi^2}{4\pi}\approx0.075\right),$$
**the tensor force falls out of pion exchange automatically**: the deuteron quadrupole moment stops being a fact and becomes a consequence. Then extend: intermediate attraction from scalar-isoscalar exchange (the "$\sigma$") and short-range repulsion from vector-isoscalar exchange (the $\omega$). **Box these two: they are QHD-I.** You meet the $\sigma$-$\omega$ model here, thirteen modules before it gets its name.

## Skip-test (40 minutes, no notes)

1. Solve $(-\nabla^2+m^2)\phi=g\delta^3(\mathbf r)$ in momentum space and invert by contour integration to obtain $\phi=\frac{g}{4\pi}\frac{e^{-mr}}{r}$.
2. Repeat for a massive vector field with a conserved-current source (the Proca case): $(-\nabla^2+m^2)V^0=g\rho$.
3. Show that scalar exchange between like sources attracts and vector exchange repels, from the energy of the static field configuration.
4. Evaluate $\boldsymbol\tau_1\cdot\boldsymbol\tau_2$ and $\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2$ in the four $(S,T)$ channels and tabulate the OPEP strengths.
5. Show $(\boldsymbol\sigma_1\cdot\nabla)(\boldsymbol\sigma_2\cdot\nabla)\frac{e^{-mr}}{r}$ contains the tensor operator $S_{12}$.

## Prerequisites

Modules 01 and 06.

## Detailed topics (checklist)

**The static field equations [Must]**
- Scalar: $\mathcal L=\tfrac12(\partial\phi)^2-\tfrac12m^2\phi^2-g\phi\rho_s$; static equation $(-\nabla^2+m^2)\phi=-g\rho_s$. Vector: $\mathcal L=-\tfrac14F_{\mu\nu}F^{\mu\nu}+\tfrac12m^2V_\mu V^\mu-gV_\mu J^\mu$; static equation with $J^\mu=(\rho,\mathbf 0)$: $(-\nabla^2+m^2)V^0=g\rho$.
- Fourier inversion: $\int\frac{d^3q}{(2\pi)^3}\frac{e^{i\mathbf q\cdot\mathbf r}}{q^2+m^2}=\frac{e^{-mr}}{4\pi r}$ (the angular integral gives $\frac{\sin qr}{qr}$, then close the $q$ contour in the upper half plane picking the pole at $q=im$).

**The sign rule [Must]**
- On shell $\int\left[\tfrac12(\nabla\phi)^2+\tfrac12m^2\phi^2\right]=-\tfrac12g\int\rho_s\phi$ for the scalar, giving a static energy $E=-\frac{g^2}{4\pi}\frac{e^{-mr}}{r}$ between like sources (attraction). For the vector the time component $V^0$ enters the Lagrangian with the "wrong" sign (as in electrodynamics), giving $E=+\frac{g^2}{4\pi}\frac{e^{-mr}}{r}$ (repulsion). **That one sign is the entire saturation mechanism of Module 22.**

**OPEP [Must]**
- Pseudoscalar coupling $\sim\frac{f}{m_\pi}\bar\psi\gamma^5\gamma^\mu\boldsymbol\tau\psi\cdot\partial_\mu\boldsymbol\pi$; the static amplitude $\propto\frac{(\boldsymbol\sigma_1\cdot\mathbf q)(\boldsymbol\sigma_2\cdot\mathbf q)}{q^2+m_\pi^2}(\boldsymbol\tau_1\cdot\boldsymbol\tau_2)$; its Fourier transform is $\frac13\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2\left[m^2\frac{e^{-mr}}r-4\pi\delta^3\right]+\frac13S_{12}\left(m^2+\frac{3m}{r}+\frac{3}{r^2}\right)\frac{e^{-mr}}{r}$; the $\delta$ term is dropped (hard core). The tensor force emerges from the spin structure, not from an extra postulate.
- Heavier exchanges: $\sigma$ ($\sim500$ to $550$ MeV, scalar-isoscalar), $\rho$ ($770$ MeV, vector-isovector, tensor), $\omega$ ($783$ MeV, vector-isoscalar).

## Method card

**Static Yukawa from a field equation:** (1) write the equation $(-\nabla^2+m^2)\psi=\text{source}$; (2) Fourier transform to $\tilde\psi=\frac{\widetilde{\rm source}}{q^2+m^2}$; (3) invert with $\int\frac{d^3q}{(2\pi)^3}\frac{e^{i\mathbf q\cdot\mathbf r}}{q^2+m^2}=\frac{e^{-mr}}{4\pi r}$ (angular integral, then residue at $q=im$); (4) multiply by the source strength; (5) get the interaction energy from the on-shell field energy and read the sign.

## Reading plan

| Block | Reading |
| --- | --- |
| Session 1 | Walecka chapter 1, meson-exchange sections; the self-contained derivation (exercise 1) |
| Session 2 | Bertulani OBE; exercises 2 and 3 |
| Session 3 | OPEP and the tensor operator; exercises 4 to 6 |
| Session 4 | The $\sigma$-$\omega$ potential; exercises 7 to 10 |

## Derive from scratch

1. The static Klein-Gordon Green function.
2. The same for the massive vector with a conserved current.
3. The sign rule from the static energy.
4. The OPEP spin-isospin structure and the tensor operator.
5. The $\sigma$-$\omega$ two-body potential.

## Bare-minimum exercises (with expected results)

1. **Yukawa (both cases):** carry out the derivation above for the scalar and the Proca case and **keep both pages**: $\phi=-\frac{g}{4\pi}\int\rho_s(\mathbf x')\frac{e^{-m|\mathbf x-\mathbf x'|}}{|\mathbf x-\mathbf x'|}d^3x'$ and $V^0=+\frac{g}{4\pi}\int\rho\frac{e^{-mR}}{R}d^3x'$.
2. **Sign rule:** show $E_{\rm int}^{\rm scalar}=-\frac{g_1g_2}{4\pi}\frac{e^{-mr}}{r}$ and $E_{\rm int}^{\rm vector}=+\frac{g_1g_2}{4\pi}\frac{e^{-mr}}{r}$ for like sources, from the on-shell energies above (the vector's $V^0$ has the opposite sign of kinetic energy).
3. **Spin-isospin table:** $(\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2)(\boldsymbol\tau_1\cdot\boldsymbol\tau_2)$ is $-3$ for $(S,T)=(1,0)$, $-3$ for $(0,1)$, $+1$ for $(1,1)$, $+9$ for $(0,0)$; the tensor coefficient is $\boldsymbol\tau_1\cdot\boldsymbol\tau_2$ (acting only for $S=1$): $-3$ for the deuteron channel, $+1$ for $T=1$; check the sign pattern against the known phase shifts.
4. **Ranges:** $\frac{\hbar c}{m_\pi}=1.41$ fm, $\frac{\hbar c}{550\,{\rm MeV}}=0.36$ fm, $\frac{\hbar c}{783\,{\rm MeV}}=0.25$ fm; why the heavier mesons give the short-range part of the force.
5. **Contour inversion:** $\int\frac{d^3q}{(2\pi)^3}\frac{e^{i\mathbf q\cdot\mathbf r}}{q^2+m^2}=\frac{1}{4\pi^2ir}\int_{-\infty}^\infty\frac{qe^{iqr}}{q^2+m^2}dq=\frac{e^{-mr}}{4\pi r}$ (close in the upper half plane; residue at $q=im$).
6. **Tensor from the gradient structure:** show $(\boldsymbol\sigma_1\cdot\nabla)(\boldsymbol\sigma_2\cdot\nabla)\frac{e^{-mr}}{r}=\frac13\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2\left(m^2\frac{e^{-mr}}{r}-4\pi\delta^3\right)+\frac13S_{12}\left(m^2+\frac{3m}{r}+\frac3{r^2}\right)\frac{e^{-mr}}{r}$ (use $\partial_i\partial_j\frac{e^{-mr}}{r}$ decomposed into trace and traceless parts).
7. **$\sigma$-$\omega$ potential:** with $\frac{g_s^2}{4\pi}=7.29$, $\frac{g_v^2}{4\pi}=10.83$, $m_s=550$, $m_v=783$ MeV: $V(r)=\frac{\hbar c}{r}\left[-\frac{g_s^2}{4\pi}e^{-m_sr/\hbar c}+\frac{g_v^2}{4\pi}e^{-m_vr/\hbar c}\right]$ gives $+713$ MeV at $0.2$ fm, $+88$ at $0.3$, $-87$ at $0.4$, $-126$ (the minimum region) at $0.5$ and $-82$ at $0.8$ fm: repulsive inside $\approx0.34$ fm, attractive outside: short-range repulsion and intermediate attraction.
8. **Why the vector wins at short distance:** the vector range is shorter but its coupling larger; verify the crossing radius $\approx0.34$ fm from the numbers above.
9. **Isovector structure:** with $\boldsymbol\tau_1\cdot\boldsymbol\tau_2$ for the $\rho$ (vector-isovector), show the like-nucleon $\rho$ exchange is repulsive and unlike attractive (it sources the symmetry energy, Module 24).
10. **Month-2 gate prep:** attempt the five blank-page items listed in Module 09.

## Optional extension

Derive the Yukawa potential from the Born amplitude of Module 01 exercise 6: the $q$-space pole at $q^2=-m^2$ is the exchanged mass.

## Pitfalls

- Getting the overall sign of the interaction energy wrong by using the Lagrangian instead of the Hamiltonian ($E=-L$ for static sources).
- Forgetting the $\delta$-function term in the Fourier transform (it is the contact term that the hard core replaces).
- Confusing the scalar $\sigma$ with the isovector pion.

## Gate questions

1. Why does scalar exchange attract and vector exchange repel?
2. Where does the tensor force come from in OPEP?
3. What sets the range of each meson exchange?

## One-page cheat sheet contents

Static Yukawa derivation; sign rule; OPEP spin-isospin structure; meson ranges; the $\sigma$-$\omega$ potential.
