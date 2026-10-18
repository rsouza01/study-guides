"""Archive helpers: HEASARC NICER queries/downloads, Zenodo downloads, and FITS event reading.

NETWORK FUNCTIONS (find_obs, download_obs, zenodo_*) WERE NOT TESTED against the live servers by
the author of this guide (the sandbox had no access to HEASARC or Zenodo). They follow the
documented APIs (astroquery.heasarc >= 0.4.10 TAP interface; Zenodo REST API). If something
breaks, read the exception and the docstrings, then fix; the offline pieces (read_events,
make_fake_nicer_evt, parse_zenodo_record) are unit-tested.
"""
import hashlib
import os
import urllib.request
import json
import numpy as np

# Target positions (ICRS, degrees) from memory -- verify with SIMBAD before relying on them.
TARGETS = {
    "crab":        (83.633212, 22.014471),     # PSR B0531+21
    "j0030+0451":  (7.614, 4.861),
    "j0437-4715":  (69.316, -47.253),
    "j0740+6620":  (115.191, 66.343),
    "j0614-3329":  (93.543, -33.499),
    "4u1820-30":   (275.919, -30.361),         # burster in NGC 6624
    "aqlx-1":      (287.817, 0.585),
    "cygx-2":      (326.171, 38.322),
    "scox-1":      (244.979, -15.640),
}

HEASARC_FTP = "https://heasarc.gsfc.nasa.gov/FTP/nicer/data/obs"


# ----------------------------------------------------------------------------- HEASARC
def find_obs(target=None, ra=None, dec=None, radius_arcmin=5.0, catalog="nicermastr"):
    """Return an astropy Table of NICER observation sequences near a target.

    Uses astroquery.heasarc.Heasarc.query_region (TAP). Inspect the returned columns
    (`tab.colnames`) -- names such as obsid, time, exposure, name, ra, dec are expected, but
    verify; HEASARC occasionally renames fields.
    """
    import astropy.units as u
    from astropy.coordinates import SkyCoord
    from astroquery.heasarc import Heasarc
    if target is not None:
        ra, dec = TARGETS[target.lower()]
    pos = SkyCoord(ra * u.deg, dec * u.deg, frame="icrs")
    tab = Heasarc.query_region(pos, catalog=catalog, radius=radius_arcmin * u.arcmin)
    return tab


def _col(tab, key):
    for c in tab.colnames:
        if c.lower() == key:
            return c
    for c in tab.colnames:
        if key in c.lower():
            return c
    raise KeyError(f"no column like '{key}' in {tab.colnames}")


def summarize_obs(tab):
    """Print a compact table: obsid, start (MJD), exposure (s)."""
    ob, tm, ex = _col(tab, "obsid"), _col(tab, "time"), _col(tab, "exposure")
    order = np.argsort(np.asarray(tab[tm], float))
    tot = 0.0
    for i in order:
        print(f"{tab[ob][i]!s:>12}  MJD {float(tab[tm][i]):10.4f}  exposure {float(tab[ex][i]):9.1f} s")
        tot += float(tab[ex][i])
    print(f"{len(tab)} sequences, total exposure {tot/1e3:.1f} ks")


def obs_url(obsid, mjd):
    """Archive directory URL for one observation (HEASARC groups by start month)."""
    from astropy.time import Time
    t = Time(float(mjd), format="mjd")
    return f"{HEASARC_FTP}/{t.datetime.year:04d}_{t.datetime.month:02d}/{int(obsid):010d}/"


def download_obs(obsid, mjd, dest=".", use_wget=True):
    """Download one observation directory (wget recursive, the HEASARC-recommended way)."""
    import subprocess
    os.makedirs(dest, exist_ok=True)
    url = obs_url(obsid, mjd)
    cmd = ["wget", "-q", "-nH", "--no-check-certificate", "--cut-dirs=5", "-r", "-l0", "-c", "-N",
           "-np", "-R", "index*", "-erobots=off", "--retr-symlinks", url]
    print(" ".join(cmd))
    if use_wget:
        subprocess.run(cmd, cwd=dest, check=True)
    return os.path.join(dest, f"{int(obsid):010d}")


