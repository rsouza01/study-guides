# Module 28: Final consolidation and capstone (Week 27)

**Books:** all, plus your monthly deliverables (`m1` to `m5`) and `error_log.md`.
**Time:** 1 week for the gate, then the capstone as a sustained block.

## Goal

Decide with evidence whether you can now derive the physics of the neutron-star outer layers from nuclear physics: masses to the crust, the NN interaction to QHD, and the EOS to observables. The capstone is code plus a validation note.

## Skip-test (final gate, under three hours, blank page)

1. The SEMF and its consequences for outer-crust composition.
2. The outer-crust construction: Gibbs minimisation, lattice energy, drip.
3. Deuteron $\to$ tensor force; effective-range expansion; Yukawa and OBE with the sign rule.
4. Shell-model level scheme; vibrator/rotor signatures and the moment-of-inertia deficit; HF; the Skyrme functional.
5. Fission deformation energy and fissility; the Gamow factor; the allowed $\beta$ spectrum and Gamow-Teller selection rules; Weisskopf estimates; the Gamow peak.
6. $E/A(n,\delta)$; the five numbers; what each controls.
7. The inner-crust cell functional; the virial relation; the crust-core criterion and its $L$ dependence.
8. The QHD-I Lagrangian; MFT; saturation; the EOS; the failures; the repairs.
9. The $\rho$ meson and the symmetry energy.
10. $\beta$ equilibrium, $x(n_B)$, the direct Urca threshold and $T^6$ emissivity.
11. The envelope: why $T_s\ne T_b$ and what sets the relation.

## Prerequisites

Modules 01 to 27.

## Detailed topics (checklist)

**Capstone project: as a module for `tov-solver.py` [Must]**
- **`eos/crust.py`**: outer crust from a mass table plus inner crust from a CLDM with a chosen Skyrme functional, thermodynamically consistent, tested to machine precision.
- **`eos/rmf.py`**: general nonlinear RMF with $\sigma$, $\omega$, $\rho$, arbitrary parameter set, $\beta$-equilibrated $npe\mu$ composition, finite-$T$ optional.
- **Matching logic**, with tests reproducing published $\Delta R$, $\Delta M$, $\Delta I/I$ for a standard EOS.
- **A validation note** (2 to 4 pages) comparing your unified EOS against SLy and against your SWRDP tables, stating where the crust treatment changes the $M$-$R$ curve and where it does not.

The crust barely moves the maximum mass and materially moves $R_{1.4}$; quantifying that with your own code, against models already validated, is a genuine result and a natural bridge to the PSR J0740+6620 work.

## Reading plan

| Block | Task |
| --- | --- |
| Session 1 | Gate items 1 to 4 |
| Session 2 | Gate items 5 to 8 |
| Session 3 | Gate items 9 to 11; grade yourself |
| Sessions 4 and beyond | The capstone |

## Derive from scratch

Redo the three derivations you found hardest during the gate.

## Bare-minimum exercises (with expected results)

1. **Gate item 2:** reproduce the composition sequence $^{56}$Fe, $^{62}$Ni, $N=50$ chain, $N=82$ chain and the drip at $\rho\approx4.3\times10^{11}$ g/cm$^3$.
2. **Gate item 6:** state the five numbers with their values ($n_0=0.16$, $B_0=16$, $K=230\pm30$, $J=31$ to $33$, $L=40$ to $80$ MeV) and write a sentence for each.
3. **Gate item 8:** reproduce the QHD-I saturation point ($k_F=1.42$ fm$^{-1}$, $E/A=-15.75$ MeV), $K\approx546$ MeV and $M^*/M\approx0.56$.
4. **Gate item 10:** derive $x_{\rm DU}=\frac19$ and $0.148$ and the $T^6$ versus $T^8$ emissivity scaling.
5. **Test of consistency:** verify $P=n_B^2\frac{d(\varepsilon/n_B)}{dn_B}$ across your unified table to $10^{-8}$ relative.
6. **Seams:** list drip, crust-core and any $npe\to npe\mu$ transition and verify continuity of $P$ and $\mu_B$ at each.
7. **TOV check:** reproduce the published $M(R)$ for a standard EOS (SLy) to better than $1\%$ in $R_{1.4}$.
8. **$L$ sensitivity:** with two Skyrme sets of different $L$, report $\Delta R$, $\Delta M$, $\Delta I/I$ at $1.4M_\odot$ and compare with the Module 20 expectation (smaller $L\Rightarrow$ thicker crust).
9. **Validation note outline:** purpose, method, tests, results (table), where the crust matters, limitations.
10. **Next steps:** choose two items from the appendix's parked list.

## Optional extension

Add superfluid entrainment parameters and compute the glitch-relevant crustal moment of inertia fraction.

## Pitfalls

- Treating a passed gate as recognition rather than recall.
- Starting the capstone before the gate (the capstone depends on the unification lessons).
- Inconsistent parameter sets across the crust and core.

## Gate questions

1. Which of the three threads (A, B, C) is weakest and what is your plan for it?
2. What is the one observable most sensitive to $L$, and what does it tell you?
3. What would you cut or add in a second pass?

## One-page cheat sheet contents

The five numbers; the saturation mechanism in a paragraph; $x_{\rm DU}$ thresholds; the unified-EOS test list.
