"""Numerical / symbolic check of the 'expected results' quoted in the complex-analysis guide.

Run:  python3 verify_expected_results.py
Needs: numpy, scipy, mpmath, sympy.
Proof-type exercises (show that ...) are not machine-checked; only the numbers and closed forms are.
"""
import numpy as np
import mpmath as mp
import sympy as sp

mp.mp.dps = 30
FAILS = []


def check(name, got, exp, tol=1e-9):
    got, exp = complex(got), complex(exp)
    ok = abs(got - exp) <= tol * max(1.0, abs(exp))
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else f"   got={got} expected={exp}"))
    if not ok:
        FAILS.append(name)


def contour(f, gamma, dgamma, a, b):
    """integral of f(z) dz along z = gamma(t), t in [a, b]"""
    return mp.quad(lambda t: f(gamma(t)) * dgamma(t), mp.linspace(a, b, 9))


circle = lambda z0, r: (lambda t: z0 + r * mp.e ** (1j * t), lambda t: 1j * r * mp.e ** (1j * t))
two_pi = 2 * mp.pi

# ---------------- CA01 ----------------
check("CA01.1 (1+i)^10 = 32i", (1 + 1j) ** 10, 32j)
for k, z in enumerate([np.sqrt(3) + 1j, -np.sqrt(3) + 1j, -2j]):
    check(f"CA01.3 root {k} of z^3=8i", z ** 3, 8j, 1e-12)
for n in (5, 7):
    w = np.exp(2j * np.pi / n)
    check(f"CA01.9 prod(1-w^k), n={n}", np.prod([1 - w ** k for k in range(1, n)]), n, 1e-12)
    check(f"CA01.2 prod roots of unity n={n}", np.prod([w ** k for k in range(n)]), (-1) ** (n + 1), 1e-12)
for th, n in [(0.7, 4), (1.9, 6)]:
    check(f"CA01.6 Dirichlet kernel th={th},n={n}", sum(np.cos(k * th) for k in range(n + 1)),
          0.5 + np.sin((n + 0.5) * th) / (2 * np.sin(th / 2)), 1e-12)
check("CA01.7 exp(0.5 ln2 + i pi/4) = 1+i", mp.e ** (0.5 * mp.log(2) + 1j * mp.pi / 4), 1 + 1j)
rng = np.random.default_rng(1)
bad = 0
for _ in range(2000):
    z = complex(*rng.uniform(-3, 3, 2))
    if abs(z) < 1e-9:
        continue
    bad += ((1 / z).real > 0.5) != (abs(z - 1) < 1)
check("CA01.8 Re(1/z)>1/2  <=>  |z-1|<1 (mismatches)", bad, 0)
check("CA01 skip-test (1+i)/(2-i) = (1+3i)/5", (1 + 1j) / (2 - 1j), (1 + 3j) / 5, 1e-12)

# ---------------- CA02 ----------------
x, y = sp.symbols("x y", real=True)
u, v = x ** 3 - 3 * x * y ** 2, 3 * x ** 2 * y - y ** 3
J = sp.Matrix([[sp.diff(u, x), sp.diff(u, y)], [sp.diff(v, x), sp.diff(v, y)]]).det()
check("CA02.7 Jacobian of z^3 at 1+i", complex(J.subs({x: 1, y: 1})), 36)
check("CA02.4 conjugate of x^3-3xy^2 is harmonic pair (u_x=v_y)", complex(sp.simplify(sp.diff(u, x) - sp.diff(v, y))), 0)
check("CA02.4 (u_y=-v_x)", complex(sp.simplify(sp.diff(u, y) + sp.diff(v, x))), 0)
u9, v9 = x ** 2, y ** 2
check("CA02.9 CR forces x=y: u_x-v_y", complex(sp.simplify(sp.diff(u9, x) - sp.diff(v9, y)).subs(y, x)), 0)

# ---------------- CA03 ----------------
check("CA03.3 i^i principal", mp.power(1j, 1j), mp.e ** (-mp.pi / 2), 1e-12)
check("CA03.2 Log(1+i)", mp.log(1 + 1j), 0.5 * mp.log(2) + 1j * mp.pi / 4)
check("CA03.4 sin(pi/2 + i ln(2+sqrt3)) = 2", mp.sin(mp.pi / 2 + 1j * mp.log(2 + mp.sqrt(3))), 2)
check("CA03.10 cos(i ln(2+sqrt3)) = 2", mp.cos(1j * mp.log(2 + mp.sqrt(3))), 2)
check("CA03.6 sqrt(1+i) = 2^(1/4) e^(i pi/8)", mp.sqrt(1 + 1j), 2 ** 0.25 * mp.e ** (1j * mp.pi / 8))
check("CA03.9 d/dz z^(1/2) at 4", mp.diff(lambda z: mp.sqrt(z), 4), 0.25)
check("CA03.7 Log(1) - 2 Log(-1)", mp.log(1) - 2 * mp.log(-1), -2j * mp.pi)

