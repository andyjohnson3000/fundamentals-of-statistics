"""Estimating KL with the Law of Large Numbers. The true parameter is
p* = 0.645. The black curve is the true KL(Bern(p*), Bern(q)) as a function
of q. Each colored curve is the LLN estimate of it from one simulated sample
of n couples, (1/n) sum_i log(p*(R_i) / p_q(R_i)), which for Bernoulli data
equals rbar log(p*/q) + (1 - rbar) log((1 - p*)/(1 - q)). Each estimated
curve is lowest at its own sample proportion rbar (dots), and it can dip
below zero, which the true KL never does. As n grows the estimated curves
close in on the black one and their minimizers close in on p*. The estimate
needs p* only through a constant that does not depend on q, which is why
minimizing it is the same as maximizing the likelihood."""
from _style import *

ps = 0.645
q = np.linspace(0.3, 0.95, 700)
true = ps * np.log(ps / q) + (1 - ps) * np.log((1 - ps) / (1 - q))
r = rng(11)
cols = [BLUE, ORANGE, AQUA, YELLOW, GRAY]

fig, axes = plt.subplots(1, 3, figsize=FULL, layout="constrained", sharey=True)
for ax, n in zip(axes, [20, 124, 1000]):
    rbs = []
    while len(rbs) < 5:
        rb = r.binomial(n, ps) / n
        if rb in rbs or abs(rb - ps) < 0.5 / n or not 0.4 < rb < 0.9:
            continue
        rbs.append(rb)
    if n == 20: rbs20 = list(rbs)
    for rb, c in zip(rbs, cols):
        est = rb * np.log(ps / q) + (1 - rb) * np.log((1 - ps) / (1 - q))
        ax.plot(q, est, color=c, lw=0.9, alpha=0.9)
        ax.plot(rb, rb * np.log(ps / rb) + (1 - rb) * np.log((1 - ps) / (1 - rb)), "o", ms=3, color=c, mec="white", mew=0.4, zorder=5)
    ax.plot(q, true, color=INK, lw=1.6, zorder=4)
    ax.axhline(0, color=INK, lw=0.5)
    ax.axvline(ps, color=INK, lw=0.5, ls=":")
    ax.set_xlim(0.3, 0.95); ax.set_ylim(-0.12, 0.32)
    ax.set_title(rf"$n = {n}$")
    ax.set_xlabel(r"$q$")
    ax.set_xticks([0.4, ps, 0.9]); ax.set_xticklabels(["0.4", r"$p^*$", "0.9"])
axes[0].set_ylabel("divergence")
bb = dict(facecolor="white", edgecolor="none", pad=1.0)
note(axes[0], "true KL", (0.88, ps * np.log(ps / 0.88) + (1 - ps) * np.log((1 - ps) / 0.12)), (0.77, 0.285), ha="center")
axes[2].text(0.645, 0.295, "five estimates,\nclose to the true curve", fontsize=7.5, color=INK, ha="center", va="top", bbox=bb)
lo = min(((rb * np.log(ps / rb) + (1 - rb) * np.log((1 - ps) / (1 - rb)), rb) for rb in rbs20))
note(axes[0], "each minimum\nis below zero", (lo[1], lo[0]), (0.32, -0.085), ha="left")
save(fig, "fig_kl_estimate")
