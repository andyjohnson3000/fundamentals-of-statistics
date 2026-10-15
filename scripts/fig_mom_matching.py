"""The method of moments as matching. Left: for the Gaussian family the
moment map sends (mu, sigma^2) to (m1, m2) = (mu, sigma^2 + mu^2). Each
vertical line is a set of parameters sharing an m1; each curve
sigma^2 = m2 - mu^2 shares an m2. The sample moments of the Old Faithful
waits, m1-hat = 70.9 and m2-hat = 5210, pick out one crossing, the estimate
(70.9, 184.1). Right: one parameter, the exponential family, m1 = 1/lambda.
The sample mean 6.23 of the subway gaps is read off the vertical axis and
sent back through the curve to lambda-hat = 0.1605."""
from _style import *

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
mu = np.linspace(40, 100, 600)
m1, s2 = 70.897, 184.144
m2 = s2 + m1 ** 2
for c, lw, ls in [(55, 0.8, DASHES[3]), (m1, 1.5, "-"), (85, 0.8, DASHES[3])]:
    ax1.axvline(c, color=BLUE, lw=lw, ls=ls)
for M2, lw, ls in [(m2 - 1200, 0.8, DASHES[3]), (m2, 1.5, "-"), (m2 + 1200, 0.8, DASHES[3])]:
    v = M2 - mu ** 2
    ax1.plot(mu, v, color=ORANGE, lw=lw, ls=ls)
ax1.plot([m1], [s2], "o", ms=5, color=INK, zorder=5)
ax1.set_xlim(40, 100); ax1.set_ylim(0, 2600)
ax1.set_xlabel(r"$\mu$"); ax1.set_ylabel(r"$\sigma^2$")
ax1.set_title("Gaussian: two moments, two unknowns")
ax1.text(88, 1500, r"$\mu = \hat m_1$" + "\n" + r"$= 70.9$", color=BLUE, fontsize=7.5, va="top")
note(ax1, r"$\sigma^2 + \mu^2$" + "\n" + r"$= \hat m_2$" + "\n" + r"$= 5210$", (66, m2 - 66 ** 2), (41, 150), ha="left", va="bottom")
note(ax1, r"crossing: $(70.9,\ 184.1)$", (m1, s2), (76, 900), ha="left")

lam = np.linspace(0.08, 1.0, 400)
ax2.plot(lam, 1 / lam, color=ORANGE, lw=1.4)
ax2.plot([0, 0.1605], [6.23, 6.23], color=GRAY, lw=0.8, ls=DASHES[1])
ax2.plot([0.1605, 0.1605], [0, 6.23], color=GRAY, lw=0.8, ls=DASHES[1])
ax2.plot([0.1605], [6.23], "o", ms=5, color=INK, zorder=5)
ax2.set_xlim(0, 1.0); ax2.set_ylim(0, 13)
ax2.set_xlabel(r"$\lambda$"); ax2.set_ylabel(r"$m_1(\lambda) = 1/\lambda$")
ax2.set_title("exponential: read the curve backwards")
ax2.text(0.22, 6.6, r"sample mean $6.23$", fontsize=7.5, color=INK, va="bottom")
ax2.text(0.18, 0.4, r"$\hat\lambda = 0.1605$", fontsize=7.5, color=INK, va="bottom")
ax2.text(0.6, 4.0, r"the moment map", color=ORANGE, fontsize=7.5)
save(fig, "fig_mom_matching")
