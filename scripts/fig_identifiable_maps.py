"""Identifiable or not, as the shape of the map from the parameter to the
distribution of what you observe. In each example you observe a Bernoulli
and its parameter is a function of theta. Left: censored Exponential,
P(X > 5) = e^(-5 lambda), strictly decreasing, so each observable p comes from
exactly one lambda (identifiable). Middle: thresholding a uniform at half its
range, P(Y >= a/2) = 1/2 for every a: constant, so the observable says nothing
about a (not identifiable). Right: the Gaussian sign example, P(Y >= 0) =
Phi(mu/sigma): one observable value, a whole ray of (mu, sigma) pairs; the
map is onto a one-dimensional set from a two-dimensional one, shown here as
the curve p against mu for three values of sigma."""
from _style import *

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(6.0, 2.5))
fig.subplots_adjust(wspace=0.35)

lam = np.linspace(0.02, 1.0, 300)
ax1.plot(lam, np.exp(-5 * lam), color=BLUE)
p0 = 0.3
l0 = -math.log(p0) / 5
ax1.plot([0, l0], [p0, p0], color=ORANGE, lw=0.8, ls="--")
ax1.plot([l0, l0], [0, p0], color=ORANGE, lw=0.8, ls="--")
ax1.plot(l0, p0, "o", ms=4, color=ORANGE, mec="white", mew=0.4, zorder=5)
ax1.text(l0 + 0.03, p0 + 0.04, r"one $p$, one $\lambda$", fontsize=7.5, color=INK)
ax1.set_xlabel(r"$\lambda$")
ax1.set_ylabel(r"$p = \mathbb{P}(\text{observe } 1)$")
ax1.set_title(r"$e^{-5\lambda}$: identifiable", fontsize=9)
ax1.set_ylim(0, 1)

a = np.linspace(0.1, 5, 300)
ax2.plot(a, 0.5 * np.ones_like(a), color=BLUE)
for aa in (1.0, 2.5, 4.0):
    ax2.plot(aa, 0.5, "o", ms=4, color=ORANGE, mec="white", mew=0.4, zorder=5)
ax2.text(2.5, 0.58, r"one $p$, every $a$", fontsize=7.5, color=INK, ha="center")
ax2.set_xlabel(r"$a$")
ax2.set_title(r"$\mathbb{P}(Y \geq a/2) = \frac{1}{2}$: not", fontsize=9)
ax2.set_ylim(0, 1)

mu = np.linspace(-3, 3, 300)
for sig, ls in ((1, DASHES[0]), (2, DASHES[1]), (4, DASHES[2])):
    ax3.plot(mu, norm_cdf(mu / sig), color=BLUE, ls=ls, label=rf"$\sigma = {sig}$")
ax3.axhline(norm_cdf(0.5), color=ORANGE, lw=0.8, ls="--")
for sig in (1, 2, 4):
    ax3.plot(0.5 * sig, norm_cdf(0.5), "o", ms=4, color=ORANGE, mec="white", mew=0.4, zorder=5)
ax3.text(-2.9, norm_cdf(0.5) + 0.06, "one $p$,\na ray of $(\\mu, \\sigma)$", fontsize=7.5, color=INK)
ax3.set_xlabel(r"$\mu$")
ax3.set_title(r"$\Phi(\mu/\sigma)$: not", fontsize=9)
ax3.set_ylim(0, 1)
ax3.legend(fontsize=7, loc="lower right")
save(fig, "fig_identifiable_maps")
