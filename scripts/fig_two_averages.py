"""Two kinds of averaging. Rows are repetitions of the experiment, columns are
the n draws within one repetition. Averaging along a row gives that
repetition's sample mean Xbar_n (right margin); averaging the row means down
the column, over all repetitions weighted by their probabilities, is the
expectation E[Xbar_n], which equals mu. Drawn for Bern(0.645) with n = 10 and
8 repetitions shown of the infinitely many the expectation averages over."""
from _style import *

p, n, reps = 0.645, 10, 8
r = rng(21)
X = r.binomial(1, p, size=(reps, n))
rowmeans = X.mean(axis=1)

fig, ax = plt.subplots(figsize=(6.0, 3.0))
ax.set_xlim(-4.2, n + 3.6)
ax.set_ylim(-2.3, reps + 0.6)
ax.axis("off")

for i in range(reps):
    y = reps - 1 - i
    for j in range(n):
        col = BLUE if X[i, j] == 1 else "white"
        ax.add_patch(plt.Rectangle((j, y), 0.9, 0.85, facecolor=col, edgecolor=GRAY, lw=0.6))
        ax.text(j + 0.45, y + 0.42, str(X[i, j]), ha="center", va="center", fontsize=7.5,
                color="white" if X[i, j] == 1 else INK)
    ax.text(-0.3, y + 0.42, f"run {i + 1}", ha="right", va="center", fontsize=7.5, color=INK)
    ax.annotate("", xy=(n + 0.25, y + 0.42), xytext=(n - 0.05, y + 0.42),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=0.7))
    ax.text(n + 0.4, y + 0.42, rf"$\bar{{x}}_{{10}} = {rowmeans[i]:.1f}$", ha="left", va="center", fontsize=7.5, color=INK)

ax.text(n / 2 - 0.05, reps + 0.25, r"the $n$ draws of one experiment $\longrightarrow$ average along the row: $\bar{X}_n$",
        ha="center", va="bottom", fontsize=8, color=INK)
ax.text(-2.3, reps / 2 - 0.1, "repetitions\n(all possible\noutcomes,\nweighted by\nprobability)", ha="right", va="center", fontsize=7, color=INK)
ax.annotate("", xy=(-1.9, -0.2), xytext=(-1.9, reps - 0.3), arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=0.7))
ax.text(n + 0.4, -0.75, r"$\vdots$", ha="left", va="center", fontsize=9, color=INK)
ax.text(n + 0.4, -1.7, r"average down the column: $\mathbb{E}[\bar{X}_n] = p = 0.645$", ha="left", va="center", fontsize=8, color=INK)
ax.annotate("", xy=(n + 1.2, -1.35), xytext=(n + 1.2, -0.3), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=0.7))
save(fig, "fig_two_averages")
