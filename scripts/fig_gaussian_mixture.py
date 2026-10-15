"""A two-component Gaussian mixture. Left: the two weighted components and
their sum, the mixture density. Right: 400 simulated draws, histogrammed and
split by the latent component Z that produced each one; every draw comes from
exactly one component, and the mixture is what you see when you cannot tell
which."""
from _style import *

pi1, mu1, var1 = 0.3, -1.5, 0.5
mu2, var2 = 2.0, 1.0
sd1, sd2 = math.sqrt(var1), math.sqrt(var2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL)

x = np.linspace(-5, 6, 900)
f1, f2 = norm_pdf(x, mu1, sd1), norm_pdf(x, mu2, sd2)
ax1.plot(x, pi1 * f1, color=BLUE, ls=DASHES[1], label=rf"$\pi f_1$, $\pi = {pi1}$")
ax1.plot(x, (1 - pi1) * f2, color=ORANGE, ls=DASHES[2], label=rf"$(1-\pi) f_2$")
ax1.plot(x, pi1 * f1 + (1 - pi1) * f2, color=INK, lw=1.5, label=r"mixture $f = \pi f_1 + (1-\pi) f_2$")
ax1.set_xlabel(r"$x$")
ax1.set_ylabel("density")
ax1.set_title("The density is a weighted sum")
ax1.set_ylim(0, 0.40)
ax1.legend(fontsize=7.5, loc="upper left")

r = rng(21)
N = 400
Z = r.binomial(1, pi1, size=N)
X = np.where(Z == 1, r.normal(mu1, sd1, size=N), r.normal(mu2, sd2, size=N))
bins = np.linspace(-5, 6, 45)
ax2.hist([X[Z == 1], X[Z == 0]], bins=bins, stacked=True, color=[BLUE, ORANGE], alpha=0.75, lw=0,
         label=[rf"$Z = 1$: from $f_1$ ({(Z == 1).sum()} draws)", rf"$Z = 0$: from $f_2$ ({(Z == 0).sum()} draws)"], density=True)
ax2.plot(x, pi1 * f1 + (1 - pi1) * f2, color=INK, lw=1.2)
ax2.set_xlabel(r"$x$")
ax2.set_title(rf"$n = {N}$ draws, colored by the hidden $Z$")
ax2.set_ylim(0, 0.40)
ax2.legend(fontsize=7.5, loc="upper left")
save(fig, "fig_gaussian_mixture")
