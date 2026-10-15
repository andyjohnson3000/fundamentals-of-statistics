"""Two inequalities the book uses in every convergence proof. Left, Markov:
for Y >= 0, the step function a * 1(Y >= a) sits below Y everywhere, so its
expectation a * P(Y >= a) is at most E[Y]. Right, Chebyshev: the probability
of being more than k standard deviations from the mean is at most 1/k^2, for
every distribution; the exact tail probabilities of the Gaussian and of
Expo(1) are far below the bound, which is why Chebyshev proves convergence
but never says how fast."""
from _style import *

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, gridspec_kw=dict(wspace=0.32))
y = np.linspace(0, 5, 400); a = 2.0
ax1.plot(y, y, color=INK, lw=1.2, label=r"$Y$")
ax1.plot(y[y < a], np.zeros_like(y[y < a]), color=ORANGE, lw=1.8)
ax1.plot(y[y >= a], a * np.ones_like(y[y >= a]), color=ORANGE, lw=1.8, label=r"$a \cdot \mathbb{1}(Y \geq a)$")
ax1.fill_between(y[y >= a], a, y[y >= a], color=BLUE, alpha=0.12, lw=0)
ax1.fill_between(y[y < a], 0, y[y < a], color=BLUE, alpha=0.12, lw=0)
ax1.set_xlabel(r"value of $Y$"); ax1.set_title(r"Markov: $a\,\mathbb{1}(Y \geq a) \leq Y$", fontsize=9)
ax1.legend(loc="upper left"); ax1.set_xticks([a]); ax1.set_xticklabels([r"$a$"])

k = np.linspace(1, 4, 300)
ax2.plot(k, 1 / k ** 2, color=INK, lw=1.3, label=r"Chebyshev bound $1/k^2$")
ax2.plot(k, 2 * (1 - norm_cdf(k)), color=BLUE, ls=DASHES[1], label=r"exact, Gauss$(0,1)$")
# Expo(1): mean 1, sd 1: P(|X-1| >= k) = P(X >= 1+k) + P(X <= 1-k) = e^{-(1+k)} + (1 - e^{-(1-k)} if k<1 else 0)
ex = np.exp(-(1 + k)) + np.where(k < 1, 1 - np.exp(-(1 - k)), 0)
ax2.plot(k, ex, color=ORANGE, ls=DASHES[2], label=r"exact, Expo$(1)$")
ax2.set_xlabel(r"$k$ (standard deviations from the mean)"); ax2.set_ylabel(r"$\mathbb{P}(|X - \mu| \geq k\sigma)$")
ax2.set_title("Chebyshev: one bound, every distribution", fontsize=9)
ax2.legend(fontsize=7)
save(fig, "fig_tk_inequalities")
