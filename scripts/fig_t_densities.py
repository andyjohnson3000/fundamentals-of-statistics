"""Student's t. Left: the densities of t_1, t_2, t_5 and t_30 with the
standard Gaussian density (black). Right: the exact probability that
|T| > 1.96 when T has the t distribution with n - 1 degrees of freedom,
against n, with the 5% line (dotted); this is the type 1 error of the
Gaussian 5% rule applied to a Gaussian sample of size n."""
from _style import *
from math import gamma, sqrt, pi

def t_pdf(t, k):
    return gamma((k + 1) / 2) / (sqrt(k * pi) * gamma(k / 2)) * (1 + t ** 2 / k) ** (-(k + 1) / 2)

def t_sf(x, k, grid=400000):
    """P(T > x) for T ~ t_k, by numerical integration of the density on [x, x + 2000] plus the tail
    beyond, approximated analytically for t_1 and by a long grid otherwise."""
    if k == 1:
        return 0.5 - math.atan(x) / pi
    u = np.linspace(x, x + 400.0, grid)
    f = t_pdf(u, k)
    return float(np.sum(0.5 * (f[1:] + f[:-1]) * np.diff(u)))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
t = np.linspace(-4.5, 4.5, 900)
ax1.plot(t, norm_pdf(t), color=INK, lw=1.2)
for k, c, ls in [(1, BLUE, DASHES[0]), (2, ORANGE, DASHES[1]), (5, AQUA, DASHES[2]), (30, YELLOW, DASHES[3])]:
    ax1.plot(t, t_pdf(t, k), color=c, lw=1.3, ls=ls)
ax1.set_xlim(-4.5, 4.5); ax1.set_ylim(0, 0.42)
ax1.set_xlabel(r"$t$"); ax1.set_ylabel("density")
ax1.set_title("Student's $t$ against the Gaussian")
note(ax1, r"$t_{30}$ and Gauss(0, 1)", (0.7, t_pdf(0.7, 30)), (1.6, 0.385), ha="left")
note(ax1, r"$t_5$", (1.2, t_pdf(1.2, 5)), (1.9, 0.31), ha="left")
note(ax1, r"$t_2$", (1.9, t_pdf(1.9, 2)), (2.5, 0.245), ha="left")
note(ax1, r"$t_1$ (Cauchy)", (3.0, t_pdf(3.0, 1)), (2.9, 0.18), ha="left")

ns = np.arange(2, 61)
err = np.array([2 * t_sf(1.96, n - 1) for n in ns])
ax2.plot(ns, err, color=BLUE, lw=1.3)
ax2.axhline(0.05, color=GRAY, lw=0.9, ls=DASHES[3])
ax2.set_xlim(0, 60); ax2.set_ylim(0, 0.32)
ax2.set_xlabel(r"sample size $n$"); ax2.set_ylabel(r"$\Pr(|t_{n-1}| > 1.96)$")
ax2.set_title("type 1 error of the Gaussian 5% rule")
for nn, xt, yt in [(3, 9, 0.27), (5, 14, 0.21), (12, 20, 0.15), (30, 36, 0.10)]:
    i = np.where(ns == nn)[0][0]
    ax2.plot([nn], [err[i]], "o", ms=4, color=INK, zorder=5)
    note(ax2, f"$n = {nn}$: {err[i]:.3f}", (nn, err[i]), (xt, yt), ha="left")
ax2.text(58, 0.066, "5%", color=GRAY, fontsize=7.5, ha="right", va="bottom")
save(fig, "fig_t_densities")
print({n: round(2 * t_sf(1.96, n - 1), 4) for n in [2, 3, 5, 10, 12, 30, 60]})
