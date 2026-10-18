"""Jeffreys' prior spreads its mass evenly over what the data can tell apart.
Left: the Beta(1/2, 1/2) density on p (orange) and five bands
p0 +- 1.96 sqrt(p0(1 - p0)/n) for n = 124 and p0 = 0.1, 0.3, 0.5, 0.7, 0.9
(blue shading): narrow near the edges, wide in the middle, each with
Jeffreys mass about 0.11. Right: the same prior and bands on the scale
phi = 2 arcsin(sqrt(p)), where the prior is flat (density 1/pi) and the bands
all have width about 2 x 1.96/sqrt(n) = 0.35."""
from _style import *

n = 124
p = np.linspace(0.0008, 0.9992, 2000)
phi_of = lambda q: 2 * np.arcsin(np.sqrt(q))
centers = [0.1, 0.3, 0.5, 0.7, 0.9]
bands = [(c - 1.96 * math.sqrt(c * (1 - c) / n), c + 1.96 * math.sqrt(c * (1 - c) / n)) for c in centers]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
dens = beta_pdf(p, 0.5, 0.5)
for lo, hi in bands:
    m = (p >= lo) & (p <= hi)
    ax1.fill_between(p[m], 0, dens[m], color=BLUE, alpha=0.35, lw=0)
ax1.plot(p, dens, color=ORANGE, lw=1.3)
ax1.set_xlim(0, 1); ax1.set_ylim(0, 2.6)
ax1.set_xlabel(r"$p$"); ax1.set_ylabel("density")
ax1.set_title(r"Jeffreys' prior on $p$")

phi = np.linspace(0, np.pi, 400)
for lo, hi in bands:
    a, b = phi_of(lo), phi_of(hi)
    ax2.fill_between([a, b], 0, [1 / np.pi, 1 / np.pi], color=BLUE, alpha=0.35, lw=0)
ax2.plot(phi, np.full_like(phi, 1 / np.pi), color=ORANGE, lw=1.3)
ax2.set_xlim(0, np.pi); ax2.set_ylim(0, 2.6 / np.pi * 0.62)
ax2.set_xticks([0, np.pi / 2, np.pi]); ax2.set_xticklabels(["0", r"$\pi/2$", r"$\pi$"])
ax2.set_xlabel(r"$\varphi = 2\arcsin\sqrt{p}$")
ax2.set_title(r"the same prior on $\varphi$: flat")
save(fig, "fig_jeffreys_equal_mass")
for (lo, hi), c in zip(bands, centers):
    from math import asin, sqrt, pi
    mass = (phi_of(hi) - phi_of(lo)) / pi
    print(f"p0 = {c}: band [{lo:.4f}, {hi:.4f}], Jeffreys mass {mass:.4f}, phi-width {phi_of(hi) - phi_of(lo):.4f}")
print("2 x 1.96 / sqrt(n) =", 2 * 1.96 / math.sqrt(n), " mass approx", 3.92 / (math.pi * math.sqrt(n)))
