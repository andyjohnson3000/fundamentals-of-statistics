"""P(|Rbar_n - p| >= eps) in the kiss experiment (p = 0.645, eps = 0.084): the exact
binomial probability, the CLT approximation, and the Chebyshev and Hoeffding
upper bounds, as functions of n."""
from _style import *

p, eps = 0.645, 0.084
sd = math.sqrt(p * (1 - p))
ns = np.arange(4, 401)

exact, clt = [], []
for n in ns:
    pmf = binom_pmf(n, p)
    k = np.arange(n + 1)
    exact.append(pmf[np.abs(k / n - p) >= eps].sum())
    clt.append(2 * (1 - norm_cdf(eps * math.sqrt(n) / sd)))
exact, clt = np.array(exact), np.array(clt)
cheb = np.minimum(1, p * (1 - p) / (ns * eps ** 2))
hoef = np.minimum(1, 2 * np.exp(-2 * ns * eps ** 2))

fig, ax = plt.subplots(figsize=(5.2, 3.0))
ax.plot(ns, cheb, color=YELLOW, ls=DASHES[3], lw=1.6, label="Chebyshev bound")
ax.plot(ns, hoef, color=ORANGE, ls=DASHES[1], label="Hoeffding bound")
ax.plot(ns, exact, color=BLUE, ls=DASHES[0], lw=0.9, alpha=0.8, label="exact (binomial)")
ax.plot(ns, clt, color=AQUA, ls=DASHES[2], lw=1.6, label="CLT approximation")
n0 = 124
ax.axvline(n0, color=GRAY, lw=0.6, ls=":")
for val, name in [(cheb[n0 - 4], "Chebyshev"), (hoef[n0 - 4], "Hoeffding"), (exact[n0 - 4], "exact")]:
    ax.plot(n0, val, "o", ms=3.5, color=INK, zorder=5)
    ax.annotate(f"{val:.2f}", (n0, val), xytext=(5, 0), textcoords="offset points",
                fontsize=7.5, color=INK, va="center")
ax.text(n0, 1.02, r"$n = 124$", ha="center", fontsize=8, color=INK)
ax.set_xlabel(r"sample size $n$")
ax.set_ylabel(r"$\Pr(|\bar{R}_n - p| \geq 0.084)$")
ax.set_ylim(0, 1.08)
ax.legend(loc="upper right")
save(fig, "fig_bounds_vs_truth")
