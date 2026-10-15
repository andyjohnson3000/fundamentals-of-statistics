"""Three layers between the sample space and a number. Left: the sample
space, every complete outcome of the study; the one that happened is marked.
Middle: the data, a function on the sample space (here the n = 12 responses
of a small kiss study, one row per outcome, 1 = turned right); the
row of the outcome that happened is the observed data set. Right: the
statistic Rbar_n, another function on the sample space; across all outcomes
weighted by probability it has a distribution (the bars), and the outcome
that happened gives one value of it. Inference runs the dashed arrow
backwards: the one value is held up against the whole distribution."""
from _style import *
from matplotlib.patches import Ellipse, Rectangle, FancyArrowPatch

n, p = 12, 0.645
r = rng(7)
rows = 7
data = r.binomial(1, p, size=(rows, n))
star = 3                      # the row that "happened"
data[star] = np.array([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0])  # 8 of 12

fig = plt.figure(figsize=(6.0, 2.7))
# explicit panel boxes: [left, bottom, width, height] in figure fractions
axL = fig.add_axes([0.01, 0.20, 0.24, 0.62])
axM = fig.add_axes([0.33, 0.20, 0.34, 0.62])
axR = fig.add_axes([0.75, 0.20, 0.24, 0.62])
for ax in (axL, axM, axR):
    ax.grid(False)

# ---- left: the sample space as a cloud of outcomes
axL.set_xlim(0, 1); axL.set_ylim(0, 1); axL.axis("off")
axL.add_patch(Ellipse((0.5, 0.5), 0.94, 0.92, facecolor="#f3f3f3", edgecolor=GRAY, lw=0.7))
pts = r.uniform(0.2, 0.8, size=(rows + 10, 2))
axL.plot(pts[:, 0], pts[:, 1], "o", ms=2.2, color=GRAY, alpha=0.7)
wx, wy = 0.42, 0.58
axL.plot(wx, wy, "o", ms=5, color=ORANGE, mec="white", mew=0.5, zorder=5)
axL.text(wx + 0.07, wy, r"$\omega^*$", fontsize=8, color=ORANGE, ha="left", va="center")
axL.text(0.5, 0.17, "what happened", fontsize=7, color=INK, ha="center", va="center")
axL.set_title(r"$\Omega$: every complete outcome", fontsize=8.5, pad=4)

# ---- middle: data, one row per outcome
axM.set_xlim(-0.9, n + 0.3); axM.set_ylim(-1.0, rows + 0.3); axM.axis("off")
for i in range(rows):
    y = rows - 1 - i
    for j in range(n):
        v = data[i, j]
        face = BLUE if v == 1 else "white"
        axM.add_patch(Rectangle((j, y), 0.92, 0.82, facecolor=face, edgecolor=GRAY, lw=0.5, alpha=1.0 if i == star else 0.45))
        axM.text(j + 0.46, y + 0.41, str(v), ha="center", va="center", fontsize=6.5, color="white" if v == 1 else INK, alpha=1.0 if i == star else 0.6)
    if i == star:
        axM.add_patch(Rectangle((-0.1, y - 0.1), n + 0.1, 1.02, facecolor="none", edgecolor=ORANGE, lw=1.2, zorder=4))
axM.text(-0.35, rows - 1 - star + 0.41, r"$\omega^*$", ha="right", va="center", fontsize=8, color=ORANGE)
axM.text(n / 2, -0.6, r"$\vdots$  one row per outcome, $2^{n}$ rows", ha="center", va="center", fontsize=7, color=GRAY)
axM.set_title(r"data $X(\omega) \in E = \{0,1\}^n$", fontsize=8.5, pad=4)

# ---- right: the statistic and its distribution
k = np.arange(n + 1)
pm = binom_pmf(n, p)
axR.bar(k / n, pm, width=0.9 / n, color=BLUE, alpha=0.35, edgecolor="none")
obs = data[star].mean()
axR.bar(obs, pm[int(round(obs * n))], width=0.9 / n, color=ORANGE, edgecolor="none")
axR.set_xlim(-0.05, 1.08); axR.set_ylim(0, pm.max() * 1.3)
axR.set_yticks([])
axR.set_xticks([0, obs, 1])
axR.set_xticklabels([r"$0$", rf"$\bar r_n = {obs:.2f}$", r"$1$"], fontsize=7.5)
axR.spines["left"].set_visible(False)
axR.text(0.0, pm.max() * 1.27, r"its distribution over all $\omega$," + "\n" + r"weighted by $\mathbb{P}_p$", fontsize=7, color=INK, ha="left", va="top")
axR.set_title(r"statistic $\bar R_n(\omega)$", fontsize=8.5, pad=4)

# ---- arrows between the panels, mid-height, with their labels above
ymid = 0.52
for x0, x1, lab in [(0.255, 0.305, r"measure" + "\n" + r"$X_i(\omega)$"), (0.68, 0.74, r"compute" + "\n" + r"$\frac{1}{n}\sum_i X_i(\omega)$")]:
    fig.patches.append(FancyArrowPatch((x0, ymid), (x1, ymid), transform=fig.transFigure,
                                       arrowstyle="->", color=INK, lw=0.8, mutation_scale=8))
    fig.text((x0 + x1) / 2, ymid + 0.04, lab, ha="center", va="bottom", fontsize=7, color=INK)
fig.patches.append(FancyArrowPatch((0.87, 0.085), (0.13, 0.085), transform=fig.transFigure,
                                   arrowstyle="->", color=ORANGE, lw=0.8, ls="--", mutation_scale=8))
fig.text(0.5, 0.01, r"inference runs backwards: hold the one value $\bar r_n$ up against the whole distribution of $\bar R_n$",
         ha="center", va="bottom", fontsize=7.5, color=INK)
save(fig, "fig_sample_space_layers")
print("observed", obs)
