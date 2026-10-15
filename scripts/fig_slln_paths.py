"""Left: six sample paths of the running mean of fair coin flips (the strong law:
each path, individually, settles into the band and stays). Right: the sliding
indicator example, which converges in probability but not almost surely: for a
fixed outcome U the sequence keeps returning to 1."""
from _style import *

N = 2000
n = np.arange(1, N + 1)
r = rng(5)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
eps = 0.05
ax1.axhspan(0.5 - eps, 0.5 + eps, color=BLUE, alpha=0.10, lw=0)
ax1.axhline(0.5, color=GRAY, lw=0.8)
for k in range(6):
    flips = r.integers(0, 2, size=N)
    path = np.cumsum(flips) / n
    ax1.plot(n, path, lw=0.9, color=SERIES[k % 4], alpha=0.85)
ax1.set_xscale("log")
ax1.set_ylim(0.2, 0.8)
ax1.set_xlabel(r"$n$ (log scale)")
ax1.set_ylabel(r"$\bar{X}_n$ (fraction of heads)")
ax1.set_title("Running mean of coin flips, six runs")
# band-edge labels at the right end, where every path has settled inside the band
ax1.text(N * 0.97, 0.5 + eps + 0.008, r"$\mu + \epsilon$", fontsize=7.5, color=INK, ha="right", va="bottom")
ax1.text(N * 0.97, 0.5 - eps - 0.008, r"$\mu - \epsilon$", fontsize=7.5, color=INK, ha="right", va="top")

# Sliding indicator: block m has m intervals [(j-1)/m, j/m], j = 1..m
U = 0.37
vals, idx = [], []
k = 0
for m in range(1, 13):
    for j in range(1, m + 1):
        k += 1
        lo, hi = (j - 1) / m, j / m
        vals.append(1 if lo <= U <= hi else 0)
        idx.append(k)
idx, vals = np.array(idx), np.array(vals)
ax2.vlines(idx[vals == 1], 0, 1, color=ORANGE, lw=1.2)
ax2.plot(idx[vals == 0], np.zeros((vals == 0).sum()), "o", ms=2.2, color=BLUE, mec="white", mew=0.3)
ax2.plot(idx[vals == 1], np.ones((vals == 1).sum()), "o", ms=2.6, color=ORANGE, mec="white", mew=0.3)
ax2.set_yticks([0, 1])
ax2.set_ylim(-0.15, 1.3)
ax2.set_xlabel(r"$n$")
ax2.set_ylabel(r"$X_n - U$")
ax2.set_title(rf"Sliding indicator, $U = {U}$")
ax2.text(0.98, 0.93, "the 1s thin out but never stop", transform=ax2.transAxes,
         ha="right", va="top", fontsize=8, color=INK)
save(fig, "fig_slln_paths")
