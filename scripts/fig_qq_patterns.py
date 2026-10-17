"""How to read a QQ plot: four samples of n = 200 plotted against Gaussian
quantiles. Each point is (Phi^{-1}((i - 1/2)/n), X_(i)); the black line
passes through the points at the first and third quartiles. Top left:
Student's t with 3 degrees of freedom (heavy tails). Top right: Unif(0, 1)
(light tails). Bottom left: Expo(1) (skewed right). Bottom right: minus an
Expo(1) (skewed left)."""
from _style import *

g = rng(275)  # a t sample whose two extremes are both moderate, so the S shape is visible
erf = np.frompyfunc(math.erf, 1, 1)


def Phi(x):
    return 0.5 * (1 + erf(np.asarray(x, float) / math.sqrt(2)).astype(float))


def Phi_inv(p):
    p = np.asarray(p, float)
    lo, hi = np.full(p.shape, -9.0), np.full(p.shape, 9.0)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        below = Phi(mid) < p
        lo = np.where(below, mid, lo)
        hi = np.where(below, hi, mid)
    return 0.5 * (lo + hi)


def qq(ax, x, title):
    x = np.sort(x)
    n = len(x)
    z = Phi_inv((np.arange(1, n + 1) - 0.5) / n)
    q1, q3 = np.quantile(x, [0.25, 0.75])
    z1, z3 = Phi_inv(np.array([0.25, 0.75]))
    slope = (q3 - q1) / (z3 - z1)
    zz = np.linspace(-3.2, 3.2, 10)
    ax.plot(zz, q1 + slope * (zz - z1), color=INK, lw=1.0)
    ax.plot(z, x, "o", ms=2.4, color=BLUE, alpha=0.8, mec="none")
    ax.set_xlim(-3.2, 3.2)
    ax.set_title(title)


n = 200
fig, axes = plt.subplots(2, 2, figsize=(6.0, 4.3), layout="constrained")
qq(axes[0, 0], g.standard_t(3, n), "heavy tails")
qq(axes[0, 1], g.random(n), "light tails")
qq(axes[1, 0], g.exponential(1.0, n), "skewed right")
qq(axes[1, 1], -g.exponential(1.0, n), "skewed left")
for ax in axes[1, :]:
    ax.set_xlabel("Gaussian quantile")
for ax in axes[:, 0]:
    ax.set_ylabel("sample quantile")
save(fig, "fig_qq_patterns")
