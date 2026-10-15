"""Density, CDF and quantile are one object seen three ways. Top: the density
of Gauss(0, 1); the shaded area between a = -1 and b = 1.5 is P(a <= X <= b).
Bottom: the CDF, whose rise from F(a) to F(b) is that same area, and whose
inverse read sideways gives the quantile: the x at which F reaches 0.95 is
q_0.05 = 1.645."""
from _style import *

a, b = -1.0, 1.0
x = np.linspace(-3.5, 3.5, 700)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5.2, 4.4), sharex=True, layout="constrained")
f = norm_pdf(x); F = norm_cdf(x)
ax1.plot(x, f, color=INK, lw=1.2)
m = (x >= a) & (x <= b)
ax1.fill_between(x[m], 0, f[m], color=BLUE, alpha=0.3, lw=0)
area = float(norm_cdf(b) - norm_cdf(a))
# two lines so the label sits fully inside the shaded region (2 units wide)
ax1.text(0.0, 0.072, rf"area $= \mathbb{{P}}(a \leq X \leq b)$" + "\n" + rf"$= {area:.3f}$",
         ha="center", va="center", fontsize=7.5, color=INK, linespacing=1.3)
ax1.set_ylabel("density"); ax1.set_title("Density: probability is area")
ax2.plot(x, F, color=INK, lw=1.2)
for v, lab in [(a, "a"), (b, "b")]:
    ax2.plot([v, v], [0, float(norm_cdf(v))], color=BLUE, lw=0.7, ls=":")
    ax2.plot([-3.5, v], [float(norm_cdf(v))] * 2, color=BLUE, lw=0.7, ls=":")
    ax2.text(v, -0.08, rf"${lab}$", ha="center", fontsize=8, color=INK)
ax2.annotate("", xy=(-3.2, float(norm_cdf(b))), xytext=(-3.2, float(norm_cdf(a))), arrowprops=dict(arrowstyle="<->", color=BLUE, lw=0.9))
ax2.text(-3.05, 0.5, rf"$F(b) - F(a) = {area:.3f}$", fontsize=8, color=INK, va="center")
q = 1.645
ax2.plot([-3.5, q], [0.95, 0.95], color=ORANGE, lw=0.8, ls="--"); ax2.plot([q, q], [0, 0.95], color=ORANGE, lw=0.8, ls="--")
# below the 0.95 line, in the empty lower-right corner, with a leader to (q, 0.95)
note(ax2, "quantile: read $0.95$ in,\nget $q_{0.05} = 1.645$ out", xy=(q, 0.95), xytext=(q + 0.25, 0.5),
     ha="left", va="center")
ax2.set_ylim(-0.15, 1.08); ax2.set_ylabel(r"$F(x)$"); ax2.set_xlabel(r"$x$")
ax2.set_title("CDF: the same probability is a rise; the quantile reads it backwards")
save(fig, "fig_tk_density_cdf")
