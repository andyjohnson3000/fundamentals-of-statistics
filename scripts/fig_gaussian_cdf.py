"""The standard Gaussian CDF read forwards (a z-score in, a probability out) and
backwards (a probability in, a quantile out), with the exam example:
scores ~ N(85, 4), so z = (90 - 85)/2 = 2.5 gives Phi(2.5) = 0.9938, and the
90th percentile is z = 1.2816, i.e. a score of 87.56."""
from _style import *

z = np.linspace(-3.5, 3.5, 800)
F = norm_cdf(z)

fig, ax = plt.subplots(figsize=(4.6, 3.0))
ax.plot(z, F, color=INK, lw=1.3)

# forwards: z = 2.5 -> 0.9938
zf, pf = 2.5, float(norm_cdf(2.5))
ax.plot([zf, zf], [0, pf], color=BLUE, lw=1.0, ls="--")
ax.plot([-3.5, zf], [pf, pf], color=BLUE, lw=1.0, ls="--")
ax.plot(zf, pf, "o", ms=4, color=BLUE)
# direct label: sits just above the blue dashed line it describes, ending over the blue point
ax.text(3.6, 1.055, r"forwards: $z = 2.5 \mapsto \Phi(2.5) = 0.9938$", ha="right", va="bottom",
        fontsize=7.5, color=INK)

# backwards: 0.90 -> 1.2816
pb, zb = 0.90, 1.2816
ax.plot([-3.5, zb], [pb, pb], color=ORANGE, lw=1.0, ls=":")
ax.plot([zb, zb], [0, pb], color=ORANGE, lw=1.0, ls=":")
ax.plot(zb, pb, "s", ms=4, color=ORANGE)
# direct label: sits just under the orange dotted line it describes, in the empty upper left
ax.text(-3.4, 0.875, r"backwards: $0.90 \mapsto \Phi^{-1}(0.90) = 1.28$", ha="left", va="top",
        fontsize=7.5, color=INK)

ax.set_xlabel(r"$z$")
ax.set_ylabel(r"$\Phi(z) = \Pr(Z \leq z)$")
ax.set_xticks([-3, -2, -1, 0, zb, 2, zf, 3])
ax.set_xticklabels(["-3", "-2", "-1", "0", "1.28", "2", "2.5", "3"], fontsize=7.5)
ax.set_yticks([0, 0.25, 0.5, 0.75, pb, 1.0])
ax.set_yticklabels(["0", "0.25", "0.5", "0.75", "0.90", "1"], fontsize=7.5)
ax.set_ylim(0, 1.13)  # a little headroom for the forwards label above the 0.9938 line
save(fig, "fig_gaussian_cdf")
