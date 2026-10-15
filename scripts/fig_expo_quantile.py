"""Quantiles of a skewed distribution. The Expo(lambda) density with
lambda = 0.16 (the subway rate): the median ln2/lambda = 4.3 minutes sits
left of the mean 1/lambda = 6.2 minutes because the long right tail pulls the
mean up, and the q_0.05 = -ln(0.05)/lambda = 18.7 minutes leaves 5%
of the mass in the upper tail."""
from _style import *

lam = 0.1605
x = np.linspace(0, 30, 600)
f = lam * np.exp(-lam * x)
med = math.log(2) / lam
mean = 1 / lam
q05 = -math.log(0.05) / lam

fig, ax = plt.subplots(figsize=(5.2, 2.7))
ax.plot(x, f, color=INK, lw=1.2)
ax.fill_between(x[x <= med], f[x <= med], color=BLUE, alpha=0.18, lw=0)
ax.fill_between(x[x >= q05], f[x >= q05], color=ORANGE, alpha=0.35, lw=0)
# Two-line labels at the top of each dotted line, above the curve. The median
# and mean lines are only 1.9 min apart, so the median label sits to the LEFT
# of its line and the other two to the right; the formulas are in the caption.
ytop = 0.19
for v, lab, side in ((med, f"median\n{med:.1f} min", "right"), (mean, f"mean\n{mean:.1f} min", "left"),
                     (q05, rf"$q_{{0.05}}$" + "\n" + f"{q05:.1f} min", "left")):
    ax.axvline(v, color=GRAY, lw=0.7, ls=":")
    ax.text(v + (0.4 if side == "left" else -0.4), ytop - 0.018, lab, fontsize=7.5, color=INK,
            va="center", ha=side, linespacing=1.3)
ax.text(1.5, 0.03, "half the mass", fontsize=7.5, color=INK)
ax.text(q05 + 0.5, 0.012, "5% of the mass", fontsize=7.5, color=INK)
ax.set_xlim(0, 30)
ax.set_ylim(0, ytop)
ax.set_xlabel("minutes between trains")
ax.set_ylabel("density")
ax.set_title(r"$\mathrm{Expo}(\lambda)$ with $\lambda = 0.16$ per minute")
save(fig, "fig_expo_quantile")
