"""Easy and hard functions to maximize. Left: the Poisson log-likelihood of
the siblings data (lambda for X - 1, n = 24, sum of x_i - 1 = 24), strictly
concave, with its one maximum at lambda-hat = 1 where the slope is 0.
Right: theta -> prod_i (theta - x_i) for five numbers x_i; it has several
points where the slope is 0, and solving h'(theta) = 0 does not tell you
which, if any, is the maximum. On the whole real line this function has no
maximum at all."""
from _style import *

lam = np.linspace(0.3, 2.4, 500)
s, n = 24, 24
ll = -n * lam + s * np.log(lam)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
ax1.plot(lam, ll, color=BLUE, lw=1.4)
ax1.plot([0.75, 1.25], [-24, -24], color=ORANGE, lw=1.0, ls=DASHES[1])
ax1.plot([1], [-24], "o", ms=4, color=ORANGE)
ax1.set_xlabel(r"$\lambda$"); ax1.set_ylabel(r"$\ell(\lambda) + $ constant")
ax1.set_title("concave: one peak, slope 0 there")
note(ax1, r"$\hat\lambda = 1$", (1, -24), (1.5, -32), ha="left")

xs = np.array([0.0, 1.0, 2.5, 3.2, 4.5])
th = np.linspace(-0.4, 4.9, 800)
h = np.prod([th - xi for xi in xs], axis=0)
ax2.plot(th, h, color=BLUE, lw=1.4)
ax2.axhline(0, color=INK, lw=0.5)
d = np.gradient(h, th); idx = np.where(np.diff(np.sign(d)) != 0)[0]
ax2.plot(th[idx], h[idx], "o", ms=4, color=ORANGE, zorder=5)
ax2.plot(xs, np.zeros_like(xs), "|", ms=7, color=INK)
ax2.set_ylim(-12, 14); ax2.set_xlim(-0.4, 4.9)
ax2.set_xlabel(r"$\theta$")
ax2.set_title(r"$\prod_i (\theta - x_i)$: four points with slope 0")
save(fig, "fig_concave_vs_not")
print(th[idx], h[idx])
