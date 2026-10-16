"""A cloud of independent standard Gaussian pairs is round, so rotating the
axes gives independent standard Gaussian coordinates again. Left: 1,500
draws of (Z_1, Z_2), with the rotated axes u_1 = (1, 1)/sqrt(2) (the
direction of the sample mean) and u_2 = (1, -1)/sqrt(2) (the direction of
the deviations from it). Right: the same points in the rotated
coordinates Y_1 = (Z_1 + Z_2)/sqrt(2) = sqrt(2) Z-bar and
Y_2 = (Z_1 - Z_2)/sqrt(2). Gray circles: contours of the density."""
from _style import *

g = rng(7)
Z = g.standard_normal((1500, 2))
Y = np.column_stack([(Z[:, 0] + Z[:, 1]) / math.sqrt(2), (Z[:, 0] - Z[:, 1]) / math.sqrt(2)])

fig, axes = plt.subplots(1, 2, figsize=(6.0, 3.1), layout="constrained")
for ax, P, title in [(axes[0], Z, "the data cloud and the rotated axes"), (axes[1], Y, "the same points in rotated coordinates")]:
    ax.scatter(P[:, 0], P[:, 1], s=4, color=BLUE, alpha=0.35, linewidths=0)
    th = np.linspace(0, 2 * math.pi, 400)
    for r in [1, 2, 3]:
        ax.plot(r * np.cos(th), r * np.sin(th), color=GRAY, lw=0.6, ls=DASHES[3])
    ax.set_xlim(-3.6, 3.6); ax.set_ylim(-3.6, 3.6)
    ax.set_aspect("equal")
    ax.set_title(title)
ax = axes[0]
L = 3.4
ax.plot([-L / math.sqrt(2), L / math.sqrt(2)], [-L / math.sqrt(2), L / math.sqrt(2)], color=ORANGE, lw=1.3)
ax.plot([-L / math.sqrt(2), L / math.sqrt(2)], [L / math.sqrt(2), -L / math.sqrt(2)], color=AQUA, lw=1.3, ls=DASHES[2])
ax.set_xlabel(r"$Z_1$"); ax.set_ylabel(r"$Z_2$")
ax.text(2.55, 2.0, r"$u_1$: mean", color=ORANGE, fontsize=7.5, ha="left")
ax.text(2.55, -2.25, r"$u_2$: deviation", color=AQUA, fontsize=7.5, ha="left")
ax = axes[1]
ax.axhline(0, color=ORANGE, lw=1.3)
ax.axvline(0, color=AQUA, lw=1.3, ls=DASHES[2])
ax.set_xlabel(r"$Y_1 = \sqrt{2}\,\bar Z$"); ax.set_ylabel(r"$Y_2 = (Z_1 - Z_2)/\sqrt{2}$")
save(fig, "fig_gaussian_rotation")
