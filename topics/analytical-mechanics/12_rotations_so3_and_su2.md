# Module 12: Rotations, $SO(3)$ and $SU(2)$

**Books:** Goldstein Chapter 4: 4.1 to 4.3 (orthogonal transformations), 4.4 (Euler angles, vocabulary only), the Cayley-Klein parameters section (4.5 or 4.6 in your printing), 4.6 to 4.7 (Euler's theorem, finite rotations), **4.8 (infinitesimal rotations)**, 4.9 (rate of change of a vector), 4.10 (Coriolis effect, optional); the Appendix on groups and algebras if your printing has one. **Skip** all of Goldstein Chapter 5 (rigid-body dynamics, tops).
**Time:** 2 weeks (four sessions).

## Why this matters for the bridge

Section 4.8 constructs the generators of infinitesimal rotations and their commutation relations. Rotations give $\mathfrak{so}(3)\cong\mathfrak{su}(2)$; the Lorentz group (in the EM guide) gives $\mathfrak{so}(1,3)$, which splits into two copies of $\mathfrak{su}(2)$. Seeing the second as a doubling of the first is how the $(j_-,j_+)$ classification of fields becomes obvious. The Cayley-Klein detour is where $SU(2)$ shows up in a nineteenth-century rigid-body context: a good antidote to the idea that spinors are a quantum invention. And it explains why angular momentum in QM has the algebra it has: it is the Lie algebra of the rotation group, the same one found classically.

## Skip-test (40 minutes, no notes)

1. Show that the matrices $(L_i)_{jk}=-\epsilon_{ijk}$ satisfy $[L_i,L_j]=\epsilon_{ijk}L_k$ and that $R(\hat{\mathbf n},\phi)=e^{\phi\,\hat{\mathbf n}\cdot\mathbf L}$ is the rotation by $\phi$ about $\hat{\mathbf n}$.
2. Derive Rodrigues' formula $R=\cos\phi\,\mathbb 1+(1-\cos\phi)\hat{\mathbf n}\hat{\mathbf n}^T+\sin\phi\,[\hat{\mathbf n}]_\times$.
3. Show that $U=e^{-i\phi\,\hat{\mathbf n}\cdot\boldsymbol\sigma/2}$ is in $SU(2)$, that $U(2\pi)=-1$ and that $U(\boldsymbol\sigma\cdot\mathbf r)U^\dagger=\boldsymbol\sigma\cdot(R\mathbf r)$.
4. State why $SU(2)$ is a double cover of $SO(3)$.
5. State the formula for the rate of change of a vector in a rotating frame: $\left(\frac{d\mathbf G}{dt}\right)_{\rm space}=\left(\frac{d\mathbf G}{dt}\right)_{\rm body}+\boldsymbol\omega\times\mathbf G$.

## Prerequisites

Modules 09, 10 (generators and brackets), Module 01 (matrix exponential).

## Detailed topics (checklist)

**Orthogonal transformations (4.2, 4.3) [Must]**
- $R^TR=1$, $\det R=1$; the group $SO(3)$; three independent parameters; Euler angles as a coordinate chart (4.4: vocabulary only); orthogonal matrices in index notation $R_{ij}$; composition and non-commutativity of finite rotations.

**Infinitesimal rotations and generators (4.8) [Must]**
- $R=1+\epsilon\,\hat{\mathbf n}\cdot\mathbf L$ with $(L_i)_{jk}=-\epsilon_{ijk}$ (antisymmetric because $R$ is orthogonal); $\delta\mathbf r=\epsilon\,\hat{\mathbf n}\times\mathbf r$; **commutation relations $[L_i,L_j]=\epsilon_{ijk}L_k$ (as matrices)**; exponentiation to finite rotations (Rodrigues); the same algebra from the Poisson brackets of $L_i=\epsilon_{ijk}x_jp_k$ (Module 09). **Two routes, one Lie algebra:** the matrices act on vectors; the phase-space functions act on observables.

**Spinors and $SU(2)$ (Cayley-Klein) [Must]**
- The $2\times2$ unitary matrices with $\det=1$; $U=e^{-i\phi\,\hat{\mathbf n}\cdot\boldsymbol\sigma/2}$; the map $SU(2)\to SO(3)$, $U(\boldsymbol\sigma\cdot\mathbf r)U^\dagger=\boldsymbol\sigma\cdot(R\mathbf r)$; the kernel $\{\pm1\}$ (double cover); $U(2\pi)=-1$: spin-1/2 states change sign under a $2\pi$ rotation; the Pauli matrices $\sigma_i\sigma_j=\delta_{ij}+i\epsilon_{ijk}\sigma_k$ and $\frac{\sigma_i}{2}$ satisfy the same algebra as $L_i$.

**Rotating frames (4.9 to 4.10) [Should]**
- Rate of change of a vector; Coriolis and centrifugal accelerations $\mathbf a=\mathbf a'+2\boldsymbol\omega\times\mathbf v'+\boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r')$; Foucault pendulum.

**The next step in the EM guide [Awareness]**
- Boost generators $\mathbf K$ and rotation generators $\mathbf S$ close into $\mathfrak{so}(1,3)$; the combinations $\mathbf A_\pm=\frac12(\mathbf S\pm i\mathbf K)$ are two commuting $\mathfrak{su}(2)$ algebras. The same construction as here, with one sign changed.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Goldstein 4.2 to 4.3, 4.6 to 4.7; derive $R^TR=1$ consequences and Rodrigues from the matrix exponential |
| B1 | Exercises 1 to 4 |
| A2 | Goldstein 4.8 and the Cayley-Klein section; derive the generator algebra and the $SU(2)\to SO(3)$ map |
| B2 | Exercises 5 to 10; (optional) 4.9 to 4.10; cheat sheet |

## Derive from scratch (A sessions, book closed)

1. The antisymmetry of an infinitesimal rotation generator from orthogonality.
2. The commutation relations $[L_i,L_j]=\epsilon_{ijk}L_k$ for the $3\times3$ matrices.
3. Rodrigues' rotation formula from $e^{\phi\,\hat{\mathbf n}\cdot\mathbf L}$.
4. The $SU(2)\to SO(3)$ map $U(\boldsymbol\sigma\cdot\mathbf r)U^\dagger=\boldsymbol\sigma\cdot(R\mathbf r)$ for a rotation about $z$.
5. The formula for the rate of change of a vector in a rotating frame.

## Bare-minimum exercises (with expected results)

1. **Generators:** build the three $3\times3$ matrices $(L_i)_{jk}=-\epsilon_{ijk}$ and verify $[L_x,L_y]=L_z$ and cyclic permutations; verify $\sum L_i^2=-2\cdot\mathbb 1$.
2. **Rodrigues:** show $e^{\phi\,\hat{\mathbf n}\cdot\mathbf L}=\cos\phi\,\mathbb 1+(1-\cos\phi)\hat{\mathbf n}\hat{\mathbf n}^T+\sin\phi[\hat{\mathbf n}]_\times$; check against $R_z(\phi)$.
3. **Non-commutativity:** compute $R_x(90^\circ)R_z(90^\circ)$ and $R_z(90^\circ)R_x(90^\circ)$; both are rotations by $120^\circ$ but about *different* axes, $(1,-1,1)/\sqrt3$ and $(1,1,1)/\sqrt3$ respectively.
4. **Poisson-bracket route:** verify $\{L_i,L_j\}=\epsilon_{ijk}L_k$ from the phase-space functions (Module 09, exercise 2) and state in one sentence why the same $\epsilon_{ijk}$ appears.
5. **$SU(2)$:** show $e^{-i\phi\sigma_z/2}$ gives $-\mathbb 1$ at $\phi=2\pi$ and $+\mathbb 1$ at $\phi=4\pi$; verify $U\sigma_xU^\dagger=\sigma_x\cos\phi+\sigma_y\sin\phi$ for $U=e^{-i\phi\sigma_z/2}$ (use $e^{i\theta\sigma_z}=\cos\theta+i\sigma_z\sin\theta$ and $\sigma_z\sigma_x=i\sigma_y$), and show this is $\boldsymbol\sigma\cdot(R_z(\phi)\hat{\mathbf x})$, i.e. a counterclockwise rotation of the vector by $\phi$ about $z$.
6. **Cayley-Klein:** for $U=\begin{pmatrix}a&b\\-b^*&a^*\end{pmatrix}$ with $|a|^2+|b|^2=1$ show $U\in SU(2)$ and identify the rotation it represents when $b=0$ ($a=e^{-i\phi/2}$).
7. **Finite versus infinitesimal:** an infinitesimal rotation $\delta\mathbf r=\boldsymbol\epsilon\times\mathbf r$ satisfies $\delta^2\mathbf r$ commutator relations: show $[\delta_{\epsilon_1},\delta_{\epsilon_2}]\mathbf r=(\boldsymbol\epsilon_1\times\boldsymbol\epsilon_2)\times\mathbf r$ (rotations about different axes do not commute; the commutator is a rotation about the third axis).
8. **Foucault pendulum:** the plane of oscillation rotates with angular velocity $\Omega\sin\lambda$ at latitude $\lambda$ ($\Omega=2\pi/24\,$h); at $\lambda=45^\circ$ the period of one full precession is $24\,{\rm h}/\sin45^\circ\approx34$ h.
9. **Coriolis deflection:** a projectile falls a distance $h$ from rest at latitude $\lambda$; the eastward deflection is $\frac13\Omega\cos\lambda\sqrt{\frac{8h^3}{g}}$ (derive it: to first order in $\Omega$ the Coriolis acceleration is $2\Omega\cos\lambda\,gt$ eastward, so $x=\frac13\Omega g\cos\lambda\,t^3$ with $t=\sqrt{2h/g}$).
10. **Spin precession:** for a spin-1/2 in a field along $z$ with $\hat H=\frac{\omega_0}{2}\sigma_z$ the evolution operator is $e^{-i\omega_0t\sigma_z/2}$, a rotation of the spin vector about $z$ at angular velocity $\omega_0$ (Larmor precession); compare with a classical magnetic moment precessing in a magnetic field.

## Optional extension

Prove that the adjoint representation of $SU(2)$ is $SO(3)$ and that the Pauli matrices transform as a vector: $U\sigma_iU^\dagger=R_{ji}\sigma_j$. Then decompose $\mathfrak{so}(1,3)\otimes\mathbb C\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ by $\mathbf A_\pm=\frac12(\mathbf S\pm i\mathbf K)$ (using the boost algebra $[K_i,K_j]=-i\epsilon_{ijk}S_k$ from the EM guide).

## Pitfalls

- Treating the Euler angles as a global coordinate system (they have singularities at $\theta=0,\pi$).
- Forgetting that $SU(2)$ double covers $SO(3)$, and thereby treating $U(2\pi)=-1$ as a mistake.
- Sign errors between active and passive rotations.
- Confusing the matrix generators $L_i$ (acting on vectors) with the phase-space functions $L_i$ (acting on observables).

## Gate questions

1. Why are the infinitesimal rotation generators antisymmetric, and what algebra do they close into?
2. How does $SU(2)$ arise in rigid-body kinematics, and what does the double cover mean physically?
3. Why is the classical angular-momentum algebra identical in form to the quantum one?

## One-page cheat sheet contents

$(L_i)_{jk}=-\epsilon_{ijk}$ and the algebra; Rodrigues' formula; $SU(2)$ rotation matrices and the double cover; the map $SU(2)\to SO(3)$; the rotating-frame formula.
