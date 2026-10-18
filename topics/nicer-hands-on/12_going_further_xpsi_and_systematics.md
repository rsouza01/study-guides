# Module 12 (Level 8): going further: X-PSI, hot-spot systematics, multi-messenger data

**Resources:** X-PSI (`github.com/xpsi-group/xpsi`; Riley et al. 2023, JOSS 8, 4977) and its tutorials; Vinciguerra et al. 2024 (ApJ 961, 62); Kini et al. 2026 (arXiv:2602.23743) and its Zenodo notebooks; Hoogkamer et al. 2025 (PhRvD 112, 023008: sampler cross-checks); Chatziioannou et al. 2025 (Rev. Mod. Phys. 97, 045007) for the EOS-inference side.
**Time:** open-ended. Everything here is optional and **untested by the guide's author** (X-PSI needs MultiNest, GSL and a compiler; nothing was installed in the sandbox).

## Why this matters

Modules 08 to 11 gave you the logic of the chain. This module is where you meet the real tools and, more importantly, the real *uncertainties*: the hot-spot model, the sampler settings, the atmosphere, the background, and which sources to combine.

## Diagnostic (15 minutes)

1. Why did the J0030 PDT-U radius move by 1.8 km between 2024 and 2026 with only 50% more counts?
2. What is the difference between statistical and modeling uncertainty in a PPM result?
3. Why is the total cost of the headline J0030 run so large?

## Detailed topics (checklist)

- **X-PSI in one page:** it ray-traces an oblate star with Schwarzschild exterior (hot spots of ST/PST/PDT type), applies atmosphere tables (NSX fully-ionised hydrogen for J0030), interstellar absorption (tbnew, $N_{\rm H}$), instrument responses (ARF/RMF) and calibration scale factors, and compares phase-channel counts with a Poisson likelihood; inference with MultiNest or UltraNest (nested sampling, also giving the evidence for model comparison). For J0030 the 2026 priors: $M\sim U(1,3)$, $R_{\rm eq}\sim U(3r_g,16\ {\rm km})$, $D\sim N(0.325,0.009^2)$ kpc, $\cos i\sim U(0,1)$, hot-spot temperatures $\log_{10}T\sim U(5.1,6.8)$.
- **Model dependence (the J0030 story):** ST+PDT gave 11.71 km and PDT-U 14.44 km in 2024 (PDT-U preferred by evidence but in mild tension with J0437, J0614 and GW170817); with 50% more data and **more conservative sampler settings (10,000 live points, efficiency 0.3)** the 2026 PDT-U result moved to 12.68 km and the likelihood surface proved bimodal (a high-mass, large-radius mode and a lower-mass mode coinciding with ST+PDT). Lesson: the sampler configuration is part of the measurement.
- **Cost:** about 4.8 million core-hours for the PDT-U headline run and about 163 million likelihood evaluations; hence no one repeats it on a laptop.
- **Cheap, safe ways in:** (a) the X-PSI tutorials (synthetic data, small runs); (b) re-plotting from released posteriors and notebooks (the J0030 Zenodo package ships the notebooks that make the paper's figures); (c) injection-recovery with the toy model of Module 08.
- **EOS side systematics:** which hot-spot model for each source; whether to combine J0030's two solutions (see `Combining the Mass-Radius Posteriors of J0030+0451 Allowing for Unknown Model Systematics`, Zenodo 10.5281/zenodo.19222905, for a principled treatment); EOS parametrisation prior (piecewise polytropes vs speed-of-sound vs Gaussian processes); chiral-EFT low-density constraints; adding GW170817 tidal deformability, other pulsar masses ($M_{\rm max}$), and radio and nuclear constraints.

## Tasks

1. Read Kini et al. 2026 sections 3 and 4.1 and write a one-page summary of why PDT-U changed.
2. In `ex11`, run the J0030 source with each of the two hot-spot models in turn (swap the file), then with both (as two separate, equally weighted sources, and with weights 0.5 each) and compare $R_{1.4}$: how much does the *choice* matter versus the statistical width?
3. (Optional) Install X-PSI in a clean environment and run its injection-recovery tutorial; record the run time and compare the recovered $(M,R)$ with the truth.

## Exercises (with expected results)

1. **Sensitivity to one source:** drop each real source in turn from the EOS inference (Module 10) and tabulate the shift in $R_{1.4}$ and $M_{\rm max}$: which source drives the result? (Expect the massive pulsar J0740 to control $M_{\rm max}$ and the $\sim1.4\,M_\odot$ sources to control $R_{1.4}$.)
2. **Tempering:** give a suspect source weight 0.5 in `infer.Source(weight=0.5)` and see how the posterior widens; interpret the weight as a crude systematic inflation.
3. **Prior sensitivity:** repeat an injection-recovery with a different EOS parametrisation (e.g. widen the $\Gamma$ priors) and see whether $R_{1.4}$ changes by more than its width.
4. **Evidence thinking:** why does nested sampling give a Bayes factor between hot-spot models while MCMC does not (directly)? What is the danger of choosing the model with the highest evidence from X-ray data alone?
5. **Bookkeeping of cost:** for 163 million likelihood evaluations in 4.8 million core-hours, how long is one evaluation? (About 0.1 core-second.) Compare with 20 ms per EOS evaluation in Module 10.

## Pitfalls

- Treating a published contour as a Gaussian.
- Combining two hot-spot models of one pulsar as if they were two independent stars.
- Quoting an EOS-derived radius without stating which sources and which models went in.

## Gate questions

1. Which modeling choices in PPM matter most for the radius?
2. What would convince you that a sampler had not converged?
3. How would you combine a PPM measurement with a gravitational-wave tidal-deformability measurement?

## One-page cheat sheet contents

X-PSI components; the J0030 2024-to-2026 timeline; cost numbers; list of systematics you must state with any inferred radius.
