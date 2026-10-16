"""The same subway log-likelihood (n = 64, mean wait 6.23 minutes), drawn in
two coordinates. Left: in the rate lambda, l_n(lambda) - l_n(lambda-hat)
(blue) with Wald's parabola in lambda (orange, dashed), centered at
lambda-hat = 0.1605 with curvature n / lambda-hat^2. Right: in the mean wait
mu = 1/lambda, with Wald's parabola in mu (yellow, dotted), centered at
mu-hat = 6.23 with curvature n / mu-hat^2. The null value is lambda0 = 0.2,
which is mu0 = 5 minutes. The blue dots, at the same height -1.67 in both,
give the likelihood ratio statistic 3.34; the parabolas' dots give Wald's
statistic, 2 x 1.94 = 3.87 in lambda and 2 x 1.25 = 2.49 in mu."""
from _style import *

n, tbar = 64, 6.23
lh, mh = 1 / tbar, tbar
l0, m0 = 0.2, 5.0
llE = lambda l: n * np.log(l) - l * n * tbar          # in the rate
top = llE(lh)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained", sharey=True)
lam = np.linspace(0.105, 0.235, 600)
ax1.plot(lam, llE(lam) - top, color=BLUE, lw=1.4)
ax1.plot(lam, -0.5 * n / lh ** 2 * (lam - lh) ** 2, color=ORANGE, lw=1.3, ls=DASHES[1])
ax1.axvline(l0, color=GRAY, lw=0.6, ls=DASHES[3])
ax1.axhline(0, color=GRAY, lw=0.6, ls=DASHES[3])
lr = llE(l0) - top
wl = -0.5 * n / lh ** 2 * (l0 - lh) ** 2
ax1.plot([l0], [lr], "o", ms=4.5, color=BLUE, zorder=5)
ax1.plot([l0], [wl], "o", ms=4.5, color=ORANGE, zorder=5)
note(ax1, f"$-{-lr:.2f}$", (l0, lr), (0.206, -0.55), ha="left")
note(ax1, f"$-{-wl:.2f}$", (l0, wl), (0.218, -1.25), ha="left")
ax1.text(l0 - 0.002, -4.35, r"$\lambda_0 = 0.2$", fontsize=7.5, color=INK, ha="right", va="bottom")
ax1.set_xlim(0.105, 0.235); ax1.set_ylim(-4.5, 0.6)
ax1.set_xlabel(r"rate $\lambda$ (per minute)"); ax1.set_ylabel(r"log-likelihood minus its maximum")
ax1.set_title(r"in the rate $\lambda$")

mu = np.linspace(4.2, 9.6, 600)
ax2.plot(mu, llE(1 / mu) - top, color=BLUE, lw=1.4)
ax2.plot(mu, -0.5 * n / mh ** 2 * (mu - mh) ** 2, color=YELLOW, lw=1.6, ls=DASHES[3])
ax2.axvline(m0, color=GRAY, lw=0.6, ls=DASHES[3])
ax2.axhline(0, color=GRAY, lw=0.6, ls=DASHES[3])
wm = -0.5 * n / mh ** 2 * (m0 - mh) ** 2
ax2.plot([m0], [lr], "o", ms=4.5, color=BLUE, zorder=5)
ax2.plot([m0], [wm], "o", ms=4.5, color=YELLOW, zorder=5)
note(ax2, f"$-{-lr:.2f}$", (m0, lr), (5.35, -2.9), ha="left")
note(ax2, f"$-{-wm:.2f}$", (m0, wm), (4.3, -0.4), ha="left")
ax2.text(m0 + 0.08, -4.35, r"$\mu_0 = 5$", fontsize=7.5, color=INK, ha="left", va="bottom")
ax2.set_xlim(4.2, 9.6)
ax2.set_xlabel(r"mean wait $\mu = 1/\lambda$ (minutes)")
ax2.set_title(r"in the mean wait $\mu$")
save(fig, "fig_wald_parameterization")
print("LR drop", lr, "Wald lambda", wl, "Wald mu", wm, "stats", -2 * lr, -2 * wl, -2 * wm)
