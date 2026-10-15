"""One-to-one or not, by the horizontal-line test. Left: lambda -> e^{-5 lambda}
is strictly decreasing, so each height is hit once: from the output you can
recover the input (the censored-exponential example of Chapter 6). Right:
(mu, sigma) -> Phi(mu/sigma) read along sigma for fixed mu = 1 hits the same
height... no: shown instead is x -> x^2 on [-2, 2], where the height 1 is hit
twice, so the input cannot be recovered. The image is the set of heights
actually reached."""
from _style import *

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, gridspec_kw=dict(wspace=0.3))
lam = np.linspace(0, 1, 300)
ax1.plot(lam, np.exp(-5 * lam), color=BLUE)
ax1.axhline(0.3, color=ORANGE, lw=0.9, ls="--")
l0 = -math.log(0.3) / 5
ax1.plot(l0, 0.3, "o", ms=5, color=ORANGE, mec="white", mew=0.4, zorder=5)
ax1.text(0.28, 0.62, "each height is hit once:\ninjective (one-to-one)", fontsize=8, color=INK)
ax1.set_xlabel(r"$\lambda$"); ax1.set_ylabel(r"$e^{-5\lambda}$"); ax1.set_title(r"Injective: $\lambda \mapsto e^{-5\lambda}$")
ax1.set_ylim(0, 1.05)

x = np.linspace(-2, 2, 300)
ax2.plot(x, x ** 2, color=BLUE)
ax2.axhline(1, color=ORANGE, lw=0.9, ls="--")
for xx in (-1, 1):
    ax2.plot(xx, 1, "o", ms=5, color=ORANGE, mec="white", mew=0.4, zorder=5)
ax2.text(0, 3.3, "height 1 is hit twice:\nnot injective", fontsize=8, color=INK, ha="center")
ax2.set_xlabel(r"$x$"); ax2.set_ylabel(r"$x^2$"); ax2.set_title(r"Not injective: $x \mapsto x^2$ on $[-2, 2]$")
ax2.set_ylim(0, 4.3)
save(fig, "fig_tk_injective")
