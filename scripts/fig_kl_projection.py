"""Fitting the wrong model: the KL projection of Expo(1) onto the Gaussian
family. Left: the Expo(1) density (gray fill) and three Gaussian candidates.
The best one in KL, Gauss(1, 1), has the same mean and the same variance as
the exponential. Right: KL(Expo(1), Gauss(mu, sigma^2)) =
(1/2) log(2 pi sigma^2) + (1 + (1 - mu)^2) / (2 sigma^2) - 1 over a grid of
(mu, sigma^2), with its minimum 0.419 at (1, 1) and the three candidates
marked. The minimum is not zero: no Gaussian is an exponential. Maximum
likelihood with a Gaussian model fitted to exponential data converges to this
point."""
from _style import *

def kl(mu, s2):
    return 0.5 * np.log(2 * np.pi * s2) + (1 + (1 - mu) ** 2) / (2 * s2) - 1

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
x = np.linspace(-2.2, 5, 900)
ex = np.where(x >= 0, np.exp(-x), 0.0)
ax1.fill_between(x, 0, ex, color=GRAY, alpha=0.22, lw=0)
ax1.plot(x[x >= 0], ex[x >= 0], color=GRAY, lw=1.0)
cands = [(1.0, 1.0, BLUE, "-"), (0.7, 0.6, ORANGE, DASHES[1]), (1.5, 1.5, AQUA, DASHES[2])]
for mu, s2, c, ls in cands:
    ax1.plot(x, norm_pdf(x, mu, np.sqrt(s2)), color=c, lw=1.3, ls=ls)
ax1.set_xlim(-2.2, 5); ax1.set_ylim(0, 1.05)
ax1.set_xlabel(r"$x$"); ax1.set_title("Expo(1) and three Gaussians")
ax1.text(-2.1, 0.75, "Expo(1)", color=GRAY, fontsize=7.5, ha="left", va="center")
note(ax1, "", (0.3, np.exp(-0.3)), (-0.85, 0.75), leader=True)
ax1.text(4.95, 0.98, r"Gauss$(1, 1)$: KL $0.419$", color=BLUE, fontsize=7.5, ha="right", va="top")
ax1.text(4.95, 0.86, r"Gauss$(0.7, 0.6)$: KL $0.572$", color=ORANGE, fontsize=7.5, ha="right", va="top")
ax1.text(4.95, 0.74, r"Gauss$(1.5, 1.5)$: KL $0.538$", color=AQUA, fontsize=7.5, ha="right", va="top")

mu = np.linspace(-0.2, 2.2, 300); s2 = np.linspace(0.25, 3.0, 300)
M, S = np.meshgrid(mu, s2); K = kl(M, S)
levels = [0.45, 0.5, 0.6, 0.75, 1.0, 1.4]
cs = ax2.contour(M, S, K, levels=levels, colors=GRAY, linewidths=0.7)
pos = {}
for d in (np.array([-0.45, 1.0]), np.array([0.8, -0.35])):
    d = d / np.linalg.norm(d)
    tt = np.linspace(0, 3, 3000); ray = np.array([1.0, 1.0])[:, None] + d[:, None] * tt
    kr = kl(ray[0], ray[1])
    for L in levels:
        j = np.argmax(kr >= L)
        if L not in pos and kr[j] >= L and 0.3 < ray[1, j] < 2.95 and -0.15 < ray[0, j] < 2.15:
            pos[L] = (ray[0, j], ray[1, j])
pos = list(pos.values())
ax2.clabel(cs, fmt="%.2f", fontsize=6.5, inline_spacing=2, manual=pos)
for m, v, c, ls in cands:
    ax2.plot(m, v, "o", ms=5 if m == 1 else 4, color=c, mec="white", mew=0.5, zorder=5)
ax2.set_xlabel(r"$\mu$"); ax2.set_ylabel(r"$\sigma^2$")
ax2.set_title(r"KL$(\mathrm{Expo}(1), \mathrm{Gauss}(\mu, \sigma^2))$")
save(fig, "fig_kl_projection")
for m, v, *_ in cands: print(m, v, kl(m, v))
