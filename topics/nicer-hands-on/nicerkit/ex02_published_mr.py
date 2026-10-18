# %% [markdown]
# # Example 02: published NICER mass-radius posteriors
# `--demo` uses SYNTHETIC Gaussians matching the headline numbers of the papers (NOT the real
# posteriors, which are banana-shaped). With real files: edit sources.json and run without --demo.
# %%
import sys, json, numpy as np
from _common import plt, savefig
from nicerkit import mr, eos as E, tov as T

DEMO_SUMMARY = {   # name: (M, sigma_M, R, sigma_R)  -- headline medians / symmetrised 68% (see Module 02)
    "J0030 (Kini+26, PDT-U)": (1.43, 0.185, 12.68, 1.18),
    "J0740 (Salmi+24)":       (2.073, 0.069, 12.49, 1.08),
    "J0614 (Mauviard+25)":    (1.44, 0.065, 10.29, 0.94),
}

def load_sources(demo):
    out = {}
    if demo:
        for k, (M0, sM, R0, sR) in DEMO_SUMMARY.items():
            out[k] = mr.gaussian_mr(M0, R0, sM, sR, n=30000, seed=len(k))
        return out
    for s in json.load(open("sources.json")):
        d = mr.load_samples(s["path"], columns=s["columns"], skiprows=s.get("skiprows", 0))
        mr.sanity_check(d["M"], d["R"], s["name"])
        out[s["name"]] = (d["M"], d["R"]) if d["w"] is None else mr.resample_equal_weight(d["M"], d["R"], d["w"])
    return out

if __name__ == "__main__":
    demo = "--demo" in sys.argv
    src = load_sources(demo)
    fig, ax = plt.subplots(figsize=(6.5, 5))
    for (name, (M, R)), col in zip(src.items(), ["C0", "C1", "C2", "C3", "C4"]):
        g = mr.GridDensity(M, R)
        l68, l95 = g.credible_levels((0.68, 0.95))
        ax.contour(g.Rg, g.Mg, g.Z, levels=[l95, l68], colors=col, linestyles=["--", "-"])
        ax.plot([], [], color=col, label=name)
        med, lo, hi = mr.summarize(R)
        print(f"{name:28s} R = {med:5.2f} -{lo:.2f} +{hi:.2f} km   M = %.2f" % np.median(M))
    sly = E.sly(); Pc, M, R = T.mr_curve_pp(sly, n=100)
    ax.plot(R, M, "k:", label="SLy (PP)")
    ax.set(xlabel="R [km]", ylabel="M [Msun]", xlim=(8, 17), ylim=(0.9, 2.5),
           title="NICER M-R" + (" (SYNTHETIC stand-ins)" if demo else ""))
    ax.legend(fontsize=8); savefig(fig, "ex02_mr_plane%s.png" % ("_demo" if demo else ""))
