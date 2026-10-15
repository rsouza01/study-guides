# Module 13: Relativistic mechanics, Lagrangian and Hamiltonian form (optional module)

**Books:** Goldstein 7.1 to 7.5 (skim: postulates, Lorentz transformations, four-vectors, the metric tensor and tensors), 7.6 to 7.8 (forces, kinematics of collisions, angular momentum: light), **7.9 to 7.10 (Lagrangian and covariant Lagrangian formulations)**, 8.4 (relativistic Hamiltonian); **Jackson Chapter 11 does special relativity better; read it alongside** (see the EM guide). Skip 7.11 (introduction to general relativity).
**Time:** 2 weeks (four sessions); condense to one week if your relativity is solid.

## Why this matters for the bridge

The relativistic Lagrangian for a charged particle $L=-mc^2\sqrt{1-v^2/c^2}-q\Phi+q\mathbf v\cdot\mathbf A$ is where **minimal coupling** $p^\mu\to p^\mu-qA^\mu$ first appears; it is the same substitution that makes the Dirac and Klein-Gordon equations electromagnetic. The covariant action $S=-mc\int ds$ and its reparametrization invariance are the first examples of a *gauge-like redundancy* with a constrained Hamiltonian, a structure that returns in every gauge theory. Also, the nonrelativistic expansion of $H=\sqrt{p^2c^2+m^2c^4}$ gives the relativistic correction $-\frac{p^4}{8m^3c^2}$ that enters the fine structure of hydrogen in QM.

## Skip-test (40 minutes, no notes)

1. Derive $p=\gamma mv$ and $H=\gamma mc^2=\sqrt{p^2c^2+m^2c^4}$ from $L=-mc^2\sqrt{1-v^2/c^2}$.
2. Write $L$ for a charge in an EM field and obtain $\mathbf p=\gamma m\mathbf v+q\mathbf A$ and $H=\sqrt{(\mathbf p-q\mathbf A)^2c^2+m^2c^4}+q\Phi$.
3. State $p^\mu p_\mu=m^2c^2$ and use it to find the threshold energy for $pp\to ppp\bar p$ on a fixed target: $T_{\rm th}=6mc^2$.
4. Write the covariant action $S=-mc\int\sqrt{\eta_{\mu\nu}dx^\mu dx^\nu}$ and the covariant equation of motion $\frac{dp^\mu}{d\tau}=\frac qcF^{\mu\nu}u_\nu$ (Gaussian units, signature $+---$).
5. Explain what reparametrization invariance means and why it forces the canonical Hamiltonian to vanish.

## Prerequisites

Modules 02, 07. Familiarity with four-vectors; metric signature $(+,-,-,-)$.

## Detailed topics (checklist)

**Relativistic kinematics (7.1 to 7.8) [Should]**
- Lorentz transformations; four-vectors; invariants; $p^\mu=(E/c,\mathbf p)$; $p^\mu p_\mu=m^2c^2$; collision kinematics (threshold energies, invariant mass $s=(p_1+p_2)^2$).
- Doppler and Compton shift from four-momentum conservation.

**Lagrangian formulation (7.9) [Must]**
- $L=-mc^2\sqrt{1-v^2/c^2}-V$; $\mathbf p=\gamma m\mathbf v$; why there is no relativistic "kinetic energy" $\frac12mv^2$ in $L$; electromagnetic coupling $L_{\rm int}=-q\Phi+q\mathbf v\cdot\mathbf A$ (SI) or $-q\Phi+\frac qc\mathbf v\cdot\mathbf A$ (Gaussian).

**Covariant Lagrangian formulation (7.10) [Must]**
- Action $S=-mc\int\sqrt{\dot x^\mu\dot x_\mu}\,d\lambda-\frac qc\int A_\mu\dot x^\mu\,d\lambda$; arbitrary parameter $\lambda$ (reparametrization invariance); the equation of motion $\frac{dp^\mu}{d\tau}=\frac qcF^{\mu\nu}u_\nu$ with $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$; the generalized momentum $P^\mu=p^\mu+\frac qcA^\mu$ and minimal coupling.
- **Constraint:** reparametrization invariance means the canonical Hamiltonian vanishes identically and the momenta satisfy $(p-qA/c)^2=m^2c^2$ (a constraint): the particle analogue of gauge redundancy.

**Relativistic Hamiltonian (8.4) [Must]**
- $H=\sqrt{(\mathbf p-q\mathbf A)^2c^2+m^2c^4}+q\Phi$; expansion $H\approx mc^2+\frac{(\mathbf p-q\mathbf A)^2}{2m}+q\Phi-\frac{(\mathbf p-q\mathbf A)^4}{8m^3c^2}$; the QM descendants: the Klein-Gordon equation is the quantized mass-shell constraint; the relativistic kinetic correction is a fine-structure term (Zettili Section 9.2.3).

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Goldstein 7.1 to 7.8 (skim); Jackson 11.2 to 11.5 (if the EM guide is running) |
| B1 | Exercises 1 to 4 |
| A2 | Goldstein 7.9 to 7.10, 8.4; derive the EM Lagrangian and Hamiltonian |
| B2 | Exercises 5 to 10; cheat sheet |

## Derive from scratch (A sessions, book closed)

