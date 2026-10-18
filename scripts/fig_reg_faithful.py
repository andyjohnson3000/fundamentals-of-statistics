"""Old Faithful, 272 eruptions. Left: waiting time to the next eruption
against the eruption's duration. Right: the waits grouped by duration in
half-minute bins (the last from 4.5 to 5.5), one box per bin (quartiles, whiskers to the extremes),
with the bin mean as an orange dot: the conditional distribution of Y
moves with x."""
from _style import *
from _faithful import faithful

x, y = faithful()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, sharey=True, layout="constrained")
ax1.scatter(x, y, s=7, color=BLUE, alpha=0.55, lw=0)
ax1.set_xlabel("eruption duration (minutes)")
ax1.set_ylabel("wait to next eruption (minutes)")
ax1.set_title("272 eruptions")
ax1.set_xlim(1.4, 5.3)

edges = np.array([1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.5])
centers, data, means = [], [], []
for lo, hi in zip(edges[:-1], edges[1:]):
    m = (x >= lo) & (x < hi)
    if m.sum() >= 5:
        centers.append(x[m].mean()); data.append(y[m]); means.append(y[m].mean())
bp = ax2.boxplot(data, positions=centers, widths=0.28, whis=(0, 100), patch_artist=True,
                 medianprops=dict(color=INK, lw=1.0), boxprops=dict(facecolor="#d9e6f6", edgecolor=BLUE, lw=0.8),
                 whiskerprops=dict(color=BLUE, lw=0.8), capprops=dict(color=BLUE, lw=0.8))
ax2.plot(centers, means, "o", color=ORANGE, ms=4, zorder=5)
ax2.set_xlim(1.4, 5.3)
ax2.set_xticks([2, 3, 4, 5]); ax2.set_xticklabels(["2", "3", "4", "5"])
ax2.set_xlabel("eruption duration (minutes)")
ax2.set_title("waits by half-minute bin")
save(fig, "fig_reg_faithful")
for c, d, mm in zip(centers, data, means):
    print(c, len(d), round(mm, 2))
