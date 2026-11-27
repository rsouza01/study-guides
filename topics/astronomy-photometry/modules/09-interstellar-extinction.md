# Module 09: Interstellar extinction

[← 08 Absolute magnitude and distance modulus](08-absolute-magnitude-and-distance-modulus.md) · [README](../README.md) · [Next: 10 Colour excess and reddening →](10-colour-excess-and-reddening.md)

**Source:** Karttunen, §4.5, pp. 97–98, eqs (4.15)–(4.19), Fig. 4.8; Examples 4.6 and 4.7, pp. 100–101; Exercise 4.5, p. 102.

---

## Session A: read

- Read §4.5 from its start (p. 97) up to "Colour Excess" (p. 98), then Examples 4.6 and 4.7.
- Key ideas:
  - Dust absorbs and scatters light. Together this is **extinction**.
  - Over a short path $dr$: $dL=-\kappa L\,dr$ (4.15), where $\kappa$ is the opacity (m⁻¹; the book writes α).
  - The **optical thickness** is $d\tau=\kappa\,dr$ (4.16), and the flux decays as $L=L_0e^{-\tau}$ (4.17).
  - The distance modulus gains an extinction term: $m-M=5\lg(r/10\,{\rm pc})+A$ (4.18), with $A=(2.5\lg e)\,\tau=1.0857\,\tau$.
  - For constant opacity, $A=a\,r$ with $a$ in mag per unit distance (4.19).
- Derivation of (4.18):
  1. $F(r)=F_0\,(R/r)^2e^{-\tau}$ and $F(10\,{\rm pc})=F_0\,(R/10\,{\rm pc})^2$, with no extinction at 10 pc.
  2. $m-M=-2.5\lg[F(r)/F(10)]=5\lg(r/10\,{\rm pc})-2.5\lg e^{-\tau}$.
  3. The last term is $+(2.5\lg e)\,\tau\equiv A$.

---

## Session B: compute

**Problem 1: optical thickness and magnitudes**

- Write `A_from_tau(tau)` and `tau_from_A(A)`.
- Example 4.7: the Sun seen through fog looks as bright as a full Moon in clear sky ($m_\odot=-26.8$, $m_{\rm Moon}=-12.5$). Find the optical thickness of the fog.

**Problem 2: Example 4.6, three ways**

- A star has $M=-2$, $m=8$ and the extinction is 2 mag/kpc. Solve $10=5\lg(r/10)+0.002\,r$ for $r$ in pc by:
  1. the book's fixed-point iteration $r\leftarrow10\times10^{\,2-0.0004\,r}$, starting from $r=1000$;
  2. bisection;
  3. Newton's method.
- Compare the number of iterations to get $\pm0.1$ pc.
- For the fixed-point map $g(r)$, compute $|g'(r)|$ at the solution and explain why it converges.

**Problem 3: distance versus extinction rate**

- Repeat Problem 2 for extinction rates of 0, 0.5, 1, 2, 3 and 4 mag/kpc.

**Problem 4: Exercise 4.5 (a triple window)**

- Stars are viewed through a triple window. Each glass surface reflects 15 % of the light.
- (a) What magnitude does Regulus (apparent $V=1.36$) have when seen through the window?
- (b) What is the optical thickness of the window?
- Take "triple" as three panes, which means six surfaces, and state your assumption. The book prints Regulus as $M_V$; it is the apparent magnitude.

<details>
<summary>Answer</summary>

With six surfaces and a simple product of transmissions, $T=0.85^6=0.377$: $\Delta m=1.06$, so $m=2.42$, and $\tau=0.975$. With three surfaces instead: $\Delta m=0.53$, $\tau=0.49$.

</details>

**Problem 5 (bonus): multiple reflections**

- The simple product ignores light that bounces between surfaces. For $N$ identical partially reflecting surfaces (no absorption), simulate $10^6$ photons bouncing back and forth and count those that get through.
- Compare with $(1-R)/\big(1+(N-1)R\big)$.
- Compare with the book's remark in Example 4.7 about multiply scattered light.

---

## Checkpoints

| Quantity | Value |
|---|---|
| $2.5\lg e$ | 1.0857 |
| Example 4.7: $\tau$ | 13.17 (the book: 13.2) |
| Example 4.6: root | 584.0 pc |
| first fixed-point iterates | 398, 693, 528, 615, 568, 593, 579, … |
| $\lvert g'\rvert$ at the root | about 0.54 |

| Extinction (mag/kpc) | $r$ (pc) |
|---|---|
| 0 | 1000.0 |
| 0.5 | 826.7 |
| 1 | 718.3 |
| 2 | 584.0 |
| 3 | 500.7 |
| 4 | 442.5 |

- Bonus: six surfaces, $T=0.85/(1+5\times0.15)=0.486$, so $\Delta m=0.78$ instead of 1.06.

---

## Done when

- You can derive $m-M=5\lg(r/10\,{\rm pc})+A$ and say what each term is.
- You can explain why iteration converges here, from your computed $\lvert g'\rvert$.
- You can say what extinction does to a distance you derive while ignoring it (too large, and by how much, for 2 mag).
