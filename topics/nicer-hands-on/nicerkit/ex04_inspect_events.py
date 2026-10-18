# %% [markdown]
# # Example 04: look inside a NICER cleaned event file (light curve + PI spectrum)
# usage: python ex04_inspect_events.py path/to/ni<obsid>_0mpu7_cl.evt     or     --demo
# %%
import sys, tempfile, numpy as np
from _common import plt, savefig
from nicerkit import archive, fold, bursts

if __name__ == "__main__":
    if "--demo" in sys.argv:
        t = fold.simulate_events(1500.0, 29.6, src_rate=60.0, bkg_rate=15.0, seed=1, t_start=3.0e8)
        pi = np.clip(np.random.default_rng(1).gamma(3.0, 40.0, len(t)).astype(int), 10, 1200)
        path = archive.make_fake_nicer_evt(tempfile.mkdtemp() + "/fake_cl.evt", t, pi)
    else:
        path = sys.argv[1]
    d = archive.read_events(path)
    print({k: v for k, v in d["header"].items() if v is not None})
    t, pi = d["t"], d["pi"]
    print(f"{len(t)} events; GTIs: {None if d['gti'] is None else len(d['gti'])}; "
          f"exposure from GTIs: {None if d['gti'] is None else (d['gti'][:,1]-d['gti'][:,0]).sum():.0f} s")
    tc, rate, _ = bursts.bin_events(t, dt=1.0)
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.6))
    ax[0].step(tc - t.min(), rate, lw=0.6); ax[0].set(xlabel="t [s]", ylabel="counts/s", title="light curve (1 s)")
    ax[1].hist(pi, bins=np.arange(0, 1200, 5), histtype="step"); ax[1].set(xlabel="PI (10 eV)", yscale="log", title="raw PI spectrum")
    savefig(fig, "ex04_lc_spec%s.png" % ("_demo" if "--demo" in sys.argv else ""))
