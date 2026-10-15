"""The same inversion picture for the subway rate lambda. By the delta method,
lambda-hat = 1/Tbar_n lands in lambda +/- q lambda/sqrt(n) with probability
about 95%: a wedge that opens as lambda grows, with no widest point, so there
is no conservative interval. The observed lambda-hat = 0.1605 is a horizontal
line; the solve interval is the chord it cuts from the wedge, and is not
centered at lambda-hat (the wedge is wider on the right). The plug-in interval
uses a band of constant width q lambda-hat/sqrt(n) and is centered."""
from _style import *

n, tbar = 64, 6.23
lam_hat = 1 / tbar
z = 1.959964
q = z / math.sqrt(n)

lam = np.linspace(0, 0.30, 600)
solve = (lam_hat / (1 + q), lam_hat / (1 - q))
plugin = (lam_hat * (1 - q), lam_hat * (1 + q))

fig, ax = plt.subplots(figsize=(4.6, 3.3))
ax.fill_between(lam, lam * (1 - q), lam * (1 + q), color=BLUE, alpha=0.18, lw=0)
ax.plot(lam, lam * (1 - q), color=BLUE, lw=0.9)
ax.plot(lam, lam * (1 + q), color=BLUE, lw=0.9)
ax.plot(lam, lam - q * lam_hat, color=AQUA, lw=0.9, ls=":")
ax.plot(lam, lam + q * lam_hat, color=AQUA, lw=0.9, ls=":")
ax.plot(lam, lam, color=INK, lw=0.5, alpha=0.5)
ax.axhline(lam_hat, color=ORANGE, lw=1.2)
# "observed": two lines just above the line, left of where it enters the band
ax.text(0.005, lam_hat + 0.006, "observed\n" + r"$\hat\lambda = 1/6.23 = 0.1605$", fontsize=7.5, color=INK, va="bottom")
# band label in the empty upper-left corner; the leader meets the upper edge of
# the wedge where it lies outside the dotted plug-in line, so it crosses nothing
ax.text(0.085, 0.292, "delta-method band\n" + r"$\lambda \pm q_{\alpha/2}\,\lambda/\sqrt{n}$", fontsize=7.5,
        color=BLUE, ha="left", va="top")
ax.annotate("", xy=(0.215, 0.215 * (1 + q)), xytext=(0.178, 0.272),
            arrowprops=dict(arrowstyle="-", color=BLUE, lw=0.6, shrinkA=0, shrinkB=2))
for (lo, hi), name, col, yy in [(solve, "solve", BLUE, lam_hat - 0.022), (plugin, "plug-in", AQUA, lam_hat - 0.062)]:
    ax.plot([lo, hi], [yy, yy], color=col, lw=2.0, solid_capstyle="butt")
    ax.plot([lo, lo], [yy, lam_hat], color=col, lw=0.6, alpha=0.9)
    ax.plot([hi, hi], [yy, lam_hat], color=col, lw=0.6, alpha=0.9)
    ax.text(hi + 0.004, yy, rf"{name} $[{lo:.3f}, {hi:.3f}]$", fontsize=7, color=INK, va="center")
ax.plot(lam_hat, lam_hat - 0.022, "|", color=INK, ms=7)
# the remark about the tick sits under the solve label, outside the band
ax.text(solve[1] + 0.004, lam_hat - 0.022 - 0.0065, r"$\hat\lambda$ (tick) is not" + "\nthe center", fontsize=7,
        color=INK, va="top", linespacing=1.1)
ax.set_xlim(0, 0.30); ax.set_ylim(0, 0.30)
ax.set_aspect("equal")
ax.set_xlabel(r"true $\lambda$")
ax.set_ylabel(r"$\hat\lambda = 1/\bar{T}_n$")
ax.set_title(r"A wedge, not a lens ($n = 64$)")
save(fig, "fig_ci_wedge")
print(solve, plugin)
