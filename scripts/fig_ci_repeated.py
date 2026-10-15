"""The frequentist meaning of a confidence interval. One hundred independent
repetitions of the kiss experiment (n = 124, true p = 0.645), each giving a
95% plug-in interval. The parameter is a fixed vertical line; the intervals
move. About 5 of 100 miss (drawn in orange); sorted by p-hat, the misses are
the samples whose proportion came out unusually low or high. The level is the hit rate of the
procedure over repetitions, not a probability about any one interval."""
from _style import *

n, p, reps = 124, 0.645, 100
z = 1.959964
r = rng(4)
phat = np.sort(r.binomial(n, p, size=reps) / n)   # sorted, so the misses sit at the two ends
half = z * np.sqrt(phat * (1 - phat) / n)
lo, hi = phat - half, phat + half
miss = (lo > p) | (hi < p)

fig, ax = plt.subplots(figsize=(6.0, 4.0))
ax.yaxis.grid(False)
ax.set_axisbelow(True)
y = np.arange(reps)
for i in range(reps):
    col = ORANGE if miss[i] else BLUE
    ax.plot([lo[i], hi[i]], [y[i], y[i]], color=col, lw=1.1 if miss[i] else 0.8, alpha=1 if miss[i] else 0.7)
    ax.plot(phat[i], y[i], "o", ms=1.8, color=col)
ax.axvline(p, color=INK, lw=1.0)
ax.text(p + 0.004, reps + 3, rf"true $p = {p}$", fontsize=8, color=INK, va="bottom")
ax.set_xlim(0.45, 0.85)
ax.set_ylim(-1.5, reps + 9)
ax.set_yticks([])
ax.set_xlabel(r"$p$")
ax.set_ylabel(r"repetitions, sorted by $\hat p$")
ax.set_title(rf"100 repetitions, 100 plug-in 95% intervals: {int(miss.sum())} miss, {reps - int(miss.sum())} cover")
save(fig, "fig_ci_repeated")
print("misses:", int(miss.sum()))
