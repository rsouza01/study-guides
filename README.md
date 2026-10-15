# Physics Self-Study Guides

A set of detailed, multi-file study guides for self-directed study of the physics behind **stellar structure, compact objects, quantum field theory and QCD**, with the classical-mechanics, electrodynamics, thermodynamics and quantum-mechanics foundations they rest on.

Each guide is a folder of Markdown files: an overview, one file per module, and an appendix. They are written to be used as **references and working plans**, not as textbooks: they tell you what to read in standard books, what to derive from scratch, which exercises to do (with expected results), and how to check that you actually learned it.

> **Status:** personal study project. The guides were drafted with the help of an AI assistant (Claude) and then edited. Read the "Accuracy and caveats" section before relying on any number or section reference.

---

## The guides

| Folder                                           | Topic                                                                                                                                                                                                                                                        | Files | Main books                                                  | Approx. effort                                                          |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----- | ----------------------------------------------------------- | ----------------------------------------------------------------------- |
| [`analytical-mechanics/`](analytical-mechanics/) | Lagrangian and Hamiltonian mechanics as the bridge from classical to quantum mechanics: Poisson brackets, generators, Hamilton-Jacobi theory, action-angle variables, fields and Noether's theorem                                                           | 23    | Goldstein (3rd ed.), Landau-Lifshitz, Dirac, Sakurai        | ~46 weeks (fast path ~33) at two 2-3 h sessions per week                |
| [`electrodynamics/`](electrodynamics/)           | Classical electrodynamics as field theory: Green functions, Lorentz covariance, the action principle, radiation (including synchrotron). Includes a calculus and problem-solving ramp for readers who need it                                                | 25    | Stewart, Griffiths, Purcell, Jackson (3rd ed.)              | ~55 weeks (fast ~38, QFT-ready core ~28) at two 2-3 h sessions per week |
| [`thermo-statmech/`](thermo-statmech/)           | Thermodynamics and statistical mechanics for stellar interiors and equations of state: Maxwell relations, adiabatic exponents, Saha equation, degenerate Fermi gases, plasmas, transport, stability of self-gravitating matter                               | 18    | Schroeder, Callen, Pathria, Mandl, Blundell, Swendsen       | ~35 weeks (fast ~18) at ~8 h/week                                       |
| [`qm-for-qcd/`](qm-for-qcd/)                     | The quantum mechanics that QCD actually needs: formalism, angular momentum and isospin, identical particles, approximation methods, scattering, relativistic QM, bridge to QFT. Pinned to Zettili's 3rd edition (chapters, sections, pages, problem numbers) | 15    | Zettili (3rd ed.), with Sakurai, Shankar, Halzen-Martin     | ~30 weeks (fast ~16)                                                    |
| [`galactic-dynamics/`](galactic-dynamics/)       | Galactic dynamics with a focus on barred spirals, globular clusters and ellipticals                                                                                                                                                                          | 15    | Binney & Tremaine, Sparke                                   | ~11-12 months at 5-6 h/week                                             |
| [`stellar-physics/`](stellar-physics/)           | Stellar physics from formation to death, ending in a MESA-like 1D evolution code (capstone)                                                                                                                                                                  | 22    | Kippenhahn et al. and ~25 further references                | ~14-16 months                                                           |
| [`compact-objects/`](compact-objects/)           | White dwarfs, neutron stars, equations of state and their observables, ending in an EOS-to-observables toolkit with Bayesian inference (capstone)                                                                                                            | 22    | Shapiro & Teukolsky, Glendenning, Haensel et al. and others | ~15 months                                                              |

Total: **140 files, about 175,000 words**.

---

## Suggested reading order

The guides are largely independent, but they share prerequisites:

```
Stewart-level calculus
        │
        ├──► electrodynamics ──────────────┐
        │                                  ▼
analytical-mechanics ──► qm-for-qcd ──► (QFT / QCD)
        │
thermo-statmech ──► stellar-physics ──► compact-objects
                          │
                          └──► galactic-dynamics (independent, uses classical mechanics)
```

