"""Gradients and the second-derivative test in two variables. Left: the
contours of a concave function h(a, b) = -(a^2 + a b + b^2) with gradient
arrows; each arrow points uphill, perpendicular to the contour through its
foot, and the arrows shrink to nothing at the top, the one point where the
gradient is 0. Right: a saddle, h(a, b) = a^2 - b^2; its gradient is also 0
at the origin, which is a maximum along one direction and a minimum along
the other, so a zero gradient alone does not certify a maximum."""
from _style import *

g = np.linspace(-2, 2, 200); A, B = np.meshgrid(g, g)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
H = -(A ** 2 + A * B + B ** 2)
ax1.contour(A, B, H, levels=np.arange(-6, 0, 0.75), colors=GRAY, linewidths=0.6, linestyles="solid")
q = np.linspace(-1.6, 1.6, 7); QA, QB = np.meshgrid(q, q)
ax1.quiver(QA, QB, -(2 * QA + QB), -(QA + 2 * QB), color=BLUE, angles="xy", scale_units="xy", scale=8, width=0.006)
ax1.plot([0], [0], "o", ms=4, color=ORANGE, zorder=5)
ax1.set_aspect("equal"); ax1.set_xlabel(r"$a$"); ax1.set_ylabel(r"$b$")
ax1.set_title("concave: arrows lead to the top")

S = A ** 2 - B ** 2
ax2.contour(A, B, S, levels=np.arange(-3.5, 4, 0.75), colors=GRAY, linewidths=0.6, linestyles="solid")
ax2.quiver(QA, QB, 2 * QA, -2 * QB, color=BLUE, angles="xy", scale_units="xy", scale=8, width=0.006)
ax2.plot([0], [0], "o", ms=4, color=ORANGE, zorder=5)
ax2.set_aspect("equal"); ax2.set_xlabel(r"$a$")
ax2.set_title("saddle: gradient 0, no maximum")
save(fig, "fig_tk_gradient")
