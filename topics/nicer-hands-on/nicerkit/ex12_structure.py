# %% [markdown]
# # Example 12: from an EOS posterior to the interior of a star
# usage: python ex12_structure.py chain.npy   (e.g. injection_chain.npy from example 10)
# %%
import sys, numpy as np
from _common import plt, savefig
from nicerkit import eos as E, tov as T, mr, infer

if __name__ == "__main__":
    chain = np.load(sys.argv[1]); rng = np.random.default_rng(0)
    pick = chain[rng.choice(len(chain), size=min(150, len(chain)), replace=False)]
    fig, ax = plt.subplots(1, 3, figsize=(15, 4)); stats = {"M": [], "R": [], "rhoc": [], "crust": [], "I": [], "Lam": []}
    for mass, col in ((1.4, "C0"), (2.0, "C3")):
        res = []
        for th in pick:
            eos = infer.make_eos(th)
            if eos is None: continue
            Pc, M, R = T.mr_curve_pp(eos, n=60)
            if M.max() < mass + 0.01: continue
            s = T.solve_star(eos, np.interp(mass, M, Pc))
            Pcc = eos.P_of_rho(eos.rho0); rc = np.interp(-Pcc, -s["P"], s["r_km"])
            res.append((s["R"], s["rho"][0] / 2.66e14, s["R"] - rc, s["I"] / 1e45, s["Lambda"]))
            ax[0].plot(s["r_km"], s["rho"] / 2.66e14, color=col, alpha=0.06)
            ax[1].plot(s["r_km"], s["m_Msun"], color=col, alpha=0.06)
        res = np.array(res)
        print(f"M={mass}: " + ", ".join(f"{n}={np.median(res[:,i]):.2f} (+{np.percentile(res[:,i],84)-np.median(res[:,i]):.2f}/-{np.median(res[:,i])-np.percentile(res[:,i],16):.2f})"
              for i, n in enumerate(["R[km]", "rho_c/rho_sat", "crust[km]", "I[1e45]", "Lambda"])))
        ax[2].hist(res[:, 0], bins=20, alpha=0.5, color=col, label=f"R({mass})")
    ax[0].set(xlabel="r [km]", ylabel="rho/rho_sat", yscale="log"); ax[1].set(xlabel="r [km]", ylabel="m(r) [Msun]")
    ax[2].legend(); ax[2].set(xlabel="R [km]"); savefig(fig, "ex12_structure.png")
