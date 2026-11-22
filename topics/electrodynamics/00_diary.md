# Study diary

## Earlier session: exercises 1 and 2

**Done**
- Exercise 1 (delta of a function): both roots handled, including δ(cos x) at π/2 and 3π/2.
- Exercise 2 (spherical delta): the constant 1/(r'² sin θ') fixed by requiring the integral to equal 1.

**Doubts cleared**
- Using cos θ as a variable is only a change of coordinate: d(cos θ) absorbs the sin θ, so the measure is flat in (r, cos θ, φ).
- The stray commas in `d³x = r² dr, d cos θ, dφ` come from the LaTeX thin spaces `\,` rendering on GitHub, not from the formula. Possible fix: `\thinspace` (not confirmed on GitHub).

**Note**
- This one took a lot of effort. It helps to let a hard exercise sit for a couple of days.

## Earlier session: study guide

**Done**
- Refactored the electrodynamics guide. Modules 02 to 22 are pinned to Griffiths 5th ed., Jackson 3rd ed., Purcell and Morin 3rd ed. and Riley 3rd ed., each with sections, pages and a problem set.
- Module 02 redone with an itemized layout, which I like.

**Decisions**
- Apply the itemized layout to the other modules.
- Make the modules more complete (full exercise statements), but not verbose.
- No timed or no-notes blank-page targets: gates test understanding, and a cheat sheet is fine.

**To do**
- Refactor the remaining modules.
- Set up the Markdown-to-PDF script (pandoc + XeLaTeX) in the gist.


## 2026-11-19 (Thu): EM Module 02, exercise 3 done

**Done**
- Finished exercise 3: ∇²(1/r) = −4π δ³(r).
  - Set F = ∇(1/r) = −r̂/r², so ∇·F = ∇²(1/r).
  - Flux through a sphere is −4π, and the radius cancels (r² from the surface element against 1/r² in the field).
  - ∇·F = 0 away from the origin, so the whole −4π must sit at the origin.
  - The integral of −4π δ³ over any region containing the origin is also −4π. The integrals agree for every region, so the integrands are equal.

**Insight**
- The delta is the conclusion about the integrands, not an equation between integrals. Comparing ∫ ∇·F dV with ∫ (−4π δ³) dV for every V is what makes the step work.

**To tidy on the page**
- Write δ³(r), not δ(x).
- Add the arbitrary-radius line and the case where V does not contain the origin (both integrals are 0).

**Next**
- Exercise 4 (point and moving charges, continuity equation), then 5, 9 and 10.
- Alternate with analytical mechanics.


## 2026-11-22 (Sun): EM Module 02, Session 2 reading and Jackson 1.3(a)

**Done**
- Session 2, part A: Jackson §1.2 (p. 24) read and re-derived.
- Jackson Problem 1.3(a): spherical shell of radius R and total charge Q, ρ(r) = Q δ(r − R) / (4π R²). The check is that integrating over all space gives Q.

**Decisions**
- The EM guide is now in the new layout: the study file says what to read and where, and the exercises live in `exercises/`. Module 02 is the test module.
- Considering merging the book problems and the module exercises into one list per session. I'll try it and decide.

**Still open (Session 2, part B)**
- Exercise 3: the two additions to my page (δ³(r) notation, and the arbitrary-radius line plus the case where V does not contain the origin).
- Exercise 4: point and moving charges, continuity equation.
- Jackson 1.3 (b) to (d). Should: Griffiths 1.48 and 1.64. Could: Griffiths 1.49 and Jackson 1.2.

**Note**
- The reading and the exercises left me energized. Stopping at midnight with energy left is a good way to end.

**Next**
- Finish Session 2 part B, then Session 3 (Fourier and index notation).
- Once the Module 02 layout is confirmed, refactor Modules 03 to 22.
