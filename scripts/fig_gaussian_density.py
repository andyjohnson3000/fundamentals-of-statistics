"""Left: three Gaussian densities, showing what mu and sigma do. Right: the
standard Gaussian with the 68 / 95 / 99.7 percent regions."""
from _style import *

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL)

x = np.linspace(-6, 16, 1200)
for k, (mu, var) in enumerate([(0, 1), (0, 4), (10, 4)]):
    sd = math.sqrt(var)
    ax1.plot(x, norm_pdf(x, mu, sd), color=SERIES[k], ls=DASHES[k],
             label=rf"$\mathrm{{Gauss}}({mu}, {var})$")
ax1.set_xlabel(r"$x$")
ax1.set_ylabel("density")
ax1.set_title(r"$\mu$ moves the center, $\sigma$ sets the width")
ax1.legend()

z = np.linspace(-4, 4, 800)
f = norm_pdf(z)
ax2.plot(z, f, color=INK, lw=1.2)
for k, (lo, hi, lab) in enumerate([(2, 3, r"99.7\%"), (1, 2, r"95\%"), (0, 1, r"68\%")]):
    sel = (np.abs(z) >= lo) & (np.abs(z) <= hi)
    ax2.fill_between(z, 0, f, where=sel, color=BLUE, alpha=0.15 + 0.25 * k, lw=0)
for s, txt in [(1, "68%"), (2, "95%"), (3, "99.7%")]:
    yy = 0.40 + 0.035 * s
    ax2.annotate("", xy=(-s, yy), xytext=(s, yy),
                 arrowprops=dict(arrowstyle="<->", color=GRAY, lw=0.7))
    ax2.text(0, yy + 0.004, txt, ha="center", va="bottom", fontsize=8, color=INK)
ax2.set_xticks([-3, -2, -1, 0, 1, 2, 3])
ax2.set_xticklabels([r"$-3\sigma$", r"$-2\sigma$", r"$-\sigma$", r"$\mu$", r"$\sigma$", r"$2\sigma$", r"$3\sigma$"])
ax2.set_yticks([])
ax2.set_ylim(0, 0.54)
ax2.set_title("The empirical rule, made exact")
ax2.grid(False)
save(fig, "fig_gaussian_density")
