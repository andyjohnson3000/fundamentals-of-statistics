"""Why Pearson's statistic has K - 1 degrees of freedom, drawn for K = 3.
2,000 samples of n = 400 from the categorical distribution p0 = (0.5, 0.3,
0.2). Left: the first two estimated proportions (p-hat_1, p-hat_2) of each
sample, with the curve where Pearson's statistic equals 5.99, the 95%
quantile of chi-squared with 2 degrees of freedom; the third proportion is
determined by the first two. Right: the standardized residuals
R_j = sqrt(n) (p-hat_j - p0_j) / sqrt(p0_j) of the same samples, written in
an orthonormal basis of the plane perpendicular to u = (sqrt(p0_1),
sqrt(p0_2), sqrt(p0_3)), where they lie exactly, with the circle of radius
sqrt(5.99) = 2.45. Pearson's statistic is the squared length of R, so a
sample is outside the curve on the left exactly when it is outside the
circle on the right; those samples are orange in both."""
from _style import *

g = rng(17)
p0 = np.array([0.5, 0.3, 0.2])
n, M = 400, 2000
Q2 = 5.991465  # 95% quantile of chi-squared with 2 degrees of freedom
N = g.multinomial(n, p0, M)
ph = N / n
T = (n * (ph - p0) ** 2 / p0).sum(1)
out = T > Q2

# orthonormal basis of the plane perpendicular to u
u = np.sqrt(p0)
v1 = np.array([u[1], -u[0], 0.0]); v1 /= np.linalg.norm(v1)
v2 = np.cross(u, v1); v2 /= np.linalg.norm(v2)
R = np.sqrt(n) * (ph - p0) / np.sqrt(p0)
assert np.allclose(R @ u, 0)
assert np.allclose((R @ v1) ** 2 + (R @ v2) ** 2, T)
c1, c2 = R @ v1, R @ v2

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.0, 3.05), layout="constrained")
ax1.scatter(ph[~out, 0], ph[~out, 1], s=3, color=BLUE, alpha=0.4, linewidths=0)
ax1.scatter(ph[out, 0], ph[out, 1], s=5, color=ORANGE, alpha=0.9, linewidths=0)
a, b = np.meshgrid(np.linspace(0.38, 0.62, 400), np.linspace(0.20, 0.40, 400))
Tg = n * ((a - p0[0]) ** 2 / p0[0] + (b - p0[1]) ** 2 / p0[1] + (1 - a - b - p0[2]) ** 2 / p0[2])
ax1.contour(a, b, Tg, levels=[Q2], colors=[INK], linewidths=1.1)
ax1.plot([p0[0]], [p0[1]], "o", ms=4, color=INK, zorder=5)
ax1.set_xlim(0.38, 0.62); ax1.set_ylim(0.20, 0.40)
ax1.set_xlabel(r"$\hat{p}_1$"); ax1.set_ylabel(r"$\hat{p}_2$")
ax1.set_title("two of the three proportions")
ax1.text(0.615, 0.393, f"outside: {out.sum()} of 2,000", fontsize=7.5, color=INK, ha="right", va="top")

ax2.scatter(c1[~out], c2[~out], s=3, color=BLUE, alpha=0.4, linewidths=0)
ax2.scatter(c1[out], c2[out], s=5, color=ORANGE, alpha=0.9, linewidths=0)
th = np.linspace(0, 2 * math.pi, 400)
ax2.plot(np.sqrt(Q2) * np.cos(th), np.sqrt(Q2) * np.sin(th), color=INK, lw=1.1)
ax2.set_aspect("equal")
ax2.set_xlim(-4.6, 4.6); ax2.set_ylim(-4.6, 4.6)
ax2.set_xlabel("first coordinate in the plane"); ax2.set_ylabel("second coordinate")
ax2.set_title("the residuals in their plane")
ax2.text(4.4, -4.4, f"outside: {out.sum()} of 2,000", fontsize=7.5, color=INK, ha="right", va="bottom")
save(fig, "fig_gof_geometry")
print("outside", out.sum(), out.mean(), "corr of p-hat_1, p-hat_2", np.corrcoef(ph[:, 0], ph[:, 1])[0, 1])
