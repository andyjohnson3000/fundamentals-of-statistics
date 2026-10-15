"""Why the exact and the CLT thresholds for the kiss experiment differ. Left:
the upper tail of Bin(124, 1/2) (bars) and the Gaussian density the CLT
replaces it with (curve), mean 62, standard deviation sqrt(31) = 5.57. Right:
the tail probability P(count >= k) as a function of k: a staircase for the
exact distribution (it can only take the values at integers), a smooth curve
for the Gaussian. The exact one-sided threshold is the first step at or below
0.05 (k = 72, tail 0.044) and the two-sided one the first at or below 0.025
(k = 74, tail 0.019); the Gaussian curve crosses 0.05 at 71.2 and 0.025 at
72.9, which round up to 72 and 73. The discreteness, not the approximation,
makes the two-sided answers differ: the Gaussian tail at 73 is 0.024, the
exact tail is 0.029."""
from _style import *

n = 124
mu, sd = n / 2, math.sqrt(n / 4)
k = np.arange(n + 1)
pm = binom_pmf(n, 0.5)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

# ---- left: pmf vs density, upper tail
sel = (k >= 60) & (k <= 84)
ax1.bar(k[sel], pm[sel], width=0.85, color=BLUE, alpha=0.4, edgecolor="none")
x = np.linspace(60, 84, 400)
ax1.plot(x, norm_pdf(x, mu, sd), color=INK, lw=1.1)
for c, col, lab in [(72, ORANGE, "72"), (74, AQUA, "74")]:
    ax1.axvline(c - 0.5, color=col, lw=0.9, ls="--")
ax1.text(71.2, 0.088, "exact one-sided: 72", fontsize=7, color=INK, ha="right", va="top")
ax1.text(73.8, 0.088, "exact two-sided: 74", fontsize=7, color=INK, ha="left", va="top")
ax1.set_xlim(59.5, 84.5)
ax1.set_ylim(0, 0.09)
ax1.set_xlabel(r"count $n\bar R_n$")
ax1.set_ylabel("probability")
ax1.set_title("Upper tail under $p = \\frac{1}{2}$")

# ---- right: tail probability as a function of the threshold
ks = np.arange(64, 81)
exact = np.array([pm[j:].sum() for j in ks])
ax2.step(ks, exact, where="post", color=BLUE, lw=1.3, label=r"exact: $\Pr(n\bar R_n \geq k)$")
xx = np.linspace(64, 81, 400)
ax2.plot(xx, 1 - norm_cdf(xx, mu, sd), color=INK, lw=1.0, ls=DASHES[1], label=r"CLT: $\Pr(\mathrm{Gauss} \geq k)$")
for lev, lab in [(0.05, r"$0.05$, one-sided"), (0.025, r"$0.025$, two-sided")]:
    ax2.axhline(lev, color=GRAY, lw=0.6, ls=":")
    ax2.text(77.6, lev + 0.004, lab, fontsize=7, color=INK, ha="left", va="bottom")
for kk, col in [(72, ORANGE), (74, AQUA)]:
    ax2.plot(kk, pm[kk:].sum(), "o", ms=4, color=col, mec="white", mew=0.4, zorder=5)
ax2.plot([71.16, 72.91], [0.05, 0.025], "s", ms=3.5, color=INK, zorder=5)
ax2.text(73.9, 0.215, "Gaussian crosses $0.05$ at $71.2$\nand $0.025$ at $72.9$: round up to 72, 73", fontsize=7, color=INK, ha="left", va="top")
ax2.annotate("", xy=(72.95, 0.03), xytext=(74.3, 0.168), arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6, shrinkA=0, shrinkB=0))
ax2.text(74.8, 0.125, "exact: first step at or below each line\nis 72 (tail 0.044) and 74 (tail 0.019)", fontsize=7, color=INK, ha="left", va="top")
ax2.annotate("", xy=(74.1, 0.024), xytext=(75.2, 0.08), arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6, shrinkA=0, shrinkB=0))
ax2.set_xlim(64, 81)
ax2.set_ylim(0, 0.33)
ax2.set_xlabel(r"threshold $k$")
ax2.set_ylabel(r"$\Pr_{1/2}(\text{count} \geq k)$")
ax2.set_title("Tail probability vs threshold")
ax2.legend(loc="upper right", fontsize=7)
save(fig, "fig_exact_vs_clt")
print({j: round(pm[j:].sum(), 4) for j in (71, 72, 73, 74)}, "gauss tail 73:", 1 - norm_cdf(72.5 + 0.5, mu, sd), 1 - norm_cdf(73, mu, sd))
