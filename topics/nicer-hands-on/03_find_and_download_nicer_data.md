# Module 03 (Level 1): find and download NICER data

**Resources:** HEASARC `nicermastr` table; `astroquery.heasarc`; the HEASARC NICER archive page; `nicerkit.archive`; `examples/ex03_query_download.py`.
**Time:** 1 session. **Network functions here were not run against live servers by the guide's author**: they follow the documented interfaces. Fix errors by reading them.

## Why this matters

Every observational project starts with "what exists, how much, and is it public yet?". `nicermastr` has one row per observation sequence with position, time, exposure and processing information; the archive path of each sequence is derived from its start month.

## Diagnostic (10 minutes)

1. What is an ObsID and a segment? Why can one target have thousands of ObsIDs?
2. Why might a recent observation not be downloadable yet?
3. Given an ObsID and a start time, build its archive directory URL.

## Detailed topics (checklist)

- **Query by position.** `Heasarc.query_region(SkyCoord, catalog='nicermastr', radius=...)` returns an astropy table; the NICER field of view is about 3 arcmin in radius, so a 5 arcmin cone around a known target is a safe selection. Inspect `tab.colnames`: expect columns such as `obsid`, `time`, `exposure`, `name`, `ra`, `dec`, `public_date`; verify before relying on any name (`archive._col` finds the closest match).
- **Public or proprietary.** Guest-observer data have a proprietary period; HEASARC states that some GO data may be encrypted. If the `public_date` is in the future, the files will not open.
- **Download.** Two routes: `astroquery`'s `Heasarc.locate_data` + `download_data` (also supports cloud hosts), or the HEASARC-recommended recursive `wget` on the observation directory (what `archive.download_obs` runs). The directory URL pattern is `https://heasarc.gsfc.nasa.gov/FTP/nicer/data/obs/YYYY_MM/<obsid>/`.
- **Choosing observations.** For a first look choose a segment with a few ks of exposure on a bright source. For pulse profiles choose many segments (Module 07); for burst searches choose a source with long exposures (Module 05).

## Tasks

1. `python ex03_query_download.py crab` (targets known to `archive.TARGETS`: `crab`, `j0030+0451`, `j0437-4715`, `j0740+6620`, `j0614-3329`, `4u1820-30`, `aqlx-1`, `cygx-2`, `scox-1`; **coordinates are from memory, check with SIMBAD**). Read the table.
2. Record in `notes/log.md`: number of sequences, total exposure, first and last date for each target.
3. Pick **one Crab sequence** with 1 to 3 ks of exposure and download it: `python ex03_query_download.py crab <obsid>`. Look at the directory tree; list file sizes.
4. Repeat for **one segment of a bright burster** and **one of J0030+0451 or J0437-4715**.

## Exercises (with expected results)

1. **Archive census:** for each target compute total exposure (ks), number of sequences and date span. **Expected:** J0437-4715 and J0030+0451 each have of order Ms of exposure (the 2026 J0030 paper quotes 4,029 ks available before the light leak, 2,974 ks after screening), the Crab has many short sequences.
2. **URL check:** `archive.obs_url(4142010107, 59520.0)` should end with `/2021_11/4142010107/` (this is the Cyg X-3 example in the HEASARC heasoftpy tutorial). Does your own downloaded sequence agree with the pattern?
3. **Exposure histogram:** plot exposure per sequence for one target; explain the peak (ISS orbit visibility windows of minutes).
4. **Time coverage:** plot sequence start MJD versus index for J0030; find gaps and relate to the 2023 light-leak period (the 2026 J0030 analysis stops at 2023 January 13).
5. **Download hygiene:** write a script that downloads N sequences with retries and verifies that each contains `xti/event_cl`; log failures.

## Pitfalls

- Assuming column names; HEASARC fields can be renamed.
- Starting a multi-GB download without checking sizes first.
- Forgetting that HEASARC organises by *start month* (a sequence crossing a month boundary lives in the start month).

## Gate questions

1. What does `exposure` in `nicermastr` mean, and how does it differ from time on target after screening?
2. How would you choose observations for (a) a blind period search, (b) a phase-energy matrix, (c) a burst search?
3. How do you make a download reproducible?

## One-page cheat sheet contents

The query snippet; the URL pattern; the target table; your notes template.
