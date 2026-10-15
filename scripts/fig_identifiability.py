"""The course's non-identifiable example. You observe only X = 1{Y >= 0} with
Y ~ Gauss(mu, sigma^2). Left: Gauss(1, 4) and Gauss(2, 16) look different but
put the same mass, Phi(1/2) = 0.691, above zero, so they produce the same
Bernoulli. Right: in the (mu, sigma) parameter space, every point on the ray
mu / sigma = 1/2 produces that same Bernoulli; the observable distribution
only pins down the ray, not the point."""
from _style import *

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

y = np.linspace(-9, 13, 1200)
for k, (mu, var) in enumerate([(1, 4), (2, 16)]):
    sd = math.sqrt(var)
    f = norm_pdf(y, mu, sd)
    ax1.plot(y, f, color=SERIES[k], ls=DASHES[k], label=rf"$\mathrm{{Gauss}}({mu}, {var})$")
    ax1.fill_between(y, 0, f, where=y >= 0, color=SERIES[k], alpha=0.18, lw=0)
ax1.axvline(0, color=GRAY, lw=0.8)
p = float(norm_cdf(0.5))
# label in the empty upper right, three short lines so it stays inside the panel,
# with a leader into the overlap of the two shaded regions
ax1.annotate("shaded area:\n" + r"$\Pr(Y \geq 0) = \Phi(1/2)$" + "\n" + rf"$= {p:.3f}$ for both",
             (7.0, 0.03), xytext=(13.3, 0.165), ha="right", va="top", fontsize=7.5, color=INK,
             arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6, relpos=(0.5, 0), shrinkA=2, shrinkB=0))
ax1.set_xlabel(r"$y$")
ax1.set_ylabel("density")
ax1.set_title(r"Two different $(\mu, \sigma^2)$, one observable $p$")
ax1.set_ylim(0, 0.26)
ax1.legend(loc="upper left", fontsize=7.5)

sig = np.linspace(0, 6, 100)
ax2.plot(0.5 * sig, sig, color=ORANGE, lw=1.6)
for mu, sd in [(1, 2), (2, 4)]:
    ax2.plot(mu, sd, "o", ms=5, color=INK)
# (2, 16): to the right of its point, in the wedge between the orange ray and the 3/2 ray
ax2.text(2.4, 4.2, r"$(\mu, \sigma^2) = (2, 16)$", ha="left", va="center", fontsize=7.5, color=INK)
# (1, 4): the wedge is too narrow there, so the label goes in the empty lower right with a leader
ax2.annotate(r"$(\mu, \sigma^2) = (1, 4)$", (1, 2), xytext=(2.9, 1.0), ha="left", va="center",
             fontsize=7.5, color=INK,
             arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6, shrinkA=2, shrinkB=4))
for ratio, col in [(-0.5, GRAY), (1.5, GRAY)]:
    ax2.plot(ratio * sig, sig, color=col, lw=0.8, ls=":")
# ray labels at the ends of the rays, in empty space beside them
ax2.text(2.35, 6.05, "$\\mu/\\sigma = 1/2$:\nall give $p = 0.691$", ha="right", va="top", fontsize=7.5, color=INK)
ax2.text(-2.0, 4.5, r"$\mu/\sigma = -1/2$", ha="left", va="center", fontsize=7, color=GRAY)
ax2.text(6.35, 2.45, r"$\mu/\sigma = 3/2$", ha="right", va="center", fontsize=7, color=GRAY)
ax2.set_xlim(-3.5, 6.5)
ax2.set_ylim(0, 6.2)
ax2.set_xlabel(r"$\mu$")
ax2.set_ylabel(r"$\sigma$")
ax2.set_title(r"Each ray in $\Theta$ collapses to one $\mathbb{P}_\theta$")
save(fig, "fig_identifiability")
