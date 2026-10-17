"""The empirical CDF and the Glivenko-Cantelli theorem, for simulated
waiting times from the exponential distribution with mean 6.23 minutes
(the subway model). Left: the true CDF (black) and the empirical CDFs of
n = 10 (blue staircase) and n = 100 (orange, dashed) simulated waits. Right: the
argument of the proof with k = 4: the quartiles t_1, t_2, t_3 of the true
CDF (dotted verticals) cut the line into four stretches on each of which F
rises by 1/4 (gray boxes); an empirical CDF of n = 40 (blue) can only leave
the staircase of boxes by as much as it misses F at the quartiles."""
from _style import *

MEAN = 6.23
F = lambda t: np.where(t > 0, 1 - np.exp(-np.clip(t, 0, None) / MEAN), 0.0)
g = rng(2128)  # a draw whose gaps are typical for each n (near the median gap)


def ecdf_xy(x, lo, hi):
    """Points of the staircase t -> F_n(t) on [lo, hi]."""
    x = np.sort(x)
    n = len(x)
    xs = np.concatenate([[lo], np.repeat(x, 2), [hi]])
    ys = np.concatenate([[0, 0], np.repeat(np.arange(1, n) / n, 2), [1, 1]])
    return xs, ys


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
t = np.linspace(0, 30, 600)
x10 = g.exponential(MEAN, 10)
x100 = g.exponential(MEAN, 100)
xs, ys = ecdf_xy(x100, 0, 30)
ax1.plot(xs, ys, color=ORANGE, lw=1.0, ls=DASHES[1])
xs, ys = ecdf_xy(x10, 0, 30)
ax1.plot(xs, ys, color=BLUE, lw=1.2)
ax1.plot(t, F(t), color=INK, lw=1.1)
ax1.set_xlim(0, 30); ax1.set_ylim(0, 1.02)
ax1.set_xlabel("minutes"); ax1.set_ylabel("cumulative proportion")
ax1.set_title("empirical CDFs approach the CDF")
# no labels on the left: the staircases cross the curve everywhere, so the key is in the caption
D10 = np.max(np.abs(np.r_[np.arange(1, 11) / 10 - F(np.sort(x10)), F(np.sort(x10)) - np.arange(0, 10) / 10]))

# right: the staircase of boxes
k = 4
q = -MEAN * np.log(1 - np.arange(1, k) / k)   # quartiles of F
edges = np.concatenate([[0], q, [30]])
for j in range(k):
    ax2.add_patch(plt.Rectangle((edges[j], j / k), edges[j + 1] - edges[j], 1 / k,
                                facecolor="#e9e9e9", edgecolor="#bbbbbb", lw=0.6, zorder=0))
for qj in q:
    ax2.axvline(qj, color=GRAY, lw=0.7, ls=DASHES[3], zorder=1)
x40 = g.exponential(MEAN, 40)
xs, ys = ecdf_xy(x40, 0, 30)
ax2.plot(xs, ys, color=BLUE, lw=1.1, zorder=3)
ax2.plot(t, F(t), color=INK, lw=1.1, zorder=2)
ax2.set_xlim(0, 30); ax2.set_ylim(0, 1.02)
ax2.set_xticks(list(np.round(q, 1)) + [30])
ax2.set_xticklabels([r"$t_1$", r"$t_2$", r"$t_3$", "30"])
ax2.set_yticks([0, 0.25, 0.5, 0.75, 1])
ax2.grid(axis="x", visible=False)  # the dotted verticals mark the quartiles
ax2.set_xlabel("minutes")
ax2.set_title("three quartiles control the whole curve")
save(fig, "fig_ecdf_gc")
print("D_10 =", D10, "quartiles", q)
for m in [10, 100, 1000]:
    U = np.sort(g.random((4000, m)), axis=1)
    i = np.arange(1, m + 1)
    Dm = np.maximum((i / m - U).max(1), (U - (i - 1) / m).max(1))
    print("n", m, "median D_n", np.median(Dm), "mean", Dm.mean(), "sqrt(n) mean", np.sqrt(m) * Dm.mean())
