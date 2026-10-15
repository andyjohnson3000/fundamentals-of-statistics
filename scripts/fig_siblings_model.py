"""The course's siblings example. The 24 values the slides show (number of
siblings including self, college students) as an empirical pmf, against the
one-parameter model X - 1 ~ Pois(lambda) with lambda estimated by the sample
mean minus 1. Seven free numbers versus one."""
from _style import *

data = [2, 3, 2, 4, 1, 3, 1, 1, 1, 1, 1, 2, 2, 3, 2, 2, 2, 3, 2, 1, 3, 1, 2, 3]
n = len(data)
vals = np.arange(1, 8)
emp = np.array([sum(1 for d in data if d == v) for v in vals]) / n
lam = np.mean(data) - 1
pois = np.array([math.exp(-lam) * lam ** (v - 1) / math.factorial(v - 1) for v in vals])
pois[-1] = 1 - pois[:-1].sum()   # last bin is the tail P(X >= 7), as its label says

fig, ax = plt.subplots(figsize=(4.8, 2.9))
w = 0.38
ax.bar(vals - w / 2, emp, width=w, color=BLUE, alpha=0.8, lw=0, label=rf"data, $n = {n}$ (7 cells, 6 free numbers)")
ax.bar(vals + w / 2, pois, width=w, color=ORANGE, alpha=0.8, lw=0,
       label=rf"$X - 1 \sim \mathrm{{Pois}}(\hat\lambda)$, $\hat\lambda = {lam:.1f}$ (1 number)")
ax.set_xticks(vals)
ax.set_xticklabels(["1", "2", "3", "4", "5", "6", r"$\geq 7$"])
ax.set_xlabel("number of siblings, including self")
ax.set_ylabel("probability")
ax.legend(fontsize=7.5)
save(fig, "fig_siblings_model")
