# Module 01, Block A: check exercises

Closed-book self-check for Block A (partial derivatives, chain rule, implicit differentiation, Jacobians). Budget about 90 minutes in total.

**Related reading:** Stewart 14.3, 14.5 and 15.9.

**Notation:** partial derivatives are written $`\partial_x w`$ and $`\partial_x^2 w`$. The square of a first derivative is written with parentheses, e.g. $`(\partial_x w)^2`$. A subscript outside the derivative marks the variables held fixed, e.g. $`\left(\frac{\partial w}{\partial x}\right)_y`$.

## Partial derivatives (Stewart 14.3)

1. For $`f=x^2y^3+e^{xy}`$, compute $`\partial_x\partial_y f`$ and $`\partial_y\partial_x f`$ and confirm they agree.
2. Show that $`u=(x^2+y^2+z^2)^{-1/2}`$ satisfies $`\partial_x^2u+\partial_y^2u+\partial_z^2u=0`$ away from the origin.

## Chain rule (Stewart 14.5)

3. Let $`z=x^2y+y\sin x`$ with $`x=t^2`$ and $`y=\cos t`$. Find $`dz/dt`$.
4. Let $`w=f(x,y)`$ with $`x=r\cos\theta`$ and $`y=r\sin\theta`$. Express $`\partial_r w`$ and $`\partial_\theta w`$ through $`\partial_x w`$ and $`\partial_y w`$, then show
   $`(\partial_x w)^2+(\partial_y w)^2=(\partial_r w)^2+\frac{1}{r^2}(\partial_\theta w)^2`$.
5. Show that $`u(x,t)=F(x-ct)+G(x+ct)`$ satisfies $`\partial_t^2u=c^2\,\partial_x^2u`$ for any twice-differentiable $`F`$ and $`G`$.
6. Let $`z=f(x,y)`$ with $`x=s+t`$ and $`y=s-t`$. Express $`\partial_s^2 z-\partial_t^2 z`$ in terms of derivatives of $`f`$.

## Implicit differentiation and held-fixed variables (Stewart 14.5)

7. For $`x^3+y^3+z^3=6xyz`$, find $`\partial z/\partial x`$ at $`(1,2,3)`$.
8. If $`F(x,y,z)=0`$ defines each variable implicitly, show
   $`\left(\frac{\partial x}{\partial y}\right)_z\left(\frac{\partial y}{\partial z}\right)_x\left(\frac{\partial z}{\partial x}\right)_y=-1`$.
9. Let $`w=x^2+y^2+z^2`$ with $`z=xy`$. Compute $`\left(\frac{\partial w}{\partial x}\right)_y`$ and $`\left(\frac{\partial w}{\partial x}\right)_z`$, and explain why they differ.

## Jacobians (Stewart 15.9)

10. Find $`\frac{\partial(x,y)}{\partial(u,v)}`$ for $`x=u^2-v^2`$ and $`y=2uv`$.
11. Derive the Jacobian of spherical coordinates from the $`3\times3`$ determinant, and check it against $`r^2\sin\theta`$.
12. For $`u=x+y`$ and $`v=x-y`$, compute $`\frac{\partial(u,v)}{\partial(x,y)}`$ and $`\frac{\partial(x,y)}{\partial(u,v)}`$ separately, and verify that they multiply to $`1`$.
13. Use $`x=au`$ and $`y=bv`$ to find the area of the ellipse $`\frac{x^2}{a^2}+\frac{y^2}{b^2}\le1`$.
14. Find the area of the region bounded by $`xy=1`$, $`xy=2`$, $`y=x`$ and $`y=2x`$, using $`u=xy`$ and $`v=y/x`$.

## Preview of Module 08 (optional)

15. For $`Q=q\cos\alpha+p\sin\alpha`$ and $`P=-q\sin\alpha+p\cos\alpha`$, compute $`\frac{\partial(Q,P)}{\partial(q,p)}`$. A transformation whose Jacobian equals $`1`$ preserves phase-space area.

