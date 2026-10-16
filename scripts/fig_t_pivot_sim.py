"""The standardized mean with an estimated standard deviation, for small
Gaussian samples. Left: a histogram of T = sqrt(n) (X-bar - mu) / S over
50,000 samples of n = 5 from Gauss(0, 1), with the standard Gaussian
density (black) and the t density with 4 degrees of freedom (orange,
dashed) over it. Right: the fraction of samples with |T| > 1.96, the
two-sided 5% rule of the Gaussian test, as a function of n; the dotted line
is the 5% it is supposed to be."""
from _style import *

g = rng(14)
reps = 50000

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

n = 5
x = g.standard_normal((reps, n))
T = np.sqrt(n) * x.mean(axis=1) / x.std(axis=1, ddof=1)
bins = np.linspace(-6, 6, 97)
ax1.hist(T, bins=bins, density=True, color=BLUE, alpha=0.55, edgecolor="none")
t = np.linspace(-6, 6, 600)
ax1.plot(t, norm_pdf(t), color=INK, lw=1.2)
k = n - 1
tpdf = math.gamma((k + 1) / 2) / (math.sqrt(k * math.pi) * math.gamma(k / 2)) * (1 + t ** 2 / k) ** (-(k + 1) / 2)
ax1.plot(t, tpdf, color=ORANGE, lw=1.3, ls=DASHES[1])
ax1.set_xlim(-6, 6); ax1.set_ylim(0, 0.43)
ax1.set_xlabel(r"$T = \sqrt{n}\,(\bar X_n - \mu)/S_n$, $n = 5$"); ax1.set_ylabel("density")
ax1.set_title("the Gaussian misses the tails")
note(ax1, "Gauss(0, 1)", (0.9, norm_pdf(0.9)), (2.4, 0.34), ha="left")
note(ax1, r"$t_4$ (dashed)", (-2.3, 0.07), (-5.8, 0.18), ha="left")
frac5 = np.mean(np.abs(T) > 1.96)

ns = np.arange(2, 61)
fr = []
for nn in ns:
    xx = g.standard_normal((20000, nn))
    TT = np.sqrt(nn) * xx.mean(axis=1) / xx.std(axis=1, ddof=1)
    fr.append(np.mean(np.abs(TT) > 1.96))
fr = np.array(fr)
ax2.plot(ns, fr, color=BLUE, lw=1.3)
ax2.axhline(0.05, color=GRAY, lw=0.9, ls=DASHES[3])
ax2.set_xlim(0, 60); ax2.set_ylim(0, 0.32)
ax2.set_xlabel(r"sample size $n$"); ax2.set_ylabel(r"fraction with $|T| > 1.96$")
ax2.set_title("how often the 5% rule rejects a true null")
i5 = np.where(ns == 5)[0][0]
ax2.plot([5], [fr[i5]], "o", ms=4, color=INK, zorder=5)
note(ax2, f"$n = 5$: {fr[i5]:.3f}\n({int(round(fr[i5]*1000))} of 1,000)", (5, fr[i5]), (14, 0.22), ha="left")
i30 = np.where(ns == 30)[0][0]
ax2.plot([30], [fr[i30]], "o", ms=4, color=INK, zorder=5)
note(ax2, f"$n = 30$: {fr[i30]:.3f}", (30, fr[i30]), (34, 0.13), ha="left")
ax2.text(58, 0.067, "5%", color=GRAY, fontsize=7.5, ha="right", va="bottom")
save(fig, "fig_t_pivot_sim")
print("n=5 fraction", frac5, "n=30", fr[i30], "n=2", fr[0], "n=10", fr[np.where(ns==10)[0][0]])
