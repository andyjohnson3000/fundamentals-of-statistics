"""Two more conjugate pairs. Left: the subway rate lambda (trains per
minute), with the prior Gamma(30, 150) (orange, dashed; mean 0.2, a train
every 5 minutes, worth 30 waits), the likelihood of the 64 waits with mean 6.23 minutes
scaled to a density (gray, dotted) and the posterior Gamma(94, 548.7) (blue).
Right: the wind turbine's mean wind speed mu (mph), with the prior
Gauss(11, 2^2) (orange, dashed), the likelihood of 12 monthly means with
mean 14.3 and sigma = 4.7 taken as known, scaled to a density (gray,
dotted), and the posterior Gauss(13.26, 1.12^2) (blue); the thin gray line
at 10 mph is the threshold of Chapter 14."""
from _style import *

# subway
n, tbar = 64, 6.23
T = n * tbar
a0, b0 = 30.0, 150.0
lam = np.linspace(0.0005, 0.36, 900)
prior = gamma_pdf(lam, a0, b0)
lik = gamma_pdf(lam, n + 1, T)          # lambda^n e^{-lambda T}, normalized
post = gamma_pdf(lam, a0 + n, b0 + T)

# wind turbine
m, xbar, sigma = 12, 14.3, 4.7
mu0, s0 = 11.0, 2.0
prec = 1 / s0 ** 2 + m / sigma ** 2
sn = math.sqrt(1 / prec)
mun = (mu0 / s0 ** 2 + m * xbar / sigma ** 2) / prec
mu = np.linspace(3, 21, 900)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
ax1.plot(lam, prior, color=ORANGE, ls=DASHES[1], lw=1.3)
ax1.plot(lam, lik, color=GRAY, ls=DASHES[3], lw=1.3)
ax1.plot(lam, post, color=BLUE, lw=1.4)
ax1.set_xlim(0, 0.36); ax1.set_ylim(0, 25)
ax1.set_xlabel(r"$\lambda$, trains per minute"); ax1.set_ylabel("density")
ax1.set_title("the subway rate")
note(ax1, "prior", (0.25, gamma_pdf(np.array([0.25]), a0, b0)[0]), (0.27, 9.0), ha="left")
note(ax1, "posterior", (0.19, gamma_pdf(np.array([0.19]), a0 + n, b0 + T)[0]), (0.23, 18.0), ha="left")
note(ax1, "likelihood", (0.14, gamma_pdf(np.array([0.14]), n + 1, T)[0]), (0.02, 16.0), ha="left")

ax2.plot(mu, norm_pdf(mu, mu0, s0), color=ORANGE, ls=DASHES[1], lw=1.3)
ax2.plot(mu, norm_pdf(mu, xbar, sigma / math.sqrt(m)), color=GRAY, ls=DASHES[3], lw=1.3)
ax2.plot(mu, norm_pdf(mu, mun, sn), color=BLUE, lw=1.4)
ax2.axvline(10, color="#9a9a9a", lw=0.7, ls="-")  # solid, so it is not confused with the dotted likelihood
ax2.set_xlim(3, 21); ax2.set_ylim(0, 0.42)
ax2.set_xlabel(r"$\mu$, mean wind speed (mph)")
ax2.set_title("the mean wind speed")
note(ax2, "prior", (8.6, norm_pdf(8.6, mu0, s0)), (4.0, 0.25), ha="left")
note(ax2, "posterior", (12.4, norm_pdf(12.4, mun, sn)), (5.0, 0.37), ha="left")
note(ax2, "likelihood", (16.0, norm_pdf(16.0, xbar, sigma / math.sqrt(m))), (17.2, 0.25), ha="left")
save(fig, "fig_bayes_conjugate")
A, B = a0 + n, b0 + T
print("subway: sum", T, "posterior Gamma", A, B, "mean", A / B, "sd", math.sqrt(A) / B, "MLE", 1 / tbar, "flat-prior mean", (n + 1) / T)
print("wind: posterior mean", mun, "sd", sn, "prior weight", (1 / s0 ** 2) / prec, "pseudo-obs", sigma ** 2 / s0 ** 2,
      "P(mu>10)", 1 - norm_cdf(10, mun, sn), "lik sd", sigma / math.sqrt(m))
