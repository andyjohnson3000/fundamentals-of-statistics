"""A statistic partitions the sample space. For n = 2 observations the sample
space is the plane; the level sets of the sample mean are the lines
x1 + x2 = const (left) and the level sets of the maximum are L-shapes (right).
Two samples on the same level set are indistinguishable to anyone who only
sees the statistic."""
from _style import *

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, sharey=True, layout="constrained")
lim = 6

for t in np.arange(1, 11, 1):
    ax1.plot([0, t], [t, 0], color=BLUE, lw=0.8, alpha=0.8)
ax1.plot([1.5, 4.5], [4.5, 1.5], "o", ms=5, color=ORANGE, mec="white", mew=0.5, zorder=5)
# No label fits between the level lines without crossing one (the lines are
# 0.7 units apart, a label is 1.5 units wide), so the coordinates of the two
# points and "both have xbar = 3" are stated in the caption instead.
ax1.set_xlim(0, lim); ax1.set_ylim(0, lim)
ax1.set_xlabel(r"$x_1$"); ax1.set_ylabel(r"$x_2$")
ax1.set_title(r"Level sets of $T = \bar{X}_2$: lines $x_1 + x_2 = 2t$")
ax1.set_aspect("equal")

for t in np.arange(1, 7, 1):
    ax2.plot([t, t, 0], [0, t, t], color=AQUA, lw=0.8, alpha=0.9)
ax2.plot([1.5, 4.5], [4.5, 4.5], "o", ms=5, color=ORANGE, mec="white", mew=0.5, zorder=5)
# point labels in the strip between the L at 4 and the L at 4.5; the second one
# sits to the left of its point because the L at 5 runs just right of it
ax2.annotate(r"$(1.5, 4.5)$", (1.5, 4.5), xytext=(0, -12), textcoords="offset points", ha="center", fontsize=8, color=INK)
ax2.annotate(r"$(4.5, 4.5)$", (4.5, 4.5), xytext=(-8, -12), textcoords="offset points", ha="right", fontsize=8, color=INK)
# in the empty strip between the L at 4.5 and the L at 5, with a leader to the L it names
ax2.annotate(r"both have $\max = 4.5$", xy=(3.6, 4.52), xytext=(0.25, 4.76), ha="left", va="center",
             fontsize=7.5, color=INK,
             arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6, shrinkB=2, relpos=(1, 0.5)))
ax2.set_xlim(0, lim); ax2.set_ylim(0, lim)
ax2.set_xlabel(r"$x_1$")
ax2.set_title(r"Level sets of $T = \max(X_1, X_2)$: L-shapes")
ax2.set_aspect("equal")
save(fig, "fig_statistic_partition")
