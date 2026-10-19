"""Least squares as a projection, drawn in perspective: the plane spanned
by the columns of the design matrix (gray parallelogram), the response
vector Y (black arrow from the origin), the fitted vector X beta-hat
(blue), which is the foot of the perpendicular from Y to the plane, and the
residual e = Y - X beta-hat (orange, dashed), perpendicular to the plane."""
from _style import *
from matplotlib.patches import Polygon, FancyArrowPatch

fig, ax = plt.subplots(figsize=(4.2, 3.0), layout="constrained")
plane = np.array([[0.2, 0.9], [4.6, 0.9], [5.6, 2.3], [1.2, 2.3]])
ax.add_patch(Polygon(plane, closed=True, color=GRAY, alpha=0.18, lw=0))
O = np.array([1.2, 1.35]); F = np.array([3.9, 1.75]); Y = F + np.array([0, 1.6])
ax.add_patch(FancyArrowPatch(O, Y, arrowstyle="-|>", mutation_scale=10, color=INK, lw=1.4))
ax.add_patch(FancyArrowPatch(O, F, arrowstyle="-|>", mutation_scale=10, color=BLUE, lw=1.4))
ax.plot([F[0], Y[0]], [F[1], Y[1]], color=ORANGE, lw=1.4, ls=DASHES[1])
# right-angle mark at F
d = 0.18
ax.plot([F[0] - d, F[0] - d, F[0]], [F[1], F[1] + d, F[1] + d], color=ORANGE, lw=0.8)
ax.plot(*O, "o", color=INK, ms=3)
ax.text(O[0] - 0.12, O[1] - 0.22, "$0$", fontsize=9, color=INK)
ax.text(Y[0] + 0.1, Y[1], "$Y$", fontsize=10, color=INK, va="center")
ax.text(F[0] + 0.12, F[1] - 0.26, r"$X\hat{\beta} = PY$", fontsize=10, color=BLUE)
ax.text(F[0] + 0.12, F[1] + 0.8, r"$e = Y - X\hat{\beta}$", fontsize=10, color=ORANGE)
ax.text(3.2, 1.0, "column space of $X$", fontsize=8.5, color=GRAY)
ax.set_xlim(0, 6); ax.set_ylim(0.6, 3.6); ax.set_aspect("equal")
ax.axis("off")
ax.set_title("least squares is a projection")
save(fig, "fig_mreg_projection")
