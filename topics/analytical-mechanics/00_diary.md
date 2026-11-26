# Study Diary

## 12-11-2026
* Block A: exercises 13 and 14 ([01_block_a_check_exercises.md](topics/analytical-mechanics/01_block_a_check_exercises.md))

## 13-11-2026
* Block B: Taylor series and exact differentials ([01_prerequisites_and_toolkit.md](topics/analytical-mechanics/01_prerequisites_and_toolkit.md#block-b-taylor-series-and-exact-differentials))

## 15-11-2026
* Block B: Taylor series in several variables (Boas formula). Got everything wrong at first because of notation confusion.

## 16-11-2026
* Block B: restarted the Maclaurin series of cos x sinh y from scratch. Key points: the power belongs to the operator, not to the first derivatives; evaluate at (0,0) only at the end; use h, k for the displacement. Expanded with the binomial theorem; n = 0 term done. Next: n = 1 to 3.

* ## 17-11-2026
* Block B: finished the Maclaurin series of cos x sinh y with the operator formula through n = 3 and matched it against the product of the one-variable series. Parity: only odd total degree survives (cos is even, sinh is odd).
* Boas two-variable Maclaurin series, cos(x+y): worked through n = 3. Missing cross term -hk at n = 2, fixed using the check against cos(h+k).
* Block B exercise 1 (e^x cos y, second order): all terms correct, then dropped the linear term h when assembling the final result. Fixed with the check against the product of the e^x and cos y series.
* Lesson: assemble the final series from a list of all terms, including the n = 1 ones, and run the product-series check before moving on.
* Next: Block B exercises 2 and 3 (ln(1+x+y), and the potential V with a minimum at (1,0)).

## 26-11-2026
* Block B exercise 2: Taylor series of ln(1+x+y) to second order, checked against the one-variable series of ln(1+s) with s = x + y.
* Block B exercise 3: potential V with a stationary point at (1,0).
  * (a) the gradient vanishes at (1,0).
  * (b) expansion to second order about (1,0): V ≈ -1/4 + (x-1)^2 + (3/2) y^2, in displacements h = x-1 and k = y.
* Lesson: this is not a Maclaurin series. The expansion point is (1,0), so h = x-1 and k = y, and the derivatives are evaluated at (1,0). In a Maclaurin series h = x and k = y, which is why the two are easy to mix up.
* Concept: a stationary point has zero gradient, so the first-order terms vanish. The second-derivative matrix then decides whether it is a minimum, maximum or saddle (Module 06 uses this for small oscillations).
* Next: finish exercise 3 with the matrix of second derivatives and its eigenvalues. Then Block B exercises 4 to 6 (exact differentials).
