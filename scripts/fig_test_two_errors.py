"""The two errors of the one-sided kiss-experiment test 'reject p = 1/2 when the
count n Rbar_n is 72 or more', drawn with the exact Binomial distribution of
the count. Top: under the null p = 1/2 the count is Bin(124, 1/2); the orange
mass at 72 and above is the type 1 error, 0.044. Bottom: under the
alternative p = 0.645 the count is Bin(124, 0.645); the gray mass below 72 is
the type 2 error, 0.057, and the blue mass at 72 and above is the power,
0.943. One threshold, two distributions, two errors."""
from _style import *

n, c = 124, 72
k = np.arange(n + 1)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.0, 4.1), sharex=True, layout="constrained")

pm0 = binom_pmf(n, 0.5)
ax1.bar(k[k < c], pm0[k < c], width=0.85, color=GRAY, alpha=0.45, edgecolor="none")
ax1.bar(k[k >= c], pm0[k >= c], width=0.85, color=ORANGE, edgecolor="none")
ax1.axvline(c - 0.5, color=INK, lw=0.8, ls="--")
a = pm0[k >= c].sum()
ax1.annotate(rf"type 1 error: reject although $p = \frac{{1}}{{2}}$" + "\n" + rf"$\Pr_{{1/2}}(n\bar R_n \geq {c}) = {a:.3f}$",
             (74, 0.006), xytext=(84, 0.045), fontsize=7.5, color=INK, ha="left", va="center",
             arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6))
ax1.text(41, 0.062, r"under $H_0$: $p = \frac{1}{2}$, count $\sim \mathrm{Bin}(124, \frac{1}{2})$", fontsize=8, color=INK, ha="left", va="center")
ax1.set_ylim(0, 0.085)
ax1.set_yticks([])
ax1.set_ylabel("probability")
sd0 = math.sqrt(n / 4)
sec = ax1.secondary_xaxis("top", functions=(lambda k: (k - n / 2) / sd0, lambda t: n / 2 + t * sd0))
sec.set_xticks([0, 1.796, 3.233])
sec.set_xticklabels([r"$0$", r"$1.80$", r"$3.23$"], fontsize=7.5)
sec.set_xlabel(r"test statistic $T_n = (\text{count} - 62)/\sqrt{31}$", fontsize=8)
sec.tick_params(length=2, color="#888888")

p1 = 0.645
pm1 = binom_pmf(n, p1)
ax2.bar(k[k < c], pm1[k < c], width=0.85, color=GRAY, edgecolor="none")
ax2.bar(k[k >= c], pm1[k >= c], width=0.85, color=BLUE, alpha=0.6, edgecolor="none")
ax2.axvline(c - 0.5, color=INK, lw=0.8, ls="--")
b = pm1[k < c].sum()
ax2.annotate(rf"type 2 error: fail to reject although $p = {p1}$" + "\n" + rf"$\Pr_{{{p1}}}(n\bar R_n < {c}) = {b:.3f}$",
             (69, 0.004), xytext=(41, 0.042), fontsize=7.5, color=INK, ha="left", va="center",
             arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6))
ax2.text(96, 0.055, rf"power $= 1 - {b:.3f} = {1 - b:.3f}$", fontsize=7.5, color=INK, ha="center", va="center")
ax2.text(41, 0.093, rf"under $H_1$, say $p = {p1}$: count $\sim \mathrm{{Bin}}(124, {p1})$", fontsize=8, color=INK, ha="left", va="center")
ax2.set_ylim(0, 0.105)
ax2.set_yticks([])
ax2.set_ylabel("probability")
ax2.set_xlim(40, 104)
ax2.set_xticks([50, 62, 72, 80, 90, 100])
ax2.set_xticklabels([r"$50$", r"$62$", r"$72$ (threshold)", r"$80$", r"$90$", r"$100$"])
ax2.set_xlabel(r"count $n\bar R_n$ turning right")
save(fig, "fig_test_two_errors")
print("alpha", a, "beta", b)
