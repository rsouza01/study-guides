# %% [markdown]
# # Example 10: EOS injection-recovery
# Build fake NICER-like (M, R) posteriors from a KNOWN EOS, infer the EOS back, and check
# the recovered R_1.4, M_max and structure.  This is the test every real analysis should
# pass before you trust it on real data.
# %%
import sys, os, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from multiprocessing import Pool
from nicerkit import eos as E, tov as T, mr, infer

TRUE = E.PiecewisePolytrope(**E.SLY_PARAMS)
Pc, Mc, Rc = T.mr_curve_pp(TRUE, n=140)
R14_true = float(np.interp(1.4, Mc, Rc))
print(f"truth: R1.4 = {R14_true:.2f} km, Mmax = {Mc.max():.2f} Msun")

# three fake sources roughly like J0030 / J0437 / J0740 precision (see Module 10)
SPECS = [(1.4, 0.12, 0.9), (1.4, 0.05, 1.1), (2.07, 0.07, 1.0)]
sources = []
for k, (M0, sM, sR) in enumerate(SPECS):
    R0 = float(np.interp(M0, Mc, Rc))
    M, R = mr.gaussian_mr(M0, R0, sM, sR, n=30000, seed=k)
    sources.append(infer.Source(f"fake{k}", mr.GridDensity(M, R)))

if __name__ == "__main__":
    nw, ns = 24, int(sys.argv[1]) if len(sys.argv) > 1 else 600
    import emcee
    theta0 = np.array(list(E.SLY_PARAMS.values()))
    rng = np.random.default_rng(3)
    p0 = []
    while len(p0) < nw:                       # every walker must start where the posterior is finite
        t = theta0 + np.array([0.05, 0.1, 0.1, 0.1]) * rng.normal(size=4)
        if np.isfinite(infer.log_posterior(t, sources)):
            p0.append(t)
    p0 = np.array(p0)
    with Pool(int(os.environ.get('NPROC', os.cpu_count() or 1))) as pool:
        sam = emcee.EnsembleSampler(nw, 4, infer.log_posterior, args=(sources,), pool=pool)
        sam.run_mcmc(p0, ns, progress=True)
    chain = sam.get_chain(discard=ns // 3, flat=True)
    np.save("injection_chain.npy", chain)
    der = [infer.derived(t) for t in chain[:: max(1, len(chain) // 400)]]
    der = [d for d in der if d]
    for key in ("R14", "Mmax", "R_at_Mmax"):
        med, lo, hi = mr.summarize(np.array([d[key] for d in der]))
        print(f"{key:10s} = {med:6.2f} -{lo:.2f} +{hi:.2f}")
