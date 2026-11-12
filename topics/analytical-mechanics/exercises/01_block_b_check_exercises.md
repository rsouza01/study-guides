# Module 01, Block B: check exercises

Self-check for Block B (Taylor series in several variables and exact differentials). Notes, books and your cheat sheet are all fair game.

## Read first

- Boas 4.2 (power series in two variables) and 4.3 (total differentials). Section numbers are from memory of the 3rd edition, so confirm them in your copy.
- Stewart 16.3 for the exactness test, which you already did in the EM prelude.

**Notation:** partial derivatives are written $`\partial_x f`$ and $`\partial_x^2 f`$. A subscript outside a derivative marks the variable held fixed, e.g. $`\left(\frac{\partial T}{\partial V}\right)_S`$.

## Taylor series in several variables

1. Write the Taylor polynomial of $`f(x,y)=e^x\cos y`$ about $`(0,0)`$ up to and including all second-order terms.

2. Write the Taylor polynomial of $`g(x,y)=\ln(1+x+y)`$ about $`(0,0)`$ up to and including all second-order terms. Then check your result against the one-variable series of $`\ln(1+s)`$ with $`s=x+y`$.

3. Let $`V(x,y)=\frac{x^4}{4}-\frac{x^2}{2}+\frac{y^2}{2}+xy^2`$.
   - Show that $`(1,0)`$ is a stationary point.
   - Expand $`V`$ to second order about $`(1,0)`$.
   - Write the matrix of second derivatives at that point. This is the matrix that gives small-oscillation frequencies in Module 06.

## Exact differentials

4. Decide whether $`(y\,e^{xy}+2x)\,dx+(x\,e^{xy}+3y^2)\,dy`$ is exact. If it is, find the function $`f(x,y)`$ whose differential it is.

5. Show that $`y\,dx-x\,dy`$ is not exact. Then show that $`\frac{1}{y^2}\,(y\,dx-x\,dy)`$ is exact, and find the function whose differential it is.

6. Thermodynamics link: for $`dU=T\,dS-P\,dV`$, use the exactness condition to deduce $`\left(\frac{\partial T}{\partial V}\right)_S=-\left(\frac{\partial P}{\partial S}\right)_V`$.

## Done when

- You can explain why the two mixed second derivatives of a smooth function must agree, and how that fact gives the exactness test.
- You can read the second-order terms of a two-variable Taylor expansion as the matrix of second derivatives.
- You can say what an integrating factor does, in your own words.

## Progress

- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4
- [ ] 5
- [ ] 6
