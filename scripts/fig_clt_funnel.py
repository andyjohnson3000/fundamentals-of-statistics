"""The Law of Large Numbers and the Central Limit Theorem in one picture: the
funnel. Twenty realizations of the running sample mean of Bern(0.645) draws
(the kiss model), with the curves p +/- 1.96 sqrt(p(1-p)/n) and
p +/- 3 sqrt(p(1-p)/n). The funnel narrows like 1/sqrt(n): that is the Law of
Large Numbers. At any fixed n about 5% of the paths are outside the inner
funnel and almost none outside the outer one: that is the CLT's stochastic
bound |Xbar_n - mu| <= 3 sigma/sqrt(n), and the inner funnel is the recipe for
every confidence interval."""
from _style import *

p = 0.645
sigma = math.sqrt(p * (1 - p))
N, paths = 400, 20
n = np.arange(1, N + 1)
r = rng(31)
fig, ax = plt.subplots(figsize=(6.0, 3.2))
outside = 0
total = 0
for j in range(paths):
    draws = r.binomial(1, p, size=N)
    xbar = np.cumsum(draws) / n
    ax.plot(n, xbar, color=BLUE, lw=0.6, alpha=0.55)
    sel = n >= 30
    outside += int(np.sum(np.abs(xbar[sel] - p) > 1.96 * sigma / np.sqrt(n[sel])))
    total += int(sel.sum())
ax.plot(n, p + 1.96 * sigma / np.sqrt(n), color=ORANGE, lw=1.3)
ax.plot(n, p - 1.96 * sigma / np.sqrt(n), color=ORANGE, lw=1.3)
ax.plot(n, p + 3 * sigma / np.sqrt(n), color=INK, lw=1.0, ls="--")
ax.plot(n, p - 3 * sigma / np.sqrt(n), color=INK, lw=1.0, ls="--")
ax.axhline(p, color=GRAY, lw=0.7)
ax.text(140, 0.515, r"$p \pm 1.96\,\sigma/\sqrt{n}$ (95%)", ha="left", va="top", fontsize=8, color=ORANGE)
ax.text(140, 0.455, r"$p \pm 3\,\sigma/\sqrt{n}$ (99.7%)", ha="left", va="top", fontsize=8, color=INK)
ax.axvline(124, color=GRAY, lw=0.6, ls=":")
ax.text(126, 0.38, r"$n = 124$", fontsize=8, color=INK)
ax.set_xlim(1, N)
ax.set_ylim(0.35, 0.95)
ax.set_xlabel(r"$n$")
ax.set_ylabel(r"running proportion $\bar{R}_n$")
ax.set_title(rf"{paths} realizations of $\bar{{R}}_n$, $p = {p}$, inside a shrinking funnel")
save(fig, "fig_clt_funnel")
print("fraction outside 95% funnel for n >= 30:", outside / total)
