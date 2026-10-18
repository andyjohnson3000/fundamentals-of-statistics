"""Equal-tailed and highest-density 95% regions for the wind turbine's
standard deviation, under the prior flat in mu times 1/sigma (n = 12,
s = 4.7). Left: the posterior density of sigma, with the highest-density
region [3.08, 7.45] shaded blue and the equal-tailed interval [3.33, 7.98]
between the gray dashed lines. Right: the posterior density of sigma^2, with
its highest-density region [8.5, 53.9] shaded blue, the equal-tailed interval
[11.1, 63.7] (the squares of the left one) between gray dashed lines, and the
squares of the left highest-density endpoints, 9.5 and 55.5, as orange
triangles: squaring the shortest interval for sigma does not give the
shortest interval for sigma^2."""
from _style import *
from math import sqrt

n, s = 12, 4.7
ss = (n - 1) * s * s


def norm(x, f):
    return f / np.sum(0.5 * (f[1:] + f[:-1]) * np.diff(x))


sig = np.linspace(1.5, 12, 4000)
fs = norm(sig, sig ** (-n) * np.exp(-ss / (2 * sig ** 2)))
v = np.linspace(2, 120, 6000)
fv = norm(v, v ** (-(n + 1) / 2) * np.exp(-ss / (2 * v)))

et_s = (3.329, 7.980); hpd_s = (3.084, 7.451)
et_v = (11.09, 63.68); hpd_v = (8.53, 53.93)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
m = (sig >= hpd_s[0]) & (sig <= hpd_s[1])
ax1.fill_between(sig[m], 0, fs[m], color=BLUE, alpha=0.35, lw=0)
ax1.plot(sig, fs, color=INK, lw=1.2)
for e in et_s:
    ax1.axvline(e, color=GRAY, lw=0.9, ls=DASHES[1])
ax1.set_xlim(1.5, 12); ax1.set_ylim(0, 0.42)
ax1.set_xlabel(r"$\sigma$ (miles per hour)"); ax1.set_ylabel("posterior density")
ax1.set_title(r"posterior of $\sigma$")

m = (v >= hpd_v[0]) & (v <= hpd_v[1])
ax2.fill_between(v[m], 0, fv[m], color=BLUE, alpha=0.35, lw=0)
ax2.plot(v, fv, color=INK, lw=1.2)
for e in et_v:
    ax2.axvline(e, color=GRAY, lw=0.9, ls=DASHES[1])
ax2.plot([hpd_s[0] ** 2, hpd_s[1] ** 2], [0.0012, 0.0012], "^", color=ORANGE, ms=6, clip_on=False, zorder=5)
ax2.set_xlim(0, 120); ax2.set_ylim(0, 0.052)
ax2.set_xlabel(r"$\sigma^2$"); ax2.set_title(r"posterior of $\sigma^2$")
save(fig, "fig_jeffreys_hpd")
print("peak sigma", sig[np.argmax(fs)], "peak v", v[np.argmax(fv)], "max fs", fs.max(), "max fv", fv.max())
print("density at hpd ends (sigma):", np.interp(hpd_s, sig, fs), " (v):", np.interp(hpd_v, v, fv))
