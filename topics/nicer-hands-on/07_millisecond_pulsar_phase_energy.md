# Module 07 (Level 3): a millisecond pulsar: coherent folding and the phase-energy matrix

**Resources:** PINT (`pint-pulsar`), NICERsoft `psrpipe`, `nicerkit.fold.phase_energy_matrix`; `examples/ex06_phase_energy.py`; Bogdanov et al. 2019 (ApJL 887, L25: NICER J0030 data and background), Kini et al. 2026 (Figure 1: phase-channel matrix and the new dataset).
**Time:** 2 to 4 sessions (the timing solution is the hard part).

## Why this matters

A pulse-profile model does not fit "a profile"; it fits **counts in a grid of (rotational phase, energy channel)**: 32 phase bins by PI channels 30 to 299, for J0030 in the papers. Making that matrix from raw events is the single most instructive step between "photons" and "$M$-$R$". It also exposes why the analysis is expensive (hundreds of channels times dozens of phase bins, joint with XMM) and where the background hides.

## Diagnostic (15 minutes)

1. How accurately must $f$ be known to fold 6 years of a 205 Hz pulsar without smearing? (Phase error $\delta f\,T$.)
2. What is a timing model (`.par` file) and what does `photonphase` do with it?
3. Why do the pulse profiles of the same star look different in different energy bands?

## Detailed topics (checklist)

- **Target:** PSR J0030+0451, an isolated 4.87 ms pulsar ($f\approx205.5$ Hz) at about 325 pc; the second-brightest in the PPM target list. Other targets: J0437-4715 (the brightest and nearest; binary), J0740+6620 (faint, massive, binary), J0614-3329.
- **Coherent phase assignment:** barycentred photon times are converted into rotational phase with a timing model: $\phi(t)=\phi_0+f(t-t_0)+\tfrac12\dot f(t-t_0)^2+\dots$ plus astrometry, binary terms if any. For multi-year NICER folds you need the **NICER team's or a pulsar-timing-array solution** (J0030 is in NANOGrav data releases; the NICER papers used a radio timing solution spanning the data). A simple $(f,\dot f)$ from a catalogue works only for short spans.
- **PINT:** `photonphase` (command line) or the Python API (`pint.models.get_model(par)`, `pint.event_toas` loaders for NICER events) assigns phases and can write them into the event file. **API details change; check the PINT documentation** for your installed version.
- **The matrix:** `fold.phase_energy_matrix(t, pi, f, fdot, nphase=32, pi_edges=np.arange(30,301,10))`. In the published figure, horizontal features near PI 35 and 55 are *Earth-atmosphere fluorescence lines* (background), not pulsar signal.
- **Background:** estimated from phases/energies where the pulsar is faint and from XMM-Newton spectra jointly; NICER's own background models (`scorpeon`, "3c50") exist; the PPM papers explore the sensitivity of $R$ to the background treatment.
- **Shortcut for learning:** the 2026 J0030 Zenodo package contains the reduced NICER event file, ARF and RMF used in the analysis (`Files/J0030_products/NICER/merged_cut.evt`, `merged_cutmpu7.arf`, `.rmf`), but it is **one 15.5 GB archive**; only download it deliberately.

## Tasks

1. **Offline:** `python ex06_phase_energy.py` (synthetic pulsar with an energy-dependent second peak). Reproduce the two panels.
2. **Real data (pick one):** (a) a few ks of J0030+0451 with a catalogue $(f,\dot f)$: fold a single segment, then two segments a few days apart and see the coherence break; (b) with PINT and a proper `.par`, assign phases to a month of segments; (c) use the Zenodo reduced file.
3. Build the 32-phase by PI 30 to 300 matrix; plot two cycles; mark the fluorescence-line rows; compare with Figure 1 of Kini et al. 2026.

## Exercises (with expected results)

1. **Coherence budget:** for a 6-year span ($1.9\times10^8$ s) and phase error below 0.01 cycles, $\delta f<5\times10^{-11}$ Hz; for $\dot f$, $\delta\dot f<2\,\delta\phi/T^2\approx6\times10^{-19}$ Hz/s. These are the accuracies a timing solution must deliver.
2. **Coherence experiment (synthetic):** simulate ten 10 ks segments spread over 100 days ($T=8.6\times10^6$ s) for $f=205.53$ Hz, $\dot f=-4\times10^{-16}$ Hz/s. Fold with the right $f$ and (a) the right $\dot f$; (b) $\dot f=0$: the phase error is $\dot fT^2/2\approx0.015$ cycles, invisible; (c) $f$ wrong by $10^{-7}$ Hz: $\delta f\,T\approx0.9$ cycles, the pulse is destroyed. Now redo the arithmetic for 6 years: $\dot fT^2/2\approx7$ cycles, so $\dot f$ *must* be modelled, and $\delta f$ must be below $5\times10^{-11}$ Hz. Which term dominates the coherence budget at which baseline?
3. **Energy-resolved profiles:** fold in three PI bands (30 to 80, 80 to 150, 150 to 300) and compare shapes, centroid phases and pulsed fractions (`pulsed_fraction`). In the demo, the second peak is harder: do you recover that? In real J0030 data, thermal emission from a hot spot softens/hardens with phase differently from a power-law component: write down what each would do to the matrix.
4. **Background estimate:** use the minimum-flux phases (or a high-PI band, 2 to 10 keV, where the pulsar is negligible) to estimate the background spectrum; subtract and see how the shape of the lowest-energy bins changes.
5. **Counting statistics:** compute the total counts and the fraction in the pulse; estimate, via the Fisher information for a sinusoid, how precisely the fundamental phase can be measured; compare with the phase scatter among independent folds of subsets.
6. **Phase-matrix bookkeeping:** show that summing over PI gives the bolometric profile used in simple fits and that summing over phase gives the spectrum; why does the joint matrix carry more information than either?
7. **Cross-check against the paper:** with the Zenodo reduced data (if you downloaded it), reproduce the exposure (2,974 ks after screening for the 2026 dataset; 1,936,864 s in the earlier V24 file name) and count the events in PI 30 to 299.

## Pitfalls

- Folding with a stale or wrong position/$\dot f$ (everything looks like noise).
- Forgetting that PINT loads need the right `TIMEREF` (barycentred vs geocentric).
- Reading fluorescence lines and detector artefacts as source features.

## Gate questions

1. Why is the radius information in the *shape* of the pulse, not its amplitude alone?
2. What breaks if the background shape is wrong at low PI?
3. Why is a joint NICER+XMM analysis used for J0030?

## One-page cheat sheet contents

Phase assignment recipe; accuracy budget; matrix construction; background strategy; list of data files in the Zenodo release.
