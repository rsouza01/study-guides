# Module 04: Adiabatic processes of stellar gases

**Books:** Schroeder (chapters 1 and 4: adiabatic processes, compression, ideal-gas heat capacities), Callen (formal relationships, adiabats), Blundell and Blundell (heat capacities, adiabatic processes, radiation), Pathria (gas plus radiation as an example).
**Time:** 2 weeks.

## Why this matters for stars and EOS

Almost every thermodynamic coefficient used in stellar structure and pulsation is an **adiabatic derivative**:

- the adiabatic exponents $\Gamma_1,\Gamma_2,\Gamma_3$ and the adiabatic gradient $\nabla_{\rm ad}$ (convection criterion, temperature gradient in convective zones, polytropic structure);
- the sound speed $c_s^2=\Gamma_1P/\rho$ (acoustic modes, pulsation, hydrostatic response);
- the thermal response of a gas to compression or expansion, which sets the stability of stars and of burning shells.

For an ideal monatomic gas these are trivial ($5/3$, $0.4$); for gas plus radiation, partially ionized gas and degenerate matter they are not.

## Skip-test (40 minutes, no notes)

1. For a monatomic ideal gas derive $PV^{5/3}={\rm const}$ and $TV^{2/3}={\rm const}$ along an adiabat, and $c_s^2=\frac53P/\rho$.
2. Define $\Gamma_1=\left(\frac{\partial\ln P}{\partial\ln\rho}\right)_S$, $\frac{\Gamma_2}{\Gamma_2-1}=\left(\frac{\partial\ln P}{\partial\ln T}\right)_S$, $\Gamma_3-1=\left(\frac{\partial\ln T}{\partial\ln\rho}\right)_S$ and show $\frac{\Gamma_1}{\Gamma_3-1}=\frac{\Gamma_2}{\Gamma_2-1}$, with $\nabla_{\rm ad}=\frac{\Gamma_2-1}{\Gamma_2}$.
3. Show $\Gamma_1=\chi_\rho+\frac{P}{\rho Tc_V}\chi_T^2$ and $\nabla_{\rm ad}=\frac{P\delta}{\rho Tc_P}$.
4. For blackbody radiation show $\Gamma_1=\Gamma_2=\Gamma_3=4/3$ and $\nabla_{\rm ad}=1/4$.
5. For a mixture of ideal gas and radiation with $\beta=P_{\rm gas}/P$ quote $\nabla_{\rm ad}=\frac{2(4-3\beta)}{32-24\beta-3\beta^2}$ and verify the limits $\beta=1$ and $\beta=0$.

## Prerequisites

Modules 02 and 03.

## Detailed topics (checklist)

**Adiabatic processes**
- Reversible adiabatic means $dS=0$. Derivation of adiabats from the entropy: $PV^\gamma={\rm const}$, $TV^{\gamma-1}={\rm const}$ for constant $\gamma=C_P/C_V=\frac{f+2}{f}$.
- Adiabatic versus isothermal compressibility; sound speed $c_s^2=\left(\frac{\partial P}{\partial\rho}\right)_S=\frac{\Gamma_1P}{\rho}$.

**The adiabatic exponents** (derive each)
- $\Gamma_1=\left(\frac{\partial\ln P}{\partial\ln\rho}\right)_S=\frac{\chi_\rho}{1-\chi_T\nabla_{\rm ad}}$.
- $\Gamma_2/(\Gamma_2-1)=\left(\frac{\partial\ln P}{\partial\ln T}\right)_S=\frac1{\nabla_{\rm ad}}$.
- $\Gamma_3-1=\left(\frac{\partial\ln T}{\partial\ln\rho}\right)_S$, with $\Gamma_3-1=\frac{P}{\rho Tc_V}\chi_T$.
- $\nabla_{\rm ad}=\frac{P\delta}{\rho Tc_P}=\frac{\Gamma_2-1}{\Gamma_2}$.
- Relation to polytropes: an adiabatic fluid obeys $P\propto\rho^{\Gamma_1}$ only when $\Gamma_1$ is constant.

**Gas plus radiation**
- $P=P_{\rm gas}+P_{\rm rad}$, $\beta=P_{\rm gas}/P$, $u=\frac{3}{2}\frac{\rho kT}{\mu m_u}+aT^4$.
- Results (derive):
$$\Gamma_1=\beta+\frac{(4-3\beta)^2(\gamma-1)}{\beta+12(\gamma-1)(1-\beta)},\quad\nabla_{\rm ad}=\frac{2(4-3\beta)}{32-24\beta-3\beta^2}\quad(\gamma=5/3),$$
with $\Gamma_1\to5/3$, $\nabla_{\rm ad}\to0.4$ for $\beta\to1$ and $\Gamma_1\to4/3$, $\nabla_{\rm ad}\to0.25$ for $\beta\to0$.
- Physical meaning: radiation makes the gas "softer" ($\Gamma_1<5/3$), which matters for the stability of massive stars (the dynamical stability limit is $\Gamma_1=4/3$).

**Other EOS regimes (preview; derived in later modules)**
- Partial ionization lowers $\Gamma_1$ and $\nabla_{\rm ad}$ because part of the compression energy goes into ionization (Module 05).
- Non-relativistic degenerate electrons: $P\propto\rho^{5/3}$, $\Gamma_1=5/3$, independent of $T$; ultra-relativistic degenerate: $\Gamma_1=4/3$ (Module 10).

## Reading plan

