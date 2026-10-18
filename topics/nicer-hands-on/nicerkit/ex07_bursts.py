# %% [markdown]
# # Example 07: find type I bursts in an LMXB light curve (--demo or an event file)
# %%
import sys, numpy as np
from _common import plt, savefig
from nicerkit import archive, bursts

if __name__ == "__main__":
    if "--demo" in sys.argv:
        tc, rate = bursts.simulate_lightcurve(seed=5)
    else:
        t = archive.read_events(sys.argv[1])["t"]; tc, rate, _ = bursts.bin_events(t, dt=1.0)
    found = bursts.find_bursts(tc, rate)
    fig, ax = plt.subplots(figsize=(9, 3.4)); ax.step(tc, rate, lw=0.6)
    for b in found:
        tau, err = bursts.fit_decay(tc, rate, b["t_peak"], b["baseline"])
        print(f"burst at t={b['t_peak']:.0f}s: peak {b['peak_rate']:.0f} c/s over baseline {b['baseline']:.0f};  e-fold decay tau = {tau:.1f} +- {err:.1f} s")
        ax.axvline(b["t_peak"], color="r", alpha=0.3)
    ax.set(xlabel="t [s]", ylabel="counts/s"); savefig(fig, "ex07_bursts%s.png" % ("_demo" if "--demo" in sys.argv else ""))
