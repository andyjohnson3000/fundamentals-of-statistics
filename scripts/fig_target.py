"""Bias and variance as a target. The bull's-eye is the truth theta; each dot
is the estimate from one sample. Bias is how far the center of the group is
from the bull's-eye; variance is how tight the group is; the quadratic risk is
the average squared distance from a dot to the bull's-eye, which the
decomposition splits into the two. The lower-left panel is the shrinkage
estimator of fig_bias_variance: a tight group slightly off center, closer on
average than the loose group centered on the target (upper right)."""
from _style import *

r = rng(12)
fig, axes = plt.subplots(2, 2, figsize=(5.0, 5.0))
cases = [
    ((0, 0), 0.12, "low bias, low variance\n" + r"(unbiased, precise)", axes[0, 0]),
    ((0, 0), 0.32, "low bias, high variance\n" + r"(unbiased, imprecise: $X_1$-like)", axes[0, 1]),
    ((0.28, 0.18), 0.12, "biased, low variance\n(the shrinkage estimator)", axes[1, 0]),
    ((0.28, 0.18), 0.32, "biased, high variance", axes[1, 1]),
]
for (bx, by), sd, title, ax in cases:
    for rad, col in ((1.0, "#f3f3f3"), (0.7, "white"), (0.4, "#f3f3f3"), (0.15, ORANGE)):
        ax.add_patch(plt.Circle((0, 0), rad, facecolor=col, edgecolor=GRAY, lw=0.6, alpha=0.9 if col != ORANGE else 0.8))
    pts = r.normal(size=(25, 2)) * sd + np.array([bx, by])
    ax.plot(pts[:, 0], pts[:, 1], "o", ms=3.2, color=BLUE, mec="white", mew=0.3)
    ax.plot(bx, by, "x", ms=7, color=INK, mew=1.2)
    risk = sd ** 2 * 2 + bx ** 2 + by ** 2
    ax.set_title(title, fontsize=8)
    ax.text(0, -1.12, rf"risk $=$ var $+$ bias$^2$ $= {2 * sd ** 2:.2f} + {bx ** 2 + by ** 2:.2f} = {risk:.2f}$",
            ha="center", va="top", fontsize=7, color=INK)
    ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.35, 1.25)
    ax.set_aspect("equal"); ax.axis("off")
axes[0, 0].annotate(r"$\theta$ (the truth)", (0, 0), xytext=(0.55, -0.75), fontsize=8, color=INK, arrowprops=dict(arrowstyle="-", color=INK, lw=0.5))
fig.subplots_adjust(hspace=0.35, wspace=0.05)
save(fig, "fig_target")
