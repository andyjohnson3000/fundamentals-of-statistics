"""The definition of q_alpha as a picture, at the moment it is defined.
Left: the density of Z ~ Gauss(0, 1); q_alpha is the cutoff with area alpha
to its right (orange) and 1 - alpha to its left (blue). The subscript is the
upper-tail area. Right: the CDF, read backwards: start at 1 - alpha on the
vertical axis, go across to the curve, drop down, and read q_alpha off the
horizontal axis. Drawn for alpha = 0.05, q_0.05 = 1.645."""
from _style import *

alpha = 0.05
q = 1.6449
x = np.linspace(-3.5, 3.5, 700)
f, F = norm_pdf(x), norm_cdf(x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

# ---- left: density, the subscript is the upper-tail area
ax1.plot(x, f, color=INK, lw=1.2)
ax1.fill_between(x, 0, f, where=x <= q, color=BLUE, alpha=0.18, lw=0)
ax1.fill_between(x, 0, f, where=x >= q, color=ORANGE, alpha=0.6, lw=0)
ax1.axvline(q, color=GRAY, lw=0.7, ls="--")
ax1.text(-0.1, 0.13, r"area $1 - \alpha = 0.95$", ha="center", fontsize=8, color=INK)
ax1.annotate(r"area $\alpha = 0.05$", (2.05, 0.018), xytext=(1.95, 0.17), fontsize=8, color=INK,
             ha="left", arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6))
ax1.set_xticks([-2, 0, q])
ax1.set_xticklabels([r"$-2$", r"$0$", r"$q_{0.05} = 1.645$"])
ax1.set_yticks([])
ax1.set_ylim(0, 0.46)
ax1.set_xlim(-3.5, 3.5)
ax1.grid(False)
ax1.set_title(r"Density: $\alpha$ is the area above $q_\alpha$")

# ---- right: CDF read backwards
ax2.plot(x, F, color=INK, lw=1.2)
ax2.plot([-3.5, q], [1 - alpha, 1 - alpha], color=ORANGE, lw=0.9, ls="--")
ax2.plot([q, q], [0, 1 - alpha], color=ORANGE, lw=0.9, ls="--")
ax2.plot(q, 1 - alpha, "o", ms=3.5, color=ORANGE, mec="white", mew=0.4, zorder=5)
# arrows along the two legs of the path, in the empty corners
ax2.annotate("", xy=(-1.0, 1 - alpha), xytext=(-3.0, 1 - alpha),
             arrowprops=dict(arrowstyle="->", color=ORANGE, lw=0.9))
ax2.annotate("", xy=(q, 0.12), xytext=(q, 0.55),
             arrowprops=dict(arrowstyle="->", color=ORANGE, lw=0.9))
ax2.text(-3.3, 0.72, "start at $1 - \\alpha$\non the vertical axis", fontsize=7.5, color=INK, ha="left", va="top")
ax2.text(1.85, 0.42, "go across to the curve,\nthen down: read off $q_\\alpha$", fontsize=7.5, color=INK, ha="left", va="top")
ax2.set_xticks([-2, 0, q])
ax2.set_xticklabels([r"$-2$", r"$0$", r"$q_{0.05}$"])
ax2.set_yticks([0, 0.5, 1 - alpha])
ax2.set_yticklabels([r"$0$", r"$0.5$", r"$1 - \alpha$"])
ax2.set_ylim(0, 1.05)
ax2.set_xlim(-3.5, 3.5)
ax2.set_ylabel(r"$F(x)$")
ax2.set_title(r"CDF read backwards: $F(q_\alpha) = 1 - \alpha$")
save(fig, "fig_quantile_def")
