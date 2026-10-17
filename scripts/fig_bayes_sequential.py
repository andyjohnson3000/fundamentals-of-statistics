"""Updating one couple at a time, flat prior Beta(1, 1). The 80 right turns
and 44 left turns are put in a random order (the study does not report the
order, and the final posterior does not depend on it). Left: the posterior
mean (blue) and the band between the 2.5% and 97.5% points of the posterior
(light blue) after each couple, with the final proportion 0.645 (dotted).
Right: the posterior density after 0 (flat), 10, 40 and 124 couples."""
from _style import *

g = rng(2003)  # the year of the kiss study
n, S = 124, 80
x = np.array([1] * S + [0] * (n - S))
g.shuffle(x)
s = np.concatenate([[0], np.cumsum(x)])
k = np.arange(n + 1)
grid = np.linspace(0.0005, 0.9995, 4000)


def beta_quantiles(a, b, qs):
    f = beta_pdf(grid, a, b)
    c = np.concatenate([[0], np.cumsum(0.5 * (f[1:] + f[:-1]) * np.diff(grid))])
    c /= c[-1]
    return [float(np.interp(q, c, grid)) for q in qs]


a, b = 1 + s, 1 + k - s
mean = a / (a + b)
lo, hi = zip(*[beta_quantiles(ai, bi, (0.025, 0.975)) for ai, bi in zip(a, b)])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
ax1.fill_between(k, lo, hi, color=BLUE, alpha=0.18, lw=0)
ax1.plot(k, mean, color=BLUE, lw=1.3)
ax1.axhline(S / n, color=GRAY, lw=0.8, ls=DASHES[3])
ax1.set_xlim(0, n); ax1.set_ylim(0, 1)
ax1.set_xlabel("couples observed"); ax1.set_ylabel(r"$p$")
ax1.set_title("the posterior, couple by couple")

shown = [(0, GRAY, "-"), (10, ORANGE, DASHES[1]), (40, AQUA, DASHES[2]), (124, BLUE, DASHES[0])]
for m, c, ls in shown:
    ax2.plot(grid, beta_pdf(grid, 1 + s[m], 1 + m - s[m]), color=c, ls=ls, lw=1.3)
ax2.set_xlim(0, 1); ax2.set_ylim(0, 10.5)
ax2.set_xlabel(r"$p$"); ax2.set_ylabel("density")
ax2.set_title("four of the posteriors")
pk = lambda m: (s[m] / m if m else 0.5)
note(ax2, "no data", (0.12, 1.0), (0.05, 2.6), ha="left")
for m, xm, xy_text in ((10, 0.40, (0.04, 4.6)), (40, None, (0.10, 7.0)), (124, None, (0.80, 9.2))):
    am, bm = 1 + s[m], 1 + m - s[m]
    if xm is None:
        xm = (am - 1) / (am + bm - 2)
    ym = beta_pdf(np.array([xm]), am, bm)[0]
    note(ax2, f"{m} couples", (xm, ym), xy_text, ha="left")
save(fig, "fig_bayes_sequential")
for m in (1, 5, 10, 20, 40, 124):
    print(m, "rights", s[m], "post mean", round(mean[m], 3), "95% band", round(lo[m], 3), round(hi[m], 3))
