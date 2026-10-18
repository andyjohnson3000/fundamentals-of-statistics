"""Regression toward the mean for a standardized bivariate Gaussian with
correlation 0.5: ellipses holding 50%, 90% and 99% of the probability
(gray), the line y = x (black, dotted), the regression line of y on x,
y = 0.5 x (blue), and of x on y, x = 0.5 y (orange, dashed). Blue dots: the
conditional means of y at x = -2, -1, 0, 1, 2."""
from _style import *

rho = 0.5
fig, ax = plt.subplots(figsize=(3.6, 3.3), layout="constrained")
th = np.linspace(0, 2 * np.pi, 400)
# ellipse: z' S^-1 z = c with S = [[1, rho],[rho, 1]]; eigen decomposition
lam1, lam2 = 1 + rho, 1 - rho
for p in (0.5, 0.9, 0.99):
    c = -2 * np.log(1 - p)
    u = np.sqrt(c * lam1) * np.cos(th); v = np.sqrt(c * lam2) * np.sin(th)
    ax.plot((u - v) / np.sqrt(2), (u + v) / np.sqrt(2), color=GRAY, lw=0.7)
t = np.array([-3.2, 3.2])
ax.plot(t, t, color=INK, lw=0.9, ls=":")
ax.plot(t, rho * t, color=BLUE, lw=1.4)
ax.plot(rho * t, t, color=ORANGE, lw=1.4, ls=DASHES[1])
xs = np.array([-2, -1, 0, 1, 2])
ax.plot(xs, rho * xs, "o", color=BLUE, ms=4)
ax.set_xlim(-3.2, 3.2); ax.set_ylim(-3.2, 3.2); ax.set_aspect("equal")
ax.set_xlabel("$x$ in standard deviations"); ax.set_ylabel("$y$ in standard deviations")
ax.set_title("correlation 0.5")
save(fig, "fig_reg_toward_mean")
