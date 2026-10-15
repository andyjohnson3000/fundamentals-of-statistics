"""Consistency of the MLE for the kiss model. Top row: the average
log-likelihood (1/n) l_n(p) for one simulated sample of n couples (color)
against its limit E_{p*}[log p_p(R)] (black), which is a constant minus
KL(Bern(p*), Bern(p)) and is maximized at the truth p* = 0.645. At n = 10
the random curve peaks well away from p*; at n = 1000 the two curves are
indistinguishable. Bottom row: the sampling distribution of p-hat at the
same n, from 20,000 simulated studies, with standard deviation
sqrt(p*(1 - p*)/n): 0.151, 0.043, 0.015."""
from _style import *

ps = 0.645
r = rng(3)
q = np.linspace(0.3, 0.95, 500)
lim = ps * np.log(q) + (1 - ps) * np.log(1 - q)
fig, axes = plt.subplots(2, 3, figsize=(6.0, 4.2), layout="constrained")
ns = [10, 124, 1000]
sds = [0.151, 0.043, 0.015]
for j, n in enumerate(ns):
    ax = axes[0, j]
    ph = r.binomial(n, ps) / n
    avg = ph * np.log(q) + (1 - ph) * np.log(1 - q)
    ax.plot(q, lim, color=INK, lw=1.6)
    ax.plot(q, avg, color=BLUE, lw=1.2, ls=DASHES[1])
    ax.plot([ph], [ph * np.log(ph) + (1 - ph) * np.log(1 - ph)], "o", ms=4, color=BLUE, mec="white", mew=0.4, zorder=5)
    ax.plot([ps], [ps * np.log(ps) + (1 - ps) * np.log(1 - ps)], "o", ms=4, color=INK, zorder=5)
    ax.axvline(ps, color=INK, lw=0.5, ls=":")
    ax.set_xlim(0.3, 0.95); ax.set_ylim(-1.05, -0.45)
    ax.set_title(rf"$n = {n}$: $\hat p = {ph:.3f}$")
    if j == 0:
        ax.set_ylabel(r"$\frac{1}{n}\,\ell_n(p)$")
        ax.text(0.60, -1.03, "limit (black)\nsample (blue)", fontsize=7.5, color=INK, va="bottom", ha="right")
    ax.set_xticks([0.4, 0.645, 0.9]); ax.set_xticklabels(["0.4", r"$p^*$", "0.9"])
    ax = axes[1, j]
    sims = r.binomial(n, ps, 20000) / n
    if n == 10:
        vals, counts = np.unique(sims, return_counts=True)
        ax.bar(vals, counts / 20000, width=0.08, color=BLUE, alpha=0.6, edgecolor="none"); ax.set_ylim(0, 0.32)
    else:
        ax.hist(sims, bins=np.arange(0.3, 1.0, 0.01), color=BLUE, alpha=0.6, edgecolor="none")
    ax.axvline(ps, color=INK, lw=0.8, ls=":")
    ax.set_xlim(0.3, 1.0); ax.set_yticks([])
    ax.set_xticks([0.4, 0.645, 0.9]); ax.set_xticklabels(["0.4", r"$p^*$", "0.9"])
    ax.set_xlabel(r"$\hat p$ over $20{,}000$ studies")
    ax.set_title(rf"sd of $\hat p$: ${sds[j]}$")
save(fig, "fig_mle_consistency")
