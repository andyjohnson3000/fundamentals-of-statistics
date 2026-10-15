"""A statistical model is a family of candidate distributions, one for each
value of the parameter. Left: the Bernoulli family (one parameter p). Middle:
the Poisson family (one parameter lambda). Right: the map from the Gaussian
parameter space (mu, sigma^2) to densities, four points marked A to D."""
from _style import *

fig = plt.figure(figsize=(6.0, 4.6))
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.15], hspace=0.75, wspace=0.3)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])

# Bernoulli family
ps = [0.2, 0.5, 0.8]
w = 0.22
for k, p in enumerate(ps):
    ax1.bar(np.array([0, 1]) + (k - 1) * w, [1 - p, p], width=w, color=SERIES[k], alpha=0.85, lw=0,
            label=rf"$p = {p}$")
ax1.set_xticks([0, 1])
ax1.set_xlabel(r"$x$")
ax1.set_ylabel("probability")
ax1.set_title("Bernoulli family\n" + r"$\{\mathrm{Bern}(p)\}_{p \in (0,1)}$")
ax1.legend(fontsize=7)

# Poisson family
k = np.arange(0, 13)
for j, lam in enumerate([1, 3, 6]):
    pm = np.exp(-lam + k * math.log(lam) - np.array([math.lgamma(i + 1) for i in k]))
    ax2.plot(k, pm, "o-", ms=3, color=SERIES[j], ls=DASHES[j], lw=1.0, label=rf"$\lambda = {lam}$")
ax2.set_xlabel(r"$x$")
ax2.set_title("Poisson family\n" + r"$\{\mathrm{Pois}(\lambda)\}_{\lambda > 0}$")
ax2.legend(fontsize=7)

# Gaussian: parameter space on the left, densities on the right
pts = {"A": (0, 1), "B": (3, 1), "C": (0, 4), "D": (3, 0.25)}
for lab, (mu, var) in pts.items():
    ax3.plot(mu, var, "o", ms=5, color=INK)
    ax3.annotate(lab, (mu, var), xytext=(5, 3), textcoords="offset points", fontsize=9, color=INK)
ax3.axhline(0, color=GRAY, lw=0.7)
ax3.set_xlim(-2.5, 5.5)
ax3.set_ylim(-0.4, 5)
ax3.set_xlabel(r"$\mu$")
ax3.set_ylabel(r"$\sigma^2$")
ax3.set_title("Gaussian parameter space\n" + r"$\Theta = \mathbb{R} \times (0, \infty)$")
ax3.text(-2.3, 0.15, r"$\sigma^2 = 0$ excluded", fontsize=7, color=GRAY, ha="left")

x = np.linspace(-4, 7, 800)
for j, (lab, (mu, var)) in enumerate(pts.items()):
    ax4.plot(x, norm_pdf(x, mu, math.sqrt(var)), color=SERIES[j], ls=DASHES[j],
             label=rf"{lab}: $\mathrm{{Gauss}}({mu}, {var})$")
ax4.set_xlabel(r"$x$")
ax4.set_title("The distributions the points map to\n" + r"$\theta \longmapsto \mathbb{P}_\theta$")
ax4.legend(fontsize=7, loc="upper left")

save(fig, "fig_model_families")
