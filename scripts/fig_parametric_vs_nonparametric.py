"""Parametric versus nonparametric. Left: the exponential family, a curve of
densities traced out by one number lambda. Right: five members of the
nonparametric model 'all unimodal densities', which no finite list of numbers
indexes."""
from _style import *

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

x = np.linspace(0, 5, 600)
for k, lam in enumerate([0.5, 1, 2, 4]):
    ax1.plot(x, lam * np.exp(-lam * x), color=SERIES[k % 4], ls=DASHES[k % 4], label=rf"$\lambda = {lam}$")
ax1.set_ylim(0, 2.2)
ax1.set_xlabel(r"$x$")
ax1.set_ylabel("density")
ax1.set_title(r"Parametric: $\{\mathrm{Expo}(\lambda)\}_{\lambda > 0}$, $\Theta \subseteq \mathbb{R}$")
ax1.legend()

x = np.linspace(-4, 6, 1000)
curves = []
curves.append(norm_pdf(x, 0, 1))                                            # Gaussian
curves.append(0.5 * np.exp(-np.abs(x - 1.5)))                                # Laplace
g = np.where(x > -1, (x + 1) ** 2 * np.exp(-(x + 1) * 1.5), 0); curves.append(g / np.trapezoid(g, x) if hasattr(np, "trapezoid") else g / np.sum(g) / (x[1] - x[0]))  # skewed
t = np.clip(1 - np.abs(x - 3) / 1.5, 0, None); curves.append(t / 1.5)       # triangular
names = ["Gaussian", "Laplace", "skewed", "triangular"]
for k, (c, nm) in enumerate(zip(curves, names)):
    ax2.plot(x, c, color=SERIES[k % 4] if k < 4 else GRAY, ls=DASHES[k % 4], label=nm)
ax2.set_xlabel(r"$x$")
ax2.set_title(r"Nonparametric: all unimodal densities $f$")
ax2.legend(fontsize=7.5, loc="upper left")  # the only empty corner: every peak is at x > -0.5
save(fig, "fig_parametric_vs_nonparametric")
