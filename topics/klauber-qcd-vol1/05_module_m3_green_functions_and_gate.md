# Module 05: Module M3, Green functions (★, Week 6; Protocol A), and the Module M gate

**Books:** Byron and Fuller or Boas for Green functions; Barton, *Elements of Green's Functions and Propagation*; second source for the KG case: Tong's scalar-field lecture. If you ran the electrodynamics guide, its Modules 05 and 11 cover the same ground.
**Time:** 1 week (a proper block), ending with the Module M gate.

## Why this matters

The Green function of a linear differential operator is its inverse: $\mathcal DG=\delta$. **Boundary conditions select a unique $G$**: this is the whole idea, and it is the same idea as the contour choice of Module 03, seen from the other side. Construction by Fourier transform; the wave-equation Green function; retarded and advanced forms; the light-cone structure.

**The module deliverable.** Solve $(\Box+m^2)G(x-x')=-\delta^4(x-x')$ by Fourier transform. You will find $\tilde G(k)\propto\frac{1}{k^2-m^2}$ **with poles on the real axis, exactly the integral you did in Module 03.** Choose the Feynman contour and complete the transform. You have just built the Klein-Gordon propagator, three weeks before Klauber does, from tools you own; when he derives it in Chapter 3 it will be a recognition rather than an introduction.

## Diagnostic (40 minutes, no notes)

1. Construct the Green function of $-\frac{d^2}{dx^2}+m^2$ on the line by Fourier transform.
2. Construct the retarded Green function of $\frac{d^2}{dt^2}+\omega^2$.
3. Write the Fourier representation of the Green function of $(\Box+m^2)$ and name the three contours.
4. State the correspondence "boundary condition $\leftrightarrow$ contour choice" for retarded, advanced and Feynman.
5. State the light-cone support of the massless retarded Green function.

## Prerequisites

Modules 03 and 04.

## Detailed topics (checklist)

- $\mathcal DG(x,x')=\delta(x-x')$; uniqueness by boundary conditions; superposition $\psi=\int G\,f$; construction by Fourier transform; the oscillator, Helmholtz and wave-equation examples.
- The Klein-Gordon operator with $\Box=\partial_t^2-\nabla^2$: $(\Box+m^2)e^{-ik\cdot x}=(m^2-k^2)e^{-ik\cdot x}$, so $(\Box+m^2)G=-\delta^4$ gives $\tilde G(k)=\frac{1}{k^2-m^2}$; the poles at $k^0=\pm E_{\mathbf k}$; **retarded** (poles below the axis; $G=0$ for $t<0$), **advanced** (poles above; $G=0$ for $t>0$), **Feynman** ($k^2-m^2+i\epsilon$: the positive-energy pole below, the negative-energy pole above).
- The massless retarded Green function of $\Box G=\delta^4$: $G_{\rm ret}=\frac{\delta(t-r)}{4\pi r}$ (support on the future light cone).

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Green functions as inverses; the 1D and oscillator examples |
| B1 | Exercises 1 and 2 |
| A2 | The Fourier construction for $\Box+m^2$ |
| B2 | Exercises 3 to 5 |
| A3 | The dictionary; the light cone |
| B3 | Exercises 6 to 10; the Module M gate |

## Derive from scratch

1. $G=\frac{e^{-m|x|}}{2m}$ for $-\partial_x^2+m^2$.
2. $G_{\rm ret}=\theta(t)\frac{\sin\omega t}{\omega}$ for $\partial_t^2+\omega^2$.
3. $\tilde G=\frac1{k^2-m^2}$ and the $k^0$ integral for each contour.
4. The dictionary of boundary conditions and contours.
5. The relation $\langle T\phi\phi\rangle=iG_F$ (preview).

## Exercises

