# Module 07: Chapter 3b, quantisation (★★, Week 9; Protocol A)

**Books:** Klauber Ch. 3 (quantisation sections); second source: Lancaster and Blundell, Tong.
**Time:** 1 week.

## Why this matters

Promotion of coefficients to operators. Commutation relations. Ladder structure, Fock space, the number operator. The Hamiltonian and its zero-point term. Normal ordering. **Calculations 3 and 4** live here, and **direction matters** for calculation 3: most treatments *postulate* the ladder commutators and check consistency (the easy way round, leaving the ladder algebra an assumption); going forward from the canonical commutator is the honest derivation and is where you find out whether calculation 2 was really done.

## Diagnostic (40 minutes, no notes)

1. Derive $[a(\mathbf k),a^\dagger(\mathbf k')]=\delta^3(\mathbf k-\mathbf k')$ from $[\phi(\mathbf x),\pi(\mathbf y)]=i\delta^3(\mathbf x-\mathbf y)$ using the inversion of Module 06.
2. Reduce $H=\int d^3x\,\mathcal H$ to $H=\int d^3k\,\omega\left[a^\dagger a+\tfrac12[a,a^\dagger]\right]$ and identify the divergent term.
3. Show $\delta^3(0)=\frac{V}{(2\pi)^3}$.
4. Define the number operator and show $[N,a^\dagger]=a^\dagger$.
5. Construct a two-particle state and verify its symmetry.

## Prerequisites

Module 06 (especially calculations 1, 2 and 8).

## Detailed topics (checklist)

- Quantisation: $\phi,\pi\to$ operators with equal-time commutators $[\phi(\mathbf x,t),\pi(\mathbf y,t)]=i\delta^3(\mathbf x-\mathbf y)$, $[\phi,\phi]=[\pi,\pi]=0$; **calculation 3:** $a(\mathbf k)=\frac{e^{i\omega t}}{\sqrt{2\omega(2\pi)^3}}\int d^3x\,e^{-i\mathbf k\cdot\mathbf x}[\omega\phi+i\pi]$ and $[a(\mathbf k),a^\dagger(\mathbf k')]=\delta^3(\mathbf k-\mathbf k')$, $[a,a]=0$.
- **Calculation 4:** the Hamiltonian $H=\int d^3k\,\omega\left[a^\dagger a+\tfrac12[a,a^\dagger]\right]$; use $\int d^3x\,e^{i(\mathbf k-\mathbf k')\cdot\mathbf x}=(2\pi)^3\delta^3(\mathbf k-\mathbf k')$ several times over a product of two integrals, keeping primed and unprimed labels straight; **the divergent term contains $\delta^3(0)$, which is not a mystery: it is the spatial volume** $\delta^3(0)=\frac{V}{(2\pi)^3}$; recognising it as a volume divergence is half of what Chapter 10 later argues about.
- Fock space: vacuum $a|0\rangle=0$; $N=\int d^3k\,a^\dagger a$; $|\mathbf k\rangle=a^\dagger(\mathbf k)|0\rangle$ with $\langle\mathbf k|\mathbf k'\rangle=\delta^3(\mathbf k-\mathbf k')$; multi-particle states and Bose symmetry; normal ordering $:H:$.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Calculation 3: derive the ladder commutators from the field commutators |
| B1 | Exercises 1 and 2 |
| A2 | Calculation 4: the Hamiltonian and its zero-point term |
| B2 | Exercises 3 to 5 |
| A3 | Fock space; multi-particle states |
| B3 | Exercises 6 to 10 |

## Derive from scratch

1. Calculation 3 in full.
2. Calculation 4 in full, with the $\delta^3(0)$ bookkeeping.
3. $[H,a^\dagger]=\omega a^\dagger$ and the energy of a Fock state.
4. The two-particle state and its norm.
5. The conversion of $\delta^3(0)$ to $V/(2\pi)^3$.

## Exercises

1. **[T] Calculation 3:** $[a(\mathbf k),a^\dagger(\mathbf k')]=\frac{1}{2\omega(2\pi)^3}\int d^3xd^3y\,e^{-i\mathbf k\cdot\mathbf x+i\mathbf k'\cdot\mathbf y}\left\{-i\omega[\phi(\mathbf x),\pi(\mathbf y)]+i\omega[\pi(\mathbf x),\phi(\mathbf y)]\right\}=\frac{2\omega}{2\omega(2\pi)^3}\int d^3x\,e^{-i(\mathbf k-\mathbf k')\cdot\mathbf x}=\delta^3(\mathbf k-\mathbf k')$.
2. **[T]** $[a,a]=0$ follows from $[\phi,\phi]=[\pi,\pi]=0$ and the combination $\omega\phi+i\pi$; show the $[\phi,\pi]$ terms cancel.
3. **[T] Calculation 4:** the zero-point energy is $E_0=\tfrac12\int d^3k\,\omega_{\mathbf k}\,\delta^3(0)=V\int\frac{d^3k}{(2\pi)^3}\tfrac12\omega_{\mathbf k}$ (the sum of $\tfrac12\omega$ over modes: the oscillator zero-point energies), UV divergent.
4. **[T] Normal ordering:** $:H:=\int d^3k\,\omega_{\mathbf k}a^\dagger(\mathbf k)a(\mathbf k)$; state what is lost and what is kept.
5. **[T] Ladder relations:** $[N,a^\dagger(\mathbf k)]=a^\dagger(\mathbf k)$ and $[H,a^\dagger(\mathbf k)]=\omega_{\mathbf k}a^\dagger(\mathbf k)$, so $H|\mathbf k\rangle=\omega_{\mathbf k}|\mathbf k\rangle$.
6. **[T] Momentum operator:** $\mathbf P=\int d^3k\,\mathbf k\,a^\dagger a$ (after normal ordering) and $\mathbf P|\mathbf k\rangle=\mathbf k|\mathbf k\rangle$.
7. **[T] Two-particle state:** $|\mathbf k_1\mathbf k_2\rangle=a^\dagger(\mathbf k_1)a^\dagger(\mathbf k_2)|0\rangle$ is symmetric under exchange, has energy $\omega_1+\omega_2$ and $\langle\mathbf k_1'\mathbf k_2'|\mathbf k_1\mathbf k_2\rangle=\delta^3(\mathbf k_1-\mathbf k_1')\delta^3(\mathbf k_2-\mathbf k_2')+\delta^3(\mathbf k_1-\mathbf k_2')\delta^3(\mathbf k_2-\mathbf k_1')$.
8. **[C] What is quantised?** The field, the modes, or the state space? Answer carefully; the sloppy version of this is a common source of confusion.
9. **[C] Zero-point energy:** what is observable about the divergent vacuum energy, and why does normal ordering not settle the question (Chapter 10 returns to this)?
10. **[C] Explain-it paragraph:** how a quantum field produces particles with definite momenta, no equations.

## Optional extension

Compute $[H,\phi(x)]$ and show the Heisenberg equation reproduces the KG equation.

## Pitfalls

- Going *backward* (postulating $[a,a^\dagger]=\delta$ and verifying) and leaving the ladder algebra as an assumption.
- Losing $\delta^3(0)$ (the volume) in the Hamiltonian reduction.
- Mixing relativistic and non-relativistic state normalisations ($2\omega$ factors).

## Gate questions

1. Why must the ladder commutators follow from the field commutators and not be assumed?
2. Where does $\delta^3(0)$ come from?
3. What does $[H,a^\dagger]=\omega a^\dagger$ imply?

## One-page cheat sheet contents

Ladder commutators and their derivation; $H$ with zero-point term; Fock states; two-particle state and norm.
