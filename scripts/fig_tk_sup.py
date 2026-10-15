"""Supremum and infimum. Left: the set {1 - 1/n : n = 1, 2, ...} has no
largest element, but 1 is its least upper bound, the supremum; every number
below 1 is exceeded by some member. Right: the function x e^{-x} on [0, 4]
attains its supremum (at x = 1) and its infimum (at x = 0): on a closed
interval a continuous function has a max and a min, and sup = max."""
from _style import *

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL)
n = np.arange(1, 31)
ax1.plot(1 - 1 / n, np.zeros_like(n, dtype=float), "o", ms=4, color=BLUE, mec="white", mew=0.3)
ax1.plot(1, 0, "o", ms=7, color=ORANGE, mec="white", mew=0.5, zorder=5)
ax1.annotate(r"$\sup = 1$, not a member", (1, 0), xytext=(-40, 30), textcoords="offset points", fontsize=8, color=INK,
             arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.6))
ax1.annotate(r"$\inf = \min = 0$", (0, 0), xytext=(-10, -30), textcoords="offset points", fontsize=8, color=INK,
             arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6))
for k in (2,):
    ax1.annotate(rf"$1 - \frac{{1}}{{{k}}}$", (1 - 1 / k, 0), xytext=(0, -16), textcoords="offset points", fontsize=7.5, color=INK, ha="center")
ax1.set_xlim(-0.08, 1.35); ax1.set_ylim(-0.6, 0.6); ax1.set_yticks([]); ax1.grid(False)
ax1.set_title(r"The set $\{1 - 1/n\}$: no largest element")

x = np.linspace(0, 4, 400)
ax2.plot(x, x * np.exp(-x), color=BLUE)
ax2.plot(1, math.exp(-1), "o", ms=5, color=ORANGE, mec="white", mew=0.4, zorder=5)
ax2.plot(0, 0, "o", ms=5, color=GRAY, mec="white", mew=0.4, zorder=5)
ax2.text(1.1, math.exp(-1) + 0.01, r"$\sup = \max = e^{-1}$ at $x = 1$", fontsize=8, color=INK)
ax2.text(0.1, 0.02, r"$\inf = \min = 0$", fontsize=8, color=INK)
ax2.set_xlabel(r"$x$"); ax2.set_title(r"$x e^{-x}$ on $[0, 4]$: both attained")
save(fig, "fig_tk_sup")
