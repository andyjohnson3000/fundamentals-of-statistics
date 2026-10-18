"""Spread in x buys precision. Twenty points with x equally spaced over
[3, 4] (left) or over [1.5, 5] (right), Y = 33.5 + 10.7 x plus
Gauss(0, 6^2) errors; the least squares lines of 30 simulated samples
(blue) around the true line (black, dashed). The slope's standard
deviation sigma/sqrt(S_xx) is 4.42 on the left and 1.26 on the right."""
from _style import *

g = rng(20)
fig, axes = plt.subplots(1, 2, figsize=FULL, sharey=True, layout="constrained")
t = np.array([1.0, 5.5])
for ax, (lo, hi) in zip(axes, ((3.0, 4.0), (1.5, 5.0))):
    x = np.linspace(lo, hi, 20)
    sxx = ((x - x.mean()) ** 2).sum()
    for _ in range(30):
        y = 33.5 + 10.7 * x + g.normal(0, 6, 20)
        b = ((x - x.mean()) * (y - y.mean())).sum() / sxx
        a = y.mean() - b * x.mean()
        ax.plot(t, a + b * t, color=BLUE, lw=0.6, alpha=0.55)
    ax.plot(t, 33.5 + 10.7 * t, color=INK, lw=1.2, ls=DASHES[1])
    ax.axvspan(lo, hi, color=GRAY, alpha=0.12, lw=0)
    ax.set_xlim(1, 5.5); ax.set_ylim(20, 120)
    ax.set_xlabel("$x$")
    ax.set_title(f"$x$ from {lo:g} to {hi:g}")
    print(lo, hi, "sd slope", 6 / np.sqrt(sxx))
axes[0].set_ylabel("$y$")
save(fig, "fig_reg_design")
