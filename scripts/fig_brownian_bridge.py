"""Donsker's theorem drawn for uniform data. Left: four realizations of the
random curve u -> sqrt(n)(G_n(u) - u), with G_n the empirical CDF of
n = 1,000 Unif(0, 1) draws; every curve starts and ends at 0, and the
dotted lines are at +-1.358, the 95% quantile of the largest absolute
value of a Brownian bridge. Right: sqrt(n) times the largest gap in 20,000
samples of n = 100 (histogram) and the density of Kolmogorov's limit
distribution, P(sup|B| <= x) = 1 - 2 sum_k (-1)^(k-1) exp(-2 k^2 x^2)
(black), with its 95% quantile 1.358 (dotted)."""
from _style import *

g = rng(1933)  # the year of Kolmogorov's paper
Q95 = 1.3581


def kolmogorov_pdf(x, terms=60):
    x = np.asarray(x, float)
    k = np.arange(1, terms + 1)[:, None]
    return np.sum((-1.0) ** (k - 1) * 8 * k ** 2 * x * np.exp(-2 * k ** 2 * x ** 2), axis=0)


def kolmogorov_sf(x, terms=60):
    k = np.arange(1, terms + 1)
    return float(2 * np.sum((-1.0) ** (k - 1) * np.exp(-2 * k ** 2 * x ** 2)))


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
n = 1000
for c, ls in zip(SERIES, DASHES):
    u = np.sort(g.random(n))
    uu = np.concatenate([[0], np.repeat(u, 2), [1]])
    gg = np.concatenate([[0, 0], np.repeat(np.arange(1, n) / n, 2), [1, 1]])
    ax1.plot(uu, np.sqrt(n) * (gg - uu), color=c, lw=0.9, ls=ls)
for s in (-1, 1):
    ax1.axhline(s * Q95, color=GRAY, lw=0.8, ls=DASHES[3])
ax1.axhline(0, color="#999999", lw=0.6)
ax1.set_xlim(0, 1); ax1.set_ylim(-1.9, 1.9)
ax1.set_xlabel(r"$u$"); ax1.set_ylabel(r"$\sqrt{n}\,(G_n(u) - u)$")
ax1.set_title("four bridges, pinned at 0 and 1")

m, M = 100, 20000
U = np.sort(g.random((M, m)), axis=1)
i = np.arange(1, m + 1)
D = np.maximum((i / m - U).max(1), (U - (i - 1) / m).max(1))
x = np.linspace(0.02, 2.4, 400)
ax2.hist(np.sqrt(m) * D, bins=np.arange(0.2, 2.45, 0.05), density=True, color=BLUE, alpha=0.55, edgecolor="none")
ax2.plot(x, kolmogorov_pdf(x), color=INK, lw=1.2)
ax2.axvline(Q95, color=GRAY, lw=0.8, ls=DASHES[3])
ax2.set_xlim(0.2, 2.4); ax2.set_ylim(0, 1.95)
ax2.set_xlabel(r"$\sqrt{n}\times$ largest gap"); ax2.set_ylabel("density")
ax2.set_title(r"the largest gap, $n = 100$")
note(ax2, "Kolmogorov's\nlimit", (1.08, float(kolmogorov_pdf(np.array([1.08]))[0])), (1.55, 1.55), ha="left")
note(ax2, "95% quantile 1.358", (Q95, 0.72), (1.52, 0.95), ha="left")
save(fig, "fig_brownian_bridge")
print("simulated P(sqrt(n)D > 1.358) at n = 100:", (np.sqrt(m) * D > Q95).mean())
print("limit sf at 1.358:", kolmogorov_sf(Q95), " sf at 1.224:", kolmogorov_sf(1.2238), " sf at 1.628:", kolmogorov_sf(1.6276))
print("simulated 95% quantile of sqrt(n)D at n=100:", np.quantile(np.sqrt(m) * D, 0.95))
