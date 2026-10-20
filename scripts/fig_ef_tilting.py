"""Exponential tilting. Left: the standard Gaussian density h(y) tilted
by e^{theta y} and renormalized, for theta = -1.5 (orange, dashed), 0
(blue) and 1.5 (aqua, dash-dot): the mean moves to theta, the shape does
not change. Right: the Poisson base weights h(y) = 1/y! tilted by
e^{theta y} and renormalized, for theta = log 1 (blue) and theta = log 4
(orange): the Poisson PMFs with means 1 and 4."""
from _style import *
from math import factorial

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
y = np.linspace(-4.5, 4.5, 500)
for th, col, ls, lab, lx, ly in ((-1.5, ORANGE, DASHES[1], r"$\theta = -1.5$", -1.5, 0.425), (0, BLUE, DASHES[0], r"$\theta = 0$", 0, 0.465), (1.5, AQUA, DASHES[2], r"$\theta = 1.5$", 1.5, 0.425)):
    f = norm_pdf(y) * np.exp(th * y); f = f / np.trapezoid(f, y)
    ax1.plot(y, f, color=col, ls=ls, lw=1.4)
    ax1.text(lx, ly, lab, ha="center", fontsize=8, color=col)
ax1.set_ylim(0, 0.5); ax1.set_xlabel("$y$"); ax1.set_ylabel("density")
ax1.set_title("tilting a Gaussian moves it")
k = np.arange(0, 13); h = np.array([1 / factorial(i) for i in k])
for th, col, dx, lab in ((np.log(1.0), BLUE, -0.18, r"$\theta = \log 1$"), (np.log(4.0), ORANGE, 0.18, r"$\theta = \log 4$")):
    w = h * np.exp(th * k); w = w / w.sum()
    ax2.bar(k + dx, w, width=0.34, color=col, alpha=0.85, lw=0)
ax2.text(1.75, 0.345, r"$\theta = 0$", fontsize=8, color=BLUE)
ax2.text(5.6, 0.2, r"$\theta = \log 4$", fontsize=8, color=ORANGE)
ax2.set_xlabel("$y$"); ax2.set_ylabel("probability"); ax2.set_xticks(range(0, 13, 2))
ax2.set_title("tilting $1/y!$ gives the Poisson")
save(fig, "fig_ef_tilting")