# ----------------------------------------------------------------------------- Zenodo
def parse_zenodo_record(js):
    """List of (name, size, md5, url) from a Zenodo API record (InvenioRDM or legacy)."""
    files = js.get("files", [])
    out = []
    if isinstance(files, dict):               # some responses: {"entries": {...}}
        files = list(files.get("entries", {}).values())
    for f in files:
        name = f.get("key") or f.get("filename") or f.get("name")
        size = f.get("size")
        md5 = (f.get("checksum") or "").replace("md5:", "")
        url = (f.get("links") or {}).get("self") or (f.get("links") or {}).get("download")
        out.append((name, size, md5, url))
    return out


def zenodo_files(record_id):
    with urllib.request.urlopen(f"https://zenodo.org/api/records/{record_id}", timeout=60) as r:
        js = json.load(r)
    return parse_zenodo_record(js)


def zenodo_download(record_id, filename, dest=".", verify=True):
    """Download one file from a Zenodo record (public records need no token)."""
    os.makedirs(dest, exist_ok=True)
    path = os.path.join(dest, filename)
    url = f"https://zenodo.org/records/{record_id}/files/{filename}?download=1"
    print("GET", url)
    urllib.request.urlretrieve(url, path)
    if verify:
        listing = {n: m for n, _, m, _ in zenodo_files(record_id)}
        md5 = listing.get(filename)
        if md5:
            h = hashlib.md5()
            with open(path, "rb") as fh:
                for chunk in iter(lambda: fh.read(1 << 20), b""):
                    h.update(chunk)
            assert h.hexdigest() == md5, f"checksum mismatch for {filename}"
            print("md5 ok")
    return path


# ----------------------------------------------------------------------------- FITS events
def read_events(path, extname="EVENTS"):
    """Read a NICER (or NICER-like) event file.

    Returns dict(t [s since MJDREF], pi [PI channel, 10 eV each], gti [(start, stop) array],
    header=dict(...)). Works on cleaned files from nicerl2 ('ni<obsid>_0mpu7_cl.evt') and,
    after barycorr, on barycentred files.
    """
    from astropy.io import fits
    with fits.open(path) as hdul:
        ev = hdul[extname]
        t = np.asarray(ev.data["TIME"], float)
        pi = np.asarray(ev.data["PI"], int) if "PI" in ev.columns.names else None
        hdr = ev.header
        info = {k: hdr.get(k) for k in ("OBJECT", "OBS_ID", "TSTART", "TSTOP", "EXPOSURE", "TIMESYS",
                                         "TIMEREF", "MJDREFI", "MJDREFF", "RA_OBJ", "DEC_OBJ", "TELESCOP",
                                         "INSTRUME")}
        gti = None
        for name in ("GTI", "STDGTI"):
            if name in hdul:
                g = hdul[name].data
                gti = np.column_stack([g["START"], g["STOP"]]).astype(float)
                break
    return dict(t=t, pi=pi, gti=gti, header=info)


def make_fake_nicer_evt(path, t, pi, gti=None, obj="FAKE", mjdrefi=56658, mjdreff=7.7759259259259e-4):
    """Write a minimal FITS event file with the columns/keywords that read_events expects.
    For tests and offline development of your analysis scripts."""
    from astropy.io import fits
    cols = [fits.Column(name="TIME", format="D", array=np.asarray(t, float)),
            fits.Column(name="PI", format="I", array=np.asarray(pi, np.int16))]
    ev = fits.BinTableHDU.from_columns(cols, name="EVENTS")
    ev.header.update(dict(OBJECT=obj, TSTART=float(np.min(t)), TSTOP=float(np.max(t)),
                          EXPOSURE=float(np.max(t) - np.min(t)), TIMESYS="TDB", TIMEREF="SOLARSYSTEM",
                          MJDREFI=mjdrefi, MJDREFF=mjdreff, TELESCOP="NICER", INSTRUME="XTI"))
    if gti is None:
        gti = [(float(np.min(t)), float(np.max(t)))]
    g = np.asarray(gti, float)
    gh = fits.BinTableHDU.from_columns([fits.Column(name="START", format="D", array=g[:, 0]),
                                        fits.Column(name="STOP", format="D", array=g[:, 1])], name="GTI")
    fits.HDUList([fits.PrimaryHDU(), ev, gh]).writeto(path, overwrite=True)
    return path
