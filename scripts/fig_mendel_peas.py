"""Mendel's dihybrid cross (Mendel 1866): 556 peas from crossing plants
hybrid for seed shape (round/wrinkled) and seed color (yellow/green).
Left: the observed counts of the four kinds of pea (blue bars) with the
counts the 9:3:3:1 theory expects (black ticks: 312.75, 104.25, 104.25,
34.75). Right: the chi-squared density with three degrees of freedom, the
observed Pearson statistic 0.47 (orange), the area to its right (the
p-value 0.93, shaded) and the 5% threshold 7.81 (dotted)."""
from _style import *

obs = np.array([315, 108, 101, 32])
p0 = np.array([9, 3, 3, 1]) / 16
n = obs.sum()
exp_ = n * p0
T = float(((obs - exp_) ** 2 / exp_).sum())
Q3 = 7.814728  # 95% quantile of chi-squared with 3 degrees of freedom

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
x = np.arange(4)
ax1.bar(x, obs, width=0.6, color=BLUE, alpha=0.75, edgecolor="none")
for xi, e in zip(x, exp_):
    ax1.plot([xi - 0.36, xi + 0.36], [e, e], color=INK, lw=1.6, solid_capstyle="butt")
for xi, o, e in zip(x, obs, exp_):
    ax1.text(xi, max(o, e) + 9, f"{o}", ha="center", va="bottom", fontsize=7.5, color=INK)
note(ax1, "expected\nunder 9:3:3:1", (1.36, exp_[1]), (2.05, 230), ha="left", va="center")
ax1.set_xticks(x)
ax1.set_xticklabels(["round\nyellow", "round\ngreen", "wrinkled\nyellow", "wrinkled\ngreen"], fontsize=7.5)
ax1.set_ylim(0, 370)
ax1.set_ylabel("number of peas")
ax1.set_title("observed and expected counts")

v = np.linspace(0.001, 14, 800)
f = gamma_pdf(v, 1.5, 0.5)  # chi-squared, 3 degrees of freedom
ax2.plot(v, f, color=INK, lw=1.2)
right = v >= T
ax2.fill_between(v[right], 0, f[right], color=ORANGE, alpha=0.18, linewidth=0)
ax2.axvline(T, color=ORANGE, lw=1.3)
ax2.vlines(Q3, 0, 0.125, color=GRAY, lw=0.8, ls=DASHES[3])  # stops below the area note
note(ax2, f"observed {T:.2f}", (T, 0.268), (2.3, 0.281), ha="left")  # leader stays above the peak, 0.242
note(ax2, "area to the right\nof 0.47: 0.93", (3.4, 0.07), (5.0, 0.165), ha="left")
note(ax2, "5% threshold 7.81", (Q3, 0.03), (9.0, 0.075), ha="left")
ax2.set_xlim(0, 14); ax2.set_ylim(0, 0.305)
ax2.set_xlabel(r"value of Pearson's statistic"); ax2.set_ylabel("density")
ax2.set_title(r"its null distribution, $\chi^2_3$")
save(fig, "fig_mendel_peas")
print("n", n, "expected", exp_, "T", T)
