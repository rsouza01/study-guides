# Module 11: Green functions for the wave equation (★★★: the most important module)

**Books:** Jackson **6.4** (Green functions for the wave equation) and **6.5** (retarded solutions for the fields: Jefimenko); Griffiths 10.2 (retarded potentials, Jefimenko's equations) and 10.3 (point charges); Barton, *Elements of Green's Functions and Propagation* (strongly recommended, precisely targeted at this goal); Module 02 (contour integrals) is the prerequisite.
**Time:** 3 weeks (six sessions). **The single most important week of the whole guide lives here.** Protect it at the expense of anything else.

## Why this matters

Jackson does the Fourier construction: $\Box G=-4\pi\delta^{(4)}\Rightarrow\tilde G(k,\omega)=\frac{4\pi}{k^2-\omega^2/c^2}$, and the poles at $\omega=\pm ck$ lie **on the real axis**. The integral is undefined until you say how to go around them. Different contours give $G_{\rm ret}$ and $G_{\rm adv}$, and in a step Jackson does not take, but you should write in the margin, the Feynman prescription $\frac{1}{k^2+i\epsilon}$. **The choice of contour is a choice of boundary condition in time.** $G_{\rm ret}$ means "no incoming radiation before the source acted"; $G_F$ means "positive frequencies forward, negative frequencies backward", which means antiparticles. What Peskin does in his Klein-Gordon propagator section is this calculation with $k^2\to k^2-m^2$.

## Skip-test (40 minutes, no notes)

1. Write the wave equation with source, $\left(\nabla^2-\frac{1}{c^2}\partial_t^2\right)\psi=-4\pi f(\mathbf x,t)$, and its Green function $\Box G=-4\pi\delta^3(\mathbf x-\mathbf x')\delta(t-t')$.
2. Fourier transform in space and time to get $\tilde G=\frac{4\pi}{k^2-\omega^2/c^2}$; state where the poles are and what the choices $\omega\to\omega\pm i\epsilon$ give.
3. Evaluate the $\omega$-integral for the retarded case to get $G_{\rm ret}(\mathbf k,\tau)=4\pi c\,\theta(\tau)\frac{\sin ck\tau}{k}$, then the $\mathbf k$-integral to get $G_{\rm ret}=\frac{\delta(\tau-R/c)}{R}$ ($\tau=t-t'$, $R=|\mathbf x-\mathbf x'|$).
4. Write the retarded potentials $\Phi=\frac{1}{4\pi\epsilon_0}\int\frac{\rho(\mathbf x',t-R/c)}{R}d^3x'$ and $\mathbf A=\frac{\mu_0}{4\pi}\int\frac{\mathbf J(\mathbf x',t-R/c)}{R}d^3x'$.
5. Rewrite $G_{\rm ret}$ in manifestly invariant form $2\theta(t-t')\delta\left[c^2(t-t')^2-R^2\right]$ (units: $x^0=ct$ conventions as in your copy).

## Prerequisites

Modules 02 (contours, $\pm i\epsilon$), 05 (Green functions), 10 (Lorenz gauge: four copies of the scalar wave equation).

## Detailed topics (checklist)

**The Green function (6.4) [Must]**
- $\Box G=-4\pi\delta^3(\mathbf x-\mathbf x')\delta(t-t')$; $G(\mathbf x,t)=\int\frac{d^3k\,d\omega}{(2\pi)^4}\frac{4\pi\,e^{i\mathbf k\cdot\mathbf R-i\omega\tau}}{k^2-\omega^2/c^2}$.
- **The $\omega$-integral:** poles at $\omega=\pm ck$ on the real axis. *Retarded:* contour passing above both poles (equivalently $\omega\to\omega+i\epsilon$): for $\tau<0$ close in the upper half plane (no poles) so $G=0$; for $\tau>0$ close below: $G_{\rm ret}(\mathbf k,\tau)=4\pi c\,\theta(\tau)\frac{\sin ck\tau}{k}$. *Advanced:* contour below the poles; $\theta(-\tau)$. *Feynman:* positive-frequency pole below, negative-frequency pole above (equivalently $k^2\to k^2-\omega^2/c^2-i\epsilon$): $\frac{i\,4\pi c}{2k}e^{-ick|\tau|}$-type (check the factor in exercise 8).
- **The $\mathbf k$-integral:** $\int\frac{d^3k}{(2\pi)^3}e^{i\mathbf k\cdot\mathbf R}\frac{\sin ck\tau}{k}=\frac{\delta(R-c\tau)}{4\pi R}$ for $\tau>0$, so $G_{\rm ret}=\frac{1}{R}\delta\left(\tau-\frac Rc\right)$ and $G_{\rm adv}=\frac1R\delta\left(\tau+\frac Rc\right)$.
- **Covariant form:** $G_{\rm ret}=2\theta(x^0-x'^0)\delta\left[(x-x')^2\right]$ with $(x-x')^2=(x^0-x'^0)^2-R^2$: support only on the forward light cone (Jackson 12.11 returns to this).

**Retarded potentials and fields (6.5) [Must]**
- Retarded potentials; the causal interpretation (the field at $(\mathbf x,t)$ depends on the source at the earlier time $t-R/c$); **Jefimenko's equations** for $\mathbf E$ and $\mathbf B$ in terms of $\rho$, $\partial_t\rho$ and $\partial_t\mathbf J$ at the retarded time.
- Quasi-static limit and the connection to Module 03 (static $\to$ Poisson).

**Dimension dependence [Should]**
- Method of descent: integrating the 3D $G$ over one (two) transverse coordinates gives the 2D (1D) Green function. In 1D, $G=2\pi c\,\theta(c\tau-|x|)$; in 2D, $G=\frac{2c\,\theta(c\tau-\rho)}{\sqrt{c^2\tau^2-\rho^2}}$ has a tail *inside* the light cone: **Huygens' principle fails in even spatial dimension**, a genuinely deep fact.

## Method card

**Retarded Green function from the contour:** (1) Fourier transform to $\tilde G=\frac{4\pi}{k^2-\omega^2/c^2}$; (2) locate the poles $\omega=\pm ck$ and choose the contour for the boundary condition ($+i\epsilon$ for retarded); (3) for each sign of $\tau$ close the contour where $e^{-i\omega\tau}$ decays; (4) sum residues; (5) do the $\mathbf k$-integral with the angular average $\int d\Omega\,e^{i\mathbf k\cdot\mathbf R}=4\pi\frac{\sin kR}{kR}$ and the identity $\int_0^\infty\sin kR\sin ck\tau\,dk=\frac\pi2[\delta(R-c\tau)-\delta(R+c\tau)]$; (6) check support (causality) and the static limit.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Jackson 6.4 (first read); Barton on $G_{\rm ret}$/$G_{\rm adv}$; Griffiths 10.2 |
| B1 | Exercises 1 and 2 |
| A2 | Re-derive the $\omega$-contour by hand with the method card |
| B2 | Exercises 3 and 4 |
| A3 | Jackson 6.5; the invariant form; Jefimenko |
| B3 | Exercises 5 to 7 |
| A4 | The Feynman contour; exercises 8 and 9 |
| B4 | **Jackson targets** (exercise 10) |
| A5 | The blank-page gate and the computational task |
| B5 | Spare session; redo the gate until it takes 20 minutes |

## Derive from scratch

1. $G_{\rm ret}(\mathbf k,\tau)=4\pi c\,\theta(\tau)\frac{\sin ck\tau}{k}$ from the contour.
2. $G_{\rm ret}(\mathbf x,\tau)=\frac{\delta(\tau-R/c)}{R}$ from the $\mathbf k$-integral.
3. The invariant form $2\theta(x^0)\delta(x^2)$.
4. The 2D Green function by descent and its tail.
5. The Feynman contour result.

## Bare-minimum exercises (with expected results)

1. **The ODE route:** for each $\mathbf k$ the equation $(\partial_\tau^2+c^2k^2)g=4\pi c^2\delta(\tau)$ with $g=0$ for $\tau<0$ has solution $g=4\pi c\,\theta(\tau)\frac{\sin ck\tau}{k}$ (continuous, with a jump $4\pi c^2$ in $\partial_\tau g$): the same jump-condition logic as Module 07, in time.
2. **Inverse transform:** $\int\frac{d^3k}{(2\pi)^3}e^{i\mathbf k\cdot\mathbf R}\frac{\sin ck\tau}{k}=\frac{1}{2\pi^2R}\int_0^\infty\sin kR\sin ck\tau\,dk=\frac{\delta(R-c\tau)}{4\pi R}$; multiply by $4\pi c$ to get $\frac{\delta(\tau-R/c)}{R}$.
3. **Retarded potentials solve the equation:** for a static source $\rho(\mathbf x')$ the retarded potential reduces to the Poisson integral $\Phi=\frac{1}{4\pi\epsilon_0}\int\frac{\rho}{R}d^3x'$; for a source switched on at $t=0$ show $\Phi$ vanishes outside the light cone.
4. **Method of descent:** integrating $\frac{1}{R}\delta(\tau-R/c)$ over $y$ gives the 2D Green function $\frac{2c\,\theta(c\tau-\rho)}{\sqrt{c^2\tau^2-\rho^2}}$; integrating over $x$ as well gives the 1D one $2\pi c\,\theta(c\tau-|x|)$.
5. **Huygens:** explain from exercise 4 why a pulse in 3D is sharp (the signal arrives and leaves) while in 2D it has a tail; give the odd/even dimension rule.
6. **Jefimenko:** the electric field is $\mathbf E=\frac{1}{4\pi\epsilon_0}\int\left[\frac{\rho\hat{\mathbf R}}{R^2}+\frac{\dot\rho\hat{\mathbf R}}{cR}-\frac{\dot{\mathbf J}}{c^2R}\right]_{t_{\rm ret}}d^3x'$; check the static limit and the radiation-field term $\propto\frac1R$.
7. **Covariant form:** use $\delta(x_0^2-R^2)=\frac{\delta(x_0-R)+\delta(x_0+R)}{2R}$ to show $\frac{1}{R}\delta(x_0-R)=2\theta(x_0)\delta(x_0^2-R^2)$.
8. **Feynman contour:** $\int\frac{d\omega}{2\pi}\frac{e^{-i\omega\tau}}{\omega_k^2-\omega^2-i\epsilon}=\frac{i}{2\omega_k}e^{-i\omega_k|\tau|}$ ($\omega_k=ck$): positive frequency forward in time, negative frequency backward. Compare with the retarded $\theta(\tau)\frac{\sin\omega_k\tau}{\omega_k}$ and the advanced $-\theta(-\tau)\frac{\sin\omega_k\tau}{\omega_k}$.
9. **Reading the contour as a boundary condition:** make a table with three columns (retarded, advanced, Feynman) and rows (pole positions relative to the contour, $\theta$-function structure, physical meaning).
10. **Jackson targets:** (a) about 6.1: the Green functions for the wave equation in one and two spatial dimensions from the 3D result (**mandatory**); (b) about 6.5: the fields of a uniformly moving charge from the retarded potentials (keep the answer: $\mathbf E=\frac{q}{4\pi\epsilon_0}\frac{(1-\beta^2)\mathbf R}{R^3\left(1-\beta^2\sin^2\psi\right)^{3/2}}$ with $\mathbf R$ from the *present* position and $\psi$ the angle between $\mathbf R$ and $\mathbf v$; you will re-derive it by boosting in Module 15).

## Blank-page gate (Month 3, item 3)

**Derive $G_{\rm ret}$ from the Fourier integral, contour and all**, reduce it to $\frac{1}{R}\delta(t'-t+R/c)$, then rewrite it in manifestly invariant form using $\delta[(x-x')^2]\theta(t-t')$ and verify agreement. *Repeat until this takes 20 minutes.*

**Computational task (project):** numerically evaluate $\int dk_0\frac{e^{-ik_0t}}{k_0^2-|\mathbf k|^2+i\epsilon}$ for all three contour prescriptions; plot $G(t)$ at fixed $\mathbf k$; take $\epsilon\to0$ and watch the retarded/advanced/Feynman structure emerge. Half a day, and it pays for itself repeatedly later.

## Pitfalls

- Closing the contour on the wrong side for the sign of $\tau$.
- Forgetting the $\theta(\tau)$ (it is what makes $G_{\rm ret}$ causal).
- Confusing Jackson's $4\pi$ normalization with the QFT $\delta^4$ normalization (note the offset once).
- Treating the retarded time as a fixed time rather than a function of $\mathbf x'$.

## Gate questions

1. Why is the choice of contour a choice of boundary condition in time?
2. Why does Huygens' principle fail in even dimensions?
3. What physical statement does $G_F$ encode that $G_{\rm ret}$ does not?

## One-page cheat sheet contents

$\Box G=-4\pi\delta^4$; $\tilde G$; the three contours and their results; $G_{\rm ret}=\frac{\delta(\tau-R/c)}{R}=2\theta\delta(x^2)$; retarded potentials; Jefimenko.
