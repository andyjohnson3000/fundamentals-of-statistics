"""Exact frequentist coverage of two 95% intervals for a proportion, as a
function of the true p: the solve (Wilson) interval of Chapter 8 (blue,
solid, left) and the equal-tailed Jeffreys interval, the 2.5% and 97.5%
points of the posterior Beta(S + 1/2, n - S + 1/2) (orange, right), with the nominal
0.95 dotted, at n = 20, one interval per side. Computed from the binomial
distribution of S, no simulation."""
from _style import *
from scipy import stats

z = 1.959964


def intervals(n):
    k = np.arange(n + 1)
    ph = k / n
    A = 1 + z * z / n
    B = -(2 * ph + z * z / n)
    C = ph * ph
    D = np.sqrt(np.maximum(B * B - 4 * A * C, 0))
    solve = np.stack([(-B - D) / (2 * A), (-B + D) / (2 * A)], 1)
    jeff = np.stack([stats.beta.ppf(0.025, k + 0.5, n - k + 0.5), stats.beta.ppf(0.975, k + 0.5, n - k + 0.5)], 1)
    return solve, jeff


def coverage(n, iv, pgrid):
    out = np.zeros_like(pgrid)
    for j, p in enumerate(pgrid):
        pm = binom_pmf(n, p)
        hit = (iv[:, 0] <= p) & (p <= iv[:, 1])
        out[j] = pm[hit].sum()
    return out


def grid(iv, lo=0.005, hi=0.995):
    """A fine grid plus the points just either side of every interval
    endpoint, where coverage jumps, so the plotted minima are exact."""
    ends = iv.ravel()
    ends = ends[(ends > lo) & (ends < hi)]
    return np.unique(np.concatenate([np.linspace(lo, hi, 991), ends - 1e-9, ends + 1e-9]))


n = 20
solve, jeff = intervals(n)
fig, axes = plt.subplots(1, 2, figsize=FULL, sharey=True, layout="constrained")
for ax, iv, col, ls, title in ((axes[0], solve, BLUE, DASHES[0], "solve (Wilson) interval"),
                               (axes[1], jeff, ORANGE, DASHES[0], "Jeffreys interval")):
    pgrid = grid(iv)
    ax.plot(pgrid, coverage(n, iv, pgrid), color=col, lw=1.0, ls=ls)
    ax.axhline(0.95, color=INK, lw=0.8, ls=":")
    ax.set_title(title + r", $n = 20$")
    ax.set_xlabel(r"true $p$")
    ax.set_xlim(0, 1)
axes[0].set_ylim(0.80, 1.0)
axes[0].set_ylabel(r"$\mathbb{P}_p(\mathcal{I} \ni p)$")
save(fig, "fig_jeffreys_coverage")
for name, iv in (("solve", solve), ("jeff", jeff)):
    pgrid = grid(iv)
    c = coverage(n, iv, pgrid)
    mid = (pgrid >= 0.1) & (pgrid <= 0.9)
    print(n, name, "min on plot", c.min().round(4), "at", pgrid[c.argmin()], "mean", c.mean().round(4), "min mid", c[mid].min().round(4))
