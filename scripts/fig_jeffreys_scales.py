"""Two priors for the kiss proportion p, drawn on two scales. Left, on p:
the flat prior (blue, solid) and Jeffreys' prior Beta(1/2, 1/2) (orange,
dashed). Right, on the log-odds psi = log(p/(1 - p)): the densities these two
priors induce by the change of variables (same colors), the flat rule applied
to psi directly (gray dotted line, improper, drawn at an arbitrary height),
and Jeffreys' rule applied to psi directly, sqrt(I(psi)) normalized (orange
dots). The flat rule gives two different answers on the two scales; Jeffreys'
rule gives one."""
from _style import *

p = np.linspace(0.0005, 0.9995, 2000)
psi = np.linspace(-7, 7, 1400)
P = 1 / (1 + np.exp(-psi))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

# left: on p
ax1.plot(p, np.ones_like(p), color=BLUE, lw=1.3)
ax1.plot(p, beta_pdf(p, 0.5, 0.5), color=ORANGE, ls=DASHES[1], lw=1.3)
ax1.set_xlim(0, 1); ax1.set_ylim(0, 3.2)
ax1.set_xlabel(r"$p$"); ax1.set_ylabel("density")
ax1.set_title(r"on the probability scale $p$")
note(ax1, "flat", (0.62, 1.0), (0.66, 1.75), ha="left")
note(ax1, r"Jeffreys, Beta$(\frac{1}{2}, \frac{1}{2})$", (0.25, beta_pdf(np.array([0.25]), 0.5, 0.5)[0]), (0.18, 2.55), ha="left")

# right: on the log-odds
flat_img = P * (1 - P)                         # Unif(0, 1) pushed to psi: logistic density
jeff_img = np.sqrt(P * (1 - P)) / np.pi        # Beta(1/2, 1/2) pushed to psi
ax2.plot(psi, flat_img, color=BLUE, lw=1.3)
ax2.plot(psi, jeff_img, color=ORANGE, ls=DASHES[1], lw=1.3)
# Jeffreys' rule computed on psi directly: I(psi) = p(1 - p), so sqrt(I) / normalizer
grid = np.arange(-6, 6.5, 1.0)
Pg = 1 / (1 + np.exp(-grid))
rule = np.sqrt(Pg * (1 - Pg))
rule = rule / np.pi                            # integral of sqrt(p(1-p)) d psi is pi
ax2.plot(grid, rule, "o", color=ORANGE, ms=3.6, mfc="white", mew=1.0)
ax2.axhline(0.22, color=GRAY, lw=1.0, ls=DASHES[3])
ax2.set_xlim(-7, 7); ax2.set_ylim(0, 0.30)
ax2.set_xlabel(r"log-odds $\psi = \log(p/(1-p))$")
ax2.set_title(r"on the log-odds scale $\psi$")
def logistic_pdf(x):
    q = 1 / (1 + np.exp(-x)); return q * (1 - q)


note(ax2, "image of the flat prior", (-1.3, logistic_pdf(-1.3)), (-6.8, 0.27), ha="left")
note(ax2, "image of Jeffreys' prior;\ndots: Jeffreys' rule on " + r"$\psi$", (2.6, np.sqrt((1 / (1 + np.exp(-2.6))) * (1 - 1 / (1 + np.exp(-2.6)))) / np.pi), (3.0, 0.13), ha="left")
note(ax2, r"flat rule on $\psi$ (improper)", (5.5, 0.22), (2.2, 0.245), ha="left", leader=False)
save(fig, "fig_jeffreys_scales")
print("logistic peak", 0.25, "sech peak", 1 / (2 * np.pi))
