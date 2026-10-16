# Module 06: Chapter 3a, the Klein-Gordon equation and the classical scalar field (★★, Weeks 7 and 8; Protocol A)

**Books:** Klauber Ch. 3 (first part); second source: Lancaster and Blundell on the scalar field, Tong's scalar-field lecture.
**Time:** 2 weeks (of the five weeks for Chapter 3).

## Why this is the hard chapter

Chapter 3 is the **analysis peak of Part One**. Chapter 4 *feels* harder (gamma matrices, index gymnastics, spin sums) but that difficulty is algebraic and repetitive. Chapter 3's difficulty is analytic and every move is being made for the first time: the invariant measure, continuum normalisation and delta functions, inverting a Fourier expansion, contour integration in the propagator. Chapters 4 and 5 re-run the same moves with more indices attached. So this is the right chapter to overspend on: time here compounds; time on spinor algebra does not. The difficulty is also **structurally invisible on a first pass**, because Klauber writes out every step: you can follow all of it and still own none of it.

### The eight calculations (the stopping condition for "understand the math")

If you can do all eight closed-book, you own the chapter. Ordered by dependency: **1** Lorentz invariance of the measure; **2** inverting the mode expansion; **3** ladder commutators *from* field commutators; **4** the Hamiltonian including the zero-point term; **5** the vacuum two-point function; **6** the propagator as a time-ordered vacuum expectation value (★★); **7** micro-causality; **8** box and continuum normalisation, both ways.

| Week | Calculations |
| --- | --- |
| 7: the KG equation | (none: the negative-probability analysis) |
| 8: the classical field | **1, 2, 8** |
| 9: quantisation | 3, 4 |
| 10: the propagator | 5, **6** |
| 11: consolidation | 7, plus all eight closed-book |

## Diagnostic (40 minutes, no notes)

1. Show the KG conserved density $\rho=i(\phi^*\dot\phi-\phi\dot\phi^*)$ is not positive-definite.
2. Show that $\frac{d^3k}{(2\pi)^32\omega_{\mathbf k}}$ is Lorentz invariant (Module 04).
3. Given $\phi$ and $\pi=\dot\phi$ at one time solve for $a(\mathbf k)$.
4. Write the classical Hamiltonian of the free scalar field in terms of $a(\mathbf k)$.
5. State what happens to KG in the non-relativistic limit.

## Prerequisites

Modules 02 to 05.

## Detailed topics (checklist)

**Week 7: the KG equation itself [Must]**
- Origin: $E^2=p^2+m^2$ with $E\to i\partial_t$, $\mathbf p\to-i\nabla$ gives $(\Box+m^2)\phi=0$. Free-particle solutions $e^{-i(Et-\mathbf p\cdot\mathbf x)}$ with $E=\pm\sqrt{p^2+m^2}$; the conserved current $j^\mu=i(\phi^*\partial^\mu\phi-\phi\partial^\mu\phi^*)$ and density $\rho=2E|\phi|^2$ for a plane wave: **negative for $E<0$**. *Work out the negative-probability problem explicitly; do not accept the summary.* It is the reason the field interpretation exists. **Concretise:** solve KG for a free particle in a box; compare with the Schrodinger case; see precisely what fails.

**Week 8: the classical scalar field [Must]**
- Lagrangian density, Euler-Lagrange, canonical momentum, Hamiltonian density; real field expansion
$$\phi(\mathbf x,t)=\int\frac{d^3k}{\sqrt{(2\pi)^32\omega_{\mathbf k}}}\left[a(\mathbf k)e^{-ik\cdot x}+a^*(\mathbf k)e^{ik\cdot x}\right],\quad\omega_{\mathbf k}=\sqrt{k^2+m^2}.$$
- **The normalisation of the expansion coefficients and the measure**: this is where Module 04 pays off, and where the first pass most likely went on autopilot. Inversion: $a(\mathbf k)=\frac{e^{i\omega t}}{\sqrt{2\omega(2\pi)^3}}\int d^3x\,e^{-i\mathbf k\cdot\mathbf x}\left[\omega\phi+i\pi\right]$. **Concretise:** compute the energy of a single classical mode and check it against the oscillator result (Module 02). Classical $H=\int d^3k\,\omega_{\mathbf k}|a(\mathbf k)|^2$.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | **Do calculation 1 before reading the chapter**; the KG equation and its current |
| B1 | Exercises 1 to 3 |
| A2 | The classical scalar field in Klauber; derive the expansion |
| B2 | Exercises 4 to 6 |
| A3 | Calculation 2 (the inversion); calculation 8 (box versus continuum) |
| B3 | Exercises 7 to 10 |

## Derive from scratch