| Block | Reading |
| --- | --- |
| Lunch 1 | Schroeder chapter 1 (adiabatic compression, heat capacity of gases) and chapter 4 (relevant sections) |
| Lunch 2 | Blundell and Blundell on adiabatic processes and heat capacities |
| Lunch 3 | Callen's formal relationships (derivative identities) |
| Lunch 4 | Pathria: gas-plus-radiation examples (the Eddington standard model of stars appears in stellar physics books; derive it here) |
| Week 2 lunches | Review; compute $\Gamma_1$ and $\nabla_{\rm ad}$ over a grid in $\beta$ |
| Evenings | Derivations; exercises |

## Derive from scratch (derivation nights)

1. The adiabat of an ideal gas with $f$ degrees of freedom from $dS=0$ and the sound speed from $\kappa_S$.
2. $\Gamma_1=\chi_\rho+\frac{P}{\rho Tc_V}\chi_T^2$ using $(\partial P/\partial\rho)_S$ and the Maxwell relations.
3. $\nabla_{\rm ad}=\frac{P\delta}{\rho Tc_P}$ from the entropy $S(T,P)$.
4. $c_V$, $c_P$ and the adiabatic coefficients of an ideal gas plus radiation as functions of $\beta$.
5. The relation $\frac{\Gamma_1}{\Gamma_3-1}=\frac{\Gamma_2}{\Gamma_2-1}$.

## Bare-minimum exercises (find matching problems with keywords: adiabatic, ratio of specific heats, speed of sound, radiation pressure)

1. **Ideal gas adiabats:** derive $PV^\gamma=$ const; compute the temperature after adiabatic compression by a factor of 8 for $\gamma=5/3$ (factor 4).
2. **Sound speed in the Sun:** at the solar centre ($P=2.3\times10^{17}$, $\rho=150$) compute $c_s=\sqrt{\Gamma_1P/\rho}\approx5\times10^7$ cm/s ($\approx500$ km/s; verify).
3. **Adiabatic exponents of radiation:** show $\Gamma_1=\Gamma_2=\Gamma_3=4/3$ and $\nabla_{\rm ad}=1/4$ from $P=aT^4/3$ and $s\propto T^3/\rho$.
4. **Gas plus radiation:** derive $c_V$ and $\Gamma_3-1=\frac{(4-3\beta)(\gamma-1)}{\beta+12(\gamma-1)(1-\beta)}$ and verify the limits; then obtain $\Gamma_1$ and $\nabla_{\rm ad}$.
5. **Table of $\nabla_{\rm ad}$:** compute $\nabla_{\rm ad}$ for $\beta=1,0.9,0.7,0.5,0.3,0.1,0$ using the formula; the values go from $0.4$ to $0.25$ monotonically.
6. **Eddington limit of stability:** show that $\Gamma_1<4/3$ would make a uniform sphere dynamically unstable; use your gas-plus-radiation $\Gamma_1(\beta)$ and note that $\Gamma_1>4/3$ for all $\beta>0$ in the pure gas-plus-radiation case (marginal only at $\beta\to0$).
7. **Partially ionized hydrogen (qualitative):** argue that the latent energy of ionization reduces $\Gamma_1$ and $\nabla_{\rm ad}$ in the ionization zone, with values as low as $\nabla_{\rm ad}\approx0.1$ (compute in Module 05).
8. **Polytrope link:** an adiabatic ideal gas satisfies $P\propto\rho^{5/3}$; relate the polytropic index $n=1/(\gamma-1)$ to $\Gamma_1$ and say which $n$ describes radiation-dominated gas ($n=3$) and non-relativistic degenerate gas ($n=3/2$).
9. **Adiabatic expansion of radiation:** show $T\propto V^{-1/3}$ and verify that the photon number and the entropy are conserved.
10. **Entropy conservation in convection:** a convective bubble rising adiabatically from pressure $P_1$ to $P_2$ has $T_2=T_1(P_2/P_1)^{\nabla_{\rm ad}}$; compute the temperature drop for a pressure drop by a factor of 2 in an ideal monatomic gas ($0.4$ power: $T_2/T_1=0.758$).

## Optional extension

Show, by a numerical scan in $\beta$ from 0 to 1, that $\nabla_{\rm ad}(\beta)$ rises monotonically from $0.25$ to $0.4$ and that $\Gamma_1(\beta)$ rises monotonically from $4/3$ to $5/3$. Then prove the monotonicity analytically for $\nabla_{\rm ad}$ by differentiating $\frac{2(4-3\beta)}{32-24\beta-3\beta^2}$.

## Pitfalls

- Using $\gamma=C_P/C_V$ for a mixture or a partially ionized gas where $\Gamma_1\ne\gamma$.
- Treating $\Gamma_1$, $\Gamma_2$, $\Gamma_3$ as equal outside the ideal limits.
- Mixing isothermal and adiabatic sound speeds.
- Ignoring that radiation pressure lowers $\Gamma_1$ only through its coupling to the gas energy.

## Gate questions

1. Why do $\Gamma_1$, $\Gamma_2$, $\Gamma_3$ differ in a non-ideal gas but not for an ideal monatomic gas?
2. Why does radiation soften the equation of state?
3. Why is $\nabla_{\rm ad}$ the relevant quantity for convection, and how does it enter the Schwarzschild criterion?

## One-page cheat sheet contents

Definitions of $\Gamma_{1,2,3}$ and $\nabla_{\rm ad}$ with identities; gas-plus-radiation formulas as functions of $\beta$; sound speed.
