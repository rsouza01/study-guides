# %% [markdown]
# # Example 09: TOV, EOS families, and the interior of a 1.4 Msun star
# %%
import numpy as np
from _common import plt, savefig
from nicerkit import eos as E, tov as T

if __name__ == "__main__":
    fams = {"soft (log p1=34.1)": [34.10, 3.0, 3.0, 3.0], "SLy": list(E.SLY_PARAMS.values()),
            "stiff (34.7)": [34.70, 3.0, 2.8, 2.8]}
    fig, ax = plt.subplots(1, 3, figsize=(15, 4))
    for name, th in fams.items():
        eos = E.PiecewisePolytrope(*th); Pc, M, R = T.mr_curve_pp(eos, n=80)
        ax[0].plot(R, M, label=name)
        s = T.solve_star(eos, np.interp(1.4, M, Pc))
        ax[1].plot(s["r_km"], s["rho"] / 2.66e14, label=f"{name}: R={s['R']:.2f}")
        print(f"{name:20s} Mmax={M.max():.2f}  R1.4={s['R']:.2f} km  Lambda1.4={s['Lambda']:.0f}  I1.4={s['I']/1e45:.2f}e45  "
              f"rho_c/rho_sat={s['rho'][0]/2.66e14:.2f}")
        ax[2].loglog(eos.rho_of_P(np.logspace(25, 35.5, 200)) / 2.66e14, np.logspace(25, 35.5, 200), label=name)
    ax[0].set(xlabel="R [km]", ylabel="M [Msun]", xlim=(8, 15)); ax[0].legend(fontsize=8)
    ax[1].set(xlabel="r [km]", ylabel="rho / rho_sat", title="1.4 Msun density profile"); ax[1].legend(fontsize=7)
    ax[2].set(xlabel="rho / rho_sat", ylabel="P [dyn/cm2]", title="the EOS itself")
    savefig(fig, "ex09_tov_eos.png")
