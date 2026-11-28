# Module MC-25: Scaling the engine, many cores and a GPU

[← MC-24](MC-24-capstone-the-functioning-star.md) · [README](../README.md)

**Source:** not in Forgan, whose §8 only counts the cost. This module ports the engine of MC-19 (loop of MC-06, tally of MC-14, jump of MC-18) to every CPU core and to a CUDA GPU.

**Optional.** Do it after the capstone. Nothing earlier depends on it, and it adds one file, `starmc/parallel.py`.

**Hardware.** A multicore CPU, and for Problem 6 an NVIDIA GPU. Without a GPU, Problems 1 to 5 and 7 still run, and Problem 6 runs in numba's CUDA simulator, which is slow but checks the logic.

---

## Session A: read

**Reading**

- numba, CPU: the page "Automatic parallelization with @jit", sections "Explicit Parallel Loops" and "Scheduling"; and "Threading Layers", section "Setting the Number of Threads" (`numba.set_num_threads`).
- numba, GPU: the CUDA part of the numba documentation. Read kernels and thread indexing (`cuda.grid`), device functions, atomic operations, and the page "Debugging CUDA Python with the CUDA Simulator".
- Install: the CUDA target of numba now lives in NVIDIA's `numba-cuda` package, and its documentation gives `pip install numba-cuda[cu12]` (or `[cu13]`). Check with `python -c "from numba import cuda; print(cuda.is_available()); cuda.detect()"`.
- Random numbers: Salmon, Moraes, Dror & Shaw (2011), "Parallel random numbers: as easy as 1, 2, 3", the description of Philox. The Random123 repository holds the known-answer vectors used in Problem 1.
- GPU execution: the CUDA C++ Programming Guide, the subsection on the SIMT architecture and the section on atomic functions. Kirk & Hwu, *Programming Massively Parallel Processors*, the chapters on control divergence and on atomics.

**What is easy here, and what is not**

- Packets are independent. Each one reads the star (`r_edges`, $\kappa\rho$, convective flags, the MRW table), which never changes, and writes its own outputs.
- The only shared write is the tally `path_shell`.
- Three questions decide the design:
  - Where do the random numbers come from, so that results do not depend on the thread count?
  - How is the tally summed without races and without losing precision?
  - What does the shape of the work (packets needing very different numbers of steps) cost on a GPU?

**1. Random numbers: a counter-based generator**

- Why `np.random.seed` is not enough:
  - On CPU, numba keeps one generator state per thread. Which packets a thread simulates depends on the scheduling, so the same seed gives different results on different thread counts.
  - On GPU, `np.random` does not exist inside a kernel.
- A **counter-based** generator is a pure function $u = F(\text{key},\text{counter})$ with no state.
  - Draw $j$ of packet $k$ is $u = F(\text{seed},(j,k))$.
  - Any backend, any thread count, any order of execution gives the same numbers. Packet $k$ is then the same random walk everywhere.
  - Different packets use different counters, so their streams cannot overlap by construction.
- Why overlap matters for sequential generators (an estimate, to see once):
  - Give $n$ packets streams of length $L$, started at independent uniform points on a cycle of length $P$.
  - Two given streams overlap if their starts are within $L$ of each other: probability about $2L/P$.
  - There are $n^2/2$ pairs, so the expected number of overlapping pairs is about $n^2L/P$.
  - With $P=2^{64}\approx1.8\times10^{19}$, $n=10^7$ and $L=10^4$ this is $10^{18}/1.8\times10^{19}\approx0.05$. A GPU run with $10^8$ packets would be in trouble. Counter-based generators remove the question.
- **Philox4x32-10** (Salmon et al. 2011). Input: a counter $(c_0,c_1,c_2,c_3)$ and a key $(k_0,k_1)$, all 32-bit unsigned. Ten rounds, each:

```text
p0 = M0 * c0                  (64-bit product)
p1 = M1 * c2
new c0 = hi(p1) xor c1 xor k0
new c1 = lo(p1)
new c2 = hi(p0) xor c3 xor k1
new c3 = lo(p0)
k0 = (k0 + W0) mod 2^32
k1 = (k1 + W1) mod 2^32
```

