"""Pulsar timing statistics on photon arrival times (already barycentred, seconds)."""
import numpy as np


def phases(t, f, fdot=0.0, t0=None, fddot=0.0):
    """Rotational phase (cycles, in [0,1)) for times t (s)."""
    t = np.asarray(t, float)
    t0 = t.min() if t0 is None else t0
    dt = t - t0
    ph = f * dt + 0.5 * fdot * dt**2 + fddot * dt**3 / 6.0
    return ph - np.floor(ph)


def z2m(ph, m=2, weights=None):
    """Z^2_m statistic (Buccheri et al. 1983). Under H0 ~ chi^2 with 2m dof."""
    ph = np.asarray(ph, float)
    w = np.ones_like(ph) if weights is None else np.asarray(weights, float)
    N = w.sum() if weights is None else (w**2).sum()
    s = 0.0
    for k in range(1, m + 1):
        c = np.sum(w * np.cos(2 * np.pi * k * ph))
        s_ = np.sum(w * np.sin(2 * np.pi * k * ph))
        s += c * c + s_ * s_
    return 2.0 * s / N


def htest(ph, mmax=20):
    """de Jager H-test: H = max_m (Z^2_m - 4m + 4). FAP ~ exp(-0.4 H). Returns (H, m_best, FAP)."""
    best, mb = -np.inf, 1
    for m in range(1, mmax + 1):
        h = z2m(ph, m) - 4 * m + 4
        if h > best:
            best, mb = h, m
    return best, mb, float(np.exp(-0.4 * best)) if best > 0 else 1.0


def z2m_scan(t, freqs, m=2, fdot=0.0, chunk=64):
    """Z^2_m on a frequency grid (vectorised in chunks)."""
    t = np.asarray(t, float)
    dt = t - t.min()
    N = len(t)
    out = np.empty(len(freqs))
    for i0 in range(0, len(freqs), chunk):
        f = np.asarray(freqs[i0:i0 + chunk])[:, None]
        ph = f * dt[None, :] + 0.5 * fdot * dt[None, :] ** 2
        s = np.zeros(f.shape[0])
        for k in range(1, m + 1):
            s += np.cos(2 * np.pi * k * ph).sum(1) ** 2 + np.sin(2 * np.pi * k * ph).sum(1) ** 2
        out[i0:i0 + chunk] = 2.0 * s / N
    return out


def frequency_grid(f_lo, f_hi, T, oversample=5):
    """Independent-Fourier-spacing grid: df = 1/(oversample * T)."""
    return np.arange(f_lo, f_hi, 1.0 / (oversample * T))


def fold(t, f, fdot=0.0, nbins=32, weights=None, t0=None):
    """Folded profile: counts per phase bin, and Poisson errors."""
    ph = phases(t, f, fdot, t0)
    counts, edges = np.histogram(ph, bins=nbins, range=(0, 1), weights=weights)
    err = np.sqrt(np.histogram(ph, bins=nbins, range=(0, 1))[0]) if weights is None else np.sqrt(
        np.histogram(ph, bins=nbins, range=(0, 1), weights=np.asarray(weights) ** 2)[0])
    return 0.5 * (edges[1:] + edges[:-1]), counts, err


def phase_energy_matrix(t, pi, f, fdot=0.0, nphase=32, pi_edges=None, t0=None):
    """2-D counts[phase_bin, energy_bin], the 'Figure 1' of NICER pulse-profile papers.
    pi: PI channel of each event (10 eV per channel; 30-300 ~ 0.3-3.0 keV)."""
    ph = phases(t, f, fdot, t0)
    if pi_edges is None:
        pi_edges = np.arange(30, 301, 10)
    H, _, _ = np.histogram2d(ph, pi, bins=[np.linspace(0, 1, nphase + 1), pi_edges])
    return H, pi_edges


def pulsed_fraction(profile, kind="amplitude"):
    """Pulsed fraction of a folded profile (counts per bin, background included).

    kind="amplitude": (max - min) / (max + min)   (what people quote for bright pulsars)
    kind="rms":       sqrt(2 * sum_k |a_k|^2) / a_0 over all harmonics k>=1 (can exceed 1 for
                      narrow peaks; noise-biased for faint sources)
    """
    p = np.asarray(profile, float)
    if kind == "amplitude":
        return float((p.max() - p.min()) / (p.max() + p.min()))
    n = len(p)
    a = np.fft.rfft(p)[1:] / n
    return float(np.sqrt(2.0 * np.sum(np.abs(a) ** 2)) / p.mean())


def simulate_events(T, f0, fdot=0.0, src_rate=50.0, bkg_rate=10.0, profile=None, seed=0, t_start=0.0):
    """Simulate barycentred photon arrival times with a periodic profile (thinning method).
    profile(phase) must return a non-negative shape with mean 1 (default: one Gaussian peak)."""
    rng = np.random.default_rng(seed)
    if profile is None:
        def profile(ph):
            x = (ph - 0.3 + 0.5) % 1.0 - 0.5
            g = np.exp(-0.5 * (x / 0.05) ** 2)
            return g / g.mean() if np.ndim(g) else g
        grid = np.linspace(0, 1, 1000, endpoint=False)
        norm = profile(grid).mean()
        _p = profile
        profile = lambda ph: _p(ph) / norm
    lam_max = (src_rate * profile(np.linspace(0, 1, 2000, endpoint=False)).max()) + bkg_rate
    n_cand = rng.poisson(lam_max * T)
    t = np.sort(rng.uniform(0.0, T, n_cand))
    ph = f0 * t + 0.5 * fdot * t**2
    ph -= np.floor(ph)
    lam = src_rate * profile(ph) + bkg_rate
    keep = rng.uniform(0, lam_max, n_cand) < lam
    return t[keep] + t_start


def fft_power_search(t, dt=0.002, pad=4, fmin=None, fmax=None):
    """Fast first-stage search: bin events, zero-padded FFT, Leahy-normalised power.

    Leahy power = 2 |FFT|^2 / N_photons; pure noise has mean 2 (chi^2 with 2 dof).
    Resolution is 1/T (oversampled by `pad`). Use z2m_scan on a narrow window to refine,
    and remember: this ignores fdot (fine when fdot * T^2 << 1/T, i.e. short segments)."""
    t = np.asarray(t, float)
    T = t.max() - t.min()
    nb = int(np.ceil(T / dt))
    counts, _ = np.histogram(t - t.min(), bins=nb, range=(0, nb * dt))
    n_fft = int(2 ** np.ceil(np.log2(nb * pad)))
    spec = np.fft.rfft(counts - counts.mean(), n=n_fft)
    power = 2.0 * np.abs(spec) ** 2 / len(t)
    f = np.fft.rfftfreq(n_fft, d=dt)
    m = np.ones_like(f, bool)
    if fmin is not None: m &= f >= fmin
    if fmax is not None: m &= f <= fmax
    return f[m], power[m]
