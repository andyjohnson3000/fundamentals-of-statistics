"""Kyphosis against the start vertebra: 81 children, a straight line fitted
by least squares (which leaves (0, 1) at both ends) and the logistic
regression curve 1/(1 + exp(-(0.890 - 0.218 x))). Points are jittered
vertically so that ties show."""
from _style import *
from _kyphosis import kyphosis, logistic_fit

X, y = kyphosis(); start = X[:, 3]
fig, ax = plt.subplots(figsize=(4.6, 2.9), layout="constrained")
r = rng(); jit = (r.uniform(-0.04, 0.04, len(y)))
ax.plot(start[y == 0], y[y == 0] + jit[y == 0], "o", color=BLUE, ms=3.2, alpha=0.7, mew=0)
ax.plot(start[y == 1], y[y == 1] + jit[y == 1], "o", color=ORANGE, ms=3.2, alpha=0.7, mew=0)
Xs = np.column_stack([np.ones(len(y)), start])
a, b = np.linalg.solve(Xs.T @ Xs, Xs.T @ y)
bb, se, ll, hist = logistic_fit(Xs, y)
g = np.linspace(0, 19, 300)
ax.plot(g, a + b * g, color=GRAY, lw=1.0, ls=DASHES[1])
ax.plot(g, 1 / (1 + np.exp(-(bb[0] + bb[1] * g))), color=INK, lw=1.4)
ax.axhline(0, color=GRAY, lw=0.5); ax.axhline(1, color=GRAY, lw=0.5)
ax.set_xlabel("start: first vertebra operated on"); ax.set_ylabel("kyphosis present (1) or absent (0)")
ax.set_ylim(-0.25, 1.15); ax.set_xlim(0, 19)
note(ax, "least squares line", (17.5, a + b * 17.5), (13.5, -0.18), ha="center")
note(ax, "logistic regression", (9.0, 1 / (1 + np.exp(-(bb[0] + bb[1] * 9.0)))), (11.5, 0.55), ha="left")
ax.set_title("a 0/1 response needs a curve that stays in (0, 1)")
print("line", a, b, "logistic", bb, se)
save(fig, "fig_glm_kyphosis")
