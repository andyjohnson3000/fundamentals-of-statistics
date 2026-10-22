"""Stack loss data, four standardized variables (air flow, water
temperature, acid concentration, stack loss). Left: the scree plot, the
eigenvalues 3.00, 0.73, 0.22, 0.05 of the correlation matrix. Right: the
first two scores of the 21 days, labeled by day number."""
from _style import *
from _stackloss import stackloss

X, y = stackloss(); A = np.column_stack([X[:, 1:], y]); Z = (A - A.mean(0)) / A.std(0); n = len(y)
S = Z.T @ Z / n; lam, V = np.linalg.eigh(S); idx = lam.argsort()[::-1]; lam = lam[idx]; V = V[:, idx]
if V[:, 0].sum() < 0: V[:, 0] = -V[:, 0]
if V[2, 1] < 0: V[:, 1] = -V[:, 1]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
k = np.arange(1, 5)
ax1.plot(k, lam, "o-", color=BLUE, lw=1.2, ms=4)
cum = np.cumsum(lam) / lam.sum()
for kk, l, c in zip(k, lam, cum): ax1.text(kk + 0.12, l + 0.1, f"{100 * c:.0f}%", fontsize=7.5, color=INK)
ax1.set_xticks(k); ax1.set_xlabel("component $j$"); ax1.set_ylabel(r"eigenvalue $\lambda_j$"); ax1.set_ylim(0, 3.4)
ax1.set_title("scree plot, with cumulative share")
sc = Z @ V[:, :2]
ax2.plot(sc[:, 0], sc[:, 1], "o", color=BLUE, ms=3.5, mew=0)
off = {19: (0.07, -0.16), 12: (0.07, -0.14), 8: (0.07, -0.14), 5: (0.07, -0.14), 6: (0.07, -0.16)}
for i in range(n):
    dx, dy = off.get(i + 1, (0.07, 0.04)); ax2.text(sc[i, 0] + dx, sc[i, 1] + dy, str(i + 1), fontsize=6.5, color=GRAY)
ax2.axhline(0, color=GRAY, lw=0.5); ax2.axvline(0, color=GRAY, lw=0.5)
ax2.set_xlabel("first score (75% of the variance)"); ax2.set_ylabel("second score (18%)")
ax2.set_title("the 21 days on the first two components")
print(lam, cum); print(V.round(3)); print(sc.round(2))
save(fig, "fig_pca_scree")
