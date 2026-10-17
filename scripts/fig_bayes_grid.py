"""Bayes' formula on a grid, for the kiss data (80 right turns among 124
couples). The prior puts probability 1/9 on each of p = 0.1, 0.2, ..., 0.9.
Left: the likelihood p^80 (1 - p)^44, scaled to have maximum 1 (black curve),
and its values at the nine candidates (blue stems). Right: the prior (gray
bars) and the posterior (blue bars), which is prior times likelihood,
rescaled to add up to 1."""
from _style import *

n, S = 124, 80
grid = np.arange(1, 10) / 10
p = np.linspace(0.001, 0.999, 800)


def loglik(q):
    return S * np.log(q) + (n - S) * np.log(1 - q)


phat = S / n
lmax = loglik(np.array([phat]))[0]
lik = np.exp(loglik(p) - lmax)
likg = np.exp(loglik(grid) - lmax)
post = likg / likg.sum()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
ax1.plot(p, lik, color=INK, lw=1.1)
ax1.vlines(grid, 0, likg, color=BLUE, lw=2.0)
ax1.plot(grid, likg, "o", color=BLUE, ms=3.5)
ax1.set_xlim(0, 1); ax1.set_ylim(0, 1.08)
ax1.set_xticks(grid[::2].tolist())
ax1.set_xlabel(r"$p$"); ax1.set_ylabel("likelihood, scaled")
ax1.set_title("the likelihood at nine candidate values")

w = 0.032
ax2.bar(grid - w / 2 - 0.002, np.full(9, 1 / 9), width=w, color="#c9c9c9", edgecolor="none")
ax2.bar(grid + w / 2 + 0.002, post, width=w, color=BLUE, edgecolor="none")
for g, q in zip(grid, post):
    if q > 0.1:
        ax2.annotate(f"{q:.2f}", (g + w / 2, q), xytext=(0, 3),
                     textcoords="offset points", ha="center", va="bottom", fontsize=7.5, color=INK)
note(ax2, "0.005", (0.5 + w / 2 + 0.002, 0.006), (0.5 + w / 2 + 0.002, 0.17), ha="center")
note(ax2, "prior: 1/9 each", (0.2 - w / 2, 1 / 9), (0.08, 0.36), ha="left")
ax2.set_xlim(0.03, 0.97); ax2.set_ylim(0, 0.68)
ax2.set_xticks(grid[::2].tolist())
ax2.set_xlabel(r"$p$"); ax2.set_ylabel("probability")
ax2.set_title("prior and posterior")
save(fig, "fig_bayes_grid")
for g, q in zip(grid, post):
    print(f"p = {g:.1f}: likelihood ratio to the max {np.exp(loglik(np.array([g]))[0] - lmax):.3e}, posterior {q:.5f}")
