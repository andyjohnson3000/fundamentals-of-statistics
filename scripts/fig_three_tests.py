"""Three ways to measure how far the null value sits from the top of the
log-likelihood, for the kiss data (80 right turns of 124, null p0 = 1/2).
Left: the log-likelihood l_n(p) - l_n(p-hat) (blue) and Wald's parabola
-(1/2) n I(p-hat) (p - p-hat)^2 (orange, dashed), the parabola that matches
the log-likelihood's height and curvature at its top. The likelihood ratio
statistic is twice the drop of the blue curve from its top to p0 (2 x 5.30
= 10.60); Wald's statistic is twice the drop of the orange parabola
(2 x 5.71 = 11.41). Right: the score at p0 is the slope of the tangent
(aqua) there, 72; the score parabola (aqua, dash-dot) has that slope and the
curvature n I(p0) = 496 at p0, and the score statistic is twice its rise from
p0 to its top, 72^2/496 = 10.45."""
from _style import *

n, S = 124, 80
ph, p0 = S / n, 0.5
ll = lambda p: S * np.log(p) + (n - S) * np.log(1 - p)
top = ll(ph)
nIh = n / (ph * (1 - ph))
nI0 = n / (p0 * (1 - p0))
sc = S / p0 - (n - S) / (1 - p0)

p = np.linspace(0.44, 0.76, 600)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained", sharey=True)

# left: likelihood ratio and Wald
ax1.plot(p, ll(p) - top, color=BLUE, lw=1.4)
ax1.plot(p, -0.5 * nIh * (p - ph) ** 2, color=ORANGE, lw=1.3, ls=DASHES[1])
ax1.axhline(0, color=GRAY, lw=0.6, ls=DASHES[3])
ax1.axvline(p0, color=GRAY, lw=0.6, ls=DASHES[3])
ax1.plot([ph, ph], [-3.5, 0.9], color=GRAY, lw=0.6, ls=DASHES[3])   # stops above the notes
lr_drop = top - ll(p0)
w_drop = 0.5 * nIh * (ph - p0) ** 2
ax1.plot([p0], [-lr_drop], "o", ms=4.5, color=BLUE, zorder=5)
ax1.plot([p0], [-w_drop], "o", ms=4.5, color=ORANGE, zorder=5)
ax1.plot([ph], [0], "o", ms=4.5, color=INK, zorder=5)
note(ax1, f"likelihood ratio: $2 \\times {lr_drop:.2f} = {2 * lr_drop:.2f}$", (p0, -lr_drop), (0.56, -4.9), ha="left")
note(ax1, f"Wald: $2 \\times {w_drop:.2f} = {2 * w_drop:.2f}$", (p0, -w_drop), (0.56, -6.4), ha="left")
ax1.text(ph + 0.004, 0.25, r"$\hat p = 0.645$", fontsize=7.5, color=INK, ha="left", va="bottom")
ax1.text(p0 + 0.004, 0.25, r"$p_0 = \frac{1}{2}$", fontsize=7.5, color=INK, ha="left", va="bottom")
ax1.set_xlim(0.44, 0.76); ax1.set_ylim(-7.4, 0.9)
ax1.set_xlabel(r"$p$"); ax1.set_ylabel(r"$\ell_n(p) - \ell_n(\hat p)$")
ax1.set_title("drop from the top")

# right: score
ax2.plot(p, ll(p) - top, color=BLUE, lw=1.4)
tl = np.linspace(p0 - 0.05, p0 + 0.07, 50)
ax2.plot(tl, ll(p0) - top + sc * (tl - p0), color=AQUA, lw=1.2)
q = ll(p0) - top + sc * (p - p0) - 0.5 * nI0 * (p - p0) ** 2
ax2.plot(p, q, color=AQUA, lw=1.3, ls=DASHES[2])
ax2.axvline(p0, color=GRAY, lw=0.6, ls=DASHES[3])
ax2.plot([ph, ph], [-3.5, 0.9], color=GRAY, lw=0.6, ls=DASHES[3])   # stops above the note
ax2.plot([p0], [ll(p0) - top], "o", ms=4.5, color=AQUA, zorder=5)
rise = sc ** 2 / (2 * nI0)
qtop = ll(p0) - top + rise
ax2.plot([p0 + sc / nI0], [qtop], "o", ms=4.5, color=AQUA, zorder=5, markerfacecolor="white")
note(ax2, f"tangent\nat $p_0$:\nslope ${sc:.0f}$", (p0 + 0.03, ll(p0) - top + sc * 0.03), (0.447, -1.2), ha="left", va="top")
note(ax2, f"score: ${sc:.0f}^2/{nI0:.0f} = {sc ** 2 / nI0:.2f}$\n$= 2 \\times {rise:.2f}$", (p0 + sc / nI0, qtop), (0.60, -4.4), ha="left")
ax2.set_xlim(0.44, 0.76)
ax2.set_xlabel(r"$p$")
ax2.set_title("slope at the null")
save(fig, "fig_three_tests")
print("LR", 2 * lr_drop, "Wald", 2 * w_drop, "score", sc ** 2 / nI0, "score parabola top at", p0 + sc / nI0, qtop)
