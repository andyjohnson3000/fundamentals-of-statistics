"""The trinity of inference on one axis. All three statements about the
kiss experiment are statements about where p sits on the line: the estimate
p-hat = 0.645 (a point), the 95% confidence interval [0.56, 0.73] (a bracket
around it), and the test of p = 1/2 (the null value, and the one-sided
threshold 72/124 = 0.581 above which the data count as evidence that
p > 1/2, with the rejection region shaded)."""
from _style import *

n, k = 124, 80
phat = k / n
ci = (0.561, 0.729)
thr = 72 / n

fig, ax = plt.subplots(figsize=(6.0, 2.0))
ax.set_xlim(0.40, 0.94)
ax.set_ylim(-0.2, 3.4)
ax.axis("off")

# the axis line
ax.annotate("", xy=(0.925, 0), xytext=(0.40, 0), arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=0.8))
for t in np.arange(0.40, 0.91, 0.1):
    ax.plot([t, t], [-0.08, 0.08], color=GRAY, lw=0.7)
    ax.text(t, -0.16, f"{t:.1f}", ha="center", va="top", fontsize=8, color=INK)
ax.text(0.93, -0.16, r"$p$", ha="left", va="top", fontsize=9, color=INK)

# 3. test: rejection region and threshold
ax.plot([thr, 0.92], [1.0, 1.0], color=ORANGE, lw=5, alpha=0.35, solid_capstyle="butt")
ax.plot([0.5, 0.5], [0.7, 1.3], color=INK, lw=1.2)
ax.text(0.5, 1.42, r"null value $p = \frac{1}{2}$", ha="center", fontsize=8, color=INK)
ax.plot([thr, thr], [0.75, 1.25], color=ORANGE, lw=1.2)
ax.text(thr + 0.005, 0.62, r"threshold $72/124 = 0.581$", ha="left", va="top", fontsize=8, color=INK)
ax.text(0.80, 1.18, "reject $p = \\frac{1}{2}$ if $\\bar{R}_n$ lands here", ha="center", va="bottom", fontsize=8, color=INK)
ax.text(0.405, 1.0, "test", ha="left", va="center", fontsize=8.5, color=INK, fontweight="bold")

# 2. confidence interval
ax.plot(list(ci), [2.0, 2.0], color=BLUE, lw=2.4, solid_capstyle="butt")
for c in ci:
    ax.plot([c, c], [1.85, 2.15], color=BLUE, lw=1.4)
ax.text(ci[1] + 0.008, 2.0, r"95% interval $[0.56, 0.73]$", ha="left", va="center", fontsize=8, color=INK)
ax.text(0.405, 2.0, "interval", ha="left", va="center", fontsize=8.5, color=INK, fontweight="bold")

# 1. estimate
ax.plot(phat, 3.0, "o", ms=7, color=ORANGE, mec="white", mew=0.6, zorder=5)
ax.text(phat + 0.012, 3.0, r"estimate $\hat{p} = 0.645$", ha="left", va="center", fontsize=8, color=INK)
ax.text(0.405, 3.0, "estimate", ha="left", va="center", fontsize=8.5, color=INK, fontweight="bold")

# dotted guide through the estimate
ax.plot([phat, phat], [0, 2.85], color=ORANGE, lw=0.6, ls=":")
save(fig, "fig_trinity_axis")