# ---------------- CA04 ----------------
g, dg = circle(0, 1)
check("CA04.1 oint dz/z", contour(lambda z: 1 / z, g, dg, 0, two_pi), 2j * mp.pi)
check("CA04.1 oint z^2 dz", contour(lambda z: z ** 2, g, dg, 0, two_pi), 0, 1e-12)
check("CA04.2 int zbar dz upper semicircle 1 -> -1", contour(lambda z: mp.conj(z), g, dg, 0, mp.pi), 1j * mp.pi)
check("CA04.3 int_0^(1+i) z^2 dz", (1 + 1j) ** 3 / 3, (-2 + 2j) / 3, 1e-12)
g2, dg2 = circle(0, 2)
check("CA04.4 oint_{|z|=2} dz/(z^2+1)", contour(lambda z: 1 / (z ** 2 + 1), g2, dg2, 0, two_pi), 0, 1e-12)
check("CA04.4 min |z^2+1| on |z|=2 is 3", min(abs((2 * np.exp(1j * t)) ** 2 + 1) for t in np.linspace(0, 6.2832, 2001)), 3, 1e-6)
g3, dg3 = circle(0, 0.5)
check("CA04.6 oint_{|z|=1/2} dz/(z(z-1))", contour(lambda z: 1 / (z * (z - 1)), g3, dg3, 0, two_pi), -2j * mp.pi)
check("CA04.6 oint_{|z|=2} dz/(z(z-1))", contour(lambda z: 1 / (z * (z - 1)), g2, dg2, 0, two_pi), 0, 1e-12)
check("CA04.8 int_0^(i pi) e^z dz", mp.e ** (1j * mp.pi) - 1, -2, 1e-12)
# wire field: Re oint (P - iQ) dz = 2 pi  with P-iQ = -i/z
check("CA04.10 wire field circulation", mp.re(contour(lambda z: -1j / z, g, dg, 0, two_pi)), two_pi)

# ---------------- CA05 ----------------
g2, dg2 = circle(0, 2)
check("CA05.1 oint e^z/(z-1), |z|=2", contour(lambda z: mp.e ** z / (z - 1), g2, dg2, 0, two_pi), 2j * mp.pi * mp.e)
check("CA05.2 oint cos z / z^3, |z|=2", contour(lambda z: mp.cos(z) / z ** 3, g2, dg2, 0, two_pi), -1j * mp.pi)
g3_, dg3_ = circle(0, 3)
check("CA05.3 oint z^2/((z-1)(z-2)), |z|=3", contour(lambda z: z ** 2 / ((z - 1) * (z - 2)), g3_, dg3_, 0, two_pi), 6j * mp.pi)
g1, dg1 = circle(0, 1)
check("CA05.4 oint sin z / z^2, |z|=1", contour(lambda z: mp.sin(z) / z ** 2, g1, dg1, 0, two_pi), 2j * mp.pi)
gm, dgm = circle(1, 0.7)
mean = mp.quad(lambda t: (1 + 0.7 * mp.e ** (1j * t)) ** 2, [0, two_pi]) / two_pi
check("CA05.5 mean value of z^2 on circle about 1", mean, 1, 1e-12)
check("CA05.7 max |z^2+1| on unit disk", max(abs(r * np.exp(1j * t)) ** 0 * abs((r * np.exp(1j * t)) ** 2 + 1)
                                              for r in np.linspace(0, 1, 101) for t in np.linspace(0, 6.2832, 721)), 2, 1e-5)
check("CA05.8 grad u . grad v = 0 (u=x^2-y^2, v=2xy)", complex(sp.simplify(sp.diff(x**2 - y**2, x) * sp.diff(2*x*y, x) + sp.diff(x**2 - y**2, y) * sp.diff(2*x*y, y))), 0)

