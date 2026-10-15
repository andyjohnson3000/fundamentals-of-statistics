"""Total variation is an area. Left: the densities of Gauss(0, 1) and
Gauss(1, 1). Where the blue density is higher, the region between the curves
has area TV; where the orange is higher, the region has the same area; what
both densities share (gray) has area 1 - TV. TV = 2 Phi(1/2) - 1 = 0.383.
Right: the distributions of the number of couples turning right out of 124
under the two kiss hypotheses, p = 1/2 and p = 0.645. They overlap in very
little (gray), TV = 0.900, and they cross between 71 and 72: the event where
the second is more likely is exactly 'at least 72 turn right'."""
from _style import *

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")

# ---- left: two Gaussians
x = np.linspace(-3.6, 4.6, 900)
f, g = norm_pdf(x, 0, 1), norm_pdf(x, 1, 1)
ax1.fill_between(x, 0, np.minimum(f, g), color=GRAY, alpha=0.22, lw=0)
ax1.fill_between(x, g, f, where=f > g, color=BLUE, alpha=0.35, lw=0)
ax1.fill_between(x, f, g, where=g > f, color=ORANGE, alpha=0.35, lw=0)
ax1.plot(x, f, color=BLUE, lw=1.3)
ax1.plot(x, g, color=ORANGE, lw=1.3, ls=DASHES[1])
tv = float(2 * norm_cdf(0.5) - 1)
note(ax1, rf"blue above orange:" + "\n" + rf"area $= \mathrm{{TV}} = {tv:.3f}$", (-0.9, 0.17), (-3.5, 0.47), ha="left")
note(ax1, rf"orange above blue:" + "\n" + rf"same area, ${tv:.3f}$", (1.9, 0.17), (2.4, 0.47), ha="left")
note(ax1, rf"shared (gray): ${1 - tv:.3f}$", (0.5, 0.12), (2.65, 0.30), ha="left")
ax1.text(-3.5, 0.07, r"$\mathrm{Gauss}(0,1)$", ha="left", fontsize=7.5, color=BLUE)
ax1.text(4.55, 0.07, r"$\mathrm{Gauss}(1,1)$", ha="right", fontsize=7.5, color=ORANGE)
ax1.set_ylim(0, 0.54); ax1.set_xlim(-3.6, 4.6)
ax1.set_yticks([]); ax1.grid(False)
ax1.set_xlabel(r"$x$")
ax1.set_title("Total variation is an area")

# ---- right: the two count distributions in the kiss experiment
n, p1 = 124, 80 / 124
k = np.arange(n + 1)
q0, q1 = binom_pmf(n, 0.5), binom_pmf(n, p1)
sel = (k >= 40) & (k <= 104)
ax2.bar(k[sel], np.minimum(q0, q1)[sel], width=1.0, color=GRAY, alpha=0.35, edgecolor="none")
ax2.step(k[sel], q0[sel], where="mid", color=BLUE, lw=1.2)
ax2.step(k[sel], q1[sel], where="mid", color=ORANGE, lw=1.2, ls=DASHES[1])
ax2.vlines(71.5, 0, 0.087, color=INK, lw=0.7, ls=":")
tv2 = 0.5 * np.abs(q0 - q1).sum()
ax2.text(41, 0.0975, rf"$\mathrm{{TV}} = {tv2:.3f}$; shared mass (gray) ${1 - tv2:.3f}$", fontsize=7.5, color=INK, ha="left", va="top")
ax2.text(72.3, 0.086, "they cross between\n71 and 72", fontsize=7.5, color=INK, ha="left", va="top")
ax2.text(41, 0.025, r"$p = \frac{1}{2}$", fontsize=7.5, color=BLUE, ha="left")
ax2.text(103.5, 0.025, r"$p = 0.645$", fontsize=7.5, color=ORANGE, ha="right")
ax2.set_xlim(40, 104); ax2.set_ylim(0, 0.1)
ax2.set_yticks([])
ax2.set_xlabel("number of couples turning right, out of 124")
ax2.set_title("Two kiss hypotheses, 124 couples")
save(fig, "fig_tv_area")
print("TV gauss", tv, "TV counts", tv2)
