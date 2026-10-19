"""The stack loss data, 21 days: the stack loss against each predictor
(air flow, cooling water temperature, acid concentration), with the simple
least squares line of the loss on that predictor alone (orange, dashed)."""
from _style import *
from _stackloss import stackloss

X, y = stackloss()
fig, axes = plt.subplots(1, 3, figsize=(6.0, 2.3), sharey=True, layout="constrained")
for ax, j, name in zip(axes, (1, 2, 3), ("air flow", "water temperature", "acid concentration")):
    x = X[:, j]
    ax.scatter(x, y, s=12, color=BLUE)
    b = np.polyfit(x, y, 1); t = np.array([x.min() - 1, x.max() + 1])
    ax.plot(t, np.polyval(b, t), color=ORANGE, lw=1.2, ls=DASHES[1])
    ax.set_xlabel(name); ax.set_title(f"slope {b[0]:.2f}")
axes[0].set_ylabel("stack loss")
save(fig, "fig_mreg_predictors")
