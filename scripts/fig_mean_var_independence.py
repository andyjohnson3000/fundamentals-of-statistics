"""The sample mean and sample variance of 4,000 samples of n = 5. Left:
Gauss(1, 1) data; the two are independent and the cloud shows no pattern.
Right: Expo(1) data, which also has mean 1 and variance 1; samples with a
large mean tend to have a large variance."""
from _style import *

g = rng(21)
reps, n = 4000, 5
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
X = g.standard_normal((reps, n)) + 1.0
ax1.scatter(X.mean(axis=1), X.var(axis=1, ddof=1), s=3, color=BLUE, alpha=0.35, linewidths=0)
ax1.set_xlim(-0.6, 2.6); ax1.set_ylim(0, 6)
ax1.set_xlabel(r"sample mean $\bar X_n$"); ax1.set_ylabel(r"sample variance $S_n^2$")
ax1.set_title("Gaussian data: no pattern")
E = g.exponential(1.0, (reps, n))
ax2.scatter(E.mean(axis=1), E.var(axis=1, ddof=1), s=3, color=ORANGE, alpha=0.35, linewidths=0)
ax2.set_xlim(-0.6, 2.6); ax2.set_ylim(0, 6)
ax2.set_xlabel(r"sample mean $\bar X_n$"); ax2.set_ylabel(r"sample variance $S_n^2$")
ax2.set_title("exponential data: mean and variance move together")
save(fig, "fig_mean_var_independence")
print("corr gauss", np.corrcoef(X.mean(axis=1), X.var(axis=1, ddof=1))[0, 1], "corr expo", np.corrcoef(E.mean(axis=1), E.var(axis=1, ddof=1))[0, 1])
