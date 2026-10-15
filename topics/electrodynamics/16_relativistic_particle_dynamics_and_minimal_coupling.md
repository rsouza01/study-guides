# Module 16: Relativistic particle dynamics and minimal coupling

**Books:** Jackson **12.1** (Lagrangian and Hamiltonian for a relativistic charged particle), 12.2 (motion in a uniform static magnetic field), 12.3 (motion in combined uniform static electric and magnetic fields), 12.6 (the Darwin Lagrangian: optional, but the first sight of one-photon exchange as an instantaneous potential). **Skip** 12.4 to 12.5 (drifts and adiabatic invariants: plasma physics). Your mechanics guide, Modules 07 and 13 (Hamiltonian and relativistic mechanics), is the prerequisite; Griffiths 12.3 for the physical picture.
**Time:** 2 weeks (four sessions). Gaussian units.

## Why this matters

**Minimal coupling** $p^\mu\to p^\mu-\frac qcA^\mu$ appears here for the first time in electrodynamics. It is the *same substitution* that makes the Dirac and Klein-Gordon equations electromagnetic. The canonical momentum $\mathbf p=\gamma m\mathbf v+\frac qc\mathbf A$ is not the kinetic momentum and is gauge-dependent, exactly as in your mechanics guide, but now relativistically.

## Skip-test (40 minutes, no notes)

1. Write $L=-mc^2\sqrt{1-v^2/c^2}-q\Phi+\frac qc\mathbf v\cdot\mathbf A$, the canonical momentum $\mathbf p=\gamma m\mathbf v+\frac qc\mathbf A$ and the Hamiltonian $H=\sqrt{(c\mathbf p-q\mathbf A)^2+m^2c^4}+q\Phi$.
2. Show that Hamilton's (or Lagrange's) equations reproduce $\frac{d(\gamma m\mathbf v)}{dt}=q\left(\mathbf E+\frac{\mathbf v}{c}\times\mathbf B\right)$.
3. Find the radius and angular frequency of circular motion in a uniform magnetic field: $r=\frac{pc}{qB}$, $\omega=\frac{qB}{\gamma mc}$.
4. State the drift velocity in crossed fields $\mathbf v_d=c\frac{\mathbf E\times\mathbf B}{B^2}$ (for $E<B$) and why a frame with $\mathbf E'=0$ exists.
5. Solve for the motion in a uniform electric field (hyperbolic motion).

## Prerequisites

Modules 13 and 15; mechanics guide Modules 02, 07, 13.

## Detailed topics (checklist)

**Lagrangian and Hamiltonian (12.1) [Must]**
- $L=-\frac{mc^2}{\gamma}-q\Phi+\frac qc\mathbf v\cdot\mathbf A$; $\mathbf p=\gamma m\mathbf v+\frac qc\mathbf A$; $H=\mathbf p\cdot\mathbf v-L=\gamma mc^2+q\Phi=\sqrt{(c\mathbf p-q\mathbf A)^2+m^2c^4}+q\Phi$; gauge transformation $L\to L+\frac{q}{c}\frac{d\Lambda}{dt}$, $\mathbf p\to\mathbf p+\frac qc\nabla\Lambda$.
- **Covariant formulation:** $S=-mc\int ds-\frac qc\int A_\mu dx^\mu$; the generalized momentum $P^\mu=p^\mu+\frac qcA^\mu$; $\frac{dp^\mu}{d\tau}=\frac qcF^{\mu\nu}u_\nu$.
- **Minimal coupling:** $p^\mu\to p^\mu-\frac qcA^\mu$ in the mass-shell relation $p^\mu p_\mu=m^2c^2$.

