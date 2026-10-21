"""Complete separation: six observations with x = 1, ..., 6 and y = 0 for
x <= 3, y = 1 for x >= 4. Left: the data and three logistic curves
1/(1 + exp(-b(x - 3.5))) with b = 1, 2, 4. Right: the log-likelihood of b
(with the intercept fixed at -3.5 b) rises toward 0 and never peaks."""
from _style import *

x = np.arange(1, 7); y = np.array([0, 0, 0, 1, 1, 1])
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
ax1.plot(x[y == 0], y[y == 0], "o", color=BLUE, ms=4.5); ax1.plot(x[y == 1], y[y == 1], "o", color=ORANGE, ms=4.5)
g = np.linspace(0.5, 6.5, 300)
for b, col, ls in ((1, GRAY, DASHES[1]), (2, AQUA, DASHES[2]), (4, INK, DASHES[0])):
    ax1.plot(g, 1 / (1 + np.exp(-b * (g - 3.5))), color=col, lw=1.1, ls=ls)
ax1.text(1.0, 0.3, "slope 1", color=GRAY, fontsize=7.5); ax1.text(2.75, 0.62, "2", color=AQUA, fontsize=7.5)
ax1.text(3.62, 0.85, "4", color=INK, fontsize=7.5)
ax1.set_xlabel("$x$"); ax1.set_ylabel("$y$"); ax1.set_ylim(-0.1, 1.1); ax1.set_title("the 0s and 1s do not overlap")
b = np.linspace(0, 8, 300)
ll = np.array([(y * (bb * (x - 3.5)) - np.log1p(np.exp(bb * (x - 3.5)))).sum() for bb in b])
ax2.plot(b, ll, color=BLUE, lw=1.4); ax2.axhline(0, color=GRAY, lw=0.6, ls=":")
ax2.set_xlabel("slope $b$"); ax2.set_ylabel("log-likelihood"); ax2.set_ylim(-4.5, 0.4)
ax2.set_title("the log-likelihood never reaches its top")
save(fig, "fig_glm_separation")
