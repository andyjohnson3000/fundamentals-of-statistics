"""Many tests at once. Left: the p-values of 8,064 two-sided t-tests on
samples of n = 15 from Gauss(0, 1), so every null is true; the histogram is
flat, and the bar below p = 0.001 (orange) holds the false discoveries.
Right: ten sorted p-values with the Bonferroni line p = alpha/N (dotted)
and the Benjamini-Hochberg line p = i alpha/N (dashed), alpha = 5%; filled
dots are the tests Benjamini-Hochberg rejects."""
from _style import *
from math import gamma, sqrt, pi

def t_pdf(t, k):
    return gamma((k + 1) / 2) / (sqrt(k * pi) * gamma(k / 2)) * (1 + t ** 2 / k) ** (-(k + 1) / 2)

def t_sf_vec(x, k):
    """P(T > x) for an array x, by integrating the density on a fine grid up to 60 and a tail bound."""
    u = np.linspace(0, 60, 240001)
    f = t_pdf(u, k)
    cdf_from0 = np.concatenate([[0], np.cumsum(0.5 * (f[1:] + f[:-1]) * np.diff(u))])
    return 0.5 - np.interp(x, u, cdf_from0)

g = rng(2009)
N, n = 8064, 15
X = g.standard_normal((N, n))
T = np.sqrt(n) * X.mean(axis=1) / X.std(axis=1, ddof=1)
P = 2 * t_sf_vec(np.abs(T), n - 1)
nfalse = int(np.sum(P < 0.001))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
bins = np.linspace(0, 1, 51)
ax1.hist(P, bins=bins, color=BLUE, alpha=0.55, edgecolor="none")
ax1.axhline(N / 50, color=GRAY, lw=0.8, ls=DASHES[3])
ax1.set_xlim(0, 1); ax1.set_ylim(0, 420)
ax1.set_xlabel(r"$p$-value"); ax1.set_ylabel("count of tests")
ax1.set_title(r"8,064 tests, every null true")
# inset: the p-values below 0.02, bins of width 0.001, the first bin in orange
ins = ax1.inset_axes([0.27, 0.53, 0.70, 0.43])
ins.set_facecolor("white")
fine = np.linspace(0, 0.02, 21)
counts, _ = np.histogram(P, bins=fine)
ins.bar(fine[:-1], counts, width=0.001, align="edge", color=BLUE, alpha=0.55, edgecolor="none")
ins.bar([0.0], [counts[0]], width=0.001, align="edge", color=ORANGE, edgecolor="none")
ins.set_xlim(0, 0.02); ins.set_ylim(0, max(counts) * 1.55)
ins.set_xticks([0, 0.005, 0.01, 0.015, 0.02]); ins.tick_params(labelsize=6.5)
ins.set_title(r"$p$-values below $0.02$", fontsize=7.5)
ins.grid(False)
ins.text(0.0012, max(counts) * 1.12, f"{nfalse} below $0.001$ (orange)", fontsize=7, color=INK, va="bottom", ha="left")

p10 = np.array([0.001, 0.008, 0.012, 0.03, 0.06, 0.2, 0.35, 0.5, 0.7, 0.9])
alpha, M = 0.05, 10
i = np.arange(1, M + 1)
bh = i * alpha / M
imax = max(j for j in i if p10[j - 1] <= bh[j - 1])
ax2.plot(i, bh, color=ORANGE, lw=1.1, ls=DASHES[1])
ax2.axhline(alpha / M, color=AQUA, lw=1.1, ls=DASHES[3])
rej = i <= imax
ax2.plot(i[rej], p10[rej], "o", ms=5, color=BLUE, zorder=5)
ax2.plot(i[~rej], p10[~rej], "o", ms=5, markerfacecolor="white", markeredgecolor=BLUE, zorder=5)
ax2.set_xlim(0.5, 10.5); ax2.set_ylim(0, 0.075)
ax2.set_xticks(i)
ax2.set_xlabel(r"rank $i$ of the $p$-value"); ax2.set_ylabel(r"sorted $p$-value $P_{(i)}$")
ax2.set_title("Bonferroni against Benjamini\u2013Hochberg, $N = 10$")
ax2.text(7.6, 0.027, r"BH: $i\alpha/N$", color=ORANGE, fontsize=7.5, ha="left", va="center")
ax2.text(10.3, alpha / M + 0.001, r"Bonferroni: $\alpha/N$", color=AQUA, fontsize=7.5, ha="right", va="bottom")
note(ax2, "rejected by BH", (3, p10[2]), (1.0, 0.045), ha="left")
save(fig, "fig_multiple_testing")
print("false discoveries", nfalse, "min p", P.min(), "imax", imax, "frac<0.05", np.mean(P < 0.05))
