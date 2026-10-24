# Complex Analysis for Electrodynamics and Mechanics: a Study Guide

*From Ávila's* Variáveis Complexas e Aplicações *to the retarded, advanced and Feynman Green functions*

Rodrigo Alvares de Souza, October 2026

**Target.** The complex analysis needed for the electrodynamics and mechanics guides, with one hard deadline: the contour integral that produces the retarded, advanced and Feynman Green functions (EM guide, Module 11). Secondary targets: Kramers–Kronig (EM Module 19) and a clean foundation for the QFT track.

**Starting point, stated honestly.** Complex analysis is your weak spot, and you want to follow this path rather than skim it. So every module has a fast exit (a skip-test), a tier system (Must, Should, Could), a method card for each problem type, ten exercises with expected results, and a blank-page gate.

**Format.** This overview, one file per module, and an appendix.

| File | Content |
|---|---|
| [README.md](README.md) | This overview |
| [ca01-complex-numbers.md](ca01-complex-numbers.md) | Complex numbers, polar form, roots, the exponential |
| [ca02-analytic-functions-cauchy-riemann.md](ca02-analytic-functions-cauchy-riemann.md) | Analytic functions and the Cauchy–Riemann equations |
| [ca03-elementary-functions-logarithm.md](ca03-elementary-functions-logarithm.md) | Elementary functions, the logarithm, $z^a$, branch cuts |
| [ca04-contour-integrals-cauchy-theorem.md](ca04-contour-integrals-cauchy-theorem.md) | Contour integrals and Cauchy's theorem |
| [ca05-cauchy-formula-harmonic-functions.md](ca05-cauchy-formula-harmonic-functions.md) | Cauchy's integral formula, maximum modulus, harmonic functions |
| [ca06-taylor-laurent-series.md](ca06-taylor-laurent-series.md) | Taylor and Laurent series |
| [ca07-singularities-residues.md](ca07-singularities-residues.md) | Singularities and the residue theorem |
| [ca08-improper-integrals-jordan-principal-value.md](ca08-improper-integrals-jordan-principal-value.md) | Improper integrals, Jordan's lemma, principal values |
| [ca09-capstone-three-green-functions.md](ca09-capstone-three-green-functions.md) | Capstone: the three Green functions, Wick rotation, the gate |
| [99-appendix.md](99-appendix.md) | Parked material, the QFT outline (Part 2), vocabulary, conventions, tracking |
| [tools/verify_expected_results.py](tools/verify_expected_results.py) | Script that checks the expected results quoted in the exercises |

Books: **Ávila**, *Variáveis Complexas e Aplicações* (primary); **Churchill and Brown**, *Complex Variables and Applications* (drill problems and English vocabulary); **Stewart** (prerequisites: 16.2, 16.4, Chapter 11).

> **Honesty notes.**
>
> 1. This replaces my earlier "Part 1" (seven weeks) and the informal "Part 2". Part 2 is now an outline in the appendix and becomes modules after the CA09 gate.
> 2. Ávila page numbers come from the table of contents you sent. I have not seen Ávila's exercise lists, only the pages where they sit. So each module points you to his exercise sets by page, and adds ten described exercises with expected results. I dropped the edition and publisher I had written before: I had no basis for them.
> 3. Churchill chapter numbers are from memory for the 8th and 9th editions. Verify them against your copy.
> 4. The numerical and closed-form expected results are checked by `tools/verify_expected_results.py`. Proof-type exercises say what to show and have no number to check.
> 5. The time estimates use your real pace (you rebuild each section on paper), not the faster pace behind my first estimate of 25 hours. That is why the totals below are larger.

## 1. The honest accounting

A session is 2 to 3 hours, as in your other guides.

| Path | Sessions | Hours | What you get |
|---|---|---|---|
| Full path | about 33 | about 83 | Everything below, including the harmonic-function and Dirichlet material |
| Deadline path | about 25 | about 63 | Exactly the chain to EM Module 11: CA01 (skip-test), CA02, CA03 (light), CA04, CA05 (Must), CA06, CA07, CA08, CA09 |
| Shortcut lane | 2 | 5 | Two method cards, to get through EM Module 02 if it arrives first (section 3) |

At one session a week the deadline path ends about when EM Module 11 starts (week 23 or so on the full EM path). A few weeks of overlap cost nothing: EM Modules 09 and 10 do not use contours.

## 2. Module list

