"""Distance between parameters is not distance between distributions. Both
panels show two Gaussians whose parameters differ by 0.01. Left: means 0 and
0.01 with standard deviation 1; the curves are indistinguishable and the
total variation distance is 0.004. Right: mean 0 with standard deviations
0.01 and 0.02; the curves are obviously different; their overlap (gray) is
0.677, so the total variation distance is 0.323. A difference of 0.01 in a parameter can mean almost
nothing or a great deal, depending on where in the parameter space it
happens."""
from _style import *

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
x = np.linspace(-3.5, 3.5, 800)
ax1.plot(x, norm_pdf(x, 0, 1), color=BLUE, lw=1.4)
ax1.plot(x, norm_pdf(x, 0.01, 1), color=ORANGE, lw=1.2, ls=DASHES[1])
ax1.set_ylim(0, 0.62); ax1.set_xlabel(r"$x$")
ax1.set_title(r"means $0$ and $0.01$, sd $1$")
ax1.text(-3.4, 0.6, r"$\mathrm{TV} = 0.004$", fontsize=7.5, color=INK, ha="left", va="top")
ax1.text(3.4, 0.6, "the curves coincide\nto the width of a line", fontsize=7.5, color=GRAY, ha="right", va="top")

x2 = np.linspace(-0.065, 0.065, 800)
f, g = norm_pdf(x2, 0, 0.01), norm_pdf(x2, 0, 0.02)
ax2.fill_between(x2, 0, np.minimum(f, g), color=GRAY, alpha=0.22, lw=0)
ax2.plot(x2, f, color=BLUE, lw=1.4)
ax2.plot(x2, g, color=ORANGE, lw=1.2, ls=DASHES[1])
ax2.set_ylim(0, 44); ax2.set_xlabel(r"$x$")
ax2.set_xticks([-0.05, 0, 0.05])
ax2.set_title(r"mean $0$, sd $0.01$ and $0.02$")
ax2.text(-0.064, 41, r"$\mathrm{TV} = 0.323$", fontsize=7.5, color=INK, ha="left", va="top")
ax2.text(0.019, 30, r"sd $0.01$", fontsize=7.5, color=BLUE, ha="left", va="center")
ax2.text(0.036, 6.5, r"sd $0.02$", fontsize=7.5, color=ORANGE, ha="left", va="center")
save(fig, "fig_param_vs_dist")
