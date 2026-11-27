# Module 13: The hydrogen atom (Bohr model)

[← 12 Photons and energy levels](12-photons-and-energy-levels.md) · [README](../README.md) · [Next: 14 Line profiles →](14-line-profiles.md)

**Source:** Karttunen, §5.2, pp. 105–107, eqs (5.2)–(5.8), Fig. 5.4; Example 5.1, p. 118; Exercise 5.2, p. 120.

---

## Session A: read

- Read §5.2 (pp. 105–107).
- Key ideas:
  - Bohr's first postulate: the angular momentum is quantised, $m v r=n\hbar$ (5.2). The second: an electron in an allowed orbit does not radiate; it radiates only when it jumps, $h\nu=E_{n_2}-E_{n_1}$ (5.3).
  - Combining the Coulomb force with $mv^2/r$ fixes the orbit speed and radius for each $n$ (5.4)–(5.5), and then the energies $E_n=-C/n^2$ (5.6).
  - The Rydberg formula follows: $1/\lambda=R\,(1/n_1^2-1/n_2^2)$ (5.8), with $R\approx1.097\times10^{7}$ m⁻¹.
  - The series are named by their lower level: Lyman ($n_1=1$, ultraviolet), Balmer (2, visible, $H_\alpha,H_\beta,\dots$), Paschen (3), Brackett (4), Pfund (5).
- Derivation to do on paper:
  1. Coulomb: $\dfrac{mv_n^2}{r_n}=\dfrac{1}{4\pi\epsilon_0}\dfrac{e^2}{r_n^2}$.
  2. Quantisation: $m v_n r_n=n\hbar$.
  3. Eliminate $v_n$: $r_n=\dfrac{4\pi\epsilon_0\hbar^2}{me^2}\,n^2$ and $v_n=\dfrac{e^2}{4\pi\epsilon_0\hbar}\,\dfrac1n$.
  4. Energy: $E_n=\tfrac12mv_n^2-\dfrac{1}{4\pi\epsilon_0}\dfrac{e^2}{r_n}=-\dfrac{me^4}{32\pi^2\epsilon_0^2\hbar^2}\dfrac1{n^2}$.

---

## Session B: compute

**Problem 1: constants from first principles**

- Compute from $m_e$, $e$, $\epsilon_0$, $\hbar$, $h$, $c$: the Bohr radius $a_0=r_1$, the speed $v_1$, the ground-state energy $E_1$ in eV, and the Rydberg constant $R_\infty=\dfrac{me^4}{8\epsilon_0^2h^3c}$.
- Compare $v_1/c$ with the fine-structure constant.

**Problem 2: a table of levels**

- For $n=1,\dots,6$ tabulate $r_n$, $v_n$ and $E_n$ (in eV).

**Problem 3: the line series**

- Compute wavelengths in nm for Lyman $\alpha$ and its limit, $H_\alpha$, $H_\beta$ and the Balmer limit, Paschen $\alpha$, Brackett $\alpha$, Pfund $\alpha$, using the book's $R=1.097\times10^7$ m⁻¹.
- The Balmer limit is also called the Balmer discontinuity (Fig. 5.4).

**Problem 4: the reduced-mass correction**

- The proton is not infinitely heavy. Use $R_H=R_\infty/(1+m_e/m_p)$ and recompute $H_\alpha$. By how much does it shift?

**Problem 5: Example 5.1 (radio recombination lines)**

- Find the wavelength of the transition $n=110\to109$ in hydrogen.

**Problem 6: Exercise 5.2**

- If the transition $n+1\to n$ were to correspond to a wavelength of 21.05 cm, what would $n$ be? Also compute the orbit radius $r_n$ for that $n$.
- The interstellar medium emits strongly at this wavelength. Can the radiation be due to such transitions? Think about which numbers you now have, and look again at §5.4.

<details>
<summary>Answer to Problem 6 (numbers)</summary>

$n=166$ gives 21.04 cm. Its orbit radius is $r_n=1.46\ \mu{\rm m}$. The conclusion is yours to argue.

</details>

---

## Checkpoints

| Quantity | Value |
|---|---|
| $a_0$ | $5.2918\times10^{-11}$ m |
| $v_1$ | $2.1877\times10^{6}$ m s⁻¹ ($=\alpha c$, $v_1/c=0.0072974$) |
| $E_1$ | −13.606 eV |
| $R_\infty$ | $1.09737\times10^{7}$ m⁻¹ |

Wavelengths in nm (with $R=1.097\times10^{7}$ m⁻¹):

| Line | $\lambda$ (nm) |
|---|---|
| Lyman $\alpha$ | 121.5 |
| Lyman limit | 91.16 |
| $H_\alpha$ | 656.3 |
| $H_\beta$ | 486.2 |
| Balmer limit | 364.6 |
| Paschen $\alpha$ | 1875.2 |
| Brackett $\alpha$ | 4051.5 |
| Pfund $\alpha$ | 7458.4 |

| Quantity | Value |
|---|---|
| $H_\alpha$ with $R_\infty$ / with $R_H$ | 656.11 / 656.47 nm |
| Example 5.1 wavelength | 5.98 cm (the book: 0.060 m) |

---

## Done when

- You can reproduce the four steps of the Bohr derivation on paper.
- You can say which series is visible and why $H_\alpha$ is red.
- You can explain why the reduced-mass correction is small but measurable.
