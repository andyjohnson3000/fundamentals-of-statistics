"""A random variable is a function on the sample space. Left: the 36 equally
likely outcomes of two dice, and the function X = 'sum of the two dice'
coloring each outcome by its value; P(X = 7) is the number of outcomes sent
to 7, divided by 36. Right: the resulting PMF on the real line. Two random
variables on the same sample space (X = sum, Y = larger die) are two
functions of the same outcome, which is what lets you talk about X - Y or
about X and Y being close: you compare them outcome by outcome."""
from _style import *
from matplotlib import cm

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.0, 3.0), gridspec_kw=dict(width_ratios=[1, 1.2], wspace=0.35))
cmap = plt.get_cmap("Blues")
for i in range(1, 7):
    for j in range(1, 7):
        s = i + j
        ax1.add_patch(plt.Rectangle((i - 0.5, j - 0.5), 1, 1, color=cmap(0.25 + 0.065 * (s - 2)), ec="white", lw=1.2))
        ax1.text(i, j, str(s), ha="center", va="center", fontsize=8, color=INK if s < 9 else "white")
ax1.set_xlim(0.5, 6.5); ax1.set_ylim(0.5, 6.5); ax1.set_aspect("equal")
ax1.set_xticks(range(1, 7)); ax1.set_yticks(range(1, 7)); ax1.grid(False)
ax1.set_xlabel("first die"); ax1.set_ylabel("second die")
ax1.set_title(r"The sample space, colored by $X(s) = $ sum")

k = np.arange(2, 13)
pm = np.array([min(s - 1, 13 - s) for s in k]) / 36
ax2.bar(k, pm, width=0.7, color=[cmap(0.25 + 0.065 * (s - 2)) for s in k], ec="white")
ax2.set_xticks(k); ax2.set_xlabel(r"value of $X$"); ax2.set_ylabel("probability")
ax2.set_title(r"$\mathbb{P}(X = 7) = 6/36$: six outcomes land on $7$", fontsize=8)
save(fig, "fig_tk_rv_function")
