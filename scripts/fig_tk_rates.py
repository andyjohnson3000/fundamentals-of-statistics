"""Orders of magnitude: how fast things shrink. The same three sequences,
1/sqrt(n), 1/n and e^{-n/20}, on ordinary axes (left) and on log-log axes
(right), where a power law is a straight line whose slope is the exponent and
an exponential bends away below everything. 'The error is of order 1/sqrt(n)'
means it sits on the shallowest of these lines: four times the data halves
it. Chebyshev's bound shrinks like 1/n, Hoeffding's exponentially."""
from _style import *

n = np.arange(1, 401)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL)
for ax in (ax1, ax2):
    ax.plot(n, 1 / np.sqrt(n), color=BLUE, label=r"$1/\sqrt{n}$ (the CLT rate)")
    ax.plot(n, 1 / n, color=ORANGE, ls=DASHES[1], label=r"$1/n$ (Chebyshev; the maximum of uniforms)")
    ax.plot(n, np.exp(-n / 20), color=AQUA, ls=DASHES[2], label=r"$e^{-n/20}$ (Hoeffding)")
    ax.set_xlabel(r"$n$")
ax1.set_ylim(0, 0.5); ax1.set_title("Ordinary axes")
ax2.set_xscale("log"); ax2.set_yscale("log"); ax2.set_ylim(1e-9, 1.5); ax2.set_title("Log-log axes: power laws are lines"); ax2.legend(fontsize=6.5, loc="lower left", frameon=True, facecolor="white", edgecolor="none", framealpha=0.9)
save(fig, "fig_tk_rates")
