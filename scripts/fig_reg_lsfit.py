"""The least squares line for Old Faithful. Left: the data, the line
33.47 + 10.73 x (orange) and each point's residual as a vertical gray
segment; the black dot is (x-bar, y-bar). Right: the residuals against the
duration, with their means over half-minute bins (the last runs from 4.5 to 5.5) (orange); dotted: zero."""
from _style import *
from _faithful import faithful, fit

x, y = faithful()
a, b, sxx = fit(x, y)
res = y - a - b * x
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
for xi, yi in zip(x, y):
    ax1.plot([xi, xi], [yi, a + b * xi], color=GRAY, lw=0.45, alpha=0.7, zorder=1)
ax1.scatter(x, y, s=6, color=BLUE, alpha=0.7, lw=0, zorder=2)
t = np.array([1.4, 5.3])
ax1.plot(t, a + b * t, color=ORANGE, lw=1.4, zorder=3)
ax1.plot([x.mean()], [y.mean()], "o", color=INK, ms=4.5, zorder=4)
ax1.set_xlim(1.4, 5.3)
ax1.set_xlabel("eruption duration (minutes)"); ax1.set_ylabel("wait (minutes)")
ax1.set_title("least squares line and residuals")
ax2.scatter(x, res, s=6, color=BLUE, alpha=0.6, lw=0)
ax2.axhline(0, color=INK, lw=0.8, ls=":")
edges = np.array([1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.5])
cx, cm = [], []
for lo, hi in zip(edges[:-1], edges[1:]):
    m = (x >= lo) & (x < hi)
    if m.sum() >= 5:
        cx.append(x[m].mean()); cm.append(res[m].mean())
ax2.plot(cx, cm, "o-", color=ORANGE, ms=4, lw=1.1, zorder=5)
ax2.set_xlim(1.4, 5.3)
ax2.set_xlabel("eruption duration (minutes)"); ax2.set_ylabel("residual (minutes)")
ax2.set_title("residuals")
save(fig, "fig_reg_lsfit")
print("a b", a, b, "bin residual means", [(c, round(v, 2)) for c, v in zip(cx, cm)])
