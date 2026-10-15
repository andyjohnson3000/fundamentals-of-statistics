"""The Fisher information of three one-parameter families, and what it
says about precision. Left: I(lambda) = 1/lambda^2 for Expo(lambda), large for
small rates: when gaps are long, a few of them pin down the rate well in
absolute terms. Middle: I(lambda) = 1/lambda for Pois(lambda). Right: the
width of the 95% interval for the MLE, 2 x 1.96/sqrt(n I(theta)), at n = 100,
for the three families on their own parameter scales; where I is large the
interval is narrow."""
from _style import *

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(6.0, 2.4), layout="constrained")
lam = np.linspace(0.1, 3, 300)
ax1.plot(lam, 1 / lam ** 2, color=BLUE, lw=1.4)
ax1.set_ylim(0, 25); ax1.set_xlabel(r"$\lambda$"); ax1.set_title(r"$\mathrm{Expo}(\lambda)$: $I = 1/\lambda^2$")
ax1.text(1.0, 23, r"subway rate $0.16$:" + "\n" + r"$I = 38.8$, off the chart", fontsize=7.5, color=INK, va="top")
ax2.plot(lam, 1 / lam, color=BLUE, lw=1.4)
ax2.set_ylim(0, 10); ax2.set_xlabel(r"$\lambda$"); ax2.set_title(r"$\mathrm{Pois}(\lambda)$: $I = 1/\lambda$")
ax2.plot([1.0], [1.0], "o", ms=4, color=ORANGE)
note(ax2, r"siblings $\hat\lambda = 1$: $I = 1$", (1.0, 1.0), (1.3, 5), ha="left")
pp = np.linspace(0.02, 0.98, 300)
n = 100
ax3.plot(pp, 2 * 1.96 * np.sqrt(pp * (1 - pp) / n), color=BLUE, lw=1.4)
ax3.set_ylim(0, 0.25); ax3.set_xlabel(r"$p$"); ax3.set_title(r"$\mathrm{Bern}(p)$, $n = 100$: interval width")
ax3.set_ylabel(r"$2 \times 1.96/\sqrt{n I(p)}$")
ax3.plot([0.645], [2 * 1.96 * np.sqrt(0.645 * 0.355 / n)], "o", ms=4, color=ORANGE)
note(ax3, r"$p = 0.645$: width $0.19$", (0.645, 2 * 1.96 * np.sqrt(0.645 * 0.355 / n)), (0.98, 0.115), ha="right")
save(fig, "fig_fisher_families")
