# Module 05: Central forces and the Laplace-Runge-Lenz vector (optional module)

**Books:** Goldstein 3.1 to 3.4, 3.7, **3.9 (Laplace-Runge-Lenz vector)**; Landau and Lifshitz *Mechanics* sections 13 to 15 (optional).
**Time:** 2 weeks (four sessions); condense to one week by doing only the LRL part. *Optional* because central forces are likely familiar; the single piece that matters for the bridge is the hidden symmetry.

## Why this matters for the bridge

The Laplace-Runge-Lenz (LRL) vector is a conserved quantity with no obvious geometric symmetry behind it: it comes from a *hidden* symmetry of the $1/r$ potential. Its Poisson brackets close into the algebra of $SO(4)$, whose quantum descendant explains why the energy levels of hydrogen depend only on $n$ and not on $\ell$. It is one of the cleanest demonstrations that a classical symmetry structure survives quantization essentially intact. (Come back to the bracket computations after Module 09 if Poisson brackets are not in hand yet.)

## Skip-test (40 minutes, no notes)

1. Reduce the two-body problem to an equivalent one-body problem with reduced mass $\mu=\frac{m_1m_2}{m_1+m_2}$; write the effective potential $V_{\rm eff}=\frac{L^2}{2\mu r^2}+V(r)$.
2. For $V=-k/r$ obtain the orbit $r=\frac{L^2/\mu k}{1+e\cos\theta}$ with $e=\sqrt{1+\frac{2EL^2}{\mu k^2}}$, and the energy $E=-\frac{k}{2a}$.
3. State Kepler's third law $T=2\pi\sqrt{\mu a^3/k}$.
4. Define $\mathbf A=\mathbf p\times\mathbf L-\mu k\hat{\mathbf r}$ and show $\dot{\mathbf A}=0$.
5. Show $\mathbf A\cdot\mathbf L=0$ and $|\mathbf A|=\mu ke$; deduce the orbit equation from $\mathbf A\cdot\mathbf r$.

## Prerequisites

Modules 02, 04. (Poisson brackets from Module 09 are needed for exercises 7 and 8.)

## Detailed topics (checklist)

**Central-force basics (3.1 to 3.4, 3.7) [Should]**
- Reduction to the one-body problem; conservation of $\mathbf L$ so motion is planar; $L=\mu r^2\dot\phi$ (areal velocity); the radial equation with $V_{\rm eff}$; classification of orbits by energy; turning points; stability of circular orbits ($V_{\rm eff}''>0$).
- Virial theorem for a power-law potential: $2\langle T\rangle=n\langle V\rangle$; for the inverse square $\langle T\rangle=-\frac12\langle V\rangle=-E$.
- The Kepler problem: orbit equation (conic sections), $a$, $e$, period.

**The LRL vector (3.9) [Must]**
- $\mathbf A=\mathbf p\times\mathbf L-\mu k\hat{\mathbf r}$; conservation for $V=-k/r$ only; $\mathbf A$ lies in the orbital plane and points along the major axis towards perihelion; $A^2=\mu^2k^2+2\mu EL^2$; $|\mathbf A|=\mu ke$.
- Why it explains closed orbits and why a perturbation of the $1/r$ law makes the orbit precess.
- **Poisson brackets** (classical $\mathfrak{so}(4)$ algebra), for $H=\frac{p^2}{2\mu}-\frac kr$: $\{L_i,L_j\}=\epsilon_{ijk}L_k$, $\{L_i,A_j\}=\epsilon_{ijk}A_k$, $\{A_i,A_j\}=-2\mu H\,\epsilon_{ijk}L_k$. For bound orbits ($H<0$) define $\mathbf D=\mathbf A/\sqrt{-2\mu H}$ so that $\{D_i,D_j\}=\epsilon_{ijk}L_k$: the algebra of $\mathfrak{so}(4)=\mathfrak{so}(3)\oplus\mathfrak{so}(3)$ with generators $\mathbf J_\pm=\frac12(\mathbf L\pm\mathbf D)$.
- **Quantum consequence (statement):** the same algebra gives $E_n=-\frac{\mu k^2}{2\hbar^2n^2}$ with degeneracy $n^2$: the $\ell$-independence of hydrogen levels is the quantum $SO(4)$ symmetry (compare Zettili Section 6.3.5).

