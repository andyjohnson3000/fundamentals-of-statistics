"""Old Faithful, the model wait = b0 + b1 duration + b2 (previous wait) +
b3 (previous duration), n = 271. The 95% confidence ellipse (blue) for the
pair (b2, b3) from the Gaussian linear model, its center at the estimates
(-0.283, 3.12) (dot), and the two marginal 95% confidence intervals as a
gray rectangle; the origin (0, 0) is marked with a cross. The ellipse is
tilted because the previous wait and the previous duration have
correlation 0.90."""
from _style import *
from _faithful import faithful
from scipy import stats

x, y = faithful()
Y = y[1:]; X = np.column_stack([np.ones(271), x[1:], y[:-1], x[:-1]])
n, p = X.shape
G = np.linalg.inv(X.T @ X); b = G @ X.T @ Y; r = Y - X @ b; s2 = (r @ r) / (n - p)
C = s2 * G[2:, 2:]; c = b[2:]
q = 2 * stats.f.ppf(0.95, 2, n - p)
w, V = np.linalg.eigh(C)
th = np.linspace(0, 2 * np.pi, 400)
ell = c[:, None] + V @ (np.sqrt(q * w)[:, None] * np.vstack([np.cos(th), np.sin(th)]))
t = stats.t.ppf(0.975, n - p)
fig, ax = plt.subplots(figsize=(3.8, 3.2), layout="constrained")
ax.add_patch(plt.Rectangle((c[0] - t * np.sqrt(C[0, 0]), c[1] - t * np.sqrt(C[1, 1])), 2 * t * np.sqrt(C[0, 0]), 2 * t * np.sqrt(C[1, 1]), color=GRAY, alpha=0.15, lw=0))
ax.plot(ell[0], ell[1], color=BLUE, lw=1.4)
ax.plot(c[0], c[1], "o", color=BLUE, ms=4)
ax.plot(0, 0, "x", color=INK, ms=7, mew=1.2)
ax.set_xlabel("coefficient of the previous wait"); ax.set_ylabel("coefficient of the previous duration")
ax.set_title("joint and separate 95% regions")
save(fig, "fig_mreg_ellipse")
print("b", b, "se", np.sqrt(s2 * np.diag(G)), "corr b2 b3", C[0, 1] / np.sqrt(C[0, 0] * C[1, 1]))
