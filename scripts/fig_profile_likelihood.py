"""A likelihood ratio test with a nuisance parameter: the wind-turbine data
(n = 12 monthly wind speeds, mean 14.3, standard deviation 4.7), modeled as
Gauss(mu, sigma^2), null mu0 = 10 with sigma^2 unknown. Left: contours of
the log-likelihood l_n(mu, sigma^2) minus its maximum, at -1, -2, -3.89 and
-6, with the peak (black dot) at the maximum likelihood estimate (14.3,
20.25), the null line mu = 10 (gray, dotted) and the constrained maximum on
it (orange dot) at (10, 38.74). Right: the profile log-likelihood, the
highest value of l_n on each vertical line mu = constant, minus its maximum
(blue); at mu = 10 it is -3.89, half the likelihood ratio statistic 7.78.
The dotted line at -1.92 = -3.84/2 cuts out the 95% likelihood ratio
interval (blue bar); the black bar is the exact t interval."""
from _style import *

n, xbar, s = 12, 14.3, 4.7
SS = (n - 1) * s ** 2               # sum of squared deviations
s2h = SS / n                        # MLE of sigma^2
mu0 = 10.0


def ll(mu, v):
    return -0.5 * n * np.log(2 * math.pi * v) - (SS + n * (xbar - mu) ** 2) / (2 * v)


top = ll(xbar, s2h)
v0 = s2h + (xbar - mu0) ** 2
LR = 2 * (top - ll(mu0, v0))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
M, V = np.meshgrid(np.linspace(6, 22.5, 400), np.linspace(6, 90, 400))
Z = ll(M, V) - top
levels = [-6, -LR / 2, -2, -1]
cs = ax1.contour(M, V, Z, levels=levels, colors=[GRAY, ORANGE, BLUE, BLUE], linewidths=[0.8, 1.1, 0.9, 0.9],
                 linestyles=["-", "--", "-", "-"])
ax1.axvline(mu0, color=GRAY, lw=0.8, ls=DASHES[3])
ax1.plot([xbar], [s2h], "o", ms=4.5, color=INK, zorder=5)
ax1.plot([mu0], [v0], "o", ms=4.5, color=ORANGE, zorder=5)
note(ax1, "(10, 38.7)", (mu0, v0), (11.8, 66), ha="left")
ax1.text(10.2, 86, r"$\mu = 10$", fontsize=7.5, color=GRAY, ha="left", va="top")
ax1.set_xlim(6, 22.5); ax1.set_ylim(6, 90)
ax1.set_xlabel(r"$\mu$ (miles per hour)"); ax1.set_ylabel(r"$\sigma^2$")
ax1.set_title("log-likelihood contours")

mu = np.linspace(6, 22.5, 600)
prof = ll(mu, s2h + (xbar - mu) ** 2) - top
ax2.plot(mu, prof, color=BLUE, lw=1.4)
ax2.axhline(-3.841459 / 2, color=GRAY, lw=0.8, ls=DASHES[3])
ax2.axvline(mu0, color=GRAY, lw=0.6, ls=DASHES[3])
ax2.plot([mu0], [-LR / 2], "o", ms=4.5, color=ORANGE, zorder=5)
half = math.sqrt(s2h * (math.exp(3.841459 / n) - 1))
lo, hi = xbar - half, xbar + half
tq = 2.200985                                         # t_11 quantile, 2.5% above
tlo, thi = xbar - tq * s / math.sqrt(n), xbar + tq * s / math.sqrt(n)
ax2.plot([lo, hi], [-4.6, -4.6], color=BLUE, lw=2.0, solid_capstyle="butt")
ax2.plot([tlo, thi], [-5.2, -5.2], color=INK, lw=2.0, solid_capstyle="butt")
ax2.text(xbar, -4.45, "LR", fontsize=7.5, color=BLUE, ha="center", va="bottom")
ax2.text(xbar, -5.35, r"exact $t$", fontsize=7.5, color=INK, ha="center", va="top")
note(ax2, f"$-{LR / 2:.2f}$", (mu0, -LR / 2), (6.4, -2.6), ha="left")
ax2.text(22.2, -1.92 + 0.12, r"$-1.92$", fontsize=7.5, color=GRAY, ha="right", va="bottom")
ax2.set_xlim(6, 22.5); ax2.set_ylim(-6.1, 0.4)
ax2.set_xlabel(r"$\mu$ (miles per hour)"); ax2.set_ylabel("profile log-likelihood")
ax2.set_title("the profile along $\\mu$")
save(fig, "fig_profile_likelihood")
print("s2h", s2h, "v0", v0, "LR", LR, "LR interval", lo, hi, "t interval", tlo, thi)
