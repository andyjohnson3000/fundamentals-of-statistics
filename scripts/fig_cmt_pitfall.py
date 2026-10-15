"""What the continuous mapping theorem does not give you. Take f(x) = x^2 in
the kiss model (p = 0.645, n = 124); p^2 is the probability that two
independent couples both turn right. Left: f applied to the magnified error,
(sqrt(n)(Rbar - p))^2, which the CMT says converges to (Gaussian)^2, a
chi-squared shape. True, and not what you want. Right: the magnified error of
the transformed estimator, sqrt(n)(Rbar^2 - p^2), which the delta method says
is Gaussian with variance (2p)^2 p(1-p). Both drawn from the exact Binomial
distribution of n Rbar, as densities (mass divided by the local spacing of
the lattice)."""
from _style import *

p, n = 0.645, 124
k = np.arange(n + 1)
pm = binom_pmf(n, p)
rbar = k / n
sigma = math.sqrt(p * (1 - p))


def lattice_density(ax, y, mass, color, label):
    """Bars of height mass/width on the (unequally spaced, increasing) lattice y."""
    mids = 0.5 * (y[1:] + y[:-1])
    left = np.concatenate([[y[0] - (mids[0] - y[0])], mids])
    right = np.concatenate([mids, [y[-1] + (y[-1] - mids[-1])]])
    width = right - left
    ax.bar(left, mass / width, width=width, align="edge", color=color, alpha=0.7, lw=0, label=label)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

# left: (sqrt(n)(Rbar - p))^2 ; the map folds the lattice, so bin the mass
# (the limit is sigma^2 chi^2_1 with sigma^2 = p(1-p); the formula is in the caption)
z2 = (math.sqrt(n) * (rbar - p)) ** 2
edges = np.arange(0, 2.6, 0.1)
mass, _ = np.histogram(z2, bins=edges, weights=pm)
ax1.bar(edges[:-1], mass / 0.1, width=0.1, align="edge", color=AQUA, alpha=0.7, lw=0, label="exact (Binomial)")
xx = np.linspace(0.004, 2.5, 800)
# density of sigma^2 * chi^2_1
ax1.plot(xx, np.exp(-xx / (2 * sigma ** 2)) / np.sqrt(2 * math.pi * sigma ** 2 * xx), color=INK, lw=1.2,
         label="CMT limit")
ax1.set_xlim(0, 2.5)
ax1.set_ylim(0, 6.5)
ax1.set_title(r"$f\!\left(\sqrt{n}(\bar{R}_n - p)\right)$ with $f(x) = x^2$")
ax1.set_xlabel("value")
ax1.set_ylabel("density")
ax1.legend(loc="upper right")   # upper right is empty: the curve is tall only near 0

# right: sqrt(n)(Rbar^2 - p^2)
# (the limit is Gauss(0, (2p)^2 p(1-p)), sd = 0.62; the formula is in the caption)
y2 = math.sqrt(n) * (rbar ** 2 - p ** 2)
lattice_density(ax2, y2, pm, BLUE, "exact (Binomial)")
sd = 2 * p * sigma
xx = np.linspace(-3, 3, 500)
ax2.plot(xx, norm_pdf(xx, 0, sd), color=ORANGE, lw=1.3, label="delta-method limit")
ax2.set_xlim(-2.5, 2.5)
ax2.set_ylim(0, 0.85)   # headroom so the legend sits above the peak
ax2.set_title(r"$\sqrt{n}\left(\bar{R}_n^2 - p^2\right)$")
ax2.set_xlabel("value")
ax2.legend(loc="upper left")
save(fig, "fig_cmt_pitfall")
