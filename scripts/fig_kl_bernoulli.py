"""KL divergence and total variation between Bernoulli distributions, with
the first argument fixed at the kiss estimate p = 0.645 and the second, q,
varying. Left, the whole range: TV = |p - q| is a tent with straight sides;
KL(Bern(p), Bern(q)) is smooth at q = p, and it blows up as q approaches 0 or
1, because the distribution Bern(q) then calls an outcome nearly impossible
that Bern(p) produces regularly. The two orders of KL differ: the
divergence is not symmetric. Right, close to p: KL is approximately the
parabola (p - q)^2 / (2 p (1 - p)), whose curvature is one over the variance
of a single observation. At q = 1/2 the numbers are TV = 0.145,
KL(p, q) = 0.0428, KL(q, p) = 0.0440, parabola 0.0460."""
from _style import *

p = 0.645
q = np.linspace(0.002, 0.998, 1500)
kl_pq = p * np.log(p / q) + (1 - p) * np.log((1 - p) / (1 - q))
kl_qp = q * np.log(q / p) + (1 - q) * np.log((1 - q) / (1 - p))
tv = np.abs(p - q)
quad = (p - q) ** 2 / (2 * p * (1 - p))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

ax1.plot(q, kl_pq, color=BLUE, lw=1.4)
ax1.plot(q, kl_qp, color=ORANGE, lw=1.3, ls=DASHES[1])
ax1.plot(q, tv, color=GRAY, lw=1.0, ls=DASHES[3])
ax1.axvline(p, color=INK, lw=0.5, ls=":")
ax1.set_ylim(0, 1.6); ax1.set_xlim(0, 1)
ax1.set_xlabel(r"$q$")
ax1.set_title(r"Fixed $p = 0.645$, varying $q$")
ax1.text(0.07, 1.5, r"$\mathrm{KL}(\mathrm{Bern}(p), \mathrm{Bern}(q))$", color=BLUE, fontsize=7.5, ha="left", va="top")
ax1.text(0.07, 1.33, r"$\mathrm{KL}(\mathrm{Bern}(q), \mathrm{Bern}(p))$", color=ORANGE, fontsize=7.5, ha="left", va="top")
ax1.text(0.07, 1.16, r"$\mathrm{TV} = |p - q|$", color=GRAY, fontsize=7.5, ha="left", va="top")
ax1.text(0.655, 1.5, r"$q = p$", fontsize=7.5, color=INK, ha="left", va="top")

z = (q > 0.42) & (q < 0.87)
ax2.plot(q[z], kl_pq[z], color=BLUE, lw=1.4)
ax2.plot(q[z], kl_qp[z], color=ORANGE, lw=1.3, ls=DASHES[1])
ax2.plot(q[z], quad[z], color=AQUA, lw=1.1, ls=DASHES[2])
ax2.plot(q[z], tv[z], color=GRAY, lw=1.0, ls=DASHES[3])
ax2.set_xlim(0.42, 0.87); ax2.set_ylim(0, 0.16)
ax2.set_xlabel(r"$q$")
ax2.text(0.645, 0.148, "TV", color=GRAY, fontsize=7.5, ha="center", va="center")
note(ax2, "parabola\n" + r"$\frac{(p - q)^2}{2p(1-p)}$", (0.735, (p - 0.735) ** 2 / (2 * p * (1 - p))), (0.645, 0.085), ha="center", fontsize=8)
ax2.set_title(r"Close to $p$: KL is a parabola, TV a tent")
save(fig, "fig_kl_bernoulli")
i = np.argmin(abs(q - 0.5)); print(tv[i], kl_pq[i], kl_qp[i], quad[i])