1. $p=\gamma mv$, $H=\gamma mc^2$ from $L=-mc^2\sqrt{1-v^2/c^2}$.
2. $\mathbf p=\gamma m\mathbf v+q\mathbf A$ and $H$ for the EM case.
3. The Lorentz force from the covariant action.
4. The mass-shell relation $p^\mu p_\mu=m^2c^2$ and threshold energy for a reaction.
5. The vanishing of the canonical Hamiltonian for the parametrized free particle.

## Bare-minimum exercises (with expected results)

1. **Free relativistic particle:** $\mathbf p=\gamma m\mathbf v$, $H=\sqrt{p^2c^2+m^2c^4}$, $\mathbf v=\partial H/\partial\mathbf p=\mathbf pc^2/H$; the expansion $H\approx mc^2+\frac{p^2}{2m}-\frac{p^4}{8m^3c^2}$.
2. **Charge in an EM field:** derive $H=\sqrt{(\mathbf p-q\mathbf A)^2c^2+m^2c^4}+q\Phi$ and recover the Lorentz force from Hamilton's equations (the result is $\frac{d(\gamma m\mathbf v)}{dt}=q(\mathbf E+\mathbf v\times\mathbf B)$).
3. **Threshold:** $pp\to ppp\bar p$ with a stationary target: the invariant $(E+mc^2)^2-p^2c^2=2m^2c^4+2mc^2E$ must equal $(4mc^2)^2$ at threshold; show $E_{\rm th}=7mc^2$ so $T_{\rm th}=6mc^2\approx5.6$ GeV.
4. **Compton:** conserve four-momentum for $\gamma e\to\gamma e$ at rest to get $\lambda'-\lambda=\frac{h}{mc}(1-\cos\theta)$, with $\frac h{mc}=2.426$ pm.
5. **Relativistic cyclotron motion:** in a uniform $\mathbf B$ the angular frequency is $\omega=\frac{qB}{\gamma m}$ (SI) (derive from $\frac{d(\gamma m\mathbf v)}{dt}=q\mathbf v\times\mathbf B$ with $\gamma$ constant) and the gyroradius is $r=\frac{p}{qB}$.
6. **Covariant force:** write $\frac{dp^\mu}{d\tau}=\frac qcF^{\mu\nu}u_\nu$ for $\mu=0$ and $\mu=i$ in terms of $\mathbf E,\mathbf B$ and show the $\mu=0$ component is $\frac{dE}{dt}=q\mathbf E\cdot\mathbf v$.
7. **Reparametrization:** for $S=-mc\int\sqrt{\dot x^\mu\dot x_\mu}\,d\lambda$ show $p_\mu=-mc\frac{\dot x_\mu}{\sqrt{\dot x^2}}$ satisfies $p^\mu p_\mu=m^2c^2$ identically and that the canonical Hamiltonian $p_\mu\dot x^\mu-L$ vanishes identically; the dynamics is carried by the constraint.
8. **Minimal coupling:** in $p^\mu p_\mu=m^2c^2$ replace $p^\mu\to p^\mu-\frac qcA^\mu$ and show that spatial components give $\mathbf p\to\mathbf p-\frac qc\mathbf A$ and the time component $E\to E-q\Phi$; recover $H$.
9. **Nonrelativistic limit and the QM connection:** show the first relativistic correction to the Hamiltonian is $-\frac{p^4}{8m^3c^2}$ and state its expectation value as the relativistic kinetic correction in the hydrogen atom (compare Zettili Section 9.2.3).
10. **Angular momentum:** the relativistic angular momentum $\mathbf L=\mathbf r\times\mathbf p$ with $\mathbf p=\gamma m\mathbf v$ is conserved for central forces; the boost charge $\mathbf K=\mathbf rE/c^2-\mathbf pt$ is conserved for a free particle (compare the Galilean boost charge in Module 04).

## Optional extension

Quantize the mass-shell constraint $p^\mu p_\mu-m^2c^2=0$ by $p_\mu\to i\hbar\partial_\mu$ and recover the Klein-Gordon equation $(\hbar^2\Box+m^2c^2)\psi=0$; with minimal coupling, $(i\hbar\partial_\mu-\frac qcA_\mu)^2$. The problems with a single-particle interpretation of this equation are the entry to field theory (Modules 17 to 19).

## Pitfalls

- Using $\frac12mv^2$ in a relativistic Lagrangian.
- Taking $\mathbf p=m\mathbf v$ with $m$ replaced by a velocity-dependent "relativistic mass" and then forgetting that $\gamma$ is not constant in the force law.
- Mixing metric signatures and the placement of $\mathbf A$ signs between SI and Gaussian.
- Concluding from the vanishing Hamiltonian that there is no dynamics (the constraint carries it).

## Gate questions

1. Why is the relativistic Lagrangian $-mc^2\sqrt{1-v^2/c^2}$ rather than a relativistic version of $T-V$?
2. What does reparametrization invariance imply about the Hamiltonian, and why is it called a gauge redundancy?
3. Where does minimal coupling appear in the classical theory, and where does it return in QM?

## One-page cheat sheet contents

$L$, $\mathbf p$, $H$ for free and EM cases; the covariant action and equation of motion; mass shell; minimal coupling; threshold and Compton formulas.
