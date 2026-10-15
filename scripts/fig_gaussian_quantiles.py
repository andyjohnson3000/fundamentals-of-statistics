"""Quantiles of the standard Gaussian in this book's convention: q_alpha is the
number with alpha of the mass to its RIGHT. Left: one-sided, alpha = 5%.
Right: two-sided, alpha/2 = 2.5% in each tail, so the central region holds
1 - alpha = 95%."""
from _style import *

z = np.linspace(-4, 4, 800)
f = norm_pdf(z)
q05, q025 = 1.6449, 1.9600

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, sharey=True)

ax1.plot(z, f, color=INK, lw=1.2)
ax1.fill_between(z, 0, f, where=z <= q05, color=BLUE, alpha=0.18, lw=0)
ax1.fill_between(z, 0, f, where=z >= q05, color=ORANGE, alpha=0.55, lw=0)
ax1.axvline(q05, color=GRAY, lw=0.7, ls="--")
ax1.text(-0.2, 0.17, r"$1 - \alpha = 0.95$", ha="center", fontsize=9, color=INK)
ax1.annotate(r"$\alpha = 0.05$", (2.2, 0.02), xytext=(2.4, 0.09), fontsize=9, color=INK,
             arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6))
ax1.set_xticks([-2, 0, q05])
ax1.set_xticklabels([r"$-2$", r"$0$", r"$q_{0.05} = 1.645$"])
ax1.set_title(r"One-sided: $\Pr(Z > q_\alpha) = \alpha$")
ax1.set_yticks([])
ax1.grid(False)

ax2.plot(z, f, color=INK, lw=1.2)
ax2.fill_between(z, 0, f, where=np.abs(z) <= q025, color=BLUE, alpha=0.18, lw=0)
ax2.fill_between(z, 0, f, where=np.abs(z) >= q025, color=ORANGE, alpha=0.55, lw=0)
for s in (-q025, q025):
    ax2.axvline(s, color=GRAY, lw=0.7, ls="--")
ax2.text(0, 0.17, r"$1 - \alpha = 0.95$", ha="center", fontsize=9, color=INK)
ax2.annotate(r"$\alpha/2 = 0.025$", (2.4, 0.012), xytext=(2.3, 0.07), fontsize=9, color=INK,
             arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6))
ax2.annotate(r"$\alpha/2 = 0.025$", (-2.4, 0.012), xytext=(-4.1, 0.07), fontsize=9, color=INK,
             arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6))
ax2.set_xticks([-q025, 0, q025])
ax2.set_xticklabels([r"$-q_{\alpha/2}$", r"$0$", r"$q_{\alpha/2} = 1.96$"])
ax2.set_title(r"Two-sided: $\Pr(|Z| > q_{\alpha/2}) = \alpha$")
ax2.grid(False)
save(fig, "fig_gaussian_quantiles")
