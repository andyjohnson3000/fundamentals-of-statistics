"""The function b for the Bernoulli family, b(theta) = log(1 + e^theta),
with tangent lines at theta = -2, 0 and 2 whose slopes are the means
b'(theta) = 0.12, 0.5, 0.88 (orange, dashed); the curvature b'' is the
variance p(1 - p). The dot marks the kiss data's theta-hat = log(80/44)
= 0.598, where the slope is 0.645."""
from _style import *

th = np.linspace(-4, 4, 400)
b = np.log1p(np.exp(th))
fig, ax = plt.subplots(figsize=(4.2, 2.9), layout="constrained")
ax.plot(th, b, color=BLUE, lw=1.5)
for t0 in (-2.0, 0.0, 2.0):
    p = 1 / (1 + np.exp(-t0)); b0 = np.log1p(np.exp(t0))
    s = np.linspace(t0 - 1.3, t0 + 1.3, 2)
    ax.plot(s, b0 + p * (s - t0), color=ORANGE, lw=1.0, ls=DASHES[1])
    if t0 < -1:
        ax.text(t0 - 1.3, b0 - p * 1.3 + 0.2, f"slope {p:.2f}", fontsize=7.5, color=INK, va="bottom", ha="left")
    else:
        ax.text(t0 + 1.4, b0 + p * 1.4 - 0.32, f"slope {p:.2f}", fontsize=7.5, color=INK, va="top", ha="left")
t0 = np.log(80 / 44); ax.plot(t0, np.log1p(np.exp(t0)), "o", color=INK, ms=4)
ax.text(t0 - 0.2, np.log1p(np.exp(t0)) + 0.45, r"$\hat{\theta} = 0.598$", fontsize=8, color=INK, ha="right")
ax.set_xlabel(r"$\theta$ (log-odds)"); ax.set_ylabel(r"$b(\theta)$")
ax.set_ylim(-0.1, 4.3); ax.set_title(r"$b(\theta) = \log(1 + e^\theta)$: slope is the mean")
save(fig, "fig_ef_b")
