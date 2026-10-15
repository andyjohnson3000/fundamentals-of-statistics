"""The indicator function and its expectation. Left: 1(x >= 5) is a step
function, 0 then 1. Right: for X ~ Expo(0.16), E[1(X >= 5)] is the average of
a variable that is 1 with probability P(X >= 5) and 0 otherwise, which is
P(X >= 5) itself, the shaded area under the density. An expectation of an
indicator is a probability; that one line is used in every chapter."""
from _style import *

lam = 0.16
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
x = np.linspace(0, 30, 600)
ax1.plot(x[x < 5], np.zeros_like(x[x < 5]), color=BLUE, lw=1.6)
ax1.plot(x[x >= 5], np.ones_like(x[x >= 5]), color=BLUE, lw=1.6)
ax1.plot(5, 1, "o", ms=5, color=BLUE, mec="white", mew=0.4); ax1.plot(5, 0, "o", ms=5, color="white", mec=BLUE, mew=1.0)
ax1.set_ylim(-0.15, 1.3); ax1.set_yticks([0, 1]); ax1.set_xlabel(r"$x$")
ax1.set_title(r"$\mathbb{1}(x \geq 5)$: $0$ below $5$, $1$ from $5$ on")

f = lam * np.exp(-lam * x)
ax2.plot(x, f, color=INK, lw=1.2)
ax2.fill_between(x[x >= 5], 0, f[x >= 5], color=ORANGE, alpha=0.35, lw=0)
p = math.exp(-5 * lam)
# in the empty upper-right region, with a leader into the shaded area
note(ax2, rf"$\mathbb{{E}}[\mathbb{{1}}(X \geq 5)] = \mathbb{{P}}(X \geq 5) = e^{{-5 \lambda}} = {p:.2f}$",
     xy=(9, 0.014), xytext=(30.5, 0.105), ha="right", va="center")
ax2.axvline(5, color=GRAY, lw=0.7, ls=":")
ax2.set_xlabel(r"$x$"); ax2.set_ylabel("density"); ax2.set_title(r"Its expectation is a probability")
save(fig, "fig_tk_indicator")
