"""Thermonuclear (type I) X-ray burst finder and simple decay fit for LMXB light curves."""
import numpy as np
from scipy.optimize import curve_fit


def bin_events(t, dt=1.0, t_start=None, t_stop=None):
    t_start = t.min() if t_start is None else t_start
    t_stop = t.max() if t_stop is None else t_stop
    edges = np.arange(t_start, t_stop + dt, dt)
    c, _ = np.histogram(t, bins=edges)
    return 0.5 * (edges[1:] + edges[:-1]), c / dt, edges


def find_bursts(tc, rate, dt=1.0, window=120.0, nsigma=6.0, min_ratio=2.5, merge_gap=30.0):
    """Flag bins where rate exceeds a running-median baseline by nsigma (Poisson) and min_ratio.
    Returns list of dicts: t_start, t_peak, peak_rate, baseline.  Gaps in tc (GTIs) are handled
    simply by using only the bins you pass in."""
    n = len(rate)
    w = max(3, int(window / dt))
    base = np.empty(n)
    for i in range(n):
        lo, hi = max(0, i - w), min(n, i + w + 1)
        seg = np.concatenate([rate[lo:max(lo, i - 5)], rate[min(hi, i + 25):hi]])
        base[i] = np.median(seg) if len(seg) > 5 else np.median(rate[lo:hi])
    sig = np.sqrt(np.maximum(base, 1.0) / dt)
    flag = (rate > base + nsigma * sig) & (rate > min_ratio * base)
    out, i = [], 0
    while i < n:
        if flag[i]:
            j = i
            while j < n and (flag[j] or (j - i) * dt < merge_gap and np.any(flag[j:j + int(merge_gap / dt)])):
                j += 1
            seg = slice(i, j)
            ip = i + int(np.argmax(rate[seg]))
            out.append(dict(t_start=tc[i], t_peak=tc[ip], peak_rate=rate[ip], baseline=base[ip]))
            i = j
        else:
            i += 1
    return out


def exp_decay(t, a, tau, b):
    return a * np.exp(-t / tau) + b


def fit_decay(tc, rate, t_peak, baseline, t_max=60.0):
    """Fit a*exp(-(t-t_peak)/tau)+baseline to the post-peak light curve; returns (tau, tau_err)."""
    m = (tc >= t_peak) & (tc <= t_peak + t_max)
    x, y = tc[m] - t_peak, rate[m]
    p0 = [y.max() - baseline, 10.0, baseline]
    popt, pcov = curve_fit(exp_decay, x, y, p0=p0, sigma=np.sqrt(np.maximum(y, 1.0)), maxfev=20000)
    return popt[1], float(np.sqrt(pcov[1, 1]))


def simulate_lightcurve(T=2000.0, dt=1.0, base=800.0, bursts=((600.0, 12.0, 4000.0), (1500.0, 8.0, 3000.0)),
                        rise=1.0, seed=0):
    """Persistent emission + fast-rise exponential-decay bursts (t0, tau, peak); Poisson counts."""
    rng = np.random.default_rng(seed)
    t = np.arange(0, T, dt)
    lam = np.full_like(t, base)
    for t0, tau, pk in bursts:
        x = np.maximum(t - t0, 0.0)
        lam += np.where(t > t0, pk * np.exp(-x / tau) * (1 - np.exp(-x / rise)), 0.0)
    return t + 0.5 * dt, rng.poisson(lam * dt) / dt
