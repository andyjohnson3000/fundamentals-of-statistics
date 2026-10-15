"""The Bernoulli case of Pinsker's inequality. Left: with p = 0.645 fixed,
KL(Bern(p), Bern(q)) as a function of q (blue) lies above 2(p - q)^2
(orange, dashed) everywhere, touching it only at q = p. Right: the gap
between them, g(q) = KL - 2(p - q)^2, for three values of p; each gap is
zero at q = p and nonnegative elsewhere, which is the first step of the
proof."""
from _style import *

q = np.linspace(0.005, 0.995, 1200)
def kl(p, q):
    return p * np.log(p / q) + (1 - p) * np.log((1 - p) / (1 - q))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
p = 0.645
ax1.plot(q, kl(p, q), color=BLUE, lw=1.4)
ax1.plot(q, 2 * (p - q) ** 2, color=ORANGE, lw=1.3, ls=DASHES[1])
ax1.set_xlim(0, 1); ax1.set_ylim(0, 1.2)
ax1.set_xlabel(r"$q$"); ax1.set_title(r"$p = 0.645$")
ax1.text(0.3, 1.1, r"$\mathrm{KL}(\mathrm{Bern}(p), \mathrm{Bern}(q))$", color=BLUE, fontsize=7.5, ha="left", va="top")
ax1.text(0.3, 0.98, r"$2(p - q)^2$", color=ORANGE, fontsize=7.5, ha="left", va="top")

for pp, c, ls in [(0.2, AQUA, DASHES[2]), (0.5, GRAY, DASHES[3]), (0.645, BLUE, "-")]:
    ax2.plot(q, kl(pp, q) - 2 * (pp - q) ** 2, color=c, lw=1.2, ls=ls)
ax2.set_xlim(0, 1); ax2.set_ylim(0, 0.08)
ax2.set_xlabel(r"$q$"); ax2.set_title(r"the gap $\mathrm{KL} - 2(p - q)^2$")
ax2.set_xticks([0, 0.2, 0.5, 0.645, 1.0]); ax2.set_xticklabels(["0", "0.2", "0.5", "0.645", "1"])
ax2.text(0.5, 0.074, "each gap is 0 at its own $p$", fontsize=7.5, color=INK, ha="center", va="top")
save(fig, "fig_pinsker")
