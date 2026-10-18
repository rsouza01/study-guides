# %% [markdown]
# # Example 11: EOS inference from REAL NICER posteriors (edit sources.json; see Module 10)
# usage: python ex11_real_eos_inference.py sources.json 2000    (hours on one core; use all cores)
# %%
import os, sys, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from multiprocessing import Pool
import emcee
from nicerkit import eos as E, mr, infer

def build_sources(cfg):
    out = []
    for s in json.load(open(cfg)):
        d = mr.load_samples(s["path"], columns=s["columns"], skiprows=s.get("skiprows", 0))
        mr.sanity_check(d["M"], d["R"], s["name"])
        M, R = (d["M"], d["R"]) if d["w"] is None else mr.resample_equal_weight(d["M"], d["R"], d["w"])
        out.append(infer.Source(s["name"], mr.GridDensity(M, R), weight=s.get("weight", 1.0)))
    return out

if __name__ == "__main__":
    SOURCES = build_sources(sys.argv[1]); ns = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    th0 = np.array(list(E.SLY_PARAMS.values())); nw = 32; rng = np.random.default_rng(0)
    p0 = []
    while len(p0) < nw:
        t = th0 + np.array([.05, .1, .1, .1]) * rng.normal(size=4)
        if np.isfinite(infer.log_posterior(t, SOURCES)): p0.append(t)
    p0 = np.array(p0)
    with Pool(int(os.environ.get('NPROC', os.cpu_count() or 1))) as pool:
        sam = emcee.EnsembleSampler(nw, 4, infer.log_posterior, args=(SOURCES,), pool=pool)
        sam.run_mcmc(p0, ns, progress=True)
    chain = sam.get_chain(discard=ns // 3, flat=True); np.save("eos_chain.npy", chain)
    try: print("autocorr time:", sam.get_autocorr_time(tol=0))
    except Exception as e: print(e)
    der = [d for d in (infer.derived(t) for t in chain[::max(1, len(chain)//500)]) if d]
    for k in ("R14", "Mmax", "R_at_Mmax", "rho_c_max"):
        print(k, mr.summarize(np.array([d[k] for d in der])))
