# Appendix: parked material, the QFT outline (Part 2), vocabulary, conventions and tracking

## 1. What this guide leaves out, and the cost of restoring it

All page numbers are Ávila's, from the table of contents you sent.

| Parked | Ávila pages | Why it is parked | Cost to restore | Restore when |
|---|---|---|---|---|
| Multivalued integrands (keyhole contours) | 169 to 173 | Needs branch cuts inside integrals; not used by CA08 or CA09 | about 2 sessions | Part 2, module P1 |
| Logarithmic residues, argument principle | 175 to 178 | Counting zeros and poles; bound states and dispersion theory | about 1 session | Part 2, module P1 |
| Analytic continuation | 181 to 192 | Wick rotation and continuing amplitudes; no effect on EM | about 3 sessions | Part 2, module P3 |
| Riemann surfaces | 193 to 197 | What a branch cut really is | about 1 to 2 sessions | Part 2, module P2 |
| Functions defined by integrals; the gamma function; continuation to the whole plane | 198 to 202 | Dimensional regularization | about 2 sessions | Part 2, module P4 |
| Fluid dynamics | Chapter 7, 204 to 242 | The same mathematics as 2D electrostatics, no new machinery | optional | only for intuition |
| Conformal mapping, invariance of Laplace's equation, electrostatic potential | 245 to 265 (see 248 and 260 to 265) | A second method for the 2D problems of EM Modules 04 to 06 | about 4 sessions | after EM Module 04, as a second route |

Dirichlet and Neumann problems (pp. 114 to 117) are inside CA05 as a "Could" item.

## 2. Part 2 outline: complex analysis for QFT (to be expanded into modules after the CA09 gate)

In Part 1 singularities are obstacles to route around. In Part 2 they carry physics: a pole is a stable particle, a branch point is a production threshold, and their locations are fixed by causality and unitarity rather than by convention. Prerequisite: the CA09 gate. No deadline; the natural slot is the bridge before QFT, or interleaved with the first chapters of Klauber. Each module below becomes a file with the same skeleton as CA01 to CA09.

| # | Module | Source | Sessions | What it becomes in QFT |
|---|---|---|---|---|
| P1 | Multivalued integrands, keyhole contours, the argument principle | Ávila pp. 169 to 178 | 3 | Cuts in propagators; counting bound states |
| P2 | Riemann surfaces | Ávila pp. 187 to 197 | 2 | A cut is a choice, a branch point is physics; thresholds |
| P3 | Analytic continuation and Wick rotation | Ávila pp. 181 to 192 | 3 | Euclidean field theory; continuing amplitudes |
| P4 | The gamma function and its continuation | Ávila pp. 198 to 202 | 2 | Dimensional regularization: the divergence becomes a pole of $\Gamma$ |
| P5 | Saddle point and stationary phase | **Not in Ávila.** Bender and Orszag, Chapter 6; or Boas | 3 | The semiclassical limit; WKB; instantons. Protect this one: it proves the claim in Mechanics Module 16 that classical mechanics is the stationary-phase approximation to quantum mechanics |
| P6 | Synthesis: analyticity as physics | none | 2 | The singularity dictionary: pole, resonance, branch point, cut; unitarity and the discontinuity across a cut |

One exercise from P3 you can already set up: take your CA09 capstone, the three prescriptions, and rotate the $\omega$ contour by $90^\circ$. Which prescription lets you rotate without crossing a pole? (CA09, exercise 4.)

## 3. Vocabulary (Portuguese to English)

Jackson, Churchill and every QFT text use the English terms, so use them from the start.

| Portuguese (Ávila) | English |
|---|---|
| função analítica | analytic (holomorphic) function |
| equações de Cauchy–Riemann | Cauchy–Riemann equations |
| integral de contorno | contour integral |
| teorema de Cauchy | Cauchy's theorem (Cauchy–Goursat) |
| fórmula integral de Cauchy | Cauchy's integral formula |
| série de potências, de Taylor, de Laurent | power series, Taylor series, Laurent series |
| singularidade isolada, removível, essencial | isolated, removable, essential singularity |
| polo (de ordem $m$) | pole (of order $m$) |
| resíduo; teorema do resíduo | residue; residue theorem |
| lema de Jordan | Jordan's lemma |
| valor principal (de Cauchy) | (Cauchy) principal value |
| ramo; ponto de ramificação; corte | branch; branch point; branch cut |
| conexo; simplesmente conexo | connected; simply connected |
| aberto; fechado; fronteira | open; closed; boundary |
| raio de convergência | radius of convergence |
| convergência uniforme | uniform convergence |
| função harmônica; conjugada harmônica | harmonic function; harmonic conjugate |
| princípio do módulo máximo | maximum modulus principle |
| continuação analítica | analytic continuation |
| superfície de Riemann | Riemann surface |
| zero de ordem $m$ | zero of order $m$ |
| contorno indentado | indented contour |
| estimativa $ML$ | ML-estimate |

## 4. Conventions (so that the texts agree)

* **Fourier transform (space):** $\tilde f(k)=\int f(x)e^{-ikx}\,dx$ and $f(x)=\int\frac{dk}{2\pi}\tilde f(k)e^{ikx}$. This is EM Module 02's convention. Griffiths, Jackson and Figueiredo differ by factors of $2\pi$ and signs; state yours whenever you cross-read.
* **Time dependence:** $e^{-i\omega t}$ (the physics convention, used by Jackson). Then $\tilde f(\omega)=\int f(t)e^{i\omega t}\,dt$, and a causal response function is analytic in the **upper** half-plane. Engineering texts use $e^{+j\omega t}$, which moves the analyticity to the lower half-plane. Check which one a source uses before you quote a sign.
* **Orientation:** a contour is positively oriented when it runs counterclockwise (region on the left). Closing in the lower half-plane gives $-2\pi i$ times the residues.
* **Branch of $\log$:** principal value with $-\pi<\arg z\le\pi$ unless the problem says otherwise. State your choice in the first line of any problem that needs one.
* **Greek and symbols:** your Stewart notes use $\partial_u$ for partial derivatives; keep that here.

## 5. Tracking

**`notes/error_log.md`.** One line per stuck step: date, module, exercise, the step ("which half-plane to close in", "residue at a double pole", "sign under clockwise orientation"), what resolved it. If the same step appears three times, redo that module's drill.

**One-line weekly log.** `YYYY-MM-DD, hours, modules/sections, exercises done`.

**Deliverables per module.** A file `notes/caNN-topic.md` with your blank-page derivations in your own hand and a "what surprised me" paragraph, the module's cheat sheet, and worked solutions to exercises 1 to 5.

**Re-entry protocol** (after two or more weeks off): redo the last two derivations of the previous module from a blank page, then continue.

**Verification script.** `tools/verify_expected_results.py` recomputes the numerical and closed-form expected results in the exercises. It needs `numpy`, `scipy`, `mpmath` and `sympy`. If an expected result in a module disagrees with your own calculation, run the script first and tell me which exercise: one of us has a mistake and I want to find it.
