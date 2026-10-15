"""A steep g amplifies the error, a flat g damps it. The same input Gaussian,
Rbar_n ~ Gauss(p, p(1-p)/n) with p = 0.645 and n = 124 (sd 0.043), pushed
through two functions. Left: the odds g(p) = p/(1-p), slope 1/(1-p)^2 = 7.9
at p = 0.645, so the output sd is 7.9 x 0.043 = 0.34. Right: the variance
g(p) = p(1-p), slope 1 - 2p = -0.29, so the output sd is 0.29 x 0.043 =
0.012. Same data, same precision in p, very different precision in g(p)."""
from _style import *

p, n = 0.645, 124
sd_in = math.sqrt(p * (1 - p) / n)


def panel(ax, g, gp, xlim, ylim, name, label_pos):
    x = np.linspace(xlim[0], xlim[1], 600)
    ax.plot(x, g(x), color=INK, lw=1.3)
    slope = gp(p)
    sd_out = abs(slope) * sd_in
    xt = np.linspace(p - 0.12, p + 0.12, 50)
    ax.plot(xt, g(p) + slope * (xt - p), color=ORANGE, ls="--", lw=1.1)
    # input density on the x axis
    xs = np.linspace(p - 3 * sd_in, p + 3 * sd_in, 300)
    base_y = ylim[0] + 0.02 * (ylim[1] - ylim[0])
    scale_in = 0.16 * (ylim[1] - ylim[0])
    dens = norm_pdf(xs, p, sd_in) / norm_pdf(p, p, sd_in)
    ax.fill_between(xs, base_y, base_y + scale_in * dens, color=BLUE, alpha=0.30, lw=0)
    ax.plot(xs, base_y + scale_in * dens, color=BLUE, lw=1.0)
    # output density on the y axis
    ys = np.linspace(g(p) - 3 * sd_out, g(p) + 3 * sd_out, 300)
    base_x = xlim[0] + 0.02 * (xlim[1] - xlim[0])
    scale_out = 0.16 * (xlim[1] - xlim[0])
    dens_o = norm_pdf(ys, g(p), sd_out) / norm_pdf(g(p), g(p), sd_out)
    ax.fill_betweenx(ys, base_x, base_x + scale_out * dens_o, color=AQUA, alpha=0.30, lw=0)
    ax.plot(base_x + scale_out * dens_o, ys, color=AQUA, lw=1.0)
    ax.plot([p, p], [ylim[0], g(p)], color=GRAY, lw=0.6, ls=":")
    ax.plot([xlim[0], p], [g(p), g(p)], color=GRAY, lw=0.6, ls=":")
    for s in (-2, 2):
        xx = p + s * sd_in
        yy = g(p) + slope * (xx - p)
        ax.plot([xx, xx], [ylim[0], yy], color=GRAY, lw=0.5, ls=":")
        ax.plot([xlim[0], xx], [yy, yy], color=GRAY, lw=0.5, ls=":")
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xticks([p]); ax.set_xticklabels([r"$p$"])
    ax.set_yticks([g(p)]); ax.set_yticklabels([r"$g(p)$"])
    ax.grid(False)
    ax.set_title(name)
    # three short lines in the empty corner (upper left on the steep panel,
    # upper right on the flat one), clear of the curve and the two densities
    ax.text(label_pos[0], label_pos[1], rf"$|g'(p)| = {abs(slope):.2f}$" + "\n" + rf"sd in $= {sd_in:.3f}$"
            + "\n" + rf"sd out $= {sd_out:.3f}$", fontsize=7.5, color=INK, ha=label_pos[2], va="top", linespacing=1.15)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.0, 3.1), layout="constrained")
panel(ax1, lambda x: x / (1 - x), lambda x: 1 / (1 - x) ** 2, (0.45, 0.85), (0.5, 4.0),
      r"steep: the odds $g(p) = p/(1-p)$", (0.465, 3.92, "left"))
panel(ax2, lambda x: x * (1 - x), lambda x: 1 - 2 * x, (0.45, 0.85), (0.10, 0.30),
      r"flat: the variance $g(p) = p(1-p)$", (0.845, 0.296, "right"))
save(fig, "fig_delta_steep_flat")
