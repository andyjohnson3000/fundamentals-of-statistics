"""Why a density can stand in for a probability in the likelihood. One
subway gap of x = 5 minutes, and two candidate rates, lambda = 0.1 and 0.2
per minute. The probability of a gap within h/2 of 5 is the area of a thin
strip, about f_lambda(5) * h. Left: the two densities with the strip at
h = 1. Right: the ratio of the two strip probabilities as h shrinks; it
settles at f_0.1(5) / f_0.2(5) = 0.824, the ratio of the densities. The
width h cancels from every comparison between parameters, so the density is
all the likelihood needs."""
from _style import *

x = np.linspace(0, 25, 600)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
for lam, c, ls in [(0.1, BLUE, "-"), (0.2, ORANGE, DASHES[1])]:
    ax1.plot(x, lam * np.exp(-lam * x), color=c, lw=1.3, ls=ls)
xs = np.linspace(4.5, 5.5, 50)
f1, f2 = 0.1 * np.exp(-0.1 * xs), 0.2 * np.exp(-0.2 * xs)
ax1.fill_between(xs, 0, f1, color=BLUE, alpha=0.35, lw=0)
ax1.fill_between(xs, f1, f2, color=ORANGE, alpha=0.35, lw=0)
ax1.text(6.2, 0.012, r"$\leftarrow$ strips at $x = 5$", fontsize=7.5, color=INK, ha="left", va="center")
ax1.set_xlim(0, 25); ax1.set_ylim(0, 0.21)
ax1.set_xlabel("minutes between trains"); ax1.set_title(r"strips of width $h = 1$ at $x = 5$")
ax1.text(9, 0.165, r"$\lambda = 0.2$", color=ORANGE, fontsize=7.5)
ax1.text(14, 0.045, r"$\lambda = 0.1$", color=BLUE, fontsize=7.5)

hs = np.logspace(1, -3, 200)
def strip(lam, h):
    return np.exp(-lam * (5 - h / 2)) - np.exp(-lam * (5 + h / 2))
ratio = strip(0.1, hs) / strip(0.2, hs)
ax2.plot(hs, ratio, color=INK, lw=1.3)
dens = (0.1 * np.exp(-0.5)) / (0.2 * np.exp(-1.0))
ax2.axhline(dens, color=GRAY, lw=0.8, ls=DASHES[1])
ax2.set_xscale("log"); ax2.invert_xaxis()
ax2.set_xlabel(r"strip width $h$ (minutes)")
ax2.set_title("ratio of the two strip probabilities")
ax2.text(0.002, dens - 0.006, rf"density ratio ${dens:.3f}$", fontsize=7.5, color=INK, ha="right", va="top")
save(fig, "fig_density_strip")
print(dens, strip(0.1, 1)/strip(0.2, 1), strip(0.1,10)/strip(0.2,10))
