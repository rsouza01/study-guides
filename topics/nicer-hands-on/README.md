# nicerkit

Small, tested helper package for the "NICER Hands-On" guide.

    conda env create -f env/environment.yml && conda activate nicer     # or: pip install -r env/requirements.txt
    python -m pytest -q                                                 # ~3 min (the EOS injection test dominates)
    cd examples && python ex09_tov_eos.py                                # offline, 5 s
    python ex05_crab_period.py --demo                                   # offline

Layout: `nicerkit/` (library), `tests/`, `examples/` (percent-cell scripts), `env/`.
Network functions in `nicerkit/archive.py` were written against the documented HEASARC/Zenodo APIs
but not run against the live servers by the author; everything else is covered by tests.
