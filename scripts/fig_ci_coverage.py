"""What 'asymptotic level 95%' buys at a finite n: the exact coverage
probability P_p(I contains p) of the three intervals, as a function of the
true p, computed from the binomial distribution of n Rbar_n (no simulation).
Left n = 124 (the kiss experiment), right n = 20. The conservative interval
over-covers away from p = 1/2; the plug-in (Wald) interval under-covers near
the edges, badly at small n; the solve (Wilson) interval stays near 95%
everywhere. The saw teeth are real: coverage jumps each time an endpoint of
one of the n + 1 possible intervals crosses p."""
from _style import *

z = 1.959964


def intervals(n):
    k = np.arange(n + 1)
    ph = k / n
    cons = np.stack([ph - z / (2 * math.sqrt(n)), ph + z / (2 * math.sqrt(n))], 1)
    plug = np.stack([ph - z * np.sqrt(ph * (1 - ph) / n), ph + z * np.sqrt(ph * (1 - ph) / n)], 1)
    A = 1 + z * z / n
    B = -(2 * ph + z * z / n)
    C = ph * ph
    D = np.sqrt(np.maximum(B * B - 4 * A * C, 0))
    solve = np.stack([(-B - D) / (2 * A), (-B + D) / (2 * A)], 1)
    return cons, plug, solve


def coverage(n, ivals, pgrid):
    out = np.zeros_like(pgrid)
    for j, p in enumerate(pgrid):
        pm = binom_pmf(n, p)
        hit = (ivals[:, 0] <= p) & (p <= ivals[:, 1])
        out[j] = pm[hit].sum()
    return out


pgrid = np.linspace(0.005, 0.995, 991)
fig, axes = plt.subplots(1, 2, figsize=FULL, sharey=True)
for ax, n in zip(axes, (124, 20)):
    cons, plug, solve = intervals(n)
    for iv, name, col, ls in [(cons, "conservative", GRAY, DASHES[1]), (plug, "plug-in", AQUA, DASHES[0]), (solve, "solve", BLUE, DASHES[0])]:
        ax.plot(pgrid, coverage(n, iv, pgrid), color=col, lw=1.0 if name != "plug-in" else 1.2, ls=ls, label=name)
    ax.axhline(0.95, color=INK, lw=0.8, ls=":")
    ax.set_title(rf"exact coverage, $n = {n}$")
    ax.set_xlabel(r"true $p$")
    ax.set_xlim(0, 1)
axes[0].set_ylim(0.70, 1.0)
axes[0].set_ylabel(r"$\mathbb{P}_p(\mathcal{I} \ni p)$")
axes[0].legend(loc="lower left", fontsize=7)
axes[0].axvline(0.645, color=INK, lw=0.5, ls=":")
axes[0].text(0.655, 0.705, r"$p = 0.645$", fontsize=7.5, color=INK, ha="left")
save(fig, "fig_ci_coverage")
cons, plug, solve = intervals(124)
for name, iv in [("cons", cons), ("plug", plug), ("solve", solve)]:
    c = coverage(124, iv, np.array([0.645, 0.05, 0.5]))
    print(name, c)
