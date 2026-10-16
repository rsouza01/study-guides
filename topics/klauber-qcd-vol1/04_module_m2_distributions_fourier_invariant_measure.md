# Module 04: Module M2, Distributions, Fourier transforms and the invariant measure (★, Week 5; Protocol A)

**Books:** Boas (Fourier transforms; the delta function), Byron and Fuller; **Klauber's free *Dirac delta function forms* PDF** (it matches his conventions exactly).
**Time:** 1 week (a proper block).

## Why this matters

The Dirac delta as a distribution rather than a function. The composition rule $\delta(f(x))=\sum_i\frac{\delta(x-x_i)}{|f'(x_i)|}$. Deltas in curvilinear coordinates; $\delta^3$ and $\delta^4$. Fourier transforms in one and four dimensions, and, with real care, **the $2\pi$ bookkeeping**, since convention mismatches are a silent killer on a re-read.

**Then the identity that matters most:**
$$\int d^4k\,\delta(k^2-m^2)\,\theta(k^0)\,f(k)=\int\frac{d^3k}{2E_{\mathbf k}}f(k)\Big|_{k^0=E_{\mathbf k}}.$$
Derive it using the composition rule. **This is where the relativistic normalisation of states comes from**, it is used constantly from Chapter 3 onward, and almost no text derives it in the open. If the factors of $2E_k$ in field expansions have ever felt arbitrary, this is why.

## Diagnostic (40 minutes, no notes)

1. Derive $\delta(f(x))=\sum_i\frac{\delta(x-x_i)}{|f'(x_i)|}$ and evaluate $\delta(x^2-a^2)$.
2. Write $\delta^3(\mathbf x-\mathbf x')$ in spherical coordinates.
3. Derive the invariant-measure identity above.
4. State the Fourier convention you will use for the whole guide and the resulting $2\pi$ factors for $\delta(x)$ and $\delta^3(\mathbf x)$.
5. Transform the Gaussian and the step function.

## Prerequisites

Module 03 (residues, Sokhotski).

## Detailed topics (checklist)

- Distributions: $\delta$ defined by $\int f\delta=f(0)$; composition rule; derivatives of $\delta$; $\theta(x)$ and $\theta'=\delta$; curvilinear $\delta^3$, $\delta^4$.
- Fourier transforms in 1D and 4D: $\tilde f(k)=\int dx\,f(x)e^{-ikx}$, $f(x)=\int\frac{dk}{2\pi}\tilde f(k)e^{ikx}$; $\int dx\,e^{ikx}=2\pi\delta(k)$; four-dimensional $\int d^4x\,e^{ik\cdot x}=(2\pi)^4\delta^4(k)$; Parseval; the transform of the step function $\tilde\theta(k)=\pi\delta(k)-iP\frac1k$.
- **The invariant measure:** $\delta(k_0^2-E^2)=\frac{\delta(k_0-E)+\delta(k_0+E)}{2E}$; the $\theta(k^0)$ picks the positive branch; hence $\frac{d^3k}{2E_{\mathbf k}}$ is Lorentz invariant.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Delta calculus; the composition rule |
| B1 | Exercises 1 to 3 |
| A2 | Fourier transforms; the $2\pi$ conventions |
| B2 | Exercises 4 and 5 |
| A3 | The invariant measure |
| B3 | Exercises 6 to 10 |

## Derive from scratch

1. The composition rule.
2. The spherical-coordinate form of $\delta^3$.
3. $\int dx\,e^{ikx}=2\pi\delta(k)$ (as a limit).
4. The invariant-measure identity.
5. The Lorentz invariance of $\frac{d^3k}{2E}$ by a boost Jacobian.

## Exercises

1. **[T] Composition:** $\delta(x^2-a^2)=\frac{\delta(x-a)+\delta(x+a)}{2|a|}$; $\int_0^{2\pi}f(x)\delta(\cos x)dx=f(\tfrac\pi2)+f(\tfrac{3\pi}2)$.
2. **[T] Spherical $\delta^3$:** $\delta^3(\mathbf x-\mathbf x')=\frac{\delta(r-r')\delta(\cos\theta-\cos\theta')\delta(\phi-\phi')}{r^2}$; check $\int\delta^3d^3x=1$.
3. **[T] Delta of a quadratic:** $\int dx\,g(x)\delta(x^2+x-2)=\frac{g(1)}{3}+\frac{g(-2)}{3}$ (zeros at $1$ and $-2$, $|f'|=3$ at both).
4. **[T] Fourier of a Gaussian:** $\int e^{-ax^2}e^{-ikx}dx=\sqrt{\frac\pi a}e^{-k^2/4a}$; check Parseval.
5. **[T] Step function:** $\tilde\theta(k)=\int_0^\infty e^{-ikx}dx=\pi\delta(k)-iP\frac1k=\frac{-i}{k-i\epsilon}$.
6. **[T] Invariant measure (derivation):** $\int d^4k\,\delta(k^2-m^2)\theta(k^0)f(k)=\int d^3k\int dk^0\frac{\delta(k^0-E)}{2E}f=\int\frac{d^3k}{2E}f(E,\mathbf k)$.
7. **[T] Numerical check:** with $f=e^{-k^0}$ and $m=1$: $\int\frac{d^3k}{2E}e^{-E}=2\pi\int_0^\infty\frac{k^2e^{-E}}{E}dk=2\pi K_1(1)=3.782$ (verify numerically).
8. **[T] Boost Jacobian:** under a boost along $z$ ($k_z'=\gamma(k_z+\beta E)$, $E'=\gamma(E+\beta k_z)$) show $\frac{dk_z'}{dk_z}=\frac{E'}{E}$, so $\frac{dk_z}{E}$ is invariant.
9. **[T] Box versus continuum (card):** $\sum_{\mathbf k}\leftrightarrow V\int\frac{d^3k}{(2\pi)^3}$ and $\delta_{\mathbf k\mathbf k'}\leftrightarrow\frac{(2\pi)^3}{V}\delta^3(\mathbf k-\mathbf k')$; write the dictionary card you will use from Module 07 on.
10. **[C] Not a function:** in what sense is $\delta(x)$ not a function, and why does physics get away with treating it as one? What would break if you insisted on rigour?

## Optional extension

Show that $\int\frac{d^3k}{(2\pi)^32E}e^{-ik\cdot x}$ at equal times and spacelike separation $r$ equals $\frac{m}{4\pi^2r}K_1(mr)$ (needed in Module 08).

## Pitfalls

- Missing the $|f'|$ in the composition rule.
- Mixing $2\pi$ conventions between Fourier pairs and delta functions.
- Forgetting the $\theta(k^0)$ in the invariant-measure identity.

## Gate questions

1. Where does the factor $2E$ come from?
2. Why is $\frac{d^3k}{2E}$ Lorentz invariant but $d^3k$ not?
3. What is the dictionary between box and continuum normalisation?

## One-page cheat sheet contents

Composition rule; $\delta^3$ in spherical coordinates; Fourier conventions and $2\pi$ factors; the invariant-measure identity; the box/continuum dictionary.
