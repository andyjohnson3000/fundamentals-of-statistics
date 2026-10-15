"""The delta method as a picture: a narrow Gaussian around theta on the horizontal
axis is pushed through g, and comes out as a Gaussian around g(theta) whose width
is scaled by |g'(theta)|. Here g(x) = 1/x, theta = 6.23 (the T example), and the
input sd is sigma/sqrt(n) = 6.23/8 ~ 0.78."""
from _style import *

theta = 6.23
sd_in = theta / math.sqrt(64)       # sigma / sqrt(n) with sigma = 1/lambda = theta
g = lambda x: 1 / x
gp = -1 / theta ** 2
sd_out = abs(gp) * sd_in

fig, ax = plt.subplots(figsize=(4.8, 3.6))
x = np.linspace(3.2, 10.5, 600)
ax.plot(x, g(x), color=INK, lw=1.3)
ax.text(9.6, g(9.6) + 0.012, r"$g(x) = 1/x$", fontsize=9, color=INK)

# tangent line at theta
xt = np.linspace(theta - 1.9, theta + 1.9, 50)
ax.plot(xt, g(theta) + gp * (xt - theta), color=ORANGE, ls="--", lw=1.1)
ax.text(theta + 2.0, g(theta) + gp * 2.0 - 0.022, r"tangent, slope $g'(\theta)$", fontsize=8, color=INK, va="top")

# input density drawn on the x-axis (baseline y = 0.0)
xs = np.linspace(theta - 3 * sd_in, theta + 3 * sd_in, 300)
base_y = 0.03
scale_in = 0.055
ax.fill_between(xs, base_y, base_y + scale_in * norm_pdf(xs, theta, sd_in) / norm_pdf(theta, theta, sd_in),
                color=BLUE, alpha=0.30, lw=0)
ax.plot(xs, base_y + scale_in * norm_pdf(xs, theta, sd_in) / norm_pdf(theta, theta, sd_in), color=BLUE, lw=1.0)
# label beside the density, in the empty lower-right corner, with a short
# leader to the density's right tail (past the theta + 2 sd guide line)
ax.text(8.75, 0.047, r"$\hat\theta_n \approx$" + "\n" + r"$\mathrm{Gauss}(\theta, \sigma^2/n)$", ha="left", va="center",
        fontsize=8, color=INK, linespacing=1.15)
ax.annotate("", xy=(8.3, base_y + scale_in * norm_pdf(8.3, theta, sd_in) / norm_pdf(theta, theta, sd_in)),
            xytext=(8.7, 0.040), arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6, shrinkA=0, shrinkB=2))

# output density drawn on the y-axis (baseline x = 3.2)
ys = np.linspace(g(theta) - 3 * sd_out, g(theta) + 3 * sd_out, 300)
base_x = 3.25
scale_out = 0.9
ax.fill_betweenx(ys, base_x, base_x + scale_out * norm_pdf(ys, g(theta), sd_out) / norm_pdf(g(theta), g(theta), sd_out),
                 color=AQUA, alpha=0.30, lw=0)
ax.plot(base_x + scale_out * norm_pdf(ys, g(theta), sd_out) / norm_pdf(g(theta), g(theta), sd_out), ys, color=AQUA, lw=1.0)
ax.text(4.9, 0.318, r"$g(\hat\theta_n) \approx \mathrm{Gauss}(g(\theta),\, g'(\theta)^2 \sigma^2/n)$",
        fontsize=8, color=INK, va="top")

# guide lines
ax.plot([theta, theta], [0, g(theta)], color=GRAY, lw=0.6, ls=":")
ax.plot([base_x, theta], [g(theta), g(theta)], color=GRAY, lw=0.6, ls=":")
for s in (-2, 2):
    xx = theta + s * sd_in
    ax.plot([xx, xx], [0, g(theta) + gp * (xx - theta)], color=GRAY, lw=0.5, ls=":")
    ax.plot([base_x, xx], [g(theta) + gp * (xx - theta)] * 2, color=GRAY, lw=0.5, ls=":")

ax.set_xlim(3.2, 10.5)
ax.set_ylim(0, 0.33)
ax.set_xticks([theta])
ax.set_xticklabels([r"$\theta$"])
ax.set_yticks([g(theta)])
ax.set_yticklabels([r"$g(\theta)$"])
ax.grid(False)
save(fig, "fig_delta_method")
