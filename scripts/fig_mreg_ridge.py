"""Ridge on the stack loss data, with the three predictors standardized
(mean 0, standard deviation 1) and the response centered: the three
coefficients against lambda, from least squares at lambda = 0 (air flow
blue, water temperature orange dashed, acid concentration aqua dash-dot),
with lambda on a logarithmic axis."""
from _style import *
from _stackloss import stackloss

X, y = stackloss()
Z = (X[:, 1:] - X[:, 1:].mean(0)) / X[:, 1:].std(0, ddof=1); yc = y - y.mean()
lams = np.concatenate([[0], np.logspace(-1, 2.5, 200)])
B = np.array([np.linalg.solve(Z.T @ Z + l * np.eye(3), Z.T @ yc) for l in lams])
fig, ax = plt.subplots(figsize=(4.4, 2.9), layout="constrained")
for j, (col, ls, lab) in enumerate(((BLUE, DASHES[0], "air flow"), (ORANGE, DASHES[1], "water temperature"), (AQUA, DASHES[2], "acid concentration"))):
    ax.plot(lams[1:], B[1:, j], color=col, lw=1.4, ls=ls)
    ax.text(0.12, B[1, j] + 0.25, lab, color=INK, fontsize=8, va="bottom")
ax.set_xscale("log"); ax.set_xlim(0.1, 10 ** 2.5)
ax.axhline(0, color=INK, lw=0.7, ls=":")
ax.set_xlabel(r"$\lambda$"); ax.set_ylabel("standardized coefficient")
ax.set_title("ridge shrinks the coefficients")
save(fig, "fig_mreg_ridge")
print(B[0], B[np.searchsorted(lams, 5)], B[np.searchsorted(lams, 20)])
