"""The minimum of n uniforms converges in probability to 0. The density of
X_(1) = min(X_1, ..., X_n) is n(1-x)^(n-1) on [0, 1]; as n grows it piles up
against 0, and the mass beyond epsilon, which is (1-epsilon)^n, disappears.
This is the chapter's worked proof as a picture."""
from _style import *

eps = 0.2
x = np.linspace(0, 1, 500)
fig, ax = plt.subplots(figsize=(4.8, 2.8))
for n, col, ls in [(1, YELLOW, DASHES[3]), (3, AQUA, DASHES[2]), (10, ORANGE, DASHES[1]), (30, BLUE, DASHES[0])]:
    f = n * (1 - x) ** (n - 1)
    ax.plot(x, f, color=col, ls=ls, label=rf"$n = {n}$: mass beyond $\epsilon$ is $(1-\epsilon)^{{{n}}} = {(1 - eps) ** n:.3f}$")
    ax.fill_between(x[x >= eps], 0, f[x >= eps], color=col, alpha=0.12, lw=0)
ax.axvline(eps, color=INK, lw=0.8, ls=":")
ax.text(eps + 0.01, 5.0, r"$\epsilon = 0.2$", fontsize=8, color=INK)
ax.set_xlim(0, 1)
ax.set_ylim(0, 8.5)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"density of $X_{(1)}$")
ax.set_title(r"$X_{(1)} = \min(X_1, \ldots, X_n)$ for $\mathrm{Unif}([0,1])$ draws")
ax.legend(fontsize=7, loc="upper right")
save(fig, "fig_min_uniform")
