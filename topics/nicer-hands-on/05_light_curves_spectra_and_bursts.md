# Module 05 (Level 2): light curves, spectra and thermonuclear bursts

**Resources:** `nicerkit.archive.read_events`, `nicerkit.bursts`; `examples/ex04_inspect_events.py`, `ex07_bursts.py`; HEASARC `nicerl3-lc` / `nicerl3-spect`; Galloway et al. (burst catalogue papers) and Lewin, van Paradijs & Taam (1993) for burst physics.
**Time:** 2 sessions.

## Why this matters

Before any pulse-profile modeling, you should be able to look at a NICER observation and say what it is: a light curve (counts vs time), a spectrum (counts vs PI), and for accreting neutron stars, bursts. **Type I X-ray bursts** are thermonuclear flashes on the surface of an accreting neutron star; the brightest reach the Eddington limit and expand the photosphere (photospheric radius expansion, PRE). Because the Eddington flux depends on mass and radius, and the cooling tail traces the blackbody emitting area, bursts have long been used to estimate neutron-star radii: a *replication of well-known physics* that uses exactly the data you now have.

## Diagnostic (15 minutes)

1. What distinguishes a type I burst light curve (shape, duration, spectrum) from a flare or a dropout?
2. Why does the Eddington luminosity depend on composition?
3. What is the apparent blackbody radius and how does it relate to $R$?

## Detailed topics (checklist)

- **Light curve:** bin event times (`bursts.bin_events`), restricted to GTIs; read rate in counts/s; typical variability: orbital modulation of the ISS visibility, slow source variability, background flares.
- **Spectrum:** histogram of `PI`; physical spectra need the *response* (ARF/RMF) and a background model: use `nicerl3-spect`, then fit in XSPEC/PyXspec or `sherpa`/`jaxspec`. Without a response you can still compare shapes between epochs.
- **Burst anatomy:** fast rise (about 1 s), exponential-like decay (a few s to tens of s, longer for helium-rich or PRE bursts), softening spectrum as the surface cools (temperature falls from about 2.5 to 1 keV while the apparent area stays roughly constant in the tail), recurrence from hours to days.
- **Radius from cooling tails (the classical idea):** during the decay, fit a blackbody to time-resolved spectra; the flux $F_\infty$ and temperature $T_\infty$ give an apparent radius $R_{\infty}=(1+z)R=\sqrt{F_\infty/(\sigma T_\infty^4/f_c^4)}\,D$ with colour correction $f_c\approx1.4$ to 1.5, strongly dependent on atmosphere models and distance: hence the large systematic uncertainties and why pulse-profile modeling superseded it for precision radii.
- **Detection algorithm** (`find_bursts`): running-median baseline, Poisson significance threshold plus a ratio threshold, merging of adjacent bins; `fit_decay` fits $a\,e^{-(t-t_p)/\tau}+b$.

## Tasks

1. `python ex04_inspect_events.py your.evt` (light curve + raw PI spectrum). Describe what you see.
2. `python ex07_bursts.py --demo` then on a real burster event file (download several segments of the same source). Count bursts, measure $e$-folding times and peak rates.
3. For the best burst, extract 1 s spectra across the burst with `nicerl3-spect` (time-resolved) and fit a blackbody: plot $T(t)$ and the apparent radius.

## Exercises (with expected results)

1. **Demo recovery:** on the synthetic light curve the finder returns 2 bursts at $t=604$ s and 1502 s with decay times $12.4\pm0.2$ s and $8.3\pm0.2$ s (injected 12 and 8): decay times are recovered within a few percent; peaks are lower than injected because of the 1 s binning of a 1 s rise.
2. **False positives:** on a pure Poisson light curve (rate 800 counts/s, 2000 s) run the finder 100 times with the defaults (`nsigma=6`, `min_ratio=2.5`): 0 detections. Now set `nsigma=3, min_ratio=1.0` (significance only): you get a few spurious detections per light curve (about 2000 bins times the one-sided 3-sigma tail of 0.00135, i.e. a few). Real light curves also have red noise and flares, which is why the ratio criterion (and inspecting every candidate) matters.
3. **Detection limits:** inject bursts of decreasing peak amplitude into a real persistent light curve (add Poisson events); find the minimum detectable peak versus persistent rate.
4. **Recurrence time:** for a source with several bursts, estimate the recurrence time distribution and the burst rate per day. Compare with the literature value for that source (check Galloway et al.).
5. **Spectral hardness:** compute a hardness ratio (PI 100 to 300 over 30 to 100) versus time through a burst; sketch what a cooling tail should do.
6. **Apparent radius estimate (optional, coding):** with a blackbody normalisation $K=(R_{\rm km}/D_{10})^2$ from your XSPEC fit, compute $R_\infty$ for an assumed distance and compare it with 10 to 14 km. State at least three systematic uncertainties.

## Pitfalls

- Binning with partial exposure bins at GTI edges (rate artefacts).
- Confusing dead-time-corrected and raw rates for very bright bursts.
- Colour-correction and distance systematics: do not quote a radius without them.

## Gate questions

1. What makes a burst different from a background flare in the data?
2. Why is the burst-radius method limited by systematics while PPM is limited by modeling assumptions?
3. How would you use a PRE burst to estimate the Eddington flux and what does it assume?

## One-page cheat sheet contents

Light-curve and PI-histogram recipes; the burst finder parameters; burst anatomy; the apparent-radius formula and its systematics.
