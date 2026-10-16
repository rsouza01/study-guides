# Module 10: Chapter 4, Spinors (Weeks 12 to 14; Protocol A shading into B)

**Books:** Klauber Ch. 4; second sources: Lancaster and Blundell (Dirac equation chapters), Tong's Dirac lectures, Schwartz chapter 10. If you ran the Zettili guide, its Module 11 (relativistic QM) covers the Dirac equation as first quantisation.
**Time:** 3 weeks. The algebra you have; the machinery underneath it you now also have; what remains is meaning.

## Why this matters

Chapter 4 re-runs the Chapter 3 construction with indices attached: the second instance of the same machinery (invariant measure, mode expansion, quantisation, propagator), plus gamma matrices, spin sums and the move from commutators to anticommutators.

## Diagnostic (40 minutes, no notes)

1. Derive $(\Box+m^2)\psi=0$ from the Dirac equation $(i\gamma^\mu\partial_\mu-m)\psi=0$ and the Clifford algebra.
2. Compute $\mathrm{tr}(\gamma^\mu\gamma^\nu)$ and $\mathrm{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)$.
3. State the spin sums $\sum_su\bar u$ and $\sum_sv\bar v$.
4. Show that quantising the Dirac field with commutators makes $H$ unbounded below; with anticommutators it is positive.
5. Write the spinor propagator and check that it inverts the Dirac operator.

## Prerequisites

Modules 03 to 09.

## Detailed topics (checklist)

**Week 12: the Dirac equation, gammas, covariance [Must]**
- $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$; $\gamma^\mu\gamma_\mu=4$, $\gamma^\mu\gamma^\nu\gamma_\mu=-2\gamma^\nu$, $\gamma^\mu\gamma^\nu\gamma^\rho\gamma_\mu=4g^{\nu\rho}$; representations (Dirac, Weyl/chiral); Lorentz covariance $\psi\to S(\Lambda)\psi$ with $S=\exp\left(-\tfrac i4\omega_{\mu\nu}\sigma^{\mu\nu}\right)$; $\bar\psi=\psi^\dagger\gamma^0$; the Dirac current $j^\mu=\bar\psi\gamma^\mu\psi$ with $j^0=\psi^\dagger\psi\ge0$.
- *Counterfactuals:* why first order: what breaks in KG that Dirac fixes, and does it fully fix it? Are gammas *matrices*, or is that an artefact of choosing a representation?

**Week 13: solutions, spin sums, projection operators, negative-energy states [Must]**
- Plane waves $u(p,s)e^{-ip\cdot x}$ and $v(p,s)e^{+ip\cdot x}$ with $(p\!\!\!/-m)u=0$, $(p\!\!\!/+m)v=0$, normalisation $\bar uu=2m$, $\bar vv=-2m$; spin sums $\sum_su\bar u=p\!\!\!/+m$, $\sum_sv\bar v=p\!\!\!/-m$; projection operators $\frac{p\!\!\!/\pm m}{2m}$; helicity and chirality.
- *Counterfactuals:* what do negative-energy solutions mean once the field is quantised, and why is the Dirac sea unnecessary?

