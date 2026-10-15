"""The bias-variance trade-off made concrete, for estimators of a Bernoulli p
with n = 124. Left: at p = 0.645, the (Gaussian-approximated) sampling
distributions of the unbiased p-hat = Rbar_n and of the shrinkage estimator
(n Rbar_n + 10)/(n + 20), which is biased toward 1/2 but less variable; the
shrinkage estimator has the smaller quadratic risk here. Right: quadratic
risk as a function of the true p for four estimators. No estimator wins for
every p, which is why risk is a function and not a number."""
from _style import *

n = 124
p0 = 0.645
pgrid = np.linspace(0.001, 0.999, 500)

def risk_mean(p):      # Rbar_n: unbiased, var p(1-p)/n
    return p * (1 - p) / n
m = 20                 # shrinkage toward 1/2 with the weight of m pseudo-observations
def risk_shrink(p):    # (n Rbar + m/2)/(n+m)
    mean = (n * p + m / 2) / (n + m)
    var = n * p * (1 - p) / (n + m) ** 2
    return var + (mean - p) ** 2
def risk_half(p):      # constant 0.5
    return (p - 0.5) ** 2
def risk_x1(p):        # X_1: unbiased, var p(1-p)
    return p * (1 - p)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

x = np.linspace(0.5, 0.8, 600)
sd_mean = math.sqrt(risk_mean(p0))
m_sh = (n * p0 + m / 2) / (n + m)
sd_sh = math.sqrt(n * p0 * (1 - p0)) / (n + m)
ax1.plot(x, norm_pdf(x, p0, sd_mean), color=BLUE)
ax1.plot(x, norm_pdf(x, m_sh, sd_sh), color=ORANGE, ls=DASHES[1])
ax1.axvline(p0, color=INK, lw=0.9)
# direct labels in empty space (bias and risk numbers are in the caption)
ax1.text(p0 + 0.005, 13.3, r"true $p = 0.645$", fontsize=7.5, color=INK, va="center")
note(ax1, r"$\bar R_n$ (unbiased)", xy=(0.690, norm_pdf(0.690, p0, sd_mean)), xytext=(0.715, 7.2))
note(ax1, "shrinkage (biased)", xy=(0.585, norm_pdf(0.585, m_sh, sd_sh)), xytext=(0.503, 11.3))
ax1.set_xlabel(r"value of the estimator")
ax1.set_ylabel("density")
ax1.set_title(rf"Two estimators at $p = {p0}$, $n = {n}$")
ax1.set_ylim(0, 14)

ax2.plot(pgrid, risk_mean(pgrid), color=BLUE)
ax2.plot(pgrid, risk_shrink(pgrid), color=ORANGE, ls=DASHES[1])
ax2.plot(pgrid, risk_half(pgrid), color=AQUA, ls=DASHES[2])
ax2.plot(pgrid, risk_x1(pgrid), color=YELLOW, ls=DASHES[3])
ax2.set_yscale("log")
ax2.set_ylim(1e-4, 0.4)
# direct labels, each in a gap between curves (the shrinkage formula is in the caption)
note(ax2, r"$\bar R_n$", xy=(0.82, risk_mean(0.82)), xytext=(0.82, 3.2e-4), ha="center")
note(ax2, "shrinkage", xy=(0.86, risk_shrink(0.86)), xytext=(0.86, 9e-3), ha="center")
note(ax2, r"constant $0.5$", xy=(0.37, risk_half(0.37)), xytext=(0.5, 0.045), ha="center")
note(ax2, r"$X_1$", xy=(0.5, risk_x1(0.5)), xytext=(0.5, 0.16), ha="center")
ax2.set_xlabel(r"true $p$")
ax2.set_ylabel("quadratic risk (log scale)")
ax2.set_title(r"Risk depends on the unknown $p$")
save(fig, "fig_bias_variance")