**Perturbations of the $1/r$ law [Could]**
- A small extra term (relativistic correction, $1/r^2$ term, another planet) makes $\mathbf A$ precess slowly; the precession rate is the average of the perturbation over the orbit (see Module 20).

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Goldstein 3.1 to 3.4 and 3.7 (fast); derive the orbit equation |
| B1 | Exercises 1 to 5 |
| A2 | Goldstein 3.9; derive $\dot{\mathbf A}=0$ and $A^2=\mu^2k^2+2\mu EL^2$ |
| B2 | Exercises 6 to 10 (7 and 8 after Module 09); cheat sheet |

## Derive from scratch (A sessions, book closed)

1. The reduction of the two-body problem and the effective potential.
2. The Kepler orbit equation by integrating $\dot r$ and $\dot\phi$.
3. The conservation of $\mathbf A$ for $V=-k/r$.
4. $A^2=\mu^2k^2+2\mu EL^2$.
5. The orbit equation from $\mathbf A\cdot\mathbf r$ (no integration).

## Bare-minimum exercises (with expected results)

1. **Reduced mass:** for the Earth-Sun system the reduced mass differs from the Earth's mass by a fraction $\approx3\times10^{-6}$.
2. **Stability:** for $V=-k/r^n$ stable circular orbits exist only for $n<2$.
3. **Kepler orbit:** derive $r=\frac{p}{1+e\cos\theta}$ with $p=\frac{L^2}{\mu k}$; show $E=-\frac{k}{2a}$ and $a=\frac{p}{1-e^2}$.
4. **Period:** show $T=2\pi\sqrt{\mu a^3/k}$ using the areal velocity $\frac{L}{2\mu}$ and the area $\pi ab$.
5. **Virial theorem:** verify $\langle T\rangle=-E$ for an elliptical Kepler orbit by time-averaging.
6. **LRL conservation:** compute $\dot{\mathbf A}$ explicitly using $\dot{\mathbf p}=-\frac{k}{r^2}\hat{\mathbf r}$ and $\mathbf L=\mu\mathbf r\times\dot{\mathbf r}$; the two terms cancel.
7. **Brackets (after Module 09):** compute $\{L_i,A_j\}$ and $\{A_i,A_j\}$; confirm $\{A_i,A_j\}=-2\mu H\epsilon_{ijk}L_k$.
8. **Bound-state algebra (after Module 09):** with $\mathbf D=\mathbf A/\sqrt{-2\mu H}$ show $\{D_i,D_j\}=\epsilon_{ijk}L_k$ and that $\mathbf J_\pm=\frac12(\mathbf L\pm\mathbf D)$ satisfy $\{J_{\pm i},J_{\pm j}\}=\epsilon_{ijk}J_{\pm k}$, $\{J_{+i},J_{-j}\}=0$; show $\mathbf J_+^2=\mathbf J_-^2$ (from $\mathbf L\cdot\mathbf D=0$).
9. **Precession from a perturbation:** for $V=-\frac kr-\frac\beta{r^2}$ the orbit is $r=\frac{p'}{1+e\cos(\gamma\phi)}$ with $\gamma=\sqrt{1-\frac{2\mu\beta}{L^2}}$; the perihelion advances by $\Delta\phi\approx\frac{2\pi\mu\beta}{L^2}$ per orbit for small $\beta$.
10. **Bertrand (statement):** only $V\propto-1/r$ and $V\propto r^2$ have all bounded orbits closed; state why the first has an extra conserved vector and the second has $\mathfrak{su}(3)$ symmetry (awareness).

## Optional extension

Quantize the algebra: replace $\{,\}\to\frac{1}{i\hbar}[,]$ and with $\mathbf J_\pm$ obeying two commuting $\mathfrak{su}(2)$ algebras with equal Casimirs $j(j+1)\hbar^2$ show $E_n=-\frac{\mu k^2}{2\hbar^2n^2}$ with $n=2j+1$ and degeneracy $(2j+1)^2=n^2$.

## Pitfalls

- Treating $\mathbf A$ as a coincidence rather than a symmetry.
- Applying the LRL vector to any central potential (it is conserved only for $1/r$).
- Forgetting the factor $-2\mu H$ in $\{A_i,A_j\}$ and its sign for bound versus unbound orbits.

## Gate questions

1. Why does the LRL vector explain that Kepler orbits close?
2. What symmetry group do $\mathbf L$ and $\mathbf D$ generate for bound Kepler motion?
3. How does the classical algebra explain the $n^2$-fold degeneracy of hydrogen?

## One-page cheat sheet contents

Orbit equation, $a,e,E$ relations; Kepler's third law; $\mathbf A$ and its properties; the bracket algebra; $\mathbf J_\pm$ decomposition.