- `hi` and `lo` are the upper and lower 32 bits of the 64-bit product. The constants are $M_0=$ `0xD2511F53`, $M_1=$ `0xCD9E8D57`, $W_0=$ `0x9E3779B9` ($=\lfloor2^{32}/\varphi\rfloor$, golden ratio) and $W_1=$ `0xBB67AE85` ($=\lfloor(\sqrt3-1)\,2^{32}\rfloor$). The output is the four words after round 10.
- In Python/numba keep every word as `np.uint64` holding a 32-bit value, mask with `0xFFFFFFFF`, and never mix with signed integers. A product of two 32-bit numbers overflows `int64`.
- **From words to a uniform.** Packet $k$, draw $j$, seed $s$:
  - key $=(s \bmod 2^{32},\ \lfloor s/2^{32}\rfloor)$.
  - counter $=(b \bmod 2^{32},\ \lfloor b/2^{32}\rfloor,\ k \bmod 2^{32},\ \lfloor k/2^{32}\rfloor)$ with $b=\lfloor j/2\rfloor$.
  - One call gives 128 bits, enough for two draws: use words $(w_0,w_1)$ if $j$ is even, $(w_2,w_3)$ if odd.
  - Take $x=(w_a\ll20)\,|\,(w_b\gg12)$, a 52-bit integer, and $u=(x+\tfrac12)\,2^{-52}$.
- **Why 52 bits and the $+\tfrac12$.** A double has spacing $\tfrac12$ on $[2^{51},2^{52})$, so $x+\tfrac12$ is exact for every $x\le 2^{52}-1$, and $u\in[2^{-53},\,1-2^{-53}]$ never touches 0 or 1. Then $\tau=-\ln(1-u)$ is always finite. With 53 bits, $x+\tfrac12$ is not representable near $2^{53}$ and can round to $2^{53}$, which gives $u=1$ and $\ln 0$. The chance is $2^{-53}$ per draw, so the bug would appear once in a very long run, which is the worst kind.

**2. The tally**

- One shared array written by millions of threads is a race. Two cures:
  - **Rows.** Split the packets into chunks of 128. Each chunk owns one row of a `(nchunk, M)` array. Sum the rows at the end in a fixed order.
  - **Registers first.** A packet adds its path to a local variable and writes to the row only when it leaves the shell (and when it ends). The number of writes falls from one per step to one per boundary crossing.
- On CPU, a chunk is run by one thread, so row writes are plain `+=`. The final sum over rows is in a fixed order, so the result is **bitwise independent of the number of threads**.
- On GPU, a chunk is a thread block, a row is a block's row, and the many threads of a block write it with `cuda.atomic.add`. The order of atomic additions is not fixed, so the tally agrees with the CPU only up to rounding, about $10^{-16}$ relative per addition. FP64 atomic add is native on compute capability 6.0 and above (Pascal, 2016, and newer). On older cards check the numba atomics page.
- Per-block shared-memory rows would cut the traffic further. That is a stretch (Problem 8).

**3. The shape of the work (divergence)**

- A GPU runs 32 threads (a warp) in lockstep. When the packets in a warp need different numbers of steps, finished lanes idle until the slowest one is done.
- Define the **lockstep efficiency** $\eta_W=\mathrm E[w]\,/\,\mathrm E[\max_{i\le W}w_i]$ for work $w$ per packet and warp size $W$.
- Derivation for exponentially distributed work with mean $m$ (to see once):
  - Let $T_{(1)}\le\dots\le T_{(W)}$ be the sorted values of $W$ independent draws.
  - The smallest of $W$ exponentials with mean $m$ is exponential with mean $m/W$. So $\mathrm E\,T_{(1)}=m/W$.
  - By memorylessness, at that moment the other $W-1$ lanes have remaining work again exponential with mean $m$. The wait for the next one to finish is exponential with mean $m/(W-1)$, and so on.
  - Summing, $\mathrm E\,T_{(W)}=m\,(1/W+1/(W-1)+\dots+1)=m\,H_W$, with $H_W$ the harmonic number. Therefore $\eta_W=1/H_W$.
  - For $W=32$, $H_{32}=4.058$ and $\eta=0.246$: about a quarter of the lanes do useful work.
