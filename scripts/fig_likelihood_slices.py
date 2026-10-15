"""One function, two readings. Left: the probability that k of 124 couples
turn right, P_p(count = k), as a function of both the count k and the
parameter p (darker = more probable). Reading it along a horizontal line, with
p fixed, gives the distribution of the count (probability: the data vary).
Reading it along a vertical line, with the count fixed at the observed 80,
gives the likelihood (statistics: the parameter varies). Middle: the vertical
slice at p = 0.645, a PMF over k that sums to 1. Right: the horizontal slice
at k = 80, the likelihood in p, peaking at 80/124 = 0.645; it does not
integrate to 1 (its area is 1/125)."""
from _style import *
from math import lgamma, log

n = 124
ks = np.arange(40, 105)
ps = np.linspace(0.35, 0.9, 400)
def logpmf(k, p):
    return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1) + k * np.log(p) + (n - k) * np.log(1 - p)
Z = np.array([[np.exp(logpmf(k, p)) for k in ks] for p in ps])

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(6.0, 2.5), layout="constrained")
ax1.pcolormesh(ks, ps, Z, cmap="Blues", shading="auto", rasterized=True)
ax1.axvline(80, color=ORANGE, lw=1.2)
ax1.axhline(0.645, color=AQUA, lw=1.2, ls=DASHES[1])
ax1.set_xlabel(r"count $k$"); ax1.set_ylabel(r"parameter $p$")
ax1.set_title(r"$\Pr_p(\mathrm{count} = k)$")
ax1.grid(False)

pm = np.exp([logpmf(k, 0.645) for k in ks])
ax2.bar(ks, pm, width=0.9, color=AQUA, alpha=0.8, edgecolor="none")
ax2.set_xlabel(r"count $k$"); ax2.set_yticks([])
ax2.set_title(r"fix $p = 0.645$: a PMF")
ax2.set_xlim(40, 104)

lik = np.exp([logpmf(80, p) for p in ps])
ax3.plot(ps, lik, color=ORANGE, lw=1.4)
ax3.set_xlabel(r"parameter $p$"); ax3.set_yticks([])
ax3.set_title(r"fix $k = 80$: a likelihood")
ax3.set_xlim(0.35, 0.9)
save(fig, "fig_likelihood_slices")
print("sum pmf", pm.sum(), "area lik", np.trapezoid(lik, ps))
