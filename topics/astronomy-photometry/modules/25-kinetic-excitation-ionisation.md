# Module 25: Kinetic, excitation and ionisation temperatures

[← 24 Colour temperature](24-colour-temperature.md) · [README](../README.md) · [Next: 26 Masers and population inversion →](26-masers-and-population-inversion.md)

**Source:** Karttunen, §5.8, p. 116, eqs (5.32)–(5.34).

---

## Session A: read

- Read the last paragraphs on temperatures in §5.8 (p. 116).
- Key ideas:
  - **Kinetic temperature** $T_k$: defined by the particle velocities, Maxwell–Boltzmann distribution, $\tfrac12m\langle v^2\rangle=\tfrac32kT_k$.
  - **Excitation temperature** $T_{\rm exc}$: defined by level populations through the Boltzmann formula (Module 16).
  - **Ionisation temperature** $T_{\rm ion}$: defined by the degree of ionisation through the Saha equation.
  - In **local thermodynamic equilibrium (LTE)** all of these agree. In low-density gas collisions are too rare to maintain this and they differ.
- Derivation to do on paper: from $\tfrac12m\langle v^2\rangle=\tfrac32kT$, get $v_{\rm rms}=\sqrt{3kT/m}$. The mean speed is $\sqrt{8kT/\pi m}$ and the most probable $\sqrt{2kT/m}$.

---

## Session B: compute

**Problem 1: speeds**

- Compute $v_{\rm rms}$, mean and most probable speeds of electrons at $10^6$ K (a coronal temperature), and $v_{\rm rms}$ of hydrogen atoms at $10^4$ K.
- Verify by Monte Carlo: draw velocity components from a Gaussian with $\sigma=\sqrt{kT/m}$.

**Problem 2: gas pressure**

- $P=nkT$. Evaluate for $n=10^{14}$ m⁻³ and $T=10^6$ K.

**Problem 3: do collisions set the populations?**

- Simulate a two-level atom with a Markov chain: transition probabilities up and down per collision satisfying detailed balance, $p_{\uparrow}/p_{\downarrow}=(g_2/g_1)e^{-\Delta E/kT}$.
- Take $\Delta E/kT=1$ and $g_2/g_1=3$. Run $10^6$ collisions and compare the long-run population ratio with the Boltzmann value.

**Problem 4: when do the temperatures differ?**

- Describe, with your own numbers, a situation where $T_{\rm exc}\ne T_k$: take a gas where radiative decay is faster than the collision rate, and use the two-level rate balance $n_1C_{12}=n_2(C_{21}+A_{21})$ to find $n_2/n_1$ and $T_{\rm exc}$ as a function of $n$ (the collision rate scales with density).

---

## Checkpoints

| Quantity | Value |
|---|---|
| electrons, $10^6$ K: $v_{\rm rms}$ | $6.743\times10^{6}$ m s⁻¹ |
| mean speed | $6.213\times10^{6}$ m s⁻¹ |
| most probable speed | $5.506\times10^{6}$ m s⁻¹ |
| Monte Carlo rms / mean | $6.742\times10^{6}$ / $6.212\times10^{6}$ m s⁻¹ |
| H atoms, $10^4$ K: $v_{\rm rms}$ | 15.7 km s⁻¹ |
| $P=nkT$ | $1.38\times10^{-3}$ Pa |
| two-level chain, $n_2/n_1$ | $3e^{-1}=1.1036$ |

---

## Done when

- You can state which physical process each temperature measures.
- You can explain why $T_{\rm exc}$ approaches $T_k$ at high density and why they separate at low density.
- You can derive the three characteristic speeds of a Maxwell–Boltzmann gas.
