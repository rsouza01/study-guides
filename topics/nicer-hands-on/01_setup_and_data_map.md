# Module 01: Setup, and a map of the NICER data world

**Resources:** HEASARC NICER analysis threads (`heasarc.gsfc.nasa.gov/docs/nicer/analysis_threads/`), the HEASARC NICER archive page, the heasoftpy NICER tutorial, the NICERsoft repository (`github.com/paulray/NICERsoft`), PINT, X-PSI (`github.com/xpsi-group/xpsi`).
**Time:** 1 session (plus HEASoft installation time).

## Why this matters

Half of the friction in observational work is environment and file formats. Fix both once, test them on synthetic data, and the rest of the guide is analysis, not plumbing.

## Diagnostic (15 minutes)

1. What does the *level* of a data product (unfiltered, cleaned, products) mean, and why does HEASARC say to rerun `nicerl2` even on archive data?
2. What are PI channels, in keV?
3. What is the difference between a *light curve*, a *spectrum* and a *pulse profile*, in terms of which event column each uses?

## Detailed topics (checklist)

**The software stack [Must]**
- **Python side (everything in this guide except Level 1.5):** `conda env create -f code/env/environment.yml`. `astroquery>=0.4.10` talks to HEASARC through TAP; `numba` accelerates the TOV solver; `emcee` samples.
- **HEASoft (needed to *process* NICER data):** install HEASoft from HEASARC with the NICER calibration database (CALDB). Use the latest release: it contains the NICER software (NICERDAS) and, for data taken after the 2023 repair, newer screening. The 2026 J0030 reanalysis used HEASoft 6.33 with calibration file `xti20240206`; record *your* versions in your lab notebook.
- **heasoftpy** (optional): Python wrappers for HEASoft tasks (`hsp.HSPTask('nicerl2')`). The HEASARC tutorial uses it end to end.
- **NICERsoft** (`psrpipe`) and **PINT** (`photonphase`): the pulsar timing route used by the PPM papers (Module 07).
- **X-PSI**: relativistic pulse-profile modeling and inference (Module 12); needs MultiNest, GSL and a C compiler.

**What a NICER observation looks like [Must]**
- An observation (*ObsID*, 10 digits) is split into *segments* of at most one calendar day. Downloaded directory (typical): `<obsid>/xti/event_uf` (unfiltered), `xti/event_cl` (cleaned by the archive pipeline), `auxil/` (housekeeping `.mkf`, orbit `.orb`, attitude), `log/`. After your own `nicerl2` run you get a cleaned event file, conventionally `ni<obsid>_0mpu7_cl.evt`.
- **Event files** are FITS tables: one row per detected photon, with at least `TIME` (mission elapsed time, seconds since the epoch in the header's `MJDREFI`/`MJDREFF`) and `PI` (pulse-invariant energy channel, **10 eV per channel**: PI 30 to 300 is about 0.3 to 3.0 keV, the band used for pulse-profile modeling). A GTI extension lists the "good time intervals".
- **Instrument:** NICER's X-ray Timing Instrument is an array of 56 X-ray concentrators with silicon drift detectors, working from 0.2 to 12 keV, with a few tens of detectors typically active (the J0030 analyses mention 52); large effective area near 1.5 keV (about 1900 cm$^2$, from memory) and sub-microsecond timing. It sits on the ISS, so data come in short good intervals (typically minutes) per orbit, interleaved with other targets.
- **Pitfalls specific to NICER:** *background* is significant at low and high energies (optical light loading below about 0.35 keV, particle background, and, between May 2023 and the repair, a "light leak" that raised the background in day-time data); *detector flare*s ("hot" detectors); *time system*: raw times are at the ISS, so you must **barycentre** before any pulsar analysis.

**The public products that matter for NEUTRON-STAR RADII [Must]**
- The collaborations release **posterior samples** and often full reproduction packages on Zenodo (Module 02). For radius science you *use* these; for data literacy you *look at* the raw events (Levels 1 to 3).

## Tasks

1. Create the environment; `cd code && python -m pytest -q`. **Expected:** all tests pass in about 3 minutes (the EOS injection-recovery test is the slow one).
2. Run the offline demos: `cd examples && python ex09_tov_eos.py && python ex05_crab_period.py --demo`. **Expected:** SLy: $M_{\rm max}=2.05\,M_\odot$, $R_{1.4}=11.71$ km, $\Lambda_{1.4}=294$; Crab demo recovers the injected frequency to better than $1/T$.
3. Install HEASoft and CALDB; run `nicerl2 help` and `barycorr help`; paste the version lines into `notes/log.md`.
4. Create `notes/log.md` with the template: date, target, ObsID, commands, versions, outputs, surprises.

## Exercises (with expected results)

1. **Units:** an event with `PI = 142` has energy about 1.42 keV; the interval PI 30 to 300 covers 0.3 to 3.0 keV. Write a one-line function `pi_to_kev`.
2. **Time:** read `MJDREFI`, `MJDREFF` from your event file header and convert `TSTART` to a UTC date with `astropy.time.Time`. Check it lies inside the ObsID's calendar day.
3. **Reproduce the demo numbers** of Task 2 in your own environment and paste them in your log. Any difference in the 3rd digit means a package-version issue worth understanding.
4. **Data volume budgeting:** sketch, for a bright pulsar with 1 Ms of exposure and 10$^3$ counts per second at most, how many events you must handle (up to about $10^9$); decide what you can do in memory with numpy and what needs chunking (hint: `fold.z2m_scan` already chunks over frequencies, not over events).
5. **Read one HEASARC thread** (`nicerl2`) and list its three most important parameters for your first science case (screening thresholds, `threshfilter`, time-segment options).

## Pitfalls

- Skipping `nicerl2` on archive data (calibration and screening improve over time).
- Mixing barycentred and non-barycentred times.
- Trusting a "bright source" label without checking for a detector or background problem in the light curve.

## Gate questions

1. Why must the photon times be barycentred, and what changes if you forget?
2. What does PI measure and why is it not "energy" exactly?
3. Which three files from an observation do you need for a spectrum (events, response, background)?

## One-page cheat sheet contents

Directory tree of an ObsID; event columns (`TIME`, `PI`, GTI); PI to keV; the HEASoft commands you will use (Module 04); the list of Zenodo records you use (Module 02).
