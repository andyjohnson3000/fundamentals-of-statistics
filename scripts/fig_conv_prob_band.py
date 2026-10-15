"""Convergence in probability as a picture: the probability outside the epsilon
band around the limit shrinks to zero. Xbar_n of Exp(1) draws, mu = 1."""
from _style import *

eps = 0.3
ns = [5, 20, 100]
fig, axes = plt.subplots(1, 3, figsize=(6.0, 2.6), sharey=False)
x = np.linspace(0.001, 3.0, 3000)
for ax, n in zip(axes, ns):
    f = gamma_pdf(x, n, n)
    ax.plot(x, f, color=BLUE)
    out = (x <= 1 - eps) | (x >= 1 + eps)
    ax.fill_between(x, 0, f, where=out, color=ORANGE, alpha=0.45, lw=0)
    ax.fill_between(x, 0, f, where=~out, color=BLUE, alpha=0.10, lw=0)
    ax.axvline(1 - eps, color=GRAY, lw=0.6, ls="--")
    ax.axvline(1 + eps, color=GRAY, lw=0.6, ls="--")
    p_out = gamma_tail_outside(n, n, 1 - eps, 1 + eps)
    ax.set_title(rf"$n = {n}$" + "\n" + rf"$\Pr(|\bar{{X}}_n - \mu| \geq \epsilon) = {p_out:.3f}$", fontsize=8.5)
    ax.set_xlim(0, 2.5)
    ax.set_xlabel(r"$\bar{X}_n$")
    ax.set_xticks([1 - eps, 1 + eps])
    ax.set_xticklabels([r"$\mu-\epsilon$", r"$\mu+\epsilon$"])
    ax.axvline(1, color=GRAY, lw=0.5)
axes[0].set_ylabel("density")
save(fig, "fig_conv_prob_band")
