# Module 15: Quantum numbers and selection rules

[← 14 Line profiles](14-line-profiles.md) · [README](../README.md) · [Next: 16 Boltzmann populations →](16-boltzmann-populations.md)

**Source:** Karttunen, §5.4, pp. 108–110 (up to "Population Numbers"), Figs 5.7–5.8.

---

## Session A: read

- Read §5.4 from p. 108 up to the "Population Numbers" paragraph (p. 110).
- Key ideas:
  - Four quantum numbers: $n$ (energy), $l=0,\dots,n-1$ (orbital angular momentum; letters s, p, d, f, g…), $m_l=-l,\dots,l$ (its projection, responsible for the Zeeman effect), $m_s=\pm\tfrac12$ (spin).
  - The total angular momentum has $j=l\pm\tfrac12$ (only $\tfrac12$ for $l=0$). Spin produces **fine structure**: close doublets.
  - **Selection rules** for electric dipole transitions: $\Delta l=\pm1$, $\Delta m_l=0,\pm1$; in terms of total angular momentum $\Delta j=0,\pm1$, $\Delta m_j=0,\pm1$.
  - Other transitions are **forbidden**, not impossible; they are just very slow. They show up in very rarefied gas (auroras, planetary nebulae).
  - The 21 cm line of hydrogen is a forbidden (magnetic dipole) spin-flip: electron and proton spins parallel versus antiparallel. Its probability is $A=2.8\times10^{-15}$ s⁻¹.

---

## Session B: compute

**Problem 1: count the states**

- Enumerate all $(n,l,m_l,m_s)$ for $n=1,\dots,5$. Check that shell $n$ has $2n^2$ states.

**Problem 2: fine-structure levels**

- For $n=3$ list the levels $(n,l,j)$, with $j=l\pm\tfrac12$. Count the states in each level as $2j+1$, and check they add up to 18.

**Problem 3: a selection-rule engine**

- Write `allowed(upper, lower)` using $\Delta l=\pm1$ and $\Delta j=0,\pm1$.
- Count the allowed components of the $n=3\to n=2$ transition ($H_\alpha$) with fine structure.

**Problem 4: the Zeeman effect (Fig. 5.7)**

- For a $p\to d$ transition list all pairs $(m_l,m_l')$ with $\Delta m_l\in\{0,\pm1\}$. How many transitions are there, and how many distinct energy differences in a magnetic field?
- Generalise to any $l\to l+1$.

**Problem 5: the 21 cm line**

- From $A=2.8\times10^{-15}$ s⁻¹ compute the mean lifetime in years.
- Compare with the typical allowed-line lifetime $10^{-8}$ s. Why can the line still be observed?

<details>
<summary>Hint (Problem 5)</summary>

Think about how many atoms there are along a line of sight through the Galaxy, and about the collision time in the interstellar medium (the book's argument, p. 110).

</details>

---

## Checkpoints

| Quantity | Value |
|---|---|
| states per shell $n=1..5$ | 2, 8, 18, 32, 50 |
| fine-structure levels at $n=3$ | 3s½, 3p½, 3p3/2, 3d3/2, 3d5/2 |
| allowed fine-structure components of $H_\alpha$ | 7 |
| $p\to d$ pairs with $\lvert\Delta m_l\rvert\le1$ | 9 |
| distinct lines in a field | 3 |
| 21 cm lifetime $1/A$ | $3.57\times10^{14}$ s $=1.13\times10^{7}$ yr (the book: $11\times10^6$) |
| ratio to the allowed-line lifetime | $3.6\times10^{22}$ |

---

## Done when

- You can explain what each quantum number labels and why $l$ stops at $n-1$.
- You can explain why $H_\alpha$ is observed as several close components and what the Zeeman effect does to a line.
- You can explain what "forbidden" means and why the 21 cm line is observable only in very low-density gas.
