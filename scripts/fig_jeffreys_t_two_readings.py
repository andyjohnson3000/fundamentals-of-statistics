"""One t density, read two ways, for the wind turbine (n = 12, mean 14.3,
s = 4.7). Left: if mu = 10, the sampling distribution of the standardized
mean puts probability 0.0045 above the observed 3.17 (orange); this is the
one-sided p-value. Right: given the data and the prior flat in mu times
1/sigma, the posterior of mu is 14.3 + (4.7/sqrt(12)) t_11, which puts
posterior probability 0.0045 below 10 (orange) and 0.95 on the t-interval
[11.3, 17.3] (blue)."""
from _style import *
from math import lgamma, pi, sqrt

n, xbar, s = 12, 14.3, 4.7
se = s / sqrt(n)
nu = n - 1


def t_pdf(t, k):
    c = math.exp(lgamma((k + 1) / 2) - lgamma(k / 2)) / sqrt(k * pi)
    return c * (1 + t * t / k) ** (-(k + 1) / 2)


tobs = (xbar - 10) / se
q975 = 2.200985  # 97.5% point of t_11

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
t = np.linspace(-5, 5, 1200)
ax1.plot(t, t_pdf(t, nu), color=INK, lw=1.2)
m = t >= tobs
ax1.fill_between(t[m], 0, t_pdf(t[m], nu), color=ORANGE, lw=0)
ax1.vlines(tobs, 0, 0.33, color=GRAY, lw=0.8, ls=DASHES[3])
ax1.set_xlim(-5, 5); ax1.set_ylim(0, 0.45)
ax1.set_xlabel(r"$\sqrt{12}\,(\bar{X}_{12} - 10)/S$ when $\mu = 10$")
ax1.set_ylabel("density")
ax1.set_title(r"before the data, if $\mu = 10$")
note(ax1, "observed 3.17", (tobs, 0.33), (tobs, 0.355), ha="center", leader=False)
note(ax1, "0.0045", (3.6, 0.002), (3.75, 0.09), ha="left")

mu = np.linspace(xbar - 5 * se, xbar + 5 * se, 1200)
dens = t_pdf((mu - xbar) / se, nu) / se
ax2.plot(mu, dens, color=INK, lw=1.2)
lo, hi = xbar - q975 * se, xbar + q975 * se
mm = (mu >= lo) & (mu <= hi)
ax2.fill_between(mu[mm], 0, dens[mm], color=BLUE, alpha=0.30, lw=0)
ml = mu <= 10
ax2.fill_between(mu[ml], 0, dens[ml], color=ORANGE, lw=0)
ax2.axvline(10, color=GRAY, lw=0.8, ls=DASHES[3])
ax2.set_xlim(mu[0], mu[-1]); ax2.set_ylim(0, 0.45 / se)
ax2.set_xlabel(r"$\mu$ (miles per hour)")
ax2.set_title(r"after the data, $\bar{x} = 14.3$")
note(ax2, r"$\mu = 10$", (10, 0.25), (8.1, 0.30), ha="left", leader=False)
note(ax2, "0.0045", (9.8, 0.002), (8.2, 0.06), ha="left")
save(fig, "fig_jeffreys_t_two_readings")
print("t_obs", tobs, "interval", lo, hi)
