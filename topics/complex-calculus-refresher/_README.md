# Complex Calculus Refresher: the prerequisites for Goldstein and Jackson

*Ávila (primary) + Churchill & Brown (companion) · single-file edition, v1.0 · R. A. de Souza · October 2026*

**Primary text:** Geraldo Ávila, *Variáveis Complexas e Aplicações*, 3ª ed. (the PDF from Prof. Toscano's course page).
**Companion:** J. W. Brown & R. V. Churchill, *Complex Variables and Applications* (**chapter numbers below are valid for the 7th, 8th and 9th editions**; I deliberately cite chapters, not section numbers, which can shift between editions), for English vocabulary, extra worked examples and drill problems.
**Scope:** *prerequisites only.* Everything that is not needed for Goldstein or Jackson (conformal mapping, Riemann surfaces, analytic continuation theory, the gamma function, fluid flow, the argument principle) is **parked** in Appendix A for a later, separate thread.
**Budget:** 8 weeks × 3 to 4 h ≈ **28 hours** (core), +4 to 6 h for the two optional modules. Runs *in parallel* with Goldstein and Jackson as a side study.
**Version history:** this single-file edition supersedes an earlier 10-week outline (v0.1) and a 7-week compression (v0.2). Same spine, now one self-contained document with the motivation, topic checklists, derivations to own, worked pointers, and **about 130 exercises with answers**.

> **How the answers were checked.** Every numerical or closed-form answer in this file was verified by running it (contour integrals by numerical quadrature on the contour, real integrals with `mpmath`, the damped-oscillator Green function and the Kramers-Kronig relation by direct numerical integration). The checking script is in Appendix D, so you can rerun it. What I could **not** do: open Ávila's 30+ MB PDF (too large for my tools). The page numbers below come from the table of contents of the author's copy; **do Task 0** to confirm them against yours.

---

## Contents

- [0. Why this exists and what it must deliver](#0-why-this-exists-and-what-it-must-deliver)
- [1. Working conventions](#1-working-conventions)
- [2. Study plan and triage](#2-study-plan-and-triage)
- [Module 0. Prerequisites and diagnostic](#module-0-prerequisites-and-diagnostic)
- [Module 1. Complex numbers (Week 1, part 1)](#module-1-complex-numbers-week-1-part-1)
- [Module 2. Functions, limits, analyticity, Cauchy-Riemann (Week 1, part 2)](#module-2-functions-limits-analyticity-cauchy-riemann-week-1-part-2)
- [Module 3. Elementary functions, the logarithm, branches (Week 2)](#module-3-elementary-functions-the-logarithm-branches-week-2)
- [Module 4. Contour integrals and Cauchy's theorem (Week 3)](#module-4-contour-integrals-and-cauchys-theorem-week-3)
- [Module 5. Cauchy's integral formula and its consequences (Week 4)](#module-5-cauchys-integral-formula-and-its-consequences-week-4)
- [Module 6. Taylor and Laurent series (Week 5)](#module-6-taylor-and-laurent-series-week-5)
- [Module 7. Singularities and the residue theorem (Week 6)](#module-7-singularities-and-the-residue-theorem-week-6)
- [Module 8. Real integrals by residues; Jordan's lemma; principal values (Week 7)](#module-8-real-integrals-by-residues-jordans-lemma-principal-values-week-7)
- [Module 9. Capstone: Green functions, causality and Kramers-Kronig (Week 8)](#module-9-capstone-green-functions-causality-and-kramers-kronig-week-8)
- [Module 10 (optional). Harmonic functions, maximum modulus, Dirichlet and Neumann](#module-10-optional-harmonic-functions-maximum-modulus-dirichlet-and-neumann)
- [Module 11 (optional). Multivalued integrands: keyhole contours](#module-11-optional-multivalued-integrands-keyhole-contours)
- [Appendix A. Parked: non-standard topics for a later thread](#appendix-a-parked-non-standard-topics-for-a-later-thread)
- [Appendix B. The gate (blank page, unrushed)](#appendix-b-the-gate-blank-page-unrushed)
- [Appendix C. Cheat-sheet contents](#appendix-c-cheat-sheet-contents)
- [Appendix D. Verification script](#appendix-d-verification-script)
- [Appendix E. Parallel map to Goldstein and Jackson](#appendix-e-parallel-map-to-goldstein-and-jackson)
- [Appendix F. Study tips specific to this track](#appendix-f-study-tips-specific-to-this-track)

---

## 0. Why this exists and what it must deliver

Complex analysis in your journey is a **tool**, not a destination. Three concrete payoffs, in order of urgency:

1. **Contour integration for Green functions (Jackson ch. 6, and ch. 12 on covariant Green functions; later QFT propagators).** The Fourier transform of the wave equation has poles *on the real axis*; the integral is undefined until you choose how to go around them, and the three choices (retarded, advanced, Feynman) are three physically different Green functions. The calculation is: choose the half-plane, justify the arc with **Jordan's lemma**, collect **residues**.
2. **Causality and Kramers-Kronig (Jackson ch. 7, dispersion relations).** Causality $\Leftrightarrow$ analyticity of the response function in the upper half-plane; Cauchy's formula then ties $\operatorname{Re}\chi$ to $\operatorname{Im}\chi$.
3. **Everyday fluency:** complex exponentials for oscillations (Goldstein ch. 6 on small oscillations, Jackson's plane waves and phasors), characteristic roots in the complex plane (stability, damped motion), Fourier series and transforms, harmonic functions and the mean-value/no-extremum property (Jackson ch. 1 and 2, Earnshaw).

If you can do Module 9 (the capstone) cold, the track has done its job.

### How the weeks map onto your other tracks

| Week | This track | Needed by |
| --- | --- | --- |
| 1 | Complex numbers; analyticity and Cauchy-Riemann | Goldstein ch. 6 (complex notation for oscillations); Jackson ch. 1 (2D potentials) |
| 2 | Exponential, logarithm, powers, branches | any time $\sqrt{\ }$ or $\log$ shows up in an integrand |
| 3 | Contour integrals; Cauchy's theorem | everything below |
| 4 | Cauchy's integral formula; Liouville; mean value; maximum modulus | Jackson ch. 1 (mean-value theorem), Earnshaw |
| 5 | Taylor and Laurent series | Week 6 |
| 6 | Singularities and residues | Week 7 |
| 7 | Real integrals; Jordan's lemma; principal values | Jackson ch. 6 and 12 Green functions; Fourier transforms |
| 8 | **Capstone:** Green functions, causality, Kramers-Kronig; gate | Jackson ch. 6, 7, 12; QFT later |

Your earlier plan put the deadline at Jackson Week 11 (the retarded Green function) and Kramers-Kronig at Week 21. Weeks 1 to 7 should be finished a couple of weeks before you meet each of those.

**If you slip,** the weeks that can compress are 1, 2 and the optional modules. **Weeks 6, 7, 8 cannot.**

---

## 1. Working conventions

### 1.1 The loop (use it for every module)

1. **Read Ávila** for the idea (his preface quotes Arnold: theories arise from applications and only later acquire the abstract form that makes them hard to learn; the book follows that spirit). Portuguese will read fast.
2. **Derive** the items listed under "Own it" with the book closed.
3. **Drill Churchill**: the chapter listed gives the English terms and a bigger problem bank.
4. **Do the exercises here**; check with the answers, then with Ávila's *Respostas e sugestões* (inline after most exercise sets).
5. **Verify numerically** (Appendix D): contour integrals are *numerically checkable*; get in the habit.
6. **Blank-page test** at the end of each module (the "Own it" list).

### 1.2 Notation

$z=x+iy=re^{i\theta}$; $f=u+iv$; $\operatorname{Log}$ is the *principal* logarithm ($-\pi<\arg z\le\pi$), $\log$ the multivalued one. Contours are positively oriented (counterclockwise) unless stated. Physics convention for time dependence: $e^{-i\omega t}$ (Jackson). Ávila and Churchill usually do not fix a convention; state yours.

### 1.3 Task 0 (30 minutes): your reading map

Create `notes/complex_reading_map.md` with columns *Module, Ávila pages (from your TOC), Churchill chapter, done?* and **confirm every page number below against your copy**. The pages quoted here come from your earlier TOC:

| Ávila | Pages | Content |
| --- | --- | --- |
| Cap. 1 | 1 to 33 | complex numbers; polar form and De Moivre (8 to 12); roots (15 to 20); exponential (21 to 25); plane point sets (26 to 33) |
| Cap. 2 | 34 to 74 | limits, analyticity, Cauchy-Riemann (53), necessary and sufficient condition (55), polar CR (57), geometric interpretation (59), exponential (61), logarithm (65 to 69), $z^a$ (70), trig/hyperbolic and inverses |
| Cap. 3 | 75 to 117 | arcs and contours (77), contour integral (79), invariance (81), Cauchy's theorem via Green (89), primitives (93), Cauchy integral formula (101), derivatives (103), harmonic functions (109), maximum modulus (113), Dirichlet and Neumann (114) |
| Cap. 4 | 118 to 150 | series (120), power series (127), Taylor (133), products and quotients (138), Laurent (144), infinity and zeros (147) |
| Cap. 5 | 151 to 180 | isolated singularities (151 to 154), residue theorem (157), improper integrals (161), Jordan's lemma (164), multivalued integrands (169), trig integrals (173), argument principle (175) |

### 1.4 Companion map (Churchill & Brown, 7th to 9th editions share this chapter order)

| Churchill chapter | Use it for |
| --- | --- |
| 1 Complex Numbers | Module 1 |
| 2 Analytic Functions | Module 2 (CR, harmonic functions) |
| 3 Elementary Functions | Module 3 (exp, log, branches, powers, trig, hyperbolic) |
| 4 Integrals | Modules 4 and 5 (contours, Cauchy-Goursat, Cauchy integral formula, Liouville, maximum modulus) |
| 5 Series | Module 6 (Taylor, Laurent) |
| 6 Residues and Poles | Module 7 |
| 7 Applications of Residues | Modules 8 and 9 (improper integrals, Jordan's lemma, indented paths, trig integrals; the argument principle and inverse Laplace sections are *parked*) |

### 1.5 Mini glossary (Portuguese to English)

| Português | English |
| --- | --- |
| função analítica / holomorfa | analytic / holomorphic function |
| equações de Cauchy-Riemann | Cauchy-Riemann equations |
| contorno, caminho | contour, path |
| teorema de Cauchy | Cauchy's theorem (Cauchy-Goursat) |
| fórmula integral de Cauchy | Cauchy integral formula |
| série de Taylor, série de Laurent | Taylor series, Laurent series |
| singularidade removível / pólo / essencial | removable / pole / essential singularity |
| resíduo, teorema do resíduo | residue, residue theorem |
| lema de Jordan | Jordan's lemma |
| valor principal de Cauchy | Cauchy principal value |
| ramo, corte de ramificação | branch, branch cut |
| função harmônica, harmônica conjugada | harmonic function, harmonic conjugate |
| princípio do módulo máximo | maximum modulus principle |
| simplesmente conexo | simply connected |

---

## 2. Study plan and triage

| Week | Module | Ávila | Churchill | Hours |
| --- | --- | --- | --- | --- |
| 0 | Prerequisites and diagnostic | n/a | n/a | 1 to 2 |
| 1 | 1 Complex numbers; 2 Analyticity and CR | Cap. 1; Cap. 2 pp. 34 to 62 | ch. 1, 2 | 4 |
| 2 | 3 Elementary functions, logarithm, branches | Cap. 2 pp. 63 to 74 | ch. 3 | 3 to 4 |
| 3 | 4 Contour integrals and Cauchy's theorem | Cap. 3 pp. 75 to 101 | ch. 4 (first half) | 4 |
| 4 | 5 Cauchy integral formula and consequences | Cap. 3 pp. 101 to 109 (+113) | ch. 4 (second half) | 3 to 4 |
| 5 | 6 Taylor and Laurent series | Cap. 4 | ch. 5 | 4 |
| 6 | 7 Singularities and residues | Cap. 5 pp. 151 to 161 | ch. 6 | 4 |
| 7 | 8 Real integrals, Jordan's lemma, principal values | Cap. 5 pp. 161 to 169, 173 | ch. 7 | 4 to 5 |
| 8 | 9 Capstone and gate | (yours) | ch. 7 (indented paths) | 4 to 5 |
| opt. | 10 Harmonic functions, Dirichlet and Neumann | Cap. 3 pp. 109 to 117 | ch. 2, 4 | 2 to 3 |
| opt. | 11 Multivalued integrands (keyhole contours) | Cap. 5 pp. 169 to 173 | ch. 7 | 2 to 3 |

**Triage rule.** If a week goes badly: keep the *Own it* list and the starred (★) exercises of Modules 6 to 9; drop non-starred exercises of Modules 1 to 4. Do not shorten Modules 7 to 9.

**Exercise tiers.** ◦ warm-up (5 to 10 minutes), ★ core (the skills you need), ✦ physics bridge or challenge. Answers follow each set.

---

## Module 0. Prerequisites and diagnostic

**You need** (all from your Stewart track, ✓ means you reported finishing it):

- Partial derivatives and the chain rule (14.5 ✓).
- Line integrals $\int_C P\,dx+Q\,dy$ (16.2 ✓). **A contour integral is exactly this, with complex $P,Q$.**
- Green's theorem (16.4 ✓). Ávila (p. 89) proves Cauchy's theorem with it.
- Fundamental theorem for line integrals and path independence (16.3). Cauchy's theorem is its complex cousin.
- Improper integrals (7.8 ✓).
- **Power series and radius of convergence (Stewart ch. 11, parked).** **Hard dependency for Module 6 (Week 5).** Do Stewart 11.1 to 11.10 before or alongside Weeks 1 to 4.
- Trigonometric and hyperbolic identities; basic Fourier series (helpful, not blocking).

**Diagnostic (25 minutes, no book).** If you stall on more than two, do the corresponding Stewart section first.

1. Compute $\oint_C (x^2-y)\,dx+(x+y^2)\,dy$ around the unit circle (use Green). *Answer: $\iint(1-(-1))\,dA=2\pi$.*
2. Is $\mathbf F=(2xy,\,x^2+3)$ conservative? Find $f$ with $\nabla f=\mathbf F$. *Answer: yes, $f=x^2y+3y$.*
3. Radius of convergence of $\sum n!\,x^n/n^n$. *Answer: $e$.*
4. Evaluate $\int_{-\infty}^\infty \frac{dx}{1+x^2}$ by antiderivative. *Answer: $\pi$ (keep this one: you will redo it with residues).*
5. Write $\cos 3\theta$ in terms of $\cos\theta$. *Answer: $4\cos^3\theta-3\cos\theta$ (you will redo it with De Moivre).*
6. $\sinh x$ and $\cosh x$ in terms of exponentials; $\cosh^2-\sinh^2$. *Answer: $\tfrac12(e^x\mp e^{-x})$; $1$.*
7. State the ratio test and the comparison test. *(Answer: your Stewart notes.)*
8. Parametrize the circle of radius 2 centred at $1$ in the plane, and the segment from $1$ to $3+2i$ in $\mathbb R^2$. *Answer: $(1+2\cos t,\,2\sin t)$; $(1+2s,\,2s)$, $0\le s\le1$.*

---

## Module 1. Complex numbers (Week 1, part 1)

**Read:** Ávila Cap. 1 (pp. 1 to 33). **Drill:** Churchill ch. 1. **Time:** 1.5 to 2 h (fast review; slow down only where marked).

### Motivation

Complex numbers are how oscillations become algebra. A harmonic motion $x(t)=A\cos(\omega t-\varphi)$ is $\operatorname{Re}[\,Ae^{-i\varphi}e^{i\omega t}\,]$; derivatives become multiplication by $i\omega$; ODEs become polynomial equations (Goldstein's small oscillations: $\det(V-\omega^2T)=0$ with complex exponentials; Jackson's plane waves $e^{i(\mathbf k\cdot\mathbf x-\omega t)}$; AC circuits and phasors). Every later module uses $z=re^{i\theta}$ as the *working form*.

### Topics checklist

- **Algebra:** $\mathbb C$ as ordered pairs, $i^2=-1$, conjugate $\bar z$, modulus $|z|$, $z\bar z=|z|^2$, $1/z=\bar z/|z|^2$; $\operatorname{Re}z=(z+\bar z)/2$, $\operatorname{Im}z=(z-\bar z)/2i$.
- **Inequalities:** triangle inequality $|z_1+z_2|\le|z_1|+|z_2|$, reverse triangle inequality $\big||z_1|-|z_2|\big|\le|z_1-z_2|$ (you will use these in every ML estimate).
- **Polar form and Euler** (Ávila pp. 8 to 12): $z=r(\cos\theta+i\sin\theta)=re^{i\theta}$; **argument** $\arg z$ multivalued, $\operatorname{Arg}z\in(-\pi,\pi]$; product/quotient rules; De Moivre $(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta$.
- **Roots** (pp. 15 to 20): the $n$ values of $z^{1/n}$ are $r^{1/n}e^{i(\theta+2\pi k)/n}$, $k=0,\dots,n-1$; roots of unity; **your first multivaluedness**.
- **Exponential** (pp. 21 to 25): $e^z=e^x(\cos y+i\sin y)$, $e^{z+2\pi i}=e^z$, $|e^z|=e^x$, never zero. **This periodicity is the sole reason the logarithm is multivalued.**
- **Point sets** (pp. 26 to 33): neighbourhood, open, closed, boundary, connected, **domain** (open and connected), **simply connected** (no holes). Vocabulary for Cauchy's theorem.
- The **point at infinity** (just the notion: $z\to\infty$ means $|z|\to\infty$; "behaviour at infinity" matters for Jordan's lemma).

### Own it (blank page)

1. Euler's formula from the power series of $e^{i\theta}$.
2. De Moivre, and one trig identity derived from it.
3. The $n$ roots of $z^n=a$ and why they sit on a regular polygon.
4. Why $e^{z}$ is $2\pi i$-periodic and what this forces on $\log$.

### Exercises

1. ◦ Compute $(1+i)^{10}$. *Answer: $32i$.*
2. ◦ All cube roots of $-8$. *Answer: $2e^{i\pi/3}=1+i\sqrt3$, $-2$, $1-i\sqrt3$.*
3. ◦ Solve $z^4=-16$. *Answer: $z=\pm\sqrt2\pm i\sqrt2$ (the four points $2e^{i(\pi/4+k\pi/2)}$).*
4. ★ Show that the sum of the $n$ $n$th roots of unity is $0$ for $n\ge2$, and that their product is $(-1)^{n+1}$. *Hint: factor $z^n-1$ and use Vieta.*
5. ★ Describe the set $|z-1|=|z+i|$. *Answer: the line $y=-x$.*
6. ★ Describe $|z-2|+|z+2|=6$. *Answer: the ellipse $x^2/9+y^2/5=1$ (foci $\pm2$, $a=3$, $b^2=5$).*
7. ★ Use De Moivre to prove $\cos3\theta=4\cos^3\theta-3\cos\theta$ and find $\sin3\theta$. *Answer: $\sin3\theta=3\sin\theta-4\sin^3\theta$.*
8. ★ Sum $\sum_{k=0}^{n}\cos k\theta$ in closed form. *Answer: $\dfrac{\sin\frac{(n+1)\theta}2\cos\frac{n\theta}2}{\sin\frac\theta2}$ (take the real part of a geometric series).*
9. ✦ **Phasors.** Write $3\cos\omega t+4\sin\omega t$ as $A\cos(\omega t-\varphi)$. *Answer: $A=5$, $\varphi=\arctan(4/3)\approx53.13^\circ$ (it is $\operatorname{Re}[(3-4i)e^{i\omega t}]$).*
10. ★ Show $|e^{z}|=e^{x}$, $e^z\ne0$, and find all $z$ with $e^z=-1$. *Answer: $z=i\pi(2k+1)$.*
11. ★ Prove $|z_1+z_2|^2+|z_1-z_2|^2=2(|z_1|^2+|z_2|^2)$ (parallelogram law) and interpret it.
12. ◦ Express $\operatorname{Re}\frac{1+i}{3-4i}$. *Answer: $-\tfrac1{25}$ (the quotient is $\frac{(1+i)(3+4i)}{25}=\frac{-1+7i}{25}$).*

**Pitfalls.** Using $\arg$ as single-valued; forgetting that $z^{1/n}$ has $n$ values; applying $\sqrt{ab}=\sqrt a\sqrt b$ with negative reals.

---

## Module 2. Functions, limits, analyticity, Cauchy-Riemann (Week 1, part 2)

**Read:** Ávila Cap. 2 pp. 34 to 62 (CR on p. 53, necessity and sufficiency on p. 55, polar form on p. 57, geometric meaning on p. 59). **Drill:** Churchill ch. 2. **Time:** 2 to 2.5 h.

### Motivation

Complex differentiability is a *much* stronger condition than real differentiability: the limit $\lim_{h\to0}[f(z+h)-f(z)]/h$ must be the same for $h$ approaching from **every direction in the plane**. That single requirement forces the Cauchy-Riemann equations, which force $u$ and $v$ to be **harmonic**: every analytic function hands you two solutions of Laplace's equation for free. That is the bridge to 2D electrostatics (Jackson ch. 1 and 2), and it explains why analytic functions are rigid (Module 5).

### Topics checklist

- $f:\mathbb C\to\mathbb C$ as a map $\mathbb R^2\to\mathbb R^2$, $f=u(x,y)+iv(x,y)$.
- Limits and continuity (same as real analysis, with $|z|$ in place of $|x|$).
- **Derivative:** $f'(z_0)=\lim_{h\to0}\frac{f(z_0+h)-f(z_0)}h$ (complex $h$). Differentiation rules are identical to real calculus (sum, product, quotient, chain).
- **Cauchy-Riemann:** approaching along $h\in\mathbb R$ and $h\in i\mathbb R$ gives $f'=u_x+iv_x=v_y-iu_y$, so
$$u_x=v_y,\qquad u_y=-v_x.$$
Necessary for differentiability at a point; **sufficient** if $u,v$ have continuous first partials there (Ávila p. 55).
- **Polar form:** $u_r=\tfrac1rv_\theta$, $v_r=-\tfrac1ru_\theta$; then $f'(z)=e^{-i\theta}(u_r+iv_r)$.
- **Analytic (holomorphic) at a point:** differentiable in a whole neighbourhood. **Entire:** analytic everywhere. A function can be differentiable at one point and nowhere analytic (Exercise 2).
- **Harmonic functions:** $\nabla^2u=0$. If $f=u+iv$ is analytic then $u,v$ are harmonic (needs $C^2$, which Module 5 will prove automatically) and $v$ is a **harmonic conjugate** of $u$, unique up to a constant. Level curves of $u$ and $v$ are orthogonal (field lines and equipotentials).
- **Geometry** (Ávila p. 59): where $f'\ne0$, $f$ is *conformal* (it rotates by $\arg f'$ and scales by $|f'|$, preserving angles). Only this much: conformal *mapping* theory is parked.
- **Wirtinger derivative** (useful in physics): $\partial_{\bar z}=\tfrac12(\partial_x+i\partial_y)$. CR $\Leftrightarrow\partial_{\bar z}f=0$: analytic functions do not depend on $\bar z$.

### Own it

1. Derive CR from direction-independence.
2. Show CR $\Rightarrow$ $u,v$ harmonic (assuming $C^2$).
3. Find the harmonic conjugate of a given $u$ (integrate CR).
4. $|f'|^2=u_xv_y-u_yv_x$ (the Jacobian of the map).

### Exercises

1. ◦ Show $f(z)=\bar z$ is nowhere differentiable. *Answer: $u=x$, $v=-y$: $u_x=1\ne-1=v_y$.*
2. ★ Where is $f=x^2+iy^2$ differentiable? Analytic? *Answer: differentiable only on the line $y=x$ ($u_x=2x=v_y=2y$, $u_y=v_x=0$); analytic nowhere (no open neighbourhood).*
3. ★ Show $f=e^x(\cos y+i\sin y)$ is entire and $f'=f$. *Answer: $u_x=e^x\cos y=v_y$, $u_y=-e^x\sin y=-v_x$; $f'=u_x+iv_x=f$.*
4. ★ Verify $u=x^3-3xy^2$ is harmonic and find its conjugate. *Answer: $v=3x^2y-y^3+C$ (indeed $f=z^3$).*
5. ★ $u=\ln\sqrt{x^2+y^2}=\ln|z|$ is harmonic on $z\ne0$. Find a conjugate and explain the problem. *Answer: $v=\arg z$ is **multivalued** (changes by $2\pi$ around the origin): $f=\log z$. A harmonic function on a region with a hole need not have a single-valued conjugate.*
6. ★ Derive CR in polar coordinates and verify them for $f=z^n$. *Answer: $u=r^n\cos n\theta$, $v=r^n\sin n\theta$: $u_r=nr^{n-1}\cos n\theta=\frac1rv_\theta$ ✓.*
7. ★ If $f$ is analytic and $|f|$ is constant on a domain, show $f$ is constant. *Hint: $u^2+v^2=c$, differentiate, use CR.*
8. ★ If $f$ is analytic and $\operatorname{Re}f$ is constant, show $f$ is constant.
9. ★ Show $|f'(z)|^2=u_xv_y-u_yv_x$ (Jacobian) and interpret. *Answer: it is the local area scaling.*
10. ◦ Compute $f'$ for $f=\dfrac{z^2+1}{z-i}$. *Answer: $f=z+i$ for $z\ne i$, so $f'=1$.*
11. ✦ **2D electrostatics.** A line charge $\lambda$ has potential $\Phi=-\dfrac{\lambda}{2\pi\varepsilon_0}\ln r$. Write it as $\operatorname{Re}$ of an analytic function and name the complex potential and the field lines. *Answer: $F=-\frac{\lambda}{2\pi\varepsilon_0}\log z$; equipotentials $|z|=$const, field lines $\arg z=$const (radial).*
12. ✦ Show that $\partial_{\bar z}f=0\Leftrightarrow$ CR. *Answer: $\partial_{\bar z}f=\tfrac12[(u_x-v_y)+i(v_x+u_y)]$.*
13. ★ Is $f=\operatorname{Re}z$ analytic? $f=|z|^2$? *Answer: neither ($|z|^2$ is differentiable only at $0$).*

**Pitfalls.** Treating $z$ and $\bar z$ as independent in the wrong places; forgetting that harmonic conjugates exist on simply connected domains only (Exercise 5).

---

## Module 3. Elementary functions, the logarithm, branches (Week 2)

**Read:** Ávila Cap. 2 pp. 63 to 74 (logarithm p. 65, as a transformation p. 67, properties p. 69, $z^a$ p. 70). **Drill:** Churchill ch. 3. **Time:** 3 to 4 h. **This is a whole week on purpose.**

### Motivation

Because $e^z$ is periodic, $\log z=\ln|z|+i(\arg z+2\pi k)$ is **multivalued**. To get an analytic function you must *cut* the plane and pick a *branch*. Square roots, $z^a$, $\sqrt{z^2-1}$, $\ln(1+\ldots)$: all of them. You need this in Jackson whenever an integrand has a square root (e.g. $\sqrt{k^2-\omega^2/c^2}$ in wave problems), and in QFT a *branch cut in a propagator is a multi-particle threshold*. Poles are stable particles; cuts are continua.

### Topics checklist

- **Exponential:** $e^{z_1+z_2}=e^{z_1}e^{z_2}$; $(e^z)'=e^z$.
- **Trig and hyperbolic:** $\cos z=\frac{e^{iz}+e^{-iz}}2$, $\sin z=\frac{e^{iz}-e^{-iz}}{2i}$, $\cosh z=\cos iz$, $\sinh z=-i\sin iz$; the real identities carry over; **but $|\sin z|$ and $|\cos z|$ are unbounded**. $\cos(x+iy)=\cos x\cosh y-i\sin x\sinh y$.
- **Logarithm:** $\log z=\ln r+i(\theta+2\pi k)$. **Principal value** $\operatorname{Log}z=\ln r+i\operatorname{Arg}z$, analytic on $\mathbb C\setminus(-\infty,0]$ with $(\operatorname{Log}z)'=1/z$. The negative real axis is the **branch cut**; $\operatorname{Log}$ jumps by $2\pi i$ across it. The cut is a choice; the **branch point** ($z=0$) is not.
- **Identities fail on the cut:** $\operatorname{Log}(z_1z_2)\ne\operatorname{Log}z_1+\operatorname{Log}z_2$ in general; $\log(z_1z_2)=\log z_1+\log z_2$ holds as a statement about *sets of values*.
- **Powers:** $z^a=e^{a\log z}$ (multivalued unless $a\in\mathbb Z$); principal value $e^{a\operatorname{Log}z}$; $z^{1/n}$ has $n$ branches.
- **Inverse trig/hyperbolic** as logarithms: $\arcsin z=-i\log(iz+\sqrt{1-z^2})$.
- **How to build a single-valued branch of $\sqrt{(z-a)(z-b)}$:** write it as $\sqrt{z-a}\,\sqrt{z-b}$ with each factor having its own cut; if the cuts overlap on a common ray the *jumps cancel there* and only the segment between $a$ and $b$ remains a cut. This is the standard trick (Exercise 8).

### Own it

1. $\log z$ multivalued from $e^z$ periodic; principal value and cut.
2. $z^a$ and the example $i^i$.
3. Why $\operatorname{Log}(z_1z_2)\ne\operatorname{Log}z_1+\operatorname{Log}z_2$.
4. A cut for $\sqrt{z^2-1}$ along $[-1,1]$ only.

### Exercises

1. ◦ All $z$ with $e^z=-1$; all values of $\log(-1)$. *Answer: $z=i\pi(2k+1)$; $\log(-1)=i\pi(2k+1)$; $\operatorname{Log}(-1)=i\pi$.*
2. ★ Compute $i^i$ (all values and the principal value). *Answer: $e^{-\pi/2-2\pi k}$; principal $e^{-\pi/2}\approx0.2079$ (**real!**).*
3. ★ Principal value of $(1+i)^{1+i}$. *Answer: $\sqrt2\,e^{-\pi/4}\,e^{i(\ln\sqrt2+\pi/4)}\approx0.27396+0.58370\,i$.*
4. ★ Solve $\sin z=2$. *Answer: $z=\frac\pi2+2\pi k\pm i\ln(2+\sqrt3)$, with $\ln(2+\sqrt3)\approx1.3170$ ($\sin(\tfrac\pi2+iy)=\cosh y$).*
5. ★ Find all zeros of $\cos z$ and of $\sin z$. *Answer: only the real ones, $\frac\pi2+k\pi$ and $k\pi$.*
6. ★ Show $\operatorname{Log}(z_1z_2)\ne\operatorname{Log}z_1+\operatorname{Log}z_2$ for $z_1=z_2=e^{3\pi i/4}$. *Answer: $\operatorname{Log}(z_1z_2)=-i\pi/2$ but $2\operatorname{Log}z_1=3\pi i/2$; they differ by $2\pi i$.*
7. ★ Show $\operatorname{Re}\cos(x+iy)=\cos x\cosh y$, $\operatorname{Im}=-\sin x\sinh y$; deduce $|\cos z|^2=\cos^2x+\sinh^2y$.
8. ✦ **Cut of $\sqrt{z^2-1}$.** Define $f(z)=\sqrt{z-1}\sqrt{z+1}$ using principal roots. Show $f$ is analytic off $[-1,1]$, behaves like $z$ at infinity, and **differs** from the principal value of $\sqrt{z^2-1}$ (which has extra cuts on the imaginary axis). *Check: at $z=-2+0.1i$, $f\approx-1.733+0.115i$ whereas the principal $\sqrt{z^2-1}\approx+1.733-0.115i$.*
9. ★ Show the integral $\oint_{|z|=1}\dfrac{dz}z=2\pi i$ proves $1/z$ has no single-valued antiderivative on $\mathbb C\setminus\{0\}$, and relate this to the cut of $\operatorname{Log}$.
10. ★ Derive $(\operatorname{Log}z)'=1/z$ from $e^{\operatorname{Log}z}=z$.
11. ◦ $\sinh(iy)=i\sin y$, $\cosh(iy)=\cos y$. Hence write $\sinh(x+iy)$.
12. ★ Where is $z^{1/2}$ (principal) discontinuous? Evaluate its limits at $-1\pm i0$. *Answer: on the negative real axis; $\pm i$.*

**Pitfalls.** Treating $\log$ like a real function; moving a branch cut without recomputing the function on the other side; losing a $2\pi i$.

---

## Module 4. Contour integrals and Cauchy's theorem (Week 3)

**Read:** Ávila Cap. 3 pp. 75 to 101 (contours p. 77, definition p. 79, invariance p. 81, properties p. 82, Cauchy via Green p. 89, primitives p. 93). **Drill:** Churchill ch. 4 (first half). **Time:** 4 h.

### Motivation

Everything that follows (Cauchy's formula, residues, Fourier-type integrals, Green functions) is contour integration plus one theorem: **if $f$ is analytic on and inside a closed contour, $\oint f\,dz=0$**. It is the complex version of "a conservative field does no work around a loop", and you already own the real version (Stewart 16.3, 16.4).

### Topics checklist

- **Contours:** smooth arcs $z(t)=x(t)+iy(t)$, $z'(t)\ne0$; piecewise smooth = *contour*; closed, simple closed (Jordan curve theorem, Ávila p. 77); orientation.
- **Definition:** $\int_C f\,dz=\int_a^b f(z(t))\,z'(t)\,dt=\int_C(u\,dx-v\,dy)+i\int_C(v\,dx+u\,dy)$. **Two real line integrals of the Stewart type.**
- **Properties:** linearity; reversal $\int_{-C}=-\int_C$; additivity; **independent of parametrisation** (Ávila p. 81) given orientation.
- **ML inequality:** $\left|\int_Cf\,dz\right|\le ML$ with $M=\max_C|f|$, $L$ the length. *The workhorse for discarding arcs.*
- **Fundamental theorem:** if $F'=f$ on a domain containing $C$, then $\int_Cf\,dz=F(b)-F(a)$. Hence $\oint f\,dz=0$ whenever $f$ has an antiderivative; but **$\oint dz/z=2\pi i\ne0$** shows $1/z$ has none on $\mathbb C\setminus\{0\}$.
- **Basic integral:** $\oint_{|z-a|=r}(z-a)^n\,dz=\begin{cases}2\pi i&n=-1\\0&n\neq-1\end{cases}$ (memorise; it generates everything).
- **Cauchy's theorem** (Ávila p. 89, via Green's theorem): if $f$ is analytic in a simply connected domain, then $\oint_Cf\,dz=0$ for every closed contour in it. (Goursat removes the assumption that $f'$ is continuous: state it, do not prove it.)
- **Deformation of contours:** if $C_1$ can be continuously deformed into $C_2$ through a region where $f$ is analytic, $\oint_{C_1}=\oint_{C_2}$; for **multiply connected domains**, cut to make it simply connected: $\oint_{\text{outer}}=\sum\oint_{\text{inner}}$.

### Own it

1. **Cauchy's theorem from Green's theorem.** Expand $\oint(u+iv)(dx+i\,dy)=\oint(u\,dx-v\,dy)+i\oint(v\,dx+u\,dy)$. Apply Green to each: $\iint(-v_x-u_y)\,dA+i\iint(u_x-v_y)\,dA$. **Both integrands vanish by CR.** *Do this by hand; it turns Cauchy's theorem into a corollary of something you own.*
2. $\oint z^n\,dz$ over a circle, for all integers $n$.
3. The ML bound and its use.
4. Contour deformation for an annulus.

### Exercises

1. ◦ $\oint_{|z|=1}\bar z\,dz$. *Answer: $2\pi i$ (not analytic, so no contradiction).*
2. ★ $\int_0^{1+i}z^2\,dz$ along (a) the straight segment, (b) $0\to1\to1+i$. *Answer: both $\frac{(1+i)^3}3=\frac{-2+2i}3$.*
3. ★ $\oint_{|z-a|=r}(z-a)^n\,dz$ for all integers $n$. *Answer: $2\pi i\,\delta_{n,-1}$.*
4. ★ $\int$ of $1/z$ from $1$ to $-1$ along the upper and lower unit semicircles. *Answer: $+i\pi$ and $-i\pi$; the difference $2\pi i$ is the loop integral.*
5. ★ $\oint_{|z|=2}\dfrac{dz}{z^2-1}$. *Answer: $0$ (partial fractions $\frac12[\frac1{z-1}-\frac1{z+1}]$ give $\frac12(2\pi i-2\pi i)$).*
6. ★ **ML estimate.** Show $\left|\oint_{|z|=R}\dfrac{dz}{z^2+1}\right|\le\dfrac{2\pi R}{R^2-1}\to0$. *Hint: $|z^2+1|\ge R^2-1$.*
7. ★ $\int_{i}^{1}e^{\pi z}\,dz$ (here $i$ is the lower limit; the path does not matter). *Answer: with $F=e^{\pi z}/\pi$, $[F]_i^1=\dfrac{e^{\pi}-e^{i\pi}}{\pi}=\dfrac{e^\pi+1}{\pi}\approx7.684$.*
8. ★ $\oint_{|z|=1}|z-1|\,|dz|$. *Answer: $8$ ($\int_0^{2\pi}2|\sin\frac\theta2|\,d\theta$).*
9. ★ Prove $\left|\int_C f\,dz\right|\le\int_C|f|\,|dz|$ and deduce the ML inequality.
10. ★ Square and circle: $\oint$ of $dz/z$ over the square with vertices $\pm1\pm i$ equals $2\pi i$. *Hint: deformation, or $\theta$-increment.*
11. ✦ **Green in disguise.** Show that for $f=u+iv$ with continuous partials, $\oint f\,dz=2i\iint\partial_{\bar z}f\,dA$. *Answer: this is Green's theorem in complex form; it vanishes iff CR (compare Module 2 exercise 12).*
12. ★ Integrate $f(z)=z\,\bar z$ over the unit circle (counterclockwise) and over the upper half circle from $1$ to $-1$ (use $z\bar z=1$ on the circle). *Answer: $0$ and $-2$.*

**Pitfalls.** Forgetting $z'(t)$; wrong orientation; using Cauchy's theorem when a singularity sits inside the contour.

---

## Module 5. Cauchy's integral formula and its consequences (Week 4)

**Read:** Ávila Cap. 3 pp. 101 to 109 (formula p. 101, derivatives p. 103); maximum modulus on p. 113 is in the optional Module 10 but its *statement* belongs here. **Drill:** Churchill ch. 4 (second half). **Time:** 3 to 4 h.

### Motivation

$$f(z_0)=\frac1{2\pi i}\oint_C\frac{f(z)}{z-z_0}\,dz.$$
The values of an analytic function on a closed contour **determine it everywhere inside**. Nothing in real analysis behaves like this, and it has startling corollaries: analytic functions are automatically infinitely differentiable; bounded entire functions are constant; harmonic functions satisfy the mean-value property and have **no interior extrema** (the mathematics behind Earnshaw's theorem and Jackson's mean-value theorem for the potential).

### Topics checklist

- **Cauchy integral formula (CIF)** and its proof (deform $C$ to a tiny circle around $z_0$, then ML).
- **Derivatives:** $f^{(n)}(z_0)=\dfrac{n!}{2\pi i}\oint\dfrac{f(z)}{(z-z_0)^{n+1}}dz$ ⇒ analytic functions are infinitely differentiable (Ávila p. 103).
- **Cauchy estimates:** $|f^{(n)}(z_0)|\le n!\,M/r^n$.
- **Liouville's theorem:** bounded entire ⇒ constant. **Fundamental theorem of algebra** as a corollary.
- **Mean-value property:** $f(z_0)=\frac1{2\pi}\int_0^{2\pi}f(z_0+re^{i\theta})\,d\theta$; applied to $u=\operatorname{Re}f$: **harmonic functions equal their circular averages**.
- **Maximum modulus principle** (Ávila p. 113): a non-constant analytic function on a domain has no interior maximum of $|f|$; consequently a **harmonic function has no interior maximum or minimum** (Earnshaw: no stable electrostatic equilibrium in free space).
- (State only) **Morera's theorem** (converse of Cauchy).

### Own it

1. CIF from Cauchy's theorem + the circle integral.
2. How the derivative formula follows (differentiate under the integral).
3. Liouville ⇒ FTA.
4. Mean value ⇒ no interior maximum.

### Exercises

1. ◦ $\oint_{|z|=2}\dfrac{e^z}{z-1}\,dz$. *Answer: $2\pi ie\approx17.079\,i$.*
2. ★ $\oint_{|z|=2}\dfrac{e^z}{z^3}\,dz$. *Answer: $\dfrac{2\pi i}{2!}=\pi i$.*
3. ★ $\oint_{|z|=1}\dfrac{\sin z}{z^2}\,dz$. *Answer: $2\pi i\cos0=2\pi i$.*
4. ★ $\oint_{|z|=2}\dfrac{dz}{z^2+1}$. *Answer: $0$ (residues $\pm\frac1{2i}$ cancel).*
5. ★ **A real integral from CIF.** From $\oint_{|z|=1}\frac{e^z}z\,dz=2\pi i$ derive $\int_0^{2\pi}e^{\cos\theta}\cos(\sin\theta)\,d\theta=2\pi$. *Answer: parametrize $z=e^{i\theta}$, take the real part.*
6. ★ Verify the mean-value property for $f=e^z$ at $z_0=0$: $\frac1{2\pi}\int_0^{2\pi}e^{re^{i\theta}}\,d\theta=1$ for every $r$.
7. ★ Prove Liouville from Cauchy's estimate with $n=1$; then prove that every non-constant polynomial has a root.
8. ★ Show that $|f|$ cannot have a strict interior local maximum; apply it to $f=e^z$ on the closed disc $|z|\le1$ (where is the maximum?). *Answer: on the boundary at $z=1$, $\max|e^z|=e$.*
9. ✦ **Earnshaw.** Let $\Phi$ be harmonic in a region free of charge. Use the mean-value property to show $\Phi$ has no local minimum or maximum, hence a test charge cannot sit in stable electrostatic equilibrium. *(2D version via analytic functions; the 3D version is Jackson's.)*
10. ★ Evaluate $\oint_{|z|=3}\dfrac{\cos z}{z(z-2)(z+i)}\,dz$ with partial fractions or three CIFs (all three poles $0,2,-i$ are inside). *Answer: $2\pi i\Big[\dfrac i2+\dfrac{\cos2}{2(2+i)}+\dfrac{\cosh1}{i(i+2)}\Big]\approx0.4751-2.4620\,i$ (checked numerically).*

**Pitfalls.** Applying CIF when $f$ is not analytic inside; mixing $n!$ and $(n-1)!$; forgetting that Liouville needs *entire*.

---

## Module 6. Taylor and Laurent series (Week 5)

**Read:** Ávila Cap. 4 pp. 118 to 150 (convergence p. 120, power series p. 127, Taylor p. 133, products/quotients p. 138, **Laurent p. 144**, infinity and zeros p. 147). **Drill:** Churchill ch. 5. **Time:** 4 h. **Needs Stewart ch. 11 first.**

### Motivation

A Taylor series has only non-negative powers. A **Laurent series** allows negative ones and converges in an **annulus**, because the centre may itself be a singularity: $f(z)=\sum_{n=-\infty}^{\infty}a_n(z-z_0)^n$. The coefficient $a_{-1}$ is the **residue**, and the next two modules are built on it. Also: the radius of convergence of a Taylor series is the distance to the nearest singularity *in the complex plane*, which explains why $1/(1+x^2)$ has a series that fails at $|x|=1$ although it is smooth on the real line.

### Topics checklist

- **Series of complex numbers:** absolute convergence ⇒ convergence; geometric series $\sum z^n=\frac1{1-z}$ for $|z|<1$.
- **Uniform convergence** and the Weierstrass M-test; uniformly convergent series of continuous functions can be integrated termwise (Ávila p. 120).
- **Power series:** radius of convergence $R$ (ratio and root tests); analytic inside $|z-z_0|<R$; can be differentiated and integrated termwise.
- **Taylor's theorem** (Ávila p. 133): if $f$ is analytic in $|z-z_0|<R$ then $f=\sum\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n$ there; $R$ is the distance to the nearest singularity. Coefficients $a_n=\frac1{2\pi i}\oint\frac{f}{(z-z_0)^{n+1}}dz$.
- **Standard series to know:** $e^z$, $\sin z$, $\cos z$, $\sinh z$, $\cosh z$ (entire), $\frac1{1-z}$, $\operatorname{Log}(1+z)$ ($|z|<1$), $(1+z)^a$.
- **Operations** (p. 138): sum, product (Cauchy product), quotient, composition, differentiation, integration.
- **Laurent's theorem** (p. 144): $f$ analytic in the annulus $r_1<|z-z_0|<r_2$ ⇒ unique expansion with $a_n=\frac1{2\pi i}\oint\frac{f(z)}{(z-z_0)^{n+1}}dz$. **Different annuli give different Laurent series for the same function** (Exercise 3).
- **Zeros** (p. 147): $f(z_0)=0$ with $f$ analytic ⇒ $f=(z-z_0)^mg(z)$, $g(z_0)\ne0$ (**order $m$**); zeros are isolated unless $f\equiv0$ (identity theorem: state it).
- **Behaviour at infinity** (p. 147): substitute $z=1/w$.

### Own it

1. Radius of convergence = distance to nearest singularity (explain $1/(1+z^2)$).
2. Laurent series of $1/((z-1)(z-2))$ in all three regions.
3. Why the Laurent series is unique in a given annulus.
4. How to read off the order of a zero from the Taylor series.

### Exercises

1. ◦ Radius of convergence of $\sum z^n/n!$, $\sum n!\,z^n$, $\sum z^n/n$, $\sum z^{2n}$. *Answer: $\infty$, $0$, $1$, $1$.*
2. ★ Why does the Taylor series of $\frac1{1+x^2}$ about $0$ have radius $1$? What is the radius about $x_0=1$? *Answer: nearest singularities $\pm i$: distance $1$ from $0$ and $\sqrt2$ from $1$.*
3. ★ **The classic.** Laurent series of $f(z)=\dfrac1{(z-1)(z-2)}$ about $0$ in (a) $|z|<1$, (b) $1<|z|<2$, (c) $|z|>2$. *Answer: partial fractions $f=\frac1{z-2}-\frac1{z-1}$. (a) $\sum_{n\ge0}(1-2^{-n-1})z^n$; (b) $-\sum_{n\ge0}\frac{z^n}{2^{n+1}}-\sum_{n\ge1}z^{-n}$; (c) $\sum_{n\ge1}(2^{n-1}-1)z^{-n}$.*
4. ★ Laurent series of $e^{1/z}$ about $0$. Residue? *Answer: $\sum_{n\ge0}\frac{z^{-n}}{n!}$; $a_{-1}=1$; infinitely many negative powers (essential singularity).*
5. ★ First terms of $\dfrac1{\sin z}$ at $0$. *Answer: $\frac1z+\frac z6+\frac{7z^3}{360}+\cdots$; residue $1$.*
6. ★ Taylor series of $\dfrac z{e^z-1}$. *Answer: $1-\frac z2+\frac{z^2}{12}-\frac{z^4}{720}+\cdots$ (Bernoulli numbers); removable singularity at $0$, radius $2\pi$.*
7. ★ Order of the zero at $0$ of $\sin z-z$, $1-\cos z$, $e^z-1-z$. *Answer: $3$, $2$, $2$.*
8. ★ Use the Cauchy product to verify $e^ze^{-z}=1$ to order $z^4$.
9. ★ Find the radius of convergence of the Taylor series of $\tan z$ at $0$. *Answer: $\pi/2$ (nearest pole).*
10. ★ Expand $\dfrac1z$ in a Taylor series about $z_0=1$; radius? *Answer: $\sum(-1)^n(z-1)^n$, $R=1$.*
11. ✦ **Physics.** The oscillator response $\chi(\omega)=\dfrac1{\omega_0^2-\omega^2}$: expand for $|\omega|<\omega_0$ and for $|\omega|>\omega_0$. Interpret each as a quasi-static vs high-frequency limit. *Answer: $\frac1{\omega_0^2}\sum(\omega/\omega_0)^{2n}$; $-\frac1{\omega^2}\sum(\omega_0/\omega)^{2n}$.*
12. ★ Compute $\oint_{|z|=1}\dfrac{dz}{\sin z}$ using the series. *Answer: $2\pi i$.*

**Pitfalls.** Expanding in the wrong annulus; confusing the radius of convergence at different centres; assuming the Laurent series converges at the singularity.

---

## Module 7. Singularities and the residue theorem (Week 6)

**Read:** Ávila Cap. 5 pp. 151 to 161 (isolated singularities p. 151; removable p. 152; pole p. 153; essential p. 154; residue theorem p. 157). **Drill:** Churchill ch. 6. **Time:** 4 h.

### Motivation

The residue theorem turns contour integrals into algebra:
$$\oint_Cf\,dz=2\pi i\sum_k\operatorname{Res}(f,z_k).$$
It is the engine of Jackson's Green-function calculations and of QFT propagators. The classification of singularities also carries physics: **poles are stable states, branch cuts are continua**.

### Topics checklist

- **Isolated singularity** $z_0$: $f$ analytic in a punctured disc. Branch points are *not* isolated singularities.
- **Classification by the principal part** (negative powers of the Laurent series):
  - **removable**: none ($\lim f$ exists; define $f(z_0)$ to fix it);
  - **pole of order $m$**: down to $(z-z_0)^{-m}$ ($|f|\to\infty$); equivalently $1/f$ has a zero of order $m$;
  - **essential**: infinitely many (Casorati-Weierstrass: $f$ comes arbitrarily close to *every* complex value near $z_0$).
- **Residue:** $\operatorname{Res}(f,z_0)=a_{-1}$; $\oint f\,dz=2\pi i\,a_{-1}$ on a small circle.
- **Residue theorem** (p. 157): $f$ analytic on and inside $C$ except at finitely many $z_k$ inside ⇒ $\oint_Cf=2\pi i\sum\operatorname{Res}$.
- **How to compute residues** (memorise):
  - simple pole: $\operatorname{Res}=\lim_{z\to z_0}(z-z_0)f(z)$;
  - $f=g/h$ with $h(z_0)=0$, $h'(z_0)\ne0$: $\operatorname{Res}=g(z_0)/h'(z_0)$;
  - pole of order $m$: $\operatorname{Res}=\dfrac1{(m-1)!}\lim_{z\to z_0}\dfrac{d^{m-1}}{dz^{m-1}}\big[(z-z_0)^mf(z)\big]$;
  - essential singularities: read off $a_{-1}$ from the series.
- **Sum of residues:** if $f$ decays faster than $1/z$ at infinity, the sum of *all* finite residues is $0$ (Exercise 8).

### Own it

1. The three types by Laurent structure, one example each.
2. The three residue formulas, and a proof of the $g/h$ formula.
3. Residue theorem from the deformation argument (small circles around each pole).

### Exercises

1. ◦ Classify $z=0$ for $\frac{\sin z}z$, $\frac1{z^2}$, $e^{1/z}$, $\frac{1-\cos z}{z^2}$. *Answer: removable (value $1$), pole of order 2, essential, removable (value $\frac12$).*
2. ★ $\operatorname{Res}\dfrac1{z^2+1}$ at $z=i$. *Answer: $\dfrac1{2i}=-\dfrac i2$.*
3. ★ $\operatorname{Res}\dfrac{e^z}{z^3}$ at $0$. *Answer: $\frac12$.*
4. ★ $\operatorname{Res}\dfrac1{\sin z}$ at $z=n\pi$. *Answer: $(-1)^n$.*
5. ★ $\operatorname{Res}\cot z$ at $n\pi$. *Answer: $1$.*
6. ★ $\oint_{|z|=3}\dfrac{z+1}{z^2(z-2)}\,dz$. *Answer: $0$ (residues $-\frac34$ at $0$ and $+\frac34$ at $2$).*
7. ★ Residues of $\dfrac{1}{z^4+1}$ at the four poles $e^{i\pi/4+ik\pi/2}$; show they sum to $0$. *Answer: $\operatorname{Res}=\frac1{4z_k^3}=-\frac{z_k}4$; the sum of the four roots is $0$.*
8. ★ Show: if $f=P/Q$ with $\deg Q\ge\deg P+2$, the sum of all residues is $0$. *Hint: $\oint_{|z|=R}f\to0$ by the ML bound.*
9. ★ $\oint_{|z|=2}\dfrac{e^z}{z^2(z+1)}\,dz$. *Answer: the residue at $0$ is $\dfrac d{dz}\dfrac{e^z}{z+1}\Big|_0=0$ and at $-1$ it is $e^{-1}$, so the integral is $2\pi i/e\approx2.3115\,i$.*
10. ✦ **Damped oscillator poles.** Find the poles of $\chi(\omega)=\dfrac1{\omega_0^2-\omega^2-i\gamma\omega}$ and their residues. *Answer: $\omega_\pm=-\frac{i\gamma}2\pm\Omega$, $\Omega=\sqrt{\omega_0^2-\gamma^2/4}$: both in the **lower half-plane**; $\operatorname{Res}_{\omega_\pm}=\mp\dfrac1{2\Omega}$.*
11. ★ Why is $z=0$ a non-isolated singularity of $\operatorname{Log}z$? Why does the residue theorem not apply? *Answer: the cut accumulates; no punctured disc on which $\operatorname{Log}$ is single-valued and analytic.*
12. ★ Find the residue of $\dfrac{e^{iz}}{(z^2+1)^2}$ at $z=i$ (pole of order 2). *Answer: $\dfrac d{dz}\dfrac{e^{iz}}{(z+i)^2}\Big|_{z=i}=\dfrac{e^{iz}\,[\,i(z+i)-2\,]}{(z+i)^3}\Big|_{z=i}=\dfrac{e^{-1}(-4)}{(2i)^3}=-\dfrac{i}{2e}\approx-0.1839\,i$.*

**Pitfalls.** Counting residues outside the contour; wrong order $m$ in the derivative formula; applying the residue theorem at a branch point.

---

## Module 8. Real integrals by residues; Jordan's lemma; principal values (Week 7)

**Read:** Ávila Cap. 5 pp. 161 to 169 (rational integrals p. 161, **Jordan's lemma p. 164**), 173 (trig integrals). **Drill:** Churchill ch. 7 (improper integrals, Fourier-type integrals, Jordan's lemma, indented paths, trig integrals). **Time:** 4 to 5 h. **Do many exercises; this is the one set where volume matters.**

### Motivation

This is the week the track exists for. Everything before was prerequisite. Jordan's lemma is the theorem that licenses discarding the big arc when the integrand carries $e^{iax}$, which is the form of a Fourier transform and of the retarded Green function integral.

### Topics checklist

- **(A) Trigonometric integrals** $\int_0^{2\pi}R(\cos\theta,\sin\theta)\,d\theta$: set $z=e^{i\theta}$, $\cos\theta=\frac{z+1/z}2$, $\sin\theta=\frac{z-1/z}{2i}$, $d\theta=dz/(iz)$.
- **(B) Rational functions** $\int_{-\infty}^\infty R(x)\,dx$, $\deg Q\ge\deg P+2$: close in the upper half-plane with an arc $C_R$; ML shows the arc vanishes; the answer is $2\pi i\sum\operatorname{Res}$ in the UHP.
- **(C) Fourier-type** $\int_{-\infty}^\infty R(x)\,e^{iax}\,dx$ ($a>0$), $R\to0$:
  - **Jordan's lemma:** if $f(z)\to0$ uniformly as $|z|\to\infty$ in the upper half-plane, then $\int_{C_R}f(z)e^{iaz}\,dz\to0$ for $a>0$. *Proof idea:* $|e^{iaz}|=e^{-aR\sin\theta}$ and $\sin\theta\ge2\theta/\pi$ on $[0,\pi/2]$, so $\int_0^\pi e^{-aR\sin\theta}d\theta<\pi/(aR)$.
  - **Which half-plane:** $e^{iax}$ decays in the UHP for $a>0$ and in the LHP for $a<0$. *Closing the wrong way gives a divergent arc.* In physics, the sign of $a$ is the sign of $t$ in $e^{-i\omega t}$.
- **(D) Poles on the real axis:** **indent** the contour with a small semicircle of radius $\varepsilon$ around the pole. A small arc of angle $\alpha$ around a simple pole contributes $i\alpha\operatorname{Res}$ (counterclockwise): a half-circle gives $\pm i\pi\operatorname{Res}$. The remaining straight pieces define the **Cauchy principal value**:
$$\mathrm{P}\!\!\int_{-\infty}^\infty f\,dx=\lim_{\varepsilon\to0}\left(\int_{-\infty}^{x_0-\varepsilon}+\int_{x_0+\varepsilon}^{\infty}\right)f\,dx.$$
**Which way you indent is a choice, and the two choices differ by $2\pi i\operatorname{Res}$; that difference is the whole retarded-vs-advanced story.**
- **(E) Sokhotski-Plemelj:** for $\varepsilon\to0^+$ and smooth test functions,
$$\frac1{x\mp i\varepsilon}\;\longrightarrow\;\mathrm{P}\frac1x\pm i\pi\,\delta(x).$$
(Derive it from (D).) *The $i\varepsilon$ in propagators is exactly this.*
- **(F) Two named tricks:** the Gaussian integral $\int e^{-ax^2+ibx}\,dx=\sqrt{\pi/a}\,e^{-b^2/4a}$ by shifting the contour; the Fresnel integrals by a wedge contour.

### Own it

1. Jordan's lemma, statement and the $\sin\theta\ge2\theta/\pi$ proof.
2. $\int_{-\infty}^\infty\dfrac{e^{iax}}{x^2+b^2}dx$ for $a>0$ and $a<0$.
3. The half-circle indentation lemma and Sokhotski-Plemelj.
4. $\int_0^\infty\frac{\sin x}{x}dx=\frac\pi2$.

### Exercises

*(All answers verified numerically; see Appendix D.)*

1. ◦ $\displaystyle\int_{-\infty}^\infty\frac{dx}{1+x^2}$. *Answer: $\pi$ (residue $\frac1{2i}$ at $i$, times $2\pi i$).*
2. ★ $\displaystyle\int_{-\infty}^\infty\frac{dx}{(x^2+a^2)^2}$. *Answer: $\dfrac{\pi}{2a^3}$.*
3. ★ $\displaystyle\int_0^\infty\frac{dx}{x^4+1}$. *Answer: $\dfrac{\pi}{2\sqrt2}\approx1.1107$.*
4. ★ $\displaystyle\int_{-\infty}^\infty\frac{x^2}{x^4+1}\,dx$. *Answer: $\dfrac\pi{\sqrt2}\approx2.2214$.*
5. ★ $\displaystyle\int_{-\infty}^\infty\frac{dx}{x^6+1}$. *Answer: $\dfrac{2\pi}3$. (General: $\int_{-\infty}^\infty\frac{dx}{1+x^{2n}}=\frac{\pi}{n\sin(\pi/2n)}$.)*
6. ★ $\displaystyle\int_0^\infty\frac{dx}{(x^2+1)^2}$. *Answer: $\dfrac\pi4$.*
7. ★ $\displaystyle\int_0^{2\pi}\frac{d\theta}{5+4\cos\theta}$. *Answer: $\dfrac{2\pi}3$ (general $\frac{2\pi}{\sqrt{a^2-b^2}}$).*
8. ★ $\displaystyle\int_0^\infty\frac{\cos x}{x^2+1}\,dx$. *Answer: $\dfrac\pi{2e}\approx0.5779$.*
9. ★ $\displaystyle\int_{-\infty}^\infty\frac{\cos\omega x}{x^2+a^2}\,dx$ ($a>0$). *Answer: $\dfrac\pi a\,e^{-|\omega|a}$.*
10. ★ $\displaystyle\int_{-\infty}^\infty\frac{x\sin x}{x^2+4}\,dx$. *Answer: $\pi e^{-2}\approx0.4252$.*
11. ★ $\displaystyle\int_0^\infty\frac{\sin x}x\,dx$ (indent at $0$, use $e^{iz}/z$). *Answer: $\dfrac\pi2$.*
12. ★ $\displaystyle\mathrm{P}\!\!\int_{-\infty}^\infty\frac{\cos x}{x^2-1}\,dx$. *Answer: $-\pi\sin1\approx-2.6436$. (Use $\mathrm{P}\!\int\frac{e^{ix}}{x-a}dx=i\pi e^{ia}$ and partial fractions.)*
13. ★ $\displaystyle\int_{-\infty}^\infty e^{-2x^2}\cos3x\,dx$. *Answer: $\sqrt{\pi/2}\,e^{-9/8}\approx0.4069$ (shift $x\to x+3i/4$).*
14. ✦ **Fresnel.** $\displaystyle\int_0^\infty\sin(x^2)\,dx=\int_0^\infty\cos(x^2)\,dx=\frac12\sqrt{\frac\pi2}$. *Answer: $\sqrt{\pi/8}\approx0.6267$ (wedge of angle $\pi/4$, then Gaussian).*
15. ★ **Sokhotski numerically.** For $f(x)=e^{-x^2}$ and $\varepsilon=10^{-3}$, compute $\int\frac{f(x)}{x-i\varepsilon}dx$. *Answer: $\approx i\pi f(0)=3.14159\,i$ (the principal part vanishes by oddness; you get $3.138\,i$ at this $\varepsilon$).*
16. ✦ Show that the indentation above vs below the pole $x_0$ of $\int\frac{e^{iax}}{x-x_0}dx$ ($a>0$) gives $\mathrm P\!\!\int\pm i\pi e^{iax_0}$, so the two prescriptions differ by $2\pi i\,\operatorname{Res}=2\pi ie^{iax_0}$.

**Pitfalls.** Wrong half-plane (check the sign of the exponent); forgetting the factor $\frac12$ for a half-circle around a pole on the axis; claiming Jordan's lemma when $f\not\to0$; computing a principal value as an ordinary improper integral.

---

## Module 9. Capstone: Green functions, causality and Kramers-Kronig (Week 8)

**Read/do:** no new chapter; Ávila pp. 157 to 169 *cold*, Churchill ch. 7 (indented paths). **Time:** 4 to 5 h plus the gate. **If you do one thing from this document, do this.**

### Motivation

The damped oscillator is a one-variable laboratory for exactly what Jackson does in 3+1 dimensions:

$$\ddot x+\gamma\dot x+\omega_0^2x=F(t),\qquad x(t)=\int G(t-t')F(t')\,dt',\qquad \tilde G(\omega)=\frac1{\omega_0^2-\omega^2-i\gamma\omega}.$$

With the physics convention $G(t)=\int\frac{d\omega}{2\pi}e^{-i\omega t}\tilde G(\omega)$, the poles are in the **lower** half-plane; for $t<0$ you must close in the **upper** half-plane (where $e^{-i\omega t}$ decays), find **no poles**, and get $G=0$. **Causality $\Leftrightarrow$ no poles in the upper half-plane.**

### Part A. The retarded Green function of the damped oscillator

1. Poles: $\omega_\pm=-\frac{i\gamma}2\pm\Omega$, $\Omega=\sqrt{\omega_0^2-\gamma^2/4}$ (assume $\gamma<2\omega_0$).
2. For $t>0$ close in the LHP ($e^{-i\omega t}$ decays for $\operatorname{Im}\omega<0$); Jordan's lemma applies ($\tilde G\to0$). Residues: $\operatorname{Res}_{\omega_\pm}\tilde G=\mp\dfrac1{2\Omega}$ ($\tilde G=-\dfrac1{(\omega-\omega_+)(\omega-\omega_-)}$).
3. Result (clockwise, so $-2\pi i$): 
$$G(t)=\theta(t)\,e^{-\gamma t/2}\,\frac{\sin\Omega t}{\Omega}.$$
**Check this numerically** (Appendix D): at $\omega_0=1$, $\gamma=0.5$, $t=1.7$ the direct integral gives $0.67330$ and the formula gives $0.67330$.

### Part B. From damping to $i\varepsilon$: three prescriptions

Take $\gamma\to0$. The poles reach the real axis at $\pm\omega_0$ and the integral is undefined; the damping tells you *which side*. Define

$$G_{\rm ret}(t)=\int\frac{d\omega}{2\pi}\frac{e^{-i\omega t}}{\omega_0^2-(\omega+i0)^2},\quad G_{\rm adv}(t)=\int\frac{d\omega}{2\pi}\frac{e^{-i\omega t}}{\omega_0^2-(\omega-i0)^2},\quad G_F(t)=\int\frac{d\omega}{2\pi}\frac{e^{-i\omega t}}{\omega_0^2-\omega^2-i0}.$$

Results (derive each by closing the contour; all verified):

- **Retarded** (both poles below the axis): $G_{\rm ret}=\theta(t)\,\dfrac{\sin\omega_0t}{\omega_0}$.
- **Advanced** (both poles above): $G_{\rm adv}=-\theta(-t)\,\dfrac{\sin\omega_0t}{\omega_0}$.
- **Feynman** (positive-frequency pole below, negative above): $G_F=\dfrac i{2\omega_0}\,e^{-i\omega_0|t|}$.

**Physical meaning.** Retarded: response only after the force. Advanced: response before (acausal, mathematically allowed). Feynman: positive-frequency waves propagate forward in time, negative-frequency backward: the QFT time-ordered propagator.

### Part C. Kramers-Kronig

1. **Causality ⇒ analyticity.** $\chi(\omega)=\int_0^\infty G(t)e^{i\omega t}\,dt$ (note: only $t>0$) is analytic for $\operatorname{Im}\omega>0$ and, for a decent response function, $\chi\to0$ as $|\omega|\to\infty$.
2. **Cauchy + indentation.** Apply CIF to $\chi(\omega')/(\omega'-\omega)$ on a large semicircle in the UHP with a small indentation above the real point $\omega$ (arc vanishes by Jordan/decay):
$$\chi(\omega)=\frac1{i\pi}\,\mathrm P\!\!\int_{-\infty}^\infty\frac{\chi(\omega')}{\omega'-\omega}\,d\omega'.$$
3. **Real and imaginary parts** (with $\chi(-\omega^*)=\chi(\omega)^*$ for a real response):
$$\operatorname{Re}\chi(\omega)=\frac1\pi\mathrm P\!\!\int_{-\infty}^\infty\frac{\operatorname{Im}\chi(\omega')}{\omega'-\omega}\,d\omega',\qquad \operatorname{Im}\chi(\omega)=-\frac1\pi\mathrm P\!\!\int_{-\infty}^\infty\frac{\operatorname{Re}\chi(\omega')}{\omega'-\omega}\,d\omega'.$$
4. **Numerical test** (Appendix D): $\omega_0=1,\gamma=0.5,\omega=0.7$ gives $\operatorname{Re}\chi=1.33298$ directly and $1.33298$ from the principal-value integral of $\operatorname{Im}\chi$.

### Exercises

1. ★ Derive Part A completely, including the justification of the arc, and plot $G(t)$ for $\gamma/\omega_0=0.1,0.5,1.9$. What happens at $\gamma=2\omega_0$ (critical damping)? *Answer: $\Omega\to0$ and $G\to\theta(t)\,te^{-\gamma t/2}$; beyond that $\Omega$ is imaginary and the poles lie on the negative imaginary axis.*
2. ★ For $t<0$ in Part A, show the contour closes in the UHP, encloses nothing, and $G(t)=0$.
3. ★ Derive the three prescriptions of Part B. *Hint for Feynman: pole at $+\omega_0-i0$ is enclosed when closing below ($t>0$), pole at $-\omega_0+i0$ when closing above ($t<0$).*
4. ★ Show $G_{\rm ret}-G_{\rm adv}=\dfrac{\sin\omega_0t}{\omega_0}$ for all $t$ and relate it to the residue theorem. *Answer: the two contours differ by a closed contour around both poles.*
5. ★ Prove the Kramers-Kronig relations from $\chi$ analytic in the UHP and $\chi\to0$ at infinity; where exactly is Jordan's lemma (or decay) used?
6. ★ Use KK to show $\chi(0)=\dfrac2\pi\int_0^\infty\dfrac{\operatorname{Im}\chi(\omega')}{\omega'}\,d\omega'$ for a real response. Check for the damped oscillator ($\chi(0)=1/\omega_0^2$).
7. ✦ **A causality test.** Show that $\chi(\omega)=\dfrac1{\omega_0^2-\omega^2+i\gamma\omega}$ (sign flipped) has its poles in the **upper** half-plane and therefore corresponds to the *advanced* (acausal) response: it fails KK.
8. ✦ **Keep the page.** Write a one-page note, no equations beyond three lines, explaining why "$i\varepsilon$" is a physical boundary condition and not a regularisation trick, and how the poles' positions encode retarded/advanced/Feynman. This is the sentence you will reuse in Jackson and QFT.

---

## Module 10 (optional). Harmonic functions, maximum modulus, Dirichlet and Neumann

**Read:** Ávila Cap. 3 pp. 109 to 117 (harmonic functions p. 109, a harmonic function determines an analytic function p. 111, multiply connected regions p. 112, maximum modulus p. 113, Dirichlet and Neumann p. 114). **Drill:** Churchill ch. 2 and 4. **Time:** 2 to 3 h. **Why optional:** Jackson teaches this itself, in 3D; this is a free *preview*, not a prerequisite.

**Topics.** Harmonic conjugates on simply connected domains; the Poisson integral and mean-value property; maximum/minimum principles; uniqueness for the Dirichlet problem (the difference of two solutions is harmonic with zero boundary values, hence zero), and for Neumann (up to a constant).

**Exercises**

1. ★ Prove uniqueness of the Dirichlet problem on a bounded domain from the maximum principle.
2. ★ Find the harmonic function in the unit disc with boundary value $\cos2\theta$. *Answer: $r^2\cos2\theta$.*
3. ★ Show $\Phi=\operatorname{Re}\,(a+bz^2)$ cannot have a maximum inside any charge-free disc. *Answer: harmonic.*
4. ✦ Explain how this is Jackson's uniqueness theorem and Earnshaw in two dimensions.
5. ★ Find a harmonic function on the half plane $y>0$ with boundary value $1$ for $|x|<1$, $0$ otherwise. *Answer: $\frac1\pi[\arg(z-1)-\arg(z+1)]$.*

---

## Module 11 (optional). Multivalued integrands: keyhole contours

**Read:** Ávila Cap. 5 pp. 169 to 173. **Drill:** Churchill ch. 7 (integrals involving branch cuts, if present in your edition). **Time:** 2 to 3 h. **Why optional:** not needed for Jackson's early Green functions; needed later for QFT propagators with cuts.

**Method.** For $\int_0^\infty x^{a-1}R(x)\,dx$ use a **keyhole** around the positive real axis with the branch of $z^{a-1}$ chosen so that $\arg z=0$ above the axis and $2\pi$ below; the two sides differ by the factor $e^{2\pi i(a-1)}$, so $(1-e^{2\pi ia})\int_0^\infty=2\pi i\sum\operatorname{Res}$ (small and large arcs vanish by ML).

**Exercises**

1. ★ $\displaystyle\int_0^\infty\frac{x^{a-1}}{1+x}\,dx=\frac\pi{\sin\pi a}$, $0<a<1$. *Answer: check $a=\frac13$: $\frac\pi{\sin(\pi/3)}=3.6276$.*
2. ★ $\displaystyle\int_0^\infty\frac{dx}{x^3+1}$. *Answer: $\dfrac{2\pi}{3\sqrt3}\approx1.2092$.*
3. ★ $\displaystyle\int_0^\infty\frac{\sqrt x}{x^2+1}\,dx$. *Answer: $\dfrac\pi{\sqrt2}\approx2.2214$.*
4. ✦ Explain why a cut contributes a *continuum* (an integral over the discontinuity) while a pole contributes a *discrete* term, in terms of the discontinuity across the cut.
5. ★ Sketch the keyhole and say which arcs vanish and why.

---

## Appendix A. Parked: non-standard topics for a later thread

*Not needed for Goldstein or Jackson now. When you want them, start here.*

| Topic | Ávila pages | Why you might want it later |
| --- | --- | --- |
| Analytic continuation (by chains, by reflection) | Cap. 6, 183 to 192 | pure function theory |
| **Riemann surfaces** | Cap. 6, 193 to 197 | the honest picture of a branch cut; makes multivaluedness geometric |
| **Gamma function and continuation to the whole plane** | Cap. 6, 200 to 202 | the conceptual seed of dimensional regularization in QFT |
| **Argument principle, logarithmic residues, Rouché** | Cap. 5, 175 to 178 | counting zeros and poles; stability (Nyquist), dispersion theory |
| Irrotational flows, potential functions, sources and sinks | Cap. 7, 209 to 220 | same mathematics as 2D electrostatics; good for intuition |
| Kutta-Joukowski, Joukowski profile | Cap. 7, 226 to 244 | aerodynamics |
| **Conformal mapping**: invariance of Laplace's equation, electrostatic potential | Cap. 8, 248, 260 to 265 | 2D boundary-value problems solved a second way; Jackson ch. 2 overlap (**highest-value parked item**) |
| Möbius maps, cross ratio, inversion | Cap. 8, 249 to 259 | geometry |
| Steepest descent, asymptotics; Bromwich inversion; Schwarz-Christoffel | Churchill ch. 7, 11 and beyond | later |

---

## Appendix B. The gate (blank page, unrushed)

The bar is reconstruction, not speed.

1. State CR; derive them from direction-independence; show $u,v$ are harmonic.
2. Prove Cauchy's theorem from Green's theorem, expanding $\oint(u+iv)(dx+i\,dy)$.
3. State and use CIF; say in one sentence why it has no real-variable analogue.
4. Write a Laurent series; classify the three singularity types; give one example of each.
5. State the residue theorem; compute residues at a simple pole and at a pole of order 2.
6. **Evaluate $\int_{-\infty}^\infty\frac{dx}{1+x^2}$ by residues,** justifying the arc.
7. **State Jordan's lemma, prove it, and say which half-plane for each sign of the exponent.**
8. **Explain why $\int\frac{e^{-i\omega t}}{\omega^2-\omega_0^2}d\omega$ is undefined until you choose a prescription; derive $G_{\rm ret}$, $G_{\rm adv}$, $G_F$ and say what boundary condition each encodes.**
9. Derive the Kramers-Kronig relations from analyticity in the upper half-plane.
10. State what a branch cut is and why $\log z$ needs one.
11. State the maximum modulus principle and its consequence for harmonic functions; connect it to Earnshaw.
12. State and derive Sokhotski-Plemelj.

**Timed trio (45 minutes, closed book).** (a) $\int_{-\infty}^\infty\frac{\cos x}{x^2+9}dx=\frac\pi3e^{-3}$; (b) $\int_0^{2\pi}\frac{d\theta}{3+2\cos\theta}=\frac{2\pi}{\sqrt5}$; (c) $\mathrm P\!\!\int_{-\infty}^\infty\frac{\sin x}{x(x^2+1)}dx=\pi(1-e^{-1})$. *(All verified.)*

Items 6, 7, 8 and 9 are the ones that matter; item 8 is the Jackson green-function week.

---

## Appendix C. Cheat-sheet contents

One page (write it yourself):

- CR (Cartesian and polar); $f'=u_x+iv_x$; Wirtinger form.
- $e^z$, $\operatorname{Log}z$, $z^a$ definitions; cut and jump.
- $\oint(z-a)^n\,dz=2\pi i\,\delta_{n,-1}$; ML inequality; deformation.
- CIF and derivatives; Liouville; mean value; maximum modulus.
- Standard series; Laurent coefficient formula; zero and pole orders.
- Residue formulas: simple, $g/h$, order $m$.
- Jordan's lemma statement and half-plane rule; half-residue for indentation.
- Sokhotski-Plemelj; the three Green-function prescriptions with results.
- KK relations.
- The table of integrals: $\frac\pi a e^{-|\omega|a}$; $\frac{\pi}{n\sin(\pi/2n)}$; $\frac{2\pi}{\sqrt{a^2-b^2}}$; $\frac\pi2$ ($\sin x/x$); $\frac\pi{\sin\pi a}$.

---

## Appendix D. Verification script

Run `python verify_complex.py` after saving the block below. Every exercise answer above was checked this way (plus the spot checks in the text). Requires `numpy` and `mpmath`.

```python
# verify_complex.py  (numpy, mpmath)
import numpy as np, mpmath as mp
mp.mp.dps = 25
def chk(name, got, exp, tol=1e-6):
    ok = abs(complex(got) - complex(exp)) < tol * max(1, abs(complex(exp)))
    print("OK  " if ok else "FAIL", f"{name:40s}", complex(got), complex(exp))

# --- contour integrals by direct quadrature on the contour ----------------
def cint(f, z, dz, t0, t1, n=200001):
    t = np.linspace(t0, t1, n); return np.trapezoid(f(z(t)) * dz(t), t)
circ  = lambda r, c=0: (lambda t: c + r*np.exp(1j*t))
dcirc = lambda r: (lambda t: 1j*r*np.exp(1j*t))
T = 2*np.pi
chk("∮ conj(z) dz, |z|=1", cint(np.conj, circ(1), dcirc(1), 0, T), 2j*np.pi)
chk("∮ dz/z", cint(lambda z: 1/z, circ(1), dcirc(1), 0, T), 2j*np.pi)
chk("∮ dz/(z^2-1), |z|=2", cint(lambda z: 1/(z*z-1), circ(2), dcirc(2), 0, T), 0)
chk("∮ e^z/(z-1), |z|=2", cint(lambda z: np.exp(z)/(z-1), circ(2), dcirc(2), 0, T), 2j*np.pi*np.e)
chk("∮ e^z/z^3, |z|=2", cint(lambda z: np.exp(z)/z**3, circ(2), dcirc(2), 0, T), 1j*np.pi)
chk("∮ sin z/z^2, |z|=1", cint(lambda z: np.sin(z)/z**2, circ(1), dcirc(1), 0, T), 2j*np.pi)
chk("∮ (z+1)/(z^2(z-2)), |z|=3", cint(lambda z: (z+1)/(z*z*(z-2)), circ(3), dcirc(3), 0, T), 0)
chk("∮ e^z/(z^2(z+1)), |z|=2", cint(lambda z: np.exp(z)/(z*z*(z+1)), circ(2), dcirc(2), 0, T), 2j*np.pi/np.e)
chk("∮ dz/sin z, |z|=1", cint(lambda z: 1/np.sin(z), circ(1), dcirc(1), 0, T), 2j*np.pi)
chk("∮ dz/(z^2+1), |z|=2", cint(lambda z: 1/(z*z+1), circ(2), dcirc(2), 0, T), 0)
t = np.linspace(0, T, 100001)
chk("∫ e^{cos}cos(sin)", np.trapezoid(np.exp(np.cos(t))*np.cos(np.sin(t)), t), 2*np.pi)
chk("∫|e^{it}-1|dt", np.trapezoid(abs(np.exp(1j*t)-1), t), 8)

# --- numbers ---------------------------------------------------------------
chk("(1+i)^10", (1+1j)**10, 32j)
chk("i^i", 1j**1j, np.exp(-np.pi/2))
chk("(1+i)^(1+i)", (1+1j)**(1+1j), np.sqrt(2)*np.exp(-np.pi/4)*np.exp(1j*(np.log(np.sqrt(2))+np.pi/4)))
chk("sin(pi/2+i ln(2+sqrt3))", mp.sin(mp.pi/2 + 1j*mp.log(2+mp.sqrt(3))), 2)
z1 = np.exp(3j*np.pi/4)
print("Log(z1^2) =", np.log(z1*z1), "  2 Log z1 =", 2*np.log(z1), "  (differ by 2πi)")
for zz in (-2+0.1j, 5j):
    print("sqrt(z-1)sqrt(z+1) =", np.sqrt(zz-1)*np.sqrt(zz+1), "  principal sqrt(z^2-1) =", np.sqrt(zz*zz-1))

# --- real integrals --------------------------------------------------------
I = lambda f, a, b: mp.quad(f, [a, b])
chk("∫dx/(1+x^2)", I(lambda x: 1/(x*x+1), -mp.inf, mp.inf), mp.pi)
chk("∫dx/(x^2+4)^2", I(lambda x: 1/(x*x+4)**2, -mp.inf, mp.inf), mp.pi/16)
chk("∫0^∞ dx/(x^4+1)", I(lambda x: 1/(x**4+1), 0, mp.inf), mp.pi/(2*mp.sqrt(2)))
chk("∫x^2/(x^4+1)", I(lambda x: x*x/(x**4+1), -mp.inf, mp.inf), mp.pi/mp.sqrt(2))
chk("∫dx/(x^6+1)", I(lambda x: 1/(x**6+1), -mp.inf, mp.inf), 2*mp.pi/3)
chk("∫0^∞ dx/(x^2+1)^2", I(lambda x: 1/(x*x+1)**2, 0, mp.inf), mp.pi/4)
chk("∫0^2π dθ/(5+4cosθ)", I(lambda s: 1/(5+4*mp.cos(s)), 0, 2*mp.pi), 2*mp.pi/3)
chk("∫0^2π dθ/(3+2cosθ)", I(lambda s: 1/(3+2*mp.cos(s)), 0, 2*mp.pi), 2*mp.pi/mp.sqrt(5))
chk("∫0^∞ cos x/(x^2+1)", mp.quadosc(lambda x: mp.cos(x)/(x*x+1), [0, mp.inf], omega=1), mp.pi/(2*mp.e))
chk("∫cos x/(x^2+9) full line", 2*mp.quadosc(lambda x: mp.cos(x)/(x*x+9), [0, mp.inf], omega=1), mp.pi/3*mp.e**-3)
chk("∫x sin x/(x^2+4)", 2*mp.quadosc(lambda x: x*mp.sin(x)/(x*x+4), [0, mp.inf], omega=1), mp.pi*mp.e**-2)
chk("∫0^∞ sin x/x", mp.quadosc(lambda x: mp.sin(x)/x, [0, mp.inf], omega=1), mp.pi/2)
chk("∫e^{-2x²}cos3x", I(lambda x: mp.e**(-2*x*x)*mp.cos(3*x), -mp.inf, mp.inf), mp.sqrt(mp.pi/2)*mp.e**(-mp.mpf(9)/8))
chk("∫0^∞ sin(x^2)", mp.quadosc(lambda x: mp.sin(x*x), [0, mp.inf], zeros=lambda n: mp.sqrt(mp.pi*n)), mp.sqrt(mp.pi/8))
chk("keyhole a=1/3", I(lambda x: x**(mp.mpf(1)/3-1)/(1+x), 0, mp.inf), mp.pi/mp.sin(mp.pi/3), 1e-5)
chk("∫0^∞ dx/(x^3+1)", I(lambda x: 1/(x**3+1), 0, mp.inf), 2*mp.pi/(3*mp.sqrt(3)))
chk("∫0^∞ sqrt(x)/(x^2+1)", I(lambda x: mp.sqrt(x)/(x*x+1), 0, mp.inf), mp.pi/mp.sqrt(2))
# PV  ∫ sin x /(x(x^2+1)): integrand is even and regular at 0 (no real PV issue)
chk("∫ sin x/(x(x^2+1))", 2*mp.quadosc(lambda x: mp.sin(x)/(x*(x*x+1)), [0, mp.inf], omega=1), mp.pi*(1-mp.e**-1))

# --- Green function and Kramers-Kronig ------------------------------------
w0, g, t_ = 1.0, 0.5, 1.7; Om = mp.sqrt(w0**2 - g**2/4)
Gnum = mp.quad(lambda w: mp.e**(-1j*w*t_)/(w0**2 - w*w - 1j*g*w), [-300, -30, -5, 0, 5, 30, 300])/(2*mp.pi)
chk("damped G(t=1.7)", Gnum, mp.e**(-g*t_/2)*mp.sin(Om*t_)/Om, 5e-3)
chi = lambda w: 1/(w0**2 - w*w - 1j*g*w); w = 0.7
f2 = lambda wp: mp.im(chi(wp))/(wp - w)
pv = (mp.quad(f2, [-300, -50, -5, -1, 0, w-0.2, w-1e-6]) + mp.quad(f2, [w+1e-6, w+0.2, 1, 5, 50, 300]))
chk("KK: Re chi(0.7)", pv/mp.pi, mp.re(chi(w)), 5e-3)
print("all checks done")
```

---

## Appendix E. Parallel map to Goldstein and Jackson

| Where it appears | What you use | Module |
| --- | --- | --- |
| Goldstein ch. 6 (small oscillations) | $e^{i\omega t}$ normal modes, complex eigenfrequencies, damped modes | 1, 7, 9 |
| Goldstein, stability of fixed points | eigenvalues in the complex plane | 1, 7 |
| Goldstein, Fourier methods | Fourier series/transforms via residues | 8 |
| Jackson ch. 1 and 2 | harmonic functions, mean value, no interior extrema, 2D potentials | 2, 5, 10 |
| Jackson ch. 3, 4 | complex exponentials, $e^{im\varphi}$ | 1 |
| **Jackson ch. 6** (Green function of the wave equation) | **poles on the real axis, Jordan, residues, $i\varepsilon$** | **7, 8, 9** |
| **Jackson ch. 7** (Kramers-Kronig, dispersion) | **analyticity in the UHP, principal values** | **8, 9** |
| Jackson ch. 11 and 12 (covariant Green functions) | the same contours in four dimensions | 8, 9 |
| QFT (later) | Feynman $i\varepsilon$; branch cuts as thresholds; dim. reg. (parked gamma function) | 3, 9, Appendix A |

---

## Appendix F. Study tips specific to this track

- Do **two exercises a day** rather than a long session; contour integrals reward repetition.
- When you finish an exercise, **sanity-check it numerically** (Appendix D takes five minutes to adapt). A wrong factor of $2$ or $i$ is exposed immediately.
- Keep a **mistake log**: the typical errors are the wrong half-plane, a missing $\frac12$ for a half-circle, and a lost $2\pi i$. Review it before Module 9.
- Use Ávila's *Respostas e sugestões* after trying, not before.
- When Ávila is terse, read the same topic in Churchill's chapter for a second explanation; when Churchill is dry, read the same topic in Ávila for the idea.
