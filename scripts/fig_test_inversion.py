"""The three statistics as functions of the null value, and the confidence
intervals they invert to. Left: the kiss data (80 of 124). Wald (orange,
dashed) n (p-hat - p0)^2 / (p-hat (1 - p-hat)), likelihood ratio (blue)
2 (l_n(p-hat) - l_n(p0)), score (aqua, dash-dot) n (p-hat - p0)^2 /
(p0 (1 - p0)); the dotted line is 3.84, the 95% quantile of chi-squared with
one degree of freedom, and each 95% interval is the set of p0 where its
curve is below the line (bars underneath). Right: the subway data (n = 64,
mean wait 6.23 minutes) in the rate lambda: Wald in lambda (orange, dashed),
which for this model coincides with the score statistic, likelihood ratio
(blue), Wald in the mean wait mu = 1/lambda (yellow, dotted), and the exact
Gamma interval (black bar). The vertical line marks lambda0 = 0.2."""
from _style import *

Q = 3.841459  # chi-squared(1) 95% quantile


def interval(f, lo, hi, grid=200001):
    x = np.linspace(lo, hi, grid)
    ok = f(x) <= Q
    return x[ok].min(), x[ok].max()


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

# kiss
n, S = 124, 80
ph = S / n
ll = lambda p: S * np.log(p) + (n - S) * np.log(1 - p)
W = lambda p: n * (ph - p) ** 2 / (ph * (1 - ph))
LR = lambda p: 2 * (ll(ph) - ll(p))
SC = lambda p: n * (ph - p) ** 2 / (p * (1 - p))
p = np.linspace(0.47, 0.80, 800)
ax1.plot(p, W(p), color=ORANGE, lw=1.3, ls=DASHES[1])
ax1.plot(p, LR(p), color=BLUE, lw=1.4)
ax1.plot(p, SC(p), color=AQUA, lw=1.3, ls=DASHES[2])
ax1.axhline(Q, color=GRAY, lw=0.8, ls=DASHES[3])
ints = []
for k, (f, c, ls) in enumerate([(W, ORANGE, DASHES[1]), (LR, BLUE, "-"), (SC, AQUA, DASHES[2])]):
    a, b = interval(f, 0.45, 0.85)
    ints.append((a, b))
    y = -1.0 - 0.75 * k
    ax1.plot([a, b], [y, y], color=c, lw=2.0, ls=ls, solid_capstyle="butt")
ax1.axhline(0, color=GRAY, lw=0.5)
ax1.set_xlim(0.47, 0.80); ax1.set_ylim(-3.0, 13.0)
ax1.set_yticks([0, 3.84, 6, 9, 12]); ax1.set_yticklabels(["0", "3.84", "6", "9", "12"])
ax1.set_xlabel(r"null value $p_0$"); ax1.set_ylabel("test statistic")
ax1.set_title("kiss: the three agree")
ax1.text(0.585, 12.4, r"at $p_0 = \frac{1}{2}$:" "\n" "Wald 11.41, LR 10.60" "\n" "score 10.45", fontsize=7.5, color=INK, ha="left", va="top")
ax1.text(0.742, -1.0, "Wald", fontsize=7.5, color=ORANGE, va="center")
ax1.text(0.742, -1.75, "LR", fontsize=7.5, color=BLUE, va="center")
ax1.text(0.742, -2.5, "score", fontsize=7.5, color=AQUA, va="center")

# subway
m, tbar = 64, 6.23
lh = 1 / tbar
llE = lambda l: m * np.log(l) - l * m * tbar
Wl = lambda l: m * (lh - l) ** 2 / lh ** 2
LRs = lambda l: 2 * (llE(lh) - llE(l))
Wmu = lambda l: m * (tbar - 1 / l) ** 2 / tbar ** 2
lam = np.linspace(0.10, 0.26, 800)
ax2.plot(lam, Wl(lam), color=ORANGE, lw=1.3, ls=DASHES[1])
ax2.plot(lam, LRs(lam), color=BLUE, lw=1.4)
ax2.plot(lam, Wmu(lam), color=YELLOW, lw=1.5, ls=DASHES[3])
ax2.axhline(Q, color=GRAY, lw=0.8, ls=DASHES[3])
ax2.axvline(0.2, color=GRAY, lw=0.6, ls=DASHES[3])
ints2 = []
for k, (f, c, ls) in enumerate([(Wl, ORANGE, DASHES[1]), (LRs, BLUE, "-"), (Wmu, YELLOW, DASHES[3])]):
    a, b = interval(f, 0.08, 0.3)
    ints2.append((a, b))
    y = -1.0 - 0.75 * k
    ax2.plot([a, b], [y, y], color=c, lw=2.0, ls=ls, solid_capstyle="butt")
# exact Gamma interval: lambda * n * tbar ~ Gamma(n, 1)
from math import lgamma
def gamma_cdf(x, a, grid=400000):
    t = np.linspace(1e-9, x, grid)
    f = np.exp((a - 1) * np.log(t) - t - lgamma(a))
    return float(np.sum(0.5 * (f[1:] + f[:-1]) * np.diff(t)))
def gamma_ppf(u, a):
    lo, hi = 0.0, 4 * a
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if gamma_cdf(mid, a) < u: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)
ea, eb = gamma_ppf(0.025, m) / (m * tbar), gamma_ppf(0.975, m) / (m * tbar)
ax2.plot([ea, eb], [-3.25, -3.25], color=INK, lw=2.0, solid_capstyle="butt")
ax2.axhline(0, color=GRAY, lw=0.5)
ax2.set_xlim(0.10, 0.26); ax2.set_ylim(-3.9, 13.0)
ax2.set_yticks([0, 3.84, 6, 9, 12]); ax2.set_yticklabels(["0", "3.84", "6", "9", "12"])
ax2.set_xlabel(r"null value $\lambda_0$ (per minute)")
ax2.set_title("subway: they disagree at 0.2")
ax2.text(0.221, -1.0, r"Wald $\lambda$", fontsize=7.5, color=ORANGE, va="center")
ax2.text(0.221, -1.75, "LR", fontsize=7.5, color=BLUE, va="center")
ax2.text(0.221, -2.5, r"Wald $\mu$", fontsize=7.5, color=YELLOW_TEXT, va="center")
ax2.text(0.221, -3.25, "exact", fontsize=7.5, color=INK, va="center")
ax2.text(0.121, 12.4, r"at $\lambda_0 = 0.2$:" "\n" r"Wald $\lambda$ = score 3.87" "\n" "LR 3.34" "\n" r"Wald $\mu$ 2.49", fontsize=7.5, color=INK, ha="left", va="top")
save(fig, "fig_test_inversion")
print("kiss intervals W, LR, S", ints)
print("subway intervals Wl, LR, Wmu", ints2, "exact", (ea, eb))
print("at 0.2", Wl(0.2), LRs(0.2), Wmu(0.2))
