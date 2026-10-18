"""Mass-radius posterior samples: loading, summaries, KDE grids, credible regions."""
import numpy as np
from scipy.stats import gaussian_kde
from scipy.interpolate import RegularGridInterpolator


def summarize(x, q=(16, 50, 84)):
    """median and (-, +) 68% interval of a 1-D sample (optionally weighted via numpy only)."""
    lo, med, hi = np.percentile(x, q)
    return med, med - lo, hi - med


def load_samples(path, columns="MR", weighted=False, skiprows=0, delimiter=None):
    """Load a whitespace/CSV text file of posterior samples.

    columns: string of column roles per file column, e.g. "MR" (mass, radius), "RM",
             "wMR" (weight, mass, radius).  Extra columns are ignored if you pass a
             longer-than-needed file: roles beyond len(columns) are dropped.
    Returns dict(M=..., R=..., w=... or None).  ALWAYS check the first rows against the
    README of the Zenodo record: column orders differ between releases.
    """
    arr = np.loadtxt(path, skiprows=skiprows, delimiter=delimiter, ndmin=2)
    roles = {c: i for i, c in enumerate(columns)}
    M, R = arr[:, roles["M"]], arr[:, roles["R"]]
    w = arr[:, roles["w"]] if "w" in roles else None
    return dict(M=M, R=R, w=w)


def sanity_check(M, R, name=""):
    """Raise if the columns look swapped or in the wrong units."""
    ok = (0.5 < np.median(M) < 3.5) and (5.0 < np.median(R) < 20.0)
    if not ok:
        raise ValueError(f"{name}: median M={np.median(M):.3g}, R={np.median(R):.3g}; "
                         "columns swapped or units are not (Msun, km)?")
    return True


def resample_equal_weight(M, R, w, n=None, seed=0):
    """Turn weighted nested-sampling output into equal-weight samples."""
    rng = np.random.default_rng(seed)
    n = n or len(M)
    p = w / w.sum()
    idx = rng.choice(len(M), size=n, p=p)
    return M[idx], R[idx]


class GridDensity:
    """2-D density p(M, R) on a regular grid (Gaussian KDE), with fast bilinear lookup.

    Use for likelihoods: EOS inference evaluates p(M, R_EOS(M)) thousands of times.
    """

    def __init__(self, M, R, w=None, nM=160, nR=160, bw=None, pad=3.0):
        M, R = np.asarray(M, float), np.asarray(R, float)
        kde = gaussian_kde(np.vstack([M, R]), weights=w, bw_method=bw)
        sM, sR = M.std(), R.std()
        self.Mg = np.linspace(M.min() - pad * sM, M.max() + pad * sM, nM)
        self.Rg = np.linspace(R.min() - pad * sR, R.max() + pad * sR, nR)
        MM, RR = np.meshgrid(self.Mg, self.Rg, indexing="ij")
        Z = kde(np.vstack([MM.ravel(), RR.ravel()])).reshape(MM.shape)
        self.Z = Z
        self._interp = RegularGridInterpolator((self.Mg, self.Rg), Z, bounds_error=False, fill_value=0.0)

    def __call__(self, M, R):
        pts = np.column_stack([np.broadcast_to(M, np.shape(R)), R]) if np.ndim(M) == 0 else np.column_stack([M, R])
        return self._interp(pts)

    def level_for_mass(self, fraction):
        """Density threshold whose superlevel set contains `fraction` of the probability."""
        z = self.Z.ravel()
        o = np.argsort(z)[::-1]
        cdf = np.cumsum(z[o])
        cdf /= cdf[-1]
        return z[o][np.searchsorted(cdf, fraction)]

    def credible_levels(self, fractions=(0.68, 0.95)):
        return [self.level_for_mass(f) for f in fractions]


def gaussian_mr(M0, R0, sM, sR, rho=0.0, n=20000, seed=0):
    """Synthetic correlated-Gaussian (M, R) 'posterior' for tests and injection studies."""
    rng = np.random.default_rng(seed)
    cov = np.array([[sM**2, rho * sM * sR], [rho * sM * sR, sR**2]])
    x = rng.multivariate_normal([M0, R0], cov, size=n)
    return x[:, 0], x[:, 1]
