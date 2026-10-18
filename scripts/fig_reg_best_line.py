"""The best line is not always the regression function. X ~ Unif(0, 1) and
Y = X^2 plus independent Gauss(0, 0.05^2) noise, 300 draws. Left: the
regression function x^2 (blue) and the theoretical regression line
-1/6 + x (orange, dashed). Right: the noise Y - (-1/6 + X) against X, with
its conditional mean x^2 - x + 1/6 (blue); dotted: zero."""
from _style import *

g = rng(2020)
X = g.uniform(0, 1, 300)
Y = X ** 2 + g.normal(0, 0.05, 300)
t = np.linspace(0, 1, 200)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
ax1.scatter(X, Y, s=6, color=GRAY, alpha=0.5, lw=0)
ax1.plot(t, t ** 2, color=BLUE, lw=1.4)
ax1.plot(t, -1 / 6 + t, color=ORANGE, lw=1.4, ls=DASHES[1])
ax1.set_xlabel("$x$"); ax1.set_ylabel("$y$")
ax1.set_title("regression function and best line")
ax1.set_xlim(0, 1); ax1.set_ylim(-0.25, 1.1)
eps = Y - (-1 / 6 + X)
ax2.scatter(X, eps, s=6, color=GRAY, alpha=0.5, lw=0)
ax2.plot(t, t ** 2 - t + 1 / 6, color=BLUE, lw=1.4)
ax2.axhline(0, color=INK, lw=0.8, ls=":")
ax2.set_xlabel("$x$"); ax2.set_ylabel(r"noise $\epsilon$")
ax2.set_title("the noise around the best line")
ax2.set_xlim(0, 1); ax2.set_ylim(-0.25, 0.32)
save(fig, "fig_reg_best_line")
print("sample mean eps", eps.mean().round(4), "corr(X, eps)", np.corrcoef(X, eps)[0, 1].round(4))
