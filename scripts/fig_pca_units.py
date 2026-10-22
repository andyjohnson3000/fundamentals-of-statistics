"""The units pitfall on Old Faithful. Left: the raw data (duration in
minutes, waiting in minutes) with the first principal direction, which is
tilted 86 degrees toward the waiting axis because that variable's variance
is 142 times the other's. Right: the same after standardizing each
variable, where the first direction is the 45-degree diagonal."""
from _style import *
from _faithful import faithful

x, y = faithful(); X = np.column_stack([x, y]); n = len(x)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
for ax, D, title, xl, yl in ((ax1, X - X.mean(0), "raw units: the big variance wins", "duration minus its mean (minutes)", "waiting minus its mean (minutes)"),
                             (ax2, (X - X.mean(0)) / X.std(0), "standardized: both count", "duration (standardized)", "waiting (standardized)")):
    S = D.T @ D / n; lam, V = np.linalg.eigh(S); j = lam.argmax(); v = V[:, j]
    if v[1] < 0: v = -v
    ax.plot(D[:, 0], D[:, 1], "o", color=BLUE, ms=2.4, alpha=0.5, mew=0)
    L = 2.2 * np.sqrt(lam[j]); ax.plot([-L * v[0], L * v[0]], [-L * v[1], L * v[1]], color=ORANGE, lw=1.6)
    ax.set_xlabel(xl); ax.set_ylabel(yl); ax.set_title(title, fontsize=9)
ax1.text(4, 22, r"$v_1$ at $86^\circ$", color=ORANGE, fontsize=8); ax2.text(-2.3, 2.2, r"$v_1$ at $45^\circ$", color=ORANGE, fontsize=8)
ax1.set_xlim(-32, 32); ax1.set_ylim(-32, 32); ax1.set_aspect("equal"); ax2.set_aspect("equal")
save(fig, "fig_pca_units")
