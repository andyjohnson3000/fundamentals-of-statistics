"""Orthogonal projection in the plane: a vector y (black), the line
spanned by a vector x (gray), the projection Py = (x'y / x'x) x (blue) and
the residual y - Py (orange, dashed), perpendicular to the line. The
projection is the point of the line closest to y."""
from _style import *
from matplotlib.patches import FancyArrowPatch

x = np.array([3.0, 1.0]); y = np.array([1.6, 2.4])
Py = (x @ y) / (x @ x) * x
fig, ax = plt.subplots(figsize=(3.6, 2.6), layout="constrained")
t = np.array([-0.3, 1.25])
ax.plot(t * x[0], t * x[1], color=GRAY, lw=0.8, zorder=1)
for v, col in ((y, INK), (Py, BLUE)):
    ax.add_patch(FancyArrowPatch((0, 0), v, arrowstyle="-|>", mutation_scale=10, color=col, lw=1.4, zorder=3))
ax.plot([Py[0], y[0]], [Py[1], y[1]], color=ORANGE, lw=1.3, ls=DASHES[1])
d = 0.17; u = x / np.linalg.norm(x); w = np.array([-u[1], u[0]])
c = Py; ax.plot([c[0] - d * u[0], c[0] - d * u[0] + d * w[0], c[0] + d * w[0]], [c[1] - d * u[1], c[1] - d * u[1] + d * w[1], c[1] + d * w[1]], color=ORANGE, lw=0.8)
ax.text(y[0] + 0.08, y[1] + 0.05, "$y$", fontsize=10)
ax.text(Py[0] + 0.1, Py[1] - 0.3, "$Py$", fontsize=10, color=BLUE)
ax.text(3.45, 0.78, "line spanned by $x$", fontsize=8, color=GRAY, va="top")
ax.text((Py[0] + y[0]) / 2 + 0.1, (Py[1] + y[1]) / 2, "$y - Py$", fontsize=9, color=ORANGE)
ax.plot(0, 0, "o", color=INK, ms=3); ax.text(-0.15, -0.3, "$0$", fontsize=9)
ax.set_xlim(-1.2, 5.2); ax.set_ylim(-0.6, 2.9); ax.set_aspect("equal"); ax.axis("off")
ax.set_title("projection onto a line")
save(fig, "fig_tk_projection")