1. **[T] 1D screened Green function:** $\left(-\frac{d^2}{dx^2}+m^2\right)G=\delta(x)$ has $G=\frac{e^{-m|x|}}{2m}$ (from $\int\frac{dk}{2\pi}\frac{e^{ikx}}{k^2+m^2}$ and Module 03 exercise 1).
2. **[T] Oscillator:** $\left(\frac{d^2}{dt^2}+\omega^2\right)G=\delta(t)$ with $G=0$ for $t<0$: $G_{\rm ret}=\theta(t)\frac{\sin\omega t}{\omega}$; advanced $G_{\rm adv}=-\theta(-t)\frac{\sin\omega t}\omega$; relate to Module 03 exercise 5 by $G=-\frac{I}{2\pi}$.
3. **[T] KG propagator (the deliverable):** $G(x)=\int\frac{d^4k}{(2\pi)^4}\frac{e^{-ik\cdot x}}{k^2-m^2}$; do the $k^0$ integral for $t>0$ and $t<0$ for each contour. Feynman ($+i\epsilon$): $G_F(x)=\int\frac{d^3k}{(2\pi)^3}\frac{-i}{2E_{\mathbf k}}e^{i\mathbf k\cdot\mathbf x}e^{-iE_{\mathbf k}|t|}$; retarded: $G_{\rm ret}=-\theta(t)\int\frac{d^3k}{(2\pi)^3}\frac{\sin(E_{\mathbf k}t)}{E_{\mathbf k}}e^{i\mathbf k\cdot\mathbf x}$ (the overall sign is that of $(\Box+m^2)G=-\delta^4$; check it by applying $\partial_t^2+E^2$ to the $t$-dependence).
4. **[T] Relation to the vacuum expectation value:** $D_F\equiv iG_F=\int\frac{d^4k}{(2\pi)^4}\frac{i\,e^{-ik\cdot x}}{k^2-m^2+i\epsilon}$ and $(\Box+m^2)D_F=-i\delta^4$; this is the object that equals $\langle0|T\phi(x)\phi(0)|0\rangle$ (Module 08).
5. **[T] Massless retarded Green function:** $\Box G=\delta^4$ gives $G_{\rm ret}=\frac{\delta(t-r)}{4\pi r}$; check by integrating the source $\delta^3(\mathbf x)$ over time to get the Coulomb potential $\frac1{4\pi r}$.
6. **[T] Helmholtz:** $(\nabla^2+k^2)G=-\delta^3$: $G=\frac{e^{\pm ikr}}{4\pi r}$; which sign is retarded?
7. **[C] The dictionary:** state precisely the correspondence between boundary conditions and contour choices; they are the same statement in two languages; write the dictionary.
8. **[C] Uniqueness:** why does a linear operator with no boundary conditions have no unique inverse, and what does that say about $G_{\rm ret}$ versus $G_{\rm adv}$?
9. **[C] Physical meaning:** what does each of the three Green functions mean physically for a source switched on at $t=0$?
10. **[T] One simpler operator for contrast:** the Green function of the Helmholtz or 1D oscillator problem, compared with the KG case: list what changes (dimension, poles, support).

## ▣ Module M gate (end of Week 6, about 90 minutes, closed book)

1. State and prove the residue theorem's use in evaluating a real integral by closing a contour; justify Jordan's lemma's role.
2. Evaluate $\int\frac{e^{-ik^0t}}{(k^0)^2-\omega^2\pm i\epsilon}dk^0$ for all three prescriptions and describe each resulting function.
3. Derive $\delta(f(x))=\sum\frac{\delta(x-x_i)}{|f'(x_i)|}$ and use it to get the invariant measure.
4. Construct the Green function for $(\Box+m^2)$ from scratch, contour and all.
5. State the boundary-condition $\leftrightarrow$ contour dictionary.

**If this gate is comfortable, the rest of Part One is a different experience than it was the first time.** That is the whole bet of this module.

## Optional extension

Construct the retarded KG Green function in position space and show it has support inside as well as on the light cone for $m>0$ (the tail).

## Pitfalls

- Using $\Box=\partial_t^2-\nabla^2$ and $\Box=\nabla^2-\partial_t^2$ interchangeably (sign flips).
- Forgetting the $i$ in $D_F=iG_F$.
- Treating the pole positions as a computational convenience instead of a boundary condition.

## Gate questions

1. Why is $G_F$ not zero for $t<0$?
2. Which contour gives time ordering and why?
3. Why does the massive retarded $G$ have support off the light cone?

## One-page cheat sheet contents

$\mathcal DG=\delta$; $\tilde G=\frac1{k^2-m^2}$; three contour results; the dictionary; $D_F=iG_F$.