1. Calculation 1: the invariant measure.
2. The KG current and its density.
3. Calculation 2: inverting the mode expansion.
4. Calculation 8: the box versus continuum dictionary.
5. $H=\int d^3k\,\omega|a|^2$ from $\mathcal H$.

## Exercises

1. **[T] KG density:** for $\phi=Ne^{-iEt+i\mathbf p\cdot\mathbf x}$, $\rho=2E|N|^2$, which is negative for $E=-\sqrt{p^2+m^2}$.
2. **[T] KG in a box:** with periodic boundary conditions the allowed modes are $e^{i\mathbf k\cdot\mathbf x}$, $k_i=\frac{2\pi n_i}{L}$, and $E=\pm\sqrt{k^2+m^2}$ doubles the spectrum relative to Schrodinger; write $\phi=e^{-imt}\psi$ and show $i\dot\psi=-\frac{\nabla^2}{2m}\psi$ in the non-relativistic limit.
3. **[T] Calculation 1:** $\int d^4k\,\delta(k^2-m^2)\theta(k^0)=\int\frac{d^3k}{2E}$ invariant, so $\frac{d^3k}{(2\pi)^32\omega}$ is invariant.
4. **[T] Calculation 2:** $\tilde\phi(\mathbf k,t)=\sqrt{\frac{(2\pi)^3}{2\omega}}\left[a(\mathbf k)e^{-i\omega t}+a^*(-\mathbf k)e^{i\omega t}\right]$, $\tilde\pi=-i\omega\sqrt{\frac{(2\pi)^3}{2\omega}}\left[a(\mathbf k)e^{-i\omega t}-a^*(-\mathbf k)e^{i\omega t}\right]$; combine $\omega\tilde\phi+i\tilde\pi=\sqrt{2\omega(2\pi)^3}\,a(\mathbf k)e^{-i\omega t}$.
5. **[T] Classical Hamiltonian:** substitute the expansion into $H=\int d^3x\,\frac12(\pi^2+(\nabla\phi)^2+m^2\phi^2)$ and use $\int d^3x\,e^{i(\mathbf k-\mathbf k')\cdot\mathbf x}=(2\pi)^3\delta^3(\mathbf k-\mathbf k')$ to get $H=\int d^3k\,\omega_{\mathbf k}\,a^*(\mathbf k)a(\mathbf k)$ (the $aa$ terms cancel).
6. **[T] Single mode:** a mode with $a=a_0\delta^3(\mathbf k-\mathbf k_0)$-type has energy $\omega|a|^2$ (discrete box: $\omega\,|a_{\mathbf k}|^2$), matching $E=\frac12\omega^2A^2V$ of Module 02 with $A^2V=\frac{2|a|^2}{\omega}$.
7. **[T] Calculation 8 (the dictionary):** box: $\phi=\sum_{\mathbf k}\frac{1}{\sqrt{2\omega V}}\left(a_{\mathbf k}e^{-ik\cdot x}+{\rm h.c.}\right)$ with $[a_{\mathbf k},a^\dagger_{\mathbf k'}]=\delta_{\mathbf k\mathbf k'}$; continuum $a(\mathbf k)=\sqrt{\frac{V}{(2\pi)^3}}a_{\mathbf k}$ with $[a(\mathbf k),a^\dagger(\mathbf k')]=\delta^3(\mathbf k-\mathbf k')$; verify using $\sum_{\mathbf k}\to V\int\frac{d^3k}{(2\pi)^3}$.
8. **[C] Field versus wave function:** why is reinterpreting $\psi$ as a field rather than a wave function a *solution* rather than a relabelling? What does it buy?
9. **[C] Infinitely many oscillators:** in what sense is a classical field with infinitely many modes "the same as" infinitely many oscillators, and where does the analogy stop?
10. **[C] Explain-it paragraph:** why quantised fields were needed after the KG equation failed as a wave equation.

## Optional extension

Write the complex scalar field expansion with two independent coefficient functions $a$ and $b$ and compute its conserved charge $Q=i\int d^3x(\phi^\dagger\dot\phi-\dot\phi^\dagger\phi)$; identify $b$ with the antiparticle (preview of Module 12).

## Pitfalls

- Treating the KG equation as a one-particle Schrodinger equation.
- Dropping the $\frac{1}{\sqrt{2\omega}}$ in the expansion (all downstream factors then fail).
- Mixing $a^*(\mathbf k)$ and $a^*(-\mathbf k)$ in the inversion.

## Gate questions

1. Why is the KG density not a probability density?
2. Why does the measure carry $\frac{1}{2\omega}$?
3. How does the classical $H$ in terms of $a$ resemble the oscillator?

## One-page cheat sheet contents

KG equation and current; real-field expansion; the inversion formula; $H=\int\omega|a|^2$; the box/continuum dictionary.