- `analytical-mechanics` and `electrodynamics` are designed to **run in parallel**: the mechanics modules come before the corresponding electrodynamics ones (the overview of `electrodynamics/` has the week-by-week alignment).
- `qm-for-qcd` is the quantum-mechanics counterpart; its Module 11 and the mechanics guide's bridge modules refer to each other.
- `thermo-statmech` feeds `stellar-physics` (equation of state, degenerate matter) and then `compact-objects`.

---

## How each guide is organized

Start with `00_overview.md` in each folder: it explains the goal, the module list, the dependency map and the schedule. Every module file has the same skeleton:

1. **Why it matters** for the guide's goal.
2. **Skip-test** (about 40 minutes, no notes): if you pass it, skip the module.
3. **Prerequisites** and a **detailed topic checklist** (with Must / Should / Could tiers where the guide uses them).
4. **Reading plan** (which sections of which books, split into sessions).
5. **Derivations to do from scratch** (book closed).
6. **Ten exercises with expected results**, plus pointers to book problems.
7. **Pitfalls**, **gate questions** and the contents of a one-page **cheat sheet** to write yourself.

Each guide ends with a **readiness test** (a checklist of derivations to reproduce cold, mini-projects and a mock exam) and an **appendix** (conventions, calendar, progress tracker).

### Rhythm

The guides assume a weekly rhythm of **reading in short blocks** and **derivations/exercises in longer, quiet blocks**, and each has a "fast path" for readers who already know part of the material. A week off costs nothing: the schedules are queues, not calendars.

---

## Accuracy and caveats

Please read this before using the guides.

- **Section and problem numbers are partly recalled.** `qm-for-qcd/` was pinned against a scan of Zettili's 3rd edition (page numbers are printed pages; PDF page = printed + 20; the scan was read by OCR, so a few problem numbers may be wrong). The other guides give section numbers from memory (for Goldstein, Jackson and others), and many exercises are _described_ by content rather than by number. Verify every reference against your own copy; each guide has a "Task 0" that builds a reading map from your edition.
- **Numerical check values** (constants, expected results, stellar and compact-object numbers) are from memory or recomputed by hand. Treat them as sanity checks, not as reference data; verify against a primary source.
- **Editions and units** matter: Jackson uses SI in Chapters 1-10 and Gaussian from Chapter 11; Zettili's 3rd edition uses SI; the electrodynamics appendix has a Gaussian-to-SI dictionary.
- **These are study plans, not substitutes for the books.** They contain no text from the books; they reference chapters and sections only.
- Corrections are welcome (see below).

---

## Suggested repository layout for your own work

```
.
├── README.md
├── analytical-mechanics/
├── compact-objects/
├── electrodynamics/
├── galactic-dynamics/
├── qm-for-qcd/
├── stellar-physics/
├── thermo-statmech/
└── notes/                  # your own work (create it; not part of the guides)
    ├── progress.md         # the tracking table from each guide's appendix
    ├── error_log.md        # the step you were stuck on, per exercise
    └── <module>/           # cheat sheets, derivations, written deliverables
```

Each guide's appendix has a progress-tracking template, and several guides ask for written deliverables (for example the three "bridge" documents in `analytical-mechanics/`). Keep those under `notes/` so the guides themselves stay clean and easy to update.

---

## Rendering

The files are plain Markdown with LaTeX math (`$...$` and `$$...$$`) and tables. GitHub renders the math and tables in the web view. If a formula does not render in your viewer, open the file in an editor with Markdown plus math preview (VS Code with a Markdown math extension, Obsidian, or similar), or convert with Pandoc:

```bash
pandoc 00_overview.md -o overview.pdf --pdf-engine=xelatex
```

---

## Contributing

Issues and pull requests are welcome, especially:

- corrections to section numbers, problem numbers and numerical values (please cite the edition and page);
- exercises that are ambiguous or whose expected result is wrong;
- pinned reading maps for other editions.

## License

_Choose one before publishing._ A common choice for study material is [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). The guides refer to commercially published books; this repository does not reproduce their text, figures or problems.

## Acknowledgements

Drafted with the help of Claude (Anthropic). All errors that remain are the maintainers'.
