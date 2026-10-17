"""The Kolmogorov-Smirnov statistic for ten outputs of a random number
generator, rounded to two decimals: 0.08, 0.17, 0.38, 0.51, 0.54, 0.61,
0.80, 0.87, 0.94, 0.98. Left: their empirical CDF (blue) against the
Unif(0, 1) CDF (black); the largest gap, D_10 = 0.21 at the fourth value,
is marked in orange. Right: the same ten numbers sent through the
exponential quantile function with mean 5, x = -5 log(1 - u), against the
exponential CDF (black): every gap is the same, and so is D_10."""
from _style import *

u = np.array([0.08, 0.17, 0.38, 0.51, 0.54, 0.61, 0.80, 0.87, 0.94, 0.98])
n = len(u)
i = np.arange(1, n + 1)
above = i / n - u            # F_n(U_(i)) - F0(U_(i))
below = u - (i - 1) / n      # F0(U_(i)) - F_n(U_(i)-)
D = max(above.max(), below.max())
j = int(np.argmax(below))    # index of the largest gap (it is a 'below' gap here)
MEAN = 5.0
x = -MEAN * np.log(1 - u)


def stairs(v, lo, hi):
    v = np.sort(v)
    xs = np.concatenate([[lo], np.repeat(v, 2), [hi]])
    ys = np.concatenate([[0, 0], np.repeat(np.arange(1, n) / n, 2), [1, 1]])
    return xs, ys


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
xs, ys = stairs(u, 0, 1)
ax1.plot([0, 1], [0, 1], color=INK, lw=1.1)
ax1.plot(xs, ys, color=BLUE, lw=1.3)
ax1.plot([u[j], u[j]], [j / n, u[j]], color=ORANGE, lw=2.2, solid_capstyle="butt")
ax1.set_xlim(0, 1); ax1.set_ylim(0, 1.02)
ax1.set_xlabel(r"$u$"); ax1.set_ylabel("cumulative proportion")
ax1.set_title("ten outputs against Unif(0, 1)")
note(ax1, f"$D_{{10}} = {D:.2f}$", (u[j] + 0.006, 0.33), (0.66, 0.17), ha="left")

t = np.linspace(0, 22, 500)
xs, ys = stairs(x, 0, 22)
ax2.plot(t, 1 - np.exp(-t / MEAN), color=INK, lw=1.1)
ax2.plot(xs, ys, color=BLUE, lw=1.3)
ax2.plot([x[j], x[j]], [j / n, u[j]], color=ORANGE, lw=2.2, solid_capstyle="butt")
ax2.set_xlim(0, 22); ax2.set_ylim(0, 1.02)
ax2.set_xlabel("minutes")
ax2.set_title("the same numbers as exponential waits")
note(ax2, f"$D_{{10}} = {D:.2f}$", (x[j] + 0.15, 0.33), (9.5, 0.17), ha="left")
save(fig, "fig_ks_example")
print("D =", D, "at i =", j + 1, "above", np.round(above, 2), "below", np.round(below, 2))
print("x =", np.round(x, 2))
