"""Why the definition of convergence in distribution excludes points where the
limit CDF jumps: T_n ~ Unif(5 - 1/(2n), 5 + 1/(2n)) converges to the constant 5,
but F_n(5) = 1/2 for every n while F(5) = 1."""
from _style import *

fig, ax = plt.subplots(figsize=(4.4, 2.8))
t = np.linspace(4.2, 5.8, 2000)
for k, n in enumerate([1, 2, 5, 20]):
    a, b = 5 - 1 / (2 * n), 5 + 1 / (2 * n)
    F = np.clip((t - a) / (b - a), 0, 1)
    ax.plot(t, F, color=SERIES[k], ls=DASHES[k], label=rf"$F_n$, $n={n}$")
# limit: CDF of the constant 5
ax.plot([4.2, 5], [0, 0], color=INK, lw=1.6)
ax.plot([5, 5.8], [1, 1], color=INK, lw=1.6)
ax.plot(5, 1, "o", ms=4, color=INK)
ax.plot(5, 0, "o", ms=4, mfc="white", mec=INK)
ax.plot(5, 0.5, "s", ms=5, color=ORANGE, mec="white", zorder=5)
ax.annotate(r"every $F_n(5) = 1/2$, but $F(5) = 1$", (5, 0.5), xytext=(14, -22),
            textcoords="offset points", fontsize=8, color=INK,
            arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6))
ax.text(5.55, 1.03, r"$F$ (limit)", fontsize=8, color=INK, va="bottom")
ax.set_xlabel(r"$t$")
ax.set_ylabel(r"CDF")
ax.set_ylim(-0.05, 1.12)
ax.legend(loc="center left", bbox_to_anchor=(0.0, 0.62))
save(fig, "fig_cdf_continuity_points")
