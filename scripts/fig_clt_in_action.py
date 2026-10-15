"""The CLT in action for two parents. Top row: a skewed Exp(1), histogram of
sqrt(n)(Xbar - mu)/sigma over 50,000 replications. Bottom row: the kiss-model
Bernoulli(0.645), where the standardized mean lives on a lattice, so the exact
binomial pmf is drawn as bars with area equal to probability. The N(0,1) density
is overlaid in every panel."""
from _style import *

reps = 50000
r = rng(11)
z = np.linspace(-4, 4, 400)

fig, axes = plt.subplots(2, 4, figsize=(6.0, 3.9), sharex=True, sharey="row")

# Row 1: Exp(1), mu = sigma = 1
for ax, n in zip(axes[0], [1, 5, 30, 200]):
    X = r.exponential(size=(reps, n))
    Z = math.sqrt(n) * (X.mean(axis=1) - 1.0) / 1.0
    ax.hist(Z, bins=80, range=(-4, 4), density=True, color=BLUE, alpha=0.55, lw=0)
    ax.plot(z, norm_pdf(z), color=INK, lw=0.9)
    ax.set_title("Exp(1)\n" + rf"$n={n}$")
    ax.set_ylim(0, 0.75)

# Row 2: Bernoulli(p), p = 0.645 (the kiss experiment), exact lattice pmf as density bars
p = 0.645
sd = math.sqrt(p * (1 - p))
for ax, n in zip(axes[1], [5, 30, 124, 1000]):
    k = np.arange(n + 1)
    zk = math.sqrt(n) * (k / n - p) / sd
    spacing = 1 / (math.sqrt(n) * sd)
    ax.bar(zk, binom_pmf(n, p) / spacing, width=spacing * 0.92, color=AQUA, alpha=0.6, lw=0)
    ax.plot(z, norm_pdf(z), color=INK, lw=0.9)
    ax.set_title("Bern(0.645)\n" + rf"$n={n}$")
    ax.set_xlabel(r"$\sqrt{n}(\bar{X}_n-\mu)/\sigma$")
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 0.75)
axes[0][0].set_ylabel("density")
axes[1][0].set_ylabel("density")
fig.subplots_adjust(hspace=0.55)
save(fig, "fig_clt_in_action")
