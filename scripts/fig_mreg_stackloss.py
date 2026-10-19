"""The stack loss fit. Left: observed stack loss against the fitted
values of the three-predictor model, with the line y = x (dotted). Right:
the residuals against the fitted values; day 21 is the lowest point."""
from _style import *
from _stackloss import stackloss, lse

X, y = stackloss(); b, r = lse(X, y); yh = X @ b
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FULL, layout="constrained")
ax1.scatter(yh, y, s=14, color=BLUE)
ax1.plot([4, 44], [4, 44], color=INK, lw=0.8, ls=":")
ax1.set_xlabel("fitted stack loss"); ax1.set_ylabel("observed stack loss")
ax1.set_title("observed against fitted")
ax2.scatter(yh, r, s=14, color=BLUE)
ax2.axhline(0, color=INK, lw=0.8, ls=":")
ax2.set_xlabel("fitted stack loss"); ax2.set_ylabel("residual")
ax2.set_title("residuals against fitted")
i = np.argmin(r)
note(ax2, "day 21", (yh[i], r[i]), (yh[i] + 4, r[i] + 0.3))
save(fig, "fig_mreg_stackloss")
print("b", b, "RSS", (r ** 2).sum(), "min resid day", i + 1)
