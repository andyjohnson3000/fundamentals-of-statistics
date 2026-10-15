"""Maximum likelihood without calculus. Five draws from Unif(0, theta) (rug on
the axis; largest 7.6). Left: the likelihood L(theta) = theta^(-n) for
theta >= max x_i and 0 below it. It jumps up at the largest observation and
decreases after, so the maximum is at the jump, theta-hat = max x_i = 7.6,
where the derivative is never 0. Right: the sampling distribution of the
maximum when theta = 10 and n = 5 (density 5 m^4 / 10^5 on [0, 10]); it
always falls short of theta, with mean n theta / (n + 1) = 8.33."""
from _style import *

x = np.array([1.9, 3.4, 5.1, 6.2, 7.6]); n = len(x); m = x.max()
th = np.linspace(0.5, 16, 800)
L = np.where(th >= m, th ** (-n), 0.0)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
ax1.plot(th[th < m], L[th < m] * 1e5, color=BLUE, lw=1.4)
ax1.plot(th[th >= m], L[th >= m] * 1e5, color=BLUE, lw=1.4)
ax1.plot([m, m], [0, m ** (-n) * 1e5], color=BLUE, lw=0.6, ls=":")
ax1.plot([m], [m ** (-n) * 1e5], "o", ms=4, color=ORANGE, zorder=5)
ax1.plot([m], [0], "o", ms=4, mfc="white", mec=BLUE, zorder=5)
ax1.plot(x, np.full(n, -0.22), "|", ms=5, color=INK, clip_on=False)
ax1.set_xlim(0, 16); ax1.set_ylim(-0.35, 4.4)
ax1.set_xlabel(r"$\theta$"); ax1.set_ylabel(r"$L(\theta)$, units of $10^{-5}$")
ax1.set_title(r"likelihood of $\mathrm{Unif}(0, \theta)$, $n = 5$")
note(ax1, r"maximum at the largest" + "\n" + r"observation, $\hat\theta = 7.6$", (m, m ** (-n) * 1e5), (9.5, 3.6), ha="left")
note(ax1, r"zero: $\theta$ below an observation" + "\n" + "is impossible", (4, 0.02), (0.5, 1.8), ha="left")

t = 10.0; mm = np.linspace(0, t, 500)
ax2.plot(mm, n * mm ** (n - 1) / t ** n, color=AQUA, lw=1.4)
ax2.fill_between(mm, 0, n * mm ** (n - 1) / t ** n, color=AQUA, alpha=0.2, lw=0)
ax2.axvline(t, color=INK, lw=0.8, ls=DASHES[1])
ax2.axvline(n * t / (n + 1), color=GRAY, lw=0.8, ls=":")
ax2.set_xlim(0, 11.5); ax2.set_ylim(0, 0.6)
ax2.set_xlabel(r"$\max_i X_i$ when $\theta = 10$")
ax2.set_title(r"the maximum falls short of $\theta$")
ax2.text(10.1, 0.56, r"$\theta = 10$", fontsize=7.5, color=INK, ha="left", va="top")
ax2.text(8.2, 0.56, "mean\n8.33", fontsize=7.5, color=GRAY, ha="right", va="top")
save(fig, "fig_uniform_likelihood")
