"""Conditional expectation for two dice: the 36 equally likely outcomes
plotted as (first die x, sum y), and the conditional means E[Y | X = x] =
x + 3.5 (orange); the gray band marks the six outcomes with X = 4."""
from _style import *

fig, ax = plt.subplots(figsize=(3.6, 2.7), layout="constrained")
for x in range(1, 7):
    ax.plot([x] * 6, [x + d for d in range(1, 7)], "o", color=BLUE, ms=4)
ax.axvspan(3.6, 4.4, color=GRAY, alpha=0.15, lw=0)
xs = np.arange(1, 7)
ax.plot(xs, xs + 3.5, "o-", color=ORANGE, ms=4.5, lw=1.1, zorder=5)
ax.set_xticks(xs); ax.set_yticks(range(2, 13, 2))
ax.set_xlim(0.5, 6.5); ax.set_ylim(1, 13)
ax.set_xlabel("first die $x$"); ax.set_ylabel("sum $y$")
ax.set_title("conditional means of the sum")
save(fig, "fig_tk_condexp")
