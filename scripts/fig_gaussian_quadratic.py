"""Standardizing a Gaussian vector. Left: 2,000 draws of Z = A W, where W has
two independent standard Gaussian coordinates and A is the lower-triangular
matrix with A A^T = Sigma = [[1, 1.2], [1.2, 2.25]] (standard deviations 1
and 1.5, correlation 0.8), with the ellipse z^T Sigma^{-1} z = 5.99, the 95%
quantile of chi-squared with 2 degrees of freedom. Right: the same points
mapped back by A^{-1}, which is W itself, with the circle of radius
sqrt(5.99) = 2.45. A point is outside the ellipse exactly when its image is
outside the circle; the points outside are orange in both."""
from _style import *

g = rng(32)
Sigma = np.array([[1.0, 1.2], [1.2, 2.25]])
A = np.linalg.cholesky(Sigma)
W = g.standard_normal((2000, 2))
Z = W @ A.T
q = -2 * math.log(0.05)          # chi-squared(2) quantile: P(chi2_2 > q) = exp(-q/2)
r2 = np.sum(W ** 2, axis=1)
out = r2 > q
Si = np.linalg.inv(Sigma)
quad = np.einsum("ij,jk,ik->i", Z, Si, Z)
assert np.allclose(quad, r2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.0, 3.05), layout="constrained")
th = np.linspace(0, 2 * math.pi, 400)
circ = np.sqrt(q) * np.column_stack([np.cos(th), np.sin(th)])
ell = circ @ A.T
for ax, P, curve in [(ax1, Z, ell), (ax2, W, circ)]:
    ax.scatter(P[~out, 0], P[~out, 1], s=3, color=BLUE, alpha=0.4, linewidths=0)
    ax.scatter(P[out, 0], P[out, 1], s=5, color=ORANGE, alpha=0.9, linewidths=0)
    ax.plot(curve[:, 0], curve[:, 1], color=INK, lw=1.1)
    ax.set_aspect("equal")
ax1.set_xlim(-4.6, 4.6); ax1.set_ylim(-5.4, 5.4)
ax2.set_xlim(-4.6, 4.6); ax2.set_ylim(-5.4, 5.4)
ax1.set_xlabel(r"$Z_1$"); ax1.set_ylabel(r"$Z_2$")
ax2.set_xlabel(r"$W_1$"); ax2.set_ylabel(r"$W_2$")
ax1.set_title(r"$Z = AW$: correlated")
ax2.set_title(r"$W = A^{-1}Z$: standardized")
ax1.text(4.4, -5.2, f"outside: {out.sum()} of 2,000", fontsize=7.5, color=INK, ha="right", va="bottom")
ax2.text(4.4, -5.2, f"outside: {out.sum()} of 2,000", fontsize=7.5, color=INK, ha="right", va="bottom")
save(fig, "fig_gaussian_quadratic")
print("q", q, "outside", out.sum(), out.mean(), "A", A)
