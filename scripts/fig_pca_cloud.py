"""Old Faithful, both variables standardized: the 272 points, the two
principal directions drawn from the mean with lengths 2 sqrt(lambda_j)
(lambda_1 = 1.90, lambda_2 = 0.10), and five points projected onto the
first direction (gray segments)."""
from _style import *
from _faithful import faithful

x, y = faithful(); X = np.column_stack([x, y]); Z = (X - X.mean(0)) / X.std(0); n = len(x)
S = Z.T @ Z / n; lam, V = np.linalg.eigh(S); idx = lam.argsort()[::-1]; lam = lam[idx]; V = V[:, idx]
if V[0, 0] < 0: V[:, 0] = -V[:, 0]
if V[0, 1] > 0: V[:, 1] = -V[:, 1]
fig, ax = plt.subplots(figsize=(4.2, 4.0), layout="constrained")
ax.plot(Z[:, 0], Z[:, 1], "o", color=BLUE, ms=2.6, alpha=0.55, mew=0)
L1 = 3.2; ax.plot([-L1 * V[0, 0], L1 * V[0, 0]], [-L1 * V[1, 0], L1 * V[1, 0]], color=ORANGE, lw=0.6, alpha=0.6)
for j, col in ((0, ORANGE), (1, AQUA)):
    L = 2 * np.sqrt(lam[j]); ax.annotate("", xy=(L * V[0, j], L * V[1, j]), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=col, lw=1.6))
r = rng(); pick = r.choice(np.where(Z[:, 0] > 0)[0], 5, replace=False)
for i in pick:
    t = Z[i] @ V[:, 0]; ax.plot([Z[i, 0], t * V[0, 0]], [Z[i, 1], t * V[1, 0]], color=GRAY, lw=0.8)
    ax.plot(t * V[0, 0], t * V[1, 0], "o", color=INK, ms=2.6)
ax.text(1.9, 2.55, r"$v_1$, variance $1.90$", color=ORANGE, fontsize=8, ha="left")
ax.text(-2.3, 0.75, r"$v_2$, variance $0.10$", color=AQUA, fontsize=8, ha="left")
ax.set_xlabel("eruption duration (standardized)"); ax.set_ylabel("waiting time (standardized)")
ax.set_xlim(-2.4, 2.9); ax.set_ylim(-2.6, 2.9); ax.set_aspect("equal")
ax.set_title("the two principal directions")
print(lam, V)
save(fig, "fig_pca_cloud")
