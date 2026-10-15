"""The course's four estimators of p on one axis, n = 124, p = 0.645: the
exact sampling distribution of each. Xbar_n (Binomial, scaled) is a narrow
spike at p; X_1 is two bars at 0 and 1 (unbiased, but never near p);
(X_1 + X_2)/2 is three bars; the sqrt-indicator is two bars at 0 and 1 with
mass p^2 = 0.42 at 1, centered at p^2 = 0.42 rather than at p (biased). One
picture explains both the bias table and the variance table."""
from _style import *

p, n = 0.645, 124
fig, axes = plt.subplots(4, 1, figsize=(6.0, 4.2), sharex=True)
k = np.arange(n + 1)
pm = binom_pmf(n, p)
rows = [
    (r"$\bar{X}_n$: bias $0$, var $p(1-p)/n = 0.0018$", k / n, pm, 0.9 / n),
    (r"$X_1$: bias $0$, var $p(1-p) = 0.229$", np.array([0, 1]), np.array([1 - p, p]), 0.02),
    (r"$(X_1 + X_2)/2$: bias $0$, var $p(1-p)/2 = 0.115$", np.array([0, 0.5, 1]), np.array([(1 - p) ** 2, 2 * p * (1 - p), p ** 2]), 0.02),
    (r"$\sqrt{\mathbb{1}(X_1 = 1, X_2 = 1)}$: bias $p^2 - p = -0.23$, var $p^2(1-p^2) = 0.243$", np.array([0, 1]), np.array([1 - p ** 2, p ** 2]), 0.02),
]
for ax, (title, x, m, w) in zip(axes, rows):
    ax.bar(x, m, width=w, color=BLUE, alpha=0.8, lw=0)
    mean = float(np.sum(x * m))
    ax.axvline(p, color=ORANGE, lw=1.0)
    ax.plot(mean, ax.get_ylim()[1] * 0.0, marker="^", ms=6, color=INK, clip_on=False)
    ax.text(0.01, 0.95, title, transform=ax.transAxes, fontsize=7.5, va="top", color=INK)
    ax.set_yticks([])
    ax.set_ylim(0, max(m) * 1.9)
axes[0].text(p + 0.01, axes[0].get_ylim()[1] * 0.55, r"true $p$", fontsize=7.5, color=ORANGE)
axes[3].text(p ** 2 + 0.015, axes[3].get_ylim()[1] * 0.12, r"mean $= p^2 = 0.42$", fontsize=7, color=INK, ha="left")
axes[-1].set_xlabel("value of the estimator (orange line: the truth; triangle: the estimator's mean)")
axes[-1].set_xlim(-0.05, 1.05)
fig.subplots_adjust(hspace=0.15)
save(fig, "fig_four_estimators")
