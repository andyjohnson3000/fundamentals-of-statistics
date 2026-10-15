"""Total variation for the effect sizes of an introductory course. Each
panel shows two Gaussians with the same standard deviation whose means differ
by Cohen's d standard deviations, the shared area shaded. Cohen's
conventional small, medium and large effects (d = 0.2, 0.5, 0.8) leave the
two distributions sharing 92%, 80% and 69% of their mass: TV = 2 Phi(d/2) - 1
= 0.080, 0.197, 0.311. Even a 'large' effect is a modest distance between
distributions."""
from _style import *

fig, axes = plt.subplots(1, 3, figsize=(6.0, 2.2), sharey=True, layout="constrained")
x = np.linspace(-3.4, 4.2, 700)
for ax, (d, name) in zip(axes, [(0.2, "small"), (0.5, "medium"), (0.8, "large")]):
    f, g = norm_pdf(x, 0, 1), norm_pdf(x, d, 1)
    ax.fill_between(x, 0, np.minimum(f, g), color=GRAY, alpha=0.25, lw=0)
    ax.plot(x, f, color=BLUE, lw=1.2)
    ax.plot(x, g, color=ORANGE, lw=1.2, ls=DASHES[1])
    tv = float(2 * norm_cdf(d / 2) - 1)
    ax.text(0.5, 0.97, rf"shared ${100 * (1 - tv):.0f}\%$" + "\n" + rf"$\mathrm{{TV}} = {tv:.3f}$",
            transform=ax.transAxes, ha="center", va="top", fontsize=7.5, color=INK)
    ax.set_title(rf"{name} effect, $d = {d}$", fontsize=8.5)
    ax.set_yticks([]); ax.grid(False)
    ax.set_xticks([]); ax.set_xlabel(r"means $0$ and $d$, standard deviation $1$", fontsize=7.5)
    ax.set_ylim(0, 0.56); ax.set_xlim(-3.4, 4.2)
save(fig, "fig_tv_cohen")
