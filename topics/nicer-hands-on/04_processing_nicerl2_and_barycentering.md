# Module 04 (Level 1.5): processing, screening and barycentring

**Resources:** HEASARC threads `nicerl2`, `nicer-setup`, `geomag`, `light-leak-analysis`; the heasoftpy NICER example; NICERsoft `psrpipe`; Kini et al. 2026, section 2.1 (a published screening recipe).
**Time:** 1 to 2 sessions. **HEASoft commands below are quoted from the documentation and not run by the guide's author**: check `<task> help` for your installed version before relying on parameter names.

## Why this matters

Raw archive data are not science-ready. `nicerl2` applies the team's calibration and screening; for pulsars you additionally filter noisy detectors and background-flare intervals and barycentre the photon times. The choices made here are *analysis choices that change results*, and the PPM papers document them in detail.

## Diagnostic (15 minutes)

1. What does screening remove, and why can it remove "too much" data?
2. What is the barycentric correction and why is it $\sim500$ s in amplitude?
3. What is the difference between the cleaned event file and the unfiltered one?

## Detailed topics (checklist)

- **`nicerl2`:** `nicerl2 indir=<obsid> clobber=yes` produces the cleaned event file (conventionally `ni<obsid>_0mpu7_cl.evt`) and a filtered housekeeping file; geomagnetic quantities used for background screening are obtained with `nigeodown` and passed via the `geomag_path` parameters (the heasoftpy tutorial shows this); newer releases add the `NICERV6` filter columns and a `nicerl2-screen` task for re-screening. Always use *current* HEASoft + CALDB, even for archive data.
- **Barycentring:** `barycorr` converts event times to the solar-system barycentre using the orbit file from `auxil/` and the source position, e.g. `barycorr infile=<cl.evt> outfile=<bary.evt> orbfiles=<auxil/ni<obsid>.orb> ra=<deg> dec=<deg> refframe=ICRS ephem=JPLEPH.430` (verify parameters with `barycorr help`). After this the header carries `TIMEREF=SOLARSYSTEM`; `archive.read_events` prints it.
- **Published recipe (J0030, Kini et al. 2026), for reference:** `nicerl2` (HEASoft 6.33, calibration `xti20240206`); then `psrpipe` (NICERsoft) with: individually excluding detectors with count rates more than $3\sigma$ above the median of all detectors (instead of a fixed "hot detector" list); requiring the median undershoot rate among detectors below 200 counts/s (to limit optical loading below about 0.35 keV); excluding intervals where the 2 to 10 keV rate exceeds 1.5 counts/s (a background proxy, as the pulsar contributes negligibly there); `nicerl3-spect` for the ARF and RMF (the ARF scaled by the mean number of detectors); phase-folding with PINT's `photonphase` and a timing solution; PI channels [30,300) (0.3 to 3.0 keV). Data after the May 2023 light leak were excluded (2.4% of exposure).
- **Spectra and light curves:** `nicerl3-spect` and `nicerl3-lc` produce science products with background models (the heasoftpy tutorial uses `scorpeon`); check their help for your version.

## Tasks

1. Run `nicerl2` on your downloaded Crab sequence. Open the output `.evt` with `archive.read_events`; compare event counts and exposure with the unscreened file.
2. Barycentre with `barycorr`; confirm `TIMEREF`; compute the shift of the first event time (should be within a few hundred seconds).
3. Plot the 2 to 10 keV rate versus time; mark intervals above 1.5 counts/s; how much exposure would that screening remove?
4. (Optional) Re-run with different `nicerl2` screening parameters and quantify the effect on exposure.

## Exercises (with expected results)

1. **Screening bookkeeping:** exposure before screening, after `nicerl2`, after your extra cuts: table and fractions. Expect `nicerl2` to keep 50 to 90% for a typical segment (varies widely); the J0030 programme kept 2,974 of 4,029 ks (74%).
2. **Barycentric amplitude:** the difference barycentred minus raw time should oscillate with the ISS orbit (about 92 minutes, $\pm$ about 20 ms) and with the Earth's orbit (a $\sim\pm500$ s annual term). Plot it versus time over a day.
3. **Position sensitivity (do the arithmetic, then test it):** a position error $\Delta\theta$ changes the barycentric delay by up to $\Delta\theta\times500$ s, but only its *variation* during your data span matters for folding. For $\Delta\theta=1'$ ($2.9\times10^{-4}$ rad): over one 2 ks segment the variation is $\lesssim10^{-5}$ s (negligible even for a 33 ms pulsar); over a day about $2.5$ ms; over a year about $0.15$ s. For a 4.87 ms millisecond pulsar such as J0030+0451 a multi-year fold therefore needs a position good to $\ll1''$ (and a timing solution that fits it). Verify numerically by barycentring the same Crab file with positions displaced by $1'$ and $1^\circ$ and comparing folded profiles of (a) one segment, (b) a month of segments if you have them.
4. **PI cut:** reproduce the PI band choice: count events in PI 30 to 300 versus the full range; compare the fraction.
5. **Reproducibility:** write `process.sh` that takes an ObsID and produces `bary.evt`, logs versions, and fails loudly if a step fails.

## Pitfalls

- Using stale CALDB; mixing products processed with different versions.
- Applying `barycorr` twice.
- Too-aggressive screening that removes the pulsar's scientific exposure, or too-lax screening that leaves flares.

## Gate questions

1. Which screening choices change the background and which change the source counts?
2. Why does a 1 arcmin position error not matter for folding one 2 ks segment but matter enormously for a multi-year millisecond-pulsar fold?
3. Why do PPM analyses cut at 0.3 keV and 3.0 keV?

## One-page cheat sheet contents

The command sequence (`nicerl2`, `barycorr`, `nicerl3-spect/-lc`); the screening cuts above; time-system checklist.
