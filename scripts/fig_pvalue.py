"""The p-value two ways, for the kiss experiment's statistic T_n = 3.23. Left:
the density of T_n under the null (standard Gaussian by the CLT), the
two-sided rejection region |T_n| > 1.96 shaded lightly, and the observed
value; the p-value is the probability, under the null, of a value at least
as extreme as the one observed: the two dark tails beyond +/- 3.23, total
0.0012. Right: the threshold q_{alpha/2} as a function of the level alpha,
with the observed value as a horizontal line. The test rejects at every
level whose threshold is below the line; the smallest such level is where
the curve crosses the line, and that is the p-value."""
from _style import *

t_obs = 3.233
z = np.linspace(-4.2, 4.2, 800)
f = norm_pdf(z)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

ax1.plot(z, f, color=INK, lw=1.2)
ax1.fill_between(z, 0, f, where=np.abs(z) >= 1.96, color=ORANGE, alpha=0.25, lw=0)
ax1.fill_between(z, 0, f, where=np.abs(z) >= t_obs, color=ORANGE, alpha=0.9, lw=0)
for tt in (t_obs, -t_obs):
    ax1.plot([tt, tt], [0, 0.07], color=INK, lw=0.8, ls="--")
pv = 2 * (1 - float(norm_cdf(t_obs)))
ax1.annotate(rf"$p$-value: both tails" + "\n" + rf"beyond $\pm 3.23$:" + "\n" + rf"$2\,(1 - \Phi(3.23)) = {pv:.4f}$",
             (3.45, 0.004), xytext=(1.75, 0.33), fontsize=7.5, color=INK, ha="left", va="center",
             arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6))
ax1.annotate("rejection region" + "\n" + r"at $\alpha = 0.05$:" + "\n" + r"$|T_n| > 1.96$",
             (-2.5, 0.012), xytext=(-4.15, 0.30), fontsize=7.5, color=INK, ha="left", va="center",
             arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6))
ax1.set_xticks([-t_obs, -1.96, 0, 1.96, t_obs])
ax1.set_xticklabels([r"$-3.23$", r"$-1.96$", r"$0$", r"$1.96$", r"$3.23$"], fontsize=7.5)
ax1.set_yticks([])
ax1.set_ylim(0, 0.44)
ax1.grid(False)
ax1.set_xlabel(r"$T_n$ under $H_0$")
ax1.set_title(r"Observed $T_n = 3.23$: how far out is it?")

alphas = np.logspace(-4, math.log10(0.5), 400)


def q(u):
    lo, hi = 0.0, 6.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if norm_cdf(mid) < u:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


qs = np.array([q(1 - a / 2) for a in alphas])
ax2.plot(alphas, qs, color=BLUE, label=r"threshold $q_{\alpha/2}$")
ax2.axhline(t_obs, color=INK, lw=0.8, ls="--")
ax2.fill_between(alphas, 0, 4.2, where=qs <= t_obs, color=BLUE, alpha=0.08, lw=0)
ax2.plot(pv, t_obs, "o", ms=4.5, color=ORANGE, mec="white", mew=0.5, zorder=5)
ax2.set_xscale("log")
ax2.set_xlim(1e-4, 0.5)
ax2.set_ylim(0, 4.2)
ax2.set_xticks([1e-4, 1e-3, 1e-2, 0.05, 0.5])
ax2.set_xticklabels([r"$10^{-4}$", r"$10^{-3}$", r"$10^{-2}$", r"$0.05$", r"$0.5$"], fontsize=7.5)
ax2.text(0.45, t_obs + 0.08, r"observed $T_n = 3.23$", fontsize=7.5, color=INK, ha="right", va="bottom")
ax2.annotate(r"$p$-value $= 0.0012$:" + "\n" + "the smallest $\\alpha$ that rejects", (pv, t_obs), xytext=(2.2e-4, 1.6), fontsize=7.5, color=INK, ha="left",
             arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.6))
ax2.text(0.06, 0.55, "rejects at every\n$\\alpha$ in the shaded range", fontsize=7.5, color=INK, ha="center", va="center")
ax2.set_xlabel(r"level $\alpha$ (log scale)")
ax2.set_ylabel(r"threshold $q_{\alpha/2}$")
ax2.set_title("The smallest level that rejects")
save(fig, "fig_pvalue")
print("p-value", pv)
