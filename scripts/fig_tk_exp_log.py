"""Two facts about e. Left: (1 - x/n)^n approaches e^{-x} as n grows; the
curves for n = 1, 2, 5, 20 climb toward the limit. This is the step at the
end of the maximum-of-uniforms proof in Chapter 3 and of many likelihood
computations later. Right: the logarithm turns multiplication into addition
(equal ratios become equal steps), so the log of a likelihood, a product of
n densities, is a sum of n terms, which is what lets the Law of Large Numbers
act on it in Part III."""
from _style import *

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL)
x = np.linspace(0, 4, 400)
for n, col, ls in [(1, YELLOW, DASHES[3]), (2, AQUA, DASHES[2]), (5, ORANGE, DASHES[1]), (20, BLUE, DASHES[0])]:
    y = np.where(x <= n, (1 - x / n) ** n, 0)
    ax1.plot(x[x <= n], y[x <= n], color=col, ls=ls, label=rf"$n = {n}$")
ax1.plot(x, np.exp(-x), color=INK, lw=1.4, label=r"$e^{-x}$")
ax1.set_xlabel(r"$x$"); ax1.set_title(r"$(1 - x/n)^n \to e^{-x}$"); ax1.legend(fontsize=7)
ax1.set_ylim(-0.05, 1.05)

xs = np.linspace(0.5, 17, 400)
ax2.plot(xs, np.log(xs), color=BLUE)
for k in range(5):
    v = 2 ** k
    ax2.plot([v, v], [0, math.log(v)], color=GRAY, lw=0.6, ls=":")
    ax2.plot([0, v], [math.log(v)] * 2, color=GRAY, lw=0.6, ls=":")
    ax2.plot(v, math.log(v), "o", ms=4, color=ORANGE, mec="white", mew=0.3, zorder=5)
ax2.set_xticks([1, 2, 4, 8, 16]); ax2.tick_params(axis="x", labelsize=7); ax2.set_yticks([math.log(2 ** k) for k in range(5)])
ax2.set_yticklabels([rf"${k}\log 2$" if k > 1 else ("$0$" if k == 0 else r"$\log 2$") for k in range(5)], fontsize=7.5)
ax2.set_xlabel(r"$x$"); ax2.set_ylabel(r"$\log x$")
ax2.set_title(r"$\log(ab) = \log a + \log b$: ratios become steps", fontsize=9)
ax2.text(6.5, 0.4, "doubling $x$ adds the same\namount to $\\log x$ every time", fontsize=8, color=INK)
save(fig, "fig_tk_exp_log")
