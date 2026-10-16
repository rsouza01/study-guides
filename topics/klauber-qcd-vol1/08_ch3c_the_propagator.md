# Module 08: Chapter 3c, the propagator (★★, Week 10; Protocol A): the week you asked for

**Books:** Klauber Ch. 3 (propagator sections); second source: Lancaster and Blundell, Tong, Schwartz chapter 2.
**Time:** 1 week.

## Why this matters

Klauber's derivation, done slowly, and now with Modules 03 and 05 behind you, done as recognition. All three contours. What each encodes as a boundary condition in time. Where antiparticles enter, and whether their appearance is a discovery or a definition. **Set your Module 03 and Module 05 pages beside his derivation and diff them.** Any difference is either a convention or a misunderstanding, and it is worth knowing which.

## The two key calculations

**Calculation 5: the vacuum two-point function.** Evaluate $\langle0|\phi(x)\phi(y)|0\rangle$: reduce to a three-momentum integral, do the angular part, get to a one-dimensional radial integral. No closed form is needed (it is a Bessel function). You need to see that it is **nonzero for spacelike separation**, which is what makes calculation 7 surprising and necessary.

**Calculation 6: the propagator as a time-ordered vacuum expectation value ★★.** The hardest calculation in the chapter, and what everything else has been for:
$$\langle0|T\{\phi(x)\phi(y)\}|0\rangle=\int\frac{d^4k}{(2\pi)^4}\frac{i\,e^{-ik\cdot(x-y)}}{k^2-m^2+i\epsilon}.$$
Do it in the informative direction: start from the right-hand side, perform the $k^0$ integral by residues, closing the contour **downward for $x^0>y^0$ and upward for $x^0<y^0$** (Jordan's lemma decides which, and you should be able to say why). Watch the two $\theta$ functions *generate themselves* out of the two closings. That is the moment $i\epsilon$ stops being decoration: **time ordering and the contour prescription are one statement in two languages**, and this calculation is the proof. Your three pages from Module 03 are the other half: set them beside this and confirm that the Feynman prescription is the one of the three that produces time ordering. **If you can do only one of the eight, make it this one.**

## Diagnostic (40 minutes, no notes)

1. Compute $\langle0|\phi(x)\phi(y)|0\rangle=\int\frac{d^3k}{(2\pi)^32\omega}e^{-ik\cdot(x-y)}$ at equal times and show it is nonzero for spacelike separation.
2. Perform the $k^0$ integral of $\int\frac{d^4k}{(2\pi)^4}\frac{i\,e^{-ik\cdot x}}{k^2-m^2+i\epsilon}$ by residues for $x^0>0$ and $x^0<0$.
3. Show the result equals $\theta(x^0)D(x)+\theta(-x^0)D(-x)$ with $D(x)=\int\frac{d^3k}{(2\pi)^32\omega}e^{-ik\cdot x}$.
4. State which of the three contours gives time ordering and why.
5. Express the retarded function through the commutator.

## Prerequisites

Modules 03, 05 and 07.

## Detailed topics (checklist)

- The two-point function $D(x-y)=\langle0|\phi(x)\phi(y)|0\rangle=\int\frac{d^3k}{(2\pi)^32\omega_{\mathbf k}}e^{-ik\cdot(x-y)}$; equal times: $D(r)=\frac{m}{4\pi^2r}K_1(mr)$ (massless: $\frac{1}{4\pi^2r^2}$), decaying as $e^{-mr}$ at large $r$.
- The commutator $[\phi(x),\phi(y)]=D(x-y)-D(y-x)$ and the retarded function $G_{\rm ret}(x)=-i\theta(x^0)\langle[\phi(x),\phi(0)]\rangle$ for the normalisation $(\Box+m^2)G=-\delta^4$.
- The Feynman propagator: $D_F(x-y)=\langle T\phi(x)\phi(y)\rangle=\theta(x^0-y^0)D(x-y)+\theta(y^0-x^0)D(y-x)=\int\frac{d^4k}{(2\pi)^4}\frac{i\,e^{-ik\cdot(x-y)}}{k^2-m^2+i\epsilon}$; the $i\epsilon$ puts the positive-energy pole below and the negative-energy pole above the real axis. Antiparticles: for the real field the negative-frequency part of the propagation backward in time *is* the same particle; for a complex field it is the distinct antiparticle.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Calculation 5; the radial integral |
| B1 | Exercises 1 to 3 |
| A2 | Calculation 6 by residues |
| B2 | Exercises 4 and 5 |
| A3 | Diff against your Modules 03 and 05 pages; the retarded function |
| B3 | Exercises 6 to 10 |

## Derive from scratch

1. Calculation 5, to the radial integral and its Bessel form.
2. Calculation 6, both closings.
3. $D_F=\theta D+\theta D$.
4. The commutator and $G_{\rm ret}=-i\theta\langle[\phi,\phi]\rangle$.
5. The explicit sign check against Module 05.

## Exercises

1. **[T] Calculation 5:** $\int\frac{d^3k}{(2\pi)^32\omega}e^{i\mathbf k\cdot\mathbf r}=\frac{1}{(2\pi)^3}\frac{4\pi}{r}\int_0^\infty\frac{k\sin kr}{2\omega}dk=\frac{1}{4\pi^2r}\int_0^\infty\frac{k\sin kr}{\omega}dk$; with $\int_0^\infty\frac{k\sin kr}{\sqrt{k^2+m^2}}dk=mK_1(mr)$ obtain $D(r)=\frac{m}{4\pi^2r}K_1(mr)$ (verify the identity numerically for $m=1$, $r=1$: $K_1(1)=0.602$).
2. **[T] Short and long distance:** $D(r)\to\frac{1}{4\pi^2r^2}$ for $mr\ll1$ and $\sim e^{-mr}$ for $mr\gg1$: nonzero outside the light cone.
3. **[T] Spacelike versus timelike:** show $D(x)$ depends only on $x^2$ for $x^2<0$ (Lorentz invariance) so spacelike separations $|{\bf r}|$ and $t=0$ suffice.
4. **[T] Calculation 6:** for $x^0>0$ close below, enclosing $k^0=+E$: $D_F=\int\frac{d^3k}{(2\pi)^3}\frac{1}{2E}e^{-iEx^0+i\mathbf k\cdot\mathbf x}$; for $x^0<0$ close above, enclosing $k^0=-E$ and relabel $\mathbf k\to-\mathbf k$: $\int\frac{d^3k}{(2\pi)^3}\frac1{2E}e^{+iEx^0+i\mathbf k\cdot\mathbf x}$; together $D_F=\theta(x^0)D(x)+\theta(-x^0)D(-x)$.
5. **[T] The other two contours:** check that the retarded contour gives $G_{\rm ret}=-\theta(x^0)\int\frac{d^3k}{(2\pi)^3}\frac{\sin Ex^0}{E}e^{i\mathbf k\cdot\mathbf x}=-i\theta(x^0)\langle[\phi(x),\phi(0)]\rangle$ and the advanced the mirror image; state which of the three is time-ordered.
6. **[T] Equal-time limit:** $\lim_{x^0\to0}\partial_0D_F$ and the equal-time commutator: $[\phi(\mathbf x,t),\dot\phi(\mathbf y,t)]=i\delta^3(\mathbf x-\mathbf y)$ from $\partial_0[D(x)-D(-x)]\big|_{x^0=0}=-i\delta^3(\mathbf x)$.
7. **[T] Check against Module 05:** the $D_F$ you get here equals $iG_F$ of Module 05 exercise 4 with $G_F=-\frac{i}{2E}e^{-iE|t|}$ in momentum space.
8. **[C] Contours as boundary conditions in time:** what does each of the three contours encode physically for a source turned on at $t=0$?
9. **[C] Antiparticles:** does the appearance of antiparticles come out as a discovery or as a definition? Defend your answer with the complex-field propagator.
10. **[C] The Week 10 test:** explain the Feynman prescription to someone who knows classical Green functions but no QFT, **without equations**. If this comes out cleanly you own the chapter, and it is the single best predictor of how the rest of the book will go.

## Optional extension

Evaluate $D_F$ at spacelike separation numerically by direct $k^0$ integration with a small finite $\epsilon$ and compare with $\frac{m}{4\pi^2r}K_1(mr)$.

## Pitfalls

- Closing the contour on the wrong side or forgetting the relabelling $\mathbf k\to-\mathbf k$ for $x^0<0$.
- Dropping the $i$ in the numerator of $D_F$.
- Confusing $D$ (two-point function), $\Delta$ (commutator function) and $D_F$ (time-ordered).

## Gate questions

1. Why does the Feynman contour produce time ordering?
2. Why is $D(x)\ne0$ outside the light cone while the commutator vanishes there?
3. What does the retarded function measure?

## One-page cheat sheet contents

$D(x)$; $D(r)=\frac{m}{4\pi^2r}K_1(mr)$; $D_F$ in position and momentum space; the three contours and what they select.
