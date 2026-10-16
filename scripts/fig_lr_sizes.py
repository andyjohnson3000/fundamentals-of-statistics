"""How good the chi-squared approximation is, for exponential data with
lambda0 = 1. Left: the likelihood ratio statistic 2 n (log(lambda-hat) - 1 +
1/lambda-hat) over 50,000 samples of n = 10 drawn under the null
(histogram), with the chi-squared density with one degree of freedom
(black). Right: the exact type 1 error of the three tests at nominal level
5% against n: Wald in the rate (orange, dashed; for this model it equals the
score test), the likelihood ratio (blue), and Wald in the mean wait 1/lambda
(yellow, dotted). The sum of the n observations is Gamma(n, 1) under the
null, so each type 1 error is an integral against that density."""
from _style import *

Q = 3.841459
g = rng(64)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
n = 10
S = g.gamma(n, 1.0, 50000)
lh = n / S
LR = 2 * n * (np.log(lh) - 1 + 1 / lh)
bins = np.arange(0, 10.25, 0.25)
ax1.hist(LR, bins=bins, density=True, color=BLUE, alpha=0.55, edgecolor="none")
v = np.linspace(0.02, 10, 500)
ax1.plot(v, np.exp(-v / 2) / np.sqrt(2 * math.pi * v), color=INK, lw=1.2)
ax1.axvline(Q, color=GRAY, lw=0.8, ls=DASHES[3])
frac = np.mean(LR > Q)
ax1.set_xlim(0, 10); ax1.set_ylim(0, 1.0)
ax1.set_xlabel(r"likelihood ratio statistic, $n = 10$"); ax1.set_ylabel("density")
ax1.set_title(r"Wilks at $n = 10$")
note(ax1, r"$\chi^2_1$ density", (2.2, np.exp(-1.1) / np.sqrt(2 * math.pi * 2.2)), (4.3, 0.5), ha="left")
note(ax1, f"beyond 3.84: {frac:.3f}", (5.0, 0.03), (5.4, 0.25), ha="left")


def size(stat, n):
    s = np.linspace(1e-6, n + 14 * math.sqrt(n) + 20, 300001)
    dens = gamma_pdf(s, n, 1.0)
    rej = stat(s, n) > Q
    f = dens * rej
    return float(np.sum(0.5 * (f[1:] + f[:-1]) * np.diff(s)))


W_l = lambda s, n: (n - s) ** 2 / n                     # n (lh - 1)^2 / lh^2
LR_s = lambda s, n: 2 * n * (np.log(n / s) - 1 + s / n)
W_m = lambda s, n: n * (1 - n / s) ** 2                  # n (lh - 1)^2 = Wald in the mean
ns = np.arange(3, 81)
sz = {k: np.array([size(f, m) for m in ns]) for k, f in [("Wl", W_l), ("LR", LR_s), ("Wm", W_m)]}
ax2.plot(ns, sz["Wl"], color=ORANGE, lw=1.3, ls=DASHES[1])
ax2.plot(ns, sz["LR"], color=BLUE, lw=1.4)
ax2.plot(ns, sz["Wm"], color=YELLOW, lw=1.6, ls=DASHES[3])
ax2.axhline(0.05, color=GRAY, lw=0.8, ls=DASHES[3])
ax2.set_xlim(0, 80); ax2.set_ylim(0.03, 0.15)
ax2.set_xlabel(r"sample size $n$"); ax2.set_ylabel("exact type 1 error")
ax2.set_title("which test keeps its 5%?")
ax2.text(30, 0.098, r"Wald in $\mu = 1/\lambda$", fontsize=7.5, color=YELLOW_TEXT, ha="left")
ax2.text(12, 0.0565, "likelihood ratio", fontsize=7.5, color=BLUE, ha="left", va="bottom")
ax2.text(42, 0.042, r"Wald in $\lambda$ (= score)", fontsize=7.5, color=ORANGE, ha="left", va="top")
save(fig, "fig_lr_sizes")
for m in [5, 10, 20, 64]:
    i = np.where(ns == m)[0][0]
    print(m, {k: round(v[i], 4) for k, v in sz.items()})
print("sim beyond", frac)
