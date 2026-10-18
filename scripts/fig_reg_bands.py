"""Old Faithful: the least squares line (blue), the 95% confidence band for
the regression line (shaded blue) and the 95% prediction band for a new
wait (orange, dashed), from the t_270 quantile 1.969 and sigma-hat = 5.91."""
from _style import *
from _faithful import faithful, fit
from scipy import stats

x, y = faithful()
a, b, sxx = fit(x, y)
n = len(x)
s = np.sqrt(((y - a - b * x) ** 2).sum() / (n - 2))
q = stats.t.ppf(0.975, n - 2)
t = np.linspace(1.4, 5.3, 200)
m = a + b * t
hc = q * s * np.sqrt(1 / n + (t - x.mean()) ** 2 / sxx)
hp = q * s * np.sqrt(1 + 1 / n + (t - x.mean()) ** 2 / sxx)
fig, ax = plt.subplots(figsize=(4.6, 2.9), layout="constrained")
ax.scatter(x, y, s=6, color=GRAY, alpha=0.45, lw=0)
ax.fill_between(t, m - hc, m + hc, color=BLUE, alpha=0.3, lw=0)
ax.plot(t, m, color=BLUE, lw=1.2)
ax.plot(t, m - hp, color=ORANGE, lw=1.1, ls=DASHES[1])
ax.plot(t, m + hp, color=ORANGE, lw=1.1, ls=DASHES[1])
ax.set_xlim(1.4, 5.3)
ax.set_xlabel("eruption duration (minutes)"); ax.set_ylabel("wait (minutes)")
ax.set_title("confidence band and prediction band")
save(fig, "fig_reg_bands")
for x0 in (2.0, 4.5):
    print(x0, a + b * x0, q * s * np.sqrt(1 / n + (x0 - x.mean()) ** 2 / sxx), q * s * np.sqrt(1 + 1 / n + (x0 - x.mean()) ** 2 / sxx))