**Motion in uniform fields (12.2 to 12.3) [Should]**
- Uniform $\mathbf B$: circular (helical) motion with constant $\gamma$; $r=\frac{p_\perp c}{qB}$, $\omega=\frac{qB}{\gamma mc}$; the synchrotron frequency is a $1/\gamma$-reduced cyclotron frequency (preview of Module 22).
- Crossed fields $\mathbf E\perp\mathbf B$ with $E<B$: boost to the frame with $\mathbf E'=0$ ($\boldsymbol\beta=\frac{\mathbf E\times\mathbf B}{B^2}$), gyrate there, boost back: the lab motion is a drift at $c\frac{E}{B}$ plus gyration (a cycloid-like path); for $E>B$ the particle accelerates without bound.
- Uniform $\mathbf E$ (hyperbolic motion): $x=\frac{mc^2}{qE}\left(\sqrt{1+\left(\frac{qEt}{mc}\right)^2}-1\right)$, $\gamma=\sqrt{1+\left(\frac{qEt}{mc}\right)^2}$, proper acceleration $\frac{qE}{m}$.

**The Darwin Lagrangian (12.6) [Could]**
- To order $v^2/c^2$ the Lagrangian of interacting charges $L=\sum\left[\frac12m_av_a^2+\frac{1}{8c^2}m_av_a^4\right]-\sum_{a<b}\frac{q_aq_b}{r_{ab}}\left\{1-\frac{1}{2c^2}\left[\mathbf v_a\cdot\mathbf v_b+(\mathbf v_a\cdot\hat{\mathbf n})(\mathbf v_b\cdot\hat{\mathbf n})\right]\right\}$ with the sign conventions in your copy: the first appearance of one-photon exchange as an instantaneous interaction (the origin of the Breit interaction).

## Method card

