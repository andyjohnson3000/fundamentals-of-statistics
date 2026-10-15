"""The epsilon-N definition of a limit, read as a game. Left: the sequence
x_n = 2 + (-1)^n / sqrt(n) with two bands. For epsilon = 0.3 every term past
N = 12 is inside; for the narrower epsilon = 0.1 you need N = 101. Right: the
N that works as a function of epsilon, a staircase that climbs as epsilon
shrinks. 'For every epsilon there is an N' means: whatever band your opponent
names, you can name an index past which the sequence stays inside it."""
from _style import *

n = np.arange(1, 161)
x = 2 + (-1.0) ** n / np.sqrt(n)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
ax1.plot(n, x, "o", ms=2.2, color=BLUE, mec="white", mew=0.2)
ax1.axhline(2, color=GRAY, lw=0.8)
ytop = 2.95  # ylim raised a little so the N labels sit above every point
for eps, col, N in [(0.3, ORANGE, 12), (0.1, AQUA, 101)]:
    ax1.axhspan(2 - eps, 2 + eps, color=col, alpha=0.12, lw=0)
    ax1.axvline(N, color=col, lw=0.9, ls="--")
    # label at the top of its own dashed line, just to the right of it
    ax1.annotate(rf"$\epsilon = {eps}$: $N = {N}$", (N, ytop - 0.08), xytext=(3, 0), textcoords="offset points",
                 ha="left", va="center", fontsize=7.5, color=INK)
ax1.set_xlabel(r"$n$"); ax1.set_ylabel(r"$x_n$")
ax1.set_ylim(0.9, ytop); ax1.set_xlim(right=182)  # room for the N = 101 label past its line
ax1.set_title("Two bands, two values of $N$")

eps = np.linspace(0.04, 0.6, 400)
Nof = np.floor(1 / eps ** 2) + 1
ax2.step(eps, Nof, where="post", color=BLUE)
ax2.set_xlabel(r"$\epsilon$ (the band's half-width)"); ax2.set_ylabel(r"$N(\epsilon)$", labelpad=2)
ax2.set_yscale("log")
ax2.set_title(r"Smaller $\epsilon$, larger $N$")
for e, N, col in [(0.3, 12, ORANGE), (0.1, 101, AQUA)]:
    ax2.plot(e, N, "o", ms=5, color=col, mec="white", mew=0.4, zorder=5)
save(fig, "fig_tk_epsilon_n")
