"""The data outweigh the prior. Posteriors from the flat prior (blue, solid),
Beta(10, 10) (orange, dashed) and the skeptic's Beta(33, 33) (aqua,
dash-dot), with the Gaussian Gauss(p-hat, p-hat(1 - p-hat)/n) of the
Bernstein-von Mises theorem (black, dotted). Left: the kiss data, 80 right
turns among n = 124 couples. Right: ten times as many couples with the same
proportion, 800 among 1,240."""
from _style import *

priors = [(1, 1), (10, 10), (33, 33)]
p = np.linspace(0.3, 0.9, 2000)
fig, axes = plt.subplots(1, 2, figsize=FULL, layout="constrained")
for ax, (n, S) in zip(axes, ((124, 80), (1240, 800))):
    for (a, b), c, ls in zip(priors, SERIES, DASHES):
        ax.plot(p, beta_pdf(p, a + S, b + n - S), color=c, ls=ls, lw=1.3)
    ph = S / n
    ax.plot(p, norm_pdf(p, ph, math.sqrt(ph * (1 - ph) / n)), color=INK, ls=DASHES[3], lw=1.2)
    ax.set_xlabel(r"$p$")
    means = [(a + S) / (a + b + n) for a, b in priors]
    print(n, "posterior means", [round(m, 4) for m in means], "spread", round(max(means) - min(means), 4),
          "posterior sds", [round(math.sqrt((a + S) * (b + n - S) / ((a + b + n) ** 2 * (a + b + n + 1))), 4) for a, b in priors],
          "Gaussian sd", round(math.sqrt(ph * (1 - ph) / n), 4))
axes[0].set_xlim(0.45, 0.8); axes[0].set_ylim(0, 12.5)
axes[0].set_ylabel("density")
axes[0].set_title(r"$n = 124$")
axes[1].set_xlim(0.45, 0.8); axes[1].set_ylim(0, 31)
axes[1].set_title(r"$n = 1{,}240$")
note(axes[0], "skeptic", (0.565, beta_pdf(np.array([0.565]), 113, 77)[0]), (0.46, 10.0), ha="left")
note(axes[0], "flat", (0.70, beta_pdf(np.array([0.70]), 81, 45)[0]), (0.73, 6.5), ha="left")
note(axes[1], "skeptic", (0.627, beta_pdf(np.array([0.627]), 833, 473)[0]), (0.48, 24.0), ha="left")
note(axes[1], "all four", (0.662, norm_pdf(0.662, 800 / 1240, math.sqrt(0.645 * 0.355 / 1240))), (0.70, 22.0), ha="left")
save(fig, "fig_bayes_bvm")
