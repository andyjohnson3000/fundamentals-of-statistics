"""Convex, concave, neither. A function is convex when every chord lies above
the graph (the graph 'holds water'), concave when every chord lies below, and
neither when it depends on the chord. For twice-differentiable functions the
test is the sign of the second derivative. Jensen's inequality in Chapter 7 is
the chord picture read probabilistically."""
from _style import *

fig, axes = plt.subplots(1, 3, figsize=(6.0, 2.4))
x = np.linspace(0.3, 3.0, 300)
funcs = [(lambda t: 1 / t, r"convex: $1/x$", (0.5, 2.5)),
         (lambda t: np.log(t), r"concave: $\log x$", (0.5, 2.5)),
         (lambda t: np.sin(2.2 * t), r"neither: $\sin 2.2x$", (0.5, 2.5))]
for ax, (g, title, (c1, c2)) in zip(axes, funcs):
    ax.plot(x, g(x), color=INK, lw=1.3)
    ax.plot([c1, c2], [g(c1), g(c2)], color=ORANGE, ls="--", lw=1.1)
    ax.plot([c1, c2], [g(c1), g(c2)], "o", ms=4, color=ORANGE, mec="white", mew=0.3)
    ax.set_title(title, fontsize=8.5); ax.set_xticks([]); ax.set_yticks([])
save(fig, "fig_tk_convex")
