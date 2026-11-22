# Module 02, Session 3: Fourier transforms and index notation, exercises

Self-check for Session 3. Books, notes and your cheat sheet are all fair game, and there is no clock.

**Read first:** Riley §13.1 (pp. 433 to 453) and Riley §26.1, §26.3, §26.8 (pp. 928 to 944). The study file is `02_math_patch_deltas_contours_fourier.md`.

**Notation:** $`\tilde f(k)=\int f(x)e^{-ikx}\,dx`$ and $`f(x)=\int\frac{dk}{2\pi}\tilde f(k)e^{ikx}`$. In three dimensions $`\tilde f(\mathbf k)=\int f(\mathbf x)e^{-i\mathbf k\cdot\mathbf x}\,d^3x`$. Repeated indices are summed; $`(\nabla\times\mathbf A)_i=\epsilon_{ijk}\partial_jA_k`$.

**Exercises 6 to 8 are not here on purpose.** They moved to the complex analysis guide (CA08 and CA09), and the numbers are kept so that references to exercises 9 and 10 elsewhere in the guide stay valid.

## Book problems

Riley exercises: odd numbers have worked solutions in the Student Solution Manual. The exercises are on pp. 460 to 462 (Chapter 13) and pp. 977 to 980 (Chapter 26); Chapter 12 exercises are at the end of that chapter.

| Tier | Problem | What it asks |
| --- | --- | --- |
| Must | Riley 13.1 | Fourier transform of $`e^{-\lvert t\rvert}`$ |
| Must | Riley 13.5 | transform the equation $`\phi''-K^2\phi=f(x)`$: the screened-Poisson pattern |
| Must | Riley 26.1 | Cartesian-tensor definition: basic properties |
| Must | Riley 26.6 | vector identities by tensor methods (even number: no worked solution) |
| Should | Riley 13.3 | Fourier transform of $`H(x-a)e^{-bx}`$ |
| Should | Riley 13.7 | Fourier transform of the unit rectangular distribution |
| Should | Riley 12.5 | Fourier series of $`f(x)=x`$ |
| Should | Riley 26.5 | the quotient law |
| Could | Riley 12.1 | orthogonality relations of Fourier series |
| Could | Riley 26.9 | determinant identity with $`\epsilon_{ijk}`$ |

## Module exercises

### Exercise 5: Fourier transform of a Gaussian

**Where to read:** Riley §13.1.

**Statement.** For $`a>0`$ show that $`\int_{-\infty}^{\infty}e^{-ax^2}e^{-ikx}\,dx=\sqrt{\frac\pi a}\,e^{-k^2/4a}`$. Then state the convolution theorem in your convention and say what the result tells you about the width of $`f`$ versus the width of $`\tilde f`$.

**Hint.** Two routes. (i) Complete the square in the exponent and shift the integration variable; you only need $`\int e^{-ax^2}dx=\sqrt{\pi/a}`$. (ii) Differentiate under the integral sign: $`\tilde f'(k)=-\frac{k}{2a}\tilde f(k)`$ (integrate by parts), with $`\tilde f(0)=\sqrt{\pi/a}`$. Route (ii) needs no complex shift.

**Expected result.** $`\sqrt{\frac\pi a}\,e^{-k^2/4a}`$. A narrow Gaussian in $`x`$ is a wide one in $`k`$: the product of the widths is fixed.

### Exercise 9: Yukawa and Coulomb transforms

**Where to read:** Riley §13.1 (Fourier transforms in higher dimensions).

**Statement.** Show that
$`\int d^3x\,e^{-i\mathbf k\cdot\mathbf x}\,\frac{e^{-\mu r}}{r}=\frac{4\pi}{k^2+\mu^2}`$,
then take $`\mu\to0`$ to obtain the Coulomb transform $`\frac{4\pi}{k^2}`$.

**Hint.**

- Take $`\mathbf k`$ along the polar axis. The angular integral is $`\int d\Omega\,e^{-i\mathbf k\cdot\mathbf x}=\frac{4\pi\sin kr}{kr}`$.
- That leaves $`\frac{4\pi}{k}\int_0^\infty e^{-\mu r}\sin kr\,dr`$, and $`\int_0^\infty\sin kr\,e^{-\mu r}dr=\frac{k}{k^2+\mu^2}`$ (write $`\sin kr`$ as the imaginary part of $`e^{ikr}`$).
- Check the link with exercise 3: $`-\nabla^2`$ acts as $`k^2`$ on the transform side, so $`\nabla^2\frac1r=-4\pi\delta^3`$ reads $`-k^2\cdot\frac{4\pi}{k^2}=-4\pi`$.

**Expected result.** $`\frac{4\pi}{k^2+\mu^2}`$, and in the limit $`\frac{4\pi}{k^2}`$.

### Exercise 10: index notation

**Where to read:** Riley §26.1, §26.3, §26.8.

**Statement.** Using $`\epsilon_{ijk}`$ and $`\delta_{ij}`$, prove:

- (a) $`\nabla\cdot(\mathbf A\times\mathbf B)=\mathbf B\cdot(\nabla\times\mathbf A)-\mathbf A\cdot(\nabla\times\mathbf B)`$
- (b) $`\nabla\times(\nabla\times\mathbf A)=\nabla(\nabla\cdot\mathbf A)-\nabla^2\mathbf A`$

**Hint.**

- (a) Write $`\partial_i(\epsilon_{ijk}A_jB_k)`$ and use the product rule. The two terms are $`B_k\epsilon_{kij}\partial_iA_j`$ and $`-A_j\epsilon_{jik}\partial_iB_k`$ after cyclic relabelling; recognise each as a curl.
- (b) Write the $`i`$-th component as $`\epsilon_{ijk}\partial_j\epsilon_{klm}\partial_lA_m`$, move to $`\epsilon_{kij}\epsilon_{klm}`$ and use $`\epsilon_{kij}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}`$.

**Expected results.** The two identities as stated. In (b) the surviving terms are $`\partial_i\partial_jA_j`$ and $`\partial_j\partial_jA_i`$.

## Optional extension

Derive the Green function of $`-\frac{d^2}{dx^2}+m^2`$ on the line by Fourier transform, $`G(x)=\frac{1}{2m}e^{-m\lvert x\rvert}`$, and check it directly:

- $`G`$ is continuous.
- $`-G''+m^2G=0`$ away from the origin.
- $`G'`$ jumps by $`-1`$ at $`x=0`$.

The contour evaluation of the inverse transform is CA08 exercise 2.

## Done when

- the Gaussian transform and the Yukawa transform are done
- both index-notation identities are proved with $`\epsilon_{ijk}`$
- you can write the ($`\mathbf k`$-space) meaning of $`\nabla^2`$ and use it to read off exercise 9 from exercise 3

## Progress

- [ ] Riley 13.1
- [ ] Riley 13.5
- [ ] Riley 26.1
- [ ] Riley 26.6
- [ ] Exercise 5
- [ ] Exercise 9
- [ ] Exercise 10
- [ ] Riley 13.3, 13.7, 12.5, 26.5 (Should)
- [ ] Optional extension
