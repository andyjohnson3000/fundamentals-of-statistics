"""Calculus convergence versus random sequences inside the same epsilon band.
Left: a sequence of numbers has one N past which every term is inside. Right:
five realizations of the running sample mean; each path is one outcome of the
experiment, and the index past which a path stays inside differs from path to
path, so no single N works for every outcome."""
from _style import *

eps = 0.25
N = 60
n = np.arange(1, N + 1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, sharey=True, layout="constrained")

# Left: a deterministic sequence x_n = 2 + (-1)^n / sqrt(n)
x = 2 + (-1.0) ** n / np.sqrt(n)
ax1.axhspan(2 - eps, 2 + eps, color=BLUE, alpha=0.10, lw=0)
ax1.axhline(2, color=GRAY, lw=0.8)
ax1.plot(n, x, "o", ms=2.8, color=BLUE, mec="white", mew=0.3)
N0 = int(math.ceil(1 / eps ** 2))
ax1.axvline(N0, color=GRAY, lw=0.7, ls="--")
# beside the dashed line, in the empty region well above the band (every term past N is below 2.25)
ax1.text(N0 + 2, 2.62, r"$N$: past here every term is inside", ha="left", va="center",
         fontsize=7.5, color=INK)
ax1.text(N - 1, 2 + eps + 0.03, r"$x + \epsilon$", ha="right", va="bottom", fontsize=7.5, color=INK)
ax1.text(N - 1, 2 - eps - 0.03, r"$x - \epsilon$", ha="right", va="top", fontsize=7.5, color=INK)
ax1.set_title("A sequence of numbers\n" + r"$x_n = 2 + (-1)^n/\sqrt{n}$")
ax1.set_xlabel(r"$n$")
ax1.set_ylim(0.9, 3.1)

# Right: five sample paths of the running mean of Exponential draws with mean 2.
# Each path is one outcome of the experiment; no single N works for all of them.
r = rng(7)
paths = 5
for j in range(paths):
    draws = r.exponential(scale=2.0, size=N)
    xbar = np.cumsum(draws) / n
    inside = np.abs(xbar - 2) < eps
    ax2.plot(n, xbar, color=BLUE, lw=0.6, alpha=0.3)
    ax2.plot(n[inside], xbar[inside], "o", ms=1.7, color=BLUE, mec="white", mew=0.2,
             label="inside the band" if j == 0 else None)
    ax2.plot(n[~inside], xbar[~inside], "o", ms=2.2, color=ORANGE, mec="white", mew=0.2,
             label="outside the band" if j == 0 else None)
ax2.axhspan(2 - eps, 2 + eps, color=BLUE, alpha=0.10, lw=0)
ax2.axhline(2, color=GRAY, lw=0.8)
ax2.set_title("A sequence of random variables\n" + r"$\bar{X}_n$ of Exponential draws, five realizations")
ax2.set_xlabel(r"$n$")
# no corner of this panel is empty (paths wander everywhere), so the legend goes under the axes
legend_below(ax2, ncol=2, markerscale=2.2)

save(fig, "fig_sequence_vs_random")
