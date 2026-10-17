"""Three Beta priors for the kiss proportion p and their posteriors after
80 right turns among 124 couples. Flat prior Beta(1, 1) (blue, solid), the
shrinkage prior Beta(10, 10) (orange, dashed) and a skeptic's prior
Beta(33, 33), which puts 90% of its probability between 0.4 and 0.6 (aqua,
dash-dot). Left: the priors. Right: the posteriors Beta(81, 45), Beta(90, 54)
and Beta(113, 77), with the sample proportion 0.645 (dotted)."""
from _style import *

n, S = 124, 80
priors = [(1, 1, "flat"), (10, 10, "Beta(10, 10)"), (33, 33, "skeptic")]
p = np.linspace(0.0005, 0.9995, 1200)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
for (a, b, name), c, ls in zip(priors, SERIES, DASHES):
    ax1.plot(p, beta_pdf(p, a, b), color=c, ls=ls, lw=1.3)
    ax2.plot(p, beta_pdf(p, a + S, b + n - S), color=c, ls=ls, lw=1.3)
ax1.set_xlim(0, 1); ax1.set_ylim(0, 7.2)
ax1.set_xlabel(r"$p$"); ax1.set_ylabel("density")
ax1.set_title("three priors")
note(ax1, "flat", (0.15, 1.0), (0.08, 2.0), ha="left")
note(ax1, "Beta(10, 10)", (0.33, beta_pdf(np.array([0.33]), 10, 10)[0]), (0.03, 3.6), ha="left")
note(ax1, "skeptic, Beta(33, 33)", (0.56, beta_pdf(np.array([0.56]), 33, 33)[0]), (0.66, 5.6), ha="left")

ax2.axvline(S / n, color=GRAY, lw=0.8, ls=DASHES[3])
ax2.set_xlim(0.35, 0.85); ax2.set_ylim(0, 12.5)
ax2.set_xlabel(r"$p$")
ax2.set_title("their posteriors after 124 couples")
m_flat, m_shr, m_sk = 81 / 126, 90 / 144, 113 / 190
note(ax2, "skeptic", (0.555, beta_pdf(np.array([0.555]), 113, 77)[0]), (0.38, 10.5), ha="left")
note(ax2, "Beta(10, 10)", (0.627, beta_pdf(np.array([0.627]), 90, 54)[0] + 0.1), (0.70, 10.6), ha="left")
note(ax2, "flat", (0.70, beta_pdf(np.array([0.70]), 81, 45)[0]), (0.75, 6.2), ha="left")
note(ax2, r"$\hat{p} = 0.645$", (S / n, 12.1), (0.67, 12.1), ha="left")
save(fig, "fig_bayes_beta")
for (a, b, name) in priors:
    A, B = a + S, b + n - S
    print(name, "posterior mean", A / (A + B), "mode", (A - 1) / (A + B - 2), "sd", math.sqrt(A * B / ((A + B) ** 2 * (A + B + 1))))