**Week 14: quantisation and anticommutators; the spinor propagator [Must]**
- $\psi=\int\frac{d^3p}{(2\pi)^32E}\ldots\sum_s\left[b_su\,e^{-ip\cdot x}+d_s^\dagger v\,e^{ip\cdot x}\right]$ (with Klauber's normalisation: write the dictionary); $\{b,b^\dagger\}=\delta^3$, $\{d,d^\dagger\}=\delta^3$; $H=\int\omega\sum_s(b^\dagger b+d^\dagger d)$ after normal ordering; charge conservation; the spinor propagator $S_F(x-y)=\langle T\psi(x)\bar\psi(y)\rangle=\int\frac{d^4p}{(2\pi)^4}\frac{i(p\!\!\!/+m)}{p^2-m^2+i\epsilon}e^{-ip\cdot(x-y)}$.
- *Counterfactuals:* what forces anticommutators: is the argument a proof or a consistency requirement?

## Reading plan

| Week | Task |
| --- | --- |
| 12 | The Dirac equation, gammas, covariance; exercises 1 to 3; the [C] on spinors |
| 13 | Solutions, spin sums, negative energy; exercises 4 to 6 |
| 14 | Quantisation, anticommutators, propagator; exercises 7 to 10 |

## Derive from scratch

1. $(\Box+m^2)\psi=0$ from the Dirac equation.
2. The gamma-matrix contraction identities.
3. $\sum_su\bar u=p\!\!\!/+m$ in the rest frame and covariantly.
4. $H$ with commutators versus anticommutators.
5. The spinor propagator by contour integration (your Module 08 method).

## Exercises

1. **[T] Contractions:** $\gamma^\mu\gamma_\mu=4$; $\gamma^\mu\gamma^\nu\gamma_\mu=-2\gamma^\nu$; $\gamma^\mu\gamma^\nu\gamma^\rho\gamma_\mu=4g^{\nu\rho}$; $\gamma^\mu p\!\!\!/\gamma_\mu=-2p\!\!\!/$.
2. **[T] Traces:** $\mathrm{tr}(\gamma^\mu\gamma^\nu)=4g^{\mu\nu}$; $\mathrm{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)=4(g^{\mu\nu}g^{\rho\sigma}-g^{\mu\rho}g^{\nu\sigma}+g^{\mu\sigma}g^{\nu\rho})$; odd traces vanish; $\mathrm{tr}(p\!\!\!/q\!\!\!/)=4p\cdot q$.
3. **[T] Dirac implies KG:** $(i\gamma\cdot\partial+m)(i\gamma\cdot\partial-m)\psi=-(\Box+m^2)\psi$.
4. **[T] Rest-frame solutions:** in the Dirac representation $u(0,\pm)=\sqrt{2m}(\chi_\pm,0)^T$, $v(0,\pm)=\sqrt{2m}(0,\eta_\pm)^T$; check $(\gamma^0-1)u=0$ and $\sum_su\bar u=m(1+\gamma^0)=p\!\!\!/+m$ at $p=(m,\mathbf 0)$.
5. **[T] Spin sums:** $\sum_su\bar u=p\!\!\!/+m$, $\sum_sv\bar v=p\!\!\!/-m$; check $\mathrm{tr}\sum_su\bar u=4m$ (two spins, $\bar uu=2m$ each).
6. **[T] Current:** $\partial_\mu(\bar\psi\gamma^\mu\psi)=0$ on shell and $\psi^\dagger\psi\ge0$ for every solution, contrasting with the KG density.
7. **[T] Hamiltonian and statistics:** with anticommutators $:H:=\int\omega\sum_s(b^\dagger b+d^\dagger d)\ge0$; with commutators the antiparticle term enters as $-\omega\,d^\dagger d$ and $H$ is unbounded below.
8. **[T] The spinor propagator:** $S_F(p)=\frac{i(p\!\!\!/+m)}{p^2-m^2+i\epsilon}=\frac{i}{p\!\!\!/-m+i\epsilon}$; check $(p\!\!\!/-m)S_F=i$.
9. **[C] Spinors:** what is a spinor, stated without reference to how it transforms?
10. **[C] Positron and statistics:** is the positron a particle or a bookkeeping device? State the spin-statistics connection as an argument, not a rule.

## Optional extension

Compute the positive-frequency and negative-frequency parts of $S_F$ explicitly and show $S_F=\theta(x^0)\langle\psi\bar\psi\rangle-\theta(-x^0)\langle\bar\psi\psi\rangle$ (note the minus sign from fermionic time ordering).

## Pitfalls

- Mixing Klauber's spinor normalisation with $\bar uu=2m$ without a dictionary.
- Dropping the sign from fermionic time ordering.
- Treating the Dirac sea as necessary after field quantisation.

## Gate questions

1. Why does a first-order equation not remove the negative-energy solutions?
2. What forces anticommutators?
3. Why is the spin sum $p\!\!\!/+m$?

## One-page cheat sheet contents

Gamma contractions and traces; spin sums; mode expansion; anticommutators and $H$; the spinor propagator.
