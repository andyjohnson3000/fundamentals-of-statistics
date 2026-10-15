"""Where the three confidence intervals for p come from, in one picture.
Horizontal axis: the true p. Vertical axis: the sample proportion Rbar_n.
For each p, the CLT says Rbar_n lands in the band p +/- q sqrt(p(1-p)/n) with
probability about 95%; the band is a lens, widest at p = 1/2. We observed
Rbar_n = 0.645, a horizontal line. The 'solve' interval is the set of p whose
band contains the observed value: the chord the line cuts out of the lens.
The conservative interval replaces the lens by the widest band (p +/- q/(2
sqrt n)): a wider chord. The plug-in interval replaces the lens by a band of
constant width q sqrt(phat(1-phat)/n): a chord of almost the same length,
centered at phat. Left: the whole picture; right: zoomed on the chords."""
from _style import *

n, k = 124, 80
phat = k / n
z = 1.959964

p = np.linspace(0.0005, 0.9995, 2000)
lens = z * np.sqrt(p * (1 - p) / n)
cons = z / (2 * math.sqrt(n))
plug = z * math.sqrt(phat * (1 - phat) / n)

# interval endpoints
A, B, C = 1 + z * z / n, -(2 * phat + z * z / n), phat * phat
D = math.sqrt(B * B - 4 * A * C)
solve = ((-B - D) / (2 * A), (-B + D) / (2 * A))
conserv = (phat - cons, phat + cons)
plugin = (phat - plug, phat + plug)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.0, 3.2), layout="constrained")

for ax, zoom in ((ax1, False), (ax2, True)):
    ax.fill_between(p, p - lens, p + lens, color=BLUE, alpha=0.18, lw=0)
    ax.plot(p, p - lens, color=BLUE, lw=0.9)
    ax.plot(p, p + lens, color=BLUE, lw=0.9)
    ax.plot(p, p - cons, color=GRAY, lw=0.9, ls="--")
    ax.plot(p, p + cons, color=GRAY, lw=0.9, ls="--")
    ax.plot(p, p - plug, color=AQUA, lw=1.1, ls=":")
    ax.plot(p, p + plug, color=AQUA, lw=1.1, ls=":")
    ax.plot(p, p, color=INK, lw=0.5, alpha=0.5)
    ax.axhline(phat, color=ORANGE, lw=1.2)
    ax.set_xlabel(r"true $p$")
    ax.set_aspect("equal")

ax1.set_xlim(0, 1); ax1.set_ylim(0, 1)
ax1.set_ylabel(r"sample proportion $\bar{R}_n$")
ax1.set_title(r"Where $\bar{R}_n$ lands, for each $p$ ($n = 124$)")
# labels in the two empty corners; the leaders stay outside the band.
# "observed" sits just above its line, left of where the line enters the band.
ax1.text(0.03, phat + 0.02, r"observed $\bar{R}_n = 0.645$", fontsize=7.5, color=INK, va="bottom")

def leader(ax, start, end, color):
    """Thin leader drawn as a bare segment (an empty annotation has no text box
    for matplotlib to clip against, so the segment is exactly where asked)."""
    ax.annotate("", xy=end, xytext=start, arrowprops=dict(arrowstyle="-", color=color, lw=0.6,
                                                           shrinkA=0, shrinkB=2))

# CLT band: the leader meets the lens at its widest point (p = 1/2), where the
# blue edge is outermost, so it does not cross the gray or aqua lines.
ax1.text(0.54, 0.08, "CLT band\n" + r"$p \pm q_{\alpha/2}\sqrt{p(1-p)/n}$", fontsize=7.5, color=BLUE,
         ha="left", va="bottom")
leader(ax1, (0.59, 0.22), (0.5, 0.5 - z * math.sqrt(0.25 / n)), BLUE)
# conservative band: the leader comes from above onto the gray upper line,
# right of where the observed line enters the band.
ax1.text(0.30, 0.975, "conservative band\n" + r"$p \pm q_{\alpha/2}/(2\sqrt{n})$", fontsize=7.5, color=GRAY,
         ha="left", va="top")
leader(ax1, (0.655, 0.885), (0.72, 0.72 + cons), GRAY)
ax1.plot([solve[0], solve[1]], [phat, phat], color=INK, lw=2.2, solid_capstyle="butt")

# zoomed panel: show the three chords as separate rows just below the line
ax2.set_xlim(0.50, 0.80); ax2.set_ylim(0.50, 0.80)
ax2.set_title(r"The three intervals are chords")
rows = [(conserv, "conservative", GRAY, "--", phat - 0.035),
        (plugin, "plug-in", AQUA, ":", phat - 0.065),
        (solve, "solve", BLUE, "-", phat - 0.095)]
for (lo, hi), name, col, ls, yy in rows:
    ax2.plot([lo, hi], [yy, yy], color=col, lw=2.0, solid_capstyle="butt")
    ax2.plot([lo, lo], [yy, phat], color=col, lw=0.6, ls=ls, alpha=0.9)
    ax2.plot([hi, hi], [yy, phat], color=col, lw=0.6, ls=ls, alpha=0.9)
    ax2.text(hi + 0.006, yy, rf"{name} $[{lo:.3f}, {hi:.3f}]$", fontsize=7, color=INK, va="center")
ax2.set_yticks([0.5, 0.6, 0.645, 0.7, 0.8])
ax2.set_yticklabels(["0.5", "0.6", r"$\bar{R}_n$", "0.7", "0.8"])
save(fig, "fig_ci_inversion")
print("solve", solve, "conserv", conserv, "plug", plugin)