- The packets of this guide have a narrower spread than an exponential (the coefficient of variation of the step count is 0.6 to 0.8, not 1), so the measured $\eta$ is a little higher, 0.30 to 0.36 (checkpoints). Reducing the steps per packet by MRW (MC-18) lowers the work but **does not** improve $\eta$.
- So a simple kernel (one thread, one packet) leaves about two thirds of the lanes idle. This is the price of the simple design, and it is a measurement, not an opinion. Problem 5 measures it, and Problem 8 describes the cure.

**4. Precision**

- The engine is FP64 everywhere, and the tally must stay FP64. A float32 running sum loses every increment smaller than $S\cdot2^{-24}$, with $S$ the current sum, so it stalls. Problem 4 shows it on your machine.
- Consumer GPUs run FP64 at a small fraction of the FP32 rate (from memory, 1/32 to 1/64 on recent generations; read your card's specification). This caps the gain. A mid-range gaming card will win over one CPU core by a large factor, not by thousands.
- A float32 transport kernel with float64 tallies is possible. It is **not** tested here, and the geometry (`r_out² − r²` near a boundary) is where it would break first.

**5. What hardware does not change**

- The direct run of MC-16 needs about $10^9$ years of packet time per packet. A speed-up of $10^3$ leaves $10^6$ years. The opacity scaling (MC-17) and the jump (MC-18) stay necessary.
- The error still falls as $1/\sqrt N$ (MC-08). Hardware buys more packets, not a different exponent.
- What hardware does buy: the scaled star at $N\sim10^5$ to $10^6$ packets, the parameter sweeps of MC-21 and MC-23, and the atmosphere runs of MC-20 in seconds.

---

## Session B: do

**Problem 1: the counter-based generator**

- Implement `philox4x32(c0, c1, c2, c3, k0, k1)` as described above, with `numba.njit`, taking and returning `np.uint64` words that hold 32-bit values.
- Check it against these three known-answer vectors (counter, key, output; hexadecimal):
  - counter `0 0 0 0`, key `0 0`: `6627e8d5 e169c58d bc57ac4c 9b00dbd8`.
  - counter `ffffffff ffffffff ffffffff ffffffff`, key `ffffffff ffffffff`: `408f276d 41c83b0e a20bc7c6 6d5451fd`.
  - counter `243f6a88 85a308d3 13198a2e 03707344`, key `a4093822 299f31d0`: `d16cfe09 94fdcceb 5001e420 24126ea1`.
  - These come from the Random123 test vectors as I remember them, and my implementation reproduces all three. Compare them with the file in the repository before you rely on them.
- Implement `u01(seed, k, j)` as described. It must return the same number for the same arguments, a number strictly inside $(0,1)$, and different numbers for different `seed`, `k` or `j`.
- Using $10^5$ draws, check the mean ($0.5$), the variance ($1/12$), a 20-bin chi-square against uniformity, and the lag-1 correlation along $j$ (fixed $k$) and along $k$ (fixed $j$). Say what a correlation of $0.03$ would mean for $10^5$ draws.

**Problem 2: the engine with the new generator, serial**

- Create `run_engine_par` with `backend="cpu-serial"`. Copy the packet loop of MC-19 and change four things:
  - Each packet $k$ starts its own draw counter `ctr = 0`. Every `np.random.random()` becomes `u01(seed, k, ctr)` followed by `ctr += 1`.
  - Replace `np.log`, `np.sqrt`, `np.exp` by `math.log`, `math.sqrt`, `math.exp`. `np.*` ufuncs on scalars do not exist in CUDA kernels.
  - Replace `np.interp` in the MRW jump by your own binary-search interpolation (`np.interp` does not exist in a kernel either). Clamp outside the table as `np.interp` does.
  - The starting shell and the first direction are now found inside the per-packet function, from `r0[k]`.
- Reuse the MRW table of your MC-19 engine (log-spaced $y$, monotone $P$), passed as `logy` and `P` arrays.
- Check against the numbers of MC-19 Problems 2 and 3 (single shell, $\tau=100$): the mean path must be about 51 (plain) and agree within 3 % with MRW. You will not reproduce the MC-19 numbers digit for digit, because the random numbers differ.
- Time it against your MC-19 engine at equal $N$ (20000 packets, $\tau=100$, plain). Counter-based generation should cost you only a few percent.

**Problem 3: all CPU cores, with reproducible results**

- Add `backend="cpu"`:
  - Cut the packets into chunks of `chunk=128` packets. The array `tally` has one row per chunk.
  - `prange` over chunks. A chunk loops serially over its packets and adds to its own row.
  - After the run, `path_shell = tally.sum(axis=0)`.
- The packet outputs (`path`, `nstep`, `njump`, `mu_exit`, `done`, `nflush`) are written to per-packet arrays.
- Verify that `cpu-serial`, `cpu`, and `cpu` with `numba.set_num_threads(1)` return **identical** arrays, bit for bit. Then change `chunk` to 64: the per-packet arrays must stay identical, and `path_shell` must agree to rounding.
- Fill the table below for your machine (20000 packets, $\tau=100$, plain):

| Backend | Time | Steps per second | Speed-up |
|---|---|---|---|
| `cpu-serial` | | | 1 |
| `cpu`, 1 thread | | | |
| `cpu`, all threads | | | |

- Say what limits the speed-up on your machine (physical cores against hyper-threads, memory, the turbo clock).

**Problem 4: the tally, in registers, and why FP64**

- In the packet loop, add the path to a local `acc` and write `tally[row, shell] += acc` only when the packet crosses a boundary (an escape through the outer edge counts as a crossing), and once more if it is stopped by `max_steps`. Count the writes per packet in `nflush`.
- Check:
  - One uniform shell, plain steps: every packet has `nflush == 1`.
  - Ten shells of equal thickness, total $\tau=100$: `nflush` is far below `nstep` (a factor above 10).
  - `path_shell.sum()` equals `path.sum()` to $10^{-10}$ relative.
- Precision experiment (plain numba loops, no transport). Draw $n=2\times10^8$ increments $x=-0.01\ln(1-\zeta)$, mean $0.01$, the size of a step in a $\tau=100$ unit shell. Sum them in three ways:
  - A `float64` accumulator.
  - A `float32` accumulator, plain `s += x32`.
  - A `float32` accumulator with Kahan summation: keep a compensation `c`; for each `x`, `y = x - c`, `t = s + y`, `c = (t - s) - y`, `s = t`.
- The exact sum is $2\times10^6$ with a statistical error of about 140. Report the three results and explain the failure of the plain float32 sum with the rule "an increment is lost when it is below half a unit in the last place of the running sum".

**Problem 5: how much of a GPU would sit idle**

- Implement `warp_efficiency(work, warp=32)`: split `work` into consecutive groups of `warp` values, return the mean of `work` divided by the mean of the group maxima.
- Check the formula of Session A: for $320000$ draws from an exponential distribution, the efficiency times $H_{32}$ is $1$ within 3 %. For the same draws sorted, the efficiency is above $0.95$.
- Compute the efficiency of `nstep + njump` for three runs: the plain slab, the MRW slab (both $\tau=100$), and the scaled star of MC-19 Problem 4 with 12000 packets. Also report the coefficient of variation of the work.
- For the star, sort the packets by starting radius before computing the efficiency. Does it help? Explain with the mean steps per packet in each decile of the starting radius.
- Say what the result means for a simple one-thread-per-packet kernel, and why sorting by something known in advance cannot cure it here.

**Problem 6: the CUDA kernel**

- The same physics must be compiled twice, for the CPU and as CUDA device code. The compiled functions of one target cannot be called from the other. Write the packet function inside a factory, `_build(jit, add)`, which takes the decorator (`numba.njit` or `numba.cuda.jit(device=True)`) and the tally-add function, and returns the compiled `philox`, `draw` and `walk` functions. Inside the factory use only `math`, no `np.random`, no `np.interp`.
- The tally-add functions:
  - CPU: `tally[row, i] += x`.
  - GPU: `cuda.atomic.add(tally, (row, i), x)`.
- The kernel, one thread per packet:
  - `k = cuda.grid(1)`, and `if k < n:` call the packet function with `row = cuda.blockIdx.x`.
  - Launch with `kernel[nblocks, chunk](...)` where `chunk` is the block size (a multiple of 32, 128 is fine). Rows of the tally then match the CPU chunks.
  - Copy the arrays with `cuda.to_device`, call `cuda.synchronize()`, copy the results back with `copy_to_host()`.
- Do not try caching (`cache=True`) on the factory-built functions.
- Validate on the simulator first, with a few hundred packets (`NUMBA_ENABLE_CUDASIM=1 python your_script.py`; the simulator runs the kernel in Python, so keep $N$ small). Then on the real GPU:
  - Compare with `cpu-serial` packet by packet. `nstep`, `njump`, `nflush` should be equal for essentially all packets, and `path` equal to about $10^{-9}$ relative. This works because the random numbers are the same function of $(k,j)$.
  - A rare packet may differ if a comparison such as `tau_rem >= tcell` flips by a last-bit difference in `log` or `sqrt` between CPU and GPU. Count them. A large number would mean a bug.
- Timing: run $10^5$ packets of the scaled star on `cuda`, on `cpu`, and on `cpu-serial`, excluding the first call (compile time). Report steps per second, and the speed-up of the GPU over one core and over all cores.
- Compare the speed-up with what Problem 5 predicts: the GPU speed-up divided by the lockstep efficiency is the speed-up you would get if all lanes were busy.

**Problem 7: the capstone at larger $N$**

- Redo MC-19 Problem 4 (scaled star with a convective core, $\tau'=300$) with `run_engine_par`, once with 3000 packets and once with 12000, for six seeds each. Report the mean and the standard deviation across seeds of $T_{\rm MC}/T_{\rm RE}$ at $0.2$, $0.3$, $0.4$, $0.5R$.
- The standard deviation should fall by about a factor $2$ when $N$ grows by $4$ (MC-08). The mean at $0.5R$ should **not** go to 1: the boundary-layer error of MC-17 is not statistical, and larger $N$ only reveals it.
- Check that the path length in the convective shells is exactly zero.

**Problem 8 (stretch, no acceptance test): lane refill**

- The simple kernel leaves about two thirds of the lanes idle (Problem 5). The standard cure is to refill lanes as they finish. Design one of:
  - **Persistent threads.** Make one `while` loop in which each thread does a **single step** of its current packet, and when the packet ends, fetches the next packet index with `cuda.atomic.add` on a global counter. The per-packet state (position, direction, shell, `tau_rem`, `need`, draw counter, accumulators) lives in registers.
  - **Wavefront.** Run the kernel for a fixed number of steps, save the packet states, compact the unfinished packets on the host or with a scan, and relaunch. See Laine, Karras & Aila (2013).
- The best possible gain is $1/\eta$, about $3\times$ for these packets. The price is more registers and some bookkeeping per step.
- Also try per-block shared-memory tally rows (dynamic shared memory, `cuda.shared.array(0, dtype)` and `sharedmem` in the launch) and measure whether the atomics were a bottleneck at all after Problem 4.
- Not implemented in my reference. Treat the $1/\eta$ bound as the target and measure.

---

## Translation: text → code

| Step | Where it came from | Code |
|---|---|---|
| draw $\tau$ | MC-02 | `tau_rem = -math.log(1.0 - draw(sd, kk, ctr)); ctr += 1` |
| isotropic direction | MC-04 | `mu = 2.0*draw(sd, kk, ctr) - 1.0; ctr += 1` |
| relocation | MC-13 | `mu = math.sqrt(draw(sd, kk, ctr)); ctr += 1` |
| jump time | MC-18 | `y = math.exp(interp(draw(sd, kk, ctr), P, logy))` |
| path in shell | MC-14 | `acc += s` and, at a boundary, `add(tally, row, i, acc)` |
| packet to thread | new | `k = cuda.grid(1)` |
| chunk to block | new | `row = cuda.blockIdx.x` |
| two targets, one source | new | `_build(njit, _add_cpu)` and `_build(cuda.jit(device=True), _add_gpu)` |

---

## Contract

```text
starmc/parallel.py
  philox4x32(c0, c1, c2, c3, k0, k1) -> 4 words
      arguments: np.uint64 holding 32-bit values; returns four 32-bit values
  u01(seed, k, j) -> float, strictly inside (0, 1)
      draw j of packet k under seed; a pure function
  run_engine_par(r0, r_edges, kapparho, convective=None, gamma=0.95, kmin=2.0,
                 use_mrw=True, seed=1, max_steps=10**9,
                 backend="cpu", chunk=128) -> dict
      same inputs and keys as run_engine (MC-19), plus
        nflush (n,) int     tally writes issued by each packet
      backend: "cpu-serial", "cpu" (numba prange), "cuda"
      guarantees:
        - per-packet outputs do not depend on backend, thread count or chunk
          (cuda: up to a last-bit difference in a transcendental function)
        - path_shell = sum of per-chunk rows in a fixed order
          (cuda: equal to rounding, atomics are unordered)
  warp_efficiency(work, warp=32) -> float
      mean(work) / mean of the maxima over consecutive groups of `warp`
```

```python
# acceptance-test
import numpy as np
import numba
from starmc.parallel import philox4x32, u01, run_engine_par, warp_efficiency
from starmc.star import polytrope_star
from starmc.thermal import radiative_equilibrium_T, luminosity_profile
from starmc.opacity import kappa_rosseland
from starmc.emission import sample_radius_from_shells
from starmc.budget import optical_depth_radial
from starmc.scaling import scale_factor, physical_energy_density
from starmc.radeq import energy_density_from_paths
from starmc import consts as C

# 1. Philox known answers and the uniform
U = np.uint64
def kat(c, k):
    return tuple(int(w) for w in philox4x32(*(U(v) for v in c), *(U(v) for v in k)))
assert kat((0, 0, 0, 0), (0, 0)) == (0x6627e8d5, 0xe169c58d, 0xbc57ac4c, 0x9b00dbd8)
assert kat((0xffffffff,) * 4, (0xffffffff,) * 2) == (0x408f276d, 0x41c83b0e, 0xa20bc7c6, 0x6d5451fd)
assert kat((0x243f6a88, 0x85a308d3, 0x13198a2e, 0x03707344), (0xa4093822, 0x299f31d0)) == \
    (0xd16cfe09, 0x94fdcceb, 0x5001e420, 0x24126ea1)
x = np.array([[u01(7, k, j) for j in range(1000)] for k in range(100)])
assert x.min() > 0.0 and x.max() < 1.0
assert abs(x.mean() - 0.5) < 4e-3 and abs(12 * x.var() - 1) < 0.02
counts = np.histogram(x, bins=20, range=(0, 1))[0]
chi2 = ((counts - x.size / 20) ** 2 / (x.size / 20)).sum()
assert chi2 < 45, chi2
assert abs(np.corrcoef(x[:, :-1].ravel(), x[:, 1:].ravel())[0, 1]) < 0.02
col = np.array([u01(7, k, 3) for k in range(20000)])
assert abs(np.corrcoef(col[:-1], col[1:])[0, 1]) < 0.03
assert u01(7, 3, 5) == u01(7, 3, 5)
assert len({u01(7, 3, 5), u01(8, 3, 5), u01(7, 4, 5), u01(7, 3, 6)}) == 4

# 2. one shell: backends agree bit for bit, physics as in MC-19
E1 = np.array([0.0, 1.0])
N = 4000
kw = dict(use_mrw=False, seed=3)
a = run_engine_par(np.zeros(N), E1, np.array([100.0]), backend="cpu-serial", **kw)
b = run_engine_par(np.zeros(N), E1, np.array([100.0]), backend="cpu", **kw)
numba.set_num_threads(1)
c = run_engine_par(np.zeros(N), E1, np.array([100.0]), backend="cpu", **kw)
numba.set_num_threads(numba.config.NUMBA_NUM_THREADS)
for key in a:
    assert np.array_equal(a[key], b[key]) and np.array_equal(a[key], c[key]), key
d = run_engine_par(np.zeros(N), E1, np.array([100.0]), backend="cpu", chunk=64, **kw)
for key in ("path", "nstep", "njump", "mu_exit", "done", "nflush"):
    assert np.array_equal(a[key], d[key]), key
assert np.allclose(a["path_shell"], d["path_shell"], rtol=1e-12)
assert a["done"].all()
assert 49.5 < a["path"].mean() < 53.0, a["path"].mean()
assert 0.69 < np.nanmean(a["mu_exit"]) < 0.73
assert np.all(a["nflush"] == 1)
assert np.isclose(a["path_shell"].sum(), a["path"].sum(), rtol=1e-10)
m = run_engine_par(np.zeros(N), E1, np.array([100.0]), use_mrw=True, seed=4)
assert m["done"].all()
assert abs(m["path"].mean() / a["path"].mean() - 1) < 0.03
assert m["nstep"].mean() < a["nstep"].mean() / 100

# 3. flushes in a layered slab
E10 = np.linspace(0.0, 1.0, 11)
t = run_engine_par(np.zeros(2000), E10, np.full(10, 100.0), use_mrw=False, seed=3)
assert t["nflush"].mean() < t["nstep"].mean() / 10
assert np.isclose(t["path_shell"].sum(), t["path"].sum(), rtol=1e-10)

# 4. lockstep efficiency
rng = np.random.default_rng(1)
H = sum(1.0 / k for k in range(1, 33))
assert abs(warp_efficiency(rng.exponential(100.0, 320_000)) * H - 1) < 0.03
assert warp_efficiency(np.sort(rng.exponential(100.0, 320_000))) > 0.95
assert 0.30 < warp_efficiency(a["nstep"] + a["njump"]) < 0.42

# 5. the scaled star with a convective core, at four times the MC-19 packet number
s = polytrope_star(n_shells=100)
T, L, conv, nab = radiative_equilibrium_T(s, convect=True)
kr = kappa_rosseland(s.rho, T, s.X, s.Z) * s.rho
S = scale_factor(optical_depth_radial(s, kr), 300.0)
Lc, dL = luminosity_profile(s, T)
Np = 12000
r0, _ = sample_radius_from_shells(np.random.default_rng(8), s.r_edges, dL, Np)
o = run_engine_par(r0, s.r_edges, kr / S, convective=conv, use_mrw=False, seed=5)
assert o["done"].all()
assert np.all(o["path_shell"][conv] == 0.0)
usc = energy_density_from_paths(C.Lsun, Np, o["path_shell"], s.vol)
uph = physical_energy_density(usc, S, C.a_rad * T[-1] ** 4)
Tm = (np.maximum(uph, 0.0) / C.a_rad) ** 0.25
for f in (0.2, 0.3, 0.4, 0.5):
    i = np.searchsorted(s.r_edges[1:] / C.Rsun, f)
    assert abs(Tm[i] / T[i] - 1) < 0.025, (f, Tm[i] / T[i])

# 6. GPU, if there is one (the numba simulator counts, with fewer packets)
from numba import cuda
from numba.core import config
if cuda.is_available():
    sim = config.ENABLE_CUDASIM
    Ng = 256 if sim else 20000
    kg = dict(use_mrw=False, seed=11, chunk=64)
    g = run_engine_par(np.zeros(Ng), E1, np.array([20.0]), backend="cuda", **kg)
    h = run_engine_par(np.zeros(Ng), E1, np.array([20.0]), backend="cpu-serial", **kg)
    same = (g["nstep"] == h["nstep"]) & (g["njump"] == h["njump"])
    assert g["done"].all() and same.mean() > 0.999, same.mean()
    assert np.max(np.abs(g["path"][same] / h["path"][same] - 1)) < 1e-6
    assert np.array_equal(g["nflush"][same], h["nflush"][same])
    assert abs(g["path"].mean() / h["path"].mean() - 1) < 5e-3
    print("cuda: ok (simulator)" if sim else "cuda: ok on " + str(cuda.get_current_device().name))
else:
    print("cuda: no device, GPU part skipped")
print("MC-25 ok")
```

---

## Checkpoints

Measured on my reference code in a 2-core cloud sandbox (numba 0.68.1). Your timings will differ. The GPU rows are empty on purpose: I could not run on a GPU.

| Quantity | Value |
|---|---|
| three Philox known-answer vectors | reproduced exactly |
| $10^5$ draws (100 packets × 1000): mean, $12\times$variance | 0.4982, 1.0004 |
| slab $\tau=100$, plain, 4000 packets: mean path | 51.5 ± 0.5 |
| same: steps per packet / $\langle\mu_{\rm exit}\rangle$ | about 5150 / 0.710 |
| slab $\tau=100$, MRW: mean path, steps, jumps | 50.0 ± 0.5, about 10, about 10.6 |
| `cpu-serial` against `cpu` against 1 thread | bitwise identical |
| 20000 packets, $\tau=100$, plain: 1 thread, 2 threads, serial loop | 4.1 s, 2.2 s, 4.0 s (speed-up 1.84 on 2 cores) |
| same loop with the MC-19 engine (Mersenne twister) | 3.7 s (Philox costs about 9 %) |
| `chunk` from 8 to 5000 | no visible change (2.0 to 2.1 s) |
| `nflush`, one shell / ten shells of $\tau=100$ in total | 1 / 252 against 5324 steps (factor 21) |
| $2\times10^8$ increments: float64 / float32 plain / float32 Kahan | 2000214.86 / 893198 / 2000214.875 (exact 2000000 ± 140) |
| lockstep efficiency, exponential work | $1/H_{32}=0.246$ |
| slab, plain / slab, MRW / star | 0.36 / 0.30 / 0.32 |
| coefficient of variation of the work, same three | 0.62 / 0.78 / 0.71 |
| the same after sorting by work / by starting radius (star) | 0.99 / 0.32 (no gain) |
| scaled star, 12000 packets: time (2 cores) | about 5 s for $2.5\times10^8$ steps |
| scatter across 6 seeds of $T_{\rm MC}/T_{\rm RE}$ at $0.2,0.3,0.4,0.5R$, $N=3000$ | 0.0061, 0.0022, 0.0045, 0.0064 |
| same, $N=12000$ | 0.0024, 0.0013, 0.0020, 0.0029 |
| mean of $T_{\rm MC}/T_{\rm RE}$, $N=12000$ | 1.0018, 0.9999, 1.0030, 1.0096 |
| CUDA kernel in numba's simulator against `cpu-serial` | identical `nstep`, `njump`, `path` (256 packets; $\tau=20$ plain, $\tau=100$ MRW) |
| your GPU: steps per second, speed-up over 1 core / all cores | to fill in |

---

## Limits (what I did and did not verify)

- The kernel was run only in numba's CUDA **simulator**, not on a GPU and not with the `numba-cuda` package. The simulator checks the logic, the indexing and the atomics, but not the real compiler, the memory model, the register pressure or the speed.
- I give no GPU speed-up. Measure it (Problem 6) and compare with the bound set by Problem 5.
- The FP64 rate of consumer GPUs and the native FP64 atomic on compute capability 6.0 are from memory.
- Philox as written here is the standard Philox4x32-10 with the three known-answer vectors above. The mapping from its output to a uniform (52 bits, $+\tfrac12$) is my choice.
- Lane refill (Problem 8) and a float32 transport kernel are not implemented.

---

## Done when

- You can say why the result no longer depends on the number of threads, and which two choices (the counter-based generator and the per-chunk rows with a fixed-order sum) give that.
- You can derive $\eta=1/H_W$ for exponential work, and say why MRW reduces the total work but not the idle fraction of a warp.
- You can say why the tally stays in FP64 and what the float32 and Kahan results of Problem 4 show.
- You can say which parts of the speed-up you measured, which you only bounded, and why no amount of hardware removes the need for MC-17 and MC-18.
