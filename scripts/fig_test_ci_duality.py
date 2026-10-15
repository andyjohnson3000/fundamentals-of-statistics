"""Tests and confidence intervals are one construction. For each candidate
value p_0 on the horizontal axis, the vertical segment is the set of sample
proportions the level-5% test of H_0: p = p_0 does NOT reject: p_0 +/- 1.96
sqrt(p_0 (1 - p_0)/n), n = 124. The horizontal line is the observed
proportion 0.645. A candidate whose segment crosses the line is not
rejected (blue); one whose segment misses it is rejected (orange). The blue
candidates run from 0.558 to 0.724: exactly the solve interval of Chapter 8.
The value 1/2 is orange: rejected, as the test said."""
from _style import *

n, rbar, z = 124, 80 / 124, 1.959964
p0s = np.round(np.arange(0.40, 0.80 + 1e-9, 0.025), 3)
lo_w, hi_w = 0.5583, 0.7241   # solve (Wilson) interval endpoints from ch08

fig, ax = plt.subplots(figsize=(6.0, 3.1), layout="constrained")
for p0 in p0s:
    half = z * math.sqrt(p0 * (1 - p0) / n)
    keep = abs(rbar - p0) <= half
    col = BLUE if keep else ORANGE
    ax.plot([p0, p0], [p0 - half, p0 + half], color=col, lw=2.0, solid_capstyle="butt", alpha=0.9 if keep else 0.7)
    ax.plot(p0, p0, "_", ms=6, color=col, mew=1.2)
ax.axhline(rbar, color=INK, lw=0.9)
ax.axvspan(lo_w, hi_w, color=BLUE, alpha=0.08, lw=0)
ax.text(0.405, rbar + 0.012, r"observed $\bar R_n = 0.645$", fontsize=7.5, color=INK, ha="left", va="bottom")
ax.text((lo_w + hi_w) / 2, 0.905, "not rejected: $[0.558,\\, 0.724]$,\nthe solve interval", fontsize=7.5, color=INK, ha="center", va="top")
ax.annotate(r"$p_0 = \frac{1}{2}$: segment misses the line, rejected", (0.5, 0.5 + z * math.sqrt(0.25 / n)), xytext=(0.405, 0.84),
            fontsize=7.5, color=INK, ha="left", arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6))
ax.annotate("segment: proportions the test of\n$H_0$: $p = p_0$ does not reject", (0.75, 0.75 - z * math.sqrt(0.75 * 0.25 / n)), xytext=(0.66, 0.46),
            fontsize=7.5, color=INK, ha="left", arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6))
ax.set_xlim(0.385, 0.815)
ax.set_ylim(0.33, 0.92)
ax.set_xlabel(r"candidate null value $p_0$")
ax.set_ylabel(r"sample proportion $\bar R_n$")
ax.set_title(r"One level-5% test for each $p_0$; the ones not rejected form the 95% interval")
save(fig, "fig_test_ci_duality")
