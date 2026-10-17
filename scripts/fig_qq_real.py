"""QQ plots against Gaussian quantiles, each with the line through the
points at the first and third quartiles. Left: a simulated sample of 66
standard Gaussians, for calibration. Middle: Newcomb's 66 measurements of
the passage time of light (1882, third series; in nanoseconds above
24,800; data/newcomb.csv, from Stigler, Annals of Statistics, 1977),
with the two low values -44 and -2 marked. Right: the 272 waiting times
between eruptions of Old Faithful (minutes)."""
from _style import *
import csv

g = rng(66)
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


def read(name, col):
    with open(os.path.join(os.path.dirname(HERE), "data", name)) as f:
        return np.array([float(r[col]) for r in csv.DictReader(f)])


def qq(ax, x, title):
    x = np.sort(x)
    n = len(x)
    z = Phi_inv((np.arange(1, n + 1) - 0.5) / n)
    q1, q3 = np.quantile(x, [0.25, 0.75])
    z1, z3 = Phi_inv(np.array([0.25, 0.75]))
    slope = (q3 - q1) / (z3 - z1)
    zz = np.linspace(-3.0, 3.0, 10)
    ax.plot(zz, q1 + slope * (zz - z1), color=INK, lw=1.0)
    ax.plot(z, x, "o", ms=2.6, color=BLUE, alpha=0.85, mec="none")
    ax.set_xlim(-3.0, 3.0)
    ax.set_title(title)
    ax.set_xlabel("Gaussian quantile")
    return z, x


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(6.0, 2.6), layout="constrained")
qq(ax1, g.standard_normal(66), "Gaussian, $n = 66$")
ax1.set_ylabel("sample quantile")
z, x = qq(ax2, read("newcomb.csv", "measurement"), "Newcomb, $n = 66$")
note(ax2, "$-44$", (z[0] + 0.08, x[0]), (-1.2, -40), ha="left")
note(ax2, "$-2$", (z[1] + 0.08, x[1]), (-1.0, -14), ha="left")
qq(ax3, read("old_faithful.csv", "waiting"), "Old Faithful, $n = 272$")
save(fig, "fig_qq_real")
