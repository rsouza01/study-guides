# %% [markdown]
# # Example 06: phase-energy matrix (the 'Figure 1' of NICER pulse-profile papers)
# Real data: events must be barycentred AND you need a timing solution; here you give f, fdot
# (use PINT/photonphase for multi-year coherence, Module 06). --demo makes a synthetic ms pulsar.
# %%
import sys, numpy as np
from _common import plt, savefig
from nicerkit import fold

def demo_events():
    rng = np.random.default_rng(5); f0 = 205.53
    t = fold.simulate_events(6.0e4, f0, 0.0, src_rate=3.0, bkg_rate=0.3, seed=5,
                             profile=lambda ph: 1 + 0.9 * np.cos(2*np.pi*(ph-0.3)) + 0.35 * np.cos(4*np.pi*(ph-0.55)))
    ph = (f0 * t) % 1.0
    # energy-dependent: second peak harder
    pi = np.where(rng.uniform(size=len(t)) < 0.5 + 0.4 * (np.cos(4*np.pi*(ph-0.55)) > 0.2),
                  rng.normal(140, 45, len(t)), rng.normal(70, 25, len(t))).astype(int)
    return t, np.clip(pi, 30, 299), f0

if __name__ == "__main__":
    t, pi, f0 = demo_events()
    H, edges = fold.phase_energy_matrix(t, pi, f0, nphase=32, pi_edges=np.arange(30, 301, 10))
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    ax[0].imshow(np.r_[H, H].T, origin="lower", aspect="auto", extent=[0, 2, 30, 300]); ax[0].set(xlabel="phase", ylabel="PI")
    for lo, hi, c in [(30, 80, "C0"), (80, 150, "C1"), (150, 300, "C2")]:
        sel = (pi >= lo) & (pi < hi); x, cnt, e = fold.fold(t[sel], f0, nbins=32, t0=0.0)
        ax[1].errorbar(x, cnt / cnt.mean(), e / cnt.mean(), color=c, fmt=".-", label=f"PI {lo}-{hi}")
    ax[1].legend(); ax[1].set(xlabel="phase", ylabel="normalised counts")
    savefig(fig, "ex06_phase_energy_demo.png")
