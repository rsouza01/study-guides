# Module 21: Larmor, Thomson scattering and virtual quanta

**Books:** Jackson **14.2** (total power radiated by an accelerated charge: Larmor's formula and its relativistic generalization), **14.3** (angular distribution of radiation emitted by an accelerated charge), 14.4 (radiation emitted in the instantaneous rest frame; extremely relativistic motion: light), **14.7** (Thomson scattering of radiation), **14.8** (scattering by quasi-free charges; the Weizsacker-Williams method of virtual quanta: strongly recommended); Griffiths 11.2 (Larmor, radiation reaction preview). **Gaussian units.**
**Time:** 2 weeks (four sessions).

## Why this matters

Section 14.7 is the classical limit of Compton scattering: the same cross-section you will re-derive in QED. Section 14.8 shows that a boosted Coulomb field *is equivalent to a flux of real photons*: the classical ancestor of the virtual particle and of the parton model. Thomson scattering also gives you the **Eddington luminosity**, which limits accretion onto compact objects.

## Skip-test (40 minutes, no notes)

1. State Larmor's formula $P=\frac{2q^2a^2}{3c^3}$ and its relativistic generalization $P=\frac{2q^2}{3c}\gamma^6\left[\dot\beta^2-(\boldsymbol\beta\times\dot{\boldsymbol\beta})^2\right]$; give the special cases $\boldsymbol\beta\parallel\dot{\boldsymbol\beta}$ ($\gamma^6$) and $\boldsymbol\beta\perp\dot{\boldsymbol\beta}$ ($\gamma^4$).
2. State $\frac{dP(t')}{d\Omega}=\frac{q^2}{4\pi c}\frac{\left|\hat{\mathbf n}\times\left((\hat{\mathbf n}-\boldsymbol\beta)\times\dot{\boldsymbol\beta}\right)\right|^2}{(1-\hat{\mathbf n}\cdot\boldsymbol\beta)^5}$ and find, for linear acceleration at $\gamma\gg1$, that the peak angle is $\theta_{\max}\approx\frac{1}{2\gamma}$.
3. Derive the Thomson cross-section $\sigma_T=\frac{8\pi}{3}r_e^2=6.65\times10^{-25}$ cm$^2$ with $r_e=\frac{e^2}{mc^2}$ and the differential cross-section $\frac{d\sigma}{d\Omega}=\frac{r_e^2}{2}(1+\cos^2\Theta)$ for unpolarized radiation.
4. Describe the Weizsacker-Williams method: the transverse field of a fast charge seen from a point at impact parameter $b$ is a short pulse equivalent to a flux of photons with spectrum $\propto\frac{d\omega}{\omega}\ln\frac{\gamma c}{\omega b_{\min}}$.
5. Compute the Eddington luminosity $L_{\rm Edd}=\frac{4\pi GMm_pc}{\sigma_T}\approx1.26\times10^{38}\frac{M}{M_\odot}$ erg/s.

## Prerequisites

Module 20 (LW fields, radiation field).

## Detailed topics (checklist)

**Larmor and its relativistic form (14.2) [Must]**
- Non-relativistic: $P=\frac{2q^2}{3c^3}|\mathbf a|^2$ (and $\frac{2}{3}\frac{q^2a^2}{4\pi\epsilon_0c^3}$ in SI); from the dipole formula; angular pattern $\sin^2\Theta$ with $\Theta$ between $\hat{\mathbf n}$ and $\mathbf a$.
- Relativistic (Lienard): $P=\frac{2q^2}{3c}\gamma^6\left[\dot\beta^2-(\boldsymbol\beta\times\dot{\boldsymbol\beta})^2\right]$; covariant form $P=-\frac{2q^2}{3c}\frac{du^\mu}{d\tau}\frac{du_\mu}{d\tau}$ (an invariant, since energy emitted is a four-vector component divided by $\gamma$); linear acceleration $P=\frac{2q^2}{3c^3}\gamma^6a^2$ but in terms of the applied force $\frac{dp}{dt}$ it is $\frac{2q^2}{3m^2c^3}\left(\frac{dp}{dt}\right)^2$, *independent of $\gamma$*; circular motion $P=\frac{2q^2}{3c^3}\gamma^4a^2$, i.e. $\frac{2q^2}{3m^2c^3}\gamma^2\left(\frac{dp}{dt}\right)^2$, strongly enhanced.

**Angular distribution (14.3 to 14.4) [Must]**
- Power per unit solid angle per unit *retarded* time $\frac{dP(t')}{d\Omega}$ above (power per unit observer time carries one fewer factor of $(1-\hat{\mathbf n}\cdot\boldsymbol\beta)$); linear acceleration: $\frac{dP}{d\Omega}=\frac{q^2a^2}{4\pi c^3}\frac{\sin^2\theta}{(1-\beta\cos\theta)^5}$ with peak at $\cos\theta_{\max}=\frac{\sqrt{1+15\beta^2}-1}{3\beta}\to1-\frac{1}{8\gamma^2}$, so $\theta_{\max}\approx\frac1{2\gamma}$; the dipole pattern collapses into a forward cone (relativistic beaming).
- Total energy loss in a circular orbit: $\Delta E=\frac{4\pi}{3}\frac{q^2}{\rho}\beta^3\gamma^4$ per turn; for electrons $\Delta E[{\rm keV}]\approx88.5\,\frac{E^4[{\rm GeV}]}{\rho[{\rm m}]}$.

**Thomson scattering (14.7) [Must]**
- A free charge in a plane wave oscillates and radiates; $\frac{d\sigma}{d\Omega}=r_e^2\left|\hat{\boldsymbol\epsilon}'\cdot\hat{\boldsymbol\epsilon}\right|^2$ for a given polarization; unpolarized: $\frac{r_e^2}{2}(1+\cos^2\Theta)$; $\sigma_T=\frac{8\pi}{3}r_e^2=6.65\times10^{-25}$ cm$^2$, independent of frequency (valid for $\hbar\omega\ll mc^2$); partial polarization of the scattered light (maximum at $\Theta=90^\circ$).
- The classical limit of Compton scattering (the Klein-Nishina formula reduces to it).

**Virtual quanta (14.8) [Should]**
- Transform to the rest frame of a charge $ze$ and view an incoming fast charge $q$: the transverse field at impact parameter $b$ is a pulse of peak $\frac{\gamma q}{b^2}$ and duration $\frac{b}{\gamma v}$, with $\mathbf B\approx\hat{\mathbf n}\times\mathbf E$ so the pulse is like a plane wave; its Fourier spectrum extends to $\omega_{\max}\sim\frac{\gamma v}{b}$ and gives the equivalent photon spectrum $I(\omega)\approx\frac{2}{\pi}\frac{q^2}{c}\ln\left(\frac{\gamma c}{\omega b_{\min}}\right)$ per unit $\omega$; the classical ancestor of the virtual photon and the parton distribution $f(x)$.

## Method card

**Radiated power for a given motion:** (1) write $\boldsymbol\beta(t)$ and $\dot{\boldsymbol\beta}(t)$; (2) decide whether $\boldsymbol\beta\parallel\dot{\boldsymbol\beta}$ or $\perp$ to use the right $\gamma$ power; (3) compute $P$ and compare with the non-relativistic Larmor value; (4) for angular patterns use $\frac{dP}{d\Omega}$ with the right power of $(1-\hat{\mathbf n}\cdot\boldsymbol\beta)$ (check which time variable the distribution refers to); (5) integrate and check with $P=\frac{2q^2}{3c^3}\gamma^4a^2$ in the circular case.

## Reading plan

| Session | Task |
| --- | --- |
| A1 | Jackson 14.2; Griffiths 11.2; the relativistic Larmor formula |
| B1 | Exercises 1 to 3 |
| A2 | Jackson 14.3 to 14.4; angular pattern and the beaming angle |
| B2 | Exercise 4 |
| A3 | Jackson 14.7; Thomson cross-section and Eddington luminosity |
| B3 | Exercises 5 and 6 |
| A4 | Jackson 14.8 (virtual quanta) |
| B4 | Exercises 7 to 9; **Jackson targets** (exercise 10) |

## Derive from scratch

1. Larmor's formula from the radiation field.
2. The relativistic generalization and its $\gamma^6$ and $\gamma^4$ limits.
3. The peak angle $\theta_{\max}\approx\frac1{2\gamma}$.
4. The Thomson cross-section.
5. The pulse picture of the boosted Coulomb field.

## Bare-minimum exercises (with expected results)

1. **Classical atom:** an electron in a circular orbit of radius $a_0=5.29\times10^{-9}$ cm radiates and spirals in; the collapse time is $t\approx\frac{a_0^3}{4r_e^2c}\approx1.6\times10^{-11}$ s (one of the reasons classical physics fails for atoms).
2. **Synchrotron energy loss per turn:** for $\beta\to1$, $\Delta E=\frac{4\pi}{3}\frac{q^2}{\rho}\gamma^4$; for electrons $\Delta E\approx88.5\frac{E^4[{\rm GeV}]}{\rho[{\rm m}]}$ keV (for $E=1$ GeV and $\rho=3.3$ m, $\approx27$ keV per turn).
3. **Linear versus circular at fixed force:** in terms of $\frac{dp}{dt}$, linear acceleration radiates $\frac{2q^2}{3m^2c^3}\left(\frac{dp}{dt}\right)^2$ regardless of $\gamma$, while circular motion radiates $\gamma^2$ times as much; so radiation losses dominate in circular accelerators and not in linear ones.
4. **Beaming angle:** $\cos\theta_{\max}=\frac{\sqrt{1+15\beta^2}-1}{3\beta}$ gives $\theta_{\max}\approx2.9^\circ$ for $\gamma=10$ ($\beta=0.995$), close to $\frac{1}{2\gamma}=2.9^\circ$.
5. **Thomson cross-section:** $\sigma_T=\frac{8\pi}{3}r_e^2=\frac{8\pi}3(2.818\times10^{-13}\,{\rm cm})^2=6.65\times10^{-25}$ cm$^2$; the mean free path in fully ionized hydrogen of density $\rho$ is $\ell=\frac{m_p}{\rho\sigma_T}\approx\frac{2.5}{\rho}$ cm for $\rho$ in g/cm$^3$ (for $\rho=10^{-7}$ g/cm$^3$ it is $2.5\times10^7$ cm).
6. **Eddington luminosity:** balance the outward radiation force on electrons $\frac{L\sigma_T}{4\pi r^2c}$ against gravity on the proton $\frac{GMm_p}{r^2}$: $L_{\rm Edd}=\frac{4\pi GMm_pc}{\sigma_T}=1.26\times10^{38}\frac{M}{M_\odot}$ erg/s; for a $1.4M_\odot$ neutron star $\approx1.8\times10^{38}$ erg/s.
7. **Differential Thomson cross-section:** show $\frac{d\sigma}{d\Omega}=\frac{r_e^2}{2}(1+\cos^2\Theta)$ for unpolarized light by averaging $|\hat{\boldsymbol\epsilon}'\cdot\hat{\boldsymbol\epsilon}|^2$ over incident polarizations, and integrate to $\sigma_T$.
8. **Virtual quanta:** in the rest frame of a target, a fast charge $q$ at impact parameter $b$ produces a transverse field of peak $E_{\rm peak}=\frac{\gamma q}{b^2}$ lasting $\Delta t\approx\frac{b}{\gamma v}$, so $|E(\omega)|\approx E_{\rm peak}\Delta t=\frac{q}{bv}$, flat up to $\omega_{\max}\approx\frac{\gamma v}{b}$; the energy per unit area per unit frequency is $\frac{dI}{d\omega}\approx\frac{c}{2\pi}\frac{q^2}{b^2v^2}$. Integrate over impact parameters, $\int2\pi b\,db$, to get $\frac{cq^2}{v^2}\ln\frac{b_{\max}}{b_{\min}}$ with $b_{\max}\approx\frac{\gamma v}{\omega}$: the logarithmic equivalent-photon spectrum.
9. **Where Thomson fails:** the quantum Klein-Nishina formula reduces to Thomson only for $\hbar\omega\ll mc^2$; at higher energies the cross-section falls; estimate the energy at which this matters for electrons (about $0.5$ MeV).
10. **Jackson targets (about 14.4 and 14.5):** (a) Larmor power from a specified motion (for example the circular orbit of exercise 2 or a particle in a harmonic trap); (b) the angular distribution for linear versus circular acceleration (exercises 3 and 4).

## Optional extension

Show that the Thomson scattered radiation reaction on the free electron is the radiation-pressure force $\frac{\sigma_TI}{c}$ and use it to derive the radiation-drag limit on dust grains and on infalling plasma (Poynting-Robertson drag), an astrophysical application.

## Pitfalls

- Using $\gamma^6$ when the acceleration is perpendicular to the velocity (it is $\gamma^4$).
- Confusing power per unit retarded time with power per unit observer time (an extra factor of $1-\hat{\mathbf n}\cdot\boldsymbol\beta$).
- Applying Thomson scattering at photon energies near or above $mc^2$.
- Forgetting that $\sigma_T$ is frequency-independent only in the Thomson limit.

## Gate questions

1. Why is the radiated power Lorentz invariant, and how does the $\gamma^4$ arise for circular motion?
2. Why is the Thomson cross-section independent of frequency?
3. What does "the field of a fast charge is a flux of virtual photons" mean precisely?

## One-page cheat sheet contents

Larmor and relativistic Larmor; angular distribution and beaming; $\sigma_T$ and $d\sigma/d\Omega$; $L_{\rm Edd}$; virtual-quanta spectrum.
