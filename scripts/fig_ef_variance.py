"""The variance function V(mu) = b''(theta) at the theta with mean mu, for
four families: Gaussian with sigma = 1 (blue, constant 1), Poisson
(orange, dashed, V = mu), exponential (aqua, dash-dot, V = mu^2), and
Bernoulli (yellow, dotted, V = mu(1 - mu) on (0, 1), drawn on its own
scale at the left)."""
from _style import *

fig, ax = plt.subplots(figsize=(4.2, 2.9), layout="constrained")
mu = np.linspace(0.01, 3, 300)
ax.plot(mu, np.ones_like(mu), color=BLUE, lw=1.4); end_label(ax, 3, 1, "Gaussian, $1$", color=INK)
ax.plot(mu, mu, color=ORANGE, lw=1.4, ls=DASHES[1]); end_label(ax, 3, 3, r"Poisson, $\mu$", color=INK)
ax.plot(mu, mu ** 2, color=AQUA, lw=1.4, ls=DASHES[2]); ax.text(1.35, 3.8, r"exponential, $\mu^2$", fontsize=7.5, color=INK, ha="right")
m = np.linspace(0.001, 0.999, 200)
ax.plot(m, m * (1 - m), color=YELLOW, lw=1.6, ls=DASHES[3]); note(ax, r"Bernoulli, $\mu(1 - \mu)$", (0.5, 0.25), (0.45, 1.75), fontsize=7.5)
ax.set_xlim(0, 3.9); ax.set_ylim(0, 4.3)
ax.set_xlabel(r"mean $\mu$"); ax.set_ylabel(r"variance function $V(\mu)$")
ax.set_title("how the variance follows the mean")
save(fig, "fig_ef_variance")
