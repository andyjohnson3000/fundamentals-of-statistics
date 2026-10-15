"""Jensen's inequality for a convex function: the chord lies above the curve,
so g(E[X]) <= E[g(X)]. Drawn for g(x) = 1/x and a two-point X at 1 and 4 with
equal probability (E[X] = 2.5, g(E[X]) = 0.4, E[g(X)] = 0.625)."""
from _style import *

g = lambda x: 1 / x
x1, x2, t = 1.0, 4.0, 0.5
EX = t * x1 + (1 - t) * x2
Eg = t * g(x1) + (1 - t) * g(x2)

fig, ax = plt.subplots(figsize=(4.6, 3.2))
x = np.linspace(0.6, 5, 400)
ax.plot(x, g(x), color=INK, lw=1.3)
# curve label under the flat part of the curve, between the dotted guide lines at 2.5 and 4
ax.text(3.25, 0.15, r"$g(x) = 1/x$, convex", fontsize=8, color=INK, ha="center", va="center")
ax.plot([x1, x2], [g(x1), g(x2)], color=ORANGE, ls="--", lw=1.2)
ax.text(2.05, 0.80, "chord", fontsize=8, color=INK)  # just above the dashed chord
for xx in (x1, x2):
    ax.plot(xx, g(xx), "o", ms=5, color=INK)
    ax.plot([xx, xx], [0, g(xx)], color=GRAY, lw=0.6, ls=":")
ax.plot(EX, g(EX), "o", ms=5, color=BLUE, zorder=5)
ax.plot(EX, Eg, "s", ms=5, color=ORANGE, zorder=5)
ax.plot([EX, EX], [0, Eg], color=GRAY, lw=0.6, ls=":")
# below-left of the blue point, in the empty pocket under the curve, with a short leader
ax.annotate(r"$g(\mathbb{E}[X]) = 0.40$", (EX, g(EX)), xytext=(2.33, 0.27), ha="right", va="center",
            fontsize=8, color=INK, arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6, shrinkA=2, shrinkB=4))
ax.annotate(r"$\mathbb{E}[g(X)] = 0.625$", (EX, Eg), xytext=(10, 6), textcoords="offset points", fontsize=8, color=INK)
ax.set_xticks([x1, EX, x2])
ax.set_xticklabels([r"$x_1 = 1$", r"$\mathbb{E}[X] = 2.5$", r"$x_2 = 4$"])
ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_ylim(0, 1.15)
ax.set_xlim(0.6, 5)
ax.set_xlabel(r"$x$")
save(fig, "fig_jensen")
