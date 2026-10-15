"""The mean value theorem and the tangent-line approximation, the two facts
behind the delta method. Left: between any two points on a smooth curve there
is a point where the tangent is parallel to the chord, so g(b) - g(a) =
g'(c)(b - a) for some c between a and b. Right: near theta, g(x) is close to
its tangent line g(theta) + g'(theta)(x - theta); the gap is the curvature
term, which shrinks like the square of the distance from theta (the
first-order Taylor expansion)."""
from _style import *

g = lambda t: 1 / t; gp = lambda t: -1 / t ** 2
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
x = np.linspace(2, 10, 400)
a, b = 3.0, 9.0
ax1.plot(x, g(x), color=INK, lw=1.3)
ax1.plot([a, b], [g(a), g(b)], color=ORANGE, ls="--", lw=1.1)
slope = (g(b) - g(a)) / (b - a); c = math.sqrt(a * b)
xt = np.linspace(c - 2.2, c + 2.2, 50)
ax1.plot(xt, g(c) + gp(c) * (xt - c), color=BLUE, lw=1.1)
ax1.plot([a, b, c], [g(a), g(b), g(c)], "o", ms=4, color=INK, mec="white", mew=0.3)
for v, lab in [(a, "a"), (b, "b"), (c, "c")]:
    ax1.text(v, 0.02, rf"${lab}$", ha="center", fontsize=8, color=INK)
# empty upper-right region, above the chord
ax1.text(10.4, 0.36, "chord (orange) and the parallel\ntangent at $c$ (blue): same slope", ha="right", va="center",
         fontsize=7.5, color=INK)
ax1.set_ylim(0, 0.42); ax1.set_xlim(2, 10.5); ax1.set_xticks([]); ax1.set_yticks([]); ax1.set_title("Mean value theorem")

th = 6.23
xs = np.linspace(3.5, 9.5, 400)
ax2.plot(xs, g(xs), color=INK, lw=1.3)
ax2.plot(xs, g(th) + gp(th) * (xs - th), color=BLUE, lw=1.1)
ax2.fill_between(xs, g(xs), g(th) + gp(th) * (xs - th), color=ORANGE, alpha=0.25, lw=0)
ax2.axvspan(th - 0.78, th + 0.78, color=AQUA, alpha=0.15, lw=0)
ax2.text(th, 0.065, r"where $\hat\theta_n$ lives" + "\n" + r"($\theta \pm \sigma/\sqrt{n}$): error tiny", ha="center", fontsize=7.5, color=INK)
# direct labels instead of a legend: the green band runs the full height, so no
# corner is free of it and a legend box would cover it
ax2.text(4.1, 0.268, r"$g(x) = 1/x$", ha="left", va="bottom", fontsize=7.5, color=INK)
ax2.text(9.7, 0.055, r"tangent at $\theta$", ha="right", va="center", fontsize=7.5, color=INK)
note(ax2, "the error of\nthe tangent", xy=(8.9, 0.102), xytext=(9.75, 0.215), ha="right", va="center")
ax2.set_xticks([th]); ax2.set_xticklabels([r"$\theta$"]); ax2.set_yticks([])
ax2.set_ylim(0.035, 0.32); ax2.set_title("Tangent-line approximation")
save(fig, "fig_tk_mvt_taylor")
