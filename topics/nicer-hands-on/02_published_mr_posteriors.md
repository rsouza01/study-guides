# Module 02 (Level 0): the published NICER mass-radius posteriors

**Resources:** the papers and Zenodo records in the table below; `nicerkit.mr`; `examples/ex02_published_mr.py`.
**Time:** 1 to 2 sessions. **Start here**: nothing to install except Python, and you end with the plot at the center of the field.

## Why this matters

These posteriors are the *output* of pulse-profile modeling and the *input* of every EOS paper. Reading them with your own code (columns, units, weights, credible regions) is data literacy for neutron-star astrophysics, and it is the data you will use in Level 6.

## Diagnostic (15 minutes)

1. What do the 68% and 95% contours of a 2-D posterior contain, and why are they not unique?
2. Why can an equal-weight sample file and a weighted nested-sampling file describe the same posterior?
3. Name two reasons the same pulsar can have several published $(M,R)$ results.

## The table (verified where marked ✔; otherwise check the paper)

| Source | Result (68% unless stated) | Release | Notes |
| --- | --- | --- | --- |
| PSR J0030+0451 | Kini et al. 2026 (6 yr of data + XMM): **PDT-U** $M=1.43^{+0.20}_{-0.17}$, $R_{\rm eq}=12.68^{+1.31}_{-1.04}$ km; **ST+PDT** $M=1.29^{+0.13}_{-0.12}$, $R_{\rm eq}=11.63^{+0.95}_{-0.89}$ km ✔ | Zenodo 10.5281/zenodo.20271881 ✔ (**one 15.5 GB tar**; contains `mass_radius_contours/{weighted,equal_weight}_samples_PDTU.txt`, columns: weight, M, R / M, R ✔); the paper also cites 10.5281/zenodo.18741942 ✔ for samples | Earlier: Riley et al. 2019 and Miller et al. 2019 (Zenodo 10.5281/zenodo.3473466 ✔ for the Illinois-Maryland samples); Vinciguerra et al. 2024 (ST+PDT $11.71$ km, PDT-U $14.44$ km; Zenodo 10.5281/zenodo.8239000 ✔) |
| PSR J0740+6620 | Salmi et al. 2024: $R=12.49^{+1.28}_{-0.88}$ km, $M=2.073\pm0.069\,M_\odot$ ✔; $R<11.15$ km excluded at 95% ✔ | check the paper's data statement | Dittmann et al. 2024: $12.76^{+1.49}_{-1.02}$ km ✔; Miller et al. 2021 samples: Zenodo 10.5281/zenodo.4670689 ✔ (files like `NICER+XMM-relative_J0740_RM.txt`) |
| PSR J0437-4715 | Choudhury et al. 2024 (first analysis; from memory about 11.4 km at $M=1.418$; **verify**); Miller et al. 2026 (ApJL 1000, L48): with a modulated non-thermal component, symmetric 68% range **11.9 to 15.5 km** at $M=1.418\pm0.044\,M_\odot$ ✔ | Choudhury: Zenodo 10.5281/zenodo.13766753 ✔ | A good lesson in model dependence |
| PSR J0614-3329 | Mauviard et al. 2025: $R_{\rm eq}=10.29^{+1.01}_{-0.86}$ km, $M=1.44^{+0.06}_{-0.07}\,M_\odot$ ✔ | Zenodo 10.5281/zenodo.15603406 ✔ (v1.0.0: `MR_samples_and_contours.tar.gz`, **3.4 MB**; a newer version exists) | Smallest download: start here |
| PSR J1231-1411 | Salmi et al. 2024; a re-analysis (Qi et al. 2025) finds a smaller radius ✔ | see the papers | |
| PSR J1614-2230 | A new NICER paper appeared in September 2026 (arXiv 2609.00172); **check it** | | |

The 2026 literature is moving: read the abstracts, and always cite the exact release you used.

## Tasks

1. `from nicerkit import archive; archive.zenodo_files(15603406)` lists the files; `archive.zenodo_download(15603406, "MR_samples_and_contours.tar.gz", "data")`. (**Network function; untested by the author**: if it fails, download from the browser.) Untar and **read the README** and the first lines of each text file.
2. Write `sources.json` (see below) with the right `columns` string for each file (`"MR"`, `"RM"`, `"wMR"`), then run `python ex02_published_mr.py` (without `--demo`).
3. Run the demo (`--demo`) first to see the target figure with synthetic stand-ins.

```json
[{"name": "J0614 (Mauviard+25)", "path": "data/J0614_MR_samples.txt", "columns": "MR"},
 {"name": "J0030 PDT-U (Kini+26)", "path": "data/equal_weight_samples_PDTU.txt", "columns": "MR"}]
```

## Exercises (with expected results)

1. **Read and sanity-check:** `mr.load_samples` then `mr.sanity_check`; for J0614 expect median $R\approx10.3$ km and $M\approx1.44$; if the check raises, your columns are swapped.
2. **Summaries:** print median and 68% interval of $R$ and $M$ for each source; compare with the table above (equal-tailed 16/84% percentiles). Differences of 0.01 to 0.02 km are rounding.
3. **Contours:** plot the 68% and 95% regions (`GridDensity.credible_levels`) and overlay the SLy curve (`mr_curve_pp`). **Expected:** SLy crosses the J0030 and J0740 contours, and lies above the J0614 median at $1.44\,M_\odot$ ($R_{\rm SLy}\approx11.7$ vs $10.3$ km, about 1.5 sigma).
4. **Model dependence:** plot J0030 ST+PDT and PDT-U (2026) together, then add the 2024 values from the table as Gaussian stand-ins. What changed between 2024 and 2026 for PDT-U (radius down by about 1.8 km) and what did not (ST+PDT)? Write three sentences on why (more data, sampler settings, bimodality: see Kini et al. 2026, section 4.1).
5. **Weighted vs equal weight:** for a weighted nested-sampling file, compute the 68% interval (a) ignoring weights, (b) with `resample_equal_weight`; the first is wrong. By how much?
6. **A naive combination (and why not to do it):** take three sources near $1.4\,M_\odot$ (J0030 PDT-U $12.68\pm1.18$, J0614 $10.29\pm0.94$, J0437 about $13.5\pm1.6$) and form an inverse-variance mean radius: about $11.6\pm0.7$ km. Why is this *not* the right way to combine them? (They have different masses; the posteriors are non-Gaussian; the EOS ties $R(M)$ across masses; Module 10 does it properly.)
7. **Credible-region area:** compute the area of the 68% region (km $\times M_\odot$) for each source; rank them by constraining power.
8. **Mass priors:** for J0740, J0437 and J0614 the mass posterior is essentially the radio-timing prior; for J0030 it is not. Verify by plotting the marginal mass posteriors and noting their widths ($\sigma_M\approx0.07$, 0.04, 0.07 versus 0.18).

## Pitfalls

- Treating a contour file (R, M order, closed polygon) as samples.
- Column order: Miller et al. "RM" files list radius first; Riley/Salmi packages differ.
- Citing "the" J0030 radius without saying which hot-spot model and which dataset.

## Gate questions

1. Which published $(M,R)$ results does your EOS inference use, and which model/dataset for each?
2. Why is the J0030 PDT-U posterior bimodal and what does that do to a KDE?
3. How does the mass prior enter the interpretation of a radius at fixed mass?

## One-page cheat sheet contents

The table above; file formats and column orders you verified; the $M$-$R$ plot recipe (KDE grid, level thresholds).
