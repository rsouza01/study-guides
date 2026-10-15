# Module 23: Synthesis, mini-projects and mock exam

**Books:** all, plus your written module deliverables and your `error_log.md`.
**Time:** 3 weeks (six sessions).

## Goal

Decide with evidence whether you can now *do* electrodynamics, not just discuss it: set up and solve boundary-value and Green-function problems, move between frames with the field tensor, derive Maxwell's equations from an action, and compute radiation. The remaining deliverable is a consolidated document; the projects are for the compact-object goal.

## Part 1: exit criteria (the guide's seven abilities)

After this guide you should be able to, cold:

1. Construct the Green function for a linear differential operator in any separable geometry, including the radial reduction and jump condition (Modules 05, 07, 08).
2. Explain retarded, advanced and Feynman as three contour choices and state the physical boundary condition each encodes (Module 11).
3. Write Maxwell covariantly, transform fields between frames and compute with the invariants (Modules 14, 15).
4. Derive Maxwell from an action; construct $T^{\mu\nu}$ from that action; perform the symmetrization (Modules 17, 18).
5. Derive the Proca equation, explain why the mass term breaks gauge invariance and recover the Yukawa potential: you will have solved the sourced Klein-Gordon equation before opening a QFT chapter on it (Module 17).
6. Trace causality $\to$ analyticity $\to$ dispersion relations (Module 19).
7. Derive Lienard-Wiechert from the retarded Green function and get the synchrotron spectrum out of it (Modules 20 to 22).

Items 1, 2 and 5 pay off immediately in Klein-Gordon and Dirac. Item 7 pays off immediately in compact-object radiation modelling.

## Part 2: the master blank-page gate (no notes, 15 to 25 minutes each)

Mark each when you can do it cold; do three per session, in a different order each time.

