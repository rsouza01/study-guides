# %% [markdown]
# # Example 08: how compactness shapes a pulse profile (toy model), and how a wrong spot model biases it
# %%
import numpy as np
from _common import plt, savefig
from nicerkit import ppm

if __name__ == "__main__":
    ph = np.linspace(0, 1, 300, endpoint=False)
    fig, ax = plt.subplots(1, 3, figsize=(14, 3.8))
    for u in (0.1, 0.25, 0.35, 0.5):
        f = ppm.two_spot_profile(ph, u, np.radians(55), np.radians(55), nu=205.0)
        ax[0].plot(ph, f / f.mean(), label=f"u={u}  PF={ppm.pulsed_fraction_amp(f):.2f}")
    ax[0].legend(fontsize=8); ax[0].set(xlabel="phase", ylabel="flux / mean", title="more bending -> smaller amplitude")
    nu, nb = 205.0, 32; phb = (np.arange(nb) + 0.5) / nb
    truth = np.array([0.35, np.cos(np.radians(55)), np.radians(55), np.log10(2e5), np.log10(2e5)])
    ug = np.linspace(0.15, 0.55, 9)
    for N, ls in ((1.0, "-"), (10.0, "--")):
        t = truth.copy(); t[3:] += np.log10(N)
        c = np.random.default_rng(1).poisson(ppm.model_counts(t, phb, nu)).astype(float)
        d2 = ppm.profile_likelihood_u(c, nu, ug, n_starts=12)
        ax[1].semilogy(ug, d2 + 1e-1, ls, label=f"{c.sum():.1e} counts")
    ax[1].axhline(1, color="gray"); ax[1].axvline(0.35, color="r", alpha=.3); ax[1].legend()
    ax[1].set(xlabel="fixed u = 2GM/Rc^2", ylabel="-2 dlnL (+0.1)", title="what the profile says about u")
    rng = np.random.default_rng(2); zetas = [0.05, 0.3, 0.6, 0.9]; fits = []
    for z in zetas:
        pr = ppm.two_cap_profile(phb, 0.35, np.radians(55), np.radians(55), z, nu)
        c = rng.poisson(5e5 * pr / pr.sum() + 5e5 / nb).astype(float)
        fits.append(ppm.fit_profile(c, nu, n_starts=30)[1][0])
    ax[2].plot(zetas, fits, "o-"); ax[2].axhline(0.35, color="r", alpha=.4)
    ax[2].set(xlabel="true spot radius [rad]", ylabel="best-fit u (point-spot model)", title="model misspecification bias")
    savefig(fig, "ex08_toy_ppm.png"); print("fitted u vs spot radius:", dict(zip(zetas, np.round(fits, 3))))
