# %% [markdown]
# # Example 05: blind period search and pulse profile (Crab-like)
# Real data: barycentre first (Module 04) then  python ex05_crab_period.py file_bary.evt 29.0 30.0
# %%
import sys, tempfile, numpy as np
from _common import plt, savefig
from nicerkit import archive, fold

if __name__ == "__main__":
    if "--demo" in sys.argv:
        T, f_true = 3000.0, 29.60337
        t = fold.simulate_events(T, f_true, -3.7e-10, src_rate=2.5, bkg_rate=8.0, seed=11)
        flo, fhi = 29.55, 29.65
    else:
        d = archive.read_events(sys.argv[1]); t = d["t"]; T = t.max() - t.min()
        flo, fhi = float(sys.argv[2]), float(sys.argv[3]); f_true = None
    grid = fold.frequency_grid(flo, fhi, T, oversample=5)
    z = fold.z2m_scan(t, grid, m=2)
    fbest = grid[np.argmax(z)]
    H, m, fap = fold.htest(fold.phases(t, fbest))
    print(f"N={len(t)}  T={T:.0f}s  best f = {fbest:.6f} Hz (resolution 1/T = {1/T:.1e}),"
          f" Z2_2 = {z.max():.1f}, H = {H:.1f} (m={m}), FAP ~ {max(fap,1e-300):.1e}")
    if f_true: print(f"truth {f_true:.6f}; |df| = {abs(fbest-f_true):.2e} Hz")
    x, c, e = fold.fold(t, fbest, nbins=64)
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.6))
    ax[0].plot(grid, z, lw=0.7); ax[0].set(xlabel="f [Hz]", ylabel="Z$^2_2$", title="blind search")
    ax[1].errorbar(np.r_[x, x + 1], np.r_[c, c], np.r_[e, e], fmt=".", ms=3, lw=0.6)
    ax[1].set(xlabel="phase (2 cycles)", ylabel="counts", title=f"folded at {fbest:.5f} Hz")
    savefig(fig, "ex05_period_search%s.png" % ("_demo" if "--demo" in sys.argv else ""))