**Ramp and Thread A (Green functions)**
1. Green's second identity from the divergence theorem (under five minutes).
2. The formal solution with $G_D$; the Neumann subtlety; $G_D(\mathbf x,\mathbf x')=G_D(\mathbf x',\mathbf x)$.
3. $G_D$ for the sphere; the Poisson kernel.
4. **Construct $g_\ell(r,r')$ from scratch** (free space and between concentric spheres).
5. **Derive $G_{\rm ret}$ from the Fourier integral, contour and all**; reduce to $\frac1R\delta(t'-t+R/c)$; rewrite in invariant form. *Twenty minutes.*

**Thread C (gauge, action, conservation)**
6. The Lorenz-gauge wave equations; residual freedom; $4-1-1=2$ degrees of freedom.
7. Poynting's theorem and the Maxwell stress tensor.
8. Maxwell from the action; why the homogeneous equations need no variation.
9. The Proca equation: forced Lorenz condition, Yukawa, 3 degrees of freedom.
10. $T^{\mu\nu}_{\rm can}$, the Belinfante improvement, $\Theta^{00}$, $\Theta^{0i}$, $\Theta^\mu{}_\mu=0$.

**Thread B (covariance)**
11. The Lorentz transformation from the two postulates.
12. Index-placement rule; $\Lambda^T\eta\Lambda=\eta$; $p\cdot p=m^2c^2$.
13. The generators, closure, the $\mathbf A_\pm$ decomposition.
14. $F^{\mu\nu}$ as a matrix; covariant Maxwell; field transformation laws.
15. The two invariants and when a frame with $\mathbf E=0$ or $\mathbf B=0$ exists.

**Radiation**
16. The Lienard-Wiechert potentials with the Jacobian $(1-\hat{\mathbf n}\cdot\boldsymbol\beta)$.
17. Velocity and acceleration fields; why only the latter reaches infinity.
18. Larmor and its relativistic generalization.
19. Thomson cross-section; $L_{\rm Edd}$.
20. Synchrotron: $\omega_c$, power, cooling time, spectral index.
21. Kramers-Kronig from causality.
22. The self-energy divergence and $r_e$.

**Passing criterion:** at least 18 of 22 cleanly, and the remaining four understood after one reading. Items 4, 5 and 9 are not negotiable.

## Part 3: the synthesis document, `em-field-theory-summary.md` (8 to 12 pages)

Write in your own words, one section per thread:
1. **Thread A:** from $\nabla^2G=-4\pi\delta^3$ with boundary conditions, through $g_\ell$ and the jump condition, to $\Box G=-4\pi\delta^4$ and the choice of contour; what each prescription means physically; where it becomes the Feynman propagator.
2. **Thread B:** from the postulates to $F^{\mu\nu}$, the Lorentz algebra and $(j_-,j_+)$; why spinors exist.
3. **Thread C:** from the potentials and gauge freedom to the action; $T^{\mu\nu}$; the Proca equation and the Yukawa potential; the mass term and gauge invariance.
4. **Radiation:** Larmor, LW, synchrotron, with the compact-object mapping.
5. **The correspondence table** (below) with one line per row on what carries over to QFT and what is new.

| Classical (Jackson) | Quantum (QFT) |
| --- | --- |
| $G_D$ and boundary conditions (Ch. 1 to 3) | Propagators and their boundary conditions |
| Radial $g_\ell$ via Wronskian jump (3.9) | Radial KG/Dirac propagators; partial waves |
| Retarded $G$, contour choice (6.4, 12.11) | Feynman propagator, $i\epsilon$, antiparticles |
| Gauge freedom (6.3) | Gauge invariance; ghost and gauge-fixing machinery |
| Maxwell stress tensor (6.7, 12.10) | Noether $T^{\mu\nu}$; Belinfante improvement |
| P, T on fields (6.10) | Discrete symmetries, CPT |
| Lorentz generators (11.7) | $(j_-,j_+)$ irreps; why spinors exist |
| Proca and Yukawa (12.8) | Sourced Klein-Gordon; massive vector; Higgs |
| $\mathbf E\cdot\mathbf B$ invariant (11.9) | The $\theta$-term; strong CP |
| Kramers-Kronig (7.10) | Dispersion relations, amplitude analyticity |
| Virtual quanta (14.8) | Virtual particles; parton distributions |
| Thomson cross-section (14.7) | Compton scattering, low-energy limit |
| Self-energy divergence (16.2) | Renormalization |
| Born approximation (Appendix A of the guide) | First order in the Dyson series |

## Part 4: mini-projects (Python, standalone; the first and last are the two to fight for)

### Project 1: Green functions of the wave equation
- **Task:** numerically evaluate $\int dk_0\frac{e^{-ik_0t}}{k_0^2-|\mathbf k|^2+i\epsilon}$ for the three contour prescriptions (Module 11).
- **Checks:** retarded $=\theta(t)\frac{\sin kt}{k}$ (up to a factor $-\pi$ or $2\pi$ in your normalization), advanced with $\theta(-t)$, Feynman $\propto\frac{i}{2k}e^{-ik|t|}$; the limit $\epsilon\to0$ reproduces the analytic results.

### Project 2: radial Green function
- **Task:** implement $g_\ell(r,r')$ for free space and for the two-sphere region (Module 08); sum the series and verify against $\frac{1}{|\mathbf x-\mathbf x'|}$; plot convergence versus $\ell_{\max}$ and its failure at coincident points.

### Project 3: four-vector library and Wigner rotation
- **Task:** Minkowski product, boosts, composition, invariant mass; reproduce a threshold-energy calculation and the Wigner rotation of two perpendicular boosts (expected angle $0.143$ rad for $\beta=0.5$ each).

### Project 4: the synchrotron spectrum from Lienard-Wiechert
- **Task:** the LW fields for a circular orbit at several $\gamma$; angular power distribution and the collapse into the $1/\gamma$ cone; the FFT spectrum with the $\omega^{1/3}$ rise and the exponential cutoff above $\omega_c$ (Modules 20 and 22). Reusable for compact-object modelling.

## Part 5: mock exam (4 hours, closed book)

| Section | Content | Time |
| --- | --- | --- |
| A | One boundary-value problem solved with a Green function or separation of variables (sphere or cylinder) | 40 min |
| B | One contour/retarded Green function derivation (including the 1D or 2D case) | 40 min |
| C | One gauge/potential/conservation problem (Lorenz gauge, Poynting, stress tensor) | 30 min |
| D | One covariance problem (field transformation, invariants, a frame with $\mathbf E=0$) | 35 min |
| E | One action problem (Maxwell or Proca from $\mathcal L$, degrees of freedom) | 35 min |
| F | One radiation problem (Larmor/LW/synchrotron numbers for a compact-object example) | 40 min |
| G | One short essay: causality, analyticity and the choice of contour | 20 min |

Grade with a rubric: 2 points for the setup, 2 for the key step, 1 for the result or interpretation. Aim for 70 percent or more.

## Part 6: what to do if you fall short

| Weak area | Fix |
| --- | --- |
| Vector calculus and integrals | Redo Module 01 extra exercises (16.3 #35, 16.5 #29, #33, #34, 16.7 #45) |
| Delta functions and contours | Redo Module 02 exercises 1 to 8 |
| Electrostatics fundamentals | Redo Module 03 warm-ups and Module 04 images |
| Green functions | Redo Module 05 and 07 derivations 1 to 4 |
| Separation of variables | Redo Module 06 exercises 2, 3, 6 |
| Magnetostatics, Faraday | Redo Module 09 and 10 warm-ups |
| Wave-equation Green functions | Redo Module 11 derivations until the gate takes 20 minutes |
| Covariance | Redo Modules 13 to 15 derivations 1 to 4 |
| Action principle | Redo Module 17 derivations 1 to 4 |
| Radiation | Redo Modules 20 to 22 derivations 1 to 3 |

Use `error_log.md` as the diagnostic: any step that appears three times is a math-patch drill, not a physics problem.

## Pitfalls

- Treating the gate as recognition rather than recall.
- Spending all the time on the projects and none on closed-book derivations.
- Not updating the error log (the log is the instrument that shows which math is still missing).

## Gate questions

1. Which of the three threads is strongest and which weakest, and what is the plan for the weakest?
2. Which single derivation do you most want to be able to do cold in a year?
3. What would a second pass of this guide cut or add?
