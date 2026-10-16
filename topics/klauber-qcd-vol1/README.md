# Klauber Volume 1: A Second Pass: a Study Guide (build the machinery, then recover the concepts)

**Target:** a retained understanding of *SFQFT Vol. 1*, ending ready for Volume 2.
**Primary source:** R. D. Klauber, *Student Friendly Quantum Field Theory*, Vol. 1, **2nd edition**. A solutions booklet is recommended.
**Format:** this overview, one file per module (21 modules), and an appendix. It rebuilds your plan v0.4 in the multi-file format of your other guides: a diagnostic, prerequisites, a topic checklist, a reading plan, derivations, ten exercises with expected results where the exercise is computational (**[T]**) and prompts where it is conceptual (**[C]**), pitfalls, gate questions and a cheat sheet.

> **Honesty notes.**
> 1. **Numbering.** Verified from Klauber's site: Ch. 1 *Bird's Eye View*; Ch. 2 *Foundations*; **Part One: Free Fields** (Ch. 3 *Scalars*, 4 *Spinors*, 5 *Vectors*, 6 *Symmetry, Invariance, and Conservation*); **Part Two: Interacting Fields**, including Ch. 10 *The Vacuum Revisited*; **Part Three: Renormalization**; **Part Four: Application to Experiment**; **Addenda**, Ch. 18 *Path Integrals*. **Not verified:** numbers and titles between Ch. 6 and Ch. 18. Allocations below are by Part and content, so they survive renumbering. Write the real numbers in the margin when you start and confirm where Ch. 13 falls relative to the Part Three/Four boundary (the Phase 1/Phase 2 split sits there).
> 2. Numerical check values are from memory or recomputed by hand; verify them as you go.
> 3. **Conventions differ from other texts** (Klauber's discrete versus continuum normalisation, his sign and factor conventions). Every module that depends on a convention says so; write a dictionary card the first time it bites.
> 4. This guide does not interlock with your nuclear track (the two subjects are unrelated and the parallelism is only a use-of-hours decision). Your mechanics and electrodynamics guides *do* rehearse Module M (Green functions, contours) and the Noether/stress-tensor material; they are optional, not required.

---

## 1. The diagnosis (and why the plan has the shape it has)

You did every derivation through Chapter 13 and still did not get it. The corrected diagnosis: **in the free-field chapters the mathematical objects (contour integrals, distributions, Green functions, the invariant measure) were taken on faith rather than built.** From Chapter 4 onward every derivation was then performed correctly on symbols whose meaning had never become concrete: local correctness everywhere, understanding nowhere. Two consequences:

- **Part One is not review.** It is first-pass material, and the machinery underneath it (Module M) is material you have never properly seen.
- **Parts Two and Three** were derived competently and not absorbed: concept recovery, not re-derivation.

## 2. Two phases and the arithmetic

| Phase | Weeks | Content | Conditions |
| --- | --- | --- | --- |
| **Phase 1** | 1 to 29 | Ch. 1 to 13: Foundations, Module M, Part One, Part Two, Part Three | Absorber track: 5 to 7 h/week, budgeted by chapters |
| **Phase 2** | 30 on | Part Four and Ch. 18 (path integrals) | Undivided attention; the on-ramp to Volume 2 |

Part One and its prerequisites occupy 18 of the 29 weeks; Part Two gets 6 and Part Three 5, on the bet that a properly owned foundation makes the downstream chapters cheaper. If the bet is wrong you will know by Week 21 and Phase 2 can absorb the overflow.

## 3. Module list

| # | Module | Weeks | Protocol | Key output |
| --- | --- | --- | --- | --- |
| 01 | Ch. 1, Bird's Eye View | 1 | orientation | Your own map of QFT |
| 02 | Ch. 2, Foundations | 2 to 3 | A | Oscillator, action, Poisson brackets |
| 03 | **Module M1:** complex analysis for propagators (★) | 4 | A | Three contour pages |
| 04 | **Module M2:** distributions, Fourier, invariant measure (★) | 5 | A | $d^3k/2E$ derivation |
| 05 | **Module M3:** Green functions (★) and the Module M gate | 6 | A | The KG propagator, built |
| 06 | Ch. 3a: the KG equation and the classical scalar field (★★) | 7 to 8 | A | Calculations 1, 2, 8 |
| 07 | Ch. 3b: quantisation (★★) | 9 | A | Calculations 3, 4 |
| 08 | Ch. 3c: the propagator (★★) | 10 | A | Calculations 5, 6 |
| 09 | Ch. 3d: consolidation and the elasticity rule (★★) | 11 | A | Calculation 7 |
| 10 | Ch. 4, Spinors | 12 to 14 | A to B | Dirac field, anticommutators |
| 11 | Ch. 5, Vectors | 15 to 16 | A to B | Proca, photon, gauge |
| 12 | Ch. 6, Symmetry and conservation; Part One gate | 17 to 18 | A to B | Noether, $T^{\mu\nu}$ |
| 13 | Part Two a: interaction picture, Dyson, Wick | 19 to 20 | B | Contractions |
| 14 | Part Two b: QED rules and tree amplitudes | 21 to 22 | B | Rules, derived |
| 15 | Part Two c: cross sections and decay rates | 23 | B | One number |
| 16 | Part Two d: Ch. 10, The Vacuum Revisited; Part Two gate | 24 | B | Zero-point debate |
| 17 | Part Three a: divergences and regularization | 25 to 26 | B | Loop integral set up |
| 18 | Part Three b: counterterms, vacuum polarization, running | 27 to 28 | B | Running coupling |
| 19 | Part Three c: the programme assembled; Phase 1 gate | 29 | B | Renormalization page |
| 20 | Phase 2: Part Four, application to experiment | 30 on | new | $g-2$, Lamb shift |
| 21 | Phase 2: Ch. 18, Path integrals | 30 on | new | Three roads, one object |
| 99 | Appendix | | | Conventions, calendar |

## 4. Two protocols

**Protocol A: construction** (Modules 01 to 09 and, shading into B, 10 to 12). For material you are meeting properly for the first time. Derivations are primary:
1. **Read for the question**: what is this object for?
2. **Build it**: full derivation from the definitions; no accepting a step because it looks standard.
3. **Concretise**: for every new object produce a case you can evaluate explicitly and check against something known (an integral you can do two ways, a limit, a special case). **This step is the one that was missing the first time**: it turns a symbol into an object.
4. **State the choice**: every construction involves a choice (contour, branch, convention, ordering); name it and the alternative.
5. **Problems**: [T] and [C].

**Protocol B: concept recovery** (Modules 13 to 19). For material you derived competently and did not absorb:
1. **Prose-only pass (45 min)**: read skipping all algebra: introductions, transitions, summaries, footnotes.
2. **The three questions (60 to 90 min, written, no equations):** what question does this chapter answer and why did it arise? What breaks without it? What choice was made and what was the alternative?
3. **Counterfactual interrogation (30 min)**, listed per module.
4. **Targeted derivation only if triggered** (when step 2 or 3 exposes something you can state in words but not reconstruct as an argument).
5. **Explain-it (20 min)**: one paragraph, no equations, for a competent physicist who does not know QFT.
6. **Problems**, [T] and [C].

**The two problem streams.** **[T] Technique**: computational, checked against the solutions booklet or the expected results in this guide. **[C] Concept**: answered in prose, half a page to a page; no answer key: the check is whether your answer survives contact with a second source.

**Triage rule.** In Protocol A weeks, if time runs short **drop the [C] and keep the [T]** (you are building machinery). In Protocol B weeks, invert it: **drop the [T], keep the [C]** (technique was already demonstrated).

## 5. Second sources

Per Part, read one alternate treatment *before* the gate: *when someone else says this, do I recognise it?*
- **Lancaster and Blundell, *QFT for the Gifted Amateur***: best conceptual companion (buy this one).
- **Schwartz, *QFT and the Standard Model***: most forthcoming on motivation; use for Part Three especially.
- **David Tong's Cambridge QFT notes** (free): concise, clean, a completely different presentation.
- **Zee, *QFT in a Nutshell***: a good third voice, a poor second.
- **For Module M:** Boas, *Mathematical Methods*, Ch. 14 (complex analysis) is the friendliest; Arfken and Weber for reference; Byron and Fuller for the physicist's framing; **Klauber's own free *Dirac delta function forms* PDF** (it matches his conventions exactly). If you ran the electrodynamics guide, its Modules 02 and 11 are a rehearsal of Module M.

## 6. Operating rules

Budgeted by chapters, not hours; nominally 5 to 7 hours a week. **This is the absorber track:** when a week goes badly this pauses and your primary track does not thin. **Block, do not interleave.** **One adjustment for Module M:** Weeks 4 to 6 are the least fragmentable material in the plan (contour integration does not survive being done twenty minutes at a time); if your primary track is in a heavy stretch, shift Module M by a week or two rather than doing it badly. Keep `notes/error_log.md` and a one-line log per chapter with the column that matters: *what you could not answer*.

## 7. Deliverables

- **The log**: one line per chapter, with the column that matters: what you could not answer.
- **The Module M pages**: the three contour prescriptions, the invariant measure derivation, the KG Green function. You will use these for years.
- **The explain-it paragraphs**, one per chapter, no equations.
- **The [C] answers**: roughly 25 pages of prose by Week 29.
- **Three compression pages**: free fields (Module 12), interacting fields (Module 16), Ch. 1 to 13 (Module 19).
- **The renormalization argument** (Module 19): one page, no equations.

## 8. Open questions (from the plan, still open)

1. Is Module M three weeks or more? Sized assuming complex analysis needs a serious refresh but not a rebuild; if residues are genuinely cold, four weeks is more honest and Part Two absorbs the difference.
2. Confirm where Ch. 13 falls relative to the Part Three/Four boundary.
3. Is five weeks right for Ch. 3? If it runs faster once Module M is behind you, spend the spare weeks on Ch. 4, not on getting ahead.
4. Does the diagnosis still match? "Machinery taken on faith upstream, correct derivations on hollow symbols downstream": is that what it felt like?
