# Module 10 (Level 6): from mass-radius posteriors to the equation of state

**Resources:** `nicerkit/infer.py`, `nicerkit/mr.py`; `examples/ex10_injection_recovery.py` and `ex11_real_eos_inference.py`; Raaijmakers et al. 2019 (EOS from NICER), Read et al. 2009 (parametrisation), Chatziioannou et al. 2025 (review); the Zenodo reproduction packages of the NICER papers contain EOS-inference notebooks.
**Time:** 3 to 5 sessions. The injection test runs offline in about 3 minutes (24 walkers, 450 steps); a real run needs hours.

## Why this matters

This is the step that turns a handful of $(M,R)$ blobs into a statement about dense matter, and it is where you will make the most mistakes without noticing: wrong prior volume, truncated grids, unconverged chains, a likelihood that silently double-counts. So the rule of the module is **injection-recovery first**.

## Diagnostic (20 minutes)

1. Write the likelihood of one pulsar's data given an EOS, as an integral over the unknown mass.
2. Why must the EOS sample be restricted to stable, causal configurations?
3. What do the NICER $(M,R)$ priors have to do with the formula?

## Detailed topics (checklist)

- **Model:** the 4-parameter Read parametrisation, flat priors in $\log p_1\in[33.8,35.0]$, $\Gamma_1\in[1.5,4.5]$, $\Gamma_2,\Gamma_3\in[0.5,6]$ (`infer.BOUNDS`), SLy-like crust fixed. A parametric EOS cannot represent phase transitions or wild structure: results are *conditional on the parametrisation* (Module 12).
- **Likelihood for source $j$:** $L_j({\rm EOS})=\int_{M_{\rm lo}}^{M_{\rm max}}dM\;p_j\big(M,R_{\rm EOS}(M)\big)\big/(M_{\rm max}-M_{\rm lo})$, with $p_j$ the KDE-smoothed NICER posterior. The NICER priors were flat in $(M,R)$ (with a radio-timing Gaussian on $M$ for binaries, which belongs in the posterior and must not be divided out), so $p_j\propto$ likelihood. **The division by the mass-range width is the uniform-mass-prior normalisation**; without it an EOS with a larger $M_{\rm max}$ is favoured simply because it integrates over more masses (exercise 4).
- **Constraints:** $M_{\rm max}\ge1.97\,M_\odot$ (hard cut, so the posterior does not rely on the KDE tail alone), sound speed $c_s<c$ (the sequence is cut where $c_s$ reaches $c$), stable branch only ($dM/dP_c>0$), $M(R)$ grid reaching the true maximum (`log_Pc_max=36.7`: a grid ending at $10^{36}$ biases $M_{\rm max}$ low).
- **Sampling:** `emcee` ensemble sampler, 24 to 32 walkers, thousands of steps, one EOS evaluation about 20 ms (numba): 1e5 evaluations take about 35 min on one core. Use `NPROC` and `multiprocessing.Pool`. Always check the autocorrelation time ($N_{\rm steps}\gtrsim50\,\tau$), trace plots, and compare two independent chains.
- **Derived quantities:** `infer.derived(theta)` gives $M_{\rm max}$, $R_{\rm at\,Mmax}$, $R_{1.4}$, $P(2n_0)$, $c_s^2$ at the centre of the heaviest star.

## Tasks

1. **Injection-recovery:** `python ex10_injection_recovery.py 450` (fake sources with $J0030$-, $J0437$- and $J0740$-like errors from SLy). Read the printed summary and compare with the truth.
2. Lengthen the chain (`... 3000`), check that the summary stabilises and that the answer is within about $1\sigma$ of the truth.
3. **Real data:** build `sources.json` (Module 02) and run `python ex11_real_eos_inference.py sources.json 3000` with several cores; save `eos_chain.npy`.
4. Make the standard plots: $R_{1.4}$ posterior, $M$-$R$ band (posterior of the whole curve, `fgivenx`-style), $P(\rho)$ band.

## Exercises (with expected results)

1. **Injection result (reference run, 24 walkers $\times$ 450 steps, SLy truth $R_{1.4}=11.71$ km, $M_{\rm max}=2.05\,M_\odot$):** with the normalised mass prior $R_{1.4}=11.11^{+0.59}_{-0.36}$ km and $M_{\rm max}=2.15^{+0.20}_{-0.10}\,M_\odot$: both truths within $1\sigma$, but the radius is on the low side and the chain is **short and not converged** (do exercise 2). Your numbers will differ with seed and length.
2. **Convergence:** compute the integrated autocorrelation time per parameter (`sampler.get_autocorr_time(tol=0)`); for a 450-step chain it will warn that the chain is too short. Extend until $N/\tau>50$, and plot the running median of $R_{1.4}$.
3. **Truncated grid trap:** rerun the likelihood with the old grid limit $\log_{10}P_c^{\max}=35.9$; measure how $M_{\rm max}$ and the posterior change.
4. **Prior-volume effect:** run once with `normalise_mass_prior=False`: reference result $R_{1.4}=11.17^{+0.60}_{-0.44}$ km but $M_{\rm max}=2.32^{+0.28}_{-0.14}\,M_\odot$ (truth 2.05): $M_{\rm max}$ is biased high by 0.2 to 0.3 $M_\odot$, the signature of an unnormalised mass integral.
5. **Source dropout:** repeat dropping each fake source in turn: which one controls $R_{1.4}$, which controls $M_{\rm max}$?
6. **Real-data sanity:** with J0030 (PDT-U 2026), J0614 and J0740 (Module 02), does the posterior $R_{1.4}$ sit between 10.3 and 12.7 km? Compare with a published EOS paper (e.g. the J0614 paper reports that adding J0614 shifts the allowed region to smaller radii by about 300 m): do you see a shift of that size when you add J0614?
7. **Coverage test (advanced):** repeat the injection with 20 different random truths and seeds; in what fraction does the 68% interval for $R_{1.4}$ contain the truth? This is the real test of calibration.
8. **Compare EOS summaries:** show $P(2n_0)$ from your posterior against a chiral-EFT range (a few MeV/fm$^3$ at $2n_0$; check Hebeler et al.): what does NICER add?

## Pitfalls

- Using weighted nested-sampling output as if equal-weight.
- KDE bandwidth too small (jagged likelihood) or too large (extra width): check by comparing the KDE contour with the paper's contour.
- Starting walkers at points with $-\infty$ log-probability (the example scripts now check this).
- Not repeating with a different $P_c$ grid or seed.

## Gate questions

1. Why must the likelihood integrate over mass rather than evaluate at the pulsar's mass?
2. What does the $1/(M_{\rm max}-M_{\rm lo})$ factor do physically?
3. How would you check that an EOS posterior is prior-dominated rather than data-dominated?

## One-page cheat sheet contents

The likelihood formula; constraints; sampler checks; the injection reference numbers and the two traps (grid reach, prior volume).
