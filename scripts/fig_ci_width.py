"""What makes an interval wide. Left: the half-width q_{alpha/2}
sqrt(phat(1-phat)/n) of the plug-in interval for the kiss data as a
function of the confidence level 1 - alpha, with the quantile doing the work:
going from 95% to 99% costs 31% more width, and 100% confidence costs the
whole line. Right: the half-width at 95% as a function of n, for the plug-in
interval at phat = 0.645 and for the conservative interval (whose half-width
is q/(2 sqrt n), about 1/sqrt n): to halve the width you need four times the
data, and a margin of error of 3 points needs about 1,067 observations."""
from _style import *

n, phat = 124, 80 / 124
z95 = 1.959964

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

levels = np.linspace(0.50, 0.999, 500)
# quantile of order 1 - alpha/2 by bisection on norm_cdf (no scipy needed)
def qnorm(u):
    lo, hi = 0.0, 6.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if norm_cdf(mid) < u:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)
qs = np.array([qnorm(1 - (1 - l) / 2) for l in levels])
hw = qs * math.sqrt(phat * (1 - phat) / n)
ax1.plot(levels * 100, hw, color=BLUE)
for l, lab in [(0.50, "50%"), (0.90, "90%"), (0.95, "95%"), (0.99, "99%")]:
    q = qnorm(1 - (1 - l) / 2)
    h = q * math.sqrt(phat * (1 - phat) / n)
    ax1.plot(l * 100, h, "o", ms=4, color=ORANGE, mec="white", mew=0.4, zorder=5)
    if l == 0.50:   # curve rises to the right of this point, so the label goes below it
        ax1.annotate(rf"{lab}: $\pm{h:.3f}$", (l * 100, h), xytext=(5, -7), textcoords="offset points", fontsize=7.5, color=INK, ha="left", va="top")
    else:
        ax1.annotate(rf"{lab}: $\pm{h:.3f}$", (l * 100, h), xytext=(-6, 6), textcoords="offset points", fontsize=7.5, color=INK, ha="right")
ax1.set_xlabel(r"confidence level $1 - \alpha$ (percent)")
ax1.set_ylabel("half-width of the interval")
ax1.set_title(rf"Level vs width, plug-in, $n = {n}$")
ax1.set_xlim(48, 101)
ax1.set_ylim(0, 0.16)

ns = np.arange(10, 2001)
ax2.plot(ns, z95 * np.sqrt(phat * (1 - phat) / ns), color=BLUE, label=r"plug-in, $\hat p = 0.645$")
ax2.plot(ns, z95 / (2 * np.sqrt(ns)), color=GRAY, ls=DASHES[1], label=r"conservative $\approx 1/\sqrt{n}$")
ax2.axhline(0.03, color=INK, lw=0.6, ls=":")
n3 = (z95 / 0.06) ** 2
ax2.plot(n3, 0.03, "o", ms=4, color=ORANGE, mec="white", mew=0.4, zorder=5)
h124 = z95 * math.sqrt(phat * (1 - phat) / 124)
ax2.plot(124, h124, "o", ms=4, color=ORANGE, mec="white", mew=0.4, zorder=5)
# both point labels sit in empty space with a leader: the n = 1,067 label in the
# upper right under the legend (leader comes down from above), the n = 124 label
# in the empty lower left under the curves (leader comes up from below-left, so
# it does not cross the conservative curve that runs just above the point)
ax2.annotate(r"$\pm 3$ points needs" + "\n" + r"$n \approx 1{,}067$", (n3, 0.03), xytext=(1700, 0.205), fontsize=7.5,
             color=INK, ha="right", va="top")
ax2.annotate("", (n3, 0.03), xytext=(1010, 0.152), arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6, shrinkA=0, shrinkB=3))
ax2.annotate(r"$n = 124$: $\pm 0.084$", (124, h124), xytext=(12, 0.045), fontsize=7.5, color=INK, ha="left", va="center")
ax2.annotate("", (124, h124), xytext=(84, 0.047), arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6, shrinkA=0, shrinkB=3))
ax2.set_xscale("log")
ax2.set_xlabel(r"$n$ (log scale)")
ax2.set_title(r"Sample size vs width, 95%")
ax2.set_ylim(0, 0.32)
ax2.legend(loc="upper right", fontsize=7)
save(fig, "fig_ci_width")
