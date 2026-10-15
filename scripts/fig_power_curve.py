"""The rejection probability p -> P_p(psi = 1) of the kiss-experiment test, computed
exactly from the Binomial distribution of the count. Left: the one-sided
test (reject when the count is 72 or more) and the two-sided test (74 or
more, or 50 or fewer), both at n = 124. On the null set the curve is the
type 1 error and stays at or below 0.05; on the alternative it is the
power. Right: the one-sided test at n = 30 (threshold 20) and n = 124: more
data makes the curve steeper, which is the only way to lower both errors."""
from _style import *


def reject_prob_upper(n, c, p):
    return binom_pmf(n, p)[c:].sum()


def reject_prob_two(n, hi, lo, p):
    pm = binom_pmf(n, p)
    return pm[hi:].sum() + pm[: lo + 1].sum()


ps = np.linspace(0.3, 0.85, 221)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, sharey=True, layout="constrained")

one = np.array([reject_prob_upper(124, 72, p) for p in ps])
two = np.array([reject_prob_two(124, 74, 50, p) for p in ps])
ax1.plot(ps, one, color=BLUE)
ax1.plot(ps, two, color=ORANGE, ls=DASHES[1])
ax1.axhline(0.05, color=INK, lw=0.6, ls=":")
ax1.axvline(0.5, color=GRAY, lw=0.6, ls=":")
ax1.plot(0.645, reject_prob_upper(124, 72, 0.645), "o", ms=4, color=BLUE, mec="white", mew=0.4, zorder=5)
ax1.annotate(r"power $0.943$ at $p = 0.645$", (0.645, 0.943), xytext=(0.66, 0.70), fontsize=7.5, color=INK, ha="left",
             arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6))
ax1.text(0.31, 0.065, r"level $0.05$", fontsize=7.5, color=INK, ha="left", va="bottom")
ax1.text(0.493, 0.93, r"$H_0$: $p = \frac{1}{2}$", fontsize=7.5, color=INK, ha="right", va="center")
ax1.set_xlabel(r"true $p$")
ax1.set_ylabel(r"$\Pr_p(\psi = 1)$, probability of rejecting")
ax1.set_title(r"One-sided and two-sided, $n = 124$")
# the one-sided curve lies between the two branches of the two-sided curve, so its label sits in the empty
# pocket above-left of it (x in (0.43, 0.57), y in (0.5, 0.95)) with a short leader down to the curve
p_one = 0.585
ax1.annotate("one-sided:\nreject if\n$n\\bar R_n \\geq 72$", (p_one, reject_prob_upper(124, 72, p_one)), xytext=(0.44, 0.78),
             fontsize=7.5, color=INK, ha="left", va="center", arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6, shrinkB=2))
# the two-sided label sits to the right of both curves, leader up to the orange branch
p_two = 0.618
ax1.annotate(r"two-sided: $\geq 74$ or $\leq 50$", (p_two, reject_prob_two(124, 74, 50, p_two)), xytext=(0.645, 0.22),
             fontsize=7.5, color=INK, ha="left", va="center", arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6, shrinkB=2))
ax1.set_xlim(0.3, 0.85)
ax1.set_ylim(0, 1.04)

small = np.array([reject_prob_upper(30, 20, p) for p in ps])
ax2.plot(ps, one, color=BLUE, label=r"$n = 124$, threshold $72$")
ax2.plot(ps, small, color=AQUA, ls=DASHES[2], label=r"$n = 30$, threshold $20$")
ax2.axhline(0.05, color=INK, lw=0.6, ls=":")
ax2.axvline(0.5, color=GRAY, lw=0.6, ls=":")
ax2.set_xlabel(r"true $p$")
ax2.set_title("More data, steeper curve")
ax2.legend(loc="upper left", fontsize=7)
save(fig, "fig_power_curve")
print("one-sided at 0.5:", reject_prob_upper(124, 72, 0.5), "two-sided at 0.5:", reject_prob_two(124, 74, 50, 0.5), "n=30 at 0.5:", reject_prob_upper(30, 20, 0.5))
