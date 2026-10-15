"""The Cramer-Rao bound for the kiss model at n = 124. Variance against p
for three unbiased or nearly unbiased estimators of p and the bound
1/(n I(p)) = p(1 - p)/n (black). The sample proportion sits exactly on the
bound: it is efficient. The first-observation estimator X_1 has variance
p(1 - p), 124 times larger (off the chart). The shrinkage estimator
(n R-bar + 10)/(n + 20) dips below the bound in the middle, which the bound
allows because it is biased there; its mean squared error (dashed) is what
a biased estimator should be judged by, and it crosses above the bound away
from p = 1/2."""
from _style import *

n = 124
p = np.linspace(0.02, 0.98, 400)
bound = p * (1 - p) / n
shr_var = n * p * (1 - p) / (n + 20) ** 2
shr_bias = (n * p + 10) / (n + 20) - p
shr_mse = shr_var + shr_bias ** 2
fig, ax = plt.subplots(figsize=(4.2, 2.9), layout="constrained")
ax.plot(p, bound * 1e3, color=INK, lw=1.8)
ax.plot(p, bound * 1e3, color=BLUE, lw=1.0, ls=DASHES[1])
ax.plot(p, shr_var * 1e3, color=ORANGE, lw=1.2)
ax.plot(p, shr_mse * 1e3, color=ORANGE, lw=1.2, ls=DASHES[2])
ax.set_xlim(0, 1); ax.set_ylim(0, 3.2)
ax.set_xlabel(r"$p$"); ax.set_ylabel(r"variance $\times 10^3$, $n = 124$")
ax.set_title(r"no unbiased estimator beats $1/(nI(p))$")
note(ax, "bound $p(1-p)/n$,\nand $\\bar R_n$ lies on it", (0.85, 0.85 * 0.15 / n * 1e3), (0.72, 2.2), ha="left")
note(ax, "shrinkage: variance", (0.5, shr_var[200] * 1e3), (0.33, 0.45), ha="left")
note(ax, "shrinkage: mean squared error", (0.68, shr_mse[np.argmin(np.abs(p - 0.68))] * 1e3), (0.5, 2.75), ha="center")
save(fig, "fig_cramer_rao")
