"""One degree of freedom per estimated parameter. 20,000 samples of n = 1,000
from Pois(1), each reduced to the counts in three cells {0}, {1} and
{2 or more}. Left: Pearson's statistic computed with the true lambda = 1
(histogram) and the chi-squared density with 2 degrees of freedom (black).
Right: Pearson's statistic computed with lambda estimated by maximum
likelihood from the three counts (histogram), the chi-squared density with
1 degree of freedom (black) and, for comparison, the one with 2 (gray,
dashed). Also printed: the type 1 errors when lambda is estimated by the
sample mean of the raw data instead (the Chernoff-Lehmann case)."""
from _style import *

g = rng(1954)
n, M, lam = 1000, 20000, 1.0
KMAX = 25  # values above 25 have probability below 1e-25 under Pois(1)
pk = np.array([math.exp(-lam) * lam ** k / math.factorial(k) for k in range(KMAX)])
pk = np.append(pk, 1 - pk.sum())
NK = g.multinomial(n, pk, M)  # how many of the n observations equal 0, 1, ..., KMAX
C = np.stack([NK[:, 0], NK[:, 1], NK[:, 2:].sum(1)], 1).astype(float)
xbar = (NK * np.arange(KMAX + 1)).sum(1) / n


def cellp(l):
    l = np.asarray(l, float)[..., None]
    e = np.exp(-l)
    return np.concatenate([e, l * e, 1 - e - l * e], -1)


def pearson(C, p):
    E = n * p
    return ((C - E) ** 2 / E).sum(-1)


def grouped_mle(C):
    lo, hi = np.full(len(C), 1e-4), np.full(len(C), 20.0)
    N0, N1, N2 = C[:, 0], C[:, 1], C[:, 2]
    def score(l):
        return -N0 + N1 / l - N1 + N2 * l * np.exp(-l) / (1 - np.exp(-l) * (1 + l))
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        pos = score(mid) > 0
        lo = np.where(pos, mid, lo); hi = np.where(pos, hi, mid)
    return 0.5 * (lo + hi)


T_known = pearson(C, cellp(np.full(M, lam)))
lam_g = grouped_mle(C)
T_group = pearson(C, cellp(lam_g))
T_raw = pearson(C, cellp(xbar))
Q1, Q2 = 3.841459, 5.991465

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
bins = np.arange(0, 10.25, 0.25)
v = np.linspace(0.02, 10, 500)
ax1.hist(T_known, bins=bins, density=True, color=BLUE, alpha=0.55, edgecolor="none")
ax1.plot(v, gamma_pdf(v, 1.0, 0.5), color=INK, lw=1.2)
ax1.set_xlim(0, 10); ax1.set_ylim(0, 0.6)
ax1.set_xlabel("Pearson's statistic"); ax1.set_ylabel("density")
ax1.set_title(r"$\lambda$ known")
note(ax1, r"$\chi^2_2$ density", (2.6, 0.5 * math.exp(-1.3)), (4.4, 0.33), ha="left")

ax2.hist(T_group, bins=bins, density=True, color=ORANGE, alpha=0.5, edgecolor="none")
ax2.plot(v, gamma_pdf(v, 0.5, 0.5), color=INK, lw=1.2)
ax2.plot(v, gamma_pdf(v, 1.0, 0.5), color=GRAY, lw=0.9, ls=DASHES[1])
ax2.set_xlim(0, 10); ax2.set_ylim(0, 1.7)
ax2.set_ylabel("density")
ax2.set_xlabel("Pearson's statistic")
ax2.set_title(r"$\lambda$ estimated from the counts")
f1 = gamma_pdf(np.array([0.12]), 0.5, 0.5)[0]
note(ax2, r"$\chi^2_1$ density", (0.12, f1), (1.0, 1.3), ha="left")
note(ax2, r"$\chi^2_2$, for comparison", (4.0, 0.5 * math.exp(-2.0)), (5.2, 0.5), ha="left")
save(fig, "fig_gof_estimated")
print("known, df 2:", (T_known > Q2).mean())
print("grouped MLE, df 1:", (T_group > Q1).mean(), " df 2:", (T_group > Q2).mean())
print("raw mean, df 1:", (T_raw > Q1).mean(), " df 2:", (T_raw > Q2).mean())
print("known, wrongly df 1:", (T_known > Q1).mean())
print("mean of T: known", T_known.mean(), "grouped", T_group.mean(), "raw", T_raw.mean())