# ---------------- CA06 ----------------
n = 400
ratio = mp.factorial(n + 1) / mp.mpf(n + 1) ** (n + 1) * mp.mpf(n) ** n / mp.factorial(n)
check("CA06.1 radius of sum n!/n^n z^n (1/ratio -> e)", 1 / ratio, mp.e, 5e-3)
zz = sp.symbols("z")
check("CA06.2 series 1/(1+z^2)", complex(sp.series(1 / (1 + zz ** 2), zz, 0, 8).removeO().subs(zz, 0.1)), 1 / (1 + 0.01), 1e-6)
print("     CA06.7 z cot z =", sp.series(zz * sp.cot(zz), zz, 0, 6))
print("     CA06.6 e^z/z^3 =", sp.series(sp.exp(zz) / zz ** 3, zz, 0, 2))
print("     CA06.8 z - sin z =", sp.series(zz - sp.sin(zz), zz, 0, 6))
xx, tt = sp.symbols("xx tt")
print("     CA06.10 (1-2xt+t^2)^(-1/2) =", sp.simplify(sp.series((1 - 2 * xx * tt + tt ** 2) ** sp.Rational(-1, 2), tt, 0, 3).removeO()))
f3 = 1 / (zz * (zz - 1))
print("     CA06.3 1/(z(z-1)) 0<|z|<1:", sp.series(f3, zz, 0, 3))
# Laurent of 1/((z-1)(z-2)) in 1<|z|<2 (numeric check at z=1.5i)
zt = 1.5j
lau = -sum(zt ** k / 2 ** (k + 1) for k in range(0, 200)) - sum(zt ** (-k) for k in range(1, 200))
check("CA06.4 Laurent 1/((z-1)(z-2)) in 1<|z|<2", lau, 1 / ((zt - 1) * (zt - 2)), 1e-10)
zt = 3j
lau2 = sum(zt ** (-k) for k in range(2, 300))
check("CA06.3 Laurent 1/(z(z-1)) in |z|>1", lau2, 1 / (zt * (zt - 1)), 1e-10)

# ---------------- CA07 ----------------
print("     CA07.2 residues of 1/(z^2+1):", sp.residue(1 / (zz ** 2 + 1), zz, sp.I), sp.residue(1 / (zz ** 2 + 1), zz, -sp.I))
print("     CA07.3 residues:", sp.residue(sp.exp(zz) / zz ** 2, zz, 0), sp.residue(sp.exp(zz) / (zz - 1) ** 3, zz, 1))
print("     CA07.9 residue 1/(z^2+1)^2 at i:", sp.residue(1 / (zz ** 2 + 1) ** 2, zz, sp.I))
print("     CA07.6 residue sin z/z^4 at 0:", sp.residue(sp.sin(zz) / zz ** 4, zz, 0))
g3_, dg3_ = circle(0, 3)
check("CA07.4 oint_{|z|=3} (z+1)/(z^2-2z)", contour(lambda z: (z + 1) / (z ** 2 - 2 * z), g3_, dg3_, 0, two_pi), 2j * mp.pi)
g15, dg15 = circle(0, 1.5)
check("CA07.5 oint_{|z|=1.5} dz/(z^4+1)", contour(lambda z: 1 / (z ** 4 + 1), g15, dg15, 0, two_pi), 0, 1e-12)
check("CA07.6 oint_{|z|=1} sin z/z^4", contour(lambda z: mp.sin(z) / z ** 4, g1, dg1, 0, two_pi), -1j * mp.pi / 3)
check("CA07.7 oint_{|z|=1} cot z", contour(lambda z: mp.cot(z), g1, dg1, 0, two_pi), 2j * mp.pi)
g4, dg4 = circle(0, 4)
check("CA07.7 oint_{|z|=4} cot z", contour(lambda z: mp.cot(z), g4, dg4, 0, two_pi), 6j * mp.pi)
check("CA07.8 oint_{|z|=1} sin(1/z)", contour(lambda z: mp.sin(1 / z), g1, dg1, 0, two_pi), 2j * mp.pi)
gi, dgi = circle(1j, 1)
check("CA07.9 oint_{|z-i|=1} dz/(z^2+1)^2", contour(lambda z: 1 / (z ** 2 + 1) ** 2, gi, dgi, 0, two_pi), mp.pi / 2)
eps = 1e-6
for s in (+1, -1):
    r = np.sqrt((1 - 1j * s * eps) + 0j)
    print(f"     CA07.10 poles of 1/(k^2-m^2{'+' if s>0 else '-'}i eps), m=1: +-{r:.8f}")

