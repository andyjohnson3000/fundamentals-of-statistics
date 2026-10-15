"""Why the asymptotic variance is not the limit of the variance. For the
kiss-model estimator p-hat = Rbar_n with p = 0.645: Var(p-hat) = p(1-p)/n goes to zero
(left), while n Var(p-hat) = p(1-p) stays flat at the asymptotic variance
(right). Dots are variances estimated from 4,000 simulated samples."""
from _style import *

p = 0.645
ns = np.arange(2, 301)
v = p * (1 - p) / ns
r = rng(9)
sim_ns = [2, 5, 10, 20, 40, 80, 124, 200, 300]
sim_var = []
for n in sim_ns:
    X = r.binomial(1, p, size=(4000, n)).mean(axis=1)
    sim_var.append(X.var())
sim_var = np.array(sim_var)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
ax1.plot(ns, v, color=BLUE, label=r"$\mathbb{V}\mathrm{ar}(\hat p) = p(1-p)/n$")
ax1.plot(sim_ns, sim_var, "o", ms=4, color=ORANGE, mec="white", mew=0.4, label="simulated")
ax1.set_xlabel(r"$n$")
ax1.set_ylabel("variance")
ax1.set_title(r"The variance of $\hat p$ vanishes")
ax1.legend()

ax2.plot(ns, ns * v, color=BLUE, label=r"$n \cdot \mathbb{V}\mathrm{ar}(\hat p) = p(1-p)$")
ax2.plot(sim_ns, np.array(sim_ns) * sim_var, "o", ms=4, color=ORANGE, mec="white", mew=0.4, label="simulated")
ax2.axhline(p * (1 - p), color=GRAY, lw=0.7, ls="--")
ax2.text(300, p * (1 - p) + 0.022, r"asymptotic variance $\sigma^2 = 0.229$", ha="right", va="bottom",
         fontsize=7.5, color=INK)
ax2.set_ylim(0, 0.35)
ax2.set_xlabel(r"$n$")
ax2.set_title(r"The variance of $\sqrt{n}\,(\hat p - p)$ does not")
ax2.legend(loc="lower right")
save(fig, "fig_asymptotic_variance")
