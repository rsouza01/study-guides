# Module 19: Part Three c, the programme assembled, and the Phase 1 gate (Week 29; Protocol B)

**Books:** Klauber Part Three (the closing material); Schwartz's renormalization chapters; Tong's lecture on renormalization and effective field theory.
**Time:** 1 week.

## Why this matters

The deliverable of the whole track: **one page, no equations, stating the renormalization argument end to end**: what diverges, what is absorbed, what remains, why the remainder is predictive, what renormalizability rules out. It is also the honest test of whether the first pass converted, and it closes Phase 1.

## Diagnostic (40 minutes, no notes)

1. Carry one complete loop calculation through: set up, regularize, renormalize, take the physical limit (vacuum polarization is the standard choice).
2. State the renormalizability criterion in terms of operator dimensions and give a non-renormalizable example.
3. State why the renormalized theory is predictive despite infinitely many arbitrary-looking subtractions.
4. State the relation between running couplings and the choice of subtraction scale.
5. Write the renormalization argument in five sentences.

## Prerequisites

Modules 17 and 18.

## Detailed topics (checklist)

- The programme: (1) regulate; (2) write the bare Lagrangian with bare parameters and field renormalizations; (3) fix the finite number of parameters (mass, charge) by physical measurements (renormalization conditions); (4) every other observable is then a *prediction*, finite as the regulator is removed.
- **Renormalizability:** operators of mass dimension $\le4$ (in four dimensions) have couplings of non-negative mass dimension and give finitely many divergent structures; operators of dimension $>4$ (e.g. the four-fermion Fermi interaction, dimension 6, coefficient $G_F\sim\frac{1}{(250\,{\rm GeV})^2}$) require infinitely many counterterms and signal new physics at the scale of their coefficient (effective field theory).
- The **modern view**: renormalizable theories are the long-distance effective theories whose couplings run; "subtracting infinity" is the statement that bare parameters are not observable and the physical (renormalized) parameters at a scale are the inputs.

## ▣ Phase 1 gate (Week 29, about 2 hours)

The three Part gates back to back (Part One, Module 12; Part Two, Module 16; this Part), plus the renormalization page cold, plus **compression: Ch. 1 to 13 on one page.** That last page is the honest test of whether the first pass converted. Write it *before* deciding when Phase 2 starts.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Prose pass; the three questions on the whole programme |
| A2 | The one-loop vacuum polarization end to end; exercises 1 to 3 |
| A3 | Renormalizability and effective field theory; exercises 4 to 6 |
| A4 | The renormalization page; the compression; exercises 7 to 10; the gate |

## Derive from scratch (this module's calculation is required)

One full loop integral, regularized and renormalized, start to finish (vacuum polarization is recommended: it uses everything from Modules 17 and 18).

## Exercises

1. **[T] Vacuum polarization end to end:** set up $i\Pi^{\mu\nu}(q)=-(-ie)^2\int\frac{d^4k}{(2\pi)^4}{\rm tr}\left[\gamma^\mu\frac{i}{k\!\!\!/-m}\gamma^\nu\frac{i}{k\!\!\!/+q\!\!\!/-m}\right]$; show transversality $\Pi^{\mu\nu}=(q^2g^{\mu\nu}-q^\mu q^\nu)\Pi(q^2)$ (dimensional regularization preserves the Ward identity); obtain $\Pi(q^2)$ of Module 18 and the on-shell subtraction.
2. **[T] Operator dimensions:** $[\phi]=1$, $[\psi]=\frac32$, $[A_\mu]=1$: $\phi^4$ (4), $\bar\psi\psi\phi$ (4), $\bar\psi\gamma^\mu\psi A_\mu$ (4) are renormalizable; $\phi^6$ (6) and $(\bar\psi\psi)^2$ (6) are not.
3. **[T] Fermi theory:** $G_F=1.166\times10^{-5}$ GeV$^{-2}$ corresponds to a scale $G_F^{-1/2}=293$ GeV (more precisely $v=246$ GeV): the non-renormalizable four-fermion interaction signals the $W$ at $\sim80$ GeV.
4. **[T] Counting free parameters:** QED has two parameters ($m$, $e$) at all orders; a non-renormalizable theory needs a new counterterm at each order.
5. **[T] Scheme dependence:** changing the subtraction scale $\mu\to\mu'$ changes the coupling by $\Delta\alpha=\frac{2\alpha^2}{3\pi}\ln\frac{\mu'}{\mu}$ and leaves observables unchanged.
6. **[T] Predictions:** list three quantities predicted by QED after fixing $m$ and $e$ (e.g. $a_e$ to order $\alpha$ is $\frac{\alpha}{2\pi}=1.161\times10^{-3}$; Module 20).
7. **[C] The renormalization argument:** one page, no equations: what diverges, what is absorbed, what remains, why the remainder is predictive, what renormalizability rules out. **The deliverable of the whole track.**
8. **[C] Compression, Ch. 1 to 13:** the whole of Phase 1 on one page, as an argument.
9. **[C] Is the theory fundamental?** State the effective-field-theory view of renormalizable and non-renormalizable theories and what it says about whether QED needs to hold at all scales.
10. **[C] Phase 2 decision:** from the three compression pages decide when to start Phase 2 and which gate items need rework first.

## Optional extension

Work out the renormalization-group improvement of $\alpha(Q^2)$ to two loops and compare with the one-loop running at $Q=M_Z$.

## Pitfalls

- Writing the renormalization page with equations (it is the point of the exercise to do without).
- Identifying the renormalization scale with a physical cutoff.
- Starting Phase 2 before the Phase 1 gate has been attempted.

## Gate questions

1. What is predictive about a renormalized theory?
2. What does renormalizability rule out, and what replaces it in the effective-field-theory view?
3. Why is the first-pass hollowness best detected in this module?

## One-page cheat sheet contents

The renormalization programme in five steps; renormalizability by dimension; the running coupling; scheme independence of observables.
