"""Left: the logit link log(mu/(1-mu)) and the probit link Phi^{-1}(mu) on
(0, 1). Right: their inverses, the logistic function and the Gaussian CDF,
the curves a Bernoulli mean follows as x^T beta runs over the line; the
probit is drawn with its slope at 0 matched to the logistic's (Phi(x/1.7))
to show how close the two shapes are."""
from _style import *
from scipy.stats import norm

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
m = np.linspace(0.003, 0.997, 400)
ax1.plot(m, np.log(m / (1 - m)), color=BLUE, lw=1.4)
ax1.plot(m, norm.ppf(m), color=ORANGE, lw=1.4, ls=DASHES[1])
ax1.set_ylim(-5, 5); ax1.set_xlabel(r"mean $\mu$"); ax1.set_ylabel(r"$g(\mu)$")
ax1.text(0.72, 3.3, "logit", color=BLUE, fontsize=8); ax1.text(0.84, 0.3, "probit", color=ORANGE, fontsize=8)
ax1.set_title("two links from (0, 1) to the line")
t = np.linspace(-6, 6, 400)
ax2.plot(t, 1 / (1 + np.exp(-t)), color=BLUE, lw=1.4)
ax2.plot(t, norm.cdf(t / 1.7), color=ORANGE, lw=1.4, ls=DASHES[1])
ax2.set_xlabel(r"$x^\top\beta$"); ax2.set_ylabel(r"mean $\mu = g^{-1}(x^\top\beta)$")
ax2.text(2.6, 0.72, "logistic", color=BLUE, fontsize=8, ha="left")
ax2.text(-5.9, 0.32, r"$\Phi(x^\top\beta/1.7)$", color=ORANGE, fontsize=8, ha="left")
ax2.set_title("and back: the mean as a function of the predictor")
save(fig, "fig_glm_links")