# ---------------- CA08 ----------------
inf = mp.inf
check("CA08.1 int dx/(x^2+1)", mp.quad(lambda t: 1 / (t ** 2 + 1), [-inf, 0, inf]), mp.pi)
check("CA08.2 int dx/(x^2+1)^2", mp.quad(lambda t: 1 / (t ** 2 + 1) ** 2, [-inf, 0, inf]), mp.pi / 2)
a_, k_ = 1.3, 0.8
check("CA08.3 int cos(kx)/(x^2+a^2)", 2 * mp.quad(lambda t: mp.cos(k_ * t) / (t ** 2 + a_ ** 2), mp.linspace(0, 400, 801)) , mp.pi / a_ * mp.e ** (-k_ * a_), 2e-3)
check("CA08.3' same via quadosc", 2 * mp.quadosc(lambda t: mp.cos(k_ * t) / (t ** 2 + a_ ** 2), [0, inf], omega=k_), mp.pi / a_ * mp.e ** (-k_ * a_), 1e-8)
check("CA08.4 int x sin(kx)/(x^2+a^2)", 2 * mp.quadosc(lambda t: t * mp.sin(k_ * t) / (t ** 2 + a_ ** 2), [0, inf], omega=k_), mp.pi * mp.e ** (-k_ * a_), 1e-8)
check("CA08.5 int_0^inf dx/(x^4+1)", mp.quad(lambda t: 1 / (t ** 4 + 1), [0, inf]), mp.pi / (2 * mp.sqrt(2)))
check("CA08.6 int sin x / x", 2 * mp.quadosc(lambda t: mp.sin(t) / t, [0, inf], omega=1), mp.pi, 1e-8)
check("CA08.7 PV int cos x/(x-1) dx = -pi sin 1 (via symmetric form)", mp.quadosc(lambda s: (mp.cos(1 + s) - mp.cos(1 - s)) / s, [0, inf], omega=1), -mp.pi * mp.sin(1), 1e-8)
check("CA08.8 int_0^2pi dtheta/(2+cos)", mp.quad(lambda t: 1 / (2 + mp.cos(t)), [0, mp.pi, two_pi]), two_pi / mp.sqrt(3))
# retarded Green function with finite epsilon: theta(t) e^{-eps t} sin(w0 t)/w0
w0, epsl, tt_ = 1.0, 0.3, 2.0
def integrand(w):
    return mp.e ** (-1j * w * tt_) / (w0 ** 2 - (w + 1j * epsl) ** 2)
L = 3000
val = mp.quad(integrand, mp.linspace(-L, L, 6001)) / two_pi
check("CA08.9 retarded G(t=2), finite eps (truncated at L=3000)", val, mp.e ** (-epsl * tt_) * mp.sin(w0 * tt_) / w0, 2e-3)
val_neg = mp.quad(lambda w: mp.e ** (1j * w * tt_) / (w0 ** 2 - (w + 1j * epsl) ** 2), mp.linspace(-L, L, 6001)) / two_pi
check("CA08.9 retarded G(t=-2) = 0", val_neg, 0, 2e-3)
# Kramers-Kronig for chi = 1/(w0^2 - w^2 - i gamma w)
gam, wv = 0.5, 0.7
chi = lambda w: 1 / (w0 ** 2 - w ** 2 - 1j * gam * w)
pv = mp.quad(lambda s: (chi(wv + s).imag - chi(wv - s).imag) / s, [0, 1, 5, 50, inf]) / mp.pi
check("CA08.10 KK: Re chi = (1/pi) PV int Im chi/(w'-w)", pv, chi(wv).real, 1e-8)
pv2 = -mp.quad(lambda s: (chi(wv + s).real - chi(wv - s).real) / s, [0, 1, 5, 50, inf]) / mp.pi
check("CA08.10 KK: Im chi = -(1/pi) PV int Re chi/(w'-w)", pv2, chi(wv).imag, 1e-8)
poles = [(-1j * gam + s * np.sqrt(4 * w0 ** 2 - gam ** 2)) / 2 for s in (+1, -1)]
print("     CA08.10 poles of chi (denominator w^2 + i gam w - w0^2 = 0):", poles, "-> Im<0 both:", all(p.imag < 0 for p in poles))

