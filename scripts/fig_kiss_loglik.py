"""The kiss likelihood and log-likelihood. Left: L(p) = p^80 (1 - p)^44, in
units of 10^-36; its peak at p-hat = 0.645 is 9.4 x 10^-36, and at p = 1/2 it
is 0.047 x 10^-36, 200 times smaller. Right: the log-likelihood
l(p) = 80 log p + 44 log(1 - p), concave, with maximum -80.65 at 0.645 and
value -85.95 at 1/2; the difference 5.30 is the KL evidence of Chapter 10.
The flat tangent marks the first-order condition l'(p-hat) = 0."""
from _style import *

p = np.linspace(0.45, 0.82, 600)
ll = 80 * np.log(p) + 44 * np.log(1 - p)
ph = 80 / 124
llh = 80 * np.log(ph) + 44 * np.log(1 - ph)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
ax1.plot(p, np.exp(ll) * 1e36, color=BLUE, lw=1.4)
ax1.axvline(ph, color=INK, lw=0.5, ls=":")
ax1.set_xlabel(r"$p$"); ax1.set_ylabel(r"$L(p)$, in units of $10^{-36}$")
ax1.set_title("Likelihood")
ax1.set_ylim(0, 11)
note(ax1, r"peak $9.4$ at $\hat p = 0.645$", (ph, np.exp(llh) * 1e36), (0.455, 10.4), ha="left")
note(ax1, r"$0.047$ at $p = \frac{1}{2}$", (0.5, np.exp(124 * np.log(0.5)) * 1e36), (0.455, 4.0), ha="left")

ax2.plot(p, ll, color=BLUE, lw=1.4)
ax2.plot([ph - 0.07, ph + 0.07], [llh, llh], color=ORANGE, lw=1.0, ls=DASHES[1])
ax2.plot([0.5], [124 * np.log(0.5)], "o", ms=3.5, color=INK)
ax2.plot([ph], [llh], "o", ms=3.5, color=ORANGE)
ax2.set_xlabel(r"$p$"); ax2.set_ylabel(r"$\ell(p) = \log L(p)$")
ax2.set_title("Log-likelihood")
ax2.set_ylim(-92, -79)
ax2.annotate("", xy=(0.5, llh), xytext=(0.5, 124 * np.log(0.5)),
             arrowprops=dict(arrowstyle="<->", color=GRAY, lw=0.8))
ax2.plot([0.5, ph], [llh, llh], color=GRAY, lw=0.5, ls=":")
ax2.text(0.49, -83.3, "$5.30$", fontsize=7.5, color=INK, ha="right", va="center")
note(ax2, r"flat at the top: $\ell'(\hat p) = 0$", (ph + 0.06, llh), (0.72, -79.6), ha="left")
save(fig, "fig_kiss_loglik")
