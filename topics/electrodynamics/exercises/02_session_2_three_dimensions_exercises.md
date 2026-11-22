# Module 02, Session 2: three dimensions and point charges, exercises

Self-check for Session 2. Books, notes and your cheat sheet are all fair game, and there is no clock.

**Read first:** Jackson §1.2 (p. 24), and Griffiths §1.5.1 and §1.5.3 again. The study file is `02_math_patch_deltas_contours_fourier.md`.

**Notation:** $`\mathbf r`$ is the position vector, $`r=\lvert\mathbf r\rvert`$, $`\hat r=\mathbf r/r`$. $`\delta^3(\mathbf r)`$ is the three-dimensional delta. $`V`$ is any volume and $`dV`$ its volume element.

## Book problems

| Tier | Problem | What it asks |
| --- | --- | --- |
| Must | Jackson 1.3 (p. 51) | charge distributions written with delta functions (shell, cylinder, disc); statement in the book |
| Should | Griffiths 1.48 | 3D delta-function integrals |
| Should | Griffiths 1.64 | check that $`\nabla^2\frac1r=-4\pi\delta^3`$ another way |
| Could | Griffiths 1.49 | integral of $`e^{-r}`$ times the divergence of $`\hat r/r^2`$, by two methods |
| Could | Jackson 1.2 (p. 51) | delta function in general orthogonal coordinates, as a limit of a Gaussian |

## Module exercises

### Exercise 3: the Laplacian of $`1/r`$

**Where to read:** Griffiths §1.5.1 and §1.5.3; Jackson §1.2.

**Statement.** Show that $`\nabla^2\frac1r=-4\pi\,\delta^3(\mathbf r)`$.

Work through these steps and write each one down:

1. For $`r\neq0`$, show that $`\mathbf F=\nabla\frac1r=-\frac{\hat r}{r^2}`$, so that $`\nabla\cdot\mathbf F=\nabla^2\frac1r`$.
2. Compute the flux of $`\mathbf F`$ through a sphere of radius $`R`$ centred at the origin. Show that it is $`-4\pi`$ for every $`R`$.
3. Show that $`\nabla\cdot\mathbf F=0`$ for $`r\neq0`$.
4. Let $`V`$ be any volume. Show that $`\int_V\nabla\cdot\mathbf F\,dV`$ equals $`-4\pi`$ if the origin lies inside $`V`$ and $`0`$ if it lies outside.
5. Compute $`\int_V(-4\pi\,\delta^3(\mathbf r))\,dV`$ for the same two cases.
6. Conclude.

**Hint.**

- In step 2, $`r^2`$ from the area cancels $`1/r^2`$ from the field.
- In step 4, the divergence theorem cannot be applied directly when the origin is inside, because $`\mathbf F`$ is singular there. Surround the origin with a small sphere, apply the theorem in the region between that sphere and the boundary of $`V`$ (where $`\nabla\cdot\mathbf F=0`$), and compare the two fluxes.
- Step 6: the two integrals agree for every $`V`$, so the integrands agree as distributions. The delta is a statement about integrands; it is never an equation between an integral and $`\delta`$.

**Expected result.** Both integrals in steps 4 and 5 are $`-4\pi`$ (origin inside) or $`0`$ (origin outside), hence $`\nabla\cdot\left(\nabla\frac1r\right)=-4\pi\,\delta^3(\mathbf r)`$.

### Exercise 4: point and moving charges

**Where to read:** Jackson §1.2; Griffiths 1.47 for the static case.

**Statement.** A point charge $`q`$ moves on a given trajectory $`\mathbf r(t)`$ with velocity $`\mathbf v=\dot{\mathbf r}`$.

- (a) Write its charge density $`\rho(\mathbf x,t)`$ and current density $`\mathbf J(\mathbf x,t)`$ with delta functions.
- (b) Show that $`\partial_t\rho+\nabla\cdot\mathbf J=0`$.

**Hint.** Differentiate $`\delta^3(\mathbf x-\mathbf r(t))`$ with respect to $`t`$ by the chain rule: $`\mathbf x`$ is fixed and only $`\mathbf r(t)`$ moves, so each component brings down $`-\dot r_i`$ times a derivative of the delta with respect to its argument. For $`\nabla\cdot\mathbf J`$, remember that $`\mathbf v`$ depends on $`t`$ only, not on $`\mathbf x`$, so it comes out of the divergence.

**Expected results.**

- (a) $`\rho=q\,\delta^3(\mathbf x-\mathbf r(t))`$ and $`\mathbf J=q\mathbf v\,\delta^3(\mathbf x-\mathbf r(t))`$.
- (b) $`\partial_t\rho=-q\,\mathbf v\cdot\nabla_{\mathbf x}\delta^3(\mathbf x-\mathbf r(t))=-\nabla\cdot\mathbf J`$.

## Done when

- the flux argument for $`\nabla^2\frac1r`$ is written on one page, including the case where $`V`$ does not contain the origin
- Jackson 1.3(a) agrees with your Griffiths 1.47(c)
- you can say why the conservation law in exercise 4 is exactly what makes the Maxwell equations consistent

## Progress

- [ ] Exercise 3
- [ ] Exercise 4
- [ ] Jackson 1.3
- [ ] Griffiths 1.48 (Should)
- [ ] Griffiths 1.64 (Should)
- [ ] Griffiths 1.49 (Could)
- [ ] Jackson 1.2 (Could)