| # | Module | Ávila pages | Churchill (verify) | Sessions (full / Must) | Priority | Payoff |
|----|------------------------|---------|--------|----------|----------|--------------------------|
| CA01 | Complex numbers, roots, exponential | 1–33 | 1 | 2 / 1 | skip-test | $e^{i\theta}$, roots of unity, point sets |
| CA02 | Analytic functions, Cauchy–Riemann | 34–60 | 2 | 4 / 3 | core | Analyticity as a strong condition; $\lvert f'\rvert^2$ is a Jacobian |
| CA03 | Elementary functions, logarithm, branch cuts | 61–74 | 3 | 2 / 1 | should | Multivaluedness; why cuts exist |
| CA04 | Contour integrals, Cauchy's theorem | 75–101 | 4 | 4 / 4 | core, star | Green's theorem becomes Cauchy; the master integral |
| CA05 | Cauchy's formula, maximum modulus, harmonic functions | 101–117 | 4 | 5 / 2 | core (Must part) | Values from boundaries; Earnshaw |
| CA06 | Taylor and Laurent series | 118–150 | 5 | 6 / 4 | core, star | Laurent is how residues are defined |
| CA07 | Singularities and residues | 151–161 | 6 | 4 / 4 | core, two stars | Residue theorem |
| CA08 | Improper integrals, Jordan's lemma, principal values | 161–169, 173–174 | 7 | 4 / 4 | core, three stars | Closing contours; indentation; Kramers–Kronig |
| CA09 | Capstone and gate | none | 7 | 2 / 2 | core, three stars | The three Green functions |

The three-star modules carry the guide. If time collapses, protect CA07 to CA09 at the cost of anything else.

**Dependency map.**

```
CA01 -> CA02 -> CA03 (light)
          \
           -> CA04 -> CA05 -> CA06 -> CA07 -> CA08 -> CA09
```

CA06 needs Stewart Chapter 11 (series of constants, radius of convergence). Its skip-test tells you whether the one-session patch is needed.

## 3. How this plugs into the other guides

| Here | Needed by | Note |
|---|---|---|
| CA04 (contours, ML-estimate) | EM Module 02 (recipe), EM Module 11 | Needs Stewart 16.2 and 16.4, which you have |
| CA07, CA08 (residues, closing contours) | EM Module 02 exercises 6 to 8 | See the shortcut lane below |
| CA08, CA09 | EM Module 11 (hard deadline), Module 19 (Kramers–Kronig) | |
| CA06 (Laurent, binomial series) | EM Modules 06 and 07 (Legendre generating function) | |
| CA05 (harmonic functions, maximum modulus) | EM Modules 04 and 05 | Read after Jackson's uniqueness proof, as a second proof |
| CA09 | Zettili (scattering, propagators) | |
| Part 2 (appendix) | Mechanics guide Module 16 (stationary phase), QFT | Not before the CA09 gate |

**Shortcut lane.** If EM Module 02 arrives before you reach CA07 and CA08, do only this: read the residue method card in CA07 and the "closing a contour" card in CA08, do EM Module 02's exercises 6 and 7, then go back to the sequence here. Do not skip CA08 itself.

## 4. The routine for a contour problem (the five steps)

1. **Draw.** Plot the poles and the contour in the plane. Mark which half-plane the contour closes in.
2. **State what happens at infinity.** For a rational function use the ML-estimate. For $e^{iax}g(x)$ use Jordan's lemma, and read the sign of $a$ to choose the half-plane.
3. **Locate the singularities**, including where $\pm i\epsilon$ puts each pole. Decide whether each lies inside, outside or on the contour.
4. **Compute residues** with the method card. Keep symbols until the end.
5. **Check.** Test a symmetric case, a limit ($x\to0$, $\epsilon\to0$), and one number you know. Run the numerical integral if the answer is a closed form.

**Stuck protocol.** After 20 minutes without progress, write down which step you are stuck on (never "I don't know how to do the problem"). Look only at the next line of the solution or the method card, then close the book and continue. Log the step in `notes/error_log.md` and redo the problem two days later. If the same step appears three times, redo the relevant module drill.

## 5. Schedule and tiers

Same rules as your other guides. A week off costs nothing. After a long gap, use the re-entry protocol: redo the last two derivations of the previous module from a blank page. A 12-hour week pulls the next module's first session forward. Inside each module, tiers: **Must** (core derivations, exercises 1 to 5), **Should** (6 to 8), **Could** (9 to 10 and the extension). Dropping to Must always leaves a coherent module.

Never skip: CA04's Green's-theorem proof, CA07 and CA08 in full, and the CA09 gate.

## 6. Ground rules

1. Derive before you read the answer.
2. One cheat sheet per module, one page.
3. Keep `notes/error_log.md` and a one-line weekly log (hours, sections, exercises).
4. Do Ávila's own exercise sets first (pages are listed in each module; his answers are in the book). The ten exercises in each module are the extra with expected results.
5. Numerical checks are for checking, not a project. `tools/verify_expected_results.py` shows how.

## 7. What this guide leaves out, and where it goes

Branch cuts inside integrals (keyhole contours), Riemann surfaces, analytic continuation, the gamma function, saddle-point methods, fluid dynamics, and conformal mapping. The appendix lists each with its Ávila pages and the cost of restoring it.

## 8. How this connects to your other work

* **EM guide:** table in section 3.
* **Mechanics guide:** no dependency before Module 16, where stationary phase appears (Part 2).
* **Linear algebra and Fourier path (informal):** Figueiredo Chapter 6 (Fourier transform, convolution) is the real-variable side of CA08 and CA09.
* **Conventions** (Fourier transform, time dependence $e^{-i\omega t}$): appendix, section 4. They match EM Module 02.
