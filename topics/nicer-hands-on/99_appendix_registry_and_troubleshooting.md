# Appendix: data registry, units, troubleshooting and references

> Items marked (verify) are from memory or not independently confirmed during writing.

## 1. Data registry

| What | Where | Notes |
| --- | --- | --- |
| NICER observation catalog | HEASARC table `nicermastr` (TAP: `https://heasarc.gsfc.nasa.gov/xamin/vo/tap`) | one row per sequence |
| NICER archive tree | `https://heasarc.gsfc.nasa.gov/FTP/nicer/data/obs/YYYY_MM/<obsid>/` | example from the HEASARC tutorial: `2021_11/4142010107` (Cyg X-3) |
| J0030 (2026) | Zenodo 10.5281/zenodo.20271881 (v3, 15.5 GB tar; contains `mass_radius_contours/`, reduced NICER and XMM products, notebooks, MultiNest outputs) | also cited by the paper: 10.5281/zenodo.18741942 (samples) |
| J0030 (2024 reanalysis) | Zenodo 10.5281/zenodo.8239000 | |
| J0030 (2019, Illinois-Maryland) | Zenodo 10.5281/zenodo.3473466 | |
| J0740 (2021, Illinois-Maryland) | Zenodo 10.5281/zenodo.4670689 | files named like `NICER+XMM-relative_J0740_RM.txt` (RM = radius and mass columns; check order) |
| J0437 (Choudhury 2024) | Zenodo 10.5281/zenodo.13766753 | reproduction package |
| J0614 (Mauviard 2025) | Zenodo 10.5281/zenodo.15603406 | `MR_samples_and_contours.tar.gz`, 3.4 MB |
| J0030 combination with model systematics | Zenodo 10.5281/zenodo.19222905 | scripts and posteriors |
| Software | HEASoft/CALDB; PINT; NICERsoft; X-PSI; astroquery | see Module 01 |

## 2. Units and constants

$G=6.6743\times10^{-8}$ cgs; $c=2.99792458\times10^{10}$ cm/s; $M_\odot=1.98847\times10^{33}$ g; $GM_\odot/c^2=1.4766$ km ($r_s=2.953$ km); $\rho_{\rm sat}=2.66\times10^{14}$ g/cm$^3$ ($n_0=0.16$ fm$^{-3}$); 1 MeV/fm$^3=1.602\times10^{33}$ dyn/cm$^2$; PI channel = 10 eV; $u=2GM/Rc^2$ (toy-model compactness) versus $C=GM/Rc^2$ (TOV, $\Lambda$): do not mix.

## 3. Troubleshooting

| Symptom | Likely cause |
| --- | --- |
| `find_obs` returns nothing | wrong coordinates (check SIMBAD), too small radius, catalog name; try `Heasarc.list_catalogs(keywords=['nicer'])` |
| Download fails or empty | data still proprietary; wrong month directory; network/proxy; use `locate_data` + `download_data` |
| `nicerl2` finds no good time | over-strict screening, light-leak period; read the `nicerl2` thread on relaxing criteria |
| Folded profile flat | not barycentred; wrong position or frequency; $\dot f$ ignored over long spans |
| Sample columns look wrong | `mr.sanity_check` fails: swapped M/R or weighted file |
| EOS posterior piles at a prior edge | check prior bounds, causal truncation, the $M_{\rm max}$ constraint and the $P_c$ grid reach (`log_Pc_max=36.7`) |
| `emcee` progress bar error | `pip install tqdm` |
| Everything slow | use the numba path (`mr_curve_pp`), several cores (`NPROC`), fewer $P_c$ points (`n_pc`) |

## 4. Reading list

Gendreau et al. 2016 (NICER instrument); Bogdanov et al. 2019a,b (ApJL 887, L25 and L26); Riley et al. 2019 and Miller et al. 2019 (J0030); Riley et al. 2021 and Miller et al. 2021 (J0740); Salmi et al. 2024 (J0740, ApJ 974, 294); Choudhury et al. 2024 (J0437, ApJL 971, L20) and Miller et al. 2026 (ApJL 1000, L48); Mauviard et al. 2025 (J0614, ApJ 995, 60); Salmi et al. 2024b and Qi et al. 2025 (J1231); Kini et al. 2026 (J0030, arXiv:2602.23743); Riley et al. 2023 (X-PSI); Read et al. 2009 (piecewise polytropes); Raaijmakers et al. 2019 (EOS from NICER); Chatziioannou et al. 2025 (review).

## 5. What the guide does not cover

Spectral fitting with response matrices in detail (use XSPEC/PyXspec), proprietary data, thermal-evolution fits to cooling stars, gravitational-wave inference, magnetar and accreting-pulsar timing, and X-PSI internals.
