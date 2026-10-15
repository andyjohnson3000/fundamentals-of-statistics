"""The sample mean against the sample median as estimators of the center,
for three symmetric distributions, n = 100, 20,000 simulated samples each.
Gaussian: the mean wins (sd 0.100 against 0.125). Laplace: the median wins
(0.108 against 0.141). Cauchy: the mean does not settle at all (its
histogram is shown on the same axis and spills off both ends), while the
median has sd 0.159. The theoretical asymptotic variances are 1 and pi/2;
2 and 1; undefined and pi^2/4."""
from _style import *

r = rng(2)
n, S = 100, 20000
fig, axes = plt.subplots(1, 3, figsize=(6.0, 2.4), layout="constrained")
gens = [("Gaussian", r.normal(0, 1, (S, n))), ("Laplace", r.laplace(0, 1, (S, n))), ("Cauchy", r.standard_cauchy((S, n)))]
for ax, (name, x) in zip(axes, gens):
    m, md = x.mean(1), np.median(x, 1)
    bins = np.linspace(-0.6, 0.6, 61)
    ax.hist(m, bins=bins, density=True, color=BLUE, alpha=0.5, edgecolor="none")
    ax.hist(md, bins=bins, density=True, color=ORANGE, alpha=0.5, edgecolor="none")
    ax.set_xlim(-0.6, 0.6); ax.set_yticks([])
    ax.set_title(name)
    ax.set_xlabel("estimate of the center")
    top = ax.get_ylim()[1]
    ax.set_ylim(0, top * 1.35)
    if name != "Cauchy":
        ax.text(-0.58, top * 1.32, rf"mean: sd ${m.std():.3f}$", color=BLUE, fontsize=7.5, va="top")
        ax.text(-0.58, top * 1.17, rf"median: sd ${md.std():.3f}$", color=ORANGE, fontsize=7.5, va="top")
    else:
        ax.text(-0.58, top * 1.32, "mean: sd $72$, off the chart", color=BLUE, fontsize=7.5, va="top")
        ax.text(-0.58, top * 1.17, rf"median: sd ${md.std():.3f}$", color=ORANGE, fontsize=7.5, va="top")
    print(name, m.std(), md.std())
save(fig, "fig_robust_mean_median")
