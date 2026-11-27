# Module 26: Masers and population inversion

[← 25 Kinetic, excitation and ionisation temperatures](25-kinetic-excitation-ionisation.md) · [README](../README.md) · [Next: 27 Radiative transfer →](27-radiative-transfer.md)

**Source:** Karttunen, §5.8, p. 116, and the maser discussion of §5.4 (p. 110).

---

## Session A: read

- Read the maser paragraph on pp. 116 and the mention of induced emission on p. 104.
- Key ideas:
  - Normally $n_2<n_1$ for an upper level 2, so absorption beats induced emission and the gas attenuates.
  - If $n_2/g_2>n_1/g_1$ (**population inversion**), induced emission wins. Formally $T_{\rm exc}<0$.
  - Then the optical depth is negative, so radiation is amplified exponentially: $I=I_0e^{-\tau}$ with $\tau<0$. This is a **maser** (laser at microwave frequencies).
  - Inversion needs a pump: something that populates the upper level faster than it decays.

---

## Session B: compute

**Problem 1: a three-level pump**

- Levels 1, 2, 3. A pump moves atoms $1\to3$ at rate $P$ per atom, level 3 decays quickly to 2 at rate $A_{32}$, and level 2 decays slowly to 1 at rate $A_{21}$.
- Solve the steady state for the fractional populations with $P=3$, $A_{21}=1$, $A_{32}=100$ (arbitrary units). Show that $N_2/N_1=P/A_{21}$.

**Problem 2: negative excitation temperature**

- Use (5.11) with a ratio $N_2/N_1=3$, $g_2=g_1$, and $\Delta E=10^{-3}$ eV. What is $T_{\rm exc}$? Why is it negative?

**Problem 3: exponential amplification**

- A beam passes through $N$ identical segments, each of which multiplies the intensity by 1.1. Compute the total gain for $N=50$.
- Compare with $e^{-\tau}$ for $\tau=-5$.

**Problem 4: what limits the gain?**

- Think about what happens as the radiation field itself grows and depopulates level 2 (saturation). Sketch what you would add to Problem 1 to model it.

---

## Checkpoints

| Quantity | Value |
|---|---|
| steady-state $N_1,N_2,N_3$ | 0.24814, 0.74442, 0.00744 |
| $N_2/N_1$ | 3 ($=P/A_{21}$) |
| $T_{\rm exc}$ for ratio 3, $\Delta E=10^{-3}$ eV | −10.56 K |
| $1.1^{50}$ | 117.4 |
| $e^{5}$ | 148.4 |

---

## Done when

- You can explain why a negative $T_{\rm exc}$ is not "below absolute zero" but a statement about populations.
- You can say why a pump and a fast decay into the metastable level are both needed.
- You can explain why masers amplify only a narrow, bright line.