**Charged particle in given fields:** (1) write $L$ (or $H$) with the gauge you choose; (2) identify symmetries and conserved canonical momenta; (3) derive the equations of motion (Lorentz force) or reduce with conserved quantities; (4) transform to a frame that simplifies the fields (e.g. $\mathbf E'=0$); (5) check with energy $\gamma mc^2+q\Phi$ and the invariant $u\cdot u=c^2$.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Jackson 12.1; derive $\mathbf p$, $H$ from $L$ (closed book) |
| B1 | Exercises 1, 2 and 7 |
| A2 | Jackson 12.2; the cyclotron frequency and radius |
| B2 | Exercises 3 and 6 |
| A3 | Jackson 12.3; crossed fields and the boost to $\mathbf E'=0$ |
| B3 | Exercises 4 and 5 |
| A4 | Jackson 12.6 (optional); exercises 8 and 9 |
| B4 | **Jackson targets** (exercise 10); the computational task |

## Derive from scratch

1. $\mathbf p$ and $H$ from $L$ for a charge in an EM field.
2. The Lorentz force from the Lagrangian.
3. The cyclotron frequency and radius.
4. The crossed-field drift via the boost to $\mathbf E'=0$.
5. Hyperbolic motion in a uniform electric field.

## Bare-minimum exercises (with expected results)

1. **Canonical momentum and Hamiltonian:** $\mathbf p=\gamma m\mathbf v+\frac qc\mathbf A$ and $H=\gamma mc^2+q\Phi=\sqrt{(c\mathbf p-q\mathbf A)^2+m^2c^4}+q\Phi$; the nonrelativistic limit is $mc^2+\frac{(\mathbf p-q\mathbf A/c)^2}{2m}+q\Phi$.
2. **Lorentz force:** Lagrange's equation $\frac{d}{dt}\frac{\partial L}{\partial\mathbf v}=\frac{\partial L}{\partial\mathbf x}$ gives $\frac{d(\gamma m\mathbf v)}{dt}=q\mathbf E+\frac qc\mathbf v\times\mathbf B$ (use $\frac{d\mathbf A}{dt}=\partial_t\mathbf A+(\mathbf v\cdot\nabla)\mathbf A$ and the vector identity for $\mathbf v\times(\nabla\times\mathbf A)$).
3. **Cyclotron motion (SI numbers):** an electron with kinetic energy 1 MeV in $B=1$ T has $\gamma=2.96$, $p=1.42$ MeV$/c$, radius $r=\frac{p}{eB}\approx4.7$ mm and angular frequency $\omega=\frac{eB}{\gamma m}\approx5.9\times10^{10}$ s$^{-1}$ (the non-relativistic value would be $1.76\times10^{11}$).
4. **Crossed fields:** for $\mathbf E=E\hat{\mathbf y}$, $\mathbf B=B\hat{\mathbf z}$, $E<B$: the boost with $\beta=E/B$ along $x$ removes $\mathbf E$; the guiding-centre drift is $v_d=c\frac EB$ along $+x$; for $E\to B$ the drift approaches $c$ and the gyroradius diverges in the lab frame.
5. **Hyperbolic motion:** from $\frac{dp}{dt}=qE$, $p=qEt$, derive $\gamma=\sqrt{1+(qEt/mc)^2}$ and $x(t)$ above; for $t\to\infty$, $x\to ct$ and $v\to c$ without ever reaching it; the proper time $\tau=\frac{mc}{qE}\sinh^{-1}\frac{qEt}{mc}$.
6. **Conserved canonical momentum:** in a uniform $B\hat{\mathbf z}$ with the Landau gauge $\mathbf A=(-By,0,0)$, $p_x$ is conserved; show the orbit centre is at $y_0=-\frac{c\,p_x}{qB}$ (Gaussian: with $p_x=\gamma mv_x-\frac{qB}{c}y$): canonical and kinetic momenta differ.
7. **Gauge transformation:** show $L\to L+\frac{q}{c}\frac{d\Lambda}{dt}$ and that the canonical momentum shifts by $\frac qc\nabla\Lambda$ while the equations of motion are unchanged (as in your mechanics guide Module 02).
8. **Covariant action:** vary $S=-mc\int ds-\frac qc\int A_\mu dx^\mu$ to obtain $\frac{dp^\mu}{d\tau}=\frac qcF^{\mu\nu}u_\nu$ (use $dx^\mu=u^\mu d\tau$; the variation of $A_\mu$ along the path gives $\partial_\nu A_\mu-\partial_\mu A_\nu$).
9. **Darwin correction:** the $\frac{1}{8c^2}mv^4$ term is the expansion of $-mc^2\sqrt{1-v^2/c^2}$ ($-mc^2+\frac12mv^2+\frac{mv^4}{8c^2}$); the velocity-dependent two-body term is the first relativistic correction to the Coulomb interaction.
10. **Jackson targets (about 12.1 and 12.3):** (a) Lagrangian and Hamiltonian manipulations (exercises 1, 2, 7); (b) motion in crossed fields (exercise 4), including the $E>B$ case.

## Computational task (project, optional)

A relativistic Boris pusher for crossed $\mathbf E/\mathbf B$: check that $p_\mu p^\mu$ is conserved to machine precision (as a test of the integrator, not the physics, in pure $\mathbf B$) and that the drift velocity equals $c\,\mathbf E\times\mathbf B/B^2$.

## Pitfalls

- Treating $\mathbf p$ as $\gamma m\mathbf v$ in the presence of $\mathbf A$.
- Using the non-relativistic cyclotron frequency for relativistic electrons (the factor $1/\gamma$ matters for synchrotron).
- Forgetting that the drift velocity formula needs $E<B$.
- Mixing SI and Gaussian forms of the force law.

## Gate questions

1. Why is the canonical momentum gauge-dependent while $\gamma m\mathbf v$ is not?
2. Why does a frame with $\mathbf E'=0$ exist for $E<B$ but not for $E>B$?
3. Where does minimal coupling appear here and where does it re-appear in the Dirac equation?

## One-page cheat sheet contents

$L$, $\mathbf p$, $H$; covariant action; cyclotron radius and frequency; crossed-field drift; hyperbolic motion.
