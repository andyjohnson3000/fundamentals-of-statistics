"""The course's first heuristic for a test, drawn: put a buffer of two
standard errors around each estimate and see whether the buffers reach the
value being tested. Left: the boarding-time example (R2F 24.2 min, WilMA 15.9
min, standard errors 0.25 and 0.17): the buffers are nowhere near touching,
so the means are different. Right: two one-sample examples from the slides.
The coin (13 heads in 30, buffer 0.43 +/- 0.18) reaches 1/2 easily; the
YouTube survey (0.32 of 4,971, buffer 0.32 +/- 0.013) just reaches 0.33.
In both the heuristic is silent. The buffer shrinks like 1/sqrt(n)."""
from _style import *

z = 2.0
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

# ---- left: two samples, boarding times
m1, m2, s1, s2, n1, n2 = 24.2, 15.9, 2.1, 1.3, 72, 56
se1, se2 = s1 / math.sqrt(n1), s2 / math.sqrt(n2)
for y, m, se, col, lab in [(1, m1, se1, BLUE, r"R2F: $\bar X_n = 24.2$, $n = 72$"), (0, m2, se2, ORANGE, r"WilMA: $\bar Y_m = 15.9$, $m = 56$")]:
    ax1.plot([m - z * se, m + z * se], [y, y], color=col, lw=2.4, solid_capstyle="butt")
    ax1.plot(m, y, "o", ms=5, color=col, mec="white", mew=0.6, zorder=5)
    ax1.text(m, y + 0.2, lab, ha="center", va="bottom", fontsize=7.5, color=INK)
ax1.text(20.05, 0.5, "buffers of two standard errors\nnowhere near touching", ha="center", va="center", fontsize=7.5, color=INK)
ax1.set_yticks([]); ax1.set_ylim(-0.5, 1.7); ax1.set_xlim(11.5, 27.5)
ax1.set_xlabel("boarding time (minutes)")
ax1.set_title("Two samples: the buffers settle it")
ax1.grid(False); ax1.spines["left"].set_visible(False)

# ---- right: one sample each, proportions
cases = [(1, 13 / 30, 30, 0.5, BLUE, r"coin: $\hat p = 0.43$, $n = 30$"),
         (0, 0.32, 4971, 0.33, AQUA, r"news on YouTube: $\hat p = 0.32$, $n = 4{,}971$")]
for y, ph, n, p0, col, lab in cases:
    se = math.sqrt(ph * (1 - ph) / n)
    ax2.plot([ph - z * se, ph + z * se], [y, y], color=col, lw=2.4, solid_capstyle="butt")
    ax2.plot(ph, y, "o", ms=5, color=col, mec="white", mew=0.6, zorder=5)
    ax2.plot([p0, p0], [y - 0.12, y + 0.12], color=INK, lw=1.2, zorder=6)
    ax2.text(ph if y == 1 else 0.33, y + 0.2, lab, ha="center", va="bottom", fontsize=7.5, color=INK)
ax2.text(0.5, 1 - 0.2, r"value tested, $\frac{1}{2}$", ha="center", va="top", fontsize=7.5, color=INK)
ax2.text(0.33, 0 - 0.2, r"value tested, $0.33$", ha="center", va="top", fontsize=7.5, color=INK)
ax2.text(0.60, 0.5, "the buffers reach the value tested:\nthe heuristic is silent", ha="center", va="center", fontsize=7.5, color=INK)
ax2.set_yticks([]); ax2.set_ylim(-0.5, 1.7); ax2.set_xlim(0.18, 0.78)
ax2.set_xlabel("proportion")
ax2.set_title("One sample: the buffer shrinks like $1/\\sqrt{n}$")
ax2.grid(False); ax2.spines["left"].set_visible(False)
save(fig, "fig_test_buffer")
