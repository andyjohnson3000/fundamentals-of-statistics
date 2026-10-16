"""Chi-squared densities. Left: k = 1, 2, 3, 5, 10 degrees of freedom.
Right: k = 30, with its mean 30 marked and the Gaussian with the same mean
and variance, Gauss(30, 60), drawn over it (dashed)."""
from _style import *

def chisq_pdf(x, k):
    return gamma_pdf(x, k / 2, 0.5)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
x = np.linspace(0.001, 20, 1200)
styles = [(1, BLUE, DASHES[0]), (2, ORANGE, DASHES[1]), (3, AQUA, DASHES[2]), (5, YELLOW, DASHES[3]), (10, GRAY, DASHES[0])]
for k, c, ls in styles:
    ax1.plot(x, chisq_pdf(x, k), color=c, lw=1.3, ls=ls)
ax1.set_xlim(0, 20); ax1.set_ylim(0, 0.6)
ax1.set_xlabel(r"$v$"); ax1.set_ylabel("density")
ax1.set_title("chi-squared densities")
ax1.text(1.2, 0.52, r"$k = 1$", color=BLUE, fontsize=7.5)
ax1.text(1.6, 0.36, r"$k = 2$", color=ORANGE, fontsize=7.5)
ax1.text(3.6, 0.26, r"$k = 3$", color=AQUA, fontsize=7.5)
ax1.text(6.0, 0.17, r"$k = 5$", color=YELLOW, fontsize=7.5)
ax1.text(12.5, 0.1, r"$k = 10$", color=GRAY, fontsize=7.5)

x2 = np.linspace(0.001, 70, 1400)
k = 30
ax2.plot(x2, chisq_pdf(x2, k), color=BLUE, lw=1.3)
ax2.plot(x2, norm_pdf(x2, k, math.sqrt(2 * k)), color=INK, lw=1.1, ls=DASHES[1])
ax2.axvline(k, color=GRAY, lw=0.8, ls=DASHES[3])
ax2.set_xlim(0, 70); ax2.set_ylim(0, 0.06)
ax2.set_xlabel(r"$v$"); ax2.set_ylabel("density")
ax2.set_title(r"$k = 30$ against its Gaussian approximation")
ax2.text(33, 0.0595, r"mean $k = 30$", color=GRAY, fontsize=7.5, va="top")
note(ax2, r"$\chi^2_{30}$", (22, chisq_pdf(22, k)), (6, 0.04), ha="left")
note(ax2, "Gauss(30, 60)", (40, norm_pdf(40, k, math.sqrt(2 * k))), (50, 0.04), ha="left")
save(fig, "fig_chisq_densities")
