"""Probability and statistics as inverse problems, with the drug
example. Left (probability): the drug is known to be 80% effective, so the
number cured out of 100 is Bin(100, 0.8); the shaded region "at least 65
cured" has probability 0.9999. Right (statistics): 78 of 100 were cured and
the truth is unknown; the curve is how plausible each value of p makes the
data (the likelihood, scaled to peak at 1), and the shaded band is the 95%
confidence interval [0.699, 0.861]."""
from _style import *

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

n, p0 = 100, 0.8
k = np.arange(n + 1)
pm = binom_pmf(n, p0)
ax1.bar(k, pm, width=0.9, color=BLUE, alpha=0.35, lw=0)
ax1.bar(k[k >= 65], pm[k >= 65], width=0.9, color=BLUE, alpha=0.85, lw=0)
ax1.axvline(64.5, color=GRAY, lw=0.7, ls="--")
ax1.set_xlim(55, 100)
ax1.set_xlabel("patients cured out of 100")
ax1.set_ylabel("probability")
ax1.set_title("Probability: truth known ($p = 0.80$),\nwhat will the data look like?")
# the label is wider than the strip left of the dashed line, so it sits just right of the
# line in a strip above the tallest bars (headroom added to ylim for it)
ax1.set_ylim(0, pm.max() * 1.30)
ax1.text(66, pm.max() * 1.275, "at least 65 cured:\nprobability 0.9999", fontsize=7.5, color=INK,
         ha="left", va="top")

obs = 78
p = np.linspace(0.5, 1.0, 600)
lik = p ** obs * (1 - p) ** (n - obs)
lik = lik / lik.max()
lo, hi = 0.6988, 0.8612
ax2.plot(p, lik, color=ORANGE)
ax2.fill_between(p, 0, lik, where=(p >= lo) & (p <= hi), color=ORANGE, alpha=0.25, lw=0)
ax2.axvline(0.78, color=GRAY, lw=0.7, ls="--")
ax2.set_xlabel(r"effectiveness $p$ (unknown)")
ax2.set_ylabel("plausibility of $p$ given the data")
ax2.set_title("Statistics: data known ($78/100$ cured),\nwhat could the truth be?")
# p-hat label just right of its dashed line (centered on it, the line would run through the text)
ax2.text(0.792, 1.06, r"$\hat{p} = 0.78$", ha="left", va="center", fontsize=7.5, color=INK)
# CI label in the empty upper left, leader from its bottom center into the shaded band
ax2.annotate("95% confidence\ninterval [0.70, 0.86]", (0.71, 0.06), xytext=(0.49, 0.92), ha="left", va="bottom",
             fontsize=7.5, color=INK,
             arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6, relpos=(0.5, 0), shrinkA=2, shrinkB=0))
ax2.set_ylim(0, 1.15)
save(fig, "fig_probability_vs_statistics")
