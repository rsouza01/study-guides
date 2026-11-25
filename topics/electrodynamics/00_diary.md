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


## 2026-11-23 (Mon): EM Module 02, Session 2, Jackson 1.3 (b) and (c)

**Done**
- Jackson 1.3(b): charge λ per unit length on a cylindrical surface of radius b. ρ = λ/(2πb) · δ(r − b).
- Jackson 1.3(c): flat disc of radius R, total charge Q. ρ = Q/(πR²) · δ(z) · Θ(R − r).

**Method that worked**
- Fix the shape of ρ first (a delta where the charge sits, a step where it fills a range), leave one unknown constant C, then integrate over the whole charge distribution (with the r from the volume element) and set the result to the known total. Solve for C.
- The cross-check is that C equals the surface or linear density, and the units come out as charge per volume.

**Doubts cleared**
- λ is charge per unit length, not per area. σ is per area, ρ per volume. A surface density becomes a volume density by multiplying by a delta, which supplies the missing 1/length.
- δ(r − b) has units of 1/length, so it is a unit check on any answer.
- A step function Θ is not like a delta. It does not pick a value, it only changes the limits of the integral, so I still have to do the integral. Θ′ = δ.

**Mistakes caught on my page**
- The 4πR² (a sphere) used for the disc's area. It should be πR².
- ∫₀ᴿ r dr = R²/2, not R.
- The step pointed outward: Θ(x − R) instead of Θ(R − r). Also x in place of r.
- Having both C and σ in ρ, instead of letting C be the only unknown.

**Still open (Session 2, part B)**
- Jackson 1.3(d): the same disc in spherical coordinates. Which angle the disc sits at, and the 1/r² and delta in cos θ.
- Exercise 3: the two additions (δ³(r) notation, arbitrary radius and V without the origin).
- Exercise 4: point and moving charges, continuity equation.
- Should: Griffiths 1.48 and 1.64. Could: Griffiths 1.49 and Jackson 1.2.

**Note**
- This was a long day (up for 18 hours, work and gym), and I stopped at half past midnight, after finishing (c). Leave (d) for a fresh head.

**Next**
- Finish Session 2 part B, then Session 3 (Fourier and index notation).
- Decide whether to merge the book problems and module exercises into one list per session.
- Once the Module 02 layout is confirmed, refactor Modules 03 to 22.


## 2026-11-24 (Tue): EM Module 02, Session 2, Jackson 1.3(d) and exercise 3

**Done**
- Jackson 1.3(d): the flat disc of radius R in spherical coordinates. ρ = Q/(πR²) · δ(θ − π/2)/r · Θ(R − r).
  - Same density as in (c): z = r cos θ, so δ(z) becomes δ(θ − π/2)/r.
  - Jackson 1.3 is now complete, (a) to (d).
- Exercise 3 (∇²(1/r) = −4π δ³(r)): steps 1 and 2 redone for the cleaned-up version of my page (the arbitrary-radius flux). Step 3 onward still to finish.

**Insights**
- The volume element depends on the coordinate system: r dr dφ dz in cylindrical, r² sin θ dr dθ dφ in spherical. I started (d) with the cylindrical one by mistake.
- A delta in an angle is not a delta in a length. A step dθ at radius r covers a distance r dθ, so the slab thickness grows with r. The delta needs a 1/r (the scale factor of θ) to give a uniform surface density. Machado vol. 1 shows the same thing with scale factors: 1/r for θ and 1/(r sin θ) for φ.
- Checking units and total charge catches most errors.

**Doubts**
- (d) is not fully clear yet. I understand the slab picture and the 1/r, but it still feels like I missed a lecture. Revisit later.
- Drill for next time: write the same disc density in cylindrical and in spherical coordinates and check by hand that they agree.

**Still open (Session 2, part B)**
- Exercise 3: steps 3 to 6 (the case where V does not contain the origin, δ³(r) notation, conclusion).
- Exercise 4: point and moving charges, continuity equation.
- Should: Griffiths 1.48 and 1.64. Could: Griffiths 1.49 and Jackson 1.2.

**Next**
- Back to analytical mechanics tomorrow.
- Next EM session: finish exercise 3, then exercise 4, then Session 3.
- Decide whether to merge the book problems and the module exercises into one list per session.
- Once the Module 02 layout is confirmed, refactor Modules 03 to 22.

## 2026-11-25 (Wed): EM Module 02, Session 2, exercise 3, steps 3 to 5

**Done**
- Exercise 3, step 3: ∇·F = 0 for r ≠ 0, with F = −r̂/r².
- Exercise 3, step 4: the flux of F through any closed surface is −4π if it encloses the origin, and 0 if it does not.
  - Origin inside: a small sphere S₁ around the origin; the region between S₁ and the outer surface S₂ has ∇·F = 0, so Φ(S₂) − Φ(S₁) = 0 and Φ(S₂) = −4π. It works for any closed S₂, not only a sphere.
  - Origin outside: F is smooth in V, so the divergence theorem applies directly and the flux is 0.
- Exercise 3, step 5: ∫_V (−4π δ³) dV = 0 (origin outside V) and −4π (origin inside), by the sifting property.

**Insights**
- My first result was ∇·F = 2/r³. That was only the radial derivative: r̂ is not a constant vector, so ∇·(f r̂) = f′ + f ∇·r̂, with ∇·r̂ = 2/r. The two terms cancel for f = −1/r².
- The route I chose: write F = −r⃗/r³ in Cartesian components (r² = r⃗·r⃗ = x² + y² + z², ∂_x r = x/r) and take the divergence there. No coordinate-dependent unit vectors.
- Choosing coordinates: use the symmetry for integrating (spherical for the flux), and Cartesian for differentiating vectors. Scalars switch freely; vectors carry their basis vectors.
- Derivation of the radial divergence from a thin shell of flux: ∇·F = (1/r²) d(r²F)/dr. I wanted to see it once. The full spherical ∇ gets derived in Modules 06 and 07.
- The −4π δ³ is deduced, not put in by hand: step 4 gives measured integrals, and δ is the object with exactly that property. Historically, Dirac introduced it as a notation (1920s), and Schwartz's distributions (1940s) made it rigorous.

**Fixes for my write-up**
- Write n̂ (the outward normal), not r̂, in the flux through a general surface S₂.
- Write δ³(r) and the arbitrary-radius line.

**Still open (Session 2, part B)**
- Exercise 3, step 6: conclude that ∇·(∇(1/r)) = −4π δ³(r), using that the integrals agree for every V.
- Exercise 4: point and moving charges, continuity equation.
- Should: Griffiths 1.48 and 1.64. Could: Griffiths 1.49 and Jackson 1.2.
- Revisit Jackson 1.3(d) (the disc in spherical coordinates) later.

**Next**
- Back to analytical mechanics tomorrow.
- Next EM session (or next week, after AM): finish step 6, then exercise 4.
