"""Newton's method on the kiss log-likelihood in the log-odds theta, from
theta = 0: each step maximizes the parabola that matches the slope and
curvature at the current point. Iterates 0, 0.581, 0.598 (converged)."""
from _style import *

n, s = 124, 80
th = np.linspace(-0.6, 1.4, 400)
ll = s * th - n * np.log1p(np.exp(th)); top = ll.max()
fig, ax = plt.subplots(figsize=(4.6, 2.9), layout="constrained")
ax.plot(th, ll - top, color=BLUE, lw=1.4)
t = 0.0
for k, col in enumerate((ORANGE, AQUA)):
    p = np.exp(t) / (1 + np.exp(t)); l0 = s * t - n * np.log1p(np.exp(t)); g = s - n * p; h = n * p * (1 - p)
    par = l0 + g * (th - t) - h * (th - t) ** 2 / 2
    ax.plot(th, par - top, color=col, lw=1.1, ls=DASHES[k + 1])
    ax.plot([t], [l0 - top], "o", color=col, ms=4)
    t_new = t + g / h
    ax.annotate("", xy=(t_new, l0 + g * (t_new - t) - h * (t_new - t) ** 2 / 2 - top), xytext=(t, l0 - top),
                arrowprops=dict(arrowstyle="->", color=col, lw=0.9))
    print(k, t, t_new); t = t_new
ax.plot([t], [s * t - n * np.log1p(np.exp(t)) - top], "o", color=INK, ms=4)
ax.set_ylim(-9, 1.5); ax.set_xlabel(r"$\theta$ (log-odds)"); ax.set_ylabel("log-likelihood, from its maximum")
ax.text(0.0, -8.4, r"$\theta_0 = 0$", color=ORANGE, fontsize=8, ha="center")
ax.text(0.62, 0.75, r"$\theta_1 = 0.581$, then $\hat\theta = 0.598$", color=INK, fontsize=8, ha="left")
ax.text(-0.55, -2.6, "parabola at $\\theta_0$", color=ORANGE, fontsize=7.5, ha="left")
ax.text(0.98, -1.3, "parabola at $\\theta_1$", color=AQUA, fontsize=7.5, ha="left")
ax.set_title("Newton's method: climb the fitted parabola")
save(fig, "fig_glm_newton")
