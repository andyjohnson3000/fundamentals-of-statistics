"""Estimating the parameters changes the null distribution. Left: for
20,000 Gaussian samples of n = 50, the Kolmogorov-Smirnov gap sqrt(n) D_n
to the true Gaussian CDF (blue histogram) and the gap sqrt(n) D-hat_n to
the Gaussian with the sample mean and standard deviation plugged in
(orange histogram), with the 95% quantile of each (dotted; exact for the
first, simulated for the second). Right: the 272
waiting times between eruptions of Old Faithful (empirical CDF, blue)
against the Gaussian CDF with their mean 70.9 and standard deviation 13.6
plugged in (black); the largest gap, 0.155 at 75 minutes, in orange."""
from _style import *
import csv

g = rng(1967)  # the year of Lilliefors' paper
erf = np.frompyfunc(math.erf, 1, 1)


def Phi(x):
    return 0.5 * (1 + erf(np.asarray(x) / math.sqrt(2)).astype(float))


n, M = 50, 20000
i = np.arange(1, n + 1)
Z = np.sort(g.standard_normal((M, n)), axis=1)
U = Phi(Z)
D = np.maximum((i / n - U).max(1), (U - (i - 1) / n).max(1))
m = Z.mean(1, keepdims=True)
s = Z.std(1, ddof=1, keepdims=True)
Uh = Phi((Z - m) / s)
Dh = np.maximum((i / n - Uh).max(1), (Uh - (i - 1) / n).max(1))
# 95% points: the exact one for D_50 (0.18841, from Marsaglia, Tsang and Wang's
# algorithm for the exact distribution), and the simulated one for D-hat_50
qks, qli = np.sqrt(n) * 0.18841, np.quantile(np.sqrt(n) * Dh, 0.95)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
bins = np.arange(0.2, 2.4, 0.04)
ax1.hist(np.sqrt(n) * D, bins=bins, density=True, color=BLUE, alpha=0.5, edgecolor="none")
ax1.hist(np.sqrt(n) * Dh, bins=bins, density=True, color=ORANGE, alpha=0.5, edgecolor="none")
for q in (qks, qli):
    ax1.axvline(q, color=GRAY, lw=0.8, ls=DASHES[3])
ax1.set_xlim(0.2, 2.2); ax1.set_ylim(0, 3.3)
ax1.set_xlabel(r"$\sqrt{n}\times$ largest gap"); ax1.set_ylabel("density")
ax1.set_title(r"two null distributions, $n = 50$")
note(ax1, "parameters\nestimated", (0.71, 2.2), (1.45, 2.85), ha="left")
note(ax1, "parameters\nknown", (1.12, 0.95), (1.55, 1.75), ha="left")

w = []
with open(os.path.join(os.path.dirname(HERE), "data", "old_faithful.csv")) as f:
    for row in csv.DictReader(f):
        w.append(float(row["waiting"]))
w = np.sort(np.array(w))
N = len(w)
mu, sd = w.mean(), w.std(ddof=1)
k = np.arange(1, N + 1)
uf = Phi((w - mu) / sd)
gaps_above = k / N - uf
gaps_below = uf - (k - 1) / N
j = int(np.argmax(np.maximum(gaps_above, gaps_below)))
Dfa = max(gaps_above.max(), gaps_below.max())
t = np.linspace(40, 100, 400)
xs = np.concatenate([[40], np.repeat(w, 2), [100]])
ys = np.concatenate([[0, 0], np.repeat(k[:-1] / N, 2), [1, 1]])
ax2.plot(t, Phi((t - mu) / sd), color=INK, lw=1.1)
ax2.plot(xs, ys, color=BLUE, lw=1.1)
lo_j = (k[j] - 1) / N if gaps_below[j] >= gaps_above[j] else k[j] / N
ax2.plot([w[j], w[j]], [lo_j, uf[j]], color=ORANGE, lw=2.2, solid_capstyle="butt")
ax2.set_xlim(40, 100); ax2.set_ylim(0, 1.02)
ax2.set_xlabel("minutes between eruptions")
ax2.set_title("Old Faithful against its fitted Gaussian")
note(ax2, f"gap {Dfa:.3f}", (w[j] + 0.4, (lo_j + uf[j]) / 2), (82, 0.33), ha="left")
save(fig, "fig_lilliefors")
print("KS 95%", qks, "Lilliefors 95%", qli, "P(sqrt(n)Dh > KS threshold)", (np.sqrt(n) * Dh > qks).mean())
print("Old Faithful: mean", mu, "sd", sd, "D-hat", Dfa, "at", w[j], "F_n before", (k[j] - 1) / N, "F_n at", k[j] / N, "Phi", uf[j])
