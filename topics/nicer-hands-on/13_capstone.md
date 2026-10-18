# Module 13: capstone: an end-to-end NICER-to-interior notebook and a two-page note

**Time:** 2 to 4 sessions.

## Goal

One reproducible notebook (`capstone.ipynb` or a script) that goes from NICER-derived inputs to structure, plus a two-page note that states what you did, what you found, and what you would not trust.

## Required content

1. **Data literacy (Levels 1 to 3):** at least one *real* NICER event file inspected (light curve, PI spectrum) and one pulse profile or period search (Crab), with commands, versions and screening cuts logged. If you could not get HEASoft working, do the same on the demo files and say so.
2. **Published inputs (Level 0):** at least three NICER $(M,R)$ posteriors loaded from Zenodo, sanity-checked, with source, model and release stated.
3. **Verified physics (Level 5):** the unit tests pass; your SLy numbers match the guide ($M_{\rm max}=2.05$, $R_{1.4}=11.71$ km, $\Lambda_{1.4}=294$); cross-check with your own `tov-solver.py` to better than 0.5%.
4. **Injection-recovery (Level 6):** an injection test that recovers a known EOS within about $1\sigma$ on $R_{1.4}$ before the real run.
5. **Real EOS inference (Level 6):** the posterior on $R_{1.4}$, $M_{\rm max}$, $P(2n_0)$ and (if you add it) $\Lambda_{1.4}$; convergence diagnostics (autocorrelation time, trace plots, split chains).
6. **Structure (Level 7):** profiles, central density, crust thickness, $I$, $\Lambda$ for $1.4$ and $2.0\,M_\odot$ stars with credible bands; a paragraph on which of these NICER actually constrains and which come from the EOS parametrisation.
7. **Systematics:** at least two controlled variations (drop-one-source; the two J0030 hot-spot models; a different EOS prior) and their effect.

## Two-page note (structure)

Question; data and models (with citations and Zenodo DOIs); method (likelihood, prior, sampler, checks); results (table + 3 figures); systematics; what you would do next; reproducibility statement (commit hash, environment file, runtime).

## Self-assessment

| Item | Pass criterion |
| --- | --- |
| Reproducibility | A colleague can rerun everything from `README` in under an hour of compute (excluding downloads) |
| Honesty | Every number in the note is traceable to a file and a command |
| Judgement | You can explain why your $R_{1.4}$ error bar is not just the average of the input error bars |

## Pitfalls

- Reporting a radius without saying which hot-spot model and which datasets were used.
- Over-reading structure outputs the data do not constrain (e.g. crust thickness is mostly set by the low-density EOS you fixed).
- Running a long inference once and trusting it.
