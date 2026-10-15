"""The Gaussian log-likelihood of the boarding data (R2F, n = 72, mean 24.2
minutes, standard deviation 2.1) as a surface over (mu, sigma^2). It depends
on the data only through the mean and the sum of squared deviations. Left:
contours, with the maximum at mu-hat = 24.2, sigma^2-hat = 4.35 (the
divide-by-n variance, below the divide-by-(n - 1) value 4.41); the gradient
is zero there. Right: two slices through the maximum, one in each direction;
both are concave with a flat top at the maximum."""
from _style import *

n, xb, s = 72, 24.2, 2.1
ss = (n - 1) * s ** 2            # sum of squared deviations
def ll(mu, v):
    return -0.5 * n * np.log(2 * np.pi * v) - (ss + n * (xb - mu) ** 2) / (2 * v)
mu = np.linspace(23.2, 25.2, 300); v = np.linspace(2.5, 7.5, 300)
M, V = np.meshgrid(mu, v); Z = ll(M, V)
vh = ss / n; top = ll(xb, vh)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(6.0, 2.5), layout="constrained")
levels = top - np.array([8, 5, 3, 1.5, 0.5])
cs = ax1.contour(M, V, Z, levels=levels, colors=GRAY, linewidths=0.7, linestyles="solid")
pos = []
tt = np.linspace(0, 3, 3000)
for lv in levels:
    mu_r, v_r = xb + 0.3 * tt, vh + 1.0 * tt
    k = np.argmax(ll(mu_r, v_r) <= lv)
    pos.append((mu_r[k], v_r[k]))
ax1.clabel(cs, fmt=lambda z: f"{top - z:.1f}", fontsize=6.5, inline_spacing=2, manual=pos)
ax1.plot([xb], [vh], "o", ms=4, color=ORANGE, zorder=5)
ax1.set_xlabel(r"$\mu$ (minutes)"); ax1.set_ylabel(r"$\sigma^2$")
ax1.set_title(r"$\ell_{\max} - \ell(\mu, \sigma^2)$")
ax1.axhline(vh, color=BLUE, lw=1.0, zorder=4)
ax1.axvline(xb, color=AQUA, lw=1.0, ls=DASHES[2], zorder=4)

ax2.plot(mu, ll(mu, vh) - top, color=BLUE, lw=1.4)
ax2.set_ylim(-14, 1); ax2.set_xlabel(r"$\mu$"); ax2.set_ylabel(r"$\ell - \ell_{\max}$")
ax2.set_title(r"slice at $\sigma^2 = 4.35$")
ax3.plot(v, ll(xb, v) - top, color=AQUA, lw=1.4, ls=DASHES[2])
ax3.set_ylim(-14, 1); ax3.set_xlabel(r"$\sigma^2$")
ax3.set_title(r"slice at $\mu = 24.2$")
save(fig, "fig_gauss_loglik")
print(vh, top)
