import numpy as np
from nicerkit import archive, fold


def test_zenodo_record_parsing_both_layouts():
    js = {"files": [{"key": "a.tar.gz", "size": 10, "checksum": "md5:abc",
                     "links": {"self": "https://zenodo.org/api/records/1/files/a.tar.gz/content"}}]}
    assert archive.parse_zenodo_record(js)[0][:3] == ("a.tar.gz", 10, "abc")
    js2 = {"files": {"entries": {"b.txt": {"key": "b.txt", "size": 5, "checksum": "md5:def", "links": {"self": "u"}}}}}
    assert archive.parse_zenodo_record(js2)[0][0] == "b.txt"


def test_obs_url_pattern():
    # 2021-11 directory as in the HEASARC heasoftpy tutorial (ObsID 4142010107)
    url = archive.obs_url(4142010107, 59520.0)    # MJD 59520 = 2021-11-08
    assert url.endswith("/2021_11/4142010107/")


def test_fits_roundtrip_and_end_to_end_period_search(tmp_path):
    f0, T = 29.6, 2500.0
    t = fold.simulate_events(T, f0, 0.0, src_rate=30.0, bkg_rate=10.0, seed=7)
    pi = np.random.default_rng(0).integers(30, 300, size=len(t))
    p = archive.make_fake_nicer_evt(tmp_path / "ni_fake_cl.evt", t, pi)
    d = archive.read_events(p)
    assert len(d["t"]) == len(t) and d["pi"].max() < 300 and d["gti"].shape == (1, 2)
    grid = fold.frequency_grid(29.58, 29.62, T)
    z = fold.z2m_scan(d["t"], grid, m=2)
    assert abs(grid[np.argmax(z)] - f0) < 2.0 / T
