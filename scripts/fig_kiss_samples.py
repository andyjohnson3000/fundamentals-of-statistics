"""The population-vs-sample thought experiment. If the true proportion
of couples turning right were 0.35 or 0.65, what would the sample
proportion look like in samples of size n = 3 and n = 124? Exact binomial
distribution of Rbar_n."""
from _style import *

fig, axes = plt.subplots(1, 2, figsize=FULL)
observed = 80 / 124
for ax, n in zip(axes, [3, 124]):
    k = np.arange(n + 1)
    for p, col, ls in [(0.35, ORANGE, DASHES[1]), (0.65, BLUE, DASHES[0])]:
        pm = binom_pmf(n, p)
        width = 0.9 / n if n > 3 else 0.12
        if n == 3:
            ax.bar(k / n + (0.03 if p == 0.65 else -0.03), pm, width=0.06, color=col, alpha=0.75, lw=0,
                   label=rf"$p = {p}$")
        else:
            ax.bar(k / n, pm, width=width, color=col, alpha=0.6, lw=0, label=rf"$p = {p}$")
    ax.axvline(observed, color=INK, lw=1.0, ls=":")
    ax.set_ylim(0, (0.6 if n == 3 else ax.get_ylim()[1] * 1.08))
    if n == 124:
        ax.annotate(r"observed $\bar{R}_n = 0.645$", (observed, ax.get_ylim()[1] * 0.97),
                    xytext=(5, 0), textcoords="offset points", fontsize=7.5, color=INK, va="top")
    ax.set_title(rf"samples of size $n = {n}$")
    ax.set_xlabel(r"sample proportion $\bar{R}_n$")
    ax.set_xlim(-0.08, 1.08)
    ax.legend(loc="upper left" if n == 124 else "upper center")
axes[0].set_ylabel("probability")
save(fig, "fig_kiss_samples")
