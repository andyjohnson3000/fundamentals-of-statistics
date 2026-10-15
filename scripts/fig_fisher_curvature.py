"""Fisher information is curvature. Left: the log-likelihood of one
observation, l(p) = R log p + (1 - R) log(1 - p), for R = 1 (blue) and R = 0
(orange), and their average under p* = 0.645 (black), which peaks at p* and
whose curvature there is -I(p*) = -4.37. Right: the Fisher information of
the Bernoulli model, I(p) = 1/(p(1 - p)), smallest at p = 1/2 (4) and
growing without bound at the ends; one coin flip says most about p when p is
near 0 or 1."""
from _style import *

ps = 0.645
p = np.linspace(0.05, 0.95, 500)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
l1, l0 = np.log(p), np.log(1 - p)
avg = ps * l1 + (1 - ps) * l0
ax1.plot(p, l1, color=BLUE, lw=1.2)
ax1.plot(p, l0, color=ORANGE, lw=1.2, ls=DASHES[1])
ax1.plot(p, avg, color=INK, lw=1.6)
# tangent parabola at p*
par = (ps * np.log(ps) + (1 - ps) * np.log(1 - ps)) - 0.5 * (1 / (ps * (1 - ps))) * (p - ps) ** 2
m = np.abs(p - ps) < 0.36
ax1.plot(p[m], par[m], color=AQUA, lw=1.4, ls=DASHES[2])
ax1.axvline(ps, color=INK, lw=0.5, ls=":")
ax1.set_xlim(0.05, 0.95); ax1.set_ylim(-3, 0.3)
ax1.set_xlabel(r"$p$"); ax1.set_title("one observation's log-likelihood")
ax1.text(0.93, 0.25, r"$R = 1$: $\log p$", color=BLUE, fontsize=7.5, va="top", ha="right")
ax1.text(0.07, -2.95, r"$R = 0$: $\log(1-p)$", color=ORANGE, fontsize=7.5, va="bottom")
ax1.text(0.12, -1.6, "average under $p^*$ (black)\nand the parabola with\nits curvature (aqua)", fontsize=7.5, color=INK, va="top", ha="left")

ax2.plot(p, 1 / (p * (1 - p)), color=BLUE, lw=1.4)
ax2.plot([ps], [1 / (ps * (1 - ps))], "o", ms=4, color=ORANGE, zorder=5)
ax2.plot([0.5], [4], "o", ms=4, color=GRAY, zorder=5)
ax2.set_xlim(0, 1); ax2.set_ylim(0, 22)
ax2.set_xlabel(r"$p$"); ax2.set_ylabel(r"$I(p) = 1/(p(1-p))$")
ax2.set_title("Fisher information of one coin flip")
note(ax2, r"$I(0.645) = 4.37$", (ps, 1 / (ps * (1 - ps))), (0.55, 9.5), ha="left")
note(ax2, r"minimum $4$ at $p = \frac{1}{2}$", (0.5, 4), (0.12, 16), ha="left")
save(fig, "fig_fisher_curvature")
