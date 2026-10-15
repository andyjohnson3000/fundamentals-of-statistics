"""Two views of the same sample mean: collapsing on mu (LLN) and stabilizing after
the sqrt(n) magnification (CLT). X_i ~ Exp(1), so Xbar_n ~ Gamma(n, n)."""
from _style import *

ns = [1, 4, 16, 64]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

x = np.linspace(0.001, 3.0, 2000)
for k, n in enumerate(ns):
    f = gamma_pdf(x, n, n)
    ax1.plot(x, f, color=SERIES[k], ls=DASHES[k], label=rf"$n={n}$")
ax1.axvline(1, color=GRAY, lw=0.7)
# label beside the top of the vertical line, above every curve (the n = 64 peak is 3.19)
ax1.set_ylim(-0.16, 3.7)
ax1.text(1.04, 3.5, r"$\mu = 1$", ha="left", va="center", fontsize=7.5, color=INK)
ax1.set_title(r"Density of $\bar{X}_n$: it collapses on $\mu$")
ax1.set_xlabel(r"$\bar{X}_n$")
ax1.set_ylabel("density")
ax1.legend()

y = np.linspace(-3.5, 4.5, 2000)
for k, n in enumerate(ns):
    # Y = sqrt(n) (Xbar - 1)  =>  f_Y(y) = f_Xbar(1 + y/sqrt(n)) / sqrt(n)
    f = gamma_pdf(1 + y / math.sqrt(n), n, n) / math.sqrt(n)
    ax2.plot(y, f, color=SERIES[k], ls=DASHES[k], label=rf"$n={n}$")
ax2.plot(y, norm_pdf(y), color=INK, lw=1.0, ls=(0, (1, 1)), label=r"$\mathrm{Gauss}(0,\sigma^2)$")
ax2.set_title(r"Density of $\sqrt{n}(\bar{X}_n - \mu)$: it settles down")
ax2.set_xlabel(r"$\sqrt{n}(\bar{X}_n - \mu)$")
ax2.legend()

save(fig, "fig_lln_clt_two_views")