# ---------------- CA09 ----------------
# Feynman propagator and the identity G_F = (G_ret+G_adv)/2 + i cos(w0 t)/(2 w0)
for t in (-1.7, 0.9, 2.4):
    GF = 1j / (2 * w0) * np.exp(-1j * w0 * abs(t))
    Gr = (t > 0) * np.sin(w0 * t) / w0
    Ga = -(t < 0) * np.sin(w0 * t) / w0
    check(f"CA09.3 G_F = (Gr+Ga)/2 + i cos/(2w0), t={t}", GF, 0.5 * (Gr + Ga) + 1j * np.cos(w0 * t) / (2 * w0), 1e-12)
    check(f"CA09.2 G_ret - G_adv = sin(w0 t)/w0, t={t}", Gr - Ga, np.sin(w0 * t) / w0, 1e-12)
# Sokhotski with finite eps: int e^{-x^2}/(x - i eps) dx = i pi e^{eps^2} erfc(eps)
for e_ in (1e-2, 1e-3):
    val = mp.quad(lambda xv: mp.e ** (-xv ** 2) / (xv - 1j * e_), [-inf, -1, -e_, 0, e_, 1, inf])
    check(f"CA09.4 Sokhotski eps={e_}", val, 1j * mp.pi * mp.e ** (e_ ** 2) * mp.erfc(e_), 1e-8)
    print(f"     -> approaches i*pi = {1j*mp.pi}")
# Euclidean propagator
check("CA09.6 int dw/(2pi) e^{i w tau}/(w0^2+w^2), tau=1.3", mp.quadosc(lambda w: mp.cos(w * 1.3) / (w0 ** 2 + w ** 2), [0, inf], omega=1.3) * 2 / two_pi, mp.e ** (-w0 * 1.3) / (2 * w0), 1e-8)
# Yukawa radial integral
mu, r_ = 0.9, 1.4
check("CA09.7 int_0^inf k sin(kr)/(k^2+mu^2) = (pi/2) e^{-mu r}", mp.quadosc(lambda kk: kk * mp.sin(kk * r_) / (kk ** 2 + mu ** 2), [0, inf], omega=r_), mp.pi / 2 * mp.e ** (-mu * r_), 1e-8)
check("CA09.7 Yukawa prefactor 2/(pi r) * (pi/2) e^{-mu r} = e^{-mu r}/r", 2 / (mp.pi * r_) * mp.pi / 2 * mp.e ** (-mu * r_), mp.e ** (-mu * r_) / r_, 1e-12)


# ---------------- extra checks added after writing the modules ----------------
# CA04.7: positively oriented square with vertices +-2 +- 2i
def square_integral(f):
    pts = [-2 - 2j, 2 - 2j, 2 + 2j, -2 + 2j, -2 - 2j]
    tot = 0
    for a, b in zip(pts[:-1], pts[1:]):
        tot += mp.quad(lambda t: f(a + (b - a) * t) * (b - a), [0, 1])
    return tot
check("CA04.7 square, z0 = 1/2 inside", square_integral(lambda z: 1 / (z - 0.5)), 2j * mp.pi, 1e-12)
check("CA04.7 square, z0 = 3 outside", square_integral(lambda z: 1 / (z - 3)), 0, 1e-12)

# CA08.6: int e^{ikx}/(k^2 - m^2 +- i eps) dk at finite eps, compared with the exact finite-eps closed form
m_, eps_, x_ = 1.0, 0.3, 1.5
L = 3000
for sgn in (+1, -1):
    val = mp.quad(lambda k: mp.e ** (1j * k * x_) / (k ** 2 - m_ ** 2 + 1j * sgn * eps_), mp.linspace(-L, L, 6001))
    if sgn > 0:
        w = mp.sqrt(m_ ** 2 - 1j * eps_)
        exact = -1j * mp.pi / w * mp.e ** (-1j * w * abs(x_))
    else:
        w = mp.sqrt(m_ ** 2 + 1j * eps_)
        exact = 1j * mp.pi / w * mp.e ** (1j * w * abs(x_))
    check(f"CA08.6 closed form at finite eps, sign {'+' if sgn > 0 else '-'}i eps (truncated at L=3000)", val, exact, 2e-3)

# CA08.9 value quoted in the text
check("CA08.9 pi*sin(1) = 2.6436", mp.pi * mp.sin(1), 2.64355906408146, 1e-12)
# CA08.8 value of chi quoted in the text
check("CA08.8 chi(0.7) = 1.3330 + 0.9148 i", chi(0.7), 1.3329848405645583 + 0.9147935180345007j, 1e-12)

print()
print("ALL CHECKS PASSED" if not FAILS else f"FAILED: {FAILS}")
