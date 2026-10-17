"""How well the chi-squared approximation works for counts. For Mendel's
null p0 = (9, 3, 3, 1)/16 and every sample size n from 8 to 150, the exact
probability, under the null, that each statistic exceeds 7.81, the 95%
quantile of chi-squared with 3 degrees of freedom: Pearson's statistic
(the score statistic; aqua, dash-dot), the likelihood ratio statistic G^2
(blue) and Neyman's statistic (Wald's; orange, dashed), which divides by
the observed counts and is infinite when a cell is empty. The exact
probabilities come from summing the multinomial PMF over all possible
count vectors; the dotted line is the nominal 5%."""
from _style import *

p0 = np.array([9, 3, 3, 1]) / 16
Q3 = 7.814728
NMAX = 150
logfact = np.concatenate([[0.0], np.cumsum(np.log(np.arange(1, NMAX + 1)))])


def exact_sizes(n):
    a, b, c = np.mgrid[0:n + 1, 0:n + 1, 0:n + 1]
    keep = a + b + c <= n
    C = np.stack([a[keep], b[keep], c[keep], n - a[keep] - b[keep] - c[keep]], 1)
    logpmf = logfact[n] - logfact[C].sum(1) + (C * np.log(p0)).sum(1)
    pm = np.exp(logpmf)
    E = n * p0
    pear = ((C - E) ** 2 / E).sum(1)
    with np.errstate(divide="ignore", invalid="ignore"):
        g2 = 2 * np.where(C > 0, C * np.log(np.where(C > 0, C, 1) / E), 0.0).sum(1)
        ney = np.where((C > 0).all(1), ((C - E) ** 2 / np.where(C > 0, C, 1)).sum(1), np.inf)
    return pm.sum(), (pm * (pear > Q3)).sum(), (pm * (g2 > Q3)).sum(), (pm * (ney > Q3)).sum()


ns = np.arange(8, NMAX + 1)
res = np.array([exact_sizes(m) for m in ns])
assert np.allclose(res[:, 0], 1.0)
pear, g2, ney = res[:, 1], res[:, 2], res[:, 3]

fig, ax = plt.subplots(figsize=(4.9, 2.75), layout="constrained")
ax.plot(ns, ney, color=ORANGE, lw=1.1, ls=DASHES[1])
ax.plot(ns, g2, color=BLUE, lw=1.1)
ax.plot(ns, pear, color=AQUA, lw=1.1, ls=DASHES[2])
ax.axhline(0.05, color=GRAY, lw=0.8, ls=DASHES[3])
ax.set_xlim(0, NMAX); ax.set_ylim(0.0, 0.16)
ax.set_xlabel(r"number of peas $n$"); ax.set_ylabel("exact type 1 error")
ax.set_title("which statistic keeps its 5%?")
ax.text(92, 0.118, "Neyman (Wald)", fontsize=7.5, color=ORANGE, ha="left")
ax.text(106, 0.068, r"$G^2$ (likelihood ratio)", fontsize=7.5, color=BLUE, ha="left")
ax.text(58, 0.031, "Pearson (score)", fontsize=7.5, color=AQUA, ha="left")
save(fig, "fig_gof_sizes")
for m in [8, 16, 24, 32, 48, 64, 100, 150]:
    i = m - 8
    print(m, "Pearson", round(pear[i], 4), "G2", round(g2[i], 4), "Neyman", round(ney[i], 4))
print("Pearson range n>=8", pear.min(), pear.max(), "G2 range", g2.min(), g2.max())
print("Neyman at 40, 100, 150", ney[40 - 8], ney[100 - 8], ney[150 - 8])
