# Module 06 (Level 2): the Crab pulsar: blind period search and pulse profile

**Resources:** `nicerkit.fold`; `examples/ex05_crab_period.py`; Buccheri et al. 1983 ($Z^2_m$), de Jager et al. (H-test); the Jodrell Bank Crab pulsar monthly ephemerides (to check your frequency).
**Time:** 1 to 2 sessions.

## Why this matters

This is the cleanest *replicate-something-known* exercise: take barycentred photons from a source you know pulses, find the spin frequency blind, fold, and see the two-peaked profile that every textbook shows. Everything in pulse-profile modeling rests on this operation (fold photon times on the rotation phase), only done coherently for years and resolved in energy.

## Diagnostic (15 minutes)

1. What does $Z^2_m$ test, and what is its null distribution?
2. What frequency resolution can you get from a time span $T$, and why does a spin-down $\dot f$ matter when $\dot f\,T^2>1/T$?
3. Why is an FFT a good *first* stage but not a *final* answer?

## Detailed topics (checklist)

- **Target:** PSR B0531+21 in the Crab Nebula. Spin frequency about 29.5 to 29.7 Hz in the 2020s (scan 29 to 30 Hz rather than trusting this number) with $\dot f\approx-3.7\times10^{-10}$ Hz/s, so $\dot f\,T^2\ll1/T$ only for $T\lesssim10^4$ s: for a single segment you can ignore it, for days you cannot. Glitches and timing noise exist.
- **What NICER sees:** the pulsar *and* the whole nebula in the field of view; the nebula is unpulsed, so the pulsed *fraction* of the total counts is modest. The pulse profile has a main pulse and an interpulse roughly 0.4 cycles apart.
- **Statistics:** $Z^2_m=\frac2N\sum_{k=1}^m[(\sum\cos k\phi_i)^2+(\sum\sin k\phi_i)^2]$ is $\chi^2_{2m}$ under the null; the H-test picks $m$ automatically ($H=\max_m[Z^2_m-4m+4]$, false-alarm probability $\approx e^{-0.4H}$).
- **Algorithm:** (1) bin events at $\Delta t\approx2$ to 5 ms and FFT (`fft_power_search`); (2) take the highest peak in the plausible range; (3) refine with a fine $Z^2_m$ scan in a window of a few $1/T$ (`z2m_scan`); (4) fold (`fold`) and plot two cycles; (5) quote the frequency with an uncertainty (bootstrap it, exercise 4; for a sinusoidal pulse of fractional amplitude $A$ in $N$ photons the Cramér-Rao scaling is $\sigma_f\approx\sqrt6/(\pi A T\sqrt N)$).

## Tasks

1. Download and barycentre one or more Crab segments (Modules 03 and 04).
2. Run the blind search over 29 to 30 Hz. Report $f$, $Z^2_2$, $H$, FAP.
3. Fold; plot the profile (two cycles); identify the main pulse and interpulse; measure their separation in phase.
4. Repeat on a different day: how much did $f$ change? Compare with $\dot f\times\Delta t$.

## Exercises (with expected results)

1. **Demo run (offline):** `python ex05_crab_period.py --demo`: injected $f=29.60337$ Hz, $T=3000$ s, about 31,000 events; the search returns 29.603333 Hz ($|\Delta f|=3.7\times10^{-5}$ Hz, well inside the resolution $1/T=3.3\times10^{-4}$ Hz) with $Z^2_2\sim5\times10^3$.
2. **Null distribution:** simulate 1000 noise-only event lists and histogram $Z^2_2$; it should follow $\chi^2_4$ (mean 4). Compute the fraction above your measured peak: this is your false-alarm probability per trial; multiply by the number of independent trials ($\approx\Delta f\,T$) for the full-scan FAP.
3. **Trials factor:** your scan covered 1 Hz with resolution $1/T$: how many independent trials? A peak of $Z^2_2=25$ is how significant after trials?
4. **Frequency uncertainty:** bootstrap the events (resample with replacement 200 times), redo the refinement, and report the standard deviation of $f$; compare with the Cramér-Rao estimate $\sigma_f\approx\sqrt6/(\pi A T\sqrt N)$ for a sinusoid of fractional amplitude $A$ (check your own simulation: the two should agree within tens of percent).
5. **Spin-down:** split one long observation (or several days) and measure $f$ in each part; fit a line to get $\dot f$; compare with the literature value $\approx-3.7\times10^{-10}$ Hz/s.
6. **Pulsed fraction:** from the folded profile compute the amplitude pulsed fraction (`pulsed_fraction`); explain why the nebula lowers it, and how to measure it in a different PI band (is the pulsar harder than the nebula?).
7. **Energy dependence:** fold PI 30 to 100 and PI 100 to 300 separately and compare shapes (preview of Module 07).
8. **Wrong barycentring:** fold the non-barycentred file at the same frequency: how much does the peak broaden over 2 ks? (Hint: the ISS orbital delay changes by tens of ms over the orbit.)

## Pitfalls

- Folding with the wrong sign convention for $\dot f$.
- Quoting the FFT peak without refinement.
- Treating a harmonic as the fundamental (check $f/2$): the H-test with $m>1$ and the profile shape disambiguate.

## Gate questions

1. Why does coherent folding over years require more than a frequency and a spin-down?
2. What is the trials factor and where does it come from?
3. What does the pulsed fraction tell you about the emission geometry?

## One-page cheat sheet contents

The four-step search algorithm; $Z^2_m$ and the H-test formulas; resolution $1/T$; spin-down check.
